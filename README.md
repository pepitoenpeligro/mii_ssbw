# Tarea 0

Instalamos docker-compose y componemos nuestro primer servicio django

Si vemos lo que hay inicialmente en el directorio:

```bash
pepe@ubuntu-4gb-nbg1-3:~/mii_ssbw$ ls
docker-compose.yml  Dockerfile  README.md  requirements.txt 
```

Una vez ejecutamos 

```bash
docker-compose run web django-admin.py startproject senderos .
```


Podemos ver que tenemos un directorio *senderos* con nuestro proyecto:

```bash
Creating mii_ssbw_web_run ... done
/usr/local/bin/django-admin.py:17: RemovedInDjango40Warning: django-admin.py is deprecated in favor of django-admin.
  warnings.warn(
pepe@ubuntu-4gb-nbg1-3:~/mii_ssbw$ ls
docker-compose.yml  manage.py  requirements.txt
Dockerfile          README.md  senderos
```