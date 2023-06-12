from random import sample
from main import models

def radom_objects(models,number):
    result=set(sample(list(models),number))
    return result