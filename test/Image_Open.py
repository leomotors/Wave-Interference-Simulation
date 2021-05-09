from PIL import Image

myimg = Image.open("/mnt/d/HP/Pictures/พี่คัทซึยะ.jpg")

myimg.show()

print(type(myimg))

myimg.save("./test.jpg")