class UserProfile:
    def __init__(self, data):
        self.json = data
        self.artist_update_count = None
        self.avatar_rating = None
        self.avatar_url = None
        self.comment_count = None
        self.created_at = None
        self.email = None
        self.email_verification_status = None
        self.enable_multi_factor_authentication = None
        self.favs_are_private = None
        self.filter_content = None
        self.forum_post_count = None
        self.hide_ads = None
        self.id = None
        self.is_verified = None
        self.last_logged_in_at = None
        self.level = None
        self.name = None
        self.note_update_count = None
        self.pool_update_count = None
        self.pool_upload_count = None
        self.post_update_count = None
        self.post_upload_count = None
        self.receive_dmails = None
        self.subscription_level = None
        self.wiki_update_count = None

    @property
    def UserProfile(self):
        try: self.artist_update_count = self.json["artist_update_count"]
        except (KeyError, TypeError): pass
        try: self.avatar_rating = self.json["avatar_rating"]
        except (KeyError, TypeError): pass
        try: self.avatar_url = self.json["avatar_url"]
        except (KeyError, TypeError): pass
        try: self.comment_count = self.json["comment_count"]
        except (KeyError, TypeError): pass
        try: self.created_at = self.json["created_at"]
        except (KeyError, TypeError): pass
        try: self.email = self.json["email"]
        except (KeyError, TypeError): pass
        try: self.email_verification_status = self.json["email_verification_status"]
        except (KeyError, TypeError): pass
        try: self.enable_multi_factor_authentication = self.json["enable_multi_factor_authentication"]
        except (KeyError, TypeError): pass
        try: self.favs_are_private = self.json["favs_are_private"]
        except (KeyError, TypeError): pass
        try: self.filter_content = self.json["filter_content"]
        except (KeyError, TypeError): pass
        try: self.forum_post_count = self.json["forum_post_count"]
        except (KeyError, TypeError): pass
        try: self.hide_ads = self.json["hide_ads"]
        except (KeyError, TypeError): pass
        try: self.id = self.json["id"]
        except (KeyError, TypeError): pass
        try: self.is_verified = self.json["is_verified"]
        except (KeyError, TypeError): pass
        try: self.last_logged_in_at = self.json["last_logged_in_at"]
        except (KeyError, TypeError): pass
        try: self.level = self.json["level"]
        except (KeyError, TypeError): pass
        try: self.name = self.json["name"]
        except (KeyError, TypeError): pass
        try: self.note_update_count = self.json["note_update_count"]
        except (KeyError, TypeError): pass
        try: self.pool_update_count = self.json["pool_update_count"]
        except (KeyError, TypeError): pass
        try: self.pool_upload_count = self.json["pool_upload_count"]
        except (KeyError, TypeError): pass
        try: self.post_update_count = self.json["post_update_count"]
        except (KeyError, TypeError): pass
        try: self.post_upload_count = self.json["post_upload_count"]
        except (KeyError, TypeError): pass
        try: self.receive_dmails = self.json["receive_dmails"]
        except (KeyError, TypeError): pass
        try: self.subscription_level = self.json["subscription_level"]
        except (KeyError, TypeError): pass
        try: self.wiki_update_count = self.json["wiki_update_count"]
        except (KeyError, TypeError): pass

        return self


class Posts:
    def __init__(self, data):
        self.json = data
        self.id = []
        self.rating = []
        self.status = []
        self.author = []
        self.sample_url = []
        self.sample_width = []
        self.sample_height = []
        self.preview_url = []
        self.preview_width = []
        self.preview_height = []
        self.file_url = []
        self.width = []
        self.height = []
        self.file_size = []
        self.file_type = []
        self.created_at = []
        self.has_children = []
        self.has_comments = []
        self.has_notes = []
        self.is_favorited = []
        self.user_vote = []
        self.md5 = []
        self.parent_id = []
        self.change = []
        self.fav_count = []
        self.recommended_posts = []
        self.recommended_score = []
        self.vote_count = []
        self.total_score = []
        self.comment_count = []
        self.source = []
        self.in_visible_pool = []
        self.is_premium = []
        self.is_rating_locked = []
        self.is_note_locked = []
        self.is_status_locked = []
        self.redirect_to_signup = []
        self.sequence = []
        self.tags = []

    @property
    def Posts(self):
        for item in self.json:
            try: self.id.append(item["id"])
            except (KeyError, TypeError): self.id.append(None)
            try: self.rating.append(item["rating"])
            except (KeyError, TypeError): self.rating.append(None)
            try: self.status.append(item["status"])
            except (KeyError, TypeError): self.status.append(None)
            try: self.author.append(item["author"])
            except (KeyError, TypeError): self.author.append(None)
            try: self.sample_url.append(item["sample_url"])
            except (KeyError, TypeError): self.sample_url.append(None)
            try: self.sample_width.append(item["sample_width"])
            except (KeyError, TypeError): self.sample_width.append(None)
            try: self.sample_height.append(item["sample_height"])
            except (KeyError, TypeError): self.sample_height.append(None)
            try: self.preview_url.append(item["preview_url"])
            except (KeyError, TypeError): self.preview_url.append(None)
            try: self.preview_width.append(item["preview_width"])
            except (KeyError, TypeError): self.preview_width.append(None)
            try: self.preview_height.append(item["preview_height"])
            except (KeyError, TypeError): self.preview_height.append(None)
            try: self.file_url.append(item["file_url"])
            except (KeyError, TypeError): self.file_url.append(None)
            try: self.width.append(item["width"])
            except (KeyError, TypeError): self.width.append(None)
            try: self.height.append(item["height"])
            except (KeyError, TypeError): self.height.append(None)
            try: self.file_size.append(item["file_size"])
            except (KeyError, TypeError): self.file_size.append(None)
            try: self.file_type.append(item["file_type"])
            except (KeyError, TypeError): self.file_type.append(None)
            try: self.created_at.append(item["created_at"])
            except (KeyError, TypeError): self.created_at.append(None)
            try: self.has_children.append(item["has_children"])
            except (KeyError, TypeError): self.has_children.append(None)
            try: self.has_comments.append(item["has_comments"])
            except (KeyError, TypeError): self.has_comments.append(None)
            try: self.has_notes.append(item["has_notes"])
            except (KeyError, TypeError): self.has_notes.append(None)
            try: self.is_favorited.append(item["is_favorited"])
            except (KeyError, TypeError): self.is_favorited.append(None)
            try: self.user_vote.append(item["user_vote"])
            except (KeyError, TypeError): self.user_vote.append(None)
            try: self.md5.append(item["md5"])
            except (KeyError, TypeError): self.md5.append(None)
            try: self.parent_id.append(item["parent_id"])
            except (KeyError, TypeError): self.parent_id.append(None)
            try: self.change.append(item["change"])
            except (KeyError, TypeError): self.change.append(None)
            try: self.fav_count.append(item["fav_count"])
            except (KeyError, TypeError): self.fav_count.append(None)
            try: self.recommended_posts.append(item["recommended_posts"])
            except (KeyError, TypeError): self.recommended_posts.append(None)
            try: self.recommended_score.append(item["recommended_score"])
            except (KeyError, TypeError): self.recommended_score.append(None)
            try: self.vote_count.append(item["vote_count"])
            except (KeyError, TypeError): self.vote_count.append(None)
            try: self.total_score.append(item["total_score"])
            except (KeyError, TypeError): self.total_score.append(None)
            try: self.comment_count.append(item["comment_count"])
            except (KeyError, TypeError): self.comment_count.append(None)
            try: self.source.append(item["source"])
            except (KeyError, TypeError): self.source.append(None)
            try: self.in_visible_pool.append(item["in_visible_pool"])
            except (KeyError, TypeError): self.in_visible_pool.append(None)
            try: self.is_premium.append(item["is_premium"])
            except (KeyError, TypeError): self.is_premium.append(None)
            try: self.is_rating_locked.append(item["is_rating_locked"])
            except (KeyError, TypeError): self.is_rating_locked.append(None)
            try: self.is_note_locked.append(item["is_note_locked"])
            except (KeyError, TypeError): self.is_note_locked.append(None)
            try: self.is_status_locked.append(item["is_status_locked"])
            except (KeyError, TypeError): self.is_status_locked.append(None)
            try: self.redirect_to_signup.append(item["redirect_to_signup"])
            except (KeyError, TypeError): self.redirect_to_signup.append(None)
            try: self.sequence.append(item["sequence"])
            except (KeyError, TypeError): self.sequence.append(None)
            try: self.tags.append(Tags(item["tags"]).Tags)
            except (KeyError, TypeError): self.tags.append(Tags([]).Tags)

        return self


class PostsTags:
    def __init__(self, data):
        self.json = data
        self.id = []
        self.name = []
        self.name_en = []
        self.name_ja = []
        self.type = []
        self.count = []
        self.post_count = []
        self.pool_count = []
        self.tagName = []

    @property
    def PostsTags(self):
        for item in self.json:
            try: self.id.append(item["id"])
            except (KeyError, TypeError): self.id.append(None)
            try: self.name.append(item["name"])
            except (KeyError, TypeError): self.name.append(None)
            try: self.name_en.append(item["name_en"])
            except (KeyError, TypeError): self.name_en.append(None)
            try: self.name_ja.append(item["name_ja"])
            except (KeyError, TypeError): self.name_ja.append(None)
            try: self.type.append(item["type"])
            except (KeyError, TypeError): self.type.append(None)
            try: self.count.append(item["count"])
            except (KeyError, TypeError): self.count.append(None)
            try: self.post_count.append(item["post_count"])
            except (KeyError, TypeError): self.post_count.append(None)
            try: self.pool_count.append(item["pool_count"])
            except (KeyError, TypeError): self.pool_count.append(None)
            try: self.tagName.append(item["tagName"])
            except (KeyError, TypeError): self.tagName.append(None)

        return self


class Tags:
    def __init__(self, data):
        self.json = data
        self.count = []
        self.id = []
        self.locale = []
        self.name = []
        self.name_en = []
        self.name_ja = []
        self.pool_count = []
        self.post_count = []
        self.rating = []
        self.tagName = []
        self.type = []
        self.version = []

    @property
    def Tags(self):
        for item in self.json:
            try: self.count.append(item["count"])
            except (KeyError, TypeError): self.count.append(None)
            try: self.id.append(item["id"])
            except (KeyError, TypeError): self.id.append(None)
            try: self.locale.append(item["locale"])
            except (KeyError, TypeError): self.locale.append(None)
            try: self.name.append(item["name"])
            except (KeyError, TypeError): self.name.append(None)
            try: self.name_en.append(item["name_en"])
            except (KeyError, TypeError): self.name_en.append(None)
            try: self.name_ja.append(item["name_ja"])
            except (KeyError, TypeError): self.name_ja.append(None)
            try: self.pool_count.append(item["pool_count"])
            except (KeyError, TypeError): self.pool_count.append(None)
            try: self.post_count.append(item["post_count"])
            except (KeyError, TypeError): self.post_count.append(None)
            try: self.rating.append(item["rating"])
            except (KeyError, TypeError): self.rating.append(None)
            try: self.tagName.append(item["tagName"])
            except (KeyError, TypeError): self.tagName.append(None)
            try: self.type.append(item["type"])
            except (KeyError, TypeError): self.type.append(None)
            try: self.version.append(item["version"])
            except (KeyError, TypeError): self.version.append(None)

        return self
