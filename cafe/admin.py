from django.contrib import admin
from cafe.models import Reservation, Menu, Contact, MenuGallery, AboutUs
# Register your models here.

admin.site.register(Reservation)
admin.site.register(Menu)
admin.site.register(Contact)
admin.site.register(MenuGallery)
admin.site.register(AboutUs)