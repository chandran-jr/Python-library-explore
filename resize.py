from PIL import Image
image=Image.open('pic.png')
image = Image.open('pic.png')
width,height= image.size
image = image.resize(100,100)
image.save(" Required Folder path")
