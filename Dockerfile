FROM python:3.10

RUN apt-get update && apt-get install -y \
    apache2 \
    libapache2-mod-wsgi-py3 \
    apt-get clean

WORKDIR /app

COPY . /app

COPY requirimentes.txt /app/
RUN pip install --no-cache-dir -r requirimentes.txt

COPY apache-config.conf /etc/apache2/sites-avalibe/000-default.conf

EXPOSE 80

CMD ["apache2ctl", "-D", "FOREGROUND"]