import shutil
from shutil import copyfile
import os
import getpass

import sys

import json

import requests
import sys 
  
# total arguments 
n_count = len(sys.argv) 

from datetime import datetime

try:
    app_path = os.path.dirname(os.path.realpath(__file__))
except:
    app_path = "/home/jetson/chooch_ai_service"
    

def get_model_device_info(device_id):
    
    url = "https://api.chooch.ai/predict/device_info/?device_id={}".format(device_id)

    response = requests.post(url)

    model_data = json.loads(response.content)
    
    return model_data
    





def replace_value(input_file, output_file, find_string_val, replace_string_val):
    
    #input file
    fin = open(input_file, "rt")
    #output file to write the result to
    fout = open(output_file, "wt")
    #for each line in the input file
    for line in fin:
         #read replace the string and write to output file
         fout.write(line.replace(find_string_val, replace_string_val))
    #close input and output files
    
    
    fin.close()
    fout.close()
    
    
    
def replace_value_2(input_file, output_file, find_string_val, replace_string_val, find_string_val_2, replace_string_val_2):
    
    #input file
    fin = open(input_file, "rt")
    #output file to write the result to
    fout = open(output_file, "wt")
    #for each line in the input file
    for line in fin:
         #read replace the string and write to output file
         fout.write(line.replace(find_string_val, replace_string_val).replace(find_string_val_2, replace_string_val_2))
      
    #close input and output files
    
    

    fin.close()
    fout.close()    
    
    
app_path = os.path.dirname(os.path.realpath(__file__))



# write device_id


if n_count == 1:    
      device_id = input("Please enter device_id: ")        
else: 
      device_id = str(sys.argv[1]).strip()
        
        
        
model_data = get_model_device_info(device_id)  



now = datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")

data_new_info = {}
data_new_info["device_id"] = device_id

data_new_info["last_update"] = str(date_time)
data_new_info["models"] = model_data["models"]
data_new_info["camera_feeds"] = model_data["cameras"]     
data_new_info["device_info"] = model_data["device_info"]    


with open("{}/data/config.json".format(app_path), 'w', encoding='utf-8') as f:
              json.dump(data_new_info, f, ensure_ascii=False, indent=4)   



# replace values

user_name = getpass.getuser()

replace_value_2("{}/install/chooch_predict_on_prem_base.service".format(app_path),  "{}/chooch_predict_on_prem.service".format(app_path),   "{app_path}", app_path, "{user_name}", user_name)


# get user name



#replace_value_2("{}/chooch_predict_on_prem.service".format(app_path),  "{}/chooch_predict_on_prem.service".format(app_path),   "{user_name}", user_name)


    
replace_value("install/chooch_run_base.sh",  "chooch_run.sh",   "{app_path}", app_path)    


# give docker right
os.system("sudo chmod 666 /var/run/docker.sock")


# give excute rights to choochrun.sh
os.system("sudo chmod +x chooch_run.sh")


#copy service file
os.system("sudo cp chooch_predict_on_prem.service /etc/systemd/system")


#Give rights to service
os.system("sudo systemctl enable chooch_predict_on_prem.service")
os.system("sudo systemctl daemon-reload")


os.system("sudo systemctl stop apt-daily.timer")
os.system("sudo systemctl stop apt-daily.service")
os.system("sudo systemctl disable apt-daily.timer")
os.system("sudo systemctl disable apt-daily.service")


# Start service
os.system("sudo systemctl start chooch_predict_on_prem.service")

#copyfile("choochtrain.service",  "/etc/systemd/system/choochtrain.service")