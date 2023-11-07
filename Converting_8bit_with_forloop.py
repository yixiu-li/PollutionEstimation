import os
import arcpy

img_folder = r'C:\Users\yql5946\Desktop\input'

img_contents = os.listdir(img_folder)

for image in img_contents:
    full_path = os.path.join(img_folder, image)
    Stretch_raster = arcpy.ia.Stretch (image, "PercentClip", None, None, None, None, True, 0.25, 0.75, None, None, None)
    arcpy.CopyRaster_management(Stretch_raster, fr'C:\Users\yql5946\Desktop\input\output\raster_{image}.tif')
