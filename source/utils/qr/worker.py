import qrcode

def GenerateQRCode(data):
    try:
        if data is None:
            return "No data provided"

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill="black", back_color="white")

        img.save("qrcode.png")

        return "qrcode.png", 200

    except Exception as error:
        return f"[GenerateQRCode] Error: {error}", 500
