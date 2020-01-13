import peewee
import db_info


class Column:

    class Tweet:
        tweet_id = "TweetId"
        created_at_str = "CreatedAtStr"
        created_at = "CreatedAt"
        tweet_text = "TweetText"
        truncated = "Truncated"

        entities_hashtags = "Hashtags"
        entities_symbols = "Symbols"
        entities_user_mentions = "Mentions"
        entities_urls = "Urls"

        iso_language_code = "IsoLanguageCode"
        metadata_result_type = "ResultType"
        source = "source"

        user_id = "UserId"
        user_name = "UserName"
        user_screen_name = "UserScreenName"
        user_location = "UserLocation"
        user_description = "UserDescription"
        user_url = "UserUrl"
        user_protected = "UserProtected"
        user_followers_count = "UserFollowersCount"
        user_friends_count = "UserFriendsCount"
        user_listed_count = "UserListedCount"
        user_created_at_str = "UserCreatedAtStr"
        user_created_at = "UserCreatedAt"
        user_favourites_count = "UserFavouritesCount"
        user_utc_offset = "UserUtcOffset"       # deprecated
        user_time_zone = "UserTimeZone"         # deprecated
        user_geo_enabled = "UserGeoEnabled"     # deprecated
        user_verified = "UserVerified"
        user_statuses_count = "UserStatusesCount"
        user_lang = "UserLang"                  # deprecated

        search_metadata_completed_in = "CompletedIn"
        search_metadata_max_id = "MaxId"
        search_metadata_count = "Count"
        search_metadata_since_id = "SinceId"

        check = "Check"

        nl_score = "score"
        nl_magnitude = "magnitude"
        nl_sentences_text_content = "SentencesTextContent"
        nl_sentences_sentiment_magnitude = "SentencesMagnitude"
        nl_sentences_sentiment_score = "SentencesScore"


class BaseModel(peewee.Model):
    class Meta:
        database = db_info.db


class Tweet(BaseModel):

    tweet_id = peewee.BigIntegerField(
        db_column=Column.Tweet.tweet_id
    )
    created_at_str = peewee.FixedCharField(
        db_column=Column.Tweet.created_at_str,
        null=False,
    )
    created_at = peewee.DateTimeField(
        db_column=Column.Tweet.created_at,
        null=False,
        formats=[
            "%Y/%m/%d %H:%M:%S"
        ]
    )
    tweet_text = peewee.TextField(
        db_column=Column.Tweet.tweet_text,
        null=False,
    )
    truncated = peewee.BooleanField(
        db_column=Column.Tweet.truncated,
        null=False,
    )

    entities_hashtags = peewee.TextField(
        db_column=Column.Tweet.entities_hashtags,
        null=True,
    )
    entities_symbols = peewee.TextField(
        db_column=Column.Tweet.entities_symbols,
        null=True,
    )
    entities_user_mentions = peewee.TextField(
        db_column=Column.Tweet.entities_user_mentions,
        null=True,
    )
    entities_urls = peewee.TextField(
        db_column=Column.Tweet.entities_urls,
        null=True,
    )

    iso_language_code = peewee.FixedCharField(
        db_column=Column.Tweet.iso_language_code,
        null=False,
    )
    metadata_result_type = peewee.FixedCharField(
        db_column=Column.Tweet.metadata_result_type,
        null=False,
    )
    source = peewee.TextField(
        db_column=Column.Tweet.source,
        null=False,
    )

    user_id = peewee.BigIntegerField(
        db_column=Column.Tweet.user_id,
        null=False,
    )
    user_name = peewee.TextField(
        db_column=Column.Tweet.user_name,
        null=True,
    )
    user_screen_name = peewee.TextField(
        db_column=Column.Tweet.user_screen_name,
        null=True,
    )
    user_location = peewee.TextField(
        db_column=Column.Tweet.user_location,
        null=True,
    )
    user_description = peewee.TextField(
        db_column=Column.Tweet.user_description,
        null=True,
    )
    user_url = peewee.TextField(
        db_column=Column.Tweet.user_url,
        null=True,
    )
    user_protected = peewee.BooleanField(
        db_column=Column.Tweet.user_protected,
        null=False,
    )
    user_followers_count = peewee.IntegerField(
        db_column=Column.Tweet.user_followers_count,
        null=False,
    )
    user_friends_count = peewee.IntegerField(
        db_column=Column.Tweet.user_friends_count,
        null=False,
    )
    user_listed_count = peewee.IntegerField(
        db_column=Column.Tweet.user_listed_count,
        null=False,
    )
    user_created_at_str = peewee.FixedCharField(
        db_column=Column.Tweet.user_created_at_str,
        null=False,
    )
    user_created_at = peewee.DateTimeField(
        db_column=Column.Tweet.user_created_at,
        null=False,
        formats=[
            "%Y/%m/%d %H:%M:%S"
        ]
    )
    user_favourites_count = peewee.IntegerField(
        db_column=Column.Tweet.user_favourites_count,
        null=False,
    )
    # deprecated
    user_utc_offset = peewee.FixedCharField(
        db_column=Column.Tweet.user_utc_offset,
        null=True,
    )
    # deprecated
    user_time_zone = peewee.FixedCharField(
        db_column=Column.Tweet.user_time_zone,
        null=True,
    )
    # deprecated
    user_geo_enabled = peewee.FixedCharField(
        db_column=Column.Tweet.user_geo_enabled,
        null=True,
    )
    user_verified = peewee.BooleanField(
        db_column=Column.Tweet.user_verified,
        null=True,
    )
    user_statuses_count = peewee.IntegerField(
        db_column=Column.Tweet.user_statuses_count,
        null=True,
    )
    # deprecated
    user_lang = peewee.FixedCharField(
        db_column=Column.Tweet.user_lang,
        null=True,
    )

    search_metadata_completed_in = peewee.DoubleField(
        db_column=Column.Tweet.search_metadata_completed_in,
        null=False,
    )
    search_metadata_max_id = peewee.BigIntegerField(
        db_column=Column.Tweet.search_metadata_max_id,
        null=False,
    )
    search_metadata_count = peewee.IntegerField(
        db_column=Column.Tweet.search_metadata_count,
        null=False,
    )
    search_metadata_since_id = peewee.BigIntegerField(
        db_column=Column.Tweet.search_metadata_since_id,
        null=False,
    )

    check = peewee.BooleanField(
        db_column=Column.Tweet.check,
        null=False,
    )

    nl_score = peewee.DoubleField(
        db_column=Column.Tweet.nl_score,
        null=True,
    )
    nl_magnitude = peewee.DoubleField(
        db_column=Column.Tweet.nl_magnitude,
        null=True,
    )
    nl_sentences_text_content = peewee.TextField(
        db_column=Column.Tweet.nl_sentences_text_content,
        null=True,
    )
    nl_sentences_sentiment_magnitude = peewee.DoubleField(
        db_column=Column.Tweet.nl_sentences_sentiment_magnitude,
        null=True,
    )
    nl_sentences_sentiment_score = peewee.DoubleField(
        db_column=Column.Tweet.nl_sentences_sentiment_score,
        null=True,
    )

    # class Meta:
    #     primary_key = peewee.CompositeKey(
    #         'tweet_id',
    #     )
