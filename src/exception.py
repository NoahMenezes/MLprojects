import sys


def error_message_detail(error, error_detail):
    """
    Extracts detailed error information from the exception traceback.

    Args:
        error: The exception object.
        error_detail: The result of sys.exc_info(), a tuple (type, value, traceback).

    Returns:
        str: A formatted error message with file name, line number, and error details.
    """
    _, _, exc_tb = error_detail
    if exc_tb is None:
        return f"Error: {str(error)}"

    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]"
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        """
        Custom exception class that provides detailed error messages.

        Args:
            error_message: The original error message.
            error_detail: The result of sys.exc_info().
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
