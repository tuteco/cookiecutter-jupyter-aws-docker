FROM jupyter/all-spark-notebook

# install additional packages
COPY ./requirements.txt /home/jovyan/requirements.txt
RUN pip install --no-cache -r /home/jovyan/requirements.txt && \


WORKDIR /home/jovyan/work