from django.db import models
# from .djangolinkshortener import checker
import random 
from string import ascii_letters
# from .models import Shortener


class Shortener(models.Model ):

    original_link = models.CharField(max_length = 500)
    shortened_link = models.URLField(max_length = 100,default=None,blank=True,null=True)

    def random_link(self):
        host='localhost:8000'
        random_links = host+'/'+''.join(random.sample(ascii_letters,6))
        
        while True:
            try:
                if Shortener.objects.get(shortened_link=random_links):
                    random_links = host+'/'+''.join(random.sample(ascii_letters,6))
                    print('Repeating') # just to help recognise that the system repeated an opera
                else:
                    break 
            except:
                return random_links

    def save(self, *args, **kwargs):
        #this line below give to the instance slug field a slug name
        if not self.shortened_link:
            self.shortened_link = self.random_link()
        #this line below save every fields of the model instance
        super(Shortener, self).save(*args, **kwargs) 


