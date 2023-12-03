import os
import arcpy

# set the overwrite option to true
arcpy.env.overwriteOutput = True

# Define the background color to be removed
background_color = [0, 0, 0, 0]

print('hello')

# Check spatial analyst extension availability
if arcpy.CheckExtension("Spatial") == "Available":
    arcpy.CheckOutExtension("Spatial")
    print("Spatial Analyst extension checked out.")
else:
    print("Spatial Analyst extension is not available.")

img_folder = r'Z:\data_from_eosloan_reloc\historical_data\all_tiles_171820_resampled_500m\16_bit\all_tiles_171820_resampled_500m_resize_imgs'

img_contents = os.listdir(img_folder)

# Use the Con function to remove the background pixels
for image in img_contents:
    full_path = os.path.join(img_folder, image)
    Stretch_raster = arcpy.ia.Stretch (full_path, "MinMax", 0, 255, None, None, True, None, None, None, None, None)
    arcpy.CopyRaster_management(arcpy.sa.Con((Stretch_raster != background_color[0]) & (Stretch_raster != background_color[1]) & (Stretch_raster != background_color[2]) & (Stretch_raster != background_color[3]), Stretch_raster), fr'Z:\data_from_eosloan_reloc\historical_data\all_tiles_171820_resampled_500m\16_bit\output\raster_{image}.tif')