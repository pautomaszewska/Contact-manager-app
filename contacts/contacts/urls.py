"""contacts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from mail.views import AddPerson, AddPhone, AddMail, AddAddress, ShowAll, PersonDetails, EditPerson, EditPhone, \
    EditMail, EditAddress, DeletePerson, DeletePhone, DeleteMail, DeleteAddress, Groups, AddGroup, GroupDetails, EditGroup, \
    DeleteGroup, DeleteFromGroup, Search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ShowAll.as_view(), name='showall'),
    path('addperson', AddPerson.as_view(), name='addperson'),
    path('addphone/<id>', AddPhone.as_view(), name='addphone'),
    path('addmail/<id>', AddMail.as_view(), name='addmail'),
    path('addaddress/<id>', AddAddress.as_view(), name='addaddress'),
    path('details/<id>', PersonDetails.as_view(), name='details'),
    path('editperson/<id>', EditPerson.as_view(), name='editperson'),
    path('editphone/<id>', EditPhone.as_view(), name='editphone'),
    path('editmail/<id>', EditMail.as_view(), name='editmail'),
    path('editaddress/<id>', EditAddress.as_view(), name='editaddress'),
    path('deleteperson/<id>', DeletePerson.as_view(), name='deleteperson'),
    path('deletephone/<id>', DeletePhone.as_view(), name='deletephone'),
    path('deletemail/<id>', DeleteMail.as_view(), name='deletemail'),
    path('deleteaddress/<id>', DeleteAddress.as_view(), name='deleteaddress'),
    path('groups', Groups.as_view(), name='groups'),
    path('addgroup', AddGroup.as_view(), name='addgroup'),
    path('groupdetails/<group_id>', GroupDetails.as_view(), name='groupdetails'),
    path('editgroup/<group_id>', EditGroup.as_view(), name='editgroup'),
    path('deletegroup/<group_id>', DeleteGroup.as_view(), name='deletegroup'),
    path('deletefrom/<id>/<group_id>', DeleteFromGroup.as_view(), name='deletefrom'),
    path('search', Search.as_view(), name='search'),


]
