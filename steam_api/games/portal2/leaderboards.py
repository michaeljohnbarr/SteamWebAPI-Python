# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from steam_api.api_base import SteamWebAPI


# =============================================================================
# >> CLASSES
# =============================================================================
class IPortal2Leaderboards_620(SteamWebAPI):
    def __init__(self):
        self.interface = 'IPortal2Leaderboards_620'
        super(IPortal2Leaderboards_620, self).__init__()

    def GetBucketizedData(self, leaderboardName):
        params = {
            'leaderboardName': leaderboardName,
            }
        return self.generate_api_url(self.interface, 'GetBucketizedData', 1,
            params, key=True)
