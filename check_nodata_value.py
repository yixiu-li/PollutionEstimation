import rasterio
import os
import pandas as pd

def get_nodata_value(tif_file_path):
    with rasterio.open(tif_file_path) as dataset:
        nodata_value = dataset.nodatavals[0]  # Assuming a single band, change index if there are multiple bands
    return nodata_value

all_nodata_value = []

directory = r'C:\Users\yixiu\data_from_eosloan_reloc\pm_stations\tiles_224by224_vicinity_center'
file_list = os.listdir(directory)
for station in file_list:
    image_list = os.listdir(os.path.join(directory, station, '8_bit'))
    for image in image_list:
        nodata_value = get_nodata_value(os.path.join(directory, station, '8_bit', image))
        all_nodata_value.append(nodata_value)

df = pd.DataFrame({'Values': all_nodata_value})

excel_filename = 'output_file.xlsx'
df.to_excel(excel_filename, index=False)

print(f"All values exported to {excel_filename}")
