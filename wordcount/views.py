from django.http import HttpResponse
from django.shortcuts import render 
import operator

def homepage(request):
    # what send back to the user
    #return 'Hello'
    # we cant just send the string back from this function we have to give to give back http response 
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
   
    wordlist = fulltext.split()

    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else: 
            worddictionary[word] = 1

    sortedWords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext' : fulltext, 'count': len(wordlist), 'sortedWords' : sortedWords})

def about(request):
    return render(request, 'about.html')