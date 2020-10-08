import shutil
import os
import json






try:
    app_path = os.path.dirname(os.path.realpath(__file__))
except:
    app_path = "/home/ubuntu/chooch_ai_on_prem"




if __name__ == '__main__':
    
    
    # run docker
    
            # first read device_info
    with open("{}/data/config.json".format(app_path)) as f:        
            json_data = json.load(f)

    docker_url = json_data["docker_url"]
    
    mount_path = app_path + "/data"
    
    
    docker_command = "docker run --runtime nvidia -it  --rm  -v {}:/app/chooch_ai_on_prem/data -p 8000:8000  {} chooch_service.py".format(docker_url, mount_path)
    
                                                                                                                                   
    print(docker_command)                                                                                                                             
    os.system(docker_command)
    
    

    
    
    

   


