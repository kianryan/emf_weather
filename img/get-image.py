import wget
from PIL import Image

icon_list = [
    '01', '02', '03', '04', '09', '10', '11', '13', '50'
]

cycle_list = [
    { 'cycle': 'd', 'fill_color': (117, 219, 239) },
    { 'cycle': 'n', 'fill_color': (40, 36, 148) }
]

size = 135, 120

for icon in icon_list:
    for cycle in cycle_list:
        filename = f'{icon}{cycle["cycle"]}'
        url = f'https://openweathermap.org/img/wn/{filename}@4x.png' #100x100
        print (filename)
        wget.download(url)

        # composite image, convert to jpg
        im = Image.open(f'{filename}@4x.png')
        im.thumbnail(size, Image.BILINEAR)
        background = Image.new(im.mode[:-1], size, cycle["fill_color"])
        background.paste(im, (7, 0), im) 

        background.convert("RGB").save(f'{filename}.jpg', quality=90)
