#!/usr/bin/env python3
"""
Test client
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        expected_result = {
            "login": org_name,
            "repos_url": f"https://api.github.com/orgs/{org_name}/repos"
        }
        mock_get_json.return_value = expected_result
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=org_name)
        )
        self.assertEqual(result, expected_result)

    @patch('client.get_json')
    def test_public_repos_url(self, mock_get_json):
        # Set the return value for the mock get_json function
        org_name = "google"
        expected_org_payload = {
            "login": org_name,
            "repos_url": f"https://api.github.com/orgs/{org_name}/repos"
        }
        mock_get_json.return_value = expected_org_payload
        client = GithubOrgClient(org_name)
        result = client._public_repos_url
        mock_get_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=org_name)
        )
        expected_url = expected_org_payload["repos_url"]
        self.assertEqual(result, expected_url)

    @patch('client.get_json')
    @patch(
        'client.GithubOrgClient._public_repos_url',
        new_callable=PropertyMock
    )
    def test_public_repos(self, mock_repos_url, mock_get_json):
        org_name = "google"
        expected_repos_url = f"https://api.github.com/orgs/{org_name}/repos"
        mock_repos_url.return_value = expected_repos_url
        expected_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}}
        ]
        mock_get_json.return_value = expected_payload
        client = GithubOrgClient(org_name)
        repos = client.public_repos(license="mit")
        mock_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(expected_repos_url)
        expected_repos = ["repo1"]
        self.assertEqual(repos, expected_repos)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        client = GithubOrgClient("dummy_org")
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    tests for the `GithubOrgClient` class.
    """
    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = [
            cls.org_payload,
            cls.repos_payload,
        ]

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
