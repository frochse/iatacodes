FROM       python:3.8
LABEL      maintainer="frenk ochse"

WORKDIR    /app

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip3 install -r requirements.txt

COPY       iatacodes.py /app/
RUN        chmod a+x iatacodes.py

CMD [ "python", "-u", "./iatacodes.py" ]
