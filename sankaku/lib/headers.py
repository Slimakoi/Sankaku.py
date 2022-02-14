import base64

class Headers:
    def __init__(self, authorization = None):
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 7.1.2; SM-G973N Build/PPR1.190810.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36",
            "content-type": "application/json",
            "x-requested-with": "com.android.browser",
            "accept-encoding": "gzip, deflate"
        }

        if authorization:
            headers["authorization"] = f"Bearer {authorization}"

        self.headers = headers