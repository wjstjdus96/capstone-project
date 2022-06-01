var word_list = [
  { text: "정크랫", weight: 10, url: "http://www.htmldrive.net/" },
  {
    text: "맥크리",
    weight: 9,
    url: "http://www.htmldrive.net/",
    title: "My Title",
  },
  {
    text: "라인하르트",
    weight: 8,
    url: "javascript:alert('JavaScript in URL is OK!');",
  },
  { text: "로드호그", weight: 7 },
  { text: "자리야", weight: 6.2 },
  { text: "트레이서", weight: 5 },
  { text: "한조", weight: 5 },
  { text: "솔져", weight: 4 },
  { text: "시메트라", weight: 4 },
  { text: "윈스턴", weight: 3 },
];
$(document).ready(function () {
  $("#my_favorite_latin_words").jQCloud(word_list);
});
