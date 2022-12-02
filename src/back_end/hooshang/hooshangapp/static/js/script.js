// SETTING GLOBAL VARIABLES
// ---------------------------------
var face_url_id = '';
var sound_url_val = '';
var host = 'localhost';
var port = '8000';
var android_port = 8080;

// - - - Django Server - - - 
var django_base_url = 'http://' + host + ':' + port ;
var request_current_exp =  '/reqemo';  //URL has been set in 'hooshangapp/urls.py'
var publish_new_exp =  '/reqpub'; //URL has been set in 'hooshangapp/urls.py'
var android_server_url = 'http://' + host + ':' + android_port + '/android_server';

// - - - ROS - - -
// Workspace
var rosbridge_port = '9090';
var robot_ws = 'ws://'+host+':'+ rosbridge_port;	// Setting the websocket url for the ROS environment
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

// ------ Other functions ------
var auto_imit_val = false;

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
      var sound_url = response.sound_url;
      // Playing the recognized emotion's sound and video file
      document.getElementById("vidsrc").innerHTML = '<source src="'+ response.face_url+'" type="video/mp4">'; 
      document.getElementById("vidsrc").play()
      if (sound_url != 'No assigned sound found') {
        document.getElementById("vidsoundsrc").innerHTML = '<source src="'+ sound_url+'" type="audio/mp3">';
        document.getElementById("vidsoundsrc").play();
        } else {
          document.getElementById("vidsoundsrc").pause();
          document.getElementById("vidsoundsrc").currentTime = 0;
          document.getElementById("vidsoundsrc").innerHTML = '<source src="" type="audio/mp3">';};
 
      console.log(response);
    }
  })
  document.getElementById("msg").innerHTML = msgd;
});




var face_url_id = '';
// Taking in the user's commanded face expression 
// and passing on the url of the video file and its assigned sound's url to update_exp function.
// -----------------
function exp_face(element) {
  var face_url_id = element.id;
  var face_name_val = element.value;
  
  document.getElementById("msg").innerHTML = face_name_val;

  if (element.id == 'auto') {
    auto_imit_val = true;
  }
  
  
  $.ajax({
    type: "GET",
    url: request_current_exp, //Retrieving the requested emotion's sound file from the serever's database
    data: {
      face: face_name_val
    },
    success: function(response) {
      var sound_url = response.sound_url;
      document.getElementById("vidsrc").innerHTML = '<source src="'+ response.face_url+'" type="video/mp4">';
      if (sound_url == 'No assigned sound found' | face_url_id == 'auto') {
        document.getElementById("vidsoundsrc").pause();
        document.getElementById("vidsoundsrc").currentTime = 0;
        document.getElementById("vidsoundsrc").innerHTML = '<source src="" type="audio/mp3">';
      }
      else {
        document.getElementById("vidsoundsrc").innerHTML = '<source src="'+ sound_url+'" type="audio/mp3">';
        document.getElementById("vidsoundsrc").play();
      };
      var ids =   [face_url_id, sound_url];
      update_exp(ids);  // Returning the id of the button clicked 
                        // and it's relative sound recived as a response from the server
                        //  to be used in the update_exp function.
    }
  });
   // returning the url of the face to prevent changing the video file when sound updates


}

var csrftoken = $.cookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
var csrf = document.querySelector('meta[name="csrf-token"]').content;
function parr_b(element) {
  document.getElementById("pb_msg").innerHTML = element.value;
  dta=JSON.stringify({
    // Updating sound and video urls based on returned data from exp_face and exp_sound functions
    id: element.id,
    tag: element.id,
    '_token': csrf
  })
  $.ajax({
    type: "POST",
    contentType : 'application/json',
    url: 'parrot/',
    data: dta,
    success: function(response) {
      // Playing the new requested video and sound file
      console.log(response);
    },
    error: function(response) {
    console.log(response);// logging the response in browser's console
}}) 
}
function parr_r(element) {
  document.getElementById("pr_msg").innerHTML = element.value;
}

// Taking in the user's commanded sound and passing on the url of the sound file to update_exp function.
// -----------------
function exp_sound(element) {
  playAudio(element)
  document.getElementById("vidsoundsrc").pause()
  document.getElementById("vidsoundsrc").currentTime = 0;
  var sound_url_val = element.value;
  document.getElementById("msg_sound").innerHTML = sound_url_val;
  document.getElementById("vidsoundsrc").innerHTML = '<source src="'+ sound_url_val+'" type="audio/mp3">';
  document.getElementById("vidsoundsrc").play();
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
    url: android_server_url}); // Sending the request to the server to ask for changes in the robot's facial expression
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
      
      // Playing the new requested video and sound file
      console.log(response);
    }
  }) // logging the response in browser's console

  var exp_msg = new ROSLIB.Message({
    emotion : ids[0],
    auto_imit: auto_imit_val,
    action: 'face expression'
   });
   exp_Topic.publish(exp_msg); // Publishing the new emotion to the robot
   auto_imit_val = false; // Resetting the auto_imit_val to false to prevent auto-imitating the emotion
  }
  ids = []; // Resetting the ids array to prevent updating the video file when sound updates
  
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
  $(".play_btn")[0].currentTime = 0;
  
  if ($(input).hasClass("active") ) {
    $(input).removeClass("active");
    
  } 
  else {
    $(".play_btn").removeClass("active");
    $(input).addClass("active"); 
       

    }
  }



  function allowDrop(ev) {
    ev.preventDefault();
  }
  
  var state_var = '';
  function drag(ev, state) {
    state_var = state; 
  }
  
  function drop(ev) {
    ev.preventDefault();
    var drop_id = ev.target.id;
  //   if ($(this).find("input id=*clone")){
  //     $(document.getElementById(state_var)).appendTo(".dest_list").replaceWith(function() { 
  //     return "<li draggable='true' ondragstart='drag(event,this.id)'>" + this.innerHTML + "</li>"; 
  // });
  //   }
  //   else {

    $(document.getElementById(state_var)).clone().appendTo(".dest_list"+drop_id).replaceWith(function() { 
      $(this).find("p").addClass("sclone_p");
      $(this).css('display', 'inline-grid');
      $(this).find("input").removeClass("u-radius-50").css('font-size',' 0rem').css( 'min-width', '0.5rem');
      $(this).find("input").attr("id", state_var + "_clone");
      var del_btn = document.createElement("i");
      del_btn.setAttribute("class","bi bi-x-lg del_btn");
      del_btn.setAttribute("onclick","clear_item(this)");
      $(this).append(del_btn);
      $('#'+state_var + "_clone\*").css('border-radius','0%').css('width','10%').css('margin','-20px').css("height","inherit");
      $(".play_btn").css('margin','0');
      return "<li draggable='true' ondragstart='drag(event,this.id)'>" + this.innerHTML + "</li>"; 
  });

  }

  function auto_run(){
    // click all buttons that end with "clone" in order with a delay of 1 second
      $(".dest_list li input[id$='clone']").each(function(i) {
        $(this).removeClass("active");
        $(this).delay(5000 * i).queue(function() {
          $(this).addClass("active");
          exp_face(this);
          });

      });
    }

function clean(){
  $(".dest_list").empty();
}
function clear_item(item){
  $(item).parent().remove();
} 
  
  

  