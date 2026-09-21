from __future__ import annotations

import os
import unittest
from unittest.mock import Mock, patch

from fastapi.testclient import TestClient

from voice_authority.first_human_bootstrap_client import (
    FirstHumanBootstrapClientError,
    FirstHumanBootstrapDenied,
)
from voice_authority.main import app


SOCKET_ENV = "UCII_FIRST_HUMAN_BOOTSTRAP_SOCKET"


class FirstHumanBootstrapHttpTests(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def tearDown(self) -> None:
        os.environ.pop(SOCKET_ENV, None)

    def test_begin_fails_closed_when_socket_not_configured(self):
        response = self.client.post(
            "/human-bootstrap/begin",
            json={
                "ceremony_id": "ceremony-1",
                "human_name": "Brad Phee",
                "target_identity_id": "voice-identity",
                "allowed_governance_operations": [
                    "GRANT_DELEGATED_AUTHORITY",
                ],
            },
        )

        self.assertEqual(response.status_code, 503)
        self.assertEqual(
            response.json(),
            {
                "detail":
                    "Protected UCII bootstrap is not configured."
            },
        )

    @patch("voice_authority.main.FirstHumanBootstrapClient")
    def test_begin_relays_exact_request(self, client_class):
        os.environ[SOCKET_ENV] = "/run/test/bootstrap.sock"

        protected_client = Mock()
        protected_client.begin.return_value = {
            "status": "pending",
            "ceremony_id": "ceremony-1",
        }
        client_class.return_value = protected_client

        response = self.client.post(
            "/human-bootstrap/begin",
            json={
                "ceremony_id": "ceremony-1",
                "human_name": "Brad Phee",
                "target_identity_id": "voice-identity",
                "allowed_governance_operations": [
                    "GRANT_DELEGATED_AUTHORITY",
                    "REVOKE_DELEGATED_AUTHORITY",
                ],
            },
        )

        self.assertEqual(response.status_code, 200)

        client_class.assert_called_once_with(
            socket_path="/run/test/bootstrap.sock"
        )
        protected_client.begin.assert_called_once_with(
            ceremony_id="ceremony-1",
            human_name="Brad Phee",
            target_identity_id="voice-identity",
            allowed_governance_operations=[
                "GRANT_DELEGATED_AUTHORITY",
                "REVOKE_DELEGATED_AUTHORITY",
            ],
        )

    @patch("voice_authority.main.FirstHumanBootstrapClient")
    def test_complete_relays_exact_possession_submission(
        self,
        client_class,
    ):
        os.environ[SOCKET_ENV] = "/run/test/bootstrap.sock"

        protected_client = Mock()
        protected_client.complete.return_value = {
            "status": "established",
            "governance_relationship_id": "governance-1",
        }
        client_class.return_value = protected_client

        response = self.client.post(
            "/human-bootstrap/complete",
            json={
                "ceremony_id": "ceremony-1",
                "human_identity_id": "human-1",
                "target_identity_id": "voice-identity",
                "factor_id": "factor-1",
                "challenge_id": "challenge-1",
                "challenge_secret": "secret-1",
                "selected_target_ids": [
                    "target-1",
                    "target-2",
                ],
                "allowed_governance_operations": [
                    "GRANT_DELEGATED_AUTHORITY",
                    "REVOKE_DELEGATED_AUTHORITY",
                ],
            },
        )

        self.assertEqual(response.status_code, 200)

        protected_client.complete.assert_called_once_with(
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

    @patch("voice_authority.main.FirstHumanBootstrapClient")
    def test_ucii_denial_maps_to_403(self, client_class):
        os.environ[SOCKET_ENV] = "/run/test/bootstrap.sock"

        protected_client = Mock()
        protected_client.begin.side_effect = (
            FirstHumanBootstrapDenied(
                "bootstrap authorization already consumed"
            )
        )
        client_class.return_value = protected_client

        response = self.client.post(
            "/human-bootstrap/begin",
            json={
                "ceremony_id": "ceremony-1",
                "human_name": "Brad Phee",
                "target_identity_id": "voice-identity",
                "allowed_governance_operations": [
                    "GRANT_DELEGATED_AUTHORITY",
                ],
            },
        )

        self.assertEqual(response.status_code, 403)
        self.assertEqual(
            response.json(),
            {
                "detail":
                    "bootstrap authorization already consumed"
            },
        )

    @patch("voice_authority.main.FirstHumanBootstrapClient")
    def test_transport_failure_maps_to_502(self, client_class):
        os.environ[SOCKET_ENV] = "/run/test/bootstrap.sock"

        protected_client = Mock()
        protected_client.complete.side_effect = (
            FirstHumanBootstrapClientError(
                "protected UCII bootstrap service is unavailable"
            )
        )
        client_class.return_value = protected_client

        response = self.client.post(
            "/human-bootstrap/complete",
            json={
                "ceremony_id": "ceremony-1",
                "human_identity_id": "human-1",
                "target_identity_id": "voice-identity",
                "factor_id": "factor-1",
                "challenge_id": "challenge-1",
                "challenge_secret": "secret-1",
                "selected_target_ids": [
                    "target-1",
                ],
                "allowed_governance_operations": [
                    "GRANT_DELEGATED_AUTHORITY",
                ],
            },
        )

        self.assertEqual(response.status_code, 502)
        self.assertEqual(
            response.json(),
            {
                "detail":
                    "Protected UCII bootstrap request failed."
            },
        )


if __name__ == "__main__":
    unittest.main()
