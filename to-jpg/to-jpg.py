import os
from ftplib import FTP
from PIL import Image
from psd_tools import PSDImage

mode = 'ADD'  # ADD | TEST | BULK
skipftp = False

QUALITY = 50
IM_SIZE = 800

savos = "/Users/thomasnieborowski/Desktop/SAVOS/IMG/"
remote_img = 'public_html/sebartsvirtual/wp-content/uploads/img'

if mode == 'TEST':
    in_dir = "./in_img"
    out_dir = "./out_img"
elif mode == 'ADD':
    in_dir = savos + "ADD_IN_IMG"
    out_dir = savos + "ADD_OUT_IMG"
else:
    in_dir = savos + "IN_IMG"
    out_dir = savos + "OUT_IMG"
save_dir = savos + "IN_IMG"
save_out_dir = savos + "SAVE_OUT_IMG"
print('Processing Images in Mode: ' + mode)
print('Skipping FTP: ' + str(skipftp))
print('Image Root Dir: ' + savos)
print('input dir: ' + in_dir)
print('output dir: ' + out_dir)
print('Input files saved in : ' + save_dir)
print('quality : ' + str(QUALITY))
print('Max Size : ' + str(IM_SIZE))

if not skipftp:
    # save originally artist supplied files from previous run.
    for save in os.listdir(in_dir):
        save_path = os.path.join(in_dir, save)
        os.rename(save_path, os.path.join(save_dir, save) )

    # FTP files to local
    with open(os.path.join(savos, "savospw"), "r") as f1:
        pw = f1.read().replace('\n', '').split(',')
    ftp = FTP(pw[0], pw[1], pw[2])
    ftp.cwd(remote_img)
    files = ftp.nlst()
    for f2 in files:
        if f2 == '.' or f2 == '..':
            continue
        localf = os.path.join(in_dir, f2)
        with open(localf, 'wb') as f3:
            ftp.retrbinary('RETR '+f2, f3.write)
    for f4 in files:
        if f4 == '.' or f4 == '..':
            continue
        ftp.delete(f4)
    ftp.quit()

# Resize and compress files
for f33 in os.listdir(in_dir):
    if f33 == '.DS_Store':
        continue
    f4 = f33.lower()
    org = os.path.join(in_dir, f4)
    newfile = f4.lower()
    print('CONVERTing '+f4)
    if f4.endswith('.jpeg'):
        newfile = newfile.replace('.jpeg', '.jpg')
        im = Image.open(org)
    elif f4.endswith('.jpg'):
        im = Image.open(org)
        newfile = newfile
    elif f4.endswith('.png'):
        newfile = newfile.replace('.png', '.jpg')
        im = Image.open(org)
        im = im.convert('RGB')
    elif f4.endswith('.tif'):
        newfile = newfile.replace('.tif', '.jpg')
        im = Image.open(org)
        im = im.convert('RGB')
    elif f4.endswith('.psd'):
        png = org.replace('.psd', '.png')
        os.system('psd-tools convert '+org+' '+png)
        newfile = newfile.replace('.psd', '.jpg')
        im = Image.open(png)
        im = im.convert('RGB')
        os.remove(png)
    else:
        print('ERROR: UNEXPECTED FILE EXTENSION: ' + f4)
        continue
    im.thumbnail((IM_SIZE, IM_SIZE))
    newpath = os.path.join(out_dir, newfile)
    im.save(newpath, quality=QUALITY)
    print('CONVERTed '+f4+' to '+newpath)

for save in os.listdir(out_dir):
    if save == '.DS_Store':
        continue
    save_path = os.path.join(out_dir, save)
    os.system('cp '+ save_path + ' ' + os.path.join(save_out_dir, save))

print('Now upload precessed Images to Media Library:')
print('Dashboard > Media > Add New > Select > ' + out_dir)
