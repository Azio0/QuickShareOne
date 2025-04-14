from termcolor import colored
from utils.qr.worker import *

def ConsoleText():
    try:
        print(
            colored("QuickShareOne - Console Text to QR Code Generator\n", "green")
        )

        input_text = input(f"{colored("[QSO]", "green")} Text -> ")
        
        response, status = GenerateQRCode(input_text)
        
        if status != 200:
            raise Exception(response)

        return f"{colored("[QSO]", "green")} QR Code generated successfully", 200

    except Exception as error:
        return f"{colored("[ConsoleText]", "red")} Error: {error}", 500
