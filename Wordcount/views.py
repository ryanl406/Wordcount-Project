from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def Count(request):
    yourText = request.GET['fulltext']
    wordList = yourText.split()
    wordDictionary = {}

    for word in wordList:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1

    dictItems = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse = True)

    return render(request, 'Count.html', {'words':yourText, 'noWords':len(wordList), 'x':dictItems})
