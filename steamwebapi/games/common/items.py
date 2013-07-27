from ..core import SteamWebAPI


class BaseITFPromos(SteamWebAPI):
    """Base class for ITFPromos_###."""

    def __init__(self, *args, **kwargs):
        """Initialize SteamWebAPI."""
        super(BaseITFPromos, self).__init__(*args, **kwargs)

    def GetItemID(self, steamid, promoid, method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'steamid': steamid,
            'promoid': promoid,
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetItemID',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GrantItem(self, steamid, promoid, method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'steamid': steamid,
            'PromoID': promoid,
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GrantItem',
            method_version=method_version,
            httpmethod='POST',
            parameters=parameters,
        )


class BaseIEconItems(SteamWebAPI):
    """Base class for IEconItems_###."""

    def __init__(self, *args, **kwargs):
        """Initialize SteamWebAPI."""
        super(BaseIEconItems, self).__init__(*args, **kwargs)

    def GetPlayerItems(self, steamid, method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'steamid': steamid,
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetPlayerItems',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetSchema(self, language='', method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'language': language or self.language,
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetSchema',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )


class IEconItems(BaseIEconItems):
    def __init__(self, *args, **kwargs):
        """Initialize BaseIEconItems, which initializes SteamWebAPI."""
        super(IEconItems, self).__init__(*args, **kwargs)

    def GetSchemaURL(self, method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'key': self.key,
        }

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
            'language': language or self.language,
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetStoreMetaData',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )


class ExtendedIEconItems(IEconItems):
    def __init__(self, *args, **kwargs):
        """Initialize IEconItems, which initializes SteamWebAPI."""
        super(ExtendedIEconItems, self).__init__(*args, **kwargs)

    def GetStoreStatus(self, language='', method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'language': language or self.language,
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetStoreMetaData',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )


class BaseIEconDOTA2(SteamWebAPI):
    """Base class for IEconDOTA2_###."""

    def __init__(self, *args, **kwargs):
        """Initialize SteamWebAPI."""
        super(BaseIEconDOTA2, self).__init__(*args, **kwargs)

    def GetHeroes(self, itemizedonly, language='', method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'language': language or self.language,
            'itemizedonly': bool(itemizedonly),
            'key': self.key,
        }

        #
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetHeroes',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetRarities(self, language='', method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'language': language or self.language,
            'key': self.key,
        }

        #
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetRarities',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetTournamentPrizePool(self, method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'key': self.key,
        }

        #
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetTournamentPrizePool',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )
