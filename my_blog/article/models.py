from django.db import models

# Create your models here.
class Arcicle(models.Model):
    #标题
    title = models.CharField(max_length=100)
    #作者
    author = models.CharField(max_length=50,blank=True)
    #标签
    category = models.CharField(max_length=50,blank=True)
    #时间
    date_time = models.DateField(auto_now_add=True)
    #内容
    content = models.TextField(blank=True,null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering=['-date_time']