import qrcode
from PIL import Image

data="https://auth.geeksforgeeks.org/user/awandbhjw"
qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2,
)
qr.add_data(data)
qr.make(fit=True)
qr_image=qr.make_image(fill_color="black",back_color="#ccfb96")
logo_path="C:\\Users\\user\\Desktop\\New folder\\qr_gen\\logo1.png"
logo=Image.open(logo_path)
qr_width,qr_height=qr_image.size
logo_width,logo_height=logo.size
position=((qr_width-logo_width)//2,(qr_height-logo_height)//2)
qr_image.paste(logo,position)
qr_image.save('GfG.png')
