SteamWebAPI-Python
==================

A class-based wrapper for the Steam Community Web API.

settings.py:
------------
* STEAM_API_KEY
  
  Your Steam API Key as requested from https://steamcommunity.com/login/home/?goto=%2Fdev%2Fapikey

* DEFAULT_LANGUAGE

  If no language argument is provided to a method requesting one, this language will automatically be provided.

api_base.py:
------------
Contains the class APIQuery, which is a utility class for returning data in either raw JSON, XML, or VDF format as queried from urllib2.urlopen(API_URL) via any interface method. Example usage:

    from steam_api.user import ISteamUser
    
    # Create an instance of ISteamUser
    iSteamUser = ISteamUser()

    # Using the APIQuery methods
    return_xml = iSteamUser.GetFriendList(steamid).as_xml()
    return_json = iSteamUser.GetFriendList(steamid).as_json()
    return_vdf = iSteamUser.GetFriendList(steamid).as_vdf()

    # Using the APIQuery properties
    return_xml = iSteamUser.GetFriendList(steamid).xml
    return_json = iSteamUser.GetFriendList(steamid).json
    return_vdf = iSteamUser.GetFriendList(steamid).vdf

    # Print the URL for the base API Query
    iSteamUser.GetFriendList(steamid).url
    
    # Print the URL for the XML API Query
    iSteamUser.GetFriendList(steamid).as_xml().url