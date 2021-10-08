import re
import os
from pathlib import Path
from shutil import copyfile

imagesFolder = r'assets/'
modulesFolder = r'modules/'

for subdir in os.scandir(modulesFolder):
    newImagesFolder = os.path.join(subdir, "images")
    os.mkdir(newImagesFolder)
    if not subdir.is_file() and subdir != r'modules/.idea/':
        pagesFolder = os.path.join(subdir, "pages")
        for page in os.listdir(pagesFolder):
            dir = os.path.join(subdir, page)
            dir = Path(dir)
            if not dir.is_file():
                pagePath = os.path.join(subdir,"pages",page)
                if os.path.isfile(pagePath):
                    with open(pagePath, 'r') as currentPage:
                        for line in currentPage:
                            image = re.search('image::(.*)\[(.*)]', line)
                            if image:
                                print(image.group(1))

