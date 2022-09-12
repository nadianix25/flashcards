window.onload = load;

function load(){
  var content = document.getElementById('content')
  const btnShowContent = document.getElementById('btnShowContent')
  var btnNext = document.getElementById('btnNext')
  var btnPrev = document.getElementById('btnPrev')
  var cards = document.getElementsByClassName("cards");

  btnNext.addEventListener("click", function(){
    plusDivs(1)
  })
  btnPrev.addEventListener("click", function(){
    plusDivs(-1)
  })


  for (i = 0; i < cards.length; i++) {
    cards[i].addEventListener("dblclick", function(){

    })
  }

  var slideIndex = 1;
  showCard(slideIndex);


  function showCard(n) {
    var i;

    if (n > cards.length) {slideIndex = 1}
    if (n < 1) {slideIndex = cards.length}
    for (i = 0; i < cards.length; i++) {
      cards[i].style.display = "none";

    }
    cards[slideIndex-1].style.display = "block";

  }

  function plusDivs(n) {
    showCard(slideIndex += n);


  }

  function currentDiv(n) {
    showCard(slideIndex = n);

  }

}
