import time
from format import formatResponse
from getResponse import getResponse
from image import imageSourcing
import os


def presentationContent(query, pages, max_num):
    c = 1
    f = formatResponse(getResponse(query, pages, max_num))
    while not f:
        if c > 5:
            print("Query cannot be fulfilled")
            exit()
        c += 1
        f = formatResponse(getResponse(query, pages, max_num))
    for num, slide in enumerate(f):
        imagePrompt = slide['Image']
        imageSourcing(imagePrompt)
        time.sleep(2)
        if os.path.exists(r'Images\000001.jpg'):
            os.rename(r'Images\000001.jpg', f'Images\\{num}.jpg')
            slide['Image'] = f'Images\\{num}.jpg'
        else:
            os.rename(r'Images\000001.png', f'Images\\{num}.png')
            slide['Image'] = f'Images\\{num}.png'
    return f
