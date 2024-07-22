from django.contrib import admin     # type: ignore

# Register your models here.
from .models import ScrapedData

admin.site.register(ScrapedData)
