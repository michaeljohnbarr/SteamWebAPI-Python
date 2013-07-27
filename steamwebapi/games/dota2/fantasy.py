# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from ...core import SteamWebAPI


# =============================================================================
# >> CLASSES
# =============================================================================
class IDOTA2Fantasy_570(SteamWebAPI):
    """"""
    def GetFantasyLeagueLeaderboard(self, fantasyLeagueID, count,
                                    startTimeFilter='', endTimeFilter='',
                                    matchIDFilter='', last_match=False,
                                    in_hall=False, method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'fantasyLeagueID': fantasyLeagueID,
            'count': count,
            'startTimeFilter': startTimeFilter,
            'endTimeFilter': endTimeFilter,
            'matchIDFilter': matchIDFilter,
            'last_match': bool(last_match),
            'in_hall': bool(in_hall),
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetFantasyLeagueLeaderboard',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetFantasyPlayerScore(self, fantasyLeagueID, playerAccountID,
                              startTimeFilter='', endTimeFilter='',
                              matchIDFilter='', last_match=False,
                              method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'fantasyLeagueID': fantasyLeagueID,
            'playerAccountID': playerAccountID,
            'startTimeFilter': startTimeFilter,
            'endTimeFilter': endTimeFilter,
            'matchIDFilter': matchIDFilter,
            'last_match': bool(last_match),
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetFantasyPlayerScore',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetFantasyTeamInfoOwnedBy(self, ownerAccountID, fantasyLeagueID='',
                                  startTimeFilter='', endTimeFilter='',
                                  method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'ownerAccountID': ownerAccountID,
            'fantasyLeagueID': fantasyLeagueID,
            'startTimeFilter': startTimeFilter,
            'endTimeFilter': endTimeFilter,
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetFantasyTeamInfoOwnedBy',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetFantasyTopPlayers(self, fantasyLeagueID, count, role='',
                             startTimeFilter='', endTimeFilter='',
                             last_match=False, method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'fantasyLeagueID': fantasyLeagueID,
            'count': count,
            'role': role,
            'startTimeFilter': startTimeFilter,
            'endTimeFilter': endTimeFilter,
            'last_match': bool(last_match),
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetFantasyTopPlayers',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetValidFantasyPlayersForRoles(self, fantasyLeagueID, ownerAccountID,
                                       teamIndex, method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'fantasyLeagueID': fantasyLeagueID,
            'ownerAccountID': ownerAccountID,
            'teamIndex': teamIndex,
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetValidFantasyPlayersForRoles',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )
