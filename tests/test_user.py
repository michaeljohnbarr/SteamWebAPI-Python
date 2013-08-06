# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
from unittest import TestCase, main

# Third-Party Python Imports
from requests import HTTPError

# User Imports
from steamwebapi.user import ISteamUser

# Util Imports
from steamwebapi.util.exceptions import APIKeyRequiredError

# =============================================================================
# >> GLOBALS
# =============================================================================
VANITY_URL = 'XE_ManUp'
PUBLIC_PROFILE = '76561197970309043'
PUBLIC_PROFILE_INT = int(PUBLIC_PROFILE)
PRIVATE_PROFILE = '76561198069962646'
FRIENDSONLY_PROFILE = '76561198061223360'

# =============================================================================
# >> ISteamUser Tests
# =============================================================================
class ISteamUserNoAPIKeyTest(TestCase):
    def setUp(self):
        self.iSteamUser = ISteamUser(key='')

    def test_GetFriendList_no_api_key(self):
        """Make sure that APIKeyRequiredError is raised without a Steam Web API
        key.

        """
        with self.assertRaises(APIKeyRequiredError):
            self.iSteamUser.GetFriendList(
                steamid=PUBLIC_PROFILE
            )

    def test_GetPlayerBans_no_api_key(self):
        """Make sure that APIKeyRequiredError is raised without a Steam Web API
        key.

        """
        with self.assertRaises(APIKeyRequiredError):
            self.iSteamUser.GetPlayerBans(
                steamids=[PUBLIC_PROFILE]
            )

    def test_GetPlayerSummaries_no_api_key(self):
        """Make sure that APIKeyRequiredError is raised without a Steam Web API
        key.

        """
        with self.assertRaises(APIKeyRequiredError):
            self.iSteamUser.GetPlayerSummaries(
                steamids=[PUBLIC_PROFILE]
            )

    def test_GetUserGroupList_no_api_key(self):
        """Make sure that APIKeyRequiredError is raised without a Steam Web API
        key.

        """
        with self.assertRaises(APIKeyRequiredError):
            self.iSteamUser.GetUserGroupList(
                steamid=PUBLIC_PROFILE
            )

    def test_ResolveVanityURL_no_api_key(self):
        """Make sure that APIKeyRequiredError is raised without a Steam Web API
        key.

        """
        with self.assertRaises(APIKeyRequiredError):
            self.iSteamUser.ResolveVanityURL(
                vanityURL=VANITY_URL,
            )


class ISteamUserTest(TestCase):
    def setUp(self):
        self.iSteamUser = ISteamUser()
    
    def test_GetFriendList_valid(self):
        """Test to make sure we get a response code of 200 OK from a public
        profile.

        """
        # Retrieve the status code
        status = self.iSteamUser.GetFriendList(
            steamid=PUBLIC_PROFILE
        ).json.status_code

        # Run the test
        self.assertEqual(
            status,
            200,
            'Error retrieving friends list from a valid public profile. ' +
            'Received Status ({0}) instead of Status (401).'.format(status),
        )
    
    def test_GetFriendList_private(self):
        """Test to make sure we get a response code of 401 Unauthorized from a
        public profile.

        """
        # Retrieve the status code
        status = self.iSteamUser.GetFriendList(
            steamid=PRIVATE_PROFILE
        ).json.status_code

        # Run the test
        self.assertEqual(
            status,
            401,
            'Error retrieving friends list from a valid private profile. ' +
            'Received Status ({0}) instead of Status (401).'.format(status),
        )
    
    def test_GetFriendList_friends_only(self):
        """Test to make sure we get a response code of 401 Unauthorized from a
        friends only profile.

        """
        # Retrieve the status code
        status = self.iSteamUser.GetFriendList(
            steamid=FRIENDSONLY_PROFILE
        ).json.status_code

        # Run the test
        self.assertEqual(
            status,
            200,
            'Error retrieving friends list from a valid friends only ' +
            'profile. Received Status ({0}) instead of '.format(status) +
            'Status (200).',
        )

    def test_GetPlayerBans_list_valid(self):
        """Test to make sure we get a response code of 200 OK from a public
        profile.

        """
        # Retrieve the status code
        status = self.iSteamUser.GetPlayerBans(
            steamids=[PUBLIC_PROFILE],
        ).json.status_code

        # Run the test
        self.assertEqual(
            status,
            200,
            'Error retrieving player bans. Received Status ' +
            ' ({0}) instead of Status (200).'.format(status),
        )

    def test_GetPlayerBans_str_valid(self):
        """Test to make sure we get a response code of 200 OK from a public
        profile.

        """
        # Retrieve the status code
        status = self.iSteamUser.GetPlayerBans(
            steamids=PUBLIC_PROFILE,
        ).json.status_code

        # Run the test
        self.assertEqual(
            status,
            200,
            'Error retrieving player bans. Received Status ' +
            ' ({0}) instead of Status (200).'.format(status),
        )

    def test_GetPlayerBans_int_valid(self):
        """Test to make sure we get a response code of 200 OK from a public
        profile.

        """
        # Retrieve the status code
        status = self.iSteamUser.GetPlayerBans(
            steamids=PUBLIC_PROFILE,
        ).json.status_code

        # Run the test
        self.assertEqual(
            status,
            200,
            'Error retrieving player bans. Received Status ' +
            ' ({0}) instead of Status (200).'.format(status),
        )

    def test_GetPlayerBans_multiple_steamids_valid(self):
        """Test to make sure we get a response code of 200 OK from multiple
        public profiles.

        """
        # Retrieve the status code
        status = self.iSteamUser.GetPlayerBans(
            steamids=PUBLIC_PROFILE,
        ).json.status_code

        # Run the test
        self.assertEqual(
            status,
            200,
            'Error retrieving player bans. Received Status ' +
            ' ({0}) instead of Status (200).'.format(status),
        )

    def test_GetPlayerSummaries_list_valid(self):
        """Test to make sure we get a response code of 200 OK from a public
        profile.

        """
        # Retrieve the status code
        status = self.iSteamUser.GetPlayerSummaries(
            steamids=[PUBLIC_PROFILE],
        ).json.status_code

        # Run the test
        self.assertEqual(
            status,
            200,
            'Error retrieving player summary. Received Status ' +
            ' ({0}) instead of Status (200).'.format(status),
        )

    def test_GetPlayerSummaries_str_valid(self):
        """Test to make sure we get a response code of 200 OK from a public
        profile.

        """
        # Retrieve the status code
        status = self.iSteamUser.GetPlayerSummaries(
            steamids=PUBLIC_PROFILE,
        ).json.status_code

        # Run the test
        self.assertEqual(
            status,
            200,
            'Error retrieving player summary. Received Status ' +
            ' ({0}) instead of Status (200).'.format(status),
        )

    def test_GetPlayerSummaries_int_valid(self):
        """Test to make sure we get a response code of 200 OK from a public
        profile.

        """
        # Retrieve the status code
        status = self.iSteamUser.GetPlayerSummaries(
            steamids=PUBLIC_PROFILE_INT,
        ).json.status_code

        # Run the test
        self.assertEqual(
            status,
            200,
            'Error retrieving player summary. Received Status ' +
            ' ({0}) instead of Status (200).'.format(status),
        )

    def test_GetPlayerSummaries_multiple_steamids_valid(self):
        """Test to make sure we get a response code of 200 OK from multiple
        public profiles.

        """
        # Retrieve the status code
        status = self.iSteamUser.GetPlayerSummaries(
            steamids=[PUBLIC_PROFILE, PUBLIC_PROFILE],
        ).json.status_code

        # Run the test
        self.assertEqual(
            status,
            200,
            'Error retrieving player summary. Received Status ' +
            ' ({0}) instead of Status (200).'.format(status),
        )

    def test_GetUserGroupList_valid(self):
        # Retrieve the status code
        status = self.iSteamUser.GetUserGroupList(
            steamid=PUBLIC_PROFILE,
        ).json.status_code

        # Run the test
        self.assertEqual(
            status,
            200,
            'Error retrieving user group list. Received Status ' +
            ' ({0}) instead of Status (200).'.format(status),
        )

    def test_ResolveVanityURL_valid(self):
        # Retrieve the status code
        status = self.iSteamUser.ResolveVanityURL(
            vanityURL=VANITY_URL,
        ).json.status_code

        # Run the test
        self.assertEqual(
            status,
            200,
            'Error retrieving vanity URL. Received Status ' +
            '({0}) instead of Status (200)'.format(status),
        )


if __name__ == '__main__':
    main()
