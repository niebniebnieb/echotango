import os
from PIL import Image
from psd_tools import PSDImage

# OK after conversion to ASCII:
mode = 'ADD'
if mode == 'TEST':
    in_dir = "./in_img"
    out_dir = "./out_img"
elif mode == 'ADD':
    in_dir = "/Users/thomasnieborowski/Desktop/SAVOS/ADD_IN_IMG"
    out_dir = "/Users/thomasnieborowski/Desktop/SAVOS/OUT_IMG"
else:
    in_dir = "/Users/thomasnieborowski/Desktop/SAVOS/IN_IMG"
    out_dir = "/Users/thomasnieborowski/Desktop/SAVOS/OUT_IMG"

QUALITY = 50
IM_SIZE = 800

for file in os.listdir(in_dir):
    org = os.path.join(in_dir, file)
    new_path = os.path.join(out_dir, file)
    if file.endswith('.jpeg'):
        ff = new_path.replace('.jpeg', '.jpg')
        im = Image.open(org)
        im.thumbnail((IM_SIZE,IM_SIZE))
        im.save(ff, quality=QUALITY)
        continue
    if file.endswith('.jpg'):
        im = Image.open(org)
        im.thumbnail((IM_SIZE,IM_SIZE))
        im.save(new_path, quality=QUALITY)
        continue
    if file.endswith('.png'):
        ff = new_path.replace('.png', '.jpg')
        im = Image.open(org)
        im.thumbnail((IM_SIZE,IM_SIZE))
        im = im.convert('RGB')
        im.save(ff, quality=QUALITY)
        continue
    if file.endswith('.tif'):
        ff = new_path.replace('.tif', '.jpg')
        im = Image.open(org)
        im = im.convert('RGB')
        im.thumbnail((IM_SIZE,IM_SIZE))
        im.save(ff, "JPEG", quality=QUALITY)
        continue
    if file.endswith('.psd'):
        png = org.replace('.psd', '.png')
        os.system('psd-tools convert '+org+' '+png)
        ff = new_path.replace('.psd', '.jpg')
        im = Image.open(png)
        im = im.convert('RGB')
        im.thumbnail((IM_SIZE,IM_SIZE))
        im.save(ff, quality=QUALITY)
        os.remove(png)
        continue
print('END')
