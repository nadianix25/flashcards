window.onload = load;

function load(){

  var idgroup = document.getElementById("ipt_group_id");
  const cards = document.querySelectorAll('.group-card');
  var card_container = document.getElementById('card_container');
  const btnCreateCard = document.getElementById('iptCreateCard');
  const btnEditCard = document.getElementById('iptEditCard');
  const btnDeleteCard = document.getElementById("iptDeleteCard");
  // btnPratice
  var btnPratice = document.getElementById('btnPratice');
  //displays
  var display_pratice_on = document.getElementById('display_group');
  var display_pratice_on_description = document.getElementById('display_group_description');

  btnCreateCard.addEventListener('click', post_card);
  btnEditCard.addEventListener('click', edit_card);
  btnDeleteCard.addEventListener('click', delete_card);
  btnPratice.addEventListener('click', pratice);

  cards.forEach(card => {
  card.addEventListener('click', function handleClick(event) {
    remove_selected()
    console.log('box clicked', event);
    card.classList.add("group-card-selected")
    get_cards()
    idgroup.value = get_selected_card().firstElementChild.innerHTML
    display_pratice_on.innerHTML="Start pratice on group " + get_selected_card().firstElementChild.innerHTML

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
        div_card.classList.add("card");
        div_card.setAttribute("id_card", cards.id);
        //div_card.style.width = "50%";
        div_card.style.margin = "1%";
        header.classList.add("w3-container");
        header.setAttribute("id_card", cards.id);
        h4.innerHTML=cards.title;
        h4.setAttribute("id_card", cards.id);
        p.innerHTML=cards.content;
        p.setAttribute("id_card", cards.id);
        //Make room to the  id set up, because de object contains it
        // on the group cards create the context menu

        header.appendChild(h4)
        header.appendChild(p)
        div_card.appendChild(header)
        card_container.appendChild(div_card)
        card_container.addEventListener('click', function (event){
          //// TODO: set the values for this pop up
          id= event.target.getAttribute("id_card");
          document.getElementById('card_edit_form').style.display="block";
          get_card(id)
        })
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

    function get_card(id){

      var response =  $.ajax({
        type: "GET",
        url: "/card/"+id,
        contentType: "application/json",
        dataType: 'json',
        success: function (data) {
          if(data.success==true){
            document.getElementById('iptIdCard').value = data.data.id;
            document.getElementById('iptTitleEdit').value = data.data.title;
            document.getElementById('iptContentEdit').value = data.data.content;
            document.getElementById('iptHintEdit').value = data.data.hint;
          }
        }
      });
    }

    function edit_card(){
      var id = document.getElementById('iptIdCard');
      var title = document.getElementById('iptTitleEdit');
      var content = document.getElementById('iptContentEdit');
      var hint = document.getElementById('iptHintEdit');
      var data = {'id':id.value,
                  'title':title.value,
                  'content':content.value,
                  'hint':hint.value}
      var response =  $.ajax({
        type: "PATCH",
        url: "/card/"+id.value,
        data: JSON.stringify(data),
        contentType: "application/json",
        dataType: 'json',
        success: function (data) {
          if(data.success==true){
                 console.log(data)
          }
        }
      });

      document.getElementById('card_edit_form').style.display='none';
      refresh_cards()
    }

    function delete_card(){
      var id = document.getElementById('iptIdCard');
      var data = {'id':id.value}
      var response =  $.ajax({
        type: "PATCH",
        url: "/card/"+id.value,
        data: JSON.stringify(data),
        contentType: "application/json",
        dataType: 'json',
        success: function (data) {
          if(data.success==true){
                 console.log(data)
          }
        }
      });

      document.getElementById('card_edit_form').style.display='none';
      refresh_cards()
    }


    function refresh_cards(){
      setTimeout(function(){
        var filter =get_selected_card().firstElementChild.innerHTML//.firstChild.text
        get_cards(filter)

      }, 500);
    }

    function pratice(){
      //// TODO: retrieve group information and redirect to the endpoint
      // Simulate a mouse click:
      var group =get_selected_card().firstElementChild.innerHTML//.firstChild.text
      window.location.href = "/pratice/"+group;
    }

}
