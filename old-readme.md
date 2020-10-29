

# TIPS TO SETUP THE PROJECT

### Docker
You need docker on Unix or WSL2 on Windows 10.
Clone the repository and run :
```
docker-compose up
```

### Postgres Command
Connected to the container shell :
```
psql postgres postgres
```
Quit with ```\q```

Watch all tables with ```\dt```
Watch a table with ```\d tablename```

### Django Command
```
django-admin startproject <projectname>
```
```
./manage.py migrate
```
```
python3 manage.py showmigrations
```
```
python3 manage.py makemigrations
```

### Make a service 
```
systemctl enable <servicename>
systemctl start <servicename>
systemctl status <servicename>
systemctl stop <servicename>
```
```
service <servicename> start
```

### Other tips
Start Django app when you run docker
```
sudo docker-compose run web django-admin startproject composeexample .
```
