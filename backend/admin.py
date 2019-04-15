from django.contrib import admin
from .models import User, Major, Question, Answer


admin.site.register(User)
admin.site.register(Major)
admin.site.register(Question)
admin.site.register(Answer)
