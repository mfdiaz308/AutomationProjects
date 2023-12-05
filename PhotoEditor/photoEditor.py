from PIL import Image, ImageEnhance, ImageFilter
import os

# Create imgs (input) and editedImgs (output) folders
path = './PhotoEditor/imgs'
pathOut = './PhotoEditor/editedImgs'

for filename in os.listdir(path):
    img = Image.open(f'{path}/{filename}')
    
    # convert('L') makes it black and white
    edit = img.filter(ImageFilter.SHARPEN)

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    cleanName = os.path.splitext(filename)[0]

    edit.save(f'{pathOut}/{cleanName}_edited.jpg')
