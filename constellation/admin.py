from django.contrib import admin

# Register your models here.

from .forms import SignUpForm
from .models import SignUp

admin.site.register( SignUp )