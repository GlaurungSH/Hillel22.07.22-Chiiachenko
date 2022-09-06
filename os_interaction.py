import os
import json

system_info = {'os type': os.name,
               'system information': os.uname(),
               }

with open('os_report.json', 'w') as os_report:
    json.dump(system_info, os_report)
