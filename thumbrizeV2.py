
import base64
with open("/home/jerald/Pictures/one.jpg", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print(str)
    
#https://vision.googleapis.com/v1/images:annotate?key=AIzaSyBHjFtGpFX1b3ljX0MNXsD0o0qv3trd7Gw
#key = AIzaSyBHjFtGpFX1b3ljX0MNXsD0o0qv3trd7Gw
