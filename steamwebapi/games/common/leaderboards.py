# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from ..core import SteamWebAPI


# =============================================================================
# >> CLASSES
# =============================================================================
class IPortal2Leaderboards(SteamWebAPI):
    """Base class for IPortal2Leaderboards."""

    def __init__(self, *args, **kwargs):
        """Initialize SteamWebAPI."""
        super(IPortal2Leaderboards, self).__init__(*args, **kwargs)

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
