from django.db import models
from django.contrib import admin

class MajorGroup(models.Model):
    name = models.CharField(max_length=30)

class Family(models.Model):
    major_group = models.ForeignKey(MajorGroup)
    name = models.CharField(max_length=30)

    class Meta:
                verbose_name_plural = 'Families'

class Genus(models.Model):
    family = models.ForeignKey(Family)
    name = models.CharField(max_length=30)
    hybrid_marker = models.CharField(max_length=1)

    class Meta:
        verbose_name_plural = 'Genera'

class BotanicalSynonym(models.Model):
    INFRA_RANK_CHOICES = (('d','dummy'), )
    species = models.CharField(max_length=30)
    infraspecific_rank = models.CharField(max_length=10, choices=INFRA_RANK_CHOICES)
    infraspecific_epithet = models.CharField(max_length=30)
    cultivar = models.CharField(max_length=30)
    notes = models.TextField(blank=True, null=True)

class Nuisance(models.Model):
    NUISANCE_CHOICES = ( ('all', 'allelopathic'), ('dis', 'dispersive'), ('exp', 'expansive'), ('haf', 'hay fever'), ('per', 'persistent'), ('svv', 'sprawling vigorous vine'), ('sti', 'stings'), ('tho', 'thorny'), )
    nuisance = models.CharField(max_length=10, choices=NUISANCE_CHOICES)
    notes = models.TextField(blank=True, null=True)

class BotanicalAuthor(models.Model):
    lastname = models.CharField(max_length=40)
    firstname = models.CharField(max_length=40)
    firstname_initial = models.CharField(max_length=2)
    notes = models.TextField(blank=True, null=True)

class CommonName(models.Model):
    name = models.CharField(max_length=80)
    notes = models.TextField(blank=True, null=True)

class ReproductiveStrategy(models.Model):
    REPRODUCTIVE_CHOICES = ( ('se', 'seed'),  ('c', 'corm'),  ('r', 'runner'), ('su', 'sucker'), )
    strategy = models.CharField(max_length=10, choices=REPRODUCTIVE_CHOICES)
    notes = models.TextField(blank=True, null=True)

class Ecozone(models.Model):
    name = models.CharField(max_length=30)
    notes = models.TextField(blank=True, null=True)

class Biome(models.Model):
    ecozone = models.ForeignKey(Ecozone)
    name = models.CharField(max_length=60)
    notes = models.TextField(blank=True, null=True)

class Ecoregion(models.Model):
    biome = models.ForeignKey(Biome)
    name = models.CharField(max_length=60)
    notes = models.TextField(blank=True, null=True)

class VegetationCommunity(models.Model):
    ecoregion = models.ForeignKey(Ecoregion)
    name = models.CharField(max_length=80)
    notes = models.TextField(blank=True, null=True)

class NativeRegion(models.Model):
    ecoregion = models.ForeignKey(Ecoregion)
    notes = models.TextField(blank=True, null=True)

class Habitat(models.Model):
    HABITAT_CHOICES = (('d','dummy'), )
    habitat = models.CharField(max_length=10, choices=HABITAT_CHOICES)

class EcologicalNiche(models.Model):
    name = models.CharField(max_length=80)
    notes = models.TextField(blank=True, null=True)

class WaterNeed(models.Model):
    WATER_NEEDS_CHOICES = ( ('x', 'xeric / low water use'), ('m', 'mesic / medium water use'),  ('h', 'hydric / high water use'), )
    ecoregion = models.ForeignKey(Ecoregion)
    water_needs = models.CharField(max_length=30, choices=WATER_NEEDS_CHOICES)

class PlantPart(models.Model):
    part = models.CharField(max_length=30)
    notes = models.TextField(blank=True, null=True)

class PollinationMechanism(models.Model):
    POLLINATION_CHOICES = ( ('', 'bee'), ('', 'other insect'), ('', 'wind'), )
    mechanism = models.CharField(max_length=10, choices=POLLINATION_CHOICES)

class MedicinalUse(models.Model):
    MEDICINAL_USE_CHOICES = ( ('d', 'dummy'), )
    MEDICINAL_RATING_CHOICES = (('d','dummy'), )
    part = models.ForeignKey(PlantPart)
    rating = models.CharField(max_length=30, choices=MEDICINAL_RATING_CHOICES)
    use = models.CharField(max_length=30, choices=MEDICINAL_USE_CHOICES)
    notes = models.TextField(blank=True, null=True)

class EdibleUse(models.Model):
    EDIBLE_USE_CHOICES = ( ('', 'fresh'), ('', 'spice'), ('', 'flavouring'), ('', 'sweetener'), ('', 'cooked'), )
    EDIBLE_RATING_CHOICES = (('d','dummy'), )
    part = models.ForeignKey(PlantPart)
    use = models.CharField(max_length=20, choices=EDIBLE_USE_CHOICES)
    rating = models.CharField(max_length=10, choices=EDIBLE_RATING_CHOICES)         
    notes = models.TextField(blank=True, null=True)

class OtherUse(models.Model):
    OTHER_USE_CHOICES = ( ('d','dummy'),)
    OTHER_USE_RATING_CHOICES = ( ('d','dummy'),)
    part = models.ForeignKey(PlantPart)
    rating = models.CharField(max_length=30, choices=OTHER_USE_RATING_CHOICES)
    use = models.CharField(max_length=30, choices=OTHER_USE_CHOICES)
    notes = models.TextField()

class Month(models.Model):
    month = models.CharField(max_length=20)

class FruitingTime(models.Model):
    ecoregion = models.ForeignKey(Ecoregion)
    start_month = models.ForeignKey(Month)
    #end_month = models.ForeignKey(Month)

class VegetativeGrowthTime(models.Model):
    ecoregion = models.ForeignKey(Ecoregion)
    start_month = models.ForeignKey(Month)
    #end_month = models.ForeignKey(Month)

class FloweringTime(models.Model):
    ecoregion = models.ForeignKey(Ecoregion)
    start_month = models.ForeignKey(Month)
    #end_month = models.ForeignKey(Month)

class SeedRipeningTime(models.Model):
    ecoregion = models.ForeignKey(Ecoregion)
    start_month = models.ForeignKey(Month)
    #end_month = models.ForeignKey(Month)

class RootPattern(models.Model):
    ROOT_PATTERN_CHOICES = (('d','dummy'), )
    name = models.CharField(max_length=30, choices=ROOT_PATTERN_CHOICES)

class RootType(models.Model):
    ROOT_TYPE_CHOICES = (('d','dummy'), )
    name = models.CharField(max_length=30, choices=ROOT_TYPE_CHOICES)

class Plant(models.Model):
    HYBD_MKR_CHOICES = (('d','dummy'), )
    INFRA_RANK_CHOICES = ( )
    GROWTH_FORM_CHOICES = ( ('tr', 'tree'),  ('sh', 'shrub'),  ('ss', 'subshrub'),  ('rs', 'rosette shrub'),  ('gr', 'grass'), ('hb', 'herb'),  ('ss', 'stem-succulent'), )
    GROWTH_RATE_CHOICES=( ('f', 'fast'),  ('m', 'medium'),  ('s', 'slow'), )
    C_PATH_CHOICES = ( ('C4', 'C4'), ('C3','C3'), ('CAM','CAM'), )
    LEAF_SHAPE_CHOICES = ( ('N', 'needle'),  ('S', 'simple'), ('C', 'compound'), )
    LEAF_TYPE_CHOICES = ( ('E', 'evergreen'), ('SD', 'summer deciduous'), ('WD', 'winter deciduous'), ('S', 'succulent'), )
    N_FIXER_CHOICES = ( ('R', 'rhizobia'),  ('C', 'cyanobacteria'), ('A', 'actinorhizal'), )
    LEAF_ODOUR_CHOICES = ( ('P', 'present'),  ('VS', 'very strong'), )
    SPINE_CHOICES = ( ('L', 'leaf'),  ('B', 'branch'), )
    NECTARY_CHOICES = ( ('G', 'generalist'),  ('S', 'specialist'), )
    MYCORRHIZAL_CHOICES = ( ('end', 'endomycorrhizal'), ('ect', 'ectomycorrhizal') )
    genus = models.ForeignKey(Genus)
    hybrid_marker = models.CharField(max_length=1, choices=HYBD_MKR_CHOICES, blank=True, null=True)
    species = models.CharField(max_length=30)
    common_name = models.ManyToManyField(CommonName, blank=True, null=True)
    botanical_synonym = models.ManyToManyField(BotanicalSynonym, blank=True, null=True)
    infraspecific_rank = models.CharField(max_length=10, choices=INFRA_RANK_CHOICES, blank=True, null=True)           
    infraspecific_epithet = models.CharField(max_length=30, blank=True, null=True)
    cultivar = models.CharField(max_length=30, blank=True, null=True)
    growth_form = models.CharField(max_length=15, choices=GROWTH_FORM_CHOICES, blank=True, null=True)
    growth_rate = models.CharField(max_length=10, choices=GROWTH_RATE_CHOICES, blank=True, null=True)
    min_temp = models.IntegerField(blank=True, null=True)
    max_temp = models.IntegerField(blank=True, null=True)
    shade_tolerant = models.NullBooleanField(blank=True, null=True)
    drought_tolerant = models.NullBooleanField(blank=True, null=True)
    salt_tolerant = models.NullBooleanField(blank=True, null=True)
    pollution_tolerant = models.NullBooleanField(blank=True, null=True)
    waterlogging_tolerant = models.NullBooleanField(blank=True, null=True)
    min_ph = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    max_ph = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    preferred_pf = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    carbon_path = models.CharField(max_length=3, choices=C_PATH_CHOICES, blank=True, null=True)
    leaf_shape = models.CharField(max_length=10, choices=LEAF_SHAPE_CHOICES, blank=True, null=True)
    leaf_type = models.CharField(max_length=20, choices=LEAF_TYPE_CHOICES, blank=True, null=True)
    self_fertile = models.NullBooleanField(blank=True, null=True)
    coppices = models.NullBooleanField(blank=True, null=True)
    nitrogen_fixer = models.CharField(max_length=20, choices=N_FIXER_CHOICES, blank=True, null=True)
    leaf_odour = models.CharField(max_length=20, choices=LEAF_ODOUR_CHOICES, blank=True, null=True)
    spines = models.CharField(max_length=20, choices=SPINE_CHOICES, blank=True, null=True)
    wildlife_shelter = models.NullBooleanField(blank=True, null=True)
    wildlife_food = models.NullBooleanField(blank=True, null=True)
    nectary = models.CharField(max_length=20, choices=NECTARY_CHOICES, blank=True, null=True)             
    cultivation_notes = models.TextField(blank=True, null=True)
    mycorrhizal_association = models.CharField(max_length=20, choices=MYCORRHIZAL_CHOICES, blank=True, null=True)
    nuisance = models.ManyToManyField(Nuisance, blank=True, null=True)
    botanical_author = models.ManyToManyField(BotanicalAuthor, blank=True, null=True)
    reproductive_strategy = models.ManyToManyField(ReproductiveStrategy, blank=True, null=True)
    water_need = models.ManyToManyField(WaterNeed, blank=True, null=True)
    plant_part = models.ManyToManyField(PlantPart, blank=True, null=True)
    native_region = models.ManyToManyField(NativeRegion, blank=True, null=True)
    habitat = models.ManyToManyField(Habitat, blank=True, null=True)
    ecological_niche = models.ManyToManyField(EcologicalNiche, blank=True, null=True)
    pollination_mechanism = models.ManyToManyField(PollinationMechanism, blank=True, null=True)
    vegetation_community = models.ManyToManyField(VegetationCommunity, blank=True, null=True)
    medicinal_use = models.ManyToManyField(MedicinalUse, blank=True, null=True)
    edible_use = models.ManyToManyField(EdibleUse, blank=True, null=True)
    other_use = models.ManyToManyField(OtherUse, blank=True, null=True)
    fruiting_time = models.ManyToManyField(FruitingTime, blank=True, null=True)
    flowering_time = models.ManyToManyField(FloweringTime, blank=True, null=True)
    seed_ripening_time = models.ManyToManyField(SeedRipeningTime, blank=True, null=True)
    vegetative_growth_time = models.ManyToManyField(VegetativeGrowthTime, blank=True, null=True)
    root_type = models.ManyToManyField(RootType, blank=True, null=True)
    root_pattern = models.ManyToManyField(RootPattern, blank=True, null=True)

class PlantAdmin(admin.ModelAdmin):
    list_display = ('genus', 'species')

class Poisonous(models.Model):
    part = models.ForeignKey(PlantPart)
    notes = models.TextField(blank=True, null=True)

class Mineral(models.Model):
    MINERAL_CHOICES = ( ('B', 'Boron'),  ('Ca', 'Calcium'), ('Cl', 'Chlorine'), ('Co', 'Cobalt'),  ('Cu', 'Copper'),  ('Fe', 'Iron'),  ('K', 'Potassium'),  ('Mg', 'Magnesium'),  ('N', 'Nitrogen'),  ('Mn', 'Manganese'),  ('Mo', 'Molybdenum'), ('Na', 'Sodium'),  ('Ni', 'Nickel'), ('P', 'Phosphorus'),  ('S', 'Sulfur'),  ('Se', 'Selenium'), ('Si', 'Silicon'), ('Zn', 'Zinc'))
    name = models.CharField(max_length=20, choices=MINERAL_CHOICES)

class DynamicAccumulator(models.Model):
    plant = models.ForeignKey(Plant)
    mineral = models.ForeignKey(Mineral)
    notes = models.TextField(blank=True, null=True)

class DatasetSource(models.Model):
    name = models.CharField(max_length=30)
    data = models.FileField(upload_to='./datasets')

class DatabasePlant(models.Model):
    dataset_source = models.ForeignKey(DatasetSource)
    plant = models.ForeignKey(Plant)

class User(models.Model):
    name = models.CharField(max_length=30)

class UserPlant(models.Model):
    user = models.ForeignKey(User)
    plant = models.ForeignKey(Plant)

admin.site.register(MajorGroup)
admin.site.register(Family)
admin.site.register(Genus)
admin.site.register(Plant, PlantAdmin)
admin.site.register(Nuisance)
admin.site.register(PlantPart)
admin.site.register(EcologicalNiche)
admin.site.register(Ecozone)
admin.site.register(Biome)
admin.site.register(Ecoregion)
admin.site.register(VegetationCommunity)
admin.site.register(NativeRegion)
admin.site.register(ReproductiveStrategy)
admin.site.register(CommonName)
admin.site.register(BotanicalSynonym)
admin.site.register(BotanicalAuthor)
admin.site.register(Habitat)
admin.site.register(PollinationMechanism)
admin.site.register(MedicinalUse)
admin.site.register(EdibleUse)
admin.site.register(Month)
admin.site.register(FruitingTime)
admin.site.register(VegetativeGrowthTime)
admin.site.register(FloweringTime)
admin.site.register(SeedRipeningTime)
admin.site.register(Poisonous)
admin.site.register(Mineral)
admin.site.register(DynamicAccumulator)
admin.site.register(OtherUse)
admin.site.register(WaterNeed)
admin.site.register(RootType)
admin.site.register(RootPattern)
admin.site.register(DatasetSource)
admin.site.register(DatabasePlant)
