# this is created by me
from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
    #return HttpResponse('''<h1>Sudip</h1><a href="https://www.google.com/search?sxsrf=ACYBGNTW-wkHeU4Hml3-PfutYS3Y2LPZGg%3A1581045940006&source=hp&ei=s9g8XsCYO5vvz7sPosOoiAc&q=delhi+poll&btnK=Google+Search"> www.deccanherald.com </a>''')

#def about(request):
   # return HttpResponse("about Sudip Gupta")
    
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("home")
def ex1(request):
    s='''<h2>Navigation Bar<br></h2>
              <a href="https://www.facebook.com/">Facebook</a><br>
              <a href="https://www.google.com/">Google</a><br>
              <a href="https://www.flipkart.com/">Flipkart</a>'''
    return HttpResponse(s)
def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    #print(removepunc)
    #print(djtext)
    if removepunc=="on":
        #analyzed=djtext
        punctuation='''!()-[]{};:'"\,<>./?@#$%^&*_'''
        analyzed=""
        for char in djtext:
             if char not in punctuation:
                analyzed=analyzed+char

        params={'purpose':'remove punctuations','analyze_text':analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyze_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyze_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyze_text': analyzed}
        #djtext=analyzed
    if(removepunc!="on",fullcaps!='on',newlineremover!="on" and extraspaceremover != "on"):
        return HttpResponse("error: select an option")
    #else:
        #return HttpResponse("error")

    return render(request, 'analyze.html', params)

    #return HttpResponse("remove punc")

#def capitalfirst(request):
  #  return HttpResponse("capital first")

#def newlineremove(request):
 #   return HttpResponse("new line remove")

#def spaceremove(request):
 #   return HttpResponse("space remove")

#def charcount(request):
 #   return HttpResponse("char count <a href='/'>back</a>")
