# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from steam_api.api_base import SteamWebAPI


# =============================================================================
# >> CLASSES
# =============================================================================
class IGCVersion_520(SteamWebAPI):
    def __init__(self):
        self.interface = 'IGCVersion_520'
        super(IGCVersion_520, self).__init__()

    def GetClientVersion(self):
        params = {}
        return self.generate_api_url(self.interface, 'GetClientVersion', 1,
            params, key=True)

    def GetServerVersion(self):
        params = {}
        return self.generate_api_url(self.interface, 'GetServerVersion', 1,
            params, key=True)
