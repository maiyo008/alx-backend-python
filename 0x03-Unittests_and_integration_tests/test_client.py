#!/usr/bin/env python3
"""
Test client
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


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


if __name__ == "__main__":
    unittest.main()
