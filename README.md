# dagster-code-boilerplate

### Setup
This project use [PDM](https://pdm.fming.dev/latest/) as Python package and dependencies manager.
1. Install python virtual environment version 3.9
    ```
    conda create --prefix .venv python=3.9
    ```
2. Select python environment
    ```
    pdm use
    ```
    then select recently created `.venv`
3. Install dependencies
   ```
   pdm install
   ```

### Quik Start
1. Create `.env` file for storing neccessary config. Example
    ```
    S3_BUCKET=<xxx>

2. [Optional] Uncomment environment variables in `docker-compose.yaml`
2. Run
    ```
    docker-compose up
    ```
3. Let see http://127.0.0.1:3000/asset-groups


### Development
1. If you want to add more dependencies (example. `matplotlib``)
    ```
    pdm add matplotlib
    ```
