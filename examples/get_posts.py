import sankaku

sankaku = sankaku.Client()

login = sankaku.login(email = "__email__", password = "__password__")
print(f"Logged in as '{sankaku.profile.name}'")

posts = sankaku.get_posts()
for postUrl, postId, postTags in zip(posts.sample_url, posts.id, posts.tags):
    print(f"PostUrl : {postUrl}")
    print(f"PostId : {postId}")
    print(f"PostTags : {', '.join(postTags.tagName)}")