"""
.. module:: items
   :platform: Unix, Windows
   :synopsis: Contains the API's "core" classes for constructing queries.

.. moduleauthor:: Michael Barr <micbarr+developer@gmail.com>

"""
# =============================================================================
# >> IMPORTS
# =============================================================================
from ...core import SteamWebAPI
from ...util.decorators import api_key_required


# =============================================================================
# >> CLASSES
# =============================================================================
class _BaseITFPromos(SteamWebAPI):
    """Base class for ITFPromos_###."""

    @api_key_required
    def GetItemID(self, steamid, promoid, method_version=1):
        """
        :param steamid: The method version to use.
        :type steamid: int.
        :param promoid: The method version to use.
        :type promoid: int.
        :param method_version: The method version to use.
        :type method_version: int.
        :returns:  APIQuery,
        :raises: AttributeError, KeyError

        """
        # Set up the parameters
        parameters = {
            'steamid': steamid,
            'promoid': promoid,
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetItemID',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    @api_key_required
    def GrantItem(self, steamid, promoid, method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'steamid': steamid,
            'PromoID': promoid,
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GrantItem',
            method_version=method_version,
            httpmethod='POST',
            parameters=parameters,
        )


class _BaseIEconItems(SteamWebAPI):
    """Base class for IEconItems_###."""

    @api_key_required
    def GetPlayerItems(self, steamid, method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'steamid': steamid,
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetPlayerItems',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    @api_key_required
    def GetSchema(self, language='', method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'language': language or self.language,
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetSchema',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )


class _IEconItems(_BaseIEconItems):
    """"""

    @api_key_required
    def GetSchemaURL(self, method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetSchemaURL',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    @api_key_required
    def GetStoreMetaData(self, language='', method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'language': language or self.language,
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetStoreMetaData',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )


class _ExtendedIEconItems(_IEconItems):
    """"""

    @api_key_required
    def GetStoreStatus(self, language='', method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'language': language or self.language,
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetStoreMetaData',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )


class _BaseIEconDOTA2(SteamWebAPI):
    """Base class for IEconDOTA2_###."""

    @api_key_required
    def GetHeroes(self, itemizedonly, language='', method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'language': language or self.language,
            'itemizedonly': bool(itemizedonly),
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetHeroes',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    @api_key_required
    def GetRarities(self, language='', method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'language': language or self.language,
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetRarities',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    @api_key_required
    def GetTournamentPrizePool(self, method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetTournamentPrizePool',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )
