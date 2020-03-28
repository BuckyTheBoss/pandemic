import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pandemic.settings')

django.setup()
from cards.models import Card, City, Disease
from game.models import Cube


colors = ['red', 'yellow', 'blue', 'black']


def create_disease():
    if Disease.objects.all().count() < 4:
        for color, name in zip(colors, ['Rubella', 'Juandice', 'Blue Pox', 'Black Plague']):
            disease = Disease(color=color, name=name)
            disease.save()

def create_cities():
    with open('cities.json', 'r') as f:
        data = json.load(f)

    if City.objects.all().count() < 48:
        for city_dict in data:
            disease = Disease.objects.get(name=city_dict['territory'])
            city = City(name=city_dict['name'], disease=disease)
            city.save()
            print(f'City: {city.name} Created!')

        for city_dict in data:
            city = City.objects.get(name=city_dict['name'])
            for city_name in city_dict['connected_cities']:
                connected_city = City.objects.get(name=city_name)
                city.connected_cities.add(connected_city)
                print(f'added connection to City: {city.name} from {connected_city.name}!')


def create_epidemic_card():
    if Card.objects.filter(is_epidemic=True).count() < 1:
        card = Card(is_epidemic=True)
        card.save()


def create_event_cards():
    if Card.objects.filter(is_event=True).count() < 5:
        with open('event_cards.json', 'r') as f:
            data = json.load(f)
        for event_dict in data:
            card = Card(is_event=True, title=event_dict['title'], description=event_dict['description'])
            card.save()


def create_city_cards():
    if Card.objects.filter(is_event=True).count() < 5:
        for city in City.objects.all():
            card = Card(city=city)
            card.save()


def create_cubes():
    if Cube.objects.all().count() < 16:
        for disease in Disease.objects.all():
            for num in range(4):
                cube = Cube(disease=disease)
                cube.save()

def create_chars():
    pass


create_disease()
create_cities()
create_epidemic_card()
create_event_cards()
create_city_cards()
create_cubes()
