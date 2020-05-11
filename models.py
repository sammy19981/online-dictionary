from django.db import models

class DictionaryDb(models.Model):
    letter=models.CharField(max_length=1)
    word=models.CharField(max_length=30)
    definition=models.CharField(max_length=60)
    example=models.CharField(max_length=90)
def __str__(self):
    return"%s %s"%(self.letter,self.word)
