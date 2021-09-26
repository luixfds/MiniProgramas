#   Gerando IMG do QRCode do link
import qrcode
from qrcode.image.pil import PilImage

features = qrcode.QRCode(version=1,box_size=40,border=3)

features.add_data('https://www.youtube.com/watch?v=qRFPGuBc-KE')
features.make(fit=True)

generate_image = features.make_image(fill_color="black", back_color="white")
generate_image.save('video.png')

generate_image.show()