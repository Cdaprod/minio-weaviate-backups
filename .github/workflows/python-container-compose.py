name: Weaviate POC Test

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Set up Docker Compose
      run: docker-compose up -d

    - name: Wait for Services to be Ready
      run: sleep 30 # Adjust based on your services' startup time

    # No need to explicitly run Python scripts here; 
    # they're executed as part of the python-environment service's container startup.

    - name: Clean up
      run: docker-compose down