import os
from ftplib import FTP
from PIL import Image
from psd_tools import PSDImage

savos = "/Users/thomasnieborowski/Desktop/SAVOS/"
remote_img = 'public_html/sebartsvirtual/wp-content/uploads/img'

mode = 'ADD' # ADD | TEST | BULK
if mode == 'TEST':
    in_dir = "./in_img"
    out_dir = "./out_img"
elif mode == 'ADD':
    in_dir = savos + "ADD_IN_IMG"
    out_dir = savos + "ADD_OUT_IMG"
else:
    in_dir = savos + "IN_IMG"
    out_dir = savos + "OUT_IMG"

save_dir = savos + "ORG_ADD_IN_IMG"

QUALITY = 50
IM_SIZE = 800

# save originally artist supplied files from previous run and clear in_dir.
for save in os.listdir(in_dir):
    local_filename = os.path.join(in_dir, save)
    os.rename(local_filename, os.path.join(save_dir, save) )

# FTP files to local
with open(os.path.join(savos, "savospw"), "r") as f1:
    pw = f1.read().replace('\n', '').split(',')

ftp = FTP(pw[0], pw[1], pw[2])
ftp.cwd(remote_img)
files = ftp.nlst()

for f2 in files:
    print(" f: "+f2)
    if f2 == '.' or f2 == '..':
        continue
    localf = os.path.join(in_dir, f2)
    with open(localf, 'wb') as f3:
        ftp.retrbinary('RETR '+f2, f3.write)

for f4 in files:
    if f4 == '.' or f4 == '..':
        continue
    ftp.delete(f4)
    # was sendcmd('DELE "+f4)

ftp.quit()


# Resize and compress files
for oldfile in os.scandir(out_dir):
    os.remove(oldfile.path)

for f4 in os.listdir(in_dir):
    org = os.path.join(in_dir, f4)
    new_path = os.path.join(out_dir, f4)
    if f4.endswith('.jpeg'):
        newpath = new_path.replace('.jpeg', '.jpg')
        im = Image.open(org)
    elif f4.endswith('.jpg'):
        im = Image.open(org)
        newpath = new_path
    elif f4.endswith('.png'):
        newpath = new_path.replace('.png', '.jpg')
        im = Image.open(org)
        im = im.convert('RGB')
    elif f4.endswith('.tif'):
        newpath = new_path.replace('.tif', '.jpg')
        im = Image.open(org)
        im = im.convert('RGB')
    elif f4.endswith('.psd'):
        png = org.replace('.psd', '.png')
        os.system('psd-tools convert '+org+' '+png)
        newpath = new_path.replace('.psd', '.jpg')
        im = Image.open(png)
        im = im.convert('RGB')
        os.remove(png)
    else:
        print('ERROR: UNEXPECTED FILE EXTENSION: ' + f4)
        continue
    im.thumbnail((IM_SIZE, IM_SIZE))
    im.save(newpath, quality=QUALITY)
    print('CONVERTed '+org+' to '+newpath)

print('END')
