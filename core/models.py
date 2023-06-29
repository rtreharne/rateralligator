from django.db import models
from django.utils.text import slugify

class Alligator(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    pin = models.IntegerField()
    show_comments = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        # If the slug has already been used, append a number to the end of the slug
        if Alligator.objects.filter(slug=self.slug).exists():
            # Get all the alligators with the same slug
            alligators = Alligator.objects.filter(slug=self.slug)
            number_of_alligators = len(alligators)
            self.slug += str(number_of_alligators + 1)
        super(Alligator, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Rating(models.Model):
    alligator = models.ForeignKey(Alligator, on_delete=models.CASCADE)
    rating = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.alligator.slug + " - " + str(self.rating)
    
class Comment(models.Model):
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    comment = models.TextField()
    agree_count = models.IntegerField(default=0)
    disagree_count = models.IntegerField(default=0)
    block_count = models.IntegerField(default=0)
    hide = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rating.alligator.slug + " - " + str(self.rating.rating) + " - " + self.comment


