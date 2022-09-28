FROM ejimenezr/plotly-darts-merlion:ssh

USER root

RUN pip install -U nbdev && apt update -y && apt install curl -y && apt upgrade -y && nbdev_install_quarto

# RUN pip install yapf pylint dvc dvc[gdrive]  salesforce-merlion \
#     dvc dvc[gdrive]  statsmodels plotly pandas statsmodels \
#     matplotlib plotly phik darts salesforce-merlion


# RUN pip install plotly mlflow poetry

# RUN apt-get update && \
#     apt-get upgrade -y && \
#     apt-get install -y git  && \
#     apt-get install -y openssh-client 