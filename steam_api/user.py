# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
from urllib2 import HTTPError

# API Imports
from api_base import SteamWebAPI


# =============================================================================
# >> CLASSES
# =============================================================================
class ISteamUser(SteamWebAPI):
    def __init__(self):
        self.interface = 'ISteamUser'
        super(ISteamUser, self).__init__()

    def GetFriendList(self, steamid, relationship='all'):
        """Retrieves a dictionary of 
        """
        params = {
            'steamid': steamid,
            'relationship': relationship
        }
        # According to http://wiki.teamfortress.com/wiki/WebAPI/GetFriendList,
        #   "If the profile is not public or there are no available entries for
        #   the given relationship only an empty object will be returned."
        #   However, this is not the case. It gives a 401 Unauthorized
        #   HTTPError. Thus, we must create this workaround.
        try:
            return self.generate_api_url(self.interface, 'GetFriendList', 1,
                params)
        except HTTPError, e:
            # The expected 401 Unauthorized Error
            if e.code == 401:
                return {}
            # Expect the unexpected
            raise

    def GetPlayerBans(self, steamids=[]):
        if isinstance(steamids, str):
            pass
        else:
            ",".join(steamids)
        params = {'steamids': steamids}
        return self.generate_api_url(self.interface, 'GetPlayerBans', 1,
            params)['players']

    def GetPlayerSummaries(self, steamids=[]):
        if isinstance(steamids, str):
            pass
        else:
            ",".join(steamids)
        params = {'steamids': steamids}
        return self.generate_api_url(self.interface, 'GetPlayerSummaries', 2,
            params)['response']['players']

    def GetUserGroupList(self, steamid):
        params = {'steamid': steamid}
        return self.generate_api_url(self.interface, 'GetUserGroupList', 1,
            params)['response']['groups']

    def ResolveVanityURL(self, vanityURL):
        params = {'vanityurl': vanityURL}
        return self.generate_api_url(self.interface, 'ResolveVanityURL', 1,
            params)['response']


class ISteamUserStats(SteamWebAPI):
    def __init__(self):
        self.interface = 'ISteamUserStats'
        super(ISteamUserStats, self).__init__()

    def GetGlobalAchievementPercentagesForApp(self, gameid):
        params = {
            'gameid': gameid,
        }
        return self.generate_api_url(self.interface,
            'GetGlobalAchievementPercentagesForApp', 2, params)

    def GetGlobalStatsForGame(self, appid, count, startdate, enddate, **kwarg):
        params = {
            'appid': appid,
            'count': count,
            'startdate': startdate,
            'enddate': enddate,
        }
        params.extend(kwarg)
        return self.generate_api_url(self.interface, 'GetGlobalStatsForGame',
            1, params)

    def GetNumberOfCurrentPlayers(self, appid):
        params = {
            'appid': appid,
        }
        return self.generate_api_url(self.interface,
            'GetNumberOfCurrentPlayers', 1, params)

    def GetSchemaForGame(self, appid, l='en'):
        params = {
            'appid': appid,
            'l': l,
        }
        return self.generate_api_url(self.interface, 'GetSchemaForGame(', 2,
            params)
    
    def GetUserStatsForGame(self, steamid, appid):
        params = {
            'steamid': steamid,
            'appid': appid,
        }
        return self.generate_api_url(self.interface, 'GetUserStatsForGame', 2,
            params)

    def GetPlayerAchievements(self, steamid, appid, l='en'):
        params = {
            'steamid': steamid,
            'appid': appid,
            'l': l,
        }
        return self.generate_api_url(self.interface, 'GetPlayerAchievements',
            1, params)
