import sys
import os
from PIL import Image
from waveshare_epd import epd4in2_V2

try:
    epd = epd4in2_V2.EPD()
    epd.init()
    epd.Clear()

    Himage = Image.open('dog.jpg')

    Himage = Himage.resize((epd.width, epd.height))
    
    Himage = Himage.convert('1')

    epd.display(epd.getbuffer(Himage))
    epd.sleep()

except IOError as e:
    print(e)