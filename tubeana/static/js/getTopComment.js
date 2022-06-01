var commentChar = document.getElementsByName("commentChar");
var topCmt1 = document.getElementById("topCmt1");
var topCmt2 = document.getElementById("topCmt2");
var topCmt3 = document.getElementById("topCmt3");
var topCmt4 = document.getElementById("topCmt4");
var topCmt5 = document.getElementById("topCmt5");

for (i = 0; i < commentChar.length; i++) {
  commentChar[i].addEventListener("click", function () {
    console.log("functionON");
    switch (this.id) {
      case "positive":
        topCmt1.innerHTML = "영상 최고";
        topCmt2.innerHTML = "영상미가 좋네요!";
        topCmt3.innerHTML = "영상이 재밌어요";
        topCmt4.innerHTML = "ㅋㅋㅋㅋㅋ좋아요";
        topCmt5.innerHTML = "배꼽잡고 웃었어요 하하하";
        console.log("긍정선택");
        break;

      case "negative":
        topCmt1.innerHTML = "영상 별로";
        topCmt2.innerHTML = "이런 것도 영상이라고 만든 건가;";
        topCmt3.innerHTML = "유튜버 때려치세요";
        topCmt4.innerHTML = "개노잼임";
        topCmt5.innerHTML = "영상 본 시간이 아깝다";
        console.log("부정선택");
    }
  });
}

$(document).ready(function () {
  if ($("input[name='commentChar']:checked").val() == "positive") {
    topCmt1.innerHTML = "영상 최고";
    topCmt2.innerHTML = "영상미가 좋네요!";
    topCmt3.innerHTML = "영상이 재밌어요";
    topCmt4.innerHTML = "ㅋㅋㅋㅋㅋ좋아요";
    topCmt5.innerHTML = "배꼽잡고 웃었어요 하하하";
    console.log("긍정선택");
  }
});
