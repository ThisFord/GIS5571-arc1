#import libraries
#!pip install bs4
import arcpy
import requests
import io
import zipfile
import pandas as pd
import os
from arcpy import env
#import BeautifulSoup
#import beautifulsoup as bs4

#set directory path
proj_dir = r'C:\Users\MrJDF\Desktop\GIS5571'
#set geodatabase path
proj_gdb = r'C:\Users\MrJDF\Desktop\GIS5571\Arc1_lab01\Arc1_lab01.gdb'
#set arcpy environment, this is where this code will store the imported data
arcpy.env.workspace = proj_gdb
#test
arcpy.env.workspace

# set home url
api= r'https://ndawn.ndsu.nodak.edu/' 

# make request
req_data = requests.get(api)

#read html as pd dataframe, but not without beautiful soup, which I can't seem to install
#pd.read_html(api)

#get the directories the old fashioned way
req_data.text


#set paths to databases
pathto_db_1 = 'https://ndawn.ndsu.nodak.edu/table.csv?station=78&variable=wdmxt&ttype=weekly&quick_pick=6_m&begin_date=2022-09-26&count=1'
pathto_db_2 = r'https://ndawn.ndsu.nodak.edu/table.csv?station=78&variable=wdmnt&ttype=weekly&quick_pick=6_m&begin_date=2022-09-26&count=1'

# set output path
output_path = proj_dir

get_1 = requests.get(pathto_db_1)
get_2 = requests.get(pathto_db_2)

with open ("output_1.csv", 'w') as text_file:
    text_file.write(get_1.content.decode('utf-8'))
with open ("output_2.csv", 'w') as text_file:
    text_file.write(get_2.content.decode('utf-8'))

arcpy.conversion.TableToTable(r"C:\Users\MrJDF\Desktop\GIS5571\Arc1_lab01\output.csv", r"C:\Users\MrJDF\Desktop\GIS5571\Arc1_lab01\Arc1_lab01.gdb", "adaMNmaxTemp", '', '')
arcpy.conversion.TableToTable(r"C:\Users\MrJDF\Desktop\GIS5571\Arc1_lab01\output_2.csv", r"C:\Users\MrJDF\Desktop\GIS5571\Arc1_lab01\Arc1_lab01.gdb", "adaMNminTemp", '', '')
                          

arcpy.management.AddJoin("adaMNmaxTemp", "OBJECTID", "adaMNminTemp", "OBJECTID", "KEEP_ALL", "NO_INDEX_JOIN_FIELDS")
