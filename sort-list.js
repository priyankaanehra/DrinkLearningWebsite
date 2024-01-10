let correct_steps=[]
let score=0

$.each(data.steps, function(i, step){
    correct_steps.push(step)
})

let max_score=correct_steps.length

window.addEventListener("DOMContentLoaded", () => {
  slist(document.getElementById("sortlist"));
  $("#submit").on("click", function(){
      document.getElementById("clear").setAttribute("hidden","")
      $("#score").empty()
      compare(document.getElementById("sortlist"));
      //score_btn=document.getElementById("clear")
      //score_btn.setAttribute("href", "/quizscore/"+data.drink_id)
      //score_btn.innerHTML = "Next!"
      //$("#score").setAttribute("innerText","Next!")
      sub_btn = document.getElementById("submit")
      sub_btn.innerHTML = "Next Question"
      sub_btn.setAttribute("onclick", "goto_next()")
      //elm = document.getElementById("next")
      //elm.innerHTML = "<br><div class='col-md-6 text-right'><a class='btn btn-primary' href='/quizscore/"+data.drink_id+"' role='button'>Next!</a></div>"
      //$("#next").append("<br><div class='col-md-6 text-right'><a class='btn btn-primary' href='/quizscore/"+data.drink_id+"' role='button'>Next!</a></div>")
  })
  $("#clear").on("click", function(){
    $("#sortlist").empty();
    $("#score").empty()
    slist(document.getElementById("sortlist"));
  })
  
});


function goto_next(){
    window.location = ("/quizscore/"+data.drink_id)
}

function slist (target) {
  
  new_steps=correct_steps.sort(() => Math.random() - 0.5)
  if (new_steps==correct_steps){
  }
  else{
    new_steps=correct_steps.sort(() => Math.random() - 0.5)
  }
  console.log(new_steps)
  // (A) SET CSS + GET ALL LIST ITEMS
  target.classList.add("slist");
  //let items = new_steps, current=null
  $.each(new_steps, function(i, step){
    $("#sortlist").append("<li>"+new_steps[i]+"</li>")
  })
  
  let items = target.getElementsByTagName("li"), current = null;
  // (B) MAKE ITEMS DRAGGABLE + SORTABLE
  for (let i of items) {
    // (B1) ATTACH DRAGGABLE
    i.draggable = true;

    // (B2) DRAG START - YELLOW HIGHLIGHT DROPZONES
    i.ondragstart = (ev) => {
      current = i;
      for (let it of items) {
        if (it != current) { it.classList.add("hint"); }
      }
    };

    // (B3) DRAG ENTER - RED HIGHLIGHT DROPZONE
    i.ondragenter = (ev) => {
      if (i != current) { i.classList.add("active"); }
    };

    // (B4) DRAG LEAVE - REMOVE RED HIGHLIGHT
    i.ondragleave = () => {
      i.classList.remove("active");
    };

    // (B5) DRAG END - REMOVE ALL HIGHLIGHTS
    i.ondragend = () => { for (let it of items) {
      it.classList.remove("hint");
      it.classList.remove("active");
    }};

    // (B6) DRAG OVER - PREVENT THE DEFAULT "DROP", SO WE CAN DO OUR OWN
    i.ondragover = (evt) => { evt.preventDefault(); };

    // (B7) ON DROP - DO SOMETHING
    i.ondrop = (evt) => {
      evt.preventDefault();
      if (i != current) {
        let currentpos = 0, droppedpos = 0;
        for (let it=0; it<items.length; it++) {
          if (current == items[it]) { currentpos = it; }
          if (i == items[it]) { droppedpos = it; }
        }
        if (currentpos < droppedpos) {
          i.parentNode.insertBefore(current, i.nextSibling);
        } else {
          i.parentNode.insertBefore(current, i);
        }
      }
    };
  }
}

function compare(target){
  let items = target.getElementsByTagName("li")
  let tf_list=[]
  correct_steps=[]
  $.each(data.steps, function(i, step){
    correct_steps.push(step)
  })

  $.each(items, function(i, step){
    if (items[i].innerHTML===correct_steps[i]){
      tf_list[i]=true
    }
    else{
      tf_list[i]=false
    }
  })
  score=0
  $.each(tf_list, function(i, tf){
    if (tf){
      items[i].classList.add("correct")
      score=score+1
    }
    else{
      items[i].classList.add("wrong")
    }
  })
  console.log(score)
  //console.log(correct_steps[1])
  //console.log(items[1].innerHTML)
  //$("#score").append("Score:"+score+"/"+max_score)
  score_header = document.createElement("H4")
  let score_text = document.createTextNode("Score: "+score+"/"+max_score)
  score_header.appendChild(score_text)
  $("#score").append(score_header)
  $.ajax({
    type: "POST",
    url: "/record_q3",
    dataType : "json",
    contentType: "application/json; charset=utf-8",
    data : JSON.stringify([score,max_score]),
    success: function(newData){
        console.log(newData)
    }
  });

}

