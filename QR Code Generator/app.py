import qrcode

def generate_qrcode(text):
    """
    Generate a QR code image from the provided text.

    Parameters:
        text (str): The text to encode into the QR code.

    Returns:
        None

    Saves:
        Generates a PNG image containing the QR code with the encoded text.

    Example:
        generate_qrcode("https://www.google.com")
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="Blue", back_color="turquoise")
    img.save('qrimg001.png')

# Example usage:
if __name__ == "__main__":
    url = input('Enter your URL: ')
    generate_qrcode(url)
