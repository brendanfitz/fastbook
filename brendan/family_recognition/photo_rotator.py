from PIL import Image, ExifTags
from pathlib import Path

for ORIENTATION in ExifTags.TAGS.keys():
    if ExifTags.TAGS[ORIENTATION] == 'Orientation':
        break

family_members = ['kara', 'brendan', 'ellie']
for family_member in family_members:
    path = Path.home() / '.data' / 'images' / 'family' / family_member
    for filepath in path.glob('*'):
        image = Image.open(filepath)
        exif = image._getexif()
        if exif is not None:
            try:
                orientation = dict(exif.items())[ORIENTATION]
                if orientation == 3:
                    image = image.rotate(180, expand=True)
                elif orientation == 6:
                    image = image.rotate(270, expand=True)
                elif orientation == 8:
                    image = image.rotate(90, expand=True)
                image.save(filepath)
            except KeyError:
                next
