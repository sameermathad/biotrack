from django.contrib import admin
from user_management.models import User, Group, Permission, Role, RolePermission

admin.site.register(User)
admin.site.register(Group)
admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(RolePermission)
