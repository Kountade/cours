from django.urls import path
from blog import views
urlpatterns = [
    path("", views.acceuil, name="acceuil"),
    path("galerie", views.galerie, name="galerie"),
    path("news", views.news, name="news"),
    path("service", views.services, name="services"),
    path("illustrators", views.illustrators, name="illustrators"),
    path("blogs", views.blogs, name="blogs"),
    path('detail/<str:title>', views.detail, name="detail"),
    path("allserie", views.allserie, name="allserie"),
    path("apropos", views.apropos, name="apropos"),
    path("photoshos", views.photoshos, name="photoshos"),
    path("python", views.python, name="python"),
    path('pythondetail/<str:title>', views.pythondetail, name="pythondetail"),
    path("php", views.php, name="php"),
    path('phpdetail/<str:title>', views.phpdetail, name="phpdetail"),
    path("dart", views.dart, name="dart"),
    path('dartdetail/<str:title>', views.dartdetail, name="dartdetail"),
    path("java", views.java, name="java"),
    path("csharp", views.csharp, name="csharp"),
    path('scharpdetail/<str:title>', views.scharpdetail, name="scharpdetail"),
    path("javascript", views.javascript, name="javascript"),
    path('javascriptdetail/<str:title>',
         views.javascriptdetail, name="javascriptdetail"),
    path("detailcours", views.detailcours, name="detailcours"),
    path("register", views.register, name="register"),
    path("login", views.logIn, name="login"),
    path("logout", views.log_out, name="logout"),
    # path('activate/<uidb64>/token', views.activate, name='activate')
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         views.activate, name='activate'),
    # path('activate/<uidb64>/token', views.activate, name='activate')


]
