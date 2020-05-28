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
    out_dir = "/Users/thomasnieborowski/Desktop/SAVOS/ADD_OUT_IMG"
else:
    in_dir = "/Users/thomasnieborowski/Desktop/SAVOS/IN_IMG"
    out_dir = "/Users/thomasnieborowski/Desktop/SAVOS/OUT_IMG"

QUALITY = 50
IM_SIZE = 800

for oldfile in os.scandir(out_dir):
    os.remove(oldfile.path)

for file in os.listdir(in_dir):
    org = os.path.join(in_dir, file)
    new_path = os.path.join(out_dir, file)
    if file.endswith('.jpeg'):
        newpath = new_path.replace('.jpeg', '.jpg')
        im = Image.open(org)
    elif file.endswith('.jpg'):
        im = Image.open(org)
        newpath = new_path
    elif file.endswith('.png'):
        newpath = new_path.replace('.png', '.jpg')
        im = Image.open(org)
        im = im.convert('RGB')
    elif file.endswith('.tif'):
        newpath = new_path.replace('.tif', '.jpg')
        im = Image.open(org)
        im = im.convert('RGB')
    elif file.endswith('.psd'):
        png = org.replace('.psd', '.png')
        os.system('psd-tools convert '+org+' '+png)
        newpath = new_path.replace('.psd', '.jpg')
        im = Image.open(png)
        im = im.convert('RGB')
        os.remove(png)
    else:
        print('ERROR: UNEXPECTED FILE EXTENSION: '+file)
        continue
    im.thumbnail((IM_SIZE, IM_SIZE))
    im.save(newpath, quality=QUALITY)
    print('CONVERTed '+org+' to '+newpath)

for fff in os.scandir(in_dir):
    os.remove(fff.path)
print('END')
