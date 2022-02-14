import sankaku

sankaku = sankaku.Client()

login = sankaku.login(email = "__email__", password = "__password__")
print(f"Logged in as '{sankaku.profile.name}'")