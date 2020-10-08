import shutil
import os
import json


import requests



try:
    app_path = os.path.dirname(os.path.realpath(__file__))
except:
    app_path = "/home/ubuntu/chooch_ai_on_prem"




if __name__ == '__main__':
    
    
    # run docker
    
            # first read device_info
    with open("{}/data/config.json".format(app_path)) as f:        
            json_data = json.load(f)

    docker_url = json_data["device_info"]["device_docker"]
    
    mount_path = app_path + "/data"
    
    
    docker_command = "docker run --runtime nvidia -it  --rm  -v {}:/app/chooch_ai_on_prem/data -p 8000:8000  {} chooch_service.py".format( mount_path, docker_url)
    
                                                                                                                                   
    print(docker_command)                                                                                                                             
    os.system(docker_command)
    
    

    
    
    

   


