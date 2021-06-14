# Imagen de contendor de la aplicacion django
FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
# Montamos lo que hay en el directorio actual sobre /code dentro del contenedor
COPY . /code/