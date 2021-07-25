FROM jupyter/all-spark-notebook

# install additional packages
COPY ./requirements.txt /home/jovyan/requirements.txt
RUN pip install --no-cache -r /home/jovyan/requirements.txt && \
    R -e "if (!require('devtools')) install.packages('devtools',  dependencies=TRUE, repos = 'http://cran.rstudio.com')" && \
    R -e "devtools::install_github('IRkernel/IRkernel')" && \
    R -e "IRkernel::installspec()" && \
    R -e "install.packages(c('tidyverse', 'botor', 'formatR', 'kableExtra'), dependencies=TRUE, repos = 'http://cran.rstudio.com')" && \
    jupyter labextension install jupyterlab-plotly --no-build && \
    jupyter labextension install jupyterlab-chart-editor --no-build && \
    jupyter lab build && \
        jupyter lab clean && \
        jlpm cache clean && \
        npm cache clean --force && \
        rm -rf $HOME/.node-gyp && \
        rm -rf $HOME/.local

WORKDIR /home/jovyan/work