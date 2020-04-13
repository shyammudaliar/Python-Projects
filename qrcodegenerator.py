
#QR code generator
import pyqrcode 
from pyqrcode import QRCode 
  
  
# Enter url/link which is to be converted into the QR code
qr = input("Enter the link or url of which you want to generate the qrcode for: ")
  
# Generating QR code 
url = pyqrcode.create(qr) 

#Enter name of the file with which you want to save it
name=input("Enter name of the qrcode file: ")
name=name+".svg"
  
# Create and save the file
url.svg(name, scale = 10) 

