from rich.progress import Progress, SpinnerColumn, TextColumn


def with_spinner(message):
    def decorator(func):
        def func_with_spinner(*args):
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                transient=True,
            ) as progress:
                progress.add_task(description=message, total=None)
                return func(*args)

        return func_with_spinner

    return decorator
