# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from steam_api.api_base import SteamWebAPI


# =============================================================================
# >> CLASSES
# =============================================================================
class IGCVersion_440(SteamWebAPI):
    def GetClientVersion(self, **kwargs):
        parameters = {}
        return self.generate_api_url(
            method='GetClientVersion',
            version=kwargs.get('version', 1),
            parameters=parameters,
            key=True
        )

    def GetServerVersion(self, **kwargs):
        parameters = {}
        return self.generate_api_url(
            method='GetServerVersion',
            version=kwargs.get('version', 1),
            parameters=parameters,
            key=True
        )
