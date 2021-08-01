FROM tuteco/jupyter_datascience_pyspark:latest

# install additional packages
COPY ./requirements.txt /home/jovyan/requirements.txt
RUN pip install --no-cache -r /home/jovyan/requirements.txt && \


WORKDIR /home/jovyan/work