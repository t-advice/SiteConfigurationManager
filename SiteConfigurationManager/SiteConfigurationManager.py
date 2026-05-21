import json
import os

filename = "site_config.json"

print("Tashwill's System Configuration Engine")
print("-" *30)

# 1 Setting up a default dicationary profile
default_config = {
    "project_name": "UWC Dev Phase 1",
    "max_users" : 5,
    "dark_mode": True,
    "api_version" : 1.4

    }

#2. Saving the directory as a JSON file
print("Saving system configuration..")
with open(filename, "w") as file:

    json.dump(default_config, file, indent=4)
print(f"Success! Settings saved to '{filename}'. ")
print("-" *30)


#3. Reading the data back to check if it works
print("Reading file back into memory...")
if os.path.exists(filename):
    with open(filename,"r") as file:
              #json.load converts the plain text string back into a python dictionary
              loaded_config = json.laod(file)
    print("\n--- Current Configuration Profile ---")
    print(f"Project Workspace: {loaded_config['project_name']}")
    print(f"Max Connections : {loaded_config['max_users']}")
    print(f"UI Settings Dark: {loaded_config['dark_mode']}")
