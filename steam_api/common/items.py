from .steam_api.api_base import SteamWebAPI


class BaseITFPromos(SteamWebAPI):
    """__docstring__"""

    def __init__(self, *args, **kwargs):
        """Initialize SteamWebAPI."""
        super(BaseITFPromos, self).__init__(*args, **kwargs)

    def GetItemID(self, steamid, promoid, method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'steamid': steamid,
            'PromoID': promoid,
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetItemID',
            method_version=method_version,
            httpmethod='GET',
            params=parameters,
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
            params=parameters,
        )


class BaseIEconItems(SteamWebAPI):
    """__docstring__"""

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
            interface='ITFPromos_710',
            method='GrantItem',
            method_version=method_version,
            httpmethod='POST',
            params=parameters,
        )

    def GetSchema(self, language='', method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'language': language or self.language,
            'key': self.key,
        }

        return self.api_query(
            interface='ITFPromos_710',
            method='GrantItem',
            method_version=method_version,
            httpmethod='POST',
            params=parameters,
        )
