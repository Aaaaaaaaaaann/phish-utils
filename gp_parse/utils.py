from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Data is from a test account.
search_service_url = getenv('SEARCH_SERVICE_URL')
