# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
import urllib
import urllib2

# API Imports
from settings import STEAM_API_KEY, DEFAULT_LANGUAGE


# =============================================================================
# >> CLASSES
# =============================================================================
class SteamWebAPI(object):
    def __init__(self, key='', language=''):
        self.key = key or STEAM_API_KEY
        self.language = language or DEFAULT_LANGUAGE
        self.interface = self.__class__.__name__

    def api_query(self, method, method_version, parameters, format=None, key=True):
        # Set version for the API URL
        version = "v%04d" % method_version

        if key:
            # Automatically add the API key
            parameters.update({'key': self.key})

        # Update language to default if not set
        if 'l' in parameters:
            if not parameters['l']:
                parameters.update({'l': self.language})

        if 'language' in parameters:
            if not parameters['language']:
                parameters.update({'language': self.language})

        # Format the URL
        url = 'http://api.steampowered.com/%s/%s/%s/?%s' % (
            self.interface,
            method,
            version,
            urllib.urlencode(parameters)
        )

        # Return the APIQuery instance
        return APIQuery(url)


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
    def __init__(self, url):
        self.url = url

    def as_xml(self):
        self.url += '&format=xml'
        return urllib2.urlopen(self.url)

    def as_json(self):
        self.url += '&format=json'
        return urllib2.urlopen(self.url)

    def as_vdf(self):
        self.url += '&format=vdf'
        return urllib2.urlopen(self.url)

    @property
    def xml(self):
        return self.as_xml()

    @property
    def json(self):
        return self.as_json()

    @property
    def vdf(self):
        return self.as_vdf()
