// SETTING GLOBAL VARIABLES
// ---------------------------------
var face_url_id = '';
var sound_url_val = '';
var host = 'localhost'
var port = '5353';

// - - - Django Server - - - 
var django_base_url = 'http://' + host + ':' + port ;
var request_current_exp = django_base_url + '/reqemo';  //URL has been set in 'hooshangapp/urls.py'
var publish_new_exp = django_base_url + '/reqpub'; //URL has been set in 'hooshangapp/urls.py'

// - - - ROS - - -
// Workspace
var rosbridge_port = '9090';
var robot_ws = 'ws://'+host+':'+rosbridge_port;	// Setting the websocket url for the ROS environment
// Topics
var publish_exp_topic = '/web_exp_publisher';
var publish_motion_topic = '/web_motion_publisher';
var camera_img_topic = '/camera/rgb/image_raw';
var listen_exp_topic = '/py_exp_publisher';
var listen_motion_topic = '/cmd_vel_listener';
// Messages
var exp_msg_type = 'face_pkg/Exp';
var motion_msg_type = 'geometry_msgs/Twist';
var camera_img_msg_type = 'sensor_msgs/Image';

// ---------------------------------------------- END OF VARIABLE DECLARATION -----------------------------------------------
// //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//Changing tabs
// -----------------
function viewdiv(div) {
  $('.change').children().hide();
  $(document.getElementById(div)).show().children().show();
}



// Connecting to ROS via 'rosbridge_websocket_server' Launch Node running on the master "URI/IP/URL :Port 9090(default)"
// ----------------- 
var ros = new ROSLIB.Ros({
  url : robot_ws
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


window.addEventListener('load', (event) => {
  console.log('page is fully loaded');
  var cam_reciever = new ROSLIB.Topic({
    ros : ros,
    name : camera_img_topic,
    messageType : camera_img_msg_type
  });
  
  cam_reciever.subscribe(function(msg) {
    console.log('Received message on ' + cam_reciever.name);
    
    var canvas = document.getElementById('rgb-canvas');
    ctx = canvas.getContext('2d');
    var image = new Image();
    image.src = `data:image/png;base64,${msg.data}`;
    ctx.drawImage(image, 0, 0);
}); 
});



// /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// <---------------------------------------------- EMOTION HANDLING SECTION---------------------------------------->	
// /////////////////////////////////////////////////////////////////////////////////////////////////////////////////


// Creating and Publishing the first emotion control message on the pre-defined(initiated through 'main.py') Topic /exp
// as the interface starts interacting with the robot on user's demand.
// -----------------
var exp_msg = new ROSLIB.Message({
  action: 'face expression',
  emotion : 'Neutral',
  auto_imit: false
});

// -----------------
// Creating new Topic for expressions data
// -----------------
var exp_Topic = new ROSLIB.Topic({
  ros : ros,
  name : publish_exp_topic,
  messageType : exp_msg_type
});



// Handling the turned on facial imitiator button through the server.
// (Same as other buttons but on a different topic to be recognized by the robot/user.)
// -----------------
var autoexp_Topic = new ROSLIB.Topic({
  ros : ros,
  name : listen_exp_topic,
  messageType : exp_msg_type
});

autoexp_Topic.subscribe(function(message) {
  console.log('Received message on ' + autoexp_Topic.name + ': ' + message.emotion);
  
  var msgd = message.emotion;
  $.ajax({
    type: "GET",
    url: request_current_exp,
    data: {
      face: msgd
    },
    success: function(response) {
      // Playing the recognized emotion's sound and video file
      document.getElementById("vidsrc").innerHTML = '<source src="'+ response.face_url+'" type="video/mp4">';
      document.getElementById("vidsoundsrc").innerHTML = '<source src="'+ response.sound_url+'" type="audio/mp3">';
      
      document.getElementById("vidsrc").load()
      document.getElementById("vidsrc").play()
      document.getElementById("vidsoundsrc").play() 
    }
  })
  document.getElementById("msg").innerHTML = msgd;
  console.log(response);
});




var face_url_id = '';
// Taking in the user's commanded face expression 
// and passing on the url of the video file and its assigned sound's url to update_exp function.
// -----------------
function exp_face(element) {
  var face_url_id = element.id;
  var face_name_val = element.value;
  document.getElementById("msg").innerHTML = face_name_val;
  
  
  $.ajax({
    type: "GET",
    url: request_current_exp, //Retrieving the requested emotion's sound file from the serever's database
    data: {
      face: face_name_val
    },
    success: function(response) {
      var sound_url = response.sound_url;
      document.getElementById("vidsrc").innerHTML = '<source src="'+ response.face_url+'" type="video/mp4">';
      document.getElementById("vidsoundsrc").innerHTML = '<source src="'+ sound_url+'" type="audio/mp3">';
      var ids =   [face_url_id, sound_url];
      update_exp(ids);  // Returning the id of the button clicked 
                        // and it's relative sound recived as a response from the server
                        //  to be used in the update_exp function.
    }
  });
   // returning the url of the face to prevent changing the video file when sound updates


}




// Taking in the user's commanded sound and passing on the url of the sound file to update_exp function.
// -----------------
function exp_sound(element) {
  var sound_url_val = element.value;
  document.getElementById("msg_sound").innerHTML = sound_url_val;
  document.getElementById("vidsoundsrc").innerHTML = '<source src="'+ sound_url_val+'" type="audio/mp3">';
  var ids =   [face_url_id, sound_url_val];
  return update_exp(ids); // returning the id of the button clicked to be used in the 'exp' function.

}




// <------------- UPDATE_EXP FUNCTION ------------->

//Handling the facial expression buttons events through both the Django server and the ROS environment
// (Updating sounds and facial expressions after clicking on a button)
// -----------------
function update_exp(ids) {
  
  // Sending a GET request to the server to set a new emotion
  // -----------------
  $.ajax({
    type: "GET",
    url: publish_new_exp,
    data: {
      // Updating sound and video urls based on returned data from exp_face and exp_sound functions
      face: ids[0],
      sound: ids[1]
    },
    success: function(response) {
      document.getElementById("vidsrc").load();

      document.getElementById("vidsrc").play();
      
      document.getElementById("vidsoundsrc").play();
      // Playing the new requested video and sound file
      console.log(response);
    }
  }) // logging the response in browser's console

}
// <--- END OF UPDATE_EXP FUNCTION --->


// ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
// <----------------------------------------- END OF EMOTION HANDLING ----------------------------------------->
// ///////////////////////////////////////////////////////////////////////////////////////////////////////////////


// ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
// <----------------------------------------------- MOTION HANDLING --------------------------------------------->
// ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

// -----------------
// Listening to the /cmd_vel topic to get the robot's current velocity commanded through keyboard teleoperation.
// -----------------

var motion_Topic = new ROSLIB.Topic({
  ros : ros,
  name : listen_motion_topic,
  messageType : motion_msg_type
});


motion_Topic.subscribe(function(message) {
  console.log('Received message on ' + exp_Topic.name + ': ' + message.linear.x);
  linear_x = message.linear.x;
  linear_y = message.linear.y;
  angular_z = message.angular.z
  
});

// -----------------
// Publishing manual movement commands from the user interface(not from the keyboard) on /cmd_vel_web topic
// -----------------
var motion_Topic = new ROSLIB.Topic({
  ros : ros,
  name : publish_motion_topic,
  messageType : motion_msg_type
});

function motion(element) {
  var twist = new ROSLIB.Message({
   element
  });
  cmdVel.publish(twist);
}


// -----------------
// Audio Player for the web interface
// -----------------
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



  function allowDrop(ev) {
    ev.preventDefault();
  }
  
  function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
  }
  
  function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
  }

  