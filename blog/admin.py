
from django.contrib import admin
from.models import *

class Admincategory(admin.ModelAdmin): 
    list_display = ("name","date_added")

class Admintop(admin.ModelAdmin): 
    list_display = ("title","image","date_added")



class Admingale(admin.ModelAdmin):
    list_display = ("title","image","date_added")



class Adimillustrator(admin.ModelAdmin):
 list_display = ("title","image","description","date_added")

class Adminservice(admin.ModelAdmin):
    list_display = ("title","image","description","date_added")

class Adminblog(admin.ModelAdmin):
    list_display = ("title","image","description","date_added")

class Adminphotoshop(admin.ModelAdmin):
    
    list_display = ("title","image","description","date_added")
    
    
    
    
class AdminCategoryphp(admin.ModelAdmin):
    list_display = ("name","description")
class Admincoursphp(admin.ModelAdmin):
    list_display = ("categorie","title","code","description","date_added")
    
    
    

class AdminCategoryjavas(admin.ModelAdmin):
    list_display = ("name","description")
class Admincoursjavascript(admin.ModelAdmin):
    list_display = ("categorie","title","code","description","date_added")
    


    
    

class AdminCategoryjava(admin.ModelAdmin):
    list_display = ("name","description")
class Admincoursjava(admin.ModelAdmin):
 list_display = ("categorie","title","code","description","date_added","resultat")



class AdminCategorypython(admin.ModelAdmin):
    list_display = ("name","description")
class Admincourspython(admin.ModelAdmin):
    list_display = ("categorie","title","code","description","date_added","resultat")



class AdminCategorydart(admin.ModelAdmin):
    list_display = ("name","description")
class Admincoursdart(admin.ModelAdmin):
   list_display = ("categorie","title","code","description","date_added","resultat")


class AdminCategorycsharp(admin.ModelAdmin):
    list_display = ("name","description")
class Admincourscsharp(admin.ModelAdmin):
    list_display = ("categorie","title","code","description","date_added","resultat")


admin.site.register(category, Admincategory) 
admin.site.register(top, Admintop) 
admin.site.register(gale,Admingale) 
admin.site.register(illustrator,Adimillustrator) 
admin.site.register(service, Adminservice)
admin.site.register(blog, Adminblog) 
admin.site.register(photoshop,Adminphotoshop)
admin.site.register(coursphp,Admincoursphp)
admin.site.register(coursjava, Admincoursjava)
admin.site.register(coursjavascript, Admincoursjavascript) 
admin.site.register(courspython,Admincourspython)
admin.site.register(coursdart,Admincoursdart)
admin.site.register(courscsharp,Admincourscsharp)
# Register your models here.
admin.site.register(Categoryjavas,AdminCategoryjavas)
admin.site.register(Categorydart,AdminCategorydart)
admin.site.register(Categoryphp,AdminCategoryphp)
admin.site.register(Categoryjava,AdminCategoryjava)
admin.site.register(Categorypython,AdminCategorypython)
admin.site.register(Categorycsharp,AdminCategorycsharp)