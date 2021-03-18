from django.db import models

class Cryptocurrency(models.Model): 
    cryptocurrency = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    market_cap = models.CharField(max_length=100)
    change = models.CharField(max_length=100)

    def __str__(self):
        return self.cryptocurrency


#https://dev.to/coderasha/implement-real-time-updates-with-django-rest-framework-building-cryptocurrency-api-1kld
# https://gist.github.com/tomysmile/fe41f798516468a4c32bfbafbf7c9c12
#       