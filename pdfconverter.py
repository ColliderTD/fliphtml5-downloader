import img2pdf
import argparse
import os

header = """
    ______________________
   |                      |
   | FlipHTML5 IMG -> PDF |
   |______________________|
   """
print(header)
parser = argparse.ArgumentParser()
parser.add_argument("folderName", help="The folder containing images to be converted into pdf")
parser.add_argument("start", help="Starting image number to be converted", type=int)
parser.add_argument("end", help="Last image number to be converted", type=int)
args = parser.parse_args()
folderName = args.folderName
start = args.start
end = args.end

print("Convirtiendo...")
images = []
for num in range(start, end+1):
    filepath = "{0}/{1}.jpg".format(folderName, num)
    with open(filepath, "rb") as image:
        images.append(image.read())

with open("{0}.pdf".format(folderName), "wb") as file:
    file.write(img2pdf.convert(images))

print("\rCompletado. Presiona cualquier boton para salir")
input()
