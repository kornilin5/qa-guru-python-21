import os
from dotenv import load_dotenv

load_dotenv()
USER_APP = os.getenv('user')
PASSWORD_APP = os.getenv('key')
BROWSER_STACK_URL = os.getenv('url')
