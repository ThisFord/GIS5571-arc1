import arcpy # use arc pro objects and functions
from arcpy import env # to set working environmnet
import pandas as pd # manipulate data
import requests #fetch data from apis
import zipfile #compressed data

#set directory path
proj_dir = r'C:\Users\MrJDF\Desktop\Arc1'
#set geodatabase path
proj_gdb = r'C:\Users\MrJDF\Desktop\Arc1\Arc1_lab02\Arc1_lab02.gdb'
#set arcpy environment, this is where this code will store the imported data
arcpy.env.workspace = proj_gdb

#test
arcpy.env.workspace

#set api index base urls
dnrLidar = r'https://resources.gisdata.mn.gov/pub/data/elevation/lidar/'
exmplLas =  r'examples/lidar_sample/las/'
file01 = r'4342-12-05.las'

# make request
dnrLas = requests.get(dnrLidar + exmplLas + file01)

# Create LAS dataset
arcpy.CreateLasDataset_management(dnrLas, 'dnrLas_dataset', 'RECURSION', 'COMPUTE_STATS', 'RELATIVE_PATHS')







aprx = arcpy.mp.ArcGISProject(r"C:\Projects\YosemiteNP\Yosemite.aprx")
lyt = aprx.listLayouts("Main Attractions*")[0]
lyt.exportToPDF(r"C:\Project\YosemiteNP\Output\Yosemite.pdf", resolution = 300)
