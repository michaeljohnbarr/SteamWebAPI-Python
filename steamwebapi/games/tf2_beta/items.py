# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
import warnings

# API Imports
from ..common.items import _BaseITFPromos, _BaseIEconItems
from ...core import SteamWebAPI
from ...util.decorators import public, api_key_required


# =============================================================================
# >> CLASSES
# =============================================================================
@public
class ITFItems_520(SteamWebAPI):
    """"""

    @api_key_required
    def GetGoldenWrenches(self, method_version=2):
        # Set up the parameters
        parameters = {}

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetGoldenWrenches',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )


@public
class ITFPromos_520(_BaseITFPromos):
    """Methods for retrieving and and granting promo items."""


@public
class IEconItems_520(_BaseIEconItems):
    """Methods relating to in-game items for supported games."""

    def GetSchemaURL(self, method_version=1):
        """"""
        # Set up the parameters
        parameters = {}

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetSchemaURL',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetStoreMetaData(self, language='', method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'language': language,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetStoreMetaData',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetStoreStatus(self, method_version=1):
        """"""
        # Set up the parameters
        parameters = {}

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetStoreStatus',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )
