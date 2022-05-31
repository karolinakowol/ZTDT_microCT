import tifffile as tiff
import numpy as numpy
from numpy import asarray, empty
from PIL import Image
import matplotlib.pyplot as plt


def calculate_Hounsfield_Units(pixel_value, water_value, air_value):
    return ((pixel_value - water_value)/(water_value - air_value)) * 1000

img_120 = tiff.imread('120kV.tif')
img_80 = tiff.imread('80kV.tif')

numpy_image_120 = asarray(img_120)
numpy_image_80 = asarray(img_80)

plt.imshow(numpy_image_120, cmap ='gray')
plt.title('120kV image', loc = 'center')
plt.show()

plt.imshow(numpy_image_80, cmap ='gray')
plt.title('80kV image', loc = 'center')
plt.show()

output_120 = numpy.empty(numpy_image_120.shape,dtype = int)
output_80 = numpy.empty(numpy_image_80.shape,dtype = int)

water_120 = 22200
air_120 = 8400

water_80 = 12660
air_80 = 7720


for i in range(numpy_image_120.shape[0]):
    for j in range(numpy_image_120.shape[1]):
        output_120[i,j] = calculate_Hounsfield_Units(numpy_image_120[i,j],water_120,air_120)

print(output_120)
plt.imshow(output_120, cmap ='gray')
plt.title('120kV image in HU ', loc = 'center')
plt.show()


for i in range(numpy_image_80.shape[0]):
    for j in range(numpy_image_80.shape[1]):
        output_80[i,j] = calculate_Hounsfield_Units(numpy_image_80[i,j],water_80,air_80)

print(output_120)
plt.imshow(output_80, cmap ='gray')
plt.title('80kV image in HU ', loc = 'center')
plt.show()


