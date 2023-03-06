from django.db import models
from biocalc.models.aqua_base_item import AquaBaseItem

class Plant(AquaBaseItem):

    CHOICE = (
        ('0', 'DANGEROUS'), 
        ('1', 'NOT RECOMMENDED'), 
        ('2', 'NOT REQUIRED'), 
        ('3', 'DOES NOT AFFECT'), 
        ('4', 'UNKNOWN'), 
        ('5', 'ALLOWED'), 
        ('6', 'RECOMMENDED'),
        ('7', 'REQUIRED'))

    scientific_name = models.CharField(
        'Scientific name', 
        unique=True, 
        null=True, blank=True, 
        max_length=250) # научное название

    category = models.ForeignKey(
        "PlantCategory",
        related_query_name="Plant category",
        verbose_name="plant category", 
        on_delete=models.CASCADE)

    family = models.CharField(
        null=True, blank=True, 
        max_length=250) # семейство

    origin = models.CharField(
        null=True, blank=True, 
        max_length=250) # родина происхождения

    care = models.CharField(
        null=True, blank=True, 
        max_length=250) # сложность содержания

    ph_comfort_min = models.DecimalField(
        null=True, blank=True, 
        max_digits=4, 
        decimal_places=2) # нижний уровень кислотности для комфортного существования
    ph_comfort_max = models.DecimalField(
        null=True, blank=True, 
        max_digits=4, 
        decimal_places=2) # верхний уровень кислотности для комфортного существования
    ph_survive_min = models.DecimalField(
        null=True, blank=True, 
        max_digits=4, 
        decimal_places=2) # нижний уровень кислотности для возможности существования
    ph_survive_max = models.DecimalField(
        null=True, blank=True, 
        max_digits=4, 
        decimal_places=2) # верхний уровень кислотности для возможности существования
    
    water_hardness_comfort_min = models.DecimalField(
        null=True, blank=True, 
        max_digits=4, 
        decimal_places=2) # нижний уровень жесткости для комфортного существования
    water_hardness_comfort_max = models.DecimalField(
        null=True, blank=True, 
        max_digits=4, 
        decimal_places=2) # верхний уровень жесткости для комфортного существования
    water_hardness_survive_min = models.DecimalField(
        null=True, blank=True, 
        max_digits=4, 
        decimal_places=2) # нижний уровень жесткости для возможности существования
    water_hardness_survive_max = models.DecimalField(
        null=True, blank=True, 
        max_digits=4, 
        decimal_places=2) # верхний уровень жесткости для возможности существования
    
    temperature_comfort_min = models.DecimalField(
        null=True, blank=True, 
        max_digits=3, 
        decimal_places=1) # минимальная температура для комфортного существования
    temperature_comfort_max = models.DecimalField(
        null=True, blank=True, 
        max_digits=3, 
        decimal_places=1) # максимальная температура для комфортного существования
    temperature_survive_min = models.DecimalField(
        null=True, blank=True, 
        max_digits=3, 
        decimal_places=1) # минимальная температура для возможности существования
    temperature_survive_max = models.DecimalField(
        null=True, blank=True, 
        max_digits=3, 
        decimal_places=1) # максимальная температура для возможности существования
    
    aeration = models.CharField(
        choices=CHOICE, 
        max_length=1, 
        default="4") # необходимость принудительной аэрации
    co2 = models.CharField(
        choices=CHOICE, 
        max_length=1, 
        default="4") # необходимость дополнительного co2)
    filtration = models.CharField(
        choices=CHOICE, 
        max_length=1, 
        default="4") # необходимость и качество фильтрации
    illumination_intensity = models.PositiveSmallIntegerField(
        "Illumination (lumen/liter)", 
        default=0) # необходимая интенсивность освещения
    illumination_duration = models.CharField(
        "Duration of illumination (hours/day)", 
        max_length=2, 
        default="0") # необходимая длительность освещения
    streams = models.CharField(
        choices=CHOICE,
        max_length=1, 
        default="4") # онтошение к течениям
    soil = models.CharField(
        null=True, blank=True, 
        max_length=250) # предпочтительный грунт
    water_change  = models.CharField(
        null=True, blank=True, 
        max_length=25) # рекомендумая частота и объем подмен воды
    plant_value = models.IntegerField(
        auto_created=True,
        default=0)

    class Meta:
        verbose_name = "Plant"
        verbose_name_plural = "Plants"
        ordering = ("id",)

    def __str__(self) -> str:
        return f"{self.id}) {self.name}"


    def save(self, *args, **kwargs):
        
        if self.plant_value < 0: self.plant_value = 0 
        # if self.scientific_name = 
        # if self.family =  
        # if self.origin =  
        # if self.care =  
        if self.ph_comfort_min not in range(0,14): self.ph_comfort_min = None
        if self.ph_comfort_max not in range(0,14): self.ph_comfort_max = None
        if self.ph_survive_min not in range(0,14): self.ph_survive_min = None 
        if self.ph_survive_max not in range(0,14): self.ph_survive_max = None
        if self.water_hardness_comfort_min not in range(0,30): self.water_hardness_comfort_min =  None
        if self.water_hardness_comfort_max not in range(0,30): self.water_hardness_comfort_max =  None
        if self.water_hardness_survive_min not in range(0,30): self.water_hardness_survive_min =  None
        if self.water_hardness_survive_max not in range(0,30): self.water_hardness_survive_max =  None
        if self.temperature_comfort_min not in range(10,40): self.temperature_comfort_min =  None
        if self.temperature_comfort_max not in range(10,40): self.temperature_comfort_max =  None
        if self.temperature_survive_min not in range(10,40): self.temperature_survive_min =  None
        if self.temperature_survive_max not in range(10,40): self.temperature_survive_max =  None
        if int(self.aeration) not in range(0,7): self.aeration =  "4"
        if int(self.co2) not in range(0,7): self.co2 =  "4"
        if int(self.filtration) not in range(0,7): self.filtration =  "4"
        if int(self.streams) not in range(0,7): self.streams =  "4"
        if self.illumination_intensity < 0: self.illumination_intensity = 0
        if self.illumination_duration not in range(0,24): self.illumination_duration =  0
        # if self.soil =  
        # if self.water_change =  
        print("plant model, self: ", self)
        super(Plant, self).save(*args, **kwargs)

    