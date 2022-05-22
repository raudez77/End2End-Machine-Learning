# Download Ubuntu Image
FROM ubuntu:18.04

# Creating an ENV path 
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

# Install python 3
RUN apt update \
    && apt install -y python3-dev wget

# 1. Download Mini conda
# 2. Create a new folder
# 3. Install miniconda -b: silent install
# 4. Remove the download rm -f filename
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py37_4.12.0-Linux-x86_64.sh \
    && mkdir root/.conda \
    && sh Miniconda3-py37_4.12.0-Linux-x86_64.sh -b \
    && rm -f Miniconda3-py37_4.12.0-Linux-x86_64.sh

#Create a docnew Enviroment
RUN conda create -y -n ml python=3.7.4

# Copy files 
COPY . src/

# 1. go to src
#2. In shell linux activate the enviroment 
RUN /bin/bash -c "cd src/requirements/ \
    && source activate ml \
    && pip install -r requirements.txt"

RUN /bin/bash -c "cd src/classification_model/\
    && source activate ml \
    && python for_production.py"
