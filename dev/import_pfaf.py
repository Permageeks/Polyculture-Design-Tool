#! /usr/bin/env python

csv_filepathname="/home/harry/python/poly/dev/pfaf_species_utf8.csv"
DEBUG = True

django_project="/home/harry/python/poly/"

import sys,os
sys.path.append(django_project)
os.environ['DJANGO_SETTINGS_MODULE'] = 'poly.settings'

from poly.pdt.models import Plant, Genus, Family, CommonName

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter='|', quotechar='^')

headers = dataReader.next()
rowdicts = [dict(zip(headers, row)) for row in dataReader]

for row in rowdicts:
        #HARMONISED FIELDS
        # assign required model objects
        family = Family()
        genus = Genus()
        plant = Plant()
        common_name = CommonName()

        #family
        family_name = row['Family']
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
        
        # preprocess PFAF "Latin name" field" - split into genus and species.
        latin_name_parts = row['Latin name'].split()

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
        common_name_name = row['Common name']
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
            #INSERT HARMONISED FIELDS
            plant.genus = genus
            plant.species = plant_species
            plant.save()
            plant.common_name = common_name
            plant.cultivation_notes = row['Cultivation details']
            plant.save()
            #INSERT UNHARMONISED FIELDS
            if row['Author']: plant.pfaf_author = row['Author']
            if row['Botanical references']: plant.pfaf_botanical_references = row['Botanical references']
            if row['Habit']: plant.pfaf_habit = row['Habit']
            if row['Deciduous/Evergreen']: plant.pfaf_deciduous_evergreen = row['Deciduous/Evergreen']
            if row['Height']: plant.pfaf_height = row['Height']
            if row['Width']: plant.pfaf_width = row['Width']
            if row['Hardyness']: plant.pfaf_hardyness = row['Hardyness']
            if row['In cultivation?']: plant.pfaf_in_cultivation = row['In cultivation?']
            if row['Medicinal']: plant.pfaf_medicinal = row['Medicinal']
            if row['Range']: plant.pfaf_range = row['Range']
            if row['Habitat']: plant.pfaf_habitat = row['Habitat']
            if row['Soil']: plant.pfaf_soil = row['Soil']
            if row['Shade']: plant.pfaf_shade = row['Shade']
            if row['Moisture']: plant.pfaf_moisture = row['Moisture']
            if row['Well-drained']: plant.pfaf_well_drained = row['Well-drained']
            if row['Nitrogen fixer']: plant.pfaf_nitrogen_fixer = row['Nitrogen fixer']
            if row['pH']: plant.pfaf_ph = row['pH']
            if row['Acid']: plant.pfaf_acid = row['Acid']
            if row['Alkaline']: plant.pfaf_alkaline = row['Alkaline']
            if row['Saline']: plant.pfaf_saline = row['Saline']
            if row['Wind']: plant.pfaf_wind = row['Wind']
            if row['Growth rate']: plant.pfaf_growth_rate = row['Growth rate']
            if row['Pollution']: plant.pfaf_pollution = row['Pollution']
            if row['Poor soil']: plant.pfaf_poor_soil = row['Poor soil']
            if row['Drought']: plant.pfaf_drought = row['Drought']
            if row['Wildlife']: plant.pfaf_wildlife = row['Wildlife']
            if row['Woodland']: plant.pfaf_woodland = row['Woodland']
            if row['Meadow']: plant.pfaf_meadow = row['Meadow']
            if row['Wall']: plant.pfaf_wall = row['Wall']
            if row['In leaf']: plant.pfaf_in_leaf = row['In leaf']
            if row['Flowering time']: plant.pfaf_flowering_time = row['Flowering time']
            if row['Seed ripens']: plant.pfaf_seed_ripens = row['Seed ripens']
            if row['Flower Type']: plant.pfaf_flower_type = row['Flower Type']
            if row['Pollinators']: plant.pfaf_pollinators = row['Pollinators']
            if row['Self-fertile']: plant.pfaf_self_fertile = row['Self-fertile']
            if row['Known hazards']: plant.pfaf_known_hazards = row['Known hazards']
            if row['Synonyms']: plant.pfaf_synonyms = row['Synonyms']
            if row['Edible uses']: plant.pfaf_edible_uses = row['Edible uses']
            if row['Uses notes']: plant.pfaf_uses_notes = row['Uses notes']
            if row['Propagation 1']: plant.pfaf_propagation_1 = row['Propagation 1']
            if row['Cultivars']: plant.pfaf_cultivars = row['Cultivars']
            if row['Cultivars in cultivation']: plant.pfaf_cultivars_in_cultivation = row['Cultivars in cultivation']
            if row['Heavy clay']: plant.pfaf_heavy_clay = row['Heavy clay']
            if row['Pull-out']: plant.pfaf_pull_out = row['Pull-out']
            if row['Last update']: plant.pfaf_last_update = row['Last update']
            if row['Record checked']: plant.pfaf_record_checked = row['Record checked']
            if row['EdibilityRating']: plant.pfaf_edibility_rating = row['EdibilityRating']
            if row['FrostTender']: plant.pfaf_frost_tender = row['FrostTender']
            if row['SiteSpecificNotes']: plant.pfaf_site_specificNotes = row['SiteSpecificNotes']
            if row['Scented']: plant.pfaf_scented = row['Scented']
            if row['MedicinalRating']: plant.pfaf_medicinal_rating = row['MedicinalRating']
            plant.save()
            if DEBUG: print "plant does not exists"
        else:
            if DEBUG: print "plant " + plants[0].genus.name + " " + plants[0].species + " exists"

