"""
.. module:: leaderboards
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
class _IPortal2Leaderboards(SteamWebAPI):
    """Base class for _IPortal2Leaderboards."""

    def GetBucketizedData(self, leaderboardName, method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'leaderboardName': leaderboardName,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetBucketizedData',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )
