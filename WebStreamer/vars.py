# This file is a part of TG-FileStreamBot

# Coding : Jyothis Jayanth [@EverythingSuckz]

import sys

from os import environ

from dotenv import load_dotenv

load_dotenv()

class Var(object):

    MULTI_CLIENT = "true"

    API_ID = 27885485

    API_HASH = "7dd9974c713787410beae4a295cc1e2d"

    BOT_TOKEN = "5814606535:AAHMKvgSMunxFpVqT8cu3icMnkux7H5bFlY"

    MULTI_TOKEN1="5730078829:AAHI7p5RrF-Sh6SbcWi9JzcRhpoqp3nPoUg"
    
    SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))  # 1 minte

    WORKERS = int(environ.get("WORKERS", "6"))  # 6 workers = 6 commands at once

    BIN_CHANNEL = -1001712664367

     # you NEED to use a CHANNEL when you're using MULTI_CLIENT

    PORT = int(environ.get("PORT", 8080))

    BIND_ADDRESS = str(environ.get("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))

    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes

    HAS_SSL = "true"

    NO_PORT = "true"

    HASH_LENGTH = int(environ.get("HASH_LENGTH", 6))

    if not 5 < HASH_LENGTH < 64:

        sys.exit("Hash length should be greater than 5 and less than 64")

    FQDN = "app-assistirvideos.koyeb.app"

    URL = "http{}://{}{}/".format(

            "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)

        )

    KEEP_ALIVE = str(environ.get("KEEP_ALIVE", "0").lower()) in  ("1", "true", "t", "yes", "y")

    DEBUG = str(environ.get("DEBUG", "0").lower()) in ("1", "true", "t", "yes", "y")

    USE_SESSION_FILE = str(environ.get("USE_SESSION_FILE", "0").lower()) in ("1", "true", "t", "yes", "y")

    ALLOWED_USERS = "6360808740, 6069809284, 6238111690, 5872654872"

