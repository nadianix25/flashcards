window.onload = load;

function load(){

  var idgroup = document.getElementById("ipt_group_id");
  const cards = document.querySelectorAll('.group-card');
  var card_container = document.getElementById('card_container');
  const btnCreateCard = document.getElementById('iptCreateCard');

  btnCreateCard.addEventListener('click', post_card);

  cards.forEach(card => {
  card.addEventListener('click', function handleClick(event) {
    remove_selected()
    console.log('box clicked', event);
    card.classList.add("group-card-selected")
    get_cards()
    idgroup.value = get_selected_card().firstElementChild.innerHTML

  });
});

  function remove_selected(){
    cards.forEach(card => {
      card.classList.remove("group-card-selected")
    });
  };

  function get_selected_card(){
    return document.querySelectorAll('.group-card-selected')[0];
  }

  function get_cards(filter){
    var filter =get_selected_card().firstElementChild.innerHTML//.firstChild.text
    console.log(filter)


    var response =  $.ajax({
        type: "GET",
        url: "/card/"+ filter,
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
      cleanCards()

      for (var cards of list_of_cards) {
        var div_card = document.createElement("div");
        var header = document.createElement("header");
        var h4 = document.createElement("h4");
        var p = document.createElement("p");

        div_card.classList.add("w3-card-4");
        div_card.classList.add("w3-white");
        div_card.classList.add("fade-in");
        div_card.classList.add("w3-third");
        //div_card.style.width = "50%";
        div_card.style.margin = "1%";
        header.classList.add("w3-container");
        h4.innerHTML=cards.title;
        p.innerHTML=cards.content;

        header.appendChild(h4)
        header.appendChild(p)
        div_card.appendChild(header)
        card_container.appendChild(div_card)
      }

    }

    function cleanCards(){
      card_container.innerHTML ="";
    }


    function post_card(){
      var title = document.getElementById('iptTitle');
      var content = document.getElementById('iptContent');
      var hint = document.getElementById('iptHint');
      var data = {'title':title.value,
                  'content':content.value,
                  'hint':hint.value,
                  'group':idgroup.value}
      var response =  $.ajax({
        type: "POST",
        url: "/card",
        data: JSON.stringify(data),
        contentType: "application/json",
        dataType: 'json',
        success: function (data) {
          if(data.success==true){
                 console.log(data)
          }
        }
      });

      document.getElementById('card_form').style.display='none';
      refresh_cards()
    }

    function refresh_cards(){
      setTimeout(function(){
        var filter =get_selected_card().firstElementChild.innerHTML//.firstChild.text
        get_cards(filter)

      }, 500);
    }

}
