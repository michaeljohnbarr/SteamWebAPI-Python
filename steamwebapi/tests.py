# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
import unittest

# API Imports
from user import ISteamUser

# =============================================================================
# >> GLOBALS
# =============================================================================
VANITY_URL = 'http://steamcommunity.com/id/XE_ManUp/'
PUBLIC_PROFILE = '76561197970309043'
PRIVATE_PROFILE = '76561198061223360'
FRIENDSONLY_PROFILE = '76561198061223360'
VAC_BANNED = '76561197970309043'
COMMUNITY_BANNED = ''
ECONOMY_BANNED = ''

class ISteamUserTest(unittest.TestCase):
    def setUp(self):
        self.iSteamUser = ISteamUser()

    def test_valid_GetFriendList(self):
        self.assertTrue('friendslist' in \
            self.iSteamUser.GetFriendList(PUBLIC_PROFILE).keys(),
            'Error retrieving friends list from a valid public profile.')
    
    def test_friendsonly_GetFriendList(self):
        self.assertEqual(self.iSteamUser.GetFriendList(FRIENDSONLY_PROFILE),
            {}, 'Invalid result received from friends list of a friends ' +
            'only profile.')
    
    def test_private_GetFriendList(self):
        self.assertEqual(self.iSteamUser.GetFriendList(PRIVATE_PROFILE),
            {}, 'Invalid result received from friends list of a private ' +
            'profile.')

    def test_vac_GetPlayerBans(self):
        print self.iSteamUser.GetPlayerBans(VAC_BANNED)
        self.assertEqual(bool(
            self.iSteamUser.GetPlayerBans(VAC_BANNED)[0]['VACBanned']),
            True, 'This player should be VAC banned. Verify the VAC_BANNED id.'
            )
    #def community_GetPlayerBans(self):
    #    pass
    #def trade_GetPlayerBans(self):
    #    pass
    
def suite():
    suite = unittest.TestSuite()
    suite.addTest(ISteamUserTest('valid_GetFriendList'))
    suite.addTest(ISteamUserTest('friendsonly_GetFriendList'))
    suite.addTest(ISteamUserTest('private_GetFriendList'))
        #tests = ['valid_GetFriendList', 'friendsonly_GetFriendList',
        #    'test_private_GetFriendList', 'vac_GetPlayerBans']
        #print tests
        #suite = unittest.TestLoader().loadTestsFromTestCase(ISteamUserTest)
        #return 
    return suite

if __name__ == '__main__':
    try:
        print 'wtf'
        unittest.main()
        print 'wtf2'
    except SystemExit:
        pass
unittest.TestLoader().loadTestsFromTestCase(ISteamUserTest)
