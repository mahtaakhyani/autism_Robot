// Clock!
function clock() { 
  var t = moment(),
      a = t.minutes() * 6,
      o = t.hours() % 12 / 12 * 360 + (a / 12);
  $(".hour").css("transform", "rotate(" + o + "deg)");
  $(".minute").css("transform", "rotate(" + a + "deg)");
}
function refreshClock() {
  clock(), setTimeout(refreshClock, 1000)
}
refreshClock();

// Actual Clock Numbers
function update() {
  $('#clock').html(moment().format('h:mm A'));
}

setInterval(update, 1000);


//Spinning Loader
$( "button" ).click(function() {
  $( "#notify" ).show('this'),
  $( "#spinny" ).toggleClass( "is-active" ).delay(2000).hide('this'),
  setTimeout(function() {
    $( "#notify" ).append( '<p>Event Added <span class="glyphicon glyphicon-ok" aria-hidden="true"></span></p>' ).delay(1800).hide('this');
  }, 2000);
});


//Activate tabs
$('.anchor').click(function(){
  $('.active').removeClass('active');
  $(this).addClass('active');
});
//on load
$(window).on('load', function () {
  $('.change').children().hide();
  $("#control_panel").show().children().show();
  $('.maintab').addClass('active')
  $('.shyblush').hide();

  });
$(document).ready(function(){
var dialOne = JogDial(document.getElementById('jog_dial_example'),
    {wheelSize:'200px', knobSize:'70px', minDegree:0, maxDegree:360, degreeStartAt: 0})
    .on('mousemove', function(evt){
      $('#jog_dial_example_meter div').css('width', Math.round((evt.target.rotation/360)*100) + '%' )
    });
  });

//view dev
function viewdiv(div) {
  $('.change').children().hide();
  $(document.getElementById(div)).show().children().show();
}

//model
$(document).ready(function() {
  $(".side").hide();
  // $('#autoplay').click(function() {
  //   $('.level1-circle, .level2-circle').toggleClass('autoplay');
  //   if ($(this).prop('checked') == true)
  //     $('input[type=range]').prop('disabled', true);
  //   else
  //     $('input[type=range]').removeAttr('disabled');
  // });
  $('#arm2').on('change input', function() {
    var rotateBy = $(this).val();
    $('.level2-circle').css({
      '-webkit-transform': 'rotate(' + rotateBy + 'deg)',
      'transform': 'rotate(' + rotateBy + 'deg)'
    });
  });
});

function drag() {
  var rotateBy = $("#arm1").val();
  $('.level1-circle').css({
    '-webkit-transform': 'rotate(' + rotateBy + 'deg)',
    'transform': 'rotate(' + rotateBy + 'deg)'
  });
};
//avatar bot
function reload() {
  var $ed = $('#mainbot').children()
    , $style = $('#mainbot')
  ;
  $ed.val($style.html());
      $style.html($ed.val());

};
$(".front").on('click', function(){
  $(this).css({
    'top':'50% !important',
     'box-shadow': 'rgb(255 255 255 / 30%) 5px 5px 10px inset, rgb(0 0 0 / 15%) -5px -5px 10px inset, rgb(0 0 0 / 70%) 0px 2px 10px -5px, rgb(0 0 0 / 20%) 0px 4px 20px -10px, rgb(0 0 0 / 20%) -50px 0px 40px -20px, rgb(0 0 0 / 20%) 50px 50px 40px -20px',
     'transform-style': 'preserve-3d',
      'perspective': '1000px'
});
});
//houshangpic
function exp(element) {
  var id = element.id;
  $('#mouth').attr('class' , 'mouth-' + id );
  var lastClass = $(".housheye").attr('class').split(' ').pop();
  $(".housheye").removeClass(lastClass);
  $(".housheye").addClass( id+'eye');
  if (id == 'shy')
    $('.shyblush').show();
  else 
    $('.shyblush').hide();

  $.ajax({
    type: "GET",
    url: "http://127.0.0.1:8000/reqpub",
    data: {
      face: element.id
    }
  })
  .then(console.log);

};

//Speech

$('#speech').on('click', function(){
  $('#pulse-ring').addClass('pulse-ring');
  $('#speech , #stop').toggleClass('stop');
  const downloadLink = document.getElementById('download');
  if ($(this).hasClass('stop')===false){  
  var stopButton = document.getElementById('speech');
  }
  else {
    $('#pulse-ring').removeClass('pulse-ring');
    var stopButton = document.getElementById('stop');
    mediaRecorder.stop();
    navigator.mediaDevices.getUserMedia({ audio: false, video: false })};

  const player = document.getElementById('player');

            
            
  const handleSuccess = function(stream) {
    const options = {mimeType: 'audio/webm'};
    var recordedChunks = [];
    const mediaRecorder = new MediaRecorder(stream, options);
    
    mediaRecorder.addEventListener('dataavailable', function(e) {
      if (e.data.size > 0) recordedChunks.push(e.data);
    });
      
    downloadLink.href = URL.createObjectURL(new Blob(recordedChunks));
    const url = URL.createObjectURL(new Blob(recordedChunks));
    player.src = url;
    player.srcObject = stream;
      mediaRecorder.addEventListener('stop', function() {
        var recordedChunks = [];
        downloadLink.download = 'acetest.wav';
      });
 
      stopButton.addEventListener('click', function() {
        mediaRecorder.stop();
        // var recordedChunks = [];
        // if (window.URL)
        // else
        // player.src = stream;
      });
    mediaRecorder.start();
  };
  navigator.permissions.query({name:'microphone'}).then(function(result) {
    if (result.state == 'granted') {
    
    } else if (result.state == 'prompt') {
      navigator.mediaDevices.getUserMedia({ audio: true, video: false })
      .then(handleSuccess);
      
        } else if (result.state == 'denied') {
        
          }
          result.onchange = function() {
          
            };
          });
        
}); 

var listener = new ROSLIB.Topic({
  ros : ros,
  name : '/cmd_vel_wheel',
  messageType : 'geometry_msgs/Twist'
});

listener.subscribe(function(message) {
  console.log('Received message on ' + listener.name + ': ' + message.linear.x);
  linear_x = message.linear.x;
  linear_y = message.linear.y;
  angular_z = message.angular.z

});

//impresions
// function normal() {
//     var xmlHttp = new XMLHttpRequest();
//     xmlHttp.open( "GET", "normal", false ); // false for synchronous request
//     xmlHttp.send( null );
//     return xmlHttp.responseText;
// }
      // fetch("/normal")
      // .then(console.log)

    //     player.src = url;
    //     // const handleSuccesss = function(stream) {
      //     //   if (window.downloadLink.href) 
      //     //   player.srcObject = stream;
      
      //     //   else
      //     //   player.src = stream;
      //     // };
      //     // downloadLink.download = 'acetest.wav';
  // downloadLink.addEventListener('change', function change(e) {
  //   const file = e.target.files[0];
  //   // const url = downloadLink.href //URL.createObjectURL(file);
  //   //   // Do something with the audio file.
  //   player.src = url;
  // });
  

