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
    
    
   
    
    print(app_path)
            # first read device_info
    with open("{}/data/config.json".format(app_path)) as f:        
            json_data = json.load(f)

    docker_url = json_data["device_info"]["device_docker"]
    
    mount_path = app_path + "/data"
    
    
     # pull docker
        
    docker_command_pull = "docker pull {}".format(docker_url)
    
    print(docker_command_pull)                                                                                                                             
    os.system(docker_command_pull)
        
        
    # run docker
    
    #docker_command = "docker run --rm  -v {}:/app/chooch_ai_on_prem/data -p 8000:8000  {} python3 chooch_service.py".format(mount_path, docker_url)
    docker_command = "docker run -v D:\vantiq\repos\choochai\chooch_ai_on_prem_install\data:/app/chooch_ai_on_prem/data --log-opt max-size=50m --entrypoint /app/chooch_ai_on_prem/chooch_run.sh -p 8000:8000 -p 8001:8001 choochai/chooch_ai-x86-64-cpu:latest"
                                                                                                                                   
    print(docker_command)                                                                                                                             
    os.system(docker_command)
    
    

    
    
    

   


