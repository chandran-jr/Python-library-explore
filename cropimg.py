from PIL import Image
image=Image.new('RGBA',(1200,1200),'blue')
image.save('blue.png')
croppedImage=image.crop((300,300,500,500))
croppedImage.save('cropped.png')
