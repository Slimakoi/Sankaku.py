import sankaku

sankaku = sankaku.Client()

login = sankaku.login(email = "__email__", password = "__password__")
print(f"Logged in as '{sankaku.profile.name}'")

posts = sankaku.get_posts_from_tag(tag = "femboy")
for postName, postId in zip(posts.name, posts.id):
    print(f"PostName : {postName}")
    print(f"PostId : {postId}")