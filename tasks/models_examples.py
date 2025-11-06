from django.db import models

class FieldExamples(models.Model):

    char = models.CharField(max_length=50, null=False, blank=False, default='')
    text = models.TextField(blank=True)

    integer = models.IntegerField(null=True)
    big_integer = models.BigIntegerField(null=True)
    positive = models.PositiveIntegerField(default=0)
    small = models.SmallIntegerField(null=True)

    decimal = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    floatf = models.FloatField(null=True)

    boolean = models.BooleanField(default=False)
    boolean_nullable = models.BooleanField(null=True)

    date = models.DateField(null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)

    email = models.EmailField(max_length=254, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    uuid = models.UUIDField(null=True, blank=True)
    binary = models.BinaryField(null=True, blank=True)

    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    json = models.JSONField(null=True, blank=True)

    STATUS_CHOICES = [
        ('new', 'New'),
        ('in', 'In Progress'),
        ('done', 'Done'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new', db_index=True, help_text='Task status')

    class Meta:
        verbose_name = 'Field Example'
        verbose_name_plural = 'Field Examples'
