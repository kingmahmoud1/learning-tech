import numpy as np
from PIL import Image
img=Image.open("test.png")
img_resized=img.resize((244,244))
img_gray=img_resized.convert("L")
img_array=np.array(img_gray)/255
img_gray.save("clean.png")
print(img_array.size)
print(img_array[:3,:3])
