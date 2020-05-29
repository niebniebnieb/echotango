import os
from ftplib import FTP

savos = "/Users/thomasnieborowski/Desktop/SAVOS/"
remote_img1 = 'public_html/sebartsvirtual/wp-content/uploads/img'

mode = 'ADD'
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

with open(os.path.join(savos, "savospw"), "r") as f1:
    pw = f1.read().split(',')

print('pw0:>'+pw[0]+'<')
print('pw1:>'+pw[1]+'<')
print('pw2:>'+pw[2]+'<');
pass1 = pw[2].replace('\n', '');

ftp = FTP(pw[0], pw[1], pass1)
ftp.cwd(remote_img1)
files = ftp.nlst()

# save originally artist supplied files from previous run.
# for save in os.listdir(in_dir):
#     local_filename = os.path.join(in_dir, save)
#     os.rename(local_filename, os.path.join(save_dir, save) )

for f in files:
    print(" f: "+f)
    if f == '.' or f == '..':
        continue
    # localf = os.path.join(in_dir, f)
    # with open(localf, 'wb') as ff:
    #     ftp.retrbinary('RETR '+f, ff.write)
    # ftp.delete(os.path.join(remote_img2, f))
    ftp.sendcmd('DELE '+f)
ftp.quit()
