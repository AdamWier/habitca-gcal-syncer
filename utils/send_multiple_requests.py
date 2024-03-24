import os
from time import sleep

import requests

from .chunk_array import chunk_array
from .console import console
from .with_spinner import with_spinner
from .with_thread_pool import with_thread_pool

HABITICA_MAX_REQUESTS = 30 - 10


@with_spinner("Updating tasks...")
def send_multiple_requests(request_information):
    HABITICA_USER_ID = os.getenv("HABITICA_USER_ID")
    HABITICA_API_KEY = os.getenv("HABITICA_API_KEY")

    chunked_requests = chunk_array(request_information, HABITICA_MAX_REQUESTS)

    def send_chunked_requests(length):
        def _send_chunked_requests(input):
            index, chunk = input
            console.print(
                "Sending chunk [bold]{} of [bold]{}".format(index + 1, length)
            )
            results = send_requests(chunk)
            console.print("[green]Success")
            if index != length - 1:
                console.print("[yellow]Waiting sixty seconds to send next chunk")
                sleep(60)
            return results

        return _send_chunked_requests

    @with_thread_pool(HABITICA_MAX_REQUESTS)
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

    return list(
        map(
            send_chunked_requests(len(chunked_requests)),
            list(enumerate(chunked_requests)),
        )
    )
