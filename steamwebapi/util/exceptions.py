class SteamWebAPIError(Exception):
    pass


class APIKeyRequiredError(SteamWebAPIError):
    def __str__(self):
        return repr('This method requires a Steam Web API Key.')


class APIKeyInvalidError(SteamWebAPIError):
    def __str__(self):
        return repr('Invalid Steam Web API Key. The Steam Web API Key should' +
                    'be 32 alphanumeric characters long.')
