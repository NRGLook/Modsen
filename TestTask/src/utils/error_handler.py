import logging
from typing import Callable


def setup_logging(log_file: str = 'errors.log') -> None:
    """
    Configures logging to write errors to a specified log file.

    Parameters:
        log_file (str):
            The path to the log file. Default is 'errors.log'.

    Example:
    >>> setup_logging('my_errors.log')
    """
    logging.basicConfig(filename=log_file, level=logging.ERROR,
                        format='%(asctime)s:%(levelname)s:%(message)s')


def log_error(error: Exception, msg: str = "Error occurred") -> None:
    """
    Logs an error to the log file with a specified message.

    Parameters:
        error (Exception):
            The caught exception.
        msg (str):
            The message to log along with the error information.
            Default is "Error occurred".

    Example:
    >>> try:
    >>>     1 / 0
    >>> except Exception as e:
    >>>     log_error(e, "Division by zero")
    """
    logging.error(f"{msg}: {str(error)}")


def handle_image_error(func: Callable) -> Callable:
    """
    Decorator for handling exceptions when working with images.
    Logs the error and continues execution.

    Parameters:
        func (Callable):
            The function that might raise an exception.

    Returns:
        Callable:
            The function with error handling.

    Example:
    >>> @handle_image_error
    >>> def process_image(image):
    >>>     pass
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            log_error(e, f"Failed during {func.__name__}")
            return None
    return wrapper
