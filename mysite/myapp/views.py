from django.shortcuts import render, HttpResponse
#from twitter_api.models import User
import twitter
# Create your views here.


def index(request):
	#return HttpResponse('hello world')
	return render(request, "myapp/search.html")

def result(request):
	#OAUTH_TOKEN_HISTORY = True
	#OAUTH_TOKENS_TWITTER_CLIENT_ID = '15835972' # application ID
	#OAUTH_TOKENS_TWITTER_CLIENT_SECRET = 'xe3lb7uDFTRjC08F26qyq6YzmxsYFamZrJcuMYPFDTfMkv55U4' # application secret key
	#OAUTH_TOKENS_TWITTER_USERNAME = 'Vincent61703775' # user login
	#OAUTH_TOKENS_TWITTER_PASSWORD = 'MyTwitter@9037' # user password

	api = twitter.Api(consumer_key='KgONcuQaeXtAP7wOikj7zMgvB',
  		consumer_secret='xe3lb7uDFTRjC08F26qyq6YzmxsYFamZrJcuMYPFDTfMkv55U4',
  		access_token_key='541678864-TUYTq3kQwmogm4hK6rtlJByUbWwNrstGkt9sVGmn',
  		access_token_secret='hiGyLAMNfLdgBupE0qFanH7Iru0zmJ9S7NgJws1v5T8aS')
	name = str(request.POST["uname"])
	t = api.GetUserTimeline(screen_name=name, count=10)
	tweets = [i.AsDict() for i in t]
	context = {
		"tweets": tweets
	}
	#user = User.remote.fetch(name)
	#user.fetch_statuses(count=5)
	print('Name is %s' %(name))
	print(tweets)	
	#return HttpResponse(name)
	return render(request, "myapp/sign.html", context)
