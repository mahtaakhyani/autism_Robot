import numpy as np
import cv2

# Read an image frame
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
try:
    from PIL import Image
except ImportError:
    import Image

def gridding(image, dpi=100, interval=40):
    print("I'm in the grid!")
    my_dpi=dpi

    # Set up figure
    fig=plt.figure(figsize=(float(image.shape[0])/my_dpi,float(image.shape[1])/my_dpi),dpi=my_dpi)
    ax=fig.add_subplot(111)

    # Remove whitespace from around the image
    # fig.subplots_adjust(left=0,right=1,bottom=0,top=1)

    # Set the gridding interval: here we use the major tick interval
    myInterval=interval
    loc = plticker.MultipleLocator(base=myInterval)
    ax.xaxis.set_major_locator(loc)
    ax.yaxis.set_major_locator(loc)

    # Add the grid
    ax.grid(which='major', axis='both', linestyle='-', color='gray')
    
    # Add the image
    ax.imshow(image)
    
    # Find number of gridsquares in x and y direction
    nx=abs(int(float(ax.get_xlim()[1]-ax.get_xlim()[0])/float(myInterval)))
    ny=abs(int(float(ax.get_ylim()[1]-ax.get_ylim()[0])/float(myInterval)))

   
    # Save the figure
    fig.savefig('plotted.jpg')
    bin = cv2.imread('plotted.jpg')
    return (fig,bin)


def draw_grid(img, color=(0, 255, 0), thickness=1):
    starting_size = 20
    seq = 1
    seq_size = starting_size/seq
    h, w, _ = img.shape
    grid_shape = (int(h/seq_size),int(w/seq_size))
    rows, cols = grid_shape
    dy, dx = h / rows, w / cols

    # draw vertical lines
    for x in np.linspace(start=dx, stop=w-dx, num=cols-1):
        x = int(round(x))
        cv2.line(img, (x, 0), (x, h), color=color, thickness=thickness)

    # draw horizontal lines
    for y in np.linspace(start=dy, stop=h-dy, num=rows-1):
        y = int(round(y))
        cv2.line(img, (0, y), (w, y), color=color, thickness=thickness)


    return img


def analyse_pose(grided_img):
    pass