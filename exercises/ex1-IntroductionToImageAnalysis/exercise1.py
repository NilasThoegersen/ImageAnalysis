from skimage import color, io, measure, img_as_ubyte
from skimage.measure import profile_line
from skimage.transform import rescale, resize
import matplotlib.pyplot as plt
import numpy as np
import pydicom as dicom

# Directory containing data and images
in_dir = "data/"

# X-ray image
im_name = "metacarpals.png"

# Read the image.
# Here the directory and the image name is concatenated
# by "+" to give the full path to the image.
im_org = io.imread(in_dir + im_name)

print(im_org.shape)

print(im_org.dtype)

io.imshow(im_org)
plt.title('Metacarpal image')
io.show()

io.imshow(im_org, vmin=20, vmax=170)
plt.title('Metacarpal image (with gray level scaling)')
io.show()

count, edges, _ = plt.hist(im_org.ravel(), bins=256)


#Sets all pixels on y=30 to 0

im_org[:30] = 0
io.imshow(im_org)
io.show()

#Always scale to 400
im_custom = im_org = io.imread(in_dir + 'breakfast.png')

scale_test = rescale(im_custom, 0.3, anti_aliasing=True,
                         channel_axis=2)
print(im_custom.shape)
width, height, colors = im_custom.shape

image_rescaled = rescale(im_org, 400/width, anti_aliasing=True,
                         channel_axis=2)
print(image_rescaled.shape)

image_rescaled = rescale(scale_test, 400/scale_test.shape[0], anti_aliasing=True,
                         channel_axis=2)
print(image_rescaled.shape)
