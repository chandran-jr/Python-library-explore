from PIL import Image

image = Image.open("hulk.png")
width,height = image.size

print(width,height)
