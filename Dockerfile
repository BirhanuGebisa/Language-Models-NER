FROM python:3.8
# install requirements
COPY requirements.txt requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt

# Copy app
COPY . .
WORKDIR /

# Run
CMD [ "flask" , "run"]