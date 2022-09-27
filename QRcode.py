import pyqrcode
import png
from pyqrcode import QRCode

#assign website
s = "www.google.org"


url = pyqrcode.create(s)

#saving as myqr.svg
url.svg("yourqr.svg",scale = 10)

#png
url.png("yourqr.png", scale = 10)