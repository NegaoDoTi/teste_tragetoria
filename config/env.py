from dotenv import load_dotenv
from os import getenv

load_dotenv()

EMAIL = getenv("EMAIL")
EMAIL_PASSWORD = getenv("EMAIL_PASSWORD")