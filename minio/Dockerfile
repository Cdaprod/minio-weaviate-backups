# Using the official MinIO image as the base
FROM minio/minio

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /entrypoint.sh

# Setting up environment variables
ENV MINIO_ROOT_USER=minio \
    MINIO_ROOT_PASSWORD=minio123

# Exposing the necessary ports
EXPOSE 9000 9001

# Set the entrypoint to the script
ENTRYPOINT ["/entrypoint.sh"]

