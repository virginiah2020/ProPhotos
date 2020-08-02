from django.db import models

# Create your models here.
class Image(models.Model):
    title=models.CharField(max_length=60)
    # categories = models.ManyToManyField(categories)
    # location = models.ForeignKey(Location,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    