import yaml
from uvicorn.importer import import_from_string

out = "openapi.yaml"
app = import_from_string("main:app")
openapi = app.openapi()

with open(out, "w") as f:
    yaml.dump(openapi, f, sort_keys=False)
    print(f"spec written to {out}")