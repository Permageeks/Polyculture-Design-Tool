#! /usr/bin/env python

csv_filepathname="/home/harry/python/poly/dev/pfaf_species_utf8.csv"
DEBUG = True

your_djangoproject_home="/home/harry/python/poly/"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'poly.settings'

from poly.pdt.models import Plant, Genus, Family, CommonName

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter='|', quotechar='^')

for row in dataReader:
    if row[0] != 'Latin name': # Ignore the header row, import everything else
        family = Family()
        genus = Genus()
        plant = Plant()
        common_name = CommonName()

        latin_name_parts = row[0].split()
        #family
        family_name = row[3]
        families = Family.objects.filter(name=family_name)
        family_exists = False
        if families:
            family_exists = families[0]
            print family_exists
        if family_exists:
            family = family_exists
            if DEBUG: print "family " + family_name + " exists"
        else:
            family.name = family_name
            if DEBUG: print "family " + family_name + " does not exist"
        family.save()

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
            if family:
                genus.family = family
            if DEBUG: print "genus does not exist"
        genus.save()
        if DEBUG: print genus.name
        if DEBUG: print genus.id

        #common_name
        common_name_name = row[4]
        common_names = CommonName.objects.filter(name = common_name_name)
        common_name_exists = False
        if common_names:
            common_name_exists = common_names[0]
        if common_name_exists:
            common_name = common_name_exists
            if DEBUG: print "common name " + common_name_name + " exists"
        else:
            common_name.name = common_name_name
            if DEBUG: print "common name " + common_name_name + " added."
        common_name.save()

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
            plant.common_name = [common_name]
            plant.save()
            if DEBUG: print "plant does not exists"
        else:
            if DEBUG: print "plant " + plants[0].genus.name + " " + plants[0].species + " exists"


