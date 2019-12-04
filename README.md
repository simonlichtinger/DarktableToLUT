# DarktableToLUT
This program converts the settings from a set of images edited in darktable to a colour lookup table, i.e. a .cube 3D-LUT file.

## Prerequisites:

 * Linux OS
 * python3
 * numpy
 * darktable

## How to Run

```python3 DarktableToLUT.py [LUT size] [Image Path 1] [Image Path 2] ...```

where:

`[LUT size]` = size of the NxNxN LUT

`[Paths]` = paths to the images, which have been added in darktable (xmp files present)

## Important Notice:

Only use static effects, such as color correction, saturation, etc. Dynamic effects (vignetting, de-nnoise, etc.) cannot be represented in a LUT-file.

Tested for .png files.
