# generating qr code

import qrcode

def generate_qrcode(text):

    qr = qrcode.qrcode(

        version = 1, 
        error_correction =  qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4
    )


    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_imagge(fiil_color="black", back_color="white")
    img.save("hello.png")

url = input('Enter your url: ')
generate_qrcode('hello world')