# Create Weaviate Schema from schema.json

```bash
curl -X POST -H "Content-Type: application/json" \
--data @schema.json http://localhost:8080/v1/schema
```

# Index data.json into Weaviate Schema

```bash
curl -X POST -H "Content-Type: application/json" \
--data @data.json http://localhost:8080/v1/objects
```

Make sure to have both schema.json and data.json files in the same directory where you run these curl commands, or provide the appropriate path to each file.