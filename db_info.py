import os
import configparser
import peewee

# config.ini から設定値を読み込む
ini_file = configparser.ConfigParser()
ini_file.read_file(
    open("config.ini")
)

# # local保存の場合
# HOST = ini_file.get('db_local', 'HOST')
# DATABASE = ini_file.get('db_local', 'DATABASE')
# USER = ini_file.get('db_local', 'USER')
# PASSWD = ini_file.get('db_local', 'PASSWD')

# docker-compose 保存の場合
HOST = ini_file.get('db_docker', 'HOST')
DATABASE = ini_file.get('db_docker', 'DATABASE')
USER = ini_file.get('db_docker', 'USER')
PASSWD = ini_file.get('db_docker', 'PASSWD')

# データベース接続
db = peewee.MySQLDatabase(
    host=HOST,
    database=DATABASE,
    user=USER,
    password=PASSWD
)