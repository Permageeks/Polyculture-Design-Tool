#! /usr/bin/env python

csv_filepathname="/home/harry/python/poly/dev/pfaf_species.csv"
DEBUG = True

your_djangoproject_home="/home/harry/python/poly/"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'poly.settings'

from poly.pdt.models import Plant, Genus

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter='|', quotechar='^')

for row in dataReader:
    if row[0] != 'Latin name': # Ignore the header row, import everything else
        genus = Genus()
        plant = Plant()
        latin_name_parts = row[0].split()

        #genus
        genus_name = latin_name_parts[0]
        genera = Genus.objects.filter(name=genus_name)
        genus_exists = False
        if genera:
            genus_exists = genera[0]
        if genus_exists:
            genus = genus_exists
            if DEBUG: print "genus exists"
        else:
            genus.name = genus_name
            if DEBUG: print "genus does not exist"
        genus.save()
        if DEBUG: print genus.name
        if DEBUG: print genus.id

        #plant
        if len(latin_name_parts) > 1:
            plant_species = latin_name_parts[1]
        else:
            plant_species = 'sp.'
        plants = Plant.objects.filter(species=plant_species, genus=genus)
        plant_exists = False
        if plants:
            plant_exists = plants[0]
        if not plant_exists:
            plant.genus = genus
            plant.species = plant_species
            plant.save()
            if DEBUG: print "plant does not exists"
        else:
            if DEBUG: print "plant " + plants[0].genus.name + " " + plants[0].species + " exists"


