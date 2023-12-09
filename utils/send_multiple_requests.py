import os
from concurrent.futures import ThreadPoolExecutor

import requests


def send_multiple_requests(request_information):
    HABITICA_USER_ID = os.getenv("HABITICA_USER_ID")
    HABITICA_API_KEY = os.getenv("HABITICA_API_KEY")

    def send_requests(request_information):
        request = getattr(requests, request_information.get("verb"))
        response = request(
            request_information.get("url"),
            headers={
                "x-api-user": HABITICA_USER_ID,
                "x-api-key": HABITICA_API_KEY,
            },
            json=request_information.get("params"),
        )

        return response

    with ThreadPoolExecutor(max_workers=3) as pool:
        return tuple(pool.map(send_requests, request_information))
