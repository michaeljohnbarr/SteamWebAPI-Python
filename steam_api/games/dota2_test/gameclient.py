# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from steam_api.api_base import SteamWebAPI


# =============================================================================
# >> CLASSES
# =============================================================================
class IGCVersion_205790(SteamWebAPI):
    def __init__(self):
        self.interface = 'IGCVersion_205790'
        super(IGCVersion_205790, self).__init__()

    def GetClientVersion(self):
        params = {}
        return self.generate_api_url(self.interface, 'GetClientVersion', 1,
            params, key=True)

    def GetClusterVersion(self):
        params = {}
        return self.generate_api_url(self.interface, 'GetClusterVersion', 1,
            params, key=True)

    def GetServerVersion(self):
        params = {}
        return self.generate_api_url(self.interface, 'GetServerVersion', 1,
            params, key=True)
