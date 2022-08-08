

var twist;
var cmdVel;
var publishImmidiately = true;
var robot_WS;
var joystick;
var teleop;
var ros;
var joystick;
var linear_x
var linear_y
var angular_z;
function moveAction(linear, angular) {
    if (linear !== 0 && angular !== 0) {
        twist.linear.x = linear;
        twist.angular.z = angular;
        console.log(twist.linear.x , twist.angular.z);
        $('#vlx').text(linear.toFixed(2));
        $('#vaz').text(angular.toFixed(2));
        if (linear > 0) {$("#dx").text('Front')};
        if (linear < 0) {$("#dx").text('Back')};
        if (angular > 0) {$("#dy").text('Left')};
        if (angular < 0) {$("#dy").text('Right');};
    } else {
        twist.linear.x = 0;
        twist.angular.z = 0;
        $("#dx").text('Stopped');
        $("#dy").text('Stopped');
        $('#vlx').text(linear);
        $('#vaz').text(angular);
    }
    cmdVel.publish(twist);
}
function initVelocityPublisher() {
    // Init message with zero values.
    twist = new ROSLIB.Message({
        linear: {
            x: 0,
            y: 0,
            z: 0
        },
        angular: {
            x: 0,
            y: 0,
            z: 0
        }
    })
    // Init topic object
    cmdVel = new ROSLIB.Topic({
        ros: ros,
        name: '/cmd_vel_wheel',
        messageType: 'geometry_msgs/Twist'
    });
    // Register publisher within ROS system
    cmdVel.advertise();
}
function initTeleopKeyboard() {
    // Use w, s, a, d keys to drive your robot

    // Check if keyboard controller was aready created
    if (teleop == null) {
        // Initialize the teleop.
        teleop = new KEYBOARDTELEOP.Teleop({
            ros: ros,
            topic: '/cmd_vel_wheel'
        });
    }

    // Add event listener for slider moves
    // robotSpeedRange = document.getElementById("robot-speed");
    // robotSpeedRange.oninput = function () {
    //     teleop.scale = robotSpeedRange.value / 100
    // }
}
function createJoystick() {
    // Check if joystick was aready created
    if (joystick == null) {
        joystickContainer = document.getElementById('joystick');
        // joystck configuration, if you want to adjust joystick, refer to:
        // https://yoannmoinet.github.io/nipplejs/
        var options = {
            zone: document.getElementById('joystickArea'),
            position: { left: 50 + '%', top: 50 + '%' },
            mode: 'static',
            size: 100,
            color: ' radial-gradient(whitesmoke, #2f2121)',
            restJoystick: true,
            restOpacity: '.8'
        };
        // box-shadow: 0 2px 5px rgb(0 0 0 / 30%), 3px 5px 10px rgb(0 0 0 / 15%);
        // background: radial-gradient(whitesmoke, #2f2121)

        joystick = nipplejs.create(options);
        // event listener for joystick move
        joystick.on('move', function (evt, nipple) {
            // nipplejs returns direction is screen coordiantes
            // we need to rotate it, that dragging towards screen top will move robot forward
            var direction = nipple.angle.degree - 90;
            if (direction > 180) {
                direction = -(450 - nipple.angle.degree);
            }
            // convert angles to radians and scale linear and angular speed
            // adjust if youwant robot to drvie faster or slower
            var lin = Math.cos(direction / 57.29) * nipple.distance * 0.005;
            var ang = Math.sin(direction / 57.29) * nipple.distance * 0.05;
            // nipplejs is triggering events when joystic moves each pixel
            // we need delay between consecutive messege publications to 
            // prevent system from being flooded by messages
            // events triggered earlier than 50ms after last publication will be dropped 
            if (publishImmidiately) {
                publishImmidiately = false;
                moveAction(lin, ang);
                setTimeout(function () {
                    publishImmidiately = true;
                }, 50);
            }
        });
        // event litener for joystick release, always send stop message
        joystick.on('end', function () {
            moveAction(0, 0);
        });
    }
}

window.onload = function () {
    createJoystick()};
//     // determine robot address automatically
    var robot_IP = '0.0.0.0';
//     // set robot address statically
     ros.on('connection', function() {
      console.log('Connected to websocket server.');
    });
  
    ros.on('error', function(error) {
      console.log('Error connecting to websocket server: ', error);
    });
  
    ros.on('close', function() {
      console.log('Connection to websocket server closed.');
    });

    initVelocityPublisher();

//     // get handle for video placeholder
    video = document.getElementById('video');
//     // Populate video source 
    video.src = "http://" + robot_IP + ":8080/stream?topic=/imager";

    video = document.getElementById('videop');
    video.src = "http://" + robot_IP + ":8080/stream?topic=/imager";
    
    // video.onload = function () {
    //     console.log('video streaming started successfuly')
//         // joystick and keyboard controls will be available only when video is correctly loaded
//         createJoystick();
        // initTeleopKeyboard();
//     };
// }

var param = new ROSLIB.Param({
    ros : ros,
    name : 'robot_description'
  });

  param.get(function(param) {
    var urdfModel = new ROSLIB.UrdfModel({
      string : param
    });
    console.log(urdfModel);
  });
