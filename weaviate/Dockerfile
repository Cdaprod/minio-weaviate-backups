# Use the official Weaviate image
FROM semitechnologies/weaviate:latest
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy schema.json and entrypoint.sh into the container
COPY schema.json /weaviate/schema.json
COPY entrypoint.sh /weaviate/entrypoint.sh

# Make the script executable
RUN chmod +x /weaviate/entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/weaviate/entrypoint.sh"]