# This contains the manifest_validator and the referring schema.

## usage:

```
from .json.manifest_validator import ManifestValidator

...python

schema = open("/json/schema/manifest_schema.json").read
validator = ManifestValidator(schema)
file_to_test = open(file_to_test.json).read
r = validator.validate(file_to_test)
if r == None:
    pass
    #do something
```

## schema description