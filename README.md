# orchestrator

## Local installation
- Make sure Docker is installed and running;
- Run: $ docker compose build
- Run: $ docker compose up airflow-init
- Run: $ docker compose up -d
- Run: $ ./airflow.sh connections import /opt/airflow/config/connections.yaml --overwrite

## Adding resources
### Variables
Variables should be added to the ./.env file and after adding them, you should run the command:
``` $ docker compose build ```
### Python packages
Python packages should be added to the ./requirements.txt file and after adding them, you should run the command:
``` $ docker compose build ```
### Connections
Connections should be added to the config/connections.yaml file and after adding them, you should run the command:
``` $ ./airflow.sh connections import /opt/airflow/config/connections.yaml --overwrite ```

## About variables
- When running Airflow locally, the variables named as "AIRFLOW_VAR_[NAME]" on the .env file will be used as Airflow variables, recognised only with the [NAME] part, but in lower case. Those variables won't be seen on Airflow UI, but can be used in the DAGs code. - When running Airflow in Production, the variables need to be created on Airflow UI, using the same names as the local ones.
- The variables containing values that need be hidden, when checking the Production UI, should be named as "AIRFLOW_VAR_SECRET_[NAME]".

- Usage:  
    - A variable named "AIRFLOW_VAR_SECRET_API_SECRET_KEY" can be used in the code with the python method Variable.get('secret_api_secret_key')
    - A variable named "AIRFLOW_VAR_API_PUBLIC_KEY" can be used in the code with the python method Variable.get('api_public_key')


## Repository creation
### Initial steps
Following [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/2.5.1/howto/docker-compose/index.html):

``` $ curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.5.1/docker-compose.yaml' ```  
``` $ mkdir -p ./dags ./logs ./plugins ```  
``` $ echo -e "AIRFLOW_UID=$(id -u)" > .env ```  
``` curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.7.3/airflow.sh' ```  

### Customizations
``` $ mkdir -p ./temp ```  
- On the docker-compose file, the image block was changed to build, running a Dockerfile file;
- The file Dockerfile intalls the version of Airflow used on Cloud Composer and the python packages on the requirements file;
- A volume was added in the docker-compose.yaml file, to map a "temp" folder, allowing file transference between a local directory and the containers;
- The value of the property 'AIRFLOW__CORE__LOAD_EXAMPLES' in the docker-compose.yaml file was change to False;
- The file connections.yaml was moved to the config folder.