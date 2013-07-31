"""
.. module:: gameclient
   :platform: Unix, Windows
   :synopsis: Contains the API's "core" classes for constructing queries.

.. moduleauthor:: Michael Barr <micbarr+developer@gmail.com>

"""

# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from ...core import SteamWebAPI


# =============================================================================
# >> CLASSES
# =============================================================================
class _BaseIGCVersion(SteamWebAPI):
    """Base class for _IGCVersion_###."""

    def GetClientVersion(self, method_version=1):
        """.. function:: GetClientVersion(method_version=1)

        Retrieves the game's client version.

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
        """.. function:: GetServerVersion(method_version=1)

        Retrieves the game's server version.

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


class _IGCVersion(_BaseIGCVersion):
    """Extends _BaseIGCVersion adding methods not shared by all interfaces."""

    def GetClusterVersion(self, method_version=1):
        """.. function:: GetClusterVersion(method_version=1)

        Retrieves the game's cluster version.

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
