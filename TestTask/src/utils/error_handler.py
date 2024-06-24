import logging
from typing import Any


def setup_logging(log_file: str = 'errors.log') -> None:
    """
    Настраивает логгирование для записи ошибок в файл.

    Args:
    log_file (str): Путь к файлу лога.
    """
    logging.basicConfig(filename=log_file, level=logging.ERROR,
                        format='%(asctime)s:%(levelname)s:%(message)s')


def log_error(error: Exception, msg: str = "Error occurred") -> None:
    """
    Записывает ошибку в лог-файл с указанным сообщением.

    Args:
    error (Exception): Перехваченное исключение.
    msg (str): Сообщение для логирования вместе с информацией об ошибке.
    """
    logging.error(f"{msg}: {str(error)}")


def handle_image_error(func: Any) -> Any:
    """
    Декоратор для обработки исключений при работе с изображениями. Логирует ошибку и продолжает выполнение.

    Args:
    func (Callable): Функция, которая может вызвать исключение.

    Returns:
    Callable: Функция с обработкой ошибок.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            log_error(e, f"Failed during {func.__name__}")
            return None
    return wrapper
