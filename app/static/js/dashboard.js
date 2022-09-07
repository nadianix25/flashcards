window.onload = load;

function load(){


  const cards = document.querySelectorAll('.group-card');
  var card_container = document.getElementById('card_container');

  cards.forEach(card => {
  card.addEventListener('click', function handleClick(event) {
    remove_selected()
    console.log('box clicked', event);
    card.classList.add("group-card-selected")
    get_cards()

  });
});

  function remove_selected(){
    cards.forEach(card => {
      card.classList.remove("group-card-selected")
    });
  };

  function get_cards(filter){
    var data = {'filter':filter};

    var response =  $.ajax({
        type: "GET",
        url: "/card",
        data: JSON.stringify(data),
        contentType: "application/json",
        dataType: 'json',
        success: function (data) {
          if(data.success==true){
             console.log("it works gentji")
             show_cards(["as","as","ksa"])
          }
        }
      });
    }

    function show_cards(list_of_cards){
      //create de DOM objects
      //or can i just make it availabel for jinja2
      cleanCards()

      for (let i = 0; i < 5; i++) {
        var div_card = document.createElement("div");
        var header = document.createElement("header");
        var h4 = document.createElement("h4");
        var p = document.createElement("p");

        div_card.classList.add("w3-card-4");
        div_card.classList.add("w3-white");
        div_card.style.width = "50%";
        div_card.style.marginBottom = "1%";
        header.classList.add("w3-container");
        h4.innerHTML="no"
        p.innerHTML="you need to let it go"

        header.appendChild(h4)
        header.appendChild(p)
        div_card.appendChild(header)
        card_container.appendChild(div_card)
      }

    }

    function cleanCards(){
      card_container.innerHTML ="";
    }

}
