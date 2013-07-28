# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from ...core import SteamWebAPI


# =============================================================================
# >> CLASSES
# =============================================================================
class BaseIGCVersion(SteamWebAPI):
    """Base class for IGCVersion_###."""

    def __init__(self, *args, **kwargs):
        """Initialize SteamWebAPI."""
        super(BaseIGCVersion, self).__init__(*args, **kwargs)

    def GetClientVersion(self, method_version=1):
        """Retrieves the game's client version.

        :param method_version: The method version to use.
        :type method_version: int.
        :returns:  APIQuery,
        :raises: AttributeError, KeyError

        """
        # Set up the parameters
        parameters = {}

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetClientVersion',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetServerVersion(self, method_version=1):
        """Retrieves the game's server version.

        :param method_version: The method version to use.
        :type method_version: int.
        :returns:  APIQuery,
        :raises: AttributeError, KeyError

        """
        # Set up the parameters
        parameters = {}

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetServerVersion',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )


class IGCVersion(BaseIGCVersion):
    """Extends BaseIGCVersion adding methods not shared by all interfaces."""

    def __init__(self, *args, **kwargs):
        """Initialize BaseIGCVersion."""
        super(IGCVersion, self).__init__(*args, **kwargs)

    def GetClusterVersion(self, method_version=1):
        """Retrieves the game's cluster version.

        :param method_version: The method version to use.
        :type method_version: int.
        :returns:  APIQuery,
        :raises: AttributeError, KeyError

        """
        # Set up the parameters
        parameters = {}

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetClusterVersion',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )
