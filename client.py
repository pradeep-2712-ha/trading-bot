import time
import hmac
import hashlib
import logging
import requests
from urllib.parse import urlencode

logger = logging.getLogger(__name__)

BASE_URL = "https://testnet.binancefuture.com"


class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret.encode("utf-8")

        self.session = requests.Session()
        self.session.headers.update({
            "X-MBX-APIKEY": self.api_key
        })

    # -------------------------
    # Server time sync
    # -------------------------
    def _get_server_time(self) -> int:
        """
        Get Binance Futures server time to avoid timestamp drift
        """
        url = BASE_URL + "/fapi/v1/time"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()["serverTime"]

    # -------------------------
    # Sign request parameters
    # -------------------------
    def _sign_params(self, params: dict) -> dict:
        query_string = urlencode(params)
        signature = hmac.new(
            self.api_secret,
            query_string.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

        params["signature"] = signature
        return params

    # -------------------------
    # Low-level request handler
    # -------------------------
    def _request(self, method: str, path: str, params: dict):
        # Sync timestamp with Binance server
        params["timestamp"] = self._get_server_time()
        params["recvWindow"] = 5000

        signed_params = self._sign_params(params)

        url = BASE_URL + path
        logger.info(f"REQUEST {method} {url} {params}")

        response = self.session.request(
            method=method,
            url=url,
            params=signed_params,
            timeout=10
        )

        logger.info(f"RESPONSE {response.status_code} {response.text}")

        if not response.ok:
            raise Exception(response.text)

        return response.json()

    # -------------------------
    # Public order method
    # -------------------------
    def place_order(self, **order_params):
        """
        Place a Futures order (MARKET / LIMIT)
        """
        return self._request(
            method="POST",
            path="/fapi/v1/order",
            params=order_params
        )
