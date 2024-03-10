import sys
import os
from src.logger import logging

def error_message_detaills(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    error_message = f"Error_occured in python script name [{file_name}] line number [{line_no}] error message [{error}]"
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message_detaills(error_message,error_details=error_details)
        super().__init__(self.error_message)

        



