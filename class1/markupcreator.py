#!/usr/bin/env python

import json
import yaml

listobj = [1,2,3,4,5,{"foo": "bar", "baz": "qux"}]

with open("dumpfile.yml", "w") as f:
    f.write(yaml.dump(listobj, default_flow_style=False))

with open("dumpfile.json", "w") as f:
    json.dump(listobj, f)
