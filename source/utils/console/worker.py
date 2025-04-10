from utils.qr.worker import *

def ConsoleText():
    try:
        print(
            "QuickShareOne - Console Text to QR Code Generator\n"
        )

        input_text = input("[QSO] Text -> ")
        
        response, status = GenerateQRCode(input_text)
        
        if status != 200:
            raise Exception(response)

        return "[QSO] QR Code generated successfully", 200

    except Exception as error:
        return f"[ConsoleText] Error: {error}", 500
