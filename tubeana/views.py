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

    context = {
        'videoId': videoId,
        'title': 'vlog | 식욕폭발🔥 뜨끈한 쭈꾸미 샤브샤브, 퇴근하고 김치만두, 콘치즈 식빵, 제철 식재료로 향긋한 미나리무침, 미역국 레시피 (feat. 달다방)',
        'thumbnail': 'https://i.ytimg.com/vi/Trn5Q0NGMNs/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCra5nbPmaGJaSD6bggx-xVj0_qDA',
        'percent': '54.36',
        'top5_text': ['toptext1\n첫번째 댓글 짱짱맨', 'text2', 'text3', 'text4', 'text5'],
        'low5_text': ['lowtext1\n와자넞자ㅓ아러나어라어란라ㅓㅁㄴㅇ러ㅑ더ㅏ저\nㅇ리ㅓ히ㅏ저대거ㅓㅇ랴ㅏ덜얼재 정리ㅓㅇㄴ','text2','text3','text4','text5'],
        'keyword': ['keyword1','keyword2','keyword3','keyword4','keyword5','keyword6','keyword7','keyword8','keyword9','keyword0']
    }


    return render(request, 'tubeana/board.html', context)