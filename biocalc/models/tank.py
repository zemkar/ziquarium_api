from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Tank(models.Model):

    name = models.CharField(
        unique=True, 
        max_length=100, 
        db_index=True)
    slug = models.SlugField(
        max_length=100, 
        unique=True,
        blank=True, null=True) # уникальная часть ссылки на этот объект

    tank_volume = models.PositiveIntegerField(
        'Tank volume (l)')
    tank_dimensions = models.CharField(
        'Tank width (cm)',
        max_length=15, 
        null=True, blank=True)

    tank_filter = models.PositiveIntegerField(
        'Filter (l/h)', 
        null=True, blank=True, 
        default=0)
    tank_compressor = models.PositiveIntegerField(
        'Compressor (l/h)', 
        null=True, blank=True, 
        default=0)
    soil_volume = models.PositiveIntegerField(
        'Volume of soil (l)', 
        null=True, blank=True, 
        default=0)
    soil_type = models.CharField(
        "Soil type", 
        max_length=20)
    decor_volume = models.PositiveIntegerField(
        'Volume of decor (l)', 
        null=True, blank=True, 
        default=0)
    fish_points = models.PositiveIntegerField(
        null=True, blank=True)



    class Meta:
        verbose_name = "Tank"
        verbose_name_plural = "Tanks"

    def __str__(self):
        return self.name + ' (' + str(self.fish_points) + ' Pts)'

    @property
    def calculate_fish_points(self):
        if not self.tank_filter:
            self.tank_filter = 0
        if not self.tank_compressor:
            self.tank_compressor = 0
        fish_points = self.tank_volume + int(self.tank_filter * 0.5) + int(self.tank_compressor * 0.25)
        if fish_points > self.tank_volume * 2:
            fish_points = self.tank_volume * 2
        return fish_points
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.fish_points = self.calculate_fish_points
        return super(Tank, self).save(*args, **kwargs)

        

    def get_absolute_url(self):
        return reverse("biocalc:tanks", kwargs={'pk':str(self.pk), 'slug':self.slug}) #[self.id, self.slug])
    
        
