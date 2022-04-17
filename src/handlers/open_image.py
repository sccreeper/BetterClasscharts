from kivy.core.image import Image as KvCoreImage
from kivy.uix.image import Image as KvUIImage
from kivy.uix.screenmanager import RiseInTransition

import io
from base64 import b64decode
from PIL import Image

import globals

#Handler for displaying images in HW descs.

def open_image(uri):

    #Convert the image base64 so it can be used by Kivy.

    base64_uri = uri[1:-1].split(",")[1] + "=="
    base64_bytes = b64decode(base64_uri)

    
    data = io.BytesIO(base64_bytes)
    img = Image.open(data)

    display_data = io.BytesIO()
    img.save(display_data, format="png")

    display_data.seek(0)

    CI = KvCoreImage(io.BytesIO(display_data.read()), ext='png')

    UIImage = KvUIImage()

    UIImage.texture = CI.texture
    
    #Update the image data in the widget.

    globals.view_image_screen.image_data = UIImage.texture

    #Swap to the screen

    globals.screen_manager.transition = RiseInTransition(duration=0.25)
    globals.screen_manager.current = "ImageScreen"


