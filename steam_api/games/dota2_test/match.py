# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from steam_api.api_base import SteamWebAPI


# =============================================================================
# >> CLASSES
# =============================================================================
class IDOTA2Match_205790(SteamWebAPI):
    def __init__(self):
        self.interface = 'IDOTA2Match_205790'
        super(IDOTA2Match_205790, self).__init__()

    def GetMatchDetails(self, match_id):
        params = {
            'match_id': match_id,
            }
        return self.generate_api_url(self.interface, 'GetMatchDetails', 1,
            params, key=True)

    def GetMatchHistory(self, player_name=None, hero_id=None, game_mode=None,
        skill=None, date_min=None, date_max=None, min_players=None,
        account_id=None, league_id=None, start_at_match_id=None,
        matches_requested=None, tournament_games_only=None):
        params = {
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
        return self.generate_api_url(self.interface, 'GetMatchHistory', 1,
            params, key=True)