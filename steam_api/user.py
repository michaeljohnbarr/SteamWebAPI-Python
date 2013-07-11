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
    def GetFriendList(self, steamid, relationship='all', **kwargs):
        """Retrieves a dictionary of
        """
        parameters = {
            'steamid': steamid,
            'relationship': relationship,
            'key': self.key,
        }
        # According to http://wiki.teamfortress.com/wiki/WebAPI/GetFriendList,
        #   "If the profile is not public or there are no available entries for
        #   the given relationship only an empty object will be returned."
        #   However, this is not the case. It gives a 401 Unauthorized
        #   HTTPError. Thus, we must create this workaround.
        try:
            return self.api_query(
                method='GetFriendList',
                httpmethod='GET',
                version=kwargs.get('method_version', 1),
                params=parameters
            )
        except HTTPError, e:
            # The expected 401 Unauthorized Error
            if e.code == 401:
                return {}
            # Expect the unexpected
            raise

    def GetPlayerBans(self, steamids=[], **kwargs):
        if isinstance(steamids, str):
            pass
        else:
            ",".join(steamids)
        parameters = {
            'steamids': steamids,
            'key': self.key,
        }
        return self.api_query(
            method='GetPlayerBans',
            httpmethod='GET',
            version=kwargs.get('method_version', 1),
            params=parameters
        )

    def GetPlayerSummaries(self, steamids=[], **kwargs):
        if isinstance(steamids, str):
            pass
        else:
            ",".join(steamids)
        parameters = {
            'steamids': steamids,
            'key': self.key,
        }
        return self.api_query(
            method='GetPlayerSummaries',
            httpmethod='GET',
            version=kwargs.get('method_version', 2),
            params=parameters
        )

    def GetUserGroupList(self, steamid, **kwargs):
        parameters = {
            'steamid': steamid,
            'key': self.key,
        }
        return self.api_query(
            method='GetUserGroupList',
            httpmethod='GET',
            version=kwargs.get('method_version', 1),
            params=parameters
        )

    def ResolveVanityURL(self, vanityURL, **kwargs):
        parameters = {
            'vanityurl': vanityURL,
            'key': self.key,
        }
        return self.api_query(
            method='ResolveVanityURL',
            httpmethod='GET',
            version=kwargs.get('method_version', 1),
            params=parameters
        )


class ISteamUserStats(SteamWebAPI):
    def GetGlobalAchievementPercentagesForApp(self, gameid, **kwargs):
        parameters = {
            'gameid': gameid,
        }
        return self.api_query(
            method='GetGlobalAchievementPercentagesForApp',
            httpmethod='GET',
            version=kwargs.get('method_version', 2),
            params=parameters
        )

    def GetGlobalStatsForGame(self, appid, count, startdate, enddate, **kwargs):
        parameters = {
            'appid': appid,
            'count': count,
            'startdate': startdate,
            'enddate': enddate,
        }
        parameters.extend(kwargs)  # TODO: Figure out a way to handle name[0]...
        return self.api_query(
            method='GetGlobalStatsForGame',
            httpmethod='GET',
            version=kwargs.get('method_version', 1),
            params=parameters
        )

    def GetNumberOfCurrentPlayers(self, appid, **kwargs):
        parameters = {
            'appid': appid,
        }
        return self.api_query(
            method='GetNumberOfCurrentPlayers',
            httpmethod='GET',
            version=kwargs.get('method_version', 1),
            params=parameters
        )

    def GetSchemaForGame(self, appid, l='', **kwargs):
        """Retrieves the game schema for the given appid."""
        parameters = {
            'appid': appid,
            'l': l or self.language,
            'key': self.key,
        }
        return self.api_query(
            method='GetSchemaForGame',
            httpmethod='GET',
            version=kwargs.get('method_version', 2),
            params=parameters
        )

    def GetUserStatsForGame(self, steamid, appid, **kwargs):
        """Retrieves the stats for the given SteamID and appid."""
        parameters = {
            'steamid': steamid,
            'appid': appid,
            'key': self.key,
        }
        return self.api_query(
            method='GetUserStatsForGame',
            httpmethod='GET',
            version=kwargs.get('method_version', 2),
            params=parameters
        )

    def GetPlayerAchievements(self, steamid, appid, l='', **kwargs):
        """Retrieves the achievements for the given SteamID and appid."""
        parameters = {
            'steamid': steamid,
            'appid': appid,
            'l': l or self.language,
            'key': self.key,
        }
        return self.api_query(
            method='GetPlayerAchievements',
            httpmethod='GET',
            version=kwargs.get('method_version', 1),
            params=parameters
        )


class IPlayerService(SteamWebAPI):
    def GetRecentlyPlayedGames(self, steamid, count=0, **kwargs):
        """Retrieves the recently played games for the given SteamID up to
        the given count.

        """
        parameters = {
            'steamid': steamid,
            'count': count,
            'key': self.key,
        }
        return self.api_query(
            method='GetPlayerAchievements',
            httpmethod='GET',
            version=kwargs.get('method_version', 1),
            params=parameters
        )

    def GetOwnedGames(self, steamid, include_appinfo=True,
                      include_played_free_games=True, appids_filter=[],
                      **kwargs):
        """Retrieves games owned by the given SteamID."""
        if isinstance(appids_filter, str):
            pass
        else:
            ",".join(appids_filter)
        parameters = {
            'steamid': steamid,
            'include_appinfo': include_appinfo,
            'include_played_free_games': include_played_free_games,
            'appids_filter': appids_filter,
            'key': self.key,
        }
        return self.api_query(
            method='GetOwnedGames',
            httpmethod='GET',
            version=kwargs.get('method_version', 1),
            params=parameters
        )

    def GetSteamLevel(self, steamid, **kwargs):
        """Retrieves the Steam Level for the given SteamID."""
        parameters = {
            'steamid': steamid,
            'key': self.key,
        }
        return self.api_query(
            method='GetSteamLevel',
            httpmethod='GET',
            version=kwargs.get('method_version', 1),
            params=parameters
        )

    def GetBadges(self, steamid, **kwargs):
        """Retrieves badge information for the given SteamID."""
        parameters = {
            'steamid': steamid,
            'key': self.key,
        }
        return self.api_query(
            method='GetBadges',
            httpmethod='GET',
            version=kwargs.get('method_version', 1),
            params=parameters
        )
