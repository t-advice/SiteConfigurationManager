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

#