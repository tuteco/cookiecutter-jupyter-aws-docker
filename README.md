# cookiecutter-jupyter-aws-docker

cookiecutter template for data analysis with JupyterLab.

Based on the extended docker image [tuteco/jupyter_datascience_pyspark](https://hub.docker.com/r/tuteco/jupyter_datascience_pyspark).
You can see the packages included in the [github repository](https://github.com/tuteco/jupyter_datascience_pyspark)

## Usage
Prerequisites:
- Python 3.8+ for your OS
- [cookiecutter](https://pypi.org/project/cookiecutter/)
- [invoke](https://pypi.org/project/invoke/)

generate a new project, you simply call
```
cookiecutter git@github.com:tuteco/cookiecutter-jupyter-aws-docker.git -o <target_directory>
```
if `-o <target directory>` is omitted, the project will be generated in the current directory 

Parameters you need to provide:
- project_name: short description what you project is about
- project_dir: sluggified version of your project name, or define a directory on your own
- aws_account_number: the account number you are connecting to
- aws_default_region: default region, like eu-central-1
- aws_container_credentials_relative_uri:
    - /creds: use your local credentials from the host OS
    - /role: define a role in AWS
- aws_role: the role name, if /creds chosen before leave it empty
- s3_bucket: if filled, you will find a working example in your notebooks; if blank the example won't work
- s3_prefix: the prefix to a csv file. Also for the example code

More background information on working with local containers can be found on the 
[AWS COmpute Blog](https://aws.amazon.com/blogs/compute/a-guide-to-locally-testing-containers-with-amazon-ecs-local-endpoints-and-docker-compose/)

## extending the image
For inital working with this setup you don't need to extend the image.

If your requiremets grow for additional python libraries or jupyter extension you need for your notebooks,
you want to build your own local image. To do this, you need to modify the following files in your project:
- requirements.txt: any python library you want to install 
- Dockerfile: any extensions that cannot be installed via pip or other binaries required
- docker-compose.yaml: change the name of the image of the jupyter container

To build the local image, simply run
```
invoke build-local
```

The image crated has the default name of ``local/{project_path}``, where the `{project_path` is the one you specified 
during the cookiecutter setup. This is the new image name you need to replace in docker-compose.yml.

```
    image: tuteco/jupyter_datascience_pyspark:latest
    env_file: .env
    volumes:
      - ./work:/home/jovyan/work
    ports:
      - "8888:8888"
    depends_on:
      - {{cookiecutter.project_dir}}-ecs-local-endpoints
    networks:
      credentials_network:
        ipv4_address: "169.254.170.3"
```

