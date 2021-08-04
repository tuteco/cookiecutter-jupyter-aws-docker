# {{cookiecutter.project_name}}

Local project for jupyter lab notebooks.

## Project Purpose
> a brief description of the projects purpose and what to expect inside the notebooks.
  
## Usage

- start Jupyter Lab
  ```
  docker compose up
  ```
When the container is started, you will get a URL in the form of https://127.0.0.1:8888/....

We use `invoke` to support various task in working with the container: 
- list available tasks
  ```
  invoke --list
  ```
- get task description
  ```
  invoke --help <task>
  ```  

**Read more** on using [invoke](http://www.pyinvoke.org/) and extending it for your projetcs needs.


## Image Extension

> Instructions for extending the image can be found in 
> the [Readme of the cookiecutter template](https://github.com/tuteco/cookiecutter-jupyter-aws-docker). 
> if you extend the image, please describe the details and provide the URLs to te github or project pages

### additional python libraries
>document the python libraries you used to extend the image
- name of library: reason for usage


### additional jupyter extensions
>document the jupyter extensions you used to extend the image
- name of extension: reason for usage

### build local image

Building your local image is done by calling invoke: 

  ```
  invoke build-local
  ```
  


  