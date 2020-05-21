import os
dirr = "/Users/thomasnieborowski/Desktop/SAVOS/IMAGE"
for file in os.listdir(dirr):
    org = os.path.join(dirr, file)
    ff = org.lower()
    ff = ff.replace('.jpg', '.jpeg')
    ff = ff.replace('1.', '-art.')
    ff = ff.replace('1.', '-art.')
    ff = ff.replace('--', '-')
    ff = ff.replace(',', '-')
    ff = ff.replace(' ', '-')
    ff = ff.replace('--', '-')
    ff = ff.replace('-pub.', '-head.')
    ff = ff.replace('-publicity.', '-head.')
    ff = ff.replace('.publicity.', '-head.')
    ff = ff.replace('publicity.', '-head.')
    ff = ff.replace('pub.', '-head.')
    ff = ff.replace('--', '-')
    ff = ff.replace('jpg.jpeg', '.jpeg')
    ff = ff.replace('jpeg.jpeg', '.jpeg')
    ff = ff.replace(' .', '.')
    ff = ff.replace('2.', '-art.')
    ff = ff.replace('1.', '-art.')
    ff = ff.replace('-.', '.')
    ff = ff.replace('2.', '-art.')
    ff = ff.replace('5.', '-art.')
    ff = ff.replace('9.', '-art.')
    ff = ff.replace('--', '-')
    ff = ff.replace('-new.jpeg', '.jpeg')
    ff = ff.replace('1new.jpeg', '-art.jpeg')
    ff = ff.replace('-1.', '-art.')
    ff = ff.replace('1.', '-art.')
    if not ('-art.' in ff or '-head' in ff):
        if ff.endswith('.jpeg'):
            ff = ff.replace('.jpeg', '-art.jpeg')
        if ff.endswith('.tif'):
            ff = ff.replace('.tif', '-art.tif')
        if ff.endswith('.psd'):
            ff = ff.replace('.psd', '-art.psd')
    os.rename(org, ff)
    print(ff)


# try:
#     os.rename(original, output)
# except WindowsError:
#     os.remove(output)
#     os.rename(original, output)


print('END')
