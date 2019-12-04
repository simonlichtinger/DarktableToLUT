"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


import numpy as np
import imageio
from sys import argv
from subprocess import call

# Create an image featuring all colours
def create_test_image(filename,size):
    f = np.zeros((int(size*np.sqrt(size)),int(size*np.sqrt(size)),3))
    for i in range(int(size*np.sqrt(size))):
        for j in range(int(size*np.sqrt(size))):
            f[i,j,0]= int((i%size)*256/size)
            f[i,j,1]= int((j%size)*256/size)
            f[i,j,2]= int((i-(i%size))/size*256/size+int(np.sqrt(size))*(j-(j%size))/size*256/size)
    imageio.imsave(filename, f)

# Read in a png image
def read_image(filename):
    return imageio.imread(filename)

# Create the cube file by reading in an image, and finding the appropriate datapoints to write to the cube format
def create_cube(filename,size):
    a=read_image(filename+".png")

    # Header as required by the cube format
    header = ["TITLE \""+filename+ "\"\n",
    "LUT_3D_SIZE "+str(size)+"\n",
    "DOMAIN_MIN 0.0 0.0 0.0\n",
    "DOMAIN_MAX 1.0 1.0 1.0\n"]

    with open(filename+".cube",'w+') as f:
        f.seek(0)
        f.truncate()
        f.writelines(header)
        for b in range(size):
            for g in range(size):
                for r in range(size):
                    x,y = int(r+(b%int(np.sqrt(size)))*size), int(g+(b-(b%int(np.sqrt(size))))/int(np.sqrt(size))*size)
                    f.writelines([str(a[x,y,0]/256)+" "+str(a[x,y,1]/256)+" "+str(a[x,y,2]/256)+"\n"])

print("Starting conversion to .cube")

# Handle input from command line
size = int(argv[1])
filenames = []
for i in range(2,len(argv)):
    filenames.append(argv[i])

# Make testfile
create_test_image("testimg.png",size)

# Calculate all cube files, after running the corresponding images through darktable
for name in filenames:
    call("darktable-cli testimg.png "+name+".xmp "+name+".png", shell=True)
    create_cube(name,size)
    call("rm "+name+".png", shell=True)
call("rm testimg.png", shell=True)

print("Done converting")