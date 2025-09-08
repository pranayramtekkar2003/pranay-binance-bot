import os
from binance.client import Client
from dotenv import load_dotenv
from .logger_setup import log

def binance_client():

    #Loading API keys from .env
    load_dotenv()

    api_key = os.getenv("API_KEY")
    api_secret_key = os.getenv("API_SECRET_KEY")

    #Handling api key issue
    if not api_key or not api_secret_key:
        log.error("API Key and Secret are not set. Check or create the .env file.")
        raise ValueError("API KEY/SECRET not found in .env file")
    
    client = Client(api_key, api_secret_key, testnet=True)
    log.info("Binance Client initalization successful.")

    return Client