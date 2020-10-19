from django.db import models

# Create your models here.


ARTISTS = {
  'francis-cabrel': {'name': 'Francis Cabrel'},
  'kosov': {'name': 'Kosov'},
  'rosana': {'name': 'Rosana'},
  'maria-dolores-pradera': {'name': 'María Dolores Pradera'},
}


ALBUMS = [
  {'name': 'Sarbacane', 'artists': [ARTISTS['francis-cabrel']]},
  {'name': 'Spicy', 'artists': [ARTISTS['kosov']]},
  {'name': 'Luna Nueva', 'artists': [ARTISTS['rosana'], ARTISTS['maria-dolores-pradera']]}
]