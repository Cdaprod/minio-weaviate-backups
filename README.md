![](/article-banner.jpeg)

# MinIO-Weaviate Backups

### **Article Found Here:** [Backing Up Weaviate with MinIO S3 Buckets](https://blog.min.io/minio-weaviate-integration/)

This repository contains the necessary configurations and instructions to set up and test backup processes using MinIO with Weaviate. It's designed to showcase the integration of MinIO, a high-performance object storage, with Weaviate, an AI-powered search engine, focusing on the backup and restore functionalities within a Dockerized environment.

## Badges

[![Docker Compose Test Workflow for build-context-docker-compose.yaml](https://github.com/Cdaprod/minio-weaviate-backups/actions/workflows/build-context-docker-compose.yml/badge.svg)](https://github.com/Cdaprod/minio-weaviate-backups/actions/workflows/build-context-docker-compose.yml)

[![Docker Compose Test Build and Push](https://github.com/Cdaprod/minio-weaviate-backups/actions/workflows/build-context-compose-and-push.yml/badge.svg)](https://github.com/Cdaprod/minio-weaviate-backups/actions/workflows/build-context-compose-and-push.yml)

[![Update README with Directory Tree](https://github.com/Cdaprod/minio-weaviate-backups/actions/workflows/update_readme.yml/badge.svg)](https://github.com/Cdaprod/minio-weaviate-backups/actions/workflows/update_readme.yml)

(Failure is due to GitHub payments)

## Project Structure

Below is the directory structure of the `minio-weaviate-backups` project, which includes Docker Compose configurations, Dockerfile for MinIO setup, entrypoint scripts, and Weaviate data schemas.

<!-- DIRECTORY_TREE_START -->
```
.
├── DIRECTORY_TREE.txt
├── README.md
├── build-context-docker-compose.yaml
├── docker-compose.yaml
├── minio
│   ├── Dockerfile
│   ├── data
│   └── entrypoint.sh
├── s3_backup_module.ipynb
└── weaviate
    ├── CMD.md
    ├── Dockerfile
    ├── data
    │   ├── classifications.db
    │   ├── migration1.19.filter2search.skip.flag
    │   ├── migration1.19.filter2search.state
    │   ├── migration1.22.fs.hierarchy
    │   ├── modules.db
    │   ├── raft
    │   │   └── raft.db
    │   └── schema.db
    ├── data.json
    ├── entrypoint.sh
    └── schema.json

5 directories, 19 files

```
<!-- DIRECTORY_TREE_END -->

## Getting Started

### Prerequisites

- Docker and Docker Compose installed on your machine.
- Basic knowledge of Docker containerization and orchestration.

### Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Cdaprod/minio-weaviate-backups.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd minio-weaviate-backups
   ```

3. **Build and Run Containers:**

   Use the provided Docker Compose files to build and start the MinIO and Weaviate services.

   ```bash
   docker-compose -f docker-compose.yaml up -d
   ```

### Testing

Follow the instructions in `CMD.md` to create a Weaviate schema, index data, perform backups, and restore data using `curl` commands.

## Usage

Describe how to use the project, including how to perform backups, restore operations, and any other functionalities provided by the project.

## Summary

Below is a quick summary of the key findings--and beneath it, a structured breakdown of the POC article, the accompanying GitHub repository, and how it aligns with official Weaviate support for S3-compatible backups.

This post, "Backing Up Weaviate with MinIO S3 Buckets", by [David Cannan](github.com/Cdaprod) (6 Feb 2024), delivers a full proof-of-concept (POC) for using MinIO as an S3 backend for Weaviate’s backup-s3 module via Docker Compose￼. 

It bundles all necessary artifacts--docker-compose.yaml, schema.json, data.json, and a Jupyter Notebook (s3_backup_module.ipynb)--in a GitHub blog-assets repo for hands-on testing￼. 

Those same assets are mirrored in the Cdaprod/minio-weaviate-backups repository, which includes Dockerfiles, entrypoint scripts, and a complete directory layout for both MinIO and Weaviate services￼. The workflow leverages the Python weaviate-client library to script backups and restorations (pip install weaviate-client) within a notebook environment￼. 

This aligns perfectly with Weaviate’s official backup-s3 support--allowing single-command backup/restore to any S3-compatible store--fully documented in the Weaviate docs  ￼. Community experiences confirm seamless multi-node backups to MinIO by simply pointing BACKUP_S3_ENDPOINT at a MinIO host and toggling SSL settings  ￼.

### POC Article on MinIO Blog

#### Article Overview

David Cannan’s MinIO blog post provides a step-by-step guide to integrate Weaviate’s backup-s3 module with MinIO using Docker Compose  ￼. It highlights how vector search (via Weaviate) and object storage (via MinIO) together form a robust, AI-driven data management system  ￼.

#### Key Components

- **Docker Compose Configuration:** The provided docker-compose.yaml enables backup-s3, sets BACKUP_S3_BUCKET and BACKUP_S3_ENDPOINT to your MinIO server, and mounts ./weaviate/data for persistent storage under /var/lib/weaviate  ￼.
- **Python Notebook Workflow:** The s3_backup_module.ipynb demonstrates using client.backup.create(...) and client.backup.restore(...) with class filters and wait_for_completion=True, showing success responses in real time  ￼.
- **Curl-Based Operations:** For environments without Python, the post details curl commands to POST to /v1/backups/s3 and /v1/backups/s3/{id}/restore, illustrating identical backup/restore logic via HTTP  ￼.

With this POC, you get a fully self-contained demo of backing up and restoring a vector database to MinIO--complete with Docker orchestration, Python scripting, and HTTP APIs. If you need help extending the example--for instance, integrating it into your CI pipelines or embedding into an Electron app--let me know!

## Contributing

We welcome contributions! Please read our [Contributing Guide](LINK_TO_CONTRIBUTING_GUIDE) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the [MIT License](LICENSE) - David Cannan Cdaprod

## Acknowledgments

- [MinIO](https://min.io/) for the object storage system.
- [Weaviate](https://www.semi.technology/developers/weaviate/current/) for the AI-powered search engine.
