from django.db import models
from django.db.models.fields.related import ForeignKey


class top(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title


class category(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name


class gale(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title


class illustrator(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField()
    date_added = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=50000)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title


class photoshop(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField()
    date_added = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=50000)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title


class service(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField()
    description = models.TextField(max_length=50000)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title


class blog(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField()
    date_added = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=50000)
    full_description = models.TextField(max_length=50000000)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title


class Categoryphp(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class coursphp(models.Model):
    categorie = models.ForeignKey(
        Categoryphp, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=50000)
    code = models.TextField(max_length=50000)
    resultat = models.TextField(max_length=50000)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return self.title


class Categoryjava(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class coursjava(models.Model):
    categorie = models.ForeignKey(
        Categoryjava, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=50000)
    code = models.TextField(max_length=50000)
    date_added = models.DateTimeField(auto_now_add=True)

    resultat = models.TextField(max_length=50000)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return self.title


class Categoryjavas(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class coursjavascript(models.Model):
    categorie = models.ForeignKey(
        Categoryjavas, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=50000)
    code = models.TextField(max_length=50000)
    date_added = models.DateTimeField(auto_now_add=True)

    resultat = models.TextField(max_length=50000)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return self.title


class Categorydart(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class coursdart(models.Model):
    categorie = models.ForeignKey(
        Categorydart, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=50000)
    code = models.TextField(max_length=50000)
    date_added = models.DateTimeField(auto_now_add=True)
    resultat = models.TextField(max_length=50000)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return self.title


class Categorypython(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class courspython(models.Model):
    categorie = models.ForeignKey(
        Categorypython, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=50000)
    code = models.TextField(max_length=50000)
    date_added = models.DateTimeField(auto_now_add=True)
    resultat = models.TextField(max_length=50000)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return self.title


class Categorycsharp(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class courscsharp(models.Model):
    categorie = models.ForeignKey(
        Categorycsharp, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=50000)
    code = models.TextField(max_length=50000)
    date_added = models.DateTimeField(auto_now_add=True)
    resultat = models.TextField(max_length=50000)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title


class tutocategorie(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField()
    description = models.TextField(max_length=50000)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title
