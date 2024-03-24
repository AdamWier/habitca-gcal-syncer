def chunk_array(original_array, chunk_size):
    chunked_requests = []

    for i in range(0, len(original_array), chunk_size):
        chunk = original_array[i : i + chunk_size]
        chunked_requests.append(chunk)

    return chunked_requests
