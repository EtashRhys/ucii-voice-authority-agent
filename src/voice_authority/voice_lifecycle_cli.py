"""Protected Voice-only UCII lifecycle demo command.

Run using the UCII virtual environment and UCII source path.
Operator authorization must be independently prepared and is never
created by this command.
"""

import argparse
import os
import sys
from pathlib import Path

VOICE_IDENTITY_ID = "9df0ff8a-25d0-4340-be32-05e8263f1277"

VOICE_SOCKET = Path(
    "/run/ucii-voice-controller-lifecycle/lifecycle.sock"
)
AUTHORIZATION_PATH = Path(
    "/etc/ucii-voice-authority/lifecycle-authorization.json"
)
PROVENANCE_PATH = Path(
    "/var/lib/ucii/voice-controller-lifecycle-provenance.jsonl"
)

SUPPORTED_OPERATIONS = ("compute.inspect", "compute.purchase")


def grant(operation: str, granted_by: str) -> None:
    from ucii_agents.controller_lifecycle_authorization import (
        load_controller_lifecycle_grant_authorization,
    )
    from ucii_agents.controller_lifecycle_authorization_consumption import (
        consume_controller_lifecycle_grant_authorization,
    )
    from ucii_agents.controller_lifecycle_client import (
        ProtectedControllerLifecycleClient,
    )
    from ucii_agents.provenance_recorder import ProvenanceRecorder

    authorization = load_controller_lifecycle_grant_authorization(
        path=AUTHORIZATION_PATH
    )

    permit = consume_controller_lifecycle_grant_authorization(
        recorder=ProvenanceRecorder(PROVENANCE_PATH),
        authorization=authorization,
        identity_id=VOICE_IDENTITY_ID,
        allowed_operations=[operation],
        granted_by=granted_by,
    )

    result = ProtectedControllerLifecycleClient(
        socket_path=VOICE_SOCKET
    ).grant_delegated_authority(
        allowed_operations=list(permit.allowed_operations),
        granted_by=permit.granted_by,
    )

    if (
        result.identity_id != VOICE_IDENTITY_ID
        or result.authority_state != "ACTIVE"
        or tuple(result.allowed_operations) != permit.allowed_operations
        or result.granted_by != permit.granted_by
    ):
        raise RuntimeError("Protected Voice grant verification failed")

    print("RESULT: GRANTED")
    print("AUTHORITY_ID:", result.authority_id)
    print("IDENTITY_ID:", result.identity_id)
    print("OPERATIONS:", list(result.allowed_operations))


def revoke(authority_id: str, reason: str) -> None:
    # Match the production database used by the protected lifecycle service.
    # Load this before importing UCII database configuration.
    environment_path = Path("/etc/ucii/ucii.env")
    database_url = None

    for line in environment_path.read_text().splitlines():
        line = line.strip()
        if line.startswith("DATABASE_URL="):
            database_url = line.split("=", 1)[1].strip().strip(
                chr(34) + chr(39)
            )
            break

    if not database_url:
        raise RuntimeError("Production UCII database is not configured")

    os.environ["DATABASE_URL"] = database_url

    from pq_auth.authorization.models import ActionAuthority
    from pq_auth.config import SessionLocal
    from ucii_agents.controller_lifecycle_authorization import (
        load_controller_lifecycle_authorization,
    )
    from ucii_agents.controller_lifecycle_authorization_consumption import (
        consume_controller_lifecycle_authorization,
    )
    from ucii_agents.controller_lifecycle_client import (
        ProtectedControllerLifecycleClient,
    )
    from ucii_agents.provenance_recorder import ProvenanceRecorder

    db = SessionLocal()
    try:
        authority = (
            db.query(ActionAuthority)
            .filter(ActionAuthority.id == authority_id)
            .first()
        )
        if (
            authority is None
            or authority.subject_identity_id != VOICE_IDENTITY_ID
        ):
            raise ValueError("Voice authority record not found")
    finally:
        db.close()

    authorization = load_controller_lifecycle_authorization(
        path=AUTHORIZATION_PATH
    )

    permit = consume_controller_lifecycle_authorization(
        recorder=ProvenanceRecorder(PROVENANCE_PATH),
        authorization=authorization,
        identity_id=VOICE_IDENTITY_ID,
        authority_id=authority_id,
        reason=reason,
    )

    result = ProtectedControllerLifecycleClient(
        socket_path=VOICE_SOCKET
    ).revoke_delegated_authority(
        authority_id=permit.authority_id,
        reason=permit.reason,
    )

    if (
        result.authority_id != authority_id
        or result.identity_id != VOICE_IDENTITY_ID
        or result.authority_state != "REVOKED"
    ):
        raise RuntimeError("Protected Voice revocation verification failed")

    print("RESULT: REVOKED")
    print("AUTHORITY_ID:", result.authority_id)
    print("IDENTITY_ID:", result.identity_id)


def main() -> None:
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command", required=True)

    grant_parser = commands.add_parser("grant")
    grant_parser.add_argument(
        "--operation", choices=SUPPORTED_OPERATIONS, required=True
    )
    grant_parser.add_argument("--granted-by", required=True)

    revoke_parser = commands.add_parser("revoke")
    revoke_parser.add_argument("--authority-id", required=True)
    revoke_parser.add_argument("--reason", required=True)

    args = parser.parse_args()

    if os.geteuid() != 0:
        parser.error("Root operator access required")

    if args.command == "grant":
        grant(args.operation, args.granted_by)
    else:
        revoke(args.authority_id, args.reason)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(
            f"VOICE LIFECYCLE FAILED: {type(exc).__name__}: {exc}",
            file=sys.stderr,
        )
        sys.exit(1)
