

// var twist;
// var cmdVel;
// var publishImmidiately = true;
// var robot_WS;
// var joystick;
// var teleop;
// var ros;
// var joystick;
// var linear_x
// var linear_y
// var angular_z;
// function moveAction(linear, angular) {
//     if (linear !== 0 && angular !== 0) {
//         twist.linear.x = linear;
//         twist.angular.z = angular;
//         console.log(twist.linear.x , twist.angular.z);
//         $('#vlx').text(linear.toFixed(2));
//         $('#vaz').text(angular.toFixed(2));
//         if (linear > 0) {$("#dx").text('Front')};
//         if (linear < 0) {$("#dx").text('Back')};
//         if (angular > 0) {$("#dy").text('Left')};
//         if (angular < 0) {$("#dy").text('Right');};
//     } else {
//         twist.linear.x = 0;
//         twist.angular.z = 0;
//         $("#dx").text('Stopped');
//         $("#dy").text('Stopped');
//         $('#vlx').text(linear);
//         $('#vaz').text(angular);
//     }
//     cmdVel.publish(twist);
// }
// function initVelocityPublisher() {
//     // Init message with zero values.
//     twist = new ROSLIB.Message({
//         linear: {
//             x: 0,
//             y: 0,
//             z: 0
//         },
//         angular: {
//             x: 0,
//             y: 0,
//             z: 0
//         }
//     })
//     // Init topic object
//     cmdVel = new ROSLIB.Topic({
//         ros: ros,
//         name: '/cmd_vel_wheel',
//         messageType: 'geometry_msgs/Twist'
//     });
//     // Register publisher within ROS system
//     cmdVel.advertise();
// }
// function initTeleopKeyboard() {
//     // Use w, s, a, d keys to drive your robot

//     // Check if keyboard controller was aready created
//     if (teleop == null) {
//         // Initialize the teleop.
//         teleop = new KEYBOARDTELEOP.Teleop({
//             ros: ros,
//             topic: '/cmd_vel_wheel'
//         });
//     }

//     // Add event listener for slider moves
//     // robotSpeedRange = document.getElementById("robot-speed");
//     // robotSpeedRange.oninput = function () {
//     //     teleop.scale = robotSpeedRange.value / 100
//     // }
// }
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

// window.onload = function () {
//     createJoystick()};
// //     // determine robot address automatically
//     var robot_IP = '0.0.0.0';
// //     // set robot address statically
//      ros.on('connection', function() {
//       console.log('Connected to websocket server.');
//     });
  
//     ros.on('error', function(error) {
//       console.log('Error connecting to websocket server: ', error);
//     });
  
//     ros.on('close', function() {
//       console.log('Connection to websocket server closed.');
//     });

//     initVelocityPublisher();

//     // get handle for video placeholder
//     video = document.getElementById('video');
// //     // Populate video source 
//     video.src = "http://" + robot_IP + ":8080/stream?topic=/imager";

//     video = document.getElementById('videop');
//     video.src = "http://" + robot_IP + ":8080/stream?topic=/imager";
    
    // video.onload = function () {
    //     console.log('video streaming started successfuly')
//         // joystick and keyboard controls will be available only when video is correctly loaded
//         createJoystick();
        // initTeleopKeyboard();
//     };
// }

// var param = new ROSLIB.Param({
//     ros : ros,
//     name : 'robot_description'
//   });

//   param.get(function(param) {
//     var urdfModel = new ROSLIB.UrdfModel({
//       string : param
//     });
//     console.log(urdfModel);
//   });

function load_joystick(){

	var joystick = document.getElementById("joystick"),
			    knob = document.getElementById("knob"),
			target_x = joystick.clientWidth/2-knob.clientWidth/2,
			target_y = joystick.clientHeight/2-knob.clientHeight/2;

	var panSpan  = document.getElementById("actValue"),
			tiltSpan = document.getElementById("powerValue"),
      dirSpan = document.getElementById("dirValue"),
      linspeedSpan = document.getElementById("linValue"),
      angspeedSpan = document.getElementById("angValue");

	knob.style.webkitTransform = "translate("+target_x+"px, "+target_y+"px)";

	// update the position attributes
	var target = document.getElementById("knob");
	updatePositionAttributes(target,target_x,target_y);

	// target elements with the "draggable" class
	interact('.draggable')
		.draggable({
			inertia: false,
			// keep the element within the area of its parent
			restrict: {
				restriction: "parent",
				endOnly: false,
				elementRect: { top: 0, left: 0, bottom: 1, right: 1 }
			},
			onmove: dragMoveListener,
			onend: function (event) {
				var target = event.target;
				TweenLite.to(target, 0.2, {ease: Back.easeOut.config(1.7), "webkitTransform":"translate("+target_x+"px, "+target_y+"px)"});
				updatePositionAttributes(target,target_x,target_y);
				panSpan.innerHTML = 0;
				tiltSpan.innerHTML = 0;
        dirSpan.innerHTML = '-';
        linspeedSpan.innerHTML = 0;
        angspeedSpan.innerHTML = 0;
			}
		});

	function dragMoveListener (event) {
		var target = event.target,
				// keep the dragged position in the data-x/data-y attributes
				x = (parseFloat(target.getAttribute('data-x')) || 0) + event.dx,
				y = (parseFloat(target.getAttribute('data-y')) || 0) + event.dy;

		// translate the element
		target.style.webkitTransform = target.style.transform = 'translate(' + x + 'px, ' + y + 'px)';
		updatePositionAttributes(target,x,y);

		// update text display
    var xy = '';
    var yz = '';
    var actn ='';
    var acth ='';
    var dist = Math.sqrt(Math.pow(x-joystick.clientWidth/4,2)+Math.pow(y-joystick.clientHeight/4,2));
    var angle = Math.atan2(y-joystick.clientHeight/4,x-joystick.clientWidth/4);
    var lin = Math.cos(angle / 57.29) * dist * 0.005;
    var ang = Math.sin(angle / 57.29) * dist * 0.05;

    if (Math.abs(x-joystick.clientWidth/4) < 1.0) {
      xy = '';
      actn = ' ';
      lin = '0';
      ang = '0';
    }
    else if (x-joystick.clientWidth/4 > 0) {
      xy = 'right';
      actn = ' neck(CW)';
    }
    else {
      xy = 'left';
      actn = ' neck(CCW)';
    }
    if (Math.abs(y-joystick.clientWidth/4) < 1.0) {
      yz = '';
      acth = ' ';
    }
    else if (y-joystick.clientHeight/4 < 0) {
      acth += ' head(CCW)';
      yz = 'up';
    }
    else {
      yz = 'down';
      acth += ' head(CW)';
    }

    panSpan.innerHTML = actn+acth;
    dirSpan.innerHTML = (xy+' '+yz);
		tiltSpan.innerHTML = (Math.abs(y-joystick.clientHeight/4));
    linspeedSpan.innerHTML = (lin*100).toFixed(2);
    angspeedSpan.innerHTML = (ang*100).toFixed(2);
    
	}

	function updatePositionAttributes(element,x,y){
		target.setAttribute('data-x', x);
		target.setAttribute('data-y', y);
	}

};






function cssCircleMenuchild() {
  $("#joycontainer").toggleClass('active');
  if ($("#joycontainer").hasClass('active')) {
    load_joystick();
  } 
}

  