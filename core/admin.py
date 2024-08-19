from django.contrib import admin
from .models import Category, Product, Customer, Order, Profile
from django.contrib.auth.models import User


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Profile)


# add proofile to user tab
class ProfileInline(admin.StackedInline):
    model = Profile
    
# extend user model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username", 
              "first_name", 
              "last_name", 
              "email", 
              "date_joined",
              "is_superuser",
              "is_active",
              "is_staff"]
    inlines = [ProfileInline]
    
# remove previoous model
admin.site.unregister(User)
admin.site.register(User, UserAdmin)