import os
from binance.client import Client
from dotenv import load_dotenv
from .logger_setup import log

def binance_client():

    #Loading API keys from .env
    load_dotenv()

    api_key = os.getenv("API_KEY")
    private_key = os.getenv("PRIVATE_KEY")

    #Handling api key issue
    if not api_key or not private_key:
        log.error("API Key and PRIVATE Key are not set. Check or create the .env file.")
        raise ValueError("API KEY/PRIVATE KEY not found in .env file")
    
    try:
        client = Client(api_key=api_key, private_key=private_key, testnet=True)
        log.info("Binance Client initialised successfully.")
        return client
    except Exception as e:
        log.error(f"Falied to initialise client. \n Error Message:{e}")