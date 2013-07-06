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
            'relationship': relationship
        }
        # According to http://wiki.teamfortress.com/wiki/WebAPI/GetFriendList,
        #   "If the profile is not public or there are no available entries for
        #   the given relationship only an empty object will be returned."
        #   However, this is not the case. It gives a 401 Unauthorized
        #   HTTPError. Thus, we must create this workaround.
        try:
            return self.generate_api_url(
                method='GetFriendList',
                version=kwargs.get('method_version', 1),
                parameters=parameters
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
        }
        return self.generate_api_url(
            method='GetPlayerBans',
            version=kwargs.get('method_version', 1),
            parameters=parameters
        )

    def GetPlayerSummaries(self, steamids=[], **kwargs):
        if isinstance(steamids, str):
            pass
        else:
            ",".join(steamids)
        parameters = {
            'steamids': steamids,
        }
        return self.generate_api_url(
            method='GetPlayerSummaries',
            version=kwargs.get('method_version', 2),
            parameters=parameters
        )

    def GetUserGroupList(self, steamid, **kwargs):
        parameters = {
            'steamid': steamid,
        }
        return self.generate_api_url(
            method='GetUserGroupList',
            version=kwargs.get('method_version', 1),
            parameters=parameters
        )

    def ResolveVanityURL(self, vanityURL, **kwargs):
        parameters = {
            'vanityurl': vanityURL,
        }
        return self.generate_api_url(
            method='ResolveVanityURL',
            version=kwargs.get('method_version', 1),
            parameters=parameters
        )


class ISteamUserStats(SteamWebAPI):
    def GetGlobalAchievementPercentagesForApp(self, gameid, **kwargs):
        parameters = {
            'gameid': gameid,
        }
        return self.generate_api_url(
            method='GetGlobalAchievementPercentagesForApp',
            version=kwargs.get('method_version', 2),
            parameters=parameters
        )

    def GetGlobalStatsForGame(self, appid, count, startdate, enddate, **kwargs):
        parameters = {
            'appid': appid,
            'count': count,
            'startdate': startdate,
            'enddate': enddate,
        }
        parameters.extend(kwargs)  # TODO: Figure out a way to handle name[0]...
        return self.generate_api_url(
            method='GetGlobalStatsForGame',
            version=kwargs.get('method_version', 1),
            parameters=parameters
        )

    def GetNumberOfCurrentPlayers(self, appid, **kwargs):
        parameters = {
            'appid': appid,
        }
        return self.generate_api_url(
            method='GetNumberOfCurrentPlayers',
            version=kwargs.get('method_version', 1),
            parameters=parameters
        )

    def GetSchemaForGame(self, appid, l='', **kwargs):
        """Retrieves the game schema for the given appid."""
        parameters = {
            'appid': appid,
            'l': l,
        }
        return self.generate_api_url(
            method='GetSchemaForGame',
            version=kwargs.get('method_version', 2),
            parameters=parameters
        )

    def GetUserStatsForGame(self, steamid, appid, **kwargs):
        """Retrieves the stats for the given SteamID and appid."""
        parameters = {
            'steamid': steamid,
            'appid': appid,
        }
        return self.generate_api_url(
            method='GetUserStatsForGame',
            version=kwargs.get('method_version', 2),
            parameters=parameters
        )

    def GetPlayerAchievements(self, steamid, appid, l='', **kwargs):
        """Retrieves the achievements for the given SteamID and appid."""
        parameters = {
            'steamid': steamid,
            'appid': appid,
            'l': l,
        }
        return self.generate_api_url(
            method='GetPlayerAchievements',
            version=kwargs.get('method_version', 1),
            parameters=parameters
        )


class IPlayerService(SteamWebAPI):
    def GetRecentlyPlayedGames(self, steamid, count=0, **kwargs):
        """Retrieves the recently played games for the given SteamID up to
        the given count.

        """
        parameters = {
            'steamid': steamid,
            'count': count,
        }
        return self.generate_api_url(
            method='GetPlayerAchievements',
            version=kwargs.get('method_version', 1),
            parameters=parameters
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
        }
        return self.generate_api_url(
            method='GetOwnedGames',
            version=kwargs.get('method_version', 1),
            parameters=parameters
        )

    def GetSteamLevel(self, steamid, **kwargs):
        """Retrieves the Steam Level for the given SteamID."""
        parameters = {
            'steamid': steamid,
        }
        return self.generate_api_url(
            method='GetSteamLevel',
            version=kwargs.get('method_version', 1),
            parameters=parameters
        )

    def GetBadges(self, steamid, **kwargs):
        """Retrieves badge information for the given SteamID."""
        parameters = {
            'steamid': steamid,
        }
        return self.generate_api_url(
            method='GetBadges',
            version=kwargs.get('method_version', 1),
            parameters=parameters
        )
