from django.contrib import admin
from cafe.models import Reservation, Menu, Contact, MenuGallery, AboutUs


admin.site.register(Reservation)
admin.site.register(MenuGallery)
admin.site.register(Menu)
admin.site.register(Contact)
admin.site.register(AboutUs)
