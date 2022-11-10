from django.db import models

class Link(models.Model):
    name = models.CharField(max_length=500 , default='')
    video_url = models.URLField(max_length=1000)
    image = models.ImageField(null=True)



    @staticmethod
    def get_all_links():
        return Link.objects.all()

    @staticmethod
    def get_link_by_name(MovieName):
        return Link.objects.filter(name=MovieName)

    def __str__(self):
        return self.name