# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
import urllib
import urllib2
import json

# API Imports
from settings import STEAM_API_KEY
from settings import DEFAULT_LANGUAGE


# =============================================================================
# >> CLASSES
# =============================================================================
class SteamWebAPI(object):
    def __init__(self, key=STEAM_API_KEY, language=DEFAULT_LANGUAGE):
        self.key = key
        self.language = language

    def generate_api_url(self, interface, method, version, params, format=None,
        key=True):
        # Set version for the API URL
        version = "v%04d" %version

        # Automatically add the API key
        params.update({'key': self.key})

        # Update language to default if not set
        if 'l' in params:
            if not params['l']:
                params.update({'l': self.language})

        if 'language' in params:
            if not params['language']:
                params.update({'language': self.language})

        # Format the URL
        url = 'http://api.steampowered.com/%s/%s/%s/?%s' % (interface, method,
            version, urllib.urlencode(params))

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
        return urllib2.urlopen(self.url)#json.load(urllib2.urlopen(url))

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