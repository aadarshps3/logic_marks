from django.db import models

# Create your models here.

class marks(models.Model):
    s1=models.IntegerField()
    s2=models.IntegerField()
    s3=models.IntegerField()
    s4=models.IntegerField()
    s5=models.IntegerField()
    s6=models.IntegerField()
    total=models.IntegerField(default=0)
    status=models.CharField(max_length=20,null=True,blank=True)

    def total(self):
        self.total=self.s1+self.s2+self.s3+self.s4+self.s5+self.s6
        return self.total



