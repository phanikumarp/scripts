import yaml
import os
import io
import json
import sys

# File Locations
yaml_locations={"rosco" : "/opt/rosco/config/rosco.yml",
                "orca" : "/opt/spinnaker/config/orca.yml"
               }
js_locations={"deck_setting_js" : "/opt/spinnaker/config/settings.js",
              "setting_js" : "/opt/deck/html/settings.js"
             }



# Changes to the files
updates={"rosco_configdir" : " /opt/rosco/config/packer",
         "orca_baseurl" : "http://edge8:8090",
         "debianRepository": "http://jenkinsn42.s3-website-us-west-2.amazonaws.com trusty main",
         "netflixMode": "true"
         }

def read_yaml(file_name):
    if not os.path.exists(file_name):
        print "{} not found! Please check.".format(file_name)
        exit()
    with open(file_name) as f:
        data=yaml.load(f)
    return data

def write_yaml(data,yaml_file):
    #make the backup file and write
    os.rename(yaml_file,yaml_file+".backup")
    with io.open(yaml_file, 'w', encoding='utf8') as outfile:
        yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)

def set_true():
    for name, file_location in js_locations.items():
        if os.path.exists(file_location)
        lines=list()
        with open(file_location,"r") as f:
            for line in f.readlines():
                if "netflixMode: false" in line:
                    lines.append("netflixMode: {},\n".format(updates["netflixMode"]))
                else:
                    lines.append(line)
        #make the backup file and write
        os.rename(file_location,file_location+".backup")
        with open(file_location,"w") as f:
            f.writelines(lines)

if __name__=='__main__':
    rosco=read_yaml(yaml_locations["rosco"])
    rosco['rosco']['configDir']=updates["rosco_configdir"]
    rosco['debianRepository']=updates["debianRepository"]
    write_yaml(rosco, yaml_locations["rosco"])

    orca=read_yaml(yaml_locations["orca"])
    orca['mine']['baseUrl']=updates["orca_baseurl"]
    write_yaml(orca, yaml_locations["orca"])

    set_true()
