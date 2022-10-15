from PIL import Image

def ChSwap(r, g, b):
    return Image.merge("RGB", (b, r, g))

im = Image.open(r"image_processing\IMG_20201122_18185309.jpg")
r, g, b = im.split()

im.show()
new_rgb = ChSwap(r, g, b)

new_rgb.show()
