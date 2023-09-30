
from os import getenv
from dotenv import load_dotenv

load_dotenv()


BOT_TOKEN = getenv("BOT_TOKEN", "6484534684:AAFhc381-zhXgXLXG9eNf37ED4DDafZc1yc")
SUPPORT = getenv("SUPPORT", "-1001571197486")
API_ID = int(getenv("API_ID", "17896688") or 0)
OWNER_ID = int(getenv("OWNER_ID", "1948147616") or 0)
SESSION = getenv("SESSION", "BQAP-GEAN2C9yKSEgpt8RQB52dUyVRgyRf5bBGN6EE8S5eTP_6xlNN-mL5jFtYa66vOTChBjwG2rUVjNkahfWiJHY_lMQGXriJ7OYoiT8rZSkvb5_2gfhaf5rn4ZPkMS6G4vGlst1uhyEqV6UOhdr0LmwRkKQs8k153I5sr96bhbIN5NYRTKXFaouRURKnSveBaQQWuMWpvG21WUtq5QsmqH8B93V_U_sAiaUNMa0hXJl2VyATCvIPuSeCqNreWwvUmpDzmZkzhv8ro-SNxkx2CEBR5SCooHKEjUdof_Rrt2mxwghl3AmmxeiNn5_P-WkmkQ_OZBIAqkJtYlGvG8PhkqtleEqQAAAAGEJxocAA")
OPENAI_API = getenv("OPENAI_API", "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")
API_HASH = getenv("API_HASH", "947327cf5ff0053a66bf7951f9db5658")
USERBOT_PREFIX = getenv("USERBOT_PREFIX", "!")
SUDO_USERS_ID = list(map(int, getenv("SUDO_USERS_ID", "1948147616").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001795374467") or 0)
WELCOME_DELAY_KICK_SEC = int(getenv("WELCOME_DELAY_KICK_SEC", "600"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://fadhil01:fadhil123@fadhil01.s6lkqsq.mongodb.net/?retryWrites=true&w=majority")
ARQ_API_KEY = getenv("ARQ_API_KEY", "PBXFMD-NWMWEN-FMFLQP-JBGTTF-ARQ")
ARQ_API_URL = getenv("ARQ_API_URL", "https://arq.hamker.in")
LOG_MENTIONS = getenv("LOG_MENTIONS", "False").lower() in ["true", "1"]
RSS_DELAY = int(getenv("RSS_DELAY", "300"))
PM_PERMIT = getenv("PM_PERMIT", "False").lower() in ["true", "1"]
