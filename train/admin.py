from django.contrib import admin
from .models import Add_Train
from .models import Add_route
from .models import Passenger
from .models import Book_ticket
from .models import Asehi
# Register your models here.
admin.site.register(Add_Train)
admin.site.register(Add_route)
admin.site.register(Passenger)
admin.site.register(Book_ticket)
admin.site.register(Asehi)