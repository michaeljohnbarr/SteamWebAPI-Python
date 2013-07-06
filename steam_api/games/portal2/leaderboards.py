# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from steam_api.api_base import SteamWebAPI


# =============================================================================
# >> CLASSES
# =============================================================================
class IPortal2Leaderboards_620(SteamWebAPI):
    def GetBucketizedData(self, leaderboardName, **kwargs):
        parameters = {
            'leaderboardName': leaderboardName,
        }
        return self.generate_api_url(
            method='GetBucketizedData',
            version=kwargs.get('version', 1),
            parameters=parameters,
            key=True
        )
