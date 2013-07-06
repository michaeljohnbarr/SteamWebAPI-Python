# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from steam_api.api_base import SteamWebAPI


# =============================================================================
# >> CLASSES
# =============================================================================
class IDOTA2Match_205790(SteamWebAPI):
    def GetLeagueListing(self, **kwargs):
        parameters = {}
        return self.generate_api_url(
            method='GetLeagueListing',
            version=kwargs.get('version', 1),
            parameters=parameters,
            key=True
        )

    def GetLiveLeagueGames(self, **kwargs):
        parameters = {}
        return self.generate_api_url(
            method='GetLiveLeagueGames',
            version=kwargs.get('version', 1),
            parameters=parameters,
            key=True
        )

    def GetMatchDetails(self, match_id, **kwargs):
        parameters = {
            'match_id': match_id,
        }
        return self.generate_api_url(
            method='GetMatchDetails',
            version=kwargs.get('version', 1),
            parameters=parameters,
            key=True
        )

    def GetMatchHistory(self, player_name=None, hero_id=None, game_mode=None,
                        skill=None, date_min=None, date_max=None,
                        min_players=None, account_id=None, league_id=None,
                        start_at_match_id=None, matches_requested=None,
                        tournament_games_only=None, **kwargs):
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
        }
        return self.generate_api_url(
            method='GetMatchHistory',
            version=kwargs.get('version', 1),
            parameters=parameters,
            key=True
        )

    def GetMatchHistoryBySequenceNum(self, start_at_match_seq_num,
                                     matches_requested, **kwargs):
        parameters = {
            'start_at_match_seq_num': start_at_match_seq_num,
            'matches_requested': matches_requested,
        }
        return self.generate_api_url(
            method='GetMatchHistoryBySequenceNum',
            version=kwargs.get('version', 1),
            parameters=parameters,
            key=True
        )

    def GetTeamInfoByTeamID(self, start_at_team_id, teams_requested, **kwargs):
        parameters = {
            'start_at_team_id': start_at_team_id,
            'teams_requested': teams_requested,
        }
        return self.generate_api_url(
            method='GetTeamInfoByTeamID',
            version=kwargs.get('version', 1),
            parameters=parameters,
            key=True
        )
