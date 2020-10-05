from imageio import *
from pathlib import Path

image_folder = Path('img')
images = list(image_folder.glob('*.jpg'))
image_list = []
for file_name in images:
    image_list.append(imread(file_name))

mimwrite('result.gif',image_list)
