import os, subprocess
from PIL import Image, ExifTags
from pathlib import Path

for orientation in ExifTags.TAGS.keys():
    if ExifTags.TAGS[orientation]=='Orientation' : break 

family_members = ['kara', 'brendan', 'ellie']
for family_member in family_members:
    path = Path.home() / '.data' / 'images' / 'family' / family_member
    # path = Path.home() / '.data' / 'images' / 'family_test'

    for filename in os.listdir(path):
        if filename.lower().endswith(".heic"):
            old_filename, new_filename = filename, filename[0:-5] + '.jpg'
            old_filepath, new_filepath = path / old_filename, path / new_filename
            print(f'Converting {old_filename}...')
            subprocess.run(["heif-convert", old_filepath, new_filepath])
    
            image = Image.open(new_filepath)
            try:
                exif = dict(image._getexif().items())
            except AttributeError:
                print(f"\n\n***{new_filepath} has no EXIF dictionary\nCheck if proper rotation***\n\n")
            else:
                if exif[orientation] == 3 :
                    image=image.rotate(180, expand=True)
                elif exif[orientation] == 6 :
                    image=image.rotate(270, expand=True)
                elif exif[orientation] == 8: 
                    image=image.rotate(90, expand=True)
    
            image.save(new_filepath)
    
            os.remove(old_filepath)
    
