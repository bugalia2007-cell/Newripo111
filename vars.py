import os
from os import environ

API_ID = int(environ.get("API_ID", "123"))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

OWNER = int(environ.get("OWNER", "0"))
CREDIT = environ.get("CREDIT", "Crystal")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER if user_id.strip().isdigit()]

AUTH_USER = os.environ.get('AUTH_USERS', '').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER if user_id.strip().isdigit()]
if OWNER != 0 and OWNER not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))

api_url = environ.get("API_URL", "")
api_token = environ.get("API_TOKEN", "")
token_cp = environ.get("TOKEN_CP", "")
adda_token = environ.get("ADDA_TOKEN", "")

photologo = environ.get("PHOTO_LOGO", "https://envs.sh/GVI.jpg")
photoyt = environ.get("PHOTO_YT", "https://envs.sh/GVI.jpg")
photocp = environ.get("PHOTO_CP", "https://envs.sh/GVI.jpg")
photozip = environ.get("PHOTO_ZIP", "https://envs.sh/GVI.jpg")
