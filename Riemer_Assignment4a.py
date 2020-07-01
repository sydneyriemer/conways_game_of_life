import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from matplotlib.animation import FuncAnimation

grid = np.random.randint(2, size=(500,500)) #creates 500x500 numpy array with random assortment of ones and zeros

kernel = np.array([[1,1,1], #computes the weighted sum of the eight neighbors (with weights=1)), excluding the target cell (weight=0)
                   [1,0,1],
                   [1,1,1]])

fig, ax = plt.subplots() #creates figure

def next_gen(arr):
    """
    This function applies Conway's rules and creates the next generation.
    """
    sum_of_neighbors = ndimage.convolve(grid, kernel, mode='constant') #computes the sum of the eight neighbors of each cell
    born = (sum_of_neighbors==3) & (grid==0) #rule if dead cell has 3 alive neighbors it becomes alive
    die = ((sum_of_neighbors<2) | (sum_of_neighbors>3)) & (grid==1) #rule if live cell does not have exactly 2 or 3 live neighbors it dies
    grid[born] = 1 #apply the rules to the grid
    grid[die] = 0
    ax.imshow(grid,cmap='viridis') #shows image of numpy array holding the state of the environment
    ax.grid(False)
    
animation = FuncAnimation(fig, next_gen, interval=10, frames=100) #animates the game
#plt.show()
animation.save('assignment4a.mpg', writer='ffmpeg')