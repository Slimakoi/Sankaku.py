import requests
import json
import base64
import datetime
from sys import _getframe as getframe

from .lib import Headers, UserProfile, Posts, PostsTags

class Client:
    def __init__(self, debug: bool = False):
        self.debug = debug
        self.api = "https://capi-v2.sankakucomplex.com"
        self.login_api = "https://login.sankakucomplex.com"
        self.lang = "en"

        self.profile = UserProfile({}).UserProfile
        self.access_token = None
        self.refresh_token = None

    def _debug(self, function_name, status_code, message):
        if self.debug is True:
            print(f"[{datetime.datetime.now()}][{function_name}][{status_code}] {message}")

    def create_entry_query(self):
        data = "client_id=sankaku-android-app&" \
               "code_challenge=hbM4br0hZk6ZIUXwTiC5PIdsm1RtRidFtL2C8SdLArpUt1ZXZCQdB6804Nk5SbRb9LNj5fiP30ilO9Iqag4VCQBhkW25MuNhNRE4hEGIXoYmHLaMGrR2isOeCE9UXFEj&" \
               "code_challenge_method=plain&" \
               f"lang={self.lang}&" \
               "redirect_uri=app.sankaku.black%3A%2F%2Fsso%2Fcallback&" \
               "response_type=code&" \
               "scope=openid&" \
               "theme=black"

        return base64.b64encode(data.encode("utf-8")).decode("utf-8")

    def create_account(self, nickname: str, email: str, password: str):
        """
        Create an account on Sankaku

        :param nickname: Nickname of the account
        :param email: Email of the account
        :param password: Password of the account
        """
        data = json.dumps({
            "entry_query": self.create_entry_query(),
            "user": {
                "name": nickname,
                "password": password,
                "password_confirmation": password,
                "email": email
            },
            "lang": self.lang
        })

        response = requests.post(f"{self.login_api}/users", data=data, headers=Headers().headers)
        if response.status_code == 200:
            self._debug(getframe(0).f_code.co_name, response.status_code, response.json())
            return response.status_code
        else:
            self._debug(getframe(0).f_code.co_name, response.status_code, f"Error while Creating Account : {response.json()}")
            raise Exception(response.json())

    def get_mfa_state(self, email: str):
        """
        Get MFA state

        :param email: Email of the account
        """
        data = json.dumps({
            "login": email,
            "browserInfo": "Safari"
        })

        response = requests.post(f"{self.login_api}/user/mfa-state", data=data, headers=Headers().headers)
        if response.status_code == 200:
            self._debug(getframe(0).f_code.co_name, response.status_code, response.json())
            return response.json()
        else:
            self._debug(getframe(0).f_code.co_name, response.status_code, f"Error while getting MFA State : {response.json()}")
            raise Exception(response.json())

    def login(self, email: str, password: str):
        """
        Login on Sankaku

        :param email: Email of the account
        :param password: Password of the account
        """
        data = json.dumps({
            "login": email,
            "password": password
        })

        response = requests.post(f"{self.login_api}/auth/token", data=data, headers=Headers().headers)
        if response.status_code == 200:
            r = response.json()
            self._debug(getframe(0).f_code.co_name, response.status_code, r)

            # Saving the profile
            self.profile = UserProfile(r["current_user"]).UserProfile

            # Saving the tokens
            self.access_token = r["access_token"]
            self.refresh_token = r["refresh_token"]

            return response.status_code
        else:
            self._debug(getframe(0).f_code.co_name, response.status_code, f"Error while getting MFA State : {response.json()}")
            raise Exception(response.json())

    def get_profile(self):
        """
        Get account's profile info
        """
        response = requests.get(f"{self.login_api}/users/me", headers=Headers(self.access_token).headers)
        if response.status_code == 200:
            r = response.json()
            self._debug(getframe(0).f_code.co_name, response.status_code, r)
            return UserProfile(r["user"]).UserProfile
        else:
            self._debug(getframe(0).f_code.co_name, response.status_code, f"Error while getting Profile : {response.json()}")
            raise Exception(response.json())

    def get_posts(self, page: int = 0):
        """
        Get list of posts

        :param page: Number of the page
        """
        response = requests.get(f"{self.api}/posts?page={page}", headers=Headers().headers)
        if response.status_code == 200:
            r = response.json()
            self._debug(getframe(0).f_code.co_name, response.status_code, r)
            return Posts(r).Posts
        else:
            self._debug(getframe(0).f_code.co_name, response.status_code, f"Error while getting Profile : {response.json()}")
            raise Exception(response.json())

    def get_posts_from_tag(self, tag: str):
        """
        Get posts from tag

        :param tag: Tag for the search
        """
        response = requests.get(f"{self.api}/tags/autosuggest/v2?tag={tag}", headers=Headers().headers)
        if response.status_code == 200:
            r = response.json()
            self._debug(getframe(0).f_code.co_name, response.status_code, r)
            return PostsTags(r).PostsTags
        else:
            self._debug(getframe(0).f_code.co_name, response.status_code, f"Error while getting Suggestion from Tag : {response.json()}")
            raise Exception(response.json())


    # TODO :
    #  Get data from this request to add objects
    def get_post_comments(self, postId: int = 0):
        response = requests.get(f"{self.api}/posts/{postId}/comments", headers=Headers().headers)
        if response.status_code == 200:
            r = response.json()
            self._debug(getframe(0).f_code.co_name, response.status_code, r)
            return r
        else:
            self._debug(getframe(0).f_code.co_name, response.status_code, f"Error while getting Profile : {response.json()}")
            raise Exception(response.json())

    # TODO :
    #  No response, does it work?? (for GET)
    #  Fix this request, Error: snackbar__account_not-authorized
    def add_post_favorites(self, postId: int):
        response = requests.post(f"{self.api}/posts/{postId}/favorite", headers=Headers(self.access_token).headers)
        if response.status_code == 200:
            r = response.json()
            self._debug(getframe(0).f_code.co_name, response.status_code, r)
            return response.status_code
        else:
            self._debug(getframe(0).f_code.co_name, response.status_code, f"Error while Adding Post to Favorites : {response.json()}")
            raise Exception(response.json())

    # TODO :
    #  Get data from this request to add objects
    def get_post_notes(self, postId: int):
        response = requests.get(f"{self.api}/posts/{postId}/notes", headers=Headers().headers)
        if response.status_code == 200:
            r = response.json()
            self._debug(getframe(0).f_code.co_name, response.status_code, r)
            return r
        else:
            self._debug(getframe(0).f_code.co_name, response.status_code, f"Error while getting Post Notes : {response.json()}")
            raise Exception(response.json())

    # TODO :
    #  Fix this request, Error: snackbar__account_not-authorized
    def request_validation(self, email: str):
        data = json.dumps({
            "email": email
        })

        response = requests.post(f"{self.api}/auth/request-validation", data=data, headers=Headers().headers)
        if response.status_code == 200:
            r = response.json()
            self._debug(getframe(0).f_code.co_name, response.status_code, r)
            return r
        else:
            self._debug(getframe(0).f_code.co_name, response.status_code, f"Error while Requesting Validation : {response.json()}")
            raise Exception(response.json())

    # TODO :
    #  Fix this request, Error: snackbar__account_not-authorized
    def get_notification_settings(self):
        response = requests.get(f"{self.api}/notifications/settings", headers=Headers(self.access_token).headers)
        if response.status_code == 200:
            r = response.json()
            self._debug(getframe(0).f_code.co_name, response.status_code, r)
            return r
        else:
            self._debug(getframe(0).f_code.co_name, response.status_code, f"Error while getting Notification Settings : {response.json()}")
            raise Exception(response.json())
