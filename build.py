# Build `docker-compose.yml` and `default.conf`

import glob

# Get the name of each app
app_folders = glob.glob("apps/*")
app_folders = list(map(lambda x: x.split("/")[1], app_folders))

# Boiler plate code for docker-compose file
compose_template = """version: '3'
services:
  dragon:
    build: ./proxy
    container_name: dragon
    restart: unless-stopped
    ports:
      - "80:80"
    depends_on:
"""

# Add boilerplate to compose file
compose_string = compose_template

# Add dependencies to compose file
for app_name in app_folders:
    compose_string += f"      - {app_name}\n"

# Add apps to compose file
for app_name in app_folders:
    compose_string += f"  {app_name}:\n" 
    compose_string += f"    build: ./apps/{app_name}\n"
    compose_string += f"    container_name: {app_name}\n"
    compose_string += "    restart: unless-stopped\n"

# Write the compose file
compose_file = open("docker-compose.yml", 'w')
compose_file.write(compose_string)
compose_file.close()

# Build 

conf_template_before = """server {
    listen 80;
    location / {
        proxy_pass http://127.0.0.1;
    }
"""

conf_template_after = """
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }
}"""

conf_string = conf_template_before

for app_name in app_folders:
    conf_string += f"    location /{app_name}" + " {\n"
    conf_string += f"        rewrite ^/{app_name}(.*) /$1 break;\n"
    conf_string += f"        proxy_pass http://{app_name}:8080;\n"
    conf_string += "    }\n"

conf_string += conf_template_after

# Write to default.conf file
default_file = open("proxy/default.conf", 'w')
default_file.write(conf_string)
default_file.close()