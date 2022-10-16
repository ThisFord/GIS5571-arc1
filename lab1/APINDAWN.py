#import libraries

import arcpy
import requests
import io
import zipfile
import pandas as pd
#import geopandas as gpd #not installed in arcpy, try !pip install if needed
import os

#set directory path
proj_dir = r'C:\Users\MrJDF\Desktop\GIS5571'
#set geodatabase path
proj_gdb = r'C:\Users\MrJDF\Desktop\GIS5571\Arc1_lab01\Arc1_lab01.gdb'
#set arcpy environment, this is where this code will store the imported data
arcpy.env.workspace = proj_gdb

#test
arcpy.env.workspace

# set home url
mnGeoApi= r'https://resources.gisdata.mn.gov/pub/gdrs/data/pub/' #r'https://resources.gisdata.mn.gov/api and the action commands did not work

# set action variable
# package_list = r'/action/package_list'

# make request
req_data = requests.get(mnGeoApi)

#req_pkg_ls = requests.get(mnGeoApi)
# cast returned data as data frame for display
df_req_data = pd.DataFrame(req_data)
df_req_data.head() #ope! still in the parent directory!

#req_data

#set paths to databases
pathto_mn_streamguage = r'https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_dnr/env_wiski_coop_stream_gaging/shp_env_wiski_coop_stream_gaging.zip'
pathto_mn_superfunds = r'https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_pca/env_remediation_plp/shp_env_remediation_plp.zip'

# set output path
output_path = proj_dir


#function to retrieve data, process, extract
def get_data(pathto_yourdb):
    get = requests.get(pathto_yourdb)
    content = io.BytesIO(get.content)
    zipper = zipfile.ZipFile(content)
    zipper.extractall(output_path)
    
    

#retrieve data, process, extract
get_data(pathto_mn_streamguage)
get_data(pathto_mn_superfunds)

#set CRS
arcpy.management.DefineProjection(r"C:\Users\MrJDF\Desktop\GIS5571\csg.shp", 'PROJCS["NAD_1983_UTM_Zone_15N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-93.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]')
arcpy.management.DefineProjection(r"C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp", 'PROJCS["NAD_1983_UTM_Zone_15N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-93.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]')

#export to project's geodatabase
#arcpy.conversion.ExportFeatures(r"C:\Users\MrJDF\Desktop\GIS5571\csg.shp", proj_gdb)
arcpy.conversion.ExportFeatures(r"C:\Users\MrJDF\Desktop\GIS5571\csg.shp", r"C:\Users\MrJDF\Desktop\GIS5571\Arc1_lab01\Arc1_lab01.gdb\streamgauge", '', "NOT_USE_ALIAS", r'station "station" true true false 15 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\csg.shp,station,0,15;station_id "station_id" true true false 32 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\csg.shp,station_id,0,32;name "name" true true false 80 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\csg.shp,name,0,80;easting "easting" true true false 16 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\csg.shp,easting,0,16;northing "northing" true true false 16 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\csg.shp,northing,0,16;latitude "latitude" true true false 19 Double 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\csg.shp,latitude,-1,-1;longitude "longitude" true true false 19 Double 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\csg.shp,longitude,-1,-1;county_nam "county_nam" true true false 64 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\csg.shp,county_nam,0,64;county_num "county_num" true true false 4 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\csg.shp,county_num,0,4;dnr_minor5 "dnr_minor5" true true false 40 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\csg.shp,dnr_minor5,0,40;huc12 "huc12" true true false 40 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\csg.shp,huc12,0,40;equis_id "equis_id" true true false 40 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\csg.shp,equis_id,0,40;bio_field_ "bio_field_" true true false 40 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\csg.shp,bio_field_,0,40;usgs_id "usgs_id" true true false 40 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\csg.shp,usgs_id,0,40;nwsli "nwsli" true true false 40 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\csg.shp,nwsli,0,40;station_ty "station_ty" true true false 128 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\csg.shp,station_ty,0,128;organizati "organizati" true true false 40 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\csg.shp,organizati,0,40;station_ma "station_ma" true true false 40 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\csg.shp,station_ma,0,40;firstfield "firstfield" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\csg.shp,firstfield,-1,-1;lastfieldv "lastfieldv" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\csg.shp,lastfieldv,-1,-1;has_provis "has_provis" true true false 5 Long 0 5,First,#,C:\Users\MrJDF\Desktop\GIS5571\csg.shp,has_provis,-1,-1;has_approv "has_approv" true true false 5 Long 0 5,First,#,C:\Users\MrJDF\Desktop\GIS5571\csg.shp,has_approv,-1,-1;url "url" true true false 67 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\csg.shp,url,0,67', None)
#arcpy.conversion.ExportFeatures(r"C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp", proj_gdb)
arcpy.conversion.ExportFeatures(r"C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp", r"C:\Users\MrJDF\Desktop\GIS5571\Arc1_lab01\Arc1_lab01.gdb\superfunds", '', "NOT_USE_ALIAS", r'item_id "item_id" true true false 75 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,item_id,0,75;ai_id "ai_id" true true false 19 Double 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,ai_id,-1,-1;ai_name "ai_name" true true false 100 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,ai_name,0,100;site_type "site_type" true true false 3 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,site_type,0,3;si_type "si_type" true true false 4 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,si_type,0,4;si_cat "si_cat" true true false 4 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,si_cat,0,4;si_id "si_id" true true false 19 Double 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,si_id,-1,-1;project_ty "project_ty" true true false 50 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,project_ty,0,50;plp "plp" true true false 1 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,plp,0,1;project_id "project_id" true true false 100 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,project_id,0,100;project_na "project_na" true true false 254 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,project_na,0,254;status "status" true true false 50 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,status,0,50;acreage "acreage" true true false 19 Double 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,acreage,-1,-1;address1 "address1" true true false 100 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,address1,0,100;address2 "address2" true true false 100 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,address2,0,100;city "city" true true false 100 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,city,0,100;state "state" true true false 2 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,state,0,2;zip "zip" true true false 15 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,zip,0,15;loc_desc "loc_desc" true true false 254 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,loc_desc,0,254;county "county" true true false 254 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,county,0,254;cong_dist "cong_dist" true true false 2 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,cong_dist,0,2;house_dist "house_dist" true true false 4 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,house_dist,0,4;senate_dis "senate_dis" true true false 3 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,senate_dis,0,3;huc8 "huc8" true true false 8 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,huc8,0,8;huc8_name "huc8_name" true true false 40 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,huc8_name,0,40;huc10 "huc10" true true false 12 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,huc10,0,12;huc12 "huc12" true true false 12 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,huc12,0,12;huc12_name "huc12_name" true true false 40 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,huc12_name,0,40;dwsma_code "dwsma_code" true true false 2 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,dwsma_code,0,2;dwsma_name "dwsma_name" true true false 40 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,dwsma_name,0,40;latitude "latitude" true true false 19 Double 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,latitude,-1,-1;longitude "longitude" true true false 19 Double 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,longitude,-1,-1;method_des "method_des" true true false 50 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,method_des,0,50;project_ma "project_ma" true true false 254 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,project_ma,0,254;hydrologis "hydrologis" true true false 254 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,hydrologis,0,254;npl "npl" true true false 1 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,npl,0,1;ic "ic" true true false 1 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,ic,0,1;hrs_score "hrs_score" true true false 19 Double 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,hrs_score,-1,-1;score_year "score_year" true true false 4 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,score_year,0,4;wimn_url "wimn_url" true true false 92 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,wimn_url,0,92;site_start "site_start" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,site_start,-1,-1;received "received" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,received,-1,-1;discovered "discovered" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,discovered,-1,-1;site_close "site_close" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,site_close,-1,-1;npl_list "npl_list" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,npl_list,-1,-1;npl_delete "npl_delete" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,npl_delete,-1,-1;plp_list "plp_list" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,plp_list,-1,-1;plp_delist "plp_delist" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,plp_delist,-1,-1;inv_comple "inv_comple" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,inv_comple,-1,-1;remedy_imp "remedy_imp" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,remedy_imp,-1,-1;remedy_sel "remedy_sel" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,remedy_sel,-1,-1;asmt_compl "asmt_compl" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,asmt_compl,-1,-1;nfa_decisi "nfa_decisi" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,nfa_decisi,-1,-1', None)

# spatial join to display superfund sites within 100m of a stream guage and save to the project database
arcpy.analysis.SpatialJoin(r"C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp", r"C:\Users\MrJDF\Desktop\GIS5571\csg.shp", r"C:\Users\MrJDF\Desktop\GIS5571\Arc1_lab01\Arc1_lab01.gdb\streamauge_superfund_join", "JOIN_ONE_TO_MANY", "KEEP_ALL", r'item_id "item_id" true true false 75 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,item_id,0,75;ai_id "ai_id" true true false 19 Double 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,ai_id,-1,-1;ai_name "ai_name" true true false 100 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,ai_name,0,100;site_type "site_type" true true false 3 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,site_type,0,3;si_type "si_type" true true false 4 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,si_type,0,4;si_cat "si_cat" true true false 4 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,si_cat,0,4;si_id "si_id" true true false 19 Double 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,si_id,-1,-1;project_ty "project_ty" true true false 50 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,project_ty,0,50;plp "plp" true true false 1 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,plp,0,1;project_id "project_id" true true false 100 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,project_id,0,100;project_na "project_na" true true false 254 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,project_na,0,254;status "status" true true false 50 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,status,0,50;acreage "acreage" true true false 19 Double 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,acreage,-1,-1;address1 "address1" true true false 100 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,address1,0,100;address2 "address2" true true false 100 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,address2,0,100;city "city" true true false 100 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,city,0,100;state "state" true true false 2 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,state,0,2;zip "zip" true true false 15 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,zip,0,15;loc_desc "loc_desc" true true false 254 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,loc_desc,0,254;county "county" true true false 254 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,county,0,254;cong_dist "cong_dist" true true false 2 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,cong_dist,0,2;house_dist "house_dist" true true false 4 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,house_dist,0,4;senate_dis "senate_dis" true true false 3 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,senate_dis,0,3;huc8 "huc8" true true false 8 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,huc8,0,8;huc8_name "huc8_name" true true false 40 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,huc8_name,0,40;huc10 "huc10" true true false 12 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,huc10,0,12;huc12 "huc12" true true false 12 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,huc12,0,12;huc12_name "huc12_name" true true false 40 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,huc12_name,0,40;dwsma_code "dwsma_code" true true false 2 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,dwsma_code,0,2;dwsma_name "dwsma_name" true true false 40 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,dwsma_name,0,40;latitude "latitude" true true false 19 Double 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,latitude,-1,-1;longitude "longitude" true true false 19 Double 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,longitude,-1,-1;method_des "method_des" true true false 50 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,method_des,0,50;project_ma "project_ma" true true false 254 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,project_ma,0,254;hydrologis "hydrologis" true true false 254 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,hydrologis,0,254;npl "npl" true true false 1 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,npl,0,1;ic "ic" true true false 1 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,ic,0,1;hrs_score "hrs_score" true true false 19 Double 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,hrs_score,-1,-1;score_year "score_year" true true false 4 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,score_year,0,4;wimn_url "wimn_url" true true false 92 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,wimn_url,0,92;site_start "site_start" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,site_start,-1,-1;received "received" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,received,-1,-1;discovered "discovered" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,discovered,-1,-1;site_close "site_close" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,site_close,-1,-1;npl_list "npl_list" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,npl_list,-1,-1;npl_delete "npl_delete" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,npl_delete,-1,-1;plp_list "plp_list" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,plp_list,-1,-1;plp_delist "plp_delist" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,plp_delist,-1,-1;inv_comple "inv_comple" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,inv_comple,-1,-1;remedy_imp "remedy_imp" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,remedy_imp,-1,-1;remedy_sel "remedy_sel" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,remedy_sel,-1,-1;asmt_compl "asmt_compl" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,asmt_compl,-1,-1;nfa_decisi "nfa_decisi" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,nfa_decisi,-1,-1;item_id_1 "item_id" true true false 75 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,item_id,0,75;ai_id_1 "ai_id" true true false 19 Double 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,ai_id,-1,-1;ai_name_1 "ai_name" true true false 100 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,ai_name,0,100;site_typ_1 "site_type" true true false 3 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,site_type,0,3;si_type_1 "si_type" true true false 4 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,si_type,0,4;si_cat_1 "si_cat" true true false 4 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,si_cat,0,4;si_id_1 "si_id" true true false 19 Double 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,si_id,-1,-1;project__1 "project_ty" true true false 50 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,project_ty,0,50;plp_1 "plp" true true false 1 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,plp,0,1;project__2 "project_id" true true false 100 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,project_id,0,100;project__3 "project_na" true true false 254 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,project_na,0,254;status_1 "status" true true false 50 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,status,0,50;acreage_1 "acreage" true true false 19 Double 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,acreage,-1,-1;address1_1 "address1" true true false 100 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,address1,0,100;address2_1 "address2" true true false 100 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,address2,0,100;city_1 "city" true true false 100 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,city,0,100;state_1 "state" true true false 2 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,state,0,2;zip_1 "zip" true true false 15 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,zip,0,15;loc_desc_1 "loc_desc" true true false 254 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,loc_desc,0,254;county_1 "county" true true false 254 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,county,0,254;cong_dis_1 "cong_dist" true true false 2 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,cong_dist,0,2;house_di_1 "house_dist" true true false 4 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,house_dist,0,4;senate_d_1 "senate_dis" true true false 3 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,senate_dis,0,3;huc8_1 "huc8" true true false 8 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,huc8,0,8;huc8_nam_1 "huc8_name" true true false 40 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,huc8_name,0,40;huc10_1 "huc10" true true false 12 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,huc10,0,12;huc12_1 "huc12" true true false 12 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,huc12,0,12;huc12_na_1 "huc12_name" true true false 40 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,huc12_name,0,40;dwsma_co_1 "dwsma_code" true true false 2 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,dwsma_code,0,2;dwsma_na_1 "dwsma_name" true true false 40 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,dwsma_name,0,40;latitude_1 "latitude" true true false 19 Double 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,latitude,-1,-1;longitud_1 "longitude" true true false 19 Double 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,longitude,-1,-1;method_d_1 "method_des" true true false 50 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,method_des,0,50;project__4 "project_ma" true true false 254 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,project_ma,0,254;hydrolog_1 "hydrologis" true true false 254 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,hydrologis,0,254;npl_1 "npl" true true false 1 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,npl,0,1;ic_1 "ic" true true false 1 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,ic,0,1;hrs_scor_1 "hrs_score" true true false 19 Double 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,hrs_score,-1,-1;score_ye_1 "score_year" true true false 4 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,score_year,0,4;wimn_url_1 "wimn_url" true true false 92 Text 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,wimn_url,0,92;site_sta_1 "site_start" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,site_start,-1,-1;received_1 "received" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,received,-1,-1;discover_1 "discovered" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,discovered,-1,-1;site_clo_1 "site_close" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,site_close,-1,-1;npl_list_1 "npl_list" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,npl_list,-1,-1;npl_dele_1 "npl_delete" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,npl_delete,-1,-1;plp_list_1 "plp_list" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,plp_list,-1,-1;plp_deli_1 "plp_delist" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,plp_delist,-1,-1;inv_comp_1 "inv_comple" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,inv_comple,-1,-1;remedy_i_1 "remedy_imp" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,remedy_imp,-1,-1;remedy_s_1 "remedy_sel" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,remedy_sel,-1,-1;asmt_com_1 "asmt_compl" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,asmt_compl,-1,-1;nfa_deci_1 "nfa_decisi" true true false 8 Date 0 0,First,#,C:\Users\MrJDF\Desktop\GIS5571\permanent_list_priorities.shp,nfa_decisi,-1,-1', "WITHIN_A_DISTANCE", "100 Meters", '')


fields = ['ai_name',
          'address1',
         'huc12_name',
          'latitude',
         'longitude'
         ]

#set variable
guagesNsuperfunds = r'C:\Users\MrJDF\Desktop\GIS5571\Arc1_lab01\Arc1_lab01.gdb\streamauge_superfund_join'

#cast as pandas dataframe using the arcpy cursor function to select the fields defined above
df_gaugesNsuperfunds = pd.DataFrame([row for row in arcpy.da.SearchCursor(guagesNsuperfunds, fields)]) #[['ai_name']]) #[address1][HUI2_name][latitude][longitude])

df_gaugesNsuperfunds.head()
