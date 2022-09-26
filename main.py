import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import face


def block_mean(arr, yb=8, xb=8):
  new_shape = yb, xb
  new_arr = np.zeros(new_shape)
  block_size_y = arr.shape[0] // yb
  block_size_x = arr.shape[1] // xb
  y = 0
  x = 0
  for i in range(yb):
    stepy=0
    x=0
    for j in range(xb):
      ny = y // block_size_y
      nx = x // block_size_x
      stepy = int(ny<=yb-3)*block_size_y+int(ny>yb-3)*((arr.shape[0]-arr.shape[0]//yb*(yb-2))//2)
      stepx = int(nx<=xb-3)*block_size_x+int(nx>xb-3)*((arr.shape[1]-arr.shape[1]//xb*(xb-2))//2)
      new_arr[ny, nx] = np.mean(arr[y:y+stepy, x:x+stepx])
      x+=stepx
    y+=stepy
  return new_arr
  

img = face(gray=True)
plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.subplot(122)
arr = block_mean(img, 50, 40)
plt.imshow(arr, cmap="gray")
plt.show()
img.shape
