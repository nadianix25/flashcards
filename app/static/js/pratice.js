window.onload = load;

function load(){
  var all_cards;
  var group = document.getElementById("group");
  var card_container = document.getElementById('cards_container')
  var content = document.getElementById('content')
  const btnShowContent = document.getElementById('btnShowContent')
  var btnNext = document.getElementById('btnNext')
  var btnPrev = document.getElementById('btnPrev')
  get_cards(group.innerHTML)

  btnNext.addEventListener("click", function(){
    plusDivs(1)
  })
  btnPrev.addEventListener("click", function(){
    plusDivs(-1)
  })



  function get_cards(filter){

    var response =  $.ajax({
        type: "GET",
        url: "/card/group/"+ filter,
        contentType: "application/json",
        dataType: 'json',
        success: function (data) {
          if(data.success==true){
             console.log(data.data)
             show_cards(data.data)
          }
        }
      });
    }

    function show_cards(list_of_cards){
      //create de DOM objects
      //or can i just make it availabel for jinja2
      all_cards = list_of_cards
      index = 0;
      for (var cards of list_of_cards) {

        var div_card = document.createElement("div");
        var header = document.createElement("header");
        var h1 = document.createElement("h1");
        var p = document.createElement("p");
        var pContent = document.createElement("p");
        var btnHint = document.createElement("button")
        var btnContent = document.createElement("button")
        var footer = document.createElement("footer")
        var div = document.createElement("div")

        div.classList.add("w3-container")

        footer.classList.add("w3-container")
        footer.classList.add("footer")
        div_card.classList.add("w3-card-4");
        div_card.classList.add("w3-white");
        div_card.classList.add("fade-in");
        div_card.classList.add("w3-third");
        div_card.classList.add("cards");
        //div_card.style.width = "50%";
        div_card.style.margin = "1%";
        header.classList.add("w3-container");
        h1.innerHTML=cards.title;
        btnHint.setAttribute("index_card", index);
        btnHint.innerHTML="hint"
        btnHint.classList.add("w3-right")
        btnHint.classList.add("w3-button")
        btnHint.classList.add("w3-blue")

        btnContent.setAttribute("index_card", index);
        btnContent.innerHTML="reveal"
        btnContent.classList.add("w3-right")
        btnContent.classList.add("w3-button")
        btnContent.classList.add("w3-green")

        pContent.id = "c"+ index;
        pContent.innerHTML = cards.content
        p.id=index
        p.innerHTML= cards.hint;
        p.classList.add("fade-in")
        h1.classList.add("w3-center")
        h1.classList.add("w3-margin-top")

        //p.innerHTML=cards.content;
        //Make room to the  id set up, because de object contains it
        // on the group cards create the context menu
        div.appendChild(pContent)
        footer.appendChild(btnContent)
        header.appendChild(btnHint)
        header.appendChild(p)
        div_card.appendChild(header)
        div_card.appendChild(h1)
        div_card.appendChild(div)
        div_card.appendChild(footer)
        card_container.appendChild(div_card)

        p.style.display="none"
        pContent.style.display="none"

        showCard(1)
        btnHint.addEventListener('click', function(event){
            index= event.target.getAttribute("index_card");
            //card = get_card(id)
            //p.innerHTML= "all_cards[index].hint"
            document.getElementById(index).style.display="block"

        })

        btnContent.addEventListener('click', function(event){
            index= event.target.getAttribute("index_card");
            //card = get_card(id)
            //p.innerHTML= "all_cards[index].hint"
            document.getElementById(("c"+index)).style.display="block"

        })
        index++

      }

    }

    var cards = document.getElementsByClassName("cards");

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

      function hint_of_card(id){
        var card;
        var response =  $.ajax({
          type: "GET",
          url: "/card/"+id,
          contentType: "application/json",
          dataType: 'json',
          success: function (data) {
            if(data.success==true){
              card = data.data
            }
          }
        });
      }

}
