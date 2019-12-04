# DarktableToLUT
This programme converts the settings from a set of images edited in darktable to a .cube 3D-LUT file

Prerequisites:
Linux OS
python3 and numpy
darktable

Run by:
python3 DarktableToLUT.py [LUT size] [Image Path 1] [Image Path 2] ...

[LUT size] = size of the NxNxN LUT
[Paths] = paths to the images, which have been added in darktable (xmp files present)

Important Notice:
Only use static effects, such as color correction, saturation, etc. Dynamic effects (vignetting, de-nnoise, etc.) cannot be represented in a LUT-file.
Tested for .png files.
