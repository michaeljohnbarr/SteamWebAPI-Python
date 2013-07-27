# ==============================================================================
# >> IMPORTS
# ==============================================================================
# Python Imports
import urllib
import urllib2

# API Imports
from settings import STEAM_API_KEY, DEFAULT_LANGUAGE, DEFAULT_FORMAT


# ==============================================================================
# >> CLASSES
# ==============================================================================
class SteamWebAPI(object):
    def __init__(self, key=STEAM_API_KEY, language=DEFAULT_LANGUAGE,
                 format=DEFAULT_FORMAT):
        self.key = key
        self.language = language
        self.format = format.lower()

    def api_query(self, *args, **kwargs):
        """Returns an APIQuery instance of the method that was passed in, or an
        executed APIQuery that returns urllib2.urlopen() if a default format is
        specified.

        """
        if not self.format:
            # Return the APIQuery instance
            return APIQuery(*args, **kwargs)

        # Return an executed APIQuery call with the format of their choice
        return APIQuery(*args, **kwargs).__getattribute__(self.format)


class APIQuery(object):
    """Utility class for returning data in either raw JSON, XML, or VDF format
    as queried from urllib2.urlopen(API_URL) via any interface method.

    Example Usage:
        iSteamUser = ISteamUser()
        # Using the APIQuery methods
        return_xml = iSteamUser.GetFriendList(steamid).as_xml()
        return_json = iSteamUser.GetFriendList(steamid).as_json()
        return_vdf = iSteamUser.GetFriendList(steamid).as_vdf()

        # Using the APIQuery properties
        return_xml = iSteamUser.GetFriendList(steamid).xml
        return_json = iSteamUser.GetFriendList(steamid).json
        return_vdf = iSteamUser.GetFriendList(steamid).vdf

    """
    def __init__(self, interface, method, method_version=1, httpmethod='GET',
                 parameters={}):
        self._interface = interface
        self._method = method
        self._version = 'v{0:04d}'.format(method_version)
        self._parameters = parameters
        self._httpmethod = str(httpmethod).upper()
        self._url = self._encode_url()

    def _encode_url(self):
        """Formats the URL for the call via the Steam Web API."""
        return 'http://api.steampowered.com/{0}/{1}/{2}/?{3}'.format(
            self._interface,
            self._method,
            self._version,
            urllib.urlencode(self._parameters)
        )

    @property
    def interface(self):
        """Returns private variable interface."""
        return self._interface

    @property
    def method(self):
        """Returns private variable method."""
        return self._method

    @property
    def version(self):
        """Returns private variable version."""
        return self._version

    @property
    def httpmethod(self):
        """Returns private variable httpmethod."""
        return self._httpmethod

    @property
    def url(self):
        """Returns private variable url."""
        # We format the URL before returning it in case a parameter was changed
        self._url = self._encode_url()
        return self._url

    @property
    def parameters(self):
        """Returns private variable parameters."""
        return self._parameters

    @property
    def xml(self):
        return self.as_xml()

    @property
    def json(self):
        return self.as_json()

    @property
    def vdf(self):
        return self.as_vdf()

    def as_xml(self):
        self._url += '&format=xml'
        return urllib2.urlopen(self._url)

    def as_json(self):
        self._url += '&format=json'
        return urllib2.urlopen(self._url)

    def as_vdf(self):
        self._url += '&format=vdf'
        return urllib2.urlopen(self._url)
