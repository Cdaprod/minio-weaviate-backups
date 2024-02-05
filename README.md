# minio-weaviate-backups

[![Weaviate POC Test](https://github.com/Cdaprod/minio-weaviate-backups/actions/workflows/backup-curl-tests.yml/badge.svg)](https://github.com/Cdaprod/minio-weaviate-backups/actions/workflows/backup-curl-tests.yml)


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
└── weaviate
    ├── CMD.md
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
    └── schema.json

5 directories, 16 files

```
<!-- DIRECTORY_TREE_END -->
