import weaviate
import json

# Configuration
WEAVIATE_ENDPOINT = "http://weaviate:8080"
OUTPUT_FILE = "data.json"

# Initialize the client
client = weaviate.Client(WEAVIATE_ENDPOINT)