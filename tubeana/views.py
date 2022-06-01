from django.shortcuts import render

def index(request):
    return render(request, 'tubeana/index.html')

def board(request):
    videoId = request.GET.get("url").split("=")[-1]
    print("영상의 아이디 : " + videoId)
    return render(request, 'tubeana/board.html', {'videoId': videoId})