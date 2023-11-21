import os
import arcpy

# set the overwrite option to true
arcpy.env.overwriteOutput = True

print('hello')

img_folder = r'Z:\data_from_eosloan_reloc\historical_data\all_tiles_171820_resampled_500m\16_bit\all_tiles_171820_resampled_500m_resize_imgs'

img_contents = os.listdir(img_folder)

for image in img_contents:
    full_path = os.path.join(img_folder, image)
    Stretch_raster = arcpy.ia.Stretch (full_path, "MinMax", 0, 255, None, None, True, None, None, None, None, None)
    arcpy.CopyRaster_management(Stretch_raster, fr'Z:\data_from_eosloan_reloc\historical_data\all_tiles_171820_resampled_500m\16_bit\output\raster_{image}.tif')