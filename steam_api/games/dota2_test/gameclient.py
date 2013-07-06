# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from steam_api.api_base import SteamWebAPI


# =============================================================================
# >> CLASSES
# =============================================================================
class IGCVersion_205790(SteamWebAPI):
    def GetClientVersion(self, **kwargs):
        parameters = {}
        return self.generate_api_url(
            method='GetClientVersion',
            version=kwargs.get('version', 1),
            parameters=parameters,
            key=True
        )

    def GetClusterVersion(self, **kwargs):
        parameters = {}
        return self.generate_api_url(
            method='GetClusterVersion',
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
