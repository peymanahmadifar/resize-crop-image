from PIL import Image


def calculate_image_size(w, h, base_w, base_h):
    base_aspect_ratio = base_w / base_h
    aspect_ratio = w / h
    if aspect_ratio <= base_aspect_ratio:
        new_w = base_w
        w_percent = (base_w / float(w))
        new_h = int((float(h) * float(w_percent)))
    else:
        new_h = base_h
        h_percent = (base_h / float(h))
        new_w = int((float(w) * float(h_percent)))
    return new_w, new_h


img = Image.open('a.jpg')

base_width = 480
base_height = 240

current_width = img.size[0]
current_height = img.size[1]

new_width, new_height = calculate_image_size(w, h, base_w, base_h)

img = img.resize((new_w, new_h), Image.ANTIALIAS)
img = img.crop((0, 0, base_w, base_h))
img.save('somepic.jpg')
