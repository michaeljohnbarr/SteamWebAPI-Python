class SteamWebAPIError(Exception):
    pass


class PrivateProfileError(SteamWebAPIError):
    def __init__(self, steamid):
        self.steamid = steamid

    def __str__(self):
        return '%s has a private/friends-only profile.' % self.steamid
