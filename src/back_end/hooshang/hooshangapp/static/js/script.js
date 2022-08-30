
//Changing tabs
// -----------------
function viewdiv(div) {
  $('.change').children().hide();
  $(document.getElementById(div)).show().children().show();
}

// Init handle for rosbridge_websocket - If not willing to be initiated at the robot startup.(Limited to when control interface is requested.)
// robot_WS = 'ws://localhost:9090';
//     ros = new ROSLIB.Ros({
//     url: robot_WS
//     });  

// Connecting to ROS via 'rosbridge_websocket_server' Launch Node running on the master "URI/IP/URL :Port 9090(default)"
// ----------------- 
var ros = new ROSLIB.Ros({
  url : 'ws://localhost:9090'
});

ros.on('connection', function() {
  console.log('Connected to websocket server.');
});

ros.on('error', function(error) {
  console.log('Error connecting to websocket server: ', error);
});

ros.on('close', function() {
  console.log('Connection to websocket server closed.');
});


// Creating and Publishing the first emotion control message on the pre-defined(initiated through 'main.py') Topic /exp
// as the interface starts interacting with the robot on user's demand.
// -----------------
var exp_msg = new ROSLIB.Message({
  action: 'face expression',
  emotion : 'Neutral',
  auto_imit: false
});

// Creating new Topic for expressions data
// -----------------
var exp_Topic = new ROSLIB.Topic({
  ros : ros,
  name : '/web_exp_publisher',
  messageType : 'face_pkg/Exp'
});

// Handling the turned on facial imitiator button through the server.
// (Same as other buttons but on a different topic to be recognized by the robot/user.)
// -----------------
var autoexp_Topic = new ROSLIB.Topic({
  ros : ros,
  name : 'exp_publisher',
  messageType : 'face_pkg/Exp'
});

autoexp_Topic.subscribe(function(message) {
  console.log('Received message on ' + autoexp_Topic.name + ': ' + message.emotion);
  var msgd = message.emotion;
  // exp_Topic.unsubscribe();
  document.getElementById("msg").innerHTML = msgd;
});


 // Subscribing to the Topic
    // + Logging all recieved messages in the browser's console for debugging purposes.
    // ----------------------
    exp_Topic.subscribe(function(message) {
      console.log('Received message on ' + exp_Topic.name + ': ' + message.emotion);
      var msgd = message.emotion;
      // exp_Topic.unsubscribe();
      document.getElementById("msg").innerHTML = msgd;
    });


//Handling the facial expression buttons events through both the Django server and the ROS environment
// -----------------
function exp(element) {
  var id = element.id;
  document.getElementById("msg").innerHTML = id;

  // Sending a GET request to the server to set a new emotion on demand
  // -----------------
  $.ajax({
    type: "GET",
    url: "http://192.168.43.250:5353/reqpub", //URL has been set in 'hooshangapp/urls.py'
    data: {
      face: element.id,
      sound: null
    }
  })
  .then(console.log); // logging the response in browser's console
// -----------------
  // Publishing the new emotion on the topic /exp for the robot to react(initiate motion) via ROS, if needed.
// -----------------
  if (id == 'auto')
    var auto_bool = true
  else var auto_bool = false //checking if the button is 'auto' or not.

  var exp_msg = new ROSLIB.Message({ 
    //*NOTE: This message is of the type 'face_pkg/Exp' which is manually defined 
    // and can be safely modified to meet new needs at any time.

      action: 'facial',
      emotion : id,
      auto_imit: auto_bool
    }); // creating a new message for the topic /exp based on the button clicked and the auto_bool value.
    
    exp_Topic.publish(exp_msg);
    console.log('Published message on ' + exp_Topic.name + ': auto:' + exp_msg.auto_imit+'-->'+ exp_msg.action +':'+  exp_msg.emotion);
    // publishing the new message on the topic /exp and logging it in the browser's console.
  
};
function exp_sound(element) {
  var val = element.value;
  document.getElementById("msg_sound").innerHTML = val;
  alert(val);

  // Sending a GET request to the server to set a new sound on demand
  // -----------------
  $.ajax({
    type: "GET",
    url: "http://192.168.43.250:5353/reqpub", //URL has been set in 'hooshangapp/urls.py'
    data: {
      sound: val,
      face: null
    }
  })
  .then(console.log); // logging the response in browser's console
}

// -----------------
// Publishing manual motion control messages on the related topics
// -----------------
// var exp_Topic = new ROSLIB.Topic({
//   ros : ros,
//   name : '/cmd_vel_wheel',
//   messageType : 'geometry_msgs/Twist'
// });

// exp_Topic.subscribe(function(message) {
//   console.log('Received message on ' + exp_Topic.name + ': ' + message.linear.x);
//   linear_x = message.linear.x;
//   linear_y = message.linear.y;
//   angular_z = message.angular.z

// });


// Audio Player for the web interface

function playAudio(input) { 
  var file = input.id;
  var x = document.getElementById(file);
  if (x.paused == false) {
    x.pause();
    $(".play_btn").removeClass("active");
    
  } 
  else {
    x.play();
    $(".play_btn").removeClass("active");
    $(input).addClass("active"); 
       

    }
  }