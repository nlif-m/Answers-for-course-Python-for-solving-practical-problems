from urllib.request import urlretrieve
from pathlib import Path
import xml.etree.ElementTree as ET

file_name = "map1.osm"

url = f"https://stepik.org/media/attachments/lesson/245678/{file_name}"


if not Path(file_name).exists():
    urlretrieve(url, file_name)


with_tag = 0
without_tag = 0
tree = ET.parse(file_name)

for node in tree.findall("node"):
    if node.findall("tag"):
        with_tag += 1
    else:
        without_tag += 1


print(with_tag, without_tag)
