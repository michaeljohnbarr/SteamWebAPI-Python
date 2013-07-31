class SteamWebAPIError(Exception):
    pass


class APIKeyRequiredError(SteamWebAPIError):
    def __str__(self):
        return repr('This method requires a Steam Web API Key.')
