"""
.. module:: match
   :platform: Unix, Windows
   :synopsis: Contains the API's "core" classes for constructing queries.

.. moduleauthor:: Michael Barr <micbarr+developer@gmail.com>

"""
# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from ...core import SteamWebAPI


# =============================================================================
# >> CLASSES
# =============================================================================
class BaseIDOTA2Match(SteamWebAPI):
    """Base class for IDOTA2Match_###."""

    def GetLeagueListing(self, method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetLeagueListing',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetLiveLeagueGames(self, method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetLiveLeagueGames',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetMatchDetails(self, match_id, method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'match_id': match_id,
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetMatchDetails',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetMatchHistory(self, player_name=None, hero_id=None, game_mode=None,
                        skill=None, date_min=None, date_max=None,
                        min_players=None, account_id=None, league_id=None,
                        start_at_match_id=None, matches_requested=None,
                        tournament_games_only=None, method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'player_name': player_name,
            'hero_id': hero_id,
            'game_mode': game_mode,
            'skill': skill,
            'date_min': date_min,
            'date_max': date_max,
            'min_players': min_players,
            'account_id': account_id,
            'league_id': league_id,
            'start_at_match_id': start_at_match_id,
            'matches_requested': matches_requested,
            'tournament_games_only': tournament_games_only,
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetMatchHistory',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetMatchHistoryBySequenceNum(self, start_at_match_seq_num,
                                     matches_requested, method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'start_at_match_seq_num': start_at_match_seq_num,
            'matches_requested': matches_requested,
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetMatchHistoryBySequenceNum',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetTeamInfoByTeamID(self, start_at_team_id, teams_requested,
                            method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'start_at_team_id': start_at_team_id,
            'teams_requested': teams_requested,
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetTeamInfoByTeamID',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )
