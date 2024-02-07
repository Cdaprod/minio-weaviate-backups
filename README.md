# MinIO-Weaviate Backups

This repository contains the necessary configurations and instructions to set up and test backup processes using MinIO with Weaviate. It's designed to showcase the integration of MinIO, a high-performance object storage, with Weaviate, an AI-powered search engine, focusing on the backup and restore functionalities within a Dockerized environment.

## Badges

[![Docker Compose Test Workflow for build-context-docker-compose.yaml](https://github.com/Cdaprod/minio-weaviate-backups/actions/workflows/build-context-docker-compose.yml/badge.svg)](https://github.com/Cdaprod/minio-weaviate-backups/actions/workflows/build-context-docker-compose.yml)

[![Update README with Directory Tree](https://github.com/Cdaprod/minio-weaviate-backups/actions/workflows/update_readme.yml/badge.svg)](https://github.com/Cdaprod/minio-weaviate-backups/actions/workflows/update_readme.yml)

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

## Contributing

We welcome contributions! Please read our [Contributing Guide](LINK_TO_CONTRIBUTING_GUIDE) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the [MIT License](LICENSE) - David Cannan Cdaprod

## Acknowledgments

- [MinIO](https://min.io/) for the object storage system.
- [Weaviate](https://www.semi.technology/developers/weaviate/current/) for the AI-powered search engine.
