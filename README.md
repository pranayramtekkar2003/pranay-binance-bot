
-----

# Binance Spot Trading Bot

This is a command-line interface (CLI) trading bot for the Binance Spot market. It provides a robust framework for placing various order types, from simple market orders to more complex strategies like TWAP and Grid trading.

The bot is built with a modular structure, features structured logging for all actions, and uses the secure Ed25519 key structure for API authentication.

-----

## Features

  * **Core Orders**: Place Market and Limit orders.
  * **Advanced Orders**: Execute Stop-Loss and OCO (One-Cancels-the-Other) orders.
  * **Secure Authentication**: Uses Ed25519 key pairs for improved API security.
  * **Structured Logging**: All actions, successful transactions, and errors are logged to `bot.log` with timestamps.
  * **Testnet Ready**: Designed to work with the Binance Spot Testnet for safe development and testing.

-----

## Project Structure

```
pranay-binance-bot/
├── src/
│   ├── __init__.py
│   ├── client.py
│   ├── logger_setup.py
│   ├── market_orders.py
│   ├── limit_orders.py
│   └── advanced/
│       ├── __init__.py
│       ├── stop_limit_order.py
│       ├── oco_order.py
├── .env
├── .gitignore
├── bot.log
├── README.md
└── requirements.txt
```

-----

## Setup and Installation

### 1\. Clone the Repository

First, clone this repository to your local machine.

```bash
git clone <your-repository-url>
cd pranay-binance-bot
```

### 2\. Create a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

  * **Windows:**
    ```cmd
    python -m venv venv
    venv\Scripts\activate
    ```
  * **macOS / Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

### 3\. Install Dependencies

Install the required Python packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4\. Configure API Keys (Ed25519)

This bot uses the more secure Ed25519 key system.

1.  **Generate Keys**: Log in to your Binance Spot Testnet . There click on the **`Register Public Key`** now give the public key to it 
and it will generate an API key with Ed25519 format.[To create the pair of private and public key you need to download the key generator from there log site]
2.  **Save Private Key**: Binance will provide you with an **API Key** and a **Private Key**. Create a file in the project's root directory named **`env`** and paste the entire private key block into it.
    ```pem
    # private_key

    -----BEGIN PRIVATE KEY-----
    [... a long string of random characters ...]
    -----END PRIVATE KEY-----
    ```
3.  **Create `.env` File**: Create a file named **`.env`** in the root directory and add your API Key and the path to your private key file.
    ```.env
    BINANCE_API_KEY="YOUR_API_KEY_HERE"
    BINANCE_PRIVATE_KEY="YOUR_PRIVATE_KEY"
    ```
4.  **Security**: Remember to add `.env` to your `.gitignore` file to prevent them from being committed to version control.

-----

## How to Run the Bot

All commands must be executed from the **root directory** of the project (`pranay-binance-bot`). The scripts must be run as modules using the `python -m` flag.

### Core Orders

  * **Market Order**
    ```cmd
    python -m src.market_orders BTCUSDT BUY 0.001
    ```
  * **Limit Order**
    ```cmd
    python -m src.limit_orders BTCUSDT SELL 0.001 50000
    ```

### Advanced Orders & Strategies

> **Note on Testnet Limitations**
> The Binance Spot Testnet is limited and does not support testing for advanced order types like `STOP_LOSS` or `OCO`. The code for these scripts uses the **production endpoints** (`client.create_order` and `client.create_oco_order`). Be aware that running these will place **REAL orders** if you use mainnet API keys.

  * **Stop-Loss Order**
    ```cmd
    python -m src.advanced.stop_limit BTCUSDT SELL 0.01 28000
    ```
  * **OCO (One-Cancels-the-Other) Order**
    ```cmd
    python -m src.advanced.oco BTCUSDT SELL 0.01 55000 48000 47950
    ```

-----


1.  **Open** the root folder in for this repository in you local machine.
2.  **Activate** the virtual environment with all the dependencies installed.
3.  **Run** the script as a module: `python -m src.market_orders` along with the additional parameters
4.  **Revert** your changes when finished(if made).