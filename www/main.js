$(document).ready(function () {
    
    $('.text').textillate({
        loop:true,
        sync:true,
        in:{
            effect:"bounceIn",
        },
        out:{
            effect:'bounceOut',
        },
    });

    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        autostart: true
      });

      //GLitch Message

      $('.siri-message').textillate({
        loop:true,
        sync:true,
        in:{
            effect:"fadeInUp",
            sync:true,
        },
        out:{
            effect:'fadeInUp',
            sync:true,
        },
    });


    //mic button click event
    $("#MicBtn").click(function () { 
        $("#oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.takecommand()
    });
});