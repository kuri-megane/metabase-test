import logging

import db_info
import db_schema

# 詳細ログを記録する場合
logger = logging.getLogger('peewee')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

db_info.db.connect()
db_info.db.create_tables(
    [
        db_schema.Tweet,
    ]
)
db_info.db.close()
