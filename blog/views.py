from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import requests
from django.core.paginator import Paginator

API_KEY = "758811fbc4dc45fa9ad7c4f52f786b6e"


# Create your views here.

def news(request):
    url = f'https://newsapi.org/v2/top-headlines?language=en&category=technology&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()

    articles = data['articles']
    articles
    context = {
        'articles': articles
    }
    return render(request, 'blog/new.html', context)


def acceuil(request):

    list_top = top.objects.all()
    content = {"list_top": list_top}
    return render(request, "blog/index.html", content)


def galerie(request):
    list_galerie = gale.objects.all()
    content = {"list_galerie": list_galerie}
    return render(request, "blog/galerie.html", content)


def services(request):
    list_services = service.objects.all()
    content = {"list_services": list_services}
    return render(request, "blog/services.html", content)


def illustrators(request):
    lis_illus = illustrator.objects.all()
    context = {"lis_illus": lis_illus}
    return render(request, "blog/illustrator.html", context)


def blogs(request):
    list_blog = blog.objects.all()
    page = Paginator(list_blog, 8)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {"page": page}

    return render(request, "blog/blog.html", context)


def detail(request, title: str):
    product_object = blog.objects.get(title=title)
    return render(request, 'blog/blog_plus.html', {'blog': product_object})


def photoshos(request):
    list_photo = photoshop.objects.all()
    context = {"list_photo": list_photo}

    return render(request, "blog/photoshop.html", context)


def python(request):
    pithon1 = courspython.objects.filter(categorie_id=1).values()
    pithon2 = courspython.objects.filter(categorie_id=2).values()
    pithon3 = courspython.objects.filter(categorie_id=3).values()
    pithon4 = courspython.objects.filter(categorie_id=4).values()
    pithon5 = courspython.objects.filter(categorie_id=5).values()
    pithon6 = courspython.objects.filter(categorie_id=6).values()
    pithon7 = courspython.objects.filter(categorie_id=7).values()
    pithon8 = courspython.objects.filter(categorie_id=8).values()
    pithon9 = courspython.objects.filter(categorie_id=9).values()
    return render(request, "blog/python/python.html", {"pithon1": pithon1, "pithon2": pithon2, "pithon3": pithon3, "pithon4": pithon4, "pithon5": pithon5, "pithon6": pithon6, "pithon7": pithon7, "pithon8": pithon8, "pithon9": pithon9, })


def pythondetail(request, title: str):
    try:
        postepy = courspython.objects.get(title=title)

    except courspython.DoesNotExist:
        raise ("le poste n'excite pas")
    return render(request, 'blog/python/python_detail.html', {'postepy': postepy})


def php(request):
    data1 = coursphp.objects.filter(categorie_id=1).values()
    data2 = coursphp.objects.filter(categorie_id=2).values()
    data3 = coursphp.objects.filter(categorie_id=3).values()
    data4 = coursphp.objects.filter(categorie_id=4).values()
    data5 = coursphp.objects.filter(categorie_id=5).values()
    data6 = coursphp.objects.filter(categorie_id=6).values()
    data7 = coursphp.objects.filter(categorie_id=7).values()
    data8 = coursphp.objects.filter(categorie_id=8).values()
    data9 = coursphp.objects.filter(categorie_id=9).values()
    data10 = coursphp.objects.filter(categorie_id=10).values()
    data11 = coursphp.objects.filter(categorie_id=9).values()
    data12 = coursphp.objects.filter(categorie_id=10).values()
    return render(request, "blog/php/php.html", {"data1": data1, "data2": data2, "data3": data3, "data4": data4, "data5": data5, "data6": data6, "data7": data7, "data8": data8, "data9": data9, "data10": data10, "data11": data11, "data12": data12, })


def phpdetail(request, title: str):
    try:
        postephp = coursphp.objects.get(title=title)

    except coursphp.DoesNotExist:
        raise ("le poste n'excite pas")
    return render(request, 'blog/php/php_detail.html', {'postephp': postephp})


def javascript(request):

    scripts1 = coursjavascript.objects.filter(categorie_id=1).values()
    scripts2 = coursjavascript.objects.filter(categorie_id=2).values()
    scripts3 = coursjavascript.objects.filter(categorie_id=3).values()
    scripts4 = coursjavascript.objects.filter(categorie_id=3).values()
    scripts5 = coursjavascript.objects.filter(categorie_id=3).values()
    scripts6 = coursjavascript.objects.filter(categorie_id=3).values()
    scripts7 = coursjavascript.objects.filter(categorie_id=3).values()
    return render(request, "blog/javascript/javascript.html", {"scripts1": scripts1, "scripts2": scripts2, "scripts3": scripts3, "scripts4": scripts4, "scripts5": scripts5, "scripts6": scripts7, "scripts2": scripts7})


def javascriptdetail(request, title: str):
    try:
        poste = coursjavascript.objects.get(title=title)

    except coursjavascript.DoesNotExist:
        raise ("le poste n'excite pas")
    return render(request, 'blog/javascript/javascript_detail.html', {'poste': poste})


def dart(request):
    dart1 = coursdart.objects.filter(categorie_id=1).values()
    dart2 = coursdart.objects.filter(categorie_id=2).values()
    dart3 = coursdart.objects.filter(categorie_id=3).values()
    return render(request, "blog/dart/dart.html", {"dart1": dart1, "dart2": dart2, "dart3": dart3})


def dartdetail(request, title: str):
    try:
        postedrt = coursdart.objects.get(title=title)

    except coursdart.DoesNotExist:
        raise ("le poste n'excite pas")
    return render(request, "blog/dart/dart_detail.html", {"postedrt": postedrt})


def java(request):
    return render(request, "blog/java/java.html",)


def csharp(request):
    sharp1 = courscsharp.objects.filter(categorie_id=1).values()
    sharp2 = courscsharp.objects.filter(categorie_id=2).values()
    sharp3 = courscsharp.objects.filter(categorie_id=3).values()
    return render(request, "blog/csharp/csharp.html", {"sharp1": sharp1, "sharp2": sharp2, "sharp3": sharp3})


def scharpdetail(request, title: str):
    try:
        postechp = courscsharp.objects.get(title=title)

    except courscsharp.DoesNotExist:
        raise ("le poste n'excite pas")
    return render(request, 'blog/csharp/csharp_detail.html', {'postechp': postechp})


def detailcours(request):
    return render(request, "blog/cours/detailcours.html",)


def apropos(request):
    return render(request, "blog/apropos.html")


def allserie(request):

    list_tuto = tutocategorie.objects.all()
    content = {"list_tuto": list_tuto}
    return render(request, "blog/tuto/all.html", content)
