from __future__ import annotations

import json
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from voice_authority.first_human_bootstrap_client import (
    BEGIN_OPERATION,
    COMPLETE_OPERATION,
    PROTOCOL_VERSION,
    FirstHumanBootstrapClient,
    FirstHumanBootstrapClientError,
    FirstHumanBootstrapDenied,
)


class FirstHumanBootstrapClientTests(unittest.TestCase):
    def setUp(self) -> None:
        self.client = FirstHumanBootstrapClient(
            socket_path=Path("/run/test/bootstrap.sock")
        )

    @staticmethod
    def _socket_with_response(response: dict):
        connection = Mock()
        connection.recv.side_effect = [
            (
                json.dumps(
                    response,
                    separators=(",", ":"),
                    sort_keys=True,
                )
                + "\n"
            ).encode("utf-8")
        ]
        return connection

    def _begin_response(self) -> dict:
        return {
            "status": "pending",
            "authorization_id": "authorization-1",
            "consumption_event_id": "event-1",
            "ceremony_id": "ceremony-1",
            "human_identity_id": "human-1",
            "human_name": "Brad Phee",
            "target_identity_id": "voice-identity",
            "factor_id": "factor-1",
            "allowed_governance_operations": [
                "GRANT_DELEGATED_AUTHORITY",
                "REVOKE_DELEGATED_AUTHORITY",
            ],
            "challenge": {
                "challenge_id": "challenge-1",
                "challenge_secret": "secret-1",
                "ceremony_id": "ceremony-1",
                "human_identity_id": "human-1",
                "factor_id": "factor-1",
                "required_order": "LOW_TO_HIGH",
                "targets": [
                    {
                        "target_id": "target-1",
                        "number": 12,
                    },
                    {
                        "target_id": "target-2",
                        "number": 83,
                    },
                ],
                "expires_at": "2026-09-21T18:00:00+00:00",
            },
        }

    def _complete_response(self) -> dict:
        return {
            "status": "established",
            "ceremony_id": "ceremony-1",
            "human_identity_id": "human-1",
            "target_identity_id": "voice-identity",
            "factor_id": "factor-1",
            "challenge_id": "challenge-1",
            "governance_relationship_id": "governance-1",
            "allowed_governance_operations": [
                "GRANT_DELEGATED_AUTHORITY",
                "REVOKE_DELEGATED_AUTHORITY",
            ],
        }

    @patch("voice_authority.first_human_bootstrap_client.socket.socket")
    def test_begin_sends_exact_finite_protocol(self, socket_factory):
        connection = self._socket_with_response(
            self._begin_response()
        )
        socket_factory.return_value = connection

        response = self.client.begin(
            human_name="Brad Phee",
            target_identity_id="voice-identity",
            allowed_governance_operations=[
                "GRANT_DELEGATED_AUTHORITY",
                "REVOKE_DELEGATED_AUTHORITY",
            ],
        )

        self.assertEqual(response["status"], "pending")

        sent = connection.sendall.call_args.args[0]
        request = json.loads(sent.decode("utf-8"))

        self.assertEqual(
            request,
            {
                "version": PROTOCOL_VERSION,
                "operation": BEGIN_OPERATION,
                "human_name": "Brad Phee",
                "target_identity_id": "voice-identity",
                "allowed_governance_operations": [
                    "GRANT_DELEGATED_AUTHORITY",
                    "REVOKE_DELEGATED_AUTHORITY",
                ],
            },
        )

        connection.connect.assert_called_once_with(
            "/run/test/bootstrap.sock"
        )
        connection.close.assert_called_once()

    @patch("voice_authority.first_human_bootstrap_client.socket.socket")
    def test_complete_sends_exact_possession_submission(
        self,
        socket_factory,
    ):
        connection = self._socket_with_response(
            self._complete_response()
        )
        socket_factory.return_value = connection

        response = self.client.complete(
            ceremony_id="ceremony-1",
            human_identity_id="human-1",
            target_identity_id="voice-identity",
            factor_id="factor-1",
            challenge_id="challenge-1",
            challenge_secret="secret-1",
            selected_target_ids=[
                "target-1",
                "target-2",
            ],
            allowed_governance_operations=[
                "GRANT_DELEGATED_AUTHORITY",
                "REVOKE_DELEGATED_AUTHORITY",
            ],
        )

        self.assertEqual(
            response["governance_relationship_id"],
            "governance-1",
        )

        sent = connection.sendall.call_args.args[0]
        request = json.loads(sent.decode("utf-8"))

        self.assertEqual(
            request["operation"],
            COMPLETE_OPERATION,
        )
        self.assertEqual(
            request["selected_target_ids"],
            ["target-1", "target-2"],
        )
        self.assertEqual(
            request["challenge_secret"],
            "secret-1",
        )

    @patch("voice_authority.first_human_bootstrap_client.socket.socket")
    def test_ucii_denial_never_becomes_success(
        self,
        socket_factory,
    ):
        connection = self._socket_with_response(
            {
                "status": "denied",
                "reason": "bootstrap authorization already consumed",
            }
        )
        socket_factory.return_value = connection

        with self.assertRaisesRegex(
            FirstHumanBootstrapDenied,
            "already consumed",
        ):
            self.client.begin(
                human_name="Brad Phee",
                target_identity_id="voice-identity",
                allowed_governance_operations=[
                    "GRANT_DELEGATED_AUTHORITY",
                ],
            )

    @patch("voice_authority.first_human_bootstrap_client.socket.socket")
    def test_unknown_status_fails_closed(self, socket_factory):
        connection = self._socket_with_response(
            {"status": "authorized"}
        )
        socket_factory.return_value = connection

        with self.assertRaisesRegex(
            FirstHumanBootstrapClientError,
            "unknown status",
        ):
            self.client.begin(
                human_name="Brad Phee",
                target_identity_id="voice-identity",
                allowed_governance_operations=[
                    "GRANT_DELEGATED_AUTHORITY",
                ],
            )

    @patch("voice_authority.first_human_bootstrap_client.socket.socket")
    def test_incomplete_begin_response_fails_closed(
        self,
        socket_factory,
    ):
        connection = self._socket_with_response(
            {"status": "pending"}
        )
        socket_factory.return_value = connection

        with self.assertRaisesRegex(
            FirstHumanBootstrapClientError,
            "incomplete begin-bootstrap response",
        ):
            self.client.begin(
                human_name="Brad Phee",
                target_identity_id="voice-identity",
                allowed_governance_operations=[
                    "GRANT_DELEGATED_AUTHORITY",
                ],
            )

    @patch("voice_authority.first_human_bootstrap_client.socket.socket")
    def test_oversized_response_fails_closed(self, socket_factory):
        connection = Mock()
        connection.recv.return_value = b"x" * 9
        socket_factory.return_value = connection

        client = FirstHumanBootstrapClient(
            socket_path="/run/test/bootstrap.sock",
            max_response_bytes=8,
        )

        with self.assertRaisesRegex(
            FirstHumanBootstrapClientError,
            "response exceeded size limit",
        ):
            client.begin(
                human_name="Brad Phee",
                target_identity_id="voice-identity",
                allowed_governance_operations=[
                    "GRANT_DELEGATED_AUTHORITY",
                ],
            )

        connection.close.assert_called_once()

    def test_duplicate_selected_targets_rejected_before_ipc(self):
        with self.assertRaisesRegex(
            ValueError,
            "selected_target_ids must not contain duplicates",
        ):
            self.client.complete(
                ceremony_id="ceremony-1",
                human_identity_id="human-1",
                target_identity_id="voice-identity",
                factor_id="factor-1",
                challenge_id="challenge-1",
                challenge_secret="secret-1",
                selected_target_ids=[
                    "target-1",
                    "target-1",
                ],
                allowed_governance_operations=[
                    "GRANT_DELEGATED_AUTHORITY",
                ],
            )

    def test_wildcard_governance_operation_rejected_before_ipc(self):
        with self.assertRaisesRegex(
            ValueError,
            "must not be wildcard",
        ):
            self.client.begin(
                human_name="Brad Phee",
                target_identity_id="voice-identity",
                allowed_governance_operations=["*"],
            )

    @patch("voice_authority.first_human_bootstrap_client.socket.socket")
    def test_begin_rejects_empty_ucii_ceremony_id(
        self,
        socket_factory,
    ):
        response = self._begin_response()
        response["ceremony_id"] = ""

        connection = self._socket_with_response(response)
        socket_factory.return_value = connection

        with self.assertRaisesRegex(
            FirstHumanBootstrapClientError,
            "invalid begin-bootstrap ceremony",
        ):
            self.client.begin(
                human_name="Brad Phee",
                target_identity_id="voice-identity",
                allowed_governance_operations=[
                    "GRANT_DELEGATED_AUTHORITY",
                    "REVOKE_DELEGATED_AUTHORITY",
                ],
            )

    @patch("voice_authority.first_human_bootstrap_client.socket.socket")
    def test_begin_rejects_mismatched_challenge_binding(
        self,
        socket_factory,
    ):
        response = self._begin_response()
        response["challenge"]["factor_id"] = "different-factor"

        connection = self._socket_with_response(response)
        socket_factory.return_value = connection

        with self.assertRaisesRegex(
            FirstHumanBootstrapClientError,
            "mismatched bootstrap challenge",
        ):
            self.client.begin(
                human_name="Brad Phee",
                target_identity_id="voice-identity",
                allowed_governance_operations=[
                    "GRANT_DELEGATED_AUTHORITY",
                    "REVOKE_DELEGATED_AUTHORITY",
                ],
            )

    @patch("voice_authority.first_human_bootstrap_client.socket.socket")
    def test_complete_rejects_mismatched_governance_result(
        self,
        socket_factory,
    ):
        response = self._complete_response()
        response["target_identity_id"] = "different-target"

        connection = self._socket_with_response(response)
        socket_factory.return_value = connection

        with self.assertRaisesRegex(
            FirstHumanBootstrapClientError,
            "mismatched completion response",
        ):
            self.client.complete(
                ceremony_id="ceremony-1",
                human_identity_id="human-1",
                target_identity_id="voice-identity",
                factor_id="factor-1",
                challenge_id="challenge-1",
                challenge_secret="secret-1",
                selected_target_ids=[
                    "target-1",
                    "target-2",
                ],
                allowed_governance_operations=[
                    "GRANT_DELEGATED_AUTHORITY",
                    "REVOKE_DELEGATED_AUTHORITY",
                ],
            )

    @patch("voice_authority.first_human_bootstrap_client.socket.socket")
    def test_complete_requires_governance_relationship_id(
        self,
        socket_factory,
    ):
        response = self._complete_response()
        response["governance_relationship_id"] = ""

        connection = self._socket_with_response(response)
        socket_factory.return_value = connection

        with self.assertRaisesRegex(
            FirstHumanBootstrapClientError,
            "invalid governance relationship",
        ):
            self.client.complete(
                ceremony_id="ceremony-1",
                human_identity_id="human-1",
                target_identity_id="voice-identity",
                factor_id="factor-1",
                challenge_id="challenge-1",
                challenge_secret="secret-1",
                selected_target_ids=[
                    "target-1",
                    "target-2",
                ],
                allowed_governance_operations=[
                    "GRANT_DELEGATED_AUTHORITY",
                    "REVOKE_DELEGATED_AUTHORITY",
                ],
            )


if __name__ == "__main__":
    unittest.main()
