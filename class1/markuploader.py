#!/usr/bin/env python

import json
import yaml

with open("dumpfile.json") as f:
    jsonlist = json.load(f)
    print json.dumps(jsonlist, indent=4, sort_keys=True)

with open("dumpfile.yml") as f:
    yamllist = yaml.load(f)
    print yaml.dump(yamllist, default_flow_style=False)
    
