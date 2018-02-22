# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import os.path

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
picture = os.path.join(directory, 'Scarlett2.jpg')
# Read the image data into an array
img = plt.imread(picture)

height = len(img)
width = len(img[0])
for r in range(height):
    for c in range(width):
        if sum(img[r][c])<450: #3*255=765
            img[r][c]=[253,100,0]
            
'''Show the image data'''
# Create figure with 3 subplot
fig, ax = plt.subplots(1,1)
# Show the image data in a subplot
ax.imshow(img, interpolation='bicubic')
# Show the figure on the screen
fig.show()
fig.canvas.draw()
