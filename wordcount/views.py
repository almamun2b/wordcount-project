import operator
from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html', {})


def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            # increase
            worddictionary[word] += 1
        else:
            # add to the dictionary
            worddictionary[word] = 1

    sortedword = sorted(worddictionary.items(),
                        key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext,
                                          'count': len(wordlist), 'sortedword': sortedword})


def about(request):
    return render(request, 'about.html', {'HiThere': 'This is Mamun'})


def demo_http_response(request):
    return HttpResponse('<h1>This is demo_http_response</h1>')
