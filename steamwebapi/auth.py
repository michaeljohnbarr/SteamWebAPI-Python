# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from .core import SteamWebAPI
from .util.decorators import public


# =============================================================================
# >> CLASSES
# =============================================================================
@public
class ISteamUserAuth(SteamWebAPI):
    """Methods relating to games' store's assets."""

    def __init__(self, *args, **kwargs):
        """Initialize SteamWebAPI."""
        super(ISteamUserAuth, self).__init__(*args, **kwargs)

    def AuthenticateUser(self, steamid, sessionkey, encrypted_loginkey,
                         method_version=1):
        """
            Arguments:
                steamid             - (str) Should be the users steamid,
                                            unencrypted.
                sessionkey          - (str) Should be a 32 byte random blob of
                                            data, which is then encrypted with
                                            RSA using the Steam system's public
                                            key.  Randomness is important here
                                            for security.
                encrypted_loginkey  - (str) Should be the users hashed
                                            loginkey, AES encrypted with the
                                            sessionkey.
        """
        # Set up the parameters
        parameters = {
            'steamid': steamid,
            'sessionkey': sessionkey,
            'encrypted_loginkey': encrypted_loginkey,
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='AuthenticateUser',
            method_version=method_version,
            httpmethod='POST',
            parameters=parameters,
        )


@public
class ISteamWebUserPresenceOAuth(SteamWebAPI):
    """Methods relating to games' store's assets."""

    def __init__(self, *args, **kwargs):
        """Initialize SteamWebAPI."""
        super(ISteamWebUserPresenceOAuth, self).__init__(*args, **kwargs)

    def PollStatus(self, steamid, umqid, message, pollid='', sectimeout='',
                   secidletime='', use_accountids=False, method_version=1):
        """
            Arguments:
                steamid         - (str) Steam ID of the user
                umqid           - (int) UMQ ID
                message         - (int) Message that was last known to the user
                pollid          - (int) Caller-specific poll id
                sectimeout      - (int) Long-poll timeout in seconds
                secidletime     - (int) How many seconds is client considering
                                        itself idle
                use_accountids  - (bool) 0: (default) return steamid_from in
                                            output
                                         1: return accountid_from
        """
        # Set up the parameters
        parameters = {
            'steamid': steamid,
            'umqid': umqid,
            'message': message,
            'pollid': pollid,
            'sectimeout': sectimeout,
            'secidletime': secidletime,
            'use_accountids': int(bool(use_accountids)),
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='PollStatus',
            method_version=method_version,
            httpmethod='POST',
            parameters=parameters,
        )
