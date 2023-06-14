from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./imgs"
pathOut = "./editedImgs"

for filename in os.listdir(path):
    if filename.endswith((".jpg", ".jpeg", ".png")):
        img = Image.open(f"{path}/{filename}")
        
        edit = img.filter(ImageFilter.SHARPEN).convert('L')
        
        # Contrast
        factor = 1.5
        enhancer = ImageEnhance.Contrast(edit)
        edit = enhancer.enhance(factor)

        # Add more edits from documentation: https://pillow.readthedocs.io/en/stable/

        clean_name = os.path.splitext(filename)[0]
        edit.save(f'{pathOut}/{clean_name}_edited.jpg')
