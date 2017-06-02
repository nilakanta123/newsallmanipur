import feedparser
import datetime
from .models import Article, Feed
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView

class HomeView(ListView):
	template_name = "index.html"
	context_object_name = "articles"
	paginate_by = 6
	
	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['heading'] = "News Articles in our database"
		return context

	def get_queryset(self):
		return Article.objects.all().order_by('-a_pub_date')

def cron(request):
    feed_list = Feed.objects.all()

    for feed in feed_list:
    	try:
    		feed_data = feedparser.parse(feed.f_url)
    	except:
    		print ("Feed Parsing Error")
    		pass
    	for entry in feed_data.entries:
	        existing_entry = Article.objects.filter(a_title=entry.title)
	        if len(existing_entry) == 0:
	            article = Article()
	            article.a_title = entry.title
	            article.a_url = entry.link
	            article.a_description = entry.description
	            d = datetime.datetime(*(entry.published_parsed[0:6]))
	            date_string = d.strftime('%Y-%m-%d %H:%M:%S')
	            article.a_pub_date = date_string
	            article.feed = feed
	            article.save()

    return render(request, 'cron.html')






