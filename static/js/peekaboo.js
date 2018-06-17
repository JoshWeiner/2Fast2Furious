function getBotResponse() {
  var rawText = $("#textInput").val();
  var userHtml = '<p class="userText"><span>' + rawText + '</span></p>';
  $("#textInput").val("");
  //Displays user input in chatbox
  $("#chatbox").append(userHtml);

  var reply = $.post("/get_js", {
    rawText: rawText}, function(response)
    {
      var botHtml = '<p class="botText"><span>' + response + '</span></p>';
      $("#chatbox").append(botHtml)
    });


  /*
  document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'});
  $.get("/get", { msg: rawText }).done(function(data) {
    var botHtml = '<p class="botText"><span>' + data + '</span></p>';
    $("#chatbox").append({{botText}});
    document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'});
  });
  */
}

$("#textInput").keypress(function(e) {
    if(e.which == 13) {
        getBotResponse();
    }
});

$("#buttonInput").click(function() {
  getBotResponse();
})
