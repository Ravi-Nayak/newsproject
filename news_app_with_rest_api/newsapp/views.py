from django.shortcuts import render
from newsapi import NewsApiClient


def Index(request):
    newsapi = NewsApiClient(api_key="85d5952969de4dce8e935c0f76480689")
    topheadlines = newsapi.get_top_headlines(sources='al-jazeera-english')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []


    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])


    mylist = zip(news, desc, img)

    return render(request, 'index.html', context={"mylist": mylist})


def bbc(request):
    newsapi = NewsApiClient(api_key="85d5952969de4dce8e935c0f76480689")
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []


    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render(request, 'bbc.html', context={"mylist": mylist})


import requests
from django.contrib.auth.decorators import login_required
@login_required()
def india(request):

    url = ('http://newsapi.org/v2/top-headlines?''country=in&''apiKey=85d5952969de4dce8e935c0f76480689')
    response=requests.get(url)
    data = response.json()
    articles=data['articles']
    desc = []
    news = []
    img = []
    link=[]
    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        link.append(myarticles['url'])

        mylist = zip(news, desc,link, img)

    return render(request, 'newsapp/info.html', context={"mylist":mylist})

from newsapp.forms import signForm
from django.http import HttpResponseRedirect
def signup_view(request):
    form=signForm()
    if request.method=='POST':
       form=signForm(request.POST)
       user= form.save() #creating user object
       user.set_password(user.password) #it set the password to the user object
       user.save()
       return HttpResponseRedirect('/accounts/login')
    return render(request,'signup.html',{'form':form})

def logout_view(request):
    return  render(request,'logout.html')