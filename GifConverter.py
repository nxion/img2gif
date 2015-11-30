from images2gif import writeGif
from PIL import Image
import os

# Recursively list iamge files and store them in a variable
imFiles = sorted((fn for fn in os.listdir('.') if fn.endswith('.png')))

# Grab the images and open them all for editing
images = [Image.open(fn) for fn in imFiles]

filename = "my_gif.GIF"
writeGif(filename, images, duration=0.2)
