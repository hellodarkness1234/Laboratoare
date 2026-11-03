print("\nB1")
def tip_real(cale):
    cap = open(cale, "rb").read(8)
    # TODO: daca cap incepe cu b"%PDF" -> "pdf"
    #       b"\x89PNG" -> "png" ; 
    #       b"\xff\xd8" -> "jpeg"
    #       b"PK\x03\x04" -> "zip/docx"
    if cap.startswith(b"\x89PNG"):
        print("PNG")
    if cap.startswith(b"\xff\xd8"):
        print("JPG")
    if cap.startswith(b"PK\x03\x04"):
        print("zip/docx")
    return cap.hex()
print(tip_real("probe/foto.jpg"))
print(tip_real("probe/ascuns.png"))


print("\nB2")
import re
date = open("probe/ascuns.png", "rb").read()
# TODO: for m in re.findall(rb"[ -~]{4,}", date):
#           print(m.decode())
# cauta un indiciu: o cale, un mesaj, un nume de fisier
for m in re.findall(rb"[ -~]{4,}", date):
    print(m.decode())

    #la print se afiseaza doua linii interesante
    #secret.txtFLAG{ascuns_prin_carving}
    #secret.txtPK

print("\nB3")
from PIL import Image
from PIL.ExifTags import TAGS
exif = Image.open("probe/foto.jpg")._getexif() or {}
for id, val in exif.items():
    if TAGS.get(id) == "GPSInfo":
        print("GPSInfo:\nLatitudinea:", val[1], val[2])
        print("\nLongitudinea:", val[3], val[4]) 
# print(TAGS.get(id, id), "=", val)
# TODO: ia blocul GPS (tag 34853) si tipareste
#       latitudinea si longitudinea


print("\B4")
date = open("probe/ascuns.png", "rb").read()
i = date.find(b"PK\x03\x04")
# TODO: daca i != -1:
#   open("gasit.zip","wb").write(date[i:])
#   print("arhiva extrasa de la octetul", i)
# apoi dezarhiveaza si vezi ce era inauntru
if i != -1:
    open("gasit.zip","wb").write(date[i:])
    print("arhiva extrasa de la octetul", i)

+     # inauntru la arhiva este un fisier secret.txt, in care era urmatorul text "FLAG{ascuns_prin_carving}"

print("\nB5")
from PIL import Image
img = Image.open("probe/foto.jpg").convert("RGB")
px = list(img.get_flattened_data())
mesaj = b"FLAG{ascuns_in_pixeli}"+b"\x00"
biti = "".join(f"{x:08b}" for x in mesaj)
px_nou = []
k = 0
for (r, g, b) in px:
    canale = [r, g, b]
    for c in range(3):
        if k < len(biti):
            canale[c] = (canale[c] & ~1) | int(biti[k])
            k += 1
    px_nou.append(tuple(canale))

img.putdata(px_nou)
img.save("stego.png")                 
print(biti)


print("\nB6")
from PIL import Image
px = list(Image.open("stego.png").convert("RGB").get_flattened_data())
biti = ""
for (r, g, b) in px:
    biti += str(r & 1) + str(g & 1) + str(b & 1)
octeti = bytearray()
for i in range(0, len(biti) - 7, 8):
    octet = int(biti[i:i+8], 2)
    if octet == 0:                 
        break
    octeti.append(octet)
print(octeti.decode("utf-8", errors="replace"))
