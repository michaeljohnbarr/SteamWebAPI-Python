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
from ...util.decorators import api_key_required


# =============================================================================
# >> CLASSES
# =============================================================================
class _BaseIDOTA2Match(SteamWebAPI):
    """Base class for IDOTA2Match_###."""

    @api_key_required
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

    @api_key_required
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

    @api_key_required
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

    @api_key_required
    def GetMatchHistory(self, player_name='', hero_id='', game_mode='',
                        skill='', date_min='', date_max='',
                        min_players='', account_id='', league_id='',
                        start_at_match_id='', matches_requested='',
                        tournament_games_only='', method_version=1):
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

    @api_key_required
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

    @api_key_required
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
