from django.db import models

# Create your models here.

class Myuser(models.Model):
    number = models.CharField(max_length=12)
    curr_amount = models.IntegerField(default=25)
    added_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.number
    

DONE_CHOINCE = (
    ('start','start'),
    ('done','done')
)
WHO_WIN = (
    ('yes','yes'),
    ('no','no')
)

class Context(models.Model):
    title = models.CharField(max_length=255)
    yes_amount = models.IntegerField()
    no_amount = models.IntegerField()
    middle_line = models.CharField(max_length=255)
    chance_win = models.IntegerField()
    done = models.CharField(max_length=25,choices=DONE_CHOINCE)
    date = models.DateTimeField()
    win_chance = models.CharField(max_length=20)

    who_win = models.CharField(max_length=20,choices=WHO_WIN,blank=True, null=True)
    def __str__(self):
        return self.title
YES_NO =(
    ('yes','yes'),
    ('no','no')
)

class User_context(models.Model):
    user = models.ForeignKey(to=Myuser, on_delete=models.CASCADE)
    context = models.ForeignKey(to=Context, on_delete=models.CASCADE)
    option = models.CharField(max_length=10,choices=YES_NO)