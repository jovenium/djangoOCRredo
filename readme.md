# CWF 🍂 Notes

Hey!

So here is what I did during the CWF:

I have a project that is far too big for the time I had. I wanted to make a cryptocurrency trading robot (with Django).
But of course, I never used Django !!
So I used my time to learn how to use Django properly.
I started as an Academy Student, I graduate to Genin and am looking forward to be Chuunin 🍜

First week :
- description of the project, my needs and my desires 📓

Second week:
- discovery of Docker (get-started) 🐳
- diagrams of interactions/ diagrams for my little brain.

Third and fourth weeks:
- discovery of Django and deepening on several subjects.
- obtain the certification of a Django course :

![Certification](https://github.com/jovenium/djangoOCRredo/blob/main/certification_OCR.png?raw=true)


Jovenium 🌹🍂








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
````
sudo docker-compose run web django-admin startproject composeexample .
```
