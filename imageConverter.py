from PIL import Image

print("1. JPEG")
print("2. JPG")
print("3. PNG")
a = int(input("Choose image type to convert: "))
temp = {1:"jpeg",
        2:"jpg",
        3:"png"}

print("1. JPEG")
print("2. JPG")
print("3. PNG")

b = int(input("What do you want to convert " + temp[a] + " to: "))

aPath = input("path of the " + temp[a])

bPath = input("Where do you want to save the " + temp[b])

name = input("Name of the new image: ")

im = Image.open(aPath)
im.save(bPath + name + "." +temp[b])

print("DONE")