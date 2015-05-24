#############################################
#  Python Script SVN_handler_1.0 
#  author:
#  Read README for details
#############################################

import config
import os
from sys import exit
import shutil

Username = config.paramenters['username']
Password = config.paramenters['password']
URL = config.paramenters['URL']
revision = config.paramenters['revision']
Temp_path = config.paramenters['temp_path']
src = config.paramenters['source_cp_folder']
dest = config.paramenters['dest_cp_folder']
src_folder = config.paramenters['folder_copy']

#def read_parameters():
    ## Add mechanism to read parameters from email
    
if (os.path.isdir(src)):
    shutil.rmtree(src, ignore_errors=True)
os.system('pwd')
co_command = 'svn export --username '+Username+' --password '+Password+' -r '+revision+' '+URL+' '+src
os.system(co_command)
if (os.path.isdir(dest)):
    shutil.rmtree(dest, ignore_errors=True)
os.mkdir(dest)
scp_command = 'cp -r '+src_folder+' '+dest
os.system(scp_command)
# add your destination PUME here and copy folders in dest to werever is required

exit(0)






