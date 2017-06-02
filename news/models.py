from django.db import models

class Feed(models.Model):
    f_name = models.CharField(max_length=200)
    f_url = models.URLField()
    f_region = models.CharField(max_length=200)
    f_notes = models.TextField()

    def __unicode__(self):
        return self.f_name

class Article(models.Model):
    feed = models.ForeignKey(Feed)
    a_title = models.CharField(max_length=200)
    a_url = models.URLField()
    a_description = models.TextField()
    a_pub_date = models.DateTimeField()
    a_cluster = models.BooleanField(default=False)

    def __unicode__(self):
        return self.a_title

