# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
from unittest import TestCase, main

# Settings Imports
from steamwebapi.settings import STEAM_API_KEY, DEFAULT_LANGUAGE

# Core Imports
from steamwebapi.core import SteamWebAPI, APIQuery

# Util Imports
from steamwebapi.util.exceptions import APIKeyInvalidError


# =============================================================================
# >> TEST CLASSES
# =============================================================================
class TestCoreSteamWebAPI(TestCase):
    """Tests functionality of the SteamWebAPI within core.py."""

    def setUp(self):
        """Initializes a SteamWebAPI instance."""
        self.steamwebapi = SteamWebAPI()

    # -------------------------------------------------------------------------
    # API Key Tests
    # -------------------------------------------------------------------------
    def test_api_key_equalto_settings_api_key(self):
        """Tests that initializing SteamWebAPI without arguments retrieves
        the STEAM_API_KEY from ./steamwebapi/settings.py.

        """
        self.assertEqual(
            self.steamwebapi.key,
            STEAM_API_KEY,
            'The settings.STEAM_API_KEY was not initialized as the default ' +
            'argument for SteamWebAPI().key.',
        )

    def test_api_key_not_equalto_settings_api_key(self):
        """Tests that changing the Steam Web API key from within the
        SteamWebAPI instance works, as well as ensure that it differs from the
        STEAM_API_KEY from ./steamwebapi/settings.py.

        """
        self.steamwebapi.key = 'XXXX0000XXXX0000XXXX0000XXXX0000'
        self.assertNotEqual(
            self.steamwebapi.key,
            STEAM_API_KEY,
            'The SteamWebAPI().key instance is the same as ' +
            'settings.STEAM_API_KEY is the same although it should have ' +
            'changed.',
        )

    def test_api_key_initialized_from__init__with_keyword_arg(self):
        """Tests that initializing SteamWebAPI with the keyword argument 'key'
        creates a SteamWebAPI().key instance attribute which equals the
        keyword argument. This prevents regression of changing the name of the
        argument.

        """
        self.steamwebapi = SteamWebAPI(key='XXXX0000XXXX0000XXXX0000XXXX0000')
        self.assertEqual(
            self.steamwebapi.key,
            'XXXX0000XXXX0000XXXX0000XXXX0000',
            'The SteamWebAPI().key is not equal to the keyword argument.',
        )

    def test_api_key_initialized_from__init__no_keyword_arg(self):
        """Tests that initializing SteamWebAPI without the keyword argument
        'key' creates a SteamWebAPI().key instance attribute which equals the
        keyword argument. This ensures that we do not alter the argument order
        causing a regression for users that do not provide keyword arguments.

        """
        # Set a fake (bad) Steam Web API Key
        self.steamwebapi = SteamWebAPI('XXXX0000XXXX0000XXXX0000XXXX0000')
        self.assertEqual(
            self.steamwebapi.key,
            'XXXX0000XXXX0000XXXX0000XXXX0000',
            'The SteamWebAPI().key was not set when provided as the first ' +
            'argument without being a keyword argument.',
        )

    def test_api_key_invalid_28_alphanumeric_characters(self):
        """Tests initializing SteamWebAPI with an invalid Steam Web API Key.
        The Steam Web API Key should be 32 alphanumeric characters long. We
        will test by passing in 28 alphanumeric characters.

        """
        with self.assertRaises(APIKeyInvalidError):
            # Send a 28 instead of 32 character API key
            self.steamwebapi = SteamWebAPI('XXXX0000XXXX0000XXXX0000XXXX')

    def test_api_key_invalid_non_alphanumeric_character(self):
        """Tests initializing SteamWebAPI with an invalid Steam Web API Key.
        The Steam Web API Key should be 32 alphanumeric characters long. We
        will test by passing in a non-alphanumeric character.

        """
        with self.assertRaises(APIKeyInvalidError):
            # Add a "." (non-alphanumeric character)
            self.steamwebapi = SteamWebAPI('XXXX0000XXXX0000XXXX.000XXXX0000')

    def test_api_key_empty(self):
        """Tests initializing SteamWebAPI with an empty string as the Steam Web
        API Key. Ensures that the ./steamwebapi/core.API_KEY_RE does not raise
        the APIKeyInvalidError.

        """
        self.steamwebapi = SteamWebAPI(key='')
        self.assertEqual(
            self.steamwebapi.key,
            '',
            'The SteamWebAPI().key was initialized as an empty string, but ' +
            'not allowed.',
        )

    # -------------------------------------------------------------------------
    # Default Language Tests
    # -------------------------------------------------------------------------
    def test_default_language_equalto_settings_default_language(self):
        """Tests that initializing SteamWebAPI without arguments retrieves
        the DEFAULT_LANGUAGE from ./steamwebapi/settings.py.

        """
        self.assertEqual(
            self.steamwebapi.language,
            DEFAULT_LANGUAGE,
            'The settings.DEFAULT_LANGUAGE was not initialized as the ' +
            'default argument for SteamWebAPI().language.',
        )

    def test_default_language_not_equalto_settings_default_language(self):
        """Tests that changing the default language from within the SteamWebAPI
        instance works, as well as ensure that it differs from the
        DEFAULT_LANGUAGE from ./steamwebapi/settings.py.

        """
        self.steamwebapi.language = 'not_a_real_language'
        self.assertNotEqual(
            self.steamwebapi.language,
            DEFAULT_LANGUAGE,
            'The SteamWebAPI().language instance is the same as ' +
            'settings.DEFAULT_LANGUAGE is the same although it should have ' +
            'changed.',
        )

    def test_default_language_initialized_from__init__with_keyword_arg(self):
        """Tests that initializing SteamWebAPI with the keyword argument
        'language' creates a SteamWebAPI().language instance attribute which
        equals the keyword argument. This prevents regression of changing the
        name of the argument.

        """
        # Set a fake (bad) Steam Web API Key
        self.steamwebapi = SteamWebAPI(language='not_a_real_language')
        self.assertEqual(
            self.steamwebapi.language,
            'not_a_real_language',
            'The SteamWebAPI().language is not equal to the keyword argument.',
        )

    def test_default_language_initialized_from__init__no_keyword_arg(self):
        """Tests that initializing SteamWebAPI without the keyword argument
        'language' creates a SteamWebAPI().language instance attribute which
        equals the keyword argument. This ensures that we do not alter the
        argument order causing a regression for users that do not provide
        keyword arguments.

        """
        # Set a fake (bad) Steam Web API Key
        self.steamwebapi = SteamWebAPI(
            'XXXX0000XXXX0000XXXX0000XXXX0000',
            'not_a_real_language',
        )
        self.assertEqual(
            self.steamwebapi.language,
            'not_a_real_language',
            'The language was not set when provided as the second argument ' +
            'without being a keyword argument.',
        )


class TestAPIQuery(TestCase):
    """Tests the core.APIQuery() class to ensure the correct content-type is
    returned. We utilize ISteamWebAPIUtil().GetSupportedAPIList() as it
    does not require a key or arguments, and should always be available.

    """

    def setUp(self):
        """Initializes an APIQuery instance."""
        self.apiquery = APIQuery(
            interface='ISteamWebAPIUtil',
            method='GetSupportedAPIList',
            method_version=1,
            httpmethod='GET',
            parameters={},
        )

    def test_api_query_return_xml(self):
        """Tests that calling the XML format returns the correct
        content-type.

        """
        self.assertEqual(
            self.apiquery.xml.headers['content-type'],
            'text/xml; charset=UTF-8',
            'The content-type headers returned do not match the XML type.',
        )

    def test_api_query_return_json(self):
        """Tests that calling the JSON format returns the correct
        content-type.

        """
        self.assertEqual(
            self.apiquery.json.headers['content-type'],
            'application/json; charset=UTF-8',
            'The content-type headers returned do not match the JSON type.',
        )

    def test_api_query_return_vdf(self):
        """Tests that calling the VDF format returns the correct
        content-type.

        """
        self.assertEqual(
            self.apiquery.vdf.headers['content-type'],
            'text/vdf; charset=UTF-8',
            'The content-type headers returned do not match the VDF type.',
        )


# =============================================================================
# >> TEST FUNCTIONS
# =============================================================================
if __name__ == '__main__':
    main()
