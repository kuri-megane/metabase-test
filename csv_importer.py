import csv

import db_schema
import make_table


def import_db(input_file):
    with open(file=input_file, mode="r") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):

            print(i)

            tweet_id = int(row[0])
            created_at_str = row[1]
            created_at = row[2]
            tweet_text = row[3]

            if row[4] == "TRUE":
                truncated = True
            else:
                truncated = False

            entities_hashtags = row[5]
            entities_symbols = row[6]
            entities_user_mentions = row[7]
            entities_urls = row[8]

            iso_language_code = row[9]
            metadata_result_type = row[10]
            source = row[11]

            user_id = int(row[12])
            user_name = row[13]
            user_screen_name = row[14]
            user_location = row[15]
            user_description = row[16]
            user_url = row[17]

            if row[18] == "TRUE":
                user_protected = True
            else:
                user_protected = False

            user_followers_count = int(row[19])
            user_friends_count = int(row[20])
            user_listed_count = int(row[21])
            user_created_at_str = row[22]
            user_created_at = row[23]
            user_favourites_count = int(row[24])
            user_utc_offset = row[25]
            user_time_zone = row[26]
            user_geo_enabled = row[27]

            if row[28] == "TRUE":
                user_verified = True
            else:
                user_verified = False

            user_statuses_count = int(row[29])
            user_lang = row[30]

            search_metadata_completed_in = float(row[31])
            search_metadata_max_id = int(row[32])
            search_metadata_count = int(row[33])
            search_metadata_since_id = int(row[34])

            if row[35] == "o":
                check = True
                nl_score = float(row[36])
                nl_magnitude = float(row[37])
                nl_sentences_text_content = row[38]

                if row[39] == "":
                    nl_sentences_sentiment_magnitude = None
                else:
                    nl_sentences_sentiment_magnitude = float(row[39])

                if row[40] == "":
                    nl_sentences_sentiment_score = None
                else:
                    nl_sentences_sentiment_score = float(row[40])

            else:
                check = False
                nl_score = None
                nl_magnitude = None
                nl_sentences_text_content = ""
                nl_sentences_sentiment_magnitude = None
                nl_sentences_sentiment_score = None

            db_schema.Tweet.create(
                tweet_id=tweet_id,
                created_at_str=created_at_str,
                created_at=created_at,
                tweet_text=tweet_text,
                truncated=truncated,

                entities_hashtags=entities_hashtags,
                entities_symbols=entities_symbols,
                entities_user_mentions=entities_user_mentions,
                entities_urls=entities_urls,

                iso_language_code=iso_language_code,
                metadata_result_type=metadata_result_type,
                source=source,

                user_id=user_id,
                user_name=user_name,
                user_screen_name=user_screen_name,
                user_location=user_location,
                user_description=user_description,
                user_url=user_url,
                user_protected=user_protected,
                user_followers_count=user_followers_count,
                user_friends_count=user_friends_count,
                user_listed_count=user_listed_count,
                user_created_at_str=user_created_at_str,
                user_created_at=user_created_at,
                user_favourites_count=user_favourites_count,
                user_utc_offset=user_utc_offset,
                user_time_zone=user_time_zone,
                user_geo_enabled=user_geo_enabled,
                user_verified=user_verified,
                user_statuses_count=user_statuses_count,
                user_lang=user_lang,

                search_metadata_completed_in=search_metadata_completed_in,
                search_metadata_max_id=search_metadata_max_id,
                search_metadata_count=search_metadata_count,
                search_metadata_since_id=search_metadata_since_id,

                check=check,

                nl_score=nl_score,
                nl_magnitude=nl_magnitude,
                nl_sentences_text_content=nl_sentences_text_content,
                nl_sentences_sentiment_magnitude=nl_sentences_sentiment_magnitude,
                nl_sentences_sentiment_score=nl_sentences_sentiment_score
            )


if __name__ == '__main__':
    import_db("tweets.csv")
