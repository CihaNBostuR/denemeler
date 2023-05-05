# from django.db import models


# class Country(models.Model):
#     name = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name


# class City(models.Model):
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)
#     name = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name
    

# class State(models.Model):
#     city = models.ForeignKey(City, on_delete=models.CASCADE)
#     name = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name


# class Person(models.Model):
#     name = models.CharField(max_length=124)
#     country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
#     city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
#     # state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)

#     def __str__(self):
#         return self.name

from django.db import models


class BasimYili(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class YayinEvi(models.Model):
    basimyili = models.ForeignKey(BasimYili, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    

# class Sinif(models.Model):
#     yayinevi = models.ForeignKey(YayinEvi, on_delete=models.CASCADE)
#     name = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name

# class KitapTuru(models.Model):
#     sinif = models.ForeignKey(Sinif, on_delete=models.CASCADE)
#     name = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name


# class DersTuru(models.Model):
#     kitapturu = models.ForeignKey(KitapTuru, on_delete=models.CASCADE)
#     name = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name


class Kitap(models.Model):
    basimyili = models.ForeignKey(BasimYili, on_delete=models.SET_NULL, blank=True, null=True)
    yayinevi = models.ForeignKey(YayinEvi, on_delete=models.SET_NULL, blank=True, null=True)
    # sinif = models.ForeignKey(Sinif, on_delete=models.SET_NULL, blank=True, null=True)
    # kitapturu = models.ForeignKey(KitapTuru, on_delete=models.SET_NULL, blank=True, null=True)
    # dersturu = models.ForeignKey(DersTuru, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name