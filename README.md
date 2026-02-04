# trading-bot
Binance Futures Testnet
setup steps 
--VERIFY THE PYHTON VERSION (python --version)
--CREATE A VIRTUAL ENVIRONMENT(python -m venv venv)
--ACTIVATE VIRTUAL ENVIRONMENT(venv\Scripts\activate)
--INSTALL THE REQUIREMENTS(-r pip install -r requirements.txt)
it installs--requests,urllib3,python-dotenv
-- CREATE ENV FILE (APIKEY,API_SECRET,KEY)
RUN SLI HELP (python cli.py --help)
-RUN MARKET ORDER COMMAND-
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.003
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.002 --price 60000
