#import modules for data manipulation

import arcpy
import requests
import os
import zipfile
import io
from arcpy.sa import *

#Set variables for the working directory and project geodatabase
proj_dir = r"C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface"
proj_gdb = r"C:\Users\MrJDF\Desktop\\Lab2_Dory\Arc1Lab02DoryCostSurface\Arc1Lab02DoryCostSurface.gdb"

#set arcpy environment, this is where this script will store the imported data
arcpy.env.workspace = proj_dir

#test
arcpy.env.workspace

# set up fnction to unzip requests and save to the project's working directory
def unzip(input_zipped, working_dir):
    get_zipped = zipfile.ZipFile(
        io.BytesIO(
            input_zipped.content)
    )
    
    get_zipped.extractall(working_dir)

#import coordinate table from local file and convert to point feature layer
dory_coords = r"C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\DoryStartEndXYs.csv"
#these coords are backward in my table, so backwards in my code! lazy me.
arcpy.management.XYTableToPoint(dory_coords, "dory_start_end", "y_coord", "x_coord") # optional params: ({z_field}, {coordinate_system})

# create bounding geometry to use as clipping mask/ area extent

# create 2km Buffer around start and end points
arcpy.analysis.Buffer("dory_start_end", r"C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\Arc1Lab02DoryCostSurface.gdb\dory_start_end_Buffer", "2000 Meters", "FULL", "ROUND", "NONE", None, "PLANAR")

#create geometry to encompass buffered points
arcpy.management.MinimumBoundingGeometry("dory_start_end_Buffer", r"C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\Arc1Lab02DoryCostSurface.gdb\dory_start_end_MinimumBoundi2", "CIRCLE", "ALL", None, "NO_MBG_FIELDS")

# County boundaries
county_url = 'https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_dot/bdry_counties/shp_bdry_counties.zip'
county_post_request = requests.post(county_url)
# county_post_request

unzip(county_post_request, proj_dir)


# MN Landcover
landcover_url = 'https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_dnr/biota_landcover_nlcd_mn_2019/tif_biota_landcover_nlcd_mn_2019.zip'
get_landcover = requests.post(landcover_url)


unzip(get_landcover, proj_dir)


# Water routes

water_url = 'https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_dnr/water_strahler_stream_order/shp_water_strahler_stream_order.zip'
get_hydro = requests.post(water_url)

unzip(get_hydro, proj_dir)



# Elevation 

elevation_url = 'https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_dnr/elev_30m_digital_elevation_model/fgdb_elev_30m_digital_elevation_model.zip'
get_elev = requests.post(elevation_url)

unzip(get_elev, proj_dir)


# Roads

roads_url = 'https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_dot/trans_roads_mndot_tis/shp_trans_roads_mndot_tis.zip'
get_roads = requests.post(roads_url)

unzip(get_roads, proj_dir)

# Clip input data to study area 
#make this into a tidy loop: come back to streamline after I get it working
#Uncomment last line of each to execute clip
#set parameters
landCover = r'C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\NLCD 2019 - Land Cover.lyr'
water = r'C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\streams_with_strahler_stream_order.shp'
elevation = r'C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\elev_30m_digital_elevation_model.gdb\digital_elevation_model_30m'
roads = r'C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\STREETS_LOAD.shp'
clip_features = r'C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\Arc1Lab02DoryCostSurface.gdb\dory_start_end_MinimumBoundi2'
#out_feature_class = r'C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\study_area_water.shp'

#land, must use clip here for raster input
in_raster = landCover
rectangle = clip_features
land_out_raster = r'C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\study_area_lndCvr.tif'
#arcpy.management.Clip(in_raster, rectangle, land_out_raster) #, {in_template_dataset}, {nodata_value}, {clipping_geometry}, {maintain_clipping_extent})

#water, pairwise clip for vector
in_features = water
water_out_feature_class = r'C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\study_area_water.shp'
#arcpy.analysis.PairwiseClip(in_features, clip_features, water_out_feature_class) #optional params, {cluster_tolerance}

#Elevation, must use clip here for raster input
in_raster = elevation
rectangle = clip_features
dem_out_raster = r'C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\study_area_dem.tif'
#arcpy.management.Clip(in_raster, rectangle, dem_out_raster)

#roads
in_features = roads
road_out_feature_class = r'C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\study_area_roads.shp'
#arcpy.analysis.PairwiseClip(in_features, clip_features, road_out_feature_class)


#Import new library for slope function and other raster calculations
#from arcpy.ia import * #moved to top

# Set the local variables
in_dem = dem_out_raster

# Execute the Slope function
dem_slope = Slope(in_dem)

# Save the output
dem_slope.save(r'C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\study_dem_slope.tif')

# new import for reclassify tool!
#from arcpy.sa import *

# Slope reclass
# Set local variables

inRaster = dem_slope
reclassField = "Value"
# Define the RemapValue Object 
remap = RemapRange([[0,3,1], [3, 6, 2], [6, 10, 3],[10, 15, 4], [15, 20, 5], [20, 25, 6],[25, 30, 7], [30, 35, 8], [35, 40, 9], [40,75,10]])

# Execute Reclassify
outReclassify = Reclassify(inRaster, reclassField, remap, "NODATA")

# Save the output 
outReclassify.save("slope_reclass.tif")

# Landcover reclass
# Set local variables

inRaster = land_out_raster
reclassField = "Value"
# Define the RemapValue Object 
remap = RemapRange([[11,12, 10], [21, 24, 7], [31, 31, 3],[41, 41, 1], [42, 42, 1], [43, 43, 1],[52, 52, 5], [71, 71, 2], [81,81,10], [82,82,10], [90,90,10], [95,95,10]])

# Execute Reclassify
outReclassify = Reclassify(inRaster, reclassField, remap, "NODATA")

# Save the output 
outReclassify.save("landCvr_reclass.tif")


# Buffer roads and hydrology to create surfaces with dimension of 2 pixel values ie 60m
roads_buffer = arcpy.analysis.Buffer(road_out_feature_class, r'C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\roads_buffer', '60 Meters')
hydro_buffer = arcpy.analysis.Buffer(water_out_feature_class, r'C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\hydro_buffer', '60 Meters')

#use buffered roads to erase hydro data, creating crossable paths for Dory in the next step, where we use the river pixels to multiply values by 0, effectively deleting them from the cost surface.
# set parameters
in_features = hydro_buffer
erase_features= roads_buffer
out_feature_class = proj_dir + "\\water_minus_roads"

#execute erase function
arcpy.analysis.Erase(in_features, erase_features, out_feature_class)

# Merge the water minus roads dataset with the area of interest boundaries to identify any no value cells
arcpy.management.Merge("water_minus_roads;dory_start_end_MinimumBoundi2", r"C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\Arc1Lab02DoryCostSurface.gdb\water_minus_roads_Merge", 'FW_ID "FW_ID" true true false 10 Long 0 10,First,#,water_minus_roads,FW_ID,-1,-1;KITTLE_NBR "KITTLE_NBR" true true false 50 Text 0 0,First,#,water_minus_roads,KITTLE_NBR,0,50;KITTLE_NAM "KITTLE_NAM" true true false 50 Text 0 0,First,#,water_minus_roads,KITTLE_NAM,0,50;LENGTH_MI "LENGTH_MI" true true false 19 Double 0 0,First,#,water_minus_roads,LENGTH_MI,-1,-1;FIXED "FIXED" true true false 1 Text 0 0,First,#,water_minus_roads,FIXED,0,1;ENTIRE "ENTIRE" true true false 1 Text 0 0,First,#,water_minus_roads,ENTIRE,0,1;VALID "VALID" true true false 1 Text 0 0,First,#,water_minus_roads,VALID,0,1;LABEL "LABEL" true true false 200 Text 0 0,First,#,water_minus_roads,LABEL,0,200;EDITED_BY "EDITED_BY" true true false 16 Text 0 0,First,#,water_minus_roads,EDITED_BY,0,16;EDITED_DAT "EDITED_DAT" true true false 8 Date 0 0,First,#,water_minus_roads,EDITED_DAT,-1,-1;EDIT_COMME "EDIT_COMME" true true false 50 Text 0 0,First,#,water_minus_roads,EDIT_COMME,0,50;EVENT_TYPE "EVENT_TYPE" true true false 16 Text 0 0,First,#,water_minus_roads,EVENT_TYPE,0,16;PUBLISH_DA "PUBLISH_DA" true true false 8 Date 0 0,First,#,water_minus_roads,PUBLISH_DA,-1,-1;CONTENT_DA "CONTENT_DA" true true false 8 Date 0 0,First,#,water_minus_roads,CONTENT_DA,-1,-1;SO_ID "SO_ID" true true false 5 Long 0 5,First,#,water_minus_roads,SO_ID,-1,-1;SO_VALUE "SO_VALUE" true true false 5 Long 0 5,First,#,water_minus_roads,SO_VALUE,-1,-1;Shape_Leng "Shape_Leng" true true false 19 Double 0 0,First,#,water_minus_roads,Shape_Leng,-1,-1;BUFF_DIST "BUFF_DIST" true true false 19 Double 0 0,First,#,water_minus_roads,BUFF_DIST,-1,-1;ORIG_FID "ORIG_FID" true true false 10 Long 0 10,First,#,water_minus_roads,ORIG_FID,-1,-1', "NO_SOURCE_INFO")

# Converting to raster
arcpy.conversion.FeatureToRaster("water_minus_roads_Merge", "SO_VALUE", r"C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\Arc1Lab02DoryCostSurface.gdb\hydro_full_raster", 77.2406288442668)

# Reclassify the raster to fit the study area scale and change no data to zeros for raster calculator compatability
arcpy.ddd.Reclassify("hydro_full_raster", "Value", "1 2;2 4;3 6;4 8;5 5;NODATA 0", r"C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\Arc1Lab02DoryCostSurface.gdb\Reclass_hydro", "DATA")

#final output: Reclass_hydro


# REMOVE, REDUNDANT
#reclassify water minus roads buffer
# Set local variables


# inRaster = "hydro_raster"
# reclassField = "Value"
# # Define the RemapValue Object 
# remap = RemapRange([[0,780, 1], [780, 2000, 2], [2000, 4000, 5],[4000, 50000, 10]])

# # Execute Reclassify
# outReclassify_hydro = Reclassify(inRaster, reclassField, remap, "NODATA")

# # Save the output 
# outReclassify_hydro.save("hydro-bridges_reclass") #this won't save with the assigned name, but does save o the GDB as "Reclass_hydr3"

#Remove, Redundant
# had to merge the layers before converting to raster bc this wouldnt work

#create a full raster layer of study area and merge with the river buffer reclassified raster to make it compatible with the cost surfece function
# with out this step the river layer acts as a clipping mask

# #use feature to raster to convert shapefile layer to raster 
# arcpy.conversion.FeatureToRaster("dory_start_end_MinimumBoundi2", "Shape_Length", r"C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\Arc1Lab02DoryCostSurface.gdb\studyAreaRstr", 0.000695375730606202)

# # assign all cells a zero value with reclassify
# out_raster = arcpy.sa.Reclassify("studyAreaRstr", "VALUE", "0.546146822 0", "DATA"); out_raster.save(r"C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\Arc1Lab02DoryCostSurface.gdb\Reclass_studyArea")

# # merge with hydro-bridges values
# #Impossible!



# create weighted cost surface from input reclassified raster data using map algebra


# Set local variables
inRaster1 = "landCvr_reclass.tif"
inRaster2 = 'C:\\Users\\MrJDF\\Desktop\\Lab2_Dory\\Arc1Lab02DoryCostSurface\\slope_reclass.tif' #using double slashes to avoid a unicode error as the single slash registers as an escape character in python
inRaster3 = "Reclass_hydro" #"C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\Arc1Lab02DoryCostSurface.gdb\Reclass_hydr3"
# create weighted sum table object for input for the weighted sum raster calculation
WSumTableObj = WSTable([[inRaster1, "VALUE", 0.5], [inRaster2, "VALUE", 0.25], [inRaster3, "VALUE", 0.25 ]])

# Execute WeightedSum
outWeightedSum = WeightedSum(WSumTableObj)

# Save the output 
outWeightedSum.save("weighted_surface2.tif")



# Weighted Overlay method for weighted cost surface number 2

out_raster = arcpy.sa.WeightedOverlay(r"('C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\slope_reclass.tif' 50 'Value' (1 1; 2 2; 3 3; 4 4; 5 6; 6 7; 7 8; 8 9; 9 10; 10 1; NODATA NODATA); 'C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\landCvr_reclass.tif' 25 'Value' (1 1; 2 2; 3 3; 5 6; 7 8; 10 1; NODATA NODATA); 'C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\Arc1Lab02DoryCostSurface.gdb\Reclass_hydro' 25 'Value' (0 1; 2 2; 4 4; 5 6; 6 7; 8 9; NODATA NODATA));1 10 1"); out_raster.save(r"C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\Arc1Lab02DoryCostSurface.gdb\Weighted_srfc_02")

# create rasters from starting point and end point

#buffer to give pointts dimensions, I buffered with a 30 m radius to give at least 4 pixels to the points
arcpy.analysis.Buffer("dory_start_end", r"C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\Arc1Lab02DoryCostSurface.gdb\dory_start_end_Buffer02", "30 Meters", "FULL", "ROUND", "NONE", None, "PLANAR")

#Convert buffered points to rasters
arcpy.conversion.FeatureToRaster("dory_start_end_Buffer02", "Shape_Length", r"C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\Arc1Lab02DoryCostSurface.gdb\start_end_rstr", 0.000295961719657726)

#Create cost Distance surface from weighted surface
out_distance_raster = arcpy.sa.CostDistance("start_end_rstr", "Weighted_srfc_02", None, None, None, None, None, None, ''); out_distance_raster.save(r"C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\Arc1Lab02DoryCostSurface.gdb\CostDist_01")

#create Cost Back Link from Cost Distance (required as input for cost path tool)
out_backlink_raster = arcpy.sa.CostBackLink("dory_start_end", "CostDist_01", None, None, None, None, None, None, ''); out_backlink_raster.save(r"C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\Arc1Lab02DoryCostSurface.gdb\CostBacklink_dory1")

#create cost path (note, I couldn't get this to run with other inputs, using the buffered featureset worked somehow)
out_raster = arcpy.sa.CostPath("dory_start_end_Buffer02", "CostDist_01", "CostBacklink_dory1", "BEST_SINGLE", "ORIG_FID", "INPUT_RANGE"); out_raster.save(r"C:\Users\MrJDF\Desktop\Lab2_Dory\Arc1Lab02DoryCostSurface\Arc1Lab02DoryCostSurface.gdb\CostPat_dory2")
