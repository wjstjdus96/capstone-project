from django.shortcuts import render

from getCommentFromYoutube.utillGetComment import getComments
from django.views.decorators.csrf import csrf_exempt
from django import template

strbun = template.Library()

def index(request):
    return render(request, 'tubeana/index.html')

@csrf_exempt
@strbun.filter("board")
def board(request):
    videoId = request.GET.get("url").split("=")[-1]
    print("영상의 아이디 : " + videoId)

    cm = getComments(videoId)
    for review in cm:
        print(review)
        print()

    return render(request, 'tubeana/board.html', {'videoId': videoId})