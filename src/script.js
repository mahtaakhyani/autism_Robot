

// Init handle for rosbridge_websocket - If not willing to be initiated at the robot startup.(Limited to when control interface is requested.)
// robot_WS = 'ws://localhost:9090';
//     ros = new ROSLIB.Ros({
//     url: robot_WS
//     });  

// Connecting to ROS via 'rosbridge_websocket_server' Launch Node running on the master "URI/IP/URL :Port 9090(default)"
// ----------------- 
var ros = new ROSLIB.Ros({
  url : 'ws://127.0.0.1:9090'
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
// ---------------
// Creating and Publishing the first emotion control message on the pre-defined(initiated through 'main.py') Topic /exp
// as the interface starts interacting with the robot on user's demand.

var exp_msg = new ROSLIB.Message({
  action: 'face expression',
  emotion : 'Neutral',
  auto_imit: false
});

// Creating new Topic for expressions data
var exp_Topic = new ROSLIB.Topic({
  ros : ros,
  name : '/exp',
  messageType : 'face_pkg/Exp'
});

 // Subscribing to the Topic
    // ----------------------
    
    exp_Topic.subscribe(function(message) {
      console.log('Received message on ' + exp_Topic.name + ': ' + message.emotion);
      var msgd = message.emotion;
      // exp_Topic.unsubscribe();
      document.getElementById("msg").innerHTML = msgd;
    });

exp_Topic.publish(exp_msg);
console.log('Published message on ' + exp_Topic.name + ': ' + exp_msg.emotion);



//view dev
function viewdiv(div) {
  $('.change').children().hide();
  $(document.getElementById(div)).show().children().show();
}



//houshangexp
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

  if (id == 'auto')
    var auto_bool = true
  else var auto_bool = false
  var exp_msg = new ROSLIB.Message({
      action: 'facial',
      emotion : id,
      auto_imit: auto_bool
    });
    exp_Topic.publish(exp_msg);
    console.log('Published message on ' + exp_Topic.name + ': auto:' + exp_msg.auto_imit+'-->'+ exp_msg.action +':'+  exp_msg.emotion);
  
};

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
