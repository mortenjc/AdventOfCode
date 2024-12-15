import numpy as np
import matplotlib.pyplot as plt

#----Image Creation----#
# Set Image size ie. (height and width in pixels)
image_height = 200
image_width = 200

# Creating a black image using a NumPy array
my_image = np.zeros((image_height, image_width, 3), dtype=np.uint8)

# Show the black image using matplotlib
plt.imshow(my_image)
plt.axis('off')  # It helps when Turn off axes to remove the axis ticks and labels
plt.show()
