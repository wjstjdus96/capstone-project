from tubeana.dataFrame import df

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
        'title': 'ENG SUB) 스위스 브이로그 • 영국 런던 여행 & 스위스 여행 브이로그 EP2 | 유럽여행 브이로그, 인터라켄 베른 취리히 여행, 사랑의불시착, switzerland vlog',
        'thumbnail': 'https://i.ytimg.com/vi/OpcvdVzB0Tw/hqdefault.jpg?sqp=-oaymwEcCOADEI4CSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBJckJfi-_WOE3_5hDMSXa1KC_O4Q',
        'percent': '59.4532457754456643',
        'top5_text': ['스위스 여행.. 넘모 부럽습니다🥺 저도 나중에 방학이나 졸업하면 유일님처럼 스위스로 꼭 여행 한 번 가야겠어요🥰', '스위스가 자연에 압도될만큼 너무 예쁘다고 들었는데 정말 분위기가 너무 좋아요😊', 
        '평화로운 풍경에 힐링이 저절로 되네요!!\n한 번 더 졸업 축하해요!!', '풍경을 예쁘게 너무 잘담으시는거같아요 ㅜㅜㅜㅜㅜ', '와 스위스의 풍경은 정말 대단해요. 여행하고 싶을 때 바로 행동으로 옮길 수 있다는 게 얼마나 행복한지 지금은 코로나 때문에 여행 갈 수 없는 곳이 많으니 잘되면 꼭 한 번 가보고 싶어요.'],
        'low5_text': ['lowtext1\n와자넞자ㅓ아러나어라어란라ㅓㅁㄴㅇ러ㅑ더ㅏ저\nㅇ리ㅓ히ㅏ저대거ㅓㅇ랴ㅏ덜얼재 정리ㅓㅇㄴ','text2','text3','text4','text5'],
        'keyword': ['축구','손흥민','토트넘','한국','월드컵','운동','대표팀','챔스','결승','황희찬'],
        'likes': ['95334','34567','12434','207','2'],
        'likes_text':['진짜 나레이션이랑 멤버들 콩트케미랑 애드립 모든게 완벽했던 특집ㅋㅋㅋㅋㅋㅋㅋㅋㅋ','이 편 너무 좋음 ㅋㅋ 약간 흐릿한 저 날씨도 좋고\n다들 분위기도 좋고','이편은 진짜 봐도봐도 안질림ㅋㅋㅋㅋㅋㅋ 각자 컨셉도 너무 잘잡았고 티키타키도 너무 좋앜ㅋㅋㅋㅋㅋㅋㅋㅋ 웃기면서 따뜻함','ㅋㅋㅋㅋ','허허허'],
        'relation_thumbnails':['https://i.ytimg.com/vi/jRIHE1guY-Q/hqdefault.jpg?sqp=-oaymwEcCOADEI4CSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDXiFb36T7_J0Hszc4FQl90wdNVoA', 'https://i.ytimg.com/vi/AJzDFHQ7j0w/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLCsFdW7pDgYQ9nBxk8t0pppBgfTQA','https://i.ytimg.com/vi/REPZc2nzlyw/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBDN5oqcbiUuL3RmeUdq-AYizh7tw','https://i.ytimg.com/vi/rALBzv9p_Sc/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAJAwpe5lttpBXvrJUr8xExPp1hug','https://i.ytimg.com/vi/xqTwKxId6D8/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDslAZJgrGOhOcpy-TK4NWiVuiywA'],
        'relation_title': ['관종은 먹금 해야 하는 이유','헐레벌떡 어리둥절 빙글빙글 돌아가는 이번주 VLOG (거의 생방각) | 마트장보기, 야외에서 곱창먹기, 한강 피크닉, 성수동에서 압구정까지! 그리고 멋찐 선글라스를 샀다','박정현(Lena Park)의 킬링보이스를 라이브로!-I 꿈에, 이젠 그랬으면 좋겠네, 달아요, 미아, 하늘을 날다, 하비샴의 왈츠, 나의 하루, 편지할게요 | 딩고뮤직','4444','55555'],
        'relation_id': ['jRIHE1guY-Q','5ePKBm4spBg','XK4030cO0ko','rALBzv9p_Sc','xqTwKxId6D8'],
        'time': df,
    }
    print(df)


    return render(request, 'tubeana/board.html', context)