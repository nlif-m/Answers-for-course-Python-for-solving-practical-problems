from urllib.request import urlretrieve
from pathlib import Path
import xml.etree.ElementTree as ET

file_name = "map2.osm"

url = f"https://stepik.org/media/attachments/lesson/245681/{file_name}"


if not Path(file_name).exists():
    urlretrieve(url, file_name)


tree = ET.parse(file_name)


fuels = 0
for node in tree.findall("node"):
    for tag in node.findall("tag"):
        if tag.get("v") == "fuel":
            fuels += 1
            break
print(fuels)
