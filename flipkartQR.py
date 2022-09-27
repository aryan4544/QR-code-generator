import pyqrcode
import png
from pyqrcode import QRCode

#assign website
s = "www.flipkart.com"


url = pyqrcode.create(s)

#saving as myqr.svg
url.svg("flipkartqr.svg",scale = 10)

#png
url.png("flipkartqr.png", scale = 10)