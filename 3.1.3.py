from urllib.request import urlretrieve
from pathlib import Path

import xmltodict


file_name = "map1.osm"

url = f"https://stepik.org/media/attachments/lesson/245571/{file_name}"


if not Path(file_name).exists():
    urlretrieve(url, file_name)


with open(file_name, "r", encoding="utf-8") as f:
    xml = f.read()

parsedxml = xmltodict.parse(xml)
print(parsedxml["osm"]["node"][100]["@id"])
