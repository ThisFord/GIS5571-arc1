import arcpy
import pandas as pd
import requests


#set working envi n project envi

proj_dir = r"C:\Users\MrJDF\Desktop\Arc1_lab02_v02"
proj_gdb = r"C:\Users\MrJDF\Desktop\Arc1_lab02_v02\Arc1_lab02_v02.gdb"

#set arcpy environment, this is where this code will store the imported data
arcpy.env.workspace = proj_dir

#test
arcpy.env.workspace



#file path variables
mnDnr_indx = r"https://resources.gisdata.mn.gov/pub/data/elevation/lidar/"
exmpl_lidar_sets = r"examples/lidar_sample/las/"
lasFile = r"/4342-12-05.las" #change this to change the file for download

#set full path to file
data_path = mnDnr_indx + exmpl_lidar_sets + lasFile

# get the file from the rempte db

data = requests.get(data_path)
print(data) #response 200 is successful get per CKAN api
type(data)


#open the file in write-binary mode, write the contents of the file
with open(lasFile, 'wb') as file:
    file.write(data.content) 

# Create LAS dataset

data_path = proj_dir + lasFile

#arcpy.CreateLasDataset_management(r'C:\Users\MrJDF\Desktop\Arc1_lab02_v02\4342-12-05.las', 'dnrLas_dataset.lasd') # DONT INCLUDE THESE VARIABLES:'RECURSION', 'COMPUTE_STATS', 'RELATIVE_PATHS')
arcpy.CreateLasDataset_management(data_path, 'dnrLas_dataset_01') 

# las to tin
arcpy.ddd.LasDatasetToTin(r"C:\Users\MrJDF\Desktop\Arc1_lab02_v02\dnrLas_dataset_01.lasd", r"C:\Users\MrJDF\Desktop\Arc1_lab02_v02\dnrLas_tin", "RANDOM", 15, 3.28)

# las to DEM (using the las to raster function) saved to geodatabse

arcpy.conversion.LasDatasetToRaster(r"C:\Users\MrJDF\Desktop\Arc1_lab02_v02\dnrLas_dataset_01.lasd", r"c:\Users\MrJDF\Desktop\arc1_lab02_v02\arc1_lab02_v02.gdb\dnrlas_dem", "ELEVATION", "BINNING AVERAGE LINEAR", "FLOAT", "CELLSIZE", 10, 1)


# export Layout of TIN to PDF using .mp method (for manipulate?)

# call the desired project where the layout is
aprx = arcpy.mp.ArcGISProject(r"C:\Users\MrJDF\Desktop\Arc1_lab02_v02\Arc1_lab02_v02.aprx")

# access the layouts in the project via string search and indexing;
# the star tells the function to find objects starting with MN,
# I think it's called a "wildcard" search term,
# then starts with the index at zero.
lyt = aprx.listLayouts("MN*")[0]

#use the export to pdf function and set resolution 
lyt.exportToPDF(proj_dir + r"\Output\MNDNR_TIN.pdf", resolution = 300)

# export layout of DEM to PDF
lyt01 = aprx.listLayouts("MN*")[1]
lyt01.exportToPDF(proj_dir + r"\Output\MNDNR_DEM.pdf", resolution = 300)


