
from django.db import models
from .aqua_base_item import AquaBaseItem


class Fish(AquaBaseItem):
    """
    Model of Fish 

    Fish_value - calculate from length of fishes
    """

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
        "FishCategory", 
        related_query_name="Fish category",
        verbose_name="category", 
        on_delete=models.CASCADE)

    family = models.CharField(
        null=True, blank=True, 
        max_length=250) # семейство

    origin = models.CharField(
        null=True, blank=True, 
        max_length=250) # родина происхождения

    social = models.CharField(
        null=True, blank=True, 
        max_length=250) # отношение к другим обитателям

    flock = models.CharField(
        null=True, blank=True, 
        max_length=250) # минимальная стайка

    tank_level = models.CharField(
        null=True, blank=True, 
        max_length=25) # в какой асти аквариума предпочитает обитать
    min_tank_size_one = models.CharField(
        'Minimum area for one fish', 
        null=True, blank=True, 
        max_length=25) # минимальная площадь на одну особь
    min_tank_size_pair = models.CharField(
        'Minimum area for a pair of fish', 
        null=True, blank=True, 
        max_length=25) # -//- на пару особей
    min_tank_size_next_one = models.CharField(
        'Minimum area for each subsequent fish', 
        null=True, blank=True, 
        max_length=25) # -//- на каждую дополнительную особь
    min_water_volume_one = models.CharField(
        'Minimum volume for one fish', 
        null=True, blank=True, 
        max_length=5) # минимальный объем воды для одной особи
    min_water_volume_pair = models.CharField(
        'Minimum volume for a pair of fish', 
        null=True, blank=True, 
        max_length=5) # -//- для пары особей
    min_water_volume_next_one = models.CharField(
        'Minimum volume for each subsequent fish', 
        null=True, blank=True, 
        max_length=5) # -//- для каждой последующей особи

    diet = models.CharField(
        null=True, blank=True, 
        max_length=250) # чем и как часто питается
    breeding = models.CharField(
        null=True, blank=True, 
        max_length=250) # как размножается
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
    filtration = models.CharField(
        choices=CHOICE, 
        max_length=1, 
        default="4") # необходимость и качество фильтрации
    illumination = models.CharField(
        choices=CHOICE, 
        max_length=1, 
        default="4") # необходимость освещения, длительность и интенсивность
    water_transparency = models.CharField(
        choices=CHOICE, 
        max_length=1, 
        default="4") # предпочтительная прозрачность воды
    shelters = models.CharField(
        choices=CHOICE, 
        max_length=1, 
        default="4") # потребность в укрытиях
    open_space = models.CharField(
        choices=CHOICE, 
        max_length=1, 
        default="4") # потребность в свободном месте для плавания
    natural_driftwood = models.CharField(
        choices=CHOICE, 
        max_length=1, 
        default="4") # потребность в натуральных корягах
    living_plants = models.CharField(
        choices=CHOICE, 
        max_length=1, 
        default="4") # отношение к живым растениям
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

    lifespan = models.CharField(
        null=True, blank=True, 
        max_length=3) # продолжительность жизни
    
    male_average_length = models.CharField(
        null=True, blank=True, 
        max_length=5) # средний размер самцов
    female_average_length = models.CharField(
        null=True, blank=True, 
        max_length=5) # средний размер самок

    fish_value = models.IntegerField(
        null=True, blank=True)
    


    class Meta:
        verbose_name = "Fish"
        verbose_name_plural = "Fishes"
        ordering = ("id",)

    @property
    def get_fish_value(self):
        if self.male_average_length and self.female_average_length:
            if self.male_average_length < self.female_average_length:
                return self.female_average_length
            else:
                return self.male_average_length
        else: return 0

    def save(self, *args, **kwargs):
        self.fish_value = self.get_fish_value
        return super(Fish, self).save(*args, **kwargs)
