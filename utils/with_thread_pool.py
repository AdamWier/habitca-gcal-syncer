from concurrent.futures import ThreadPoolExecutor


def with_thread_pool(number_of_max_workers):
    def decorator(func):
        def func_with_thread_pool(*args):
            with ThreadPoolExecutor(max_workers=number_of_max_workers) as pool:
                return tuple(pool.map(func, *args))

        return func_with_thread_pool

    return decorator
