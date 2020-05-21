import pandas as pd
from PIL import Image

# OK after conversion to ASCII:
artists = pd.read_csv('artists.csv')
print(artists)
image = Image.open('schaible-tim-1.jpg')
image.thumbnail((100, 100))
image.save('image_thumbnail.jpg')
for index, row in artists.iterrows():
    fst = row['First']
    if pd.isna(fst):
        fst = '-----'
    lst = row['Last']
    if pd.isna(lst):
        lst = '-----'
    print(fst, lst)
print('END')
