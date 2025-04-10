from PIL import Image
from utils.console.worker import *
from utils.qr.worker import *
    
def QuickShareOne():
    try:
        response, status = ConsoleText()

        if status != 200:
            raise Exception(response)
        
        print(response)
        
        image = Image.open("qrcode.png")
        image.show()

    except Exception as error:
        print(f"[QuickShareOne] Error: {error}", 500)

if __name__ == "__main__":
    QuickShareOne()
