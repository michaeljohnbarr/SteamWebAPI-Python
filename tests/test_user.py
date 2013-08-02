# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
from unittest import TestCase, main

# Third-Party Python Imports
from requests import HTTPError


# =============================================================================
# >> GLOBALS
# =============================================================================
VANITY_URL = 'http://steamcommunity.com/id/XE_ManUp/'
PUBLIC_PROFILE = '76561197970309043'
PRIVATE_PROFILE = '76561198061223360'
FRIENDSONLY_PROFILE = '76561198013559637'
VAC_BANNED = '76561197970309043'
COMMUNITY_BANNED = ''
ECONOMY_BANNED = ''

class ISteamUserTest(TestCase):
    PUBLIC_PROFILE = '76561197970309043'
    PRIVATE_PROFILE = '76561198069962646'
    FRIENDSONLY_PROFILE = '76561198061223360'

    def setUp(self):
        from steamwebapi.user import ISteamUser
        self.iSteamUser = ISteamUser()

    def test_GetFriendList_no_api_key(self):
        """Make sure that APIKeyRequiredError is raised without a Steam Web API
        key.

        """
        from steamwebapi.util.exceptions import APIKeyRequiredError
        with self.assertRaises(APIKeyRequiredError):
            # Modify the ISteamUser() instance with an empty Steam Web API Key
            self.iSteamUser.key = ''
            self.iSteamUser.GetFriendList(
                steamid=ISteamUserTest.PUBLIC_PROFILE
            )
    
    def test_GetFriendList_valid(self):
        """Test to make sure we get a response code of 200 OK from a public
        profile.

        """
        self.assertEqual(
            self.iSteamUser.GetFriendList(
                steamid=ISteamUserTest.PUBLIC_PROFILE
            ).json.status_code,
            200,
            'Error retrieving friends list from a valid public profile.',
        )
    
    def test_GetFriendList_private(self):
        """Test to make sure we get a response code of 401 Unauthorized from a
        public profile.

        """
        self.assertEqual(
            self.iSteamUser.GetFriendList(
                steamid=ISteamUserTest.PRIVATE_PROFILE
            ).json.status_code,
            401,
            'Error retrieving friends list from a valid public profile.',
        )
    
    def test_GetFriendList_friends_only(self):
        """Test to make sure we get a response code of 401 Unauthorized from a
        friends only profile.

        """
        self.assertEqual(
            self.iSteamUser.GetFriendList(
                steamid=ISteamUserTest.FRIENDSONLY_PROFILE
            ).json.status_code,
            200,
            'Error retrieving friends list from a valid friends only profile.',
        )

    def test_GetPlayerBans_no_api_key(self):
        """Make sure that APIKeyRequiredError is raised without a Steam Web API
        key.

        """
        from steamwebapi.util.exceptions import APIKeyRequiredError
        with self.assertRaises(APIKeyRequiredError):
            # Modify the ISteamUser() instance with an empty Steam Web API Key
            self.iSteamUser.key = ''
            self.iSteamUser.GetPlayerBans(
                steamids=ISteamUserTest.PUBLIC_PROFILE
            )

    def test_GetPlayerBans_valid(self):
        """Make sure that APIKeyRequiredError is raised without a Steam Web API
        key.

        """
        self.assertEqual(
            self.iSteamUser.GetPlayerBans(
                    steamids=ISteamUserTest.PUBLIC_PROFILE,
            ).json.status_code,
            200,
            'Error retrieving player bans.',
        )

    #def test_GetPlayerSummaries_no_api_key(self):
    #def test_GetPlayerSummaries_valid(self):
    #def test_GetUserGroupList_no_api_key(self):
    #def test_GetUserGroupList_valid(self):
    #def test_ResolveVanityURL_no_api_key(self):
    #def test_ResolveVanityURL_valid(self):


if __name__ == '__main__':
    main()
