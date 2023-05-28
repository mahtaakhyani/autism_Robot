

// var twist;
// var cmdVel;
// var publishImmidiately = true;
// var robot_WS;
// var joystick;
var teleop;
var ros;
var motor = '';

// var joystick;
// var linear_x
// var linear_y
// var angular_z;

//     // Add event listener for slider moves
//     // robotSpeedRange = document.getElementById("robot-speed");
//     // robotSpeedRange.oninput = function () {
//     //     teleop.scale = robotSpeedRange.value / 100
//     // }
// }


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
    
		// update text display
    var xy = '';
    var yz = '';
    var actn ='';
    var acth ='';
    var dist = Math.sqrt(Math.pow(x-joystick.clientWidth/4,2)+Math.pow(y-joystick.clientHeight/4,2));
    dist = 445+x*3.87;
    var angle = Math.atan2(y-joystick.clientHeight/4,x-joystick.clientWidth/4);
    var lin = Math.cos(angle / 57.29) * dist * 0.005;
    var ang = Math.sin(angle / 57.29) * dist * 0.05;
    
    if (Math.abs(x-joystick.clientWidth/4) < 1.0) {
      xy = '';
      actn = ' ';
      lin = '0';
      ang = '0';
      motor = 0; //neck=0
    }
    else if (x-joystick.clientWidth/4 > 0) {
      xy = 'right';
      actn = ' neck(CW)';
      motor = 0; //neck=0
    }
    else {
      xy = 'left';
      actn = ' neck(CCW)';
      motor = 0; //neck=0
    }
    if (Math.abs(y-joystick.clientWidth/4) < 1.0) {
      yz = '';
      acth = ' ';
      motor = 0; //head=1
    }
    else if (y-joystick.clientHeight/4 < 0) {
      acth += ' head(CCW)';
      yz = 'up';
      motor = 0; //head=1
    }
    else {
      yz = 'down';
      acth += ' head(CW)';
      motor = 0; //head=1
    }
    
    panSpan.innerHTML = actn+acth;
    dirSpan.innerHTML = (xy+' '+yz);
		tiltSpan.innerHTML = (Math.abs(y-joystick.clientHeight/4));
    linspeedSpan.innerHTML = (dist).toFixed(2);
    angspeedSpan.innerHTML = (ang*100).toFixed(2);
    
    // updatePositionAttributes(target,x,y);
    moveAction(lin,ang,motor);
	}
  
	function updatePositionAttributes(element,x,y){
		target.setAttribute('data-x', x);
		target.setAttribute('data-y', y);
	}
  var isMouseDown,initX,initY,height = draggable.offsetHeight,width = draggable.offsetWidth;

draggable.addEventListener('mousedown', function(e) {
  isMouseDown = true;
  document.body.classList.add('no-select');
  initX = e.offsetX;
  initY = e.offsetY;
})

document.addEventListener('mousemove', function(e) {
  if (isMouseDown) {
    var cx = e.clientX - initX,
        cy = e.clientY - initY;
    if (cx < 0) {
      cx = 0;
    }
    if (cy < 0) {
      cy = 0;
    }
    if (window.innerWidth - e.clientX + initX < width) {
      cx = window.innerWidth - width;
    }
    if (e.clientY > window.innerHeight - height+ initY) {
      cy = window.innerHeight - height;
    }
    draggable.style.left = cx + 'px';
    draggable.style.top = cy + 'px';
  }
})

draggable.addEventListener('mouseup', function() {
  isMouseDown = false;
  document.body.classList.remove('no-select');
})


};

function moveAction(linear, angular, motor_number) {
    // Init message with zero values.
  movemsg = new ROSLIB.Message({
        joint: 'head',
        motor: 0,
        pose: 0
    })

  if (linear !== 0 && angular !== 0) {
      movemsg.motor = motor_number;
      movemsg.pose = linear*1225;

        // Init topic object
      cmdVel = new ROSLIB.Topic({
        ros: ros,
        name: '/head_cmd_vel',
        messageType: 'face_pkg/Motor'
     });
      // Register publisher within ROS system
      cmdVel.advertise();
      console.log(movemsg);
      // Publish message to ROS.
      cmdVel.publish(movemsg);
}
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
}




// --------------------- Gamepad ---------------------
var gamepad = {
  connected: false,
  timestamp: null,
  buttons: [],
  axes: []
}

var buttonMap = [
  'A','B',null,'X','Y',null,'BL','BR',null,null,'SELECT','START'
];

var axesMap = [
  'U','D','L','R'
];


var pollGamePad = function(){
  
  var p1 = navigator.getGamepads()[0];

  if(!p1 || (!p1.connected && gamepad.connected)){
    onDisconnect();
    return window.requestAnimationFrame(pollGamePad);
  }
  
  if(p1.connected && !gamepad.connected)
    onConnect();
  
  if(!p1 || !p1.timestamp || p1.timestamp===gamepad.timestamp) 
    return window.requestAnimationFrame(pollGamePad);

  //check buttons
  var buttons = _.map(p1.buttons, function(b){ return b.pressed });
  _.each(buttons, function(value, index){
    var isChange = (value!==gamepad.buttons[index]);
    if(isChange){
      if(value)
        onButtonDown(index);
      else
        onButtonUp(index);
    }
  })

  //check axes
  var axes = _.map(p1.axes, function(b){ return b });
  _.each(axes, function(value, index){
    var isChange = (value!==gamepad.axes[index]);
    if(isChange){
      //trim residual decimals only {-1,0,1}
      value = parseInt(value);
      if(!index){
        
        if(value<0){
          onAxesDown(2);
          onAxesUp(3);
        }
        else if(value>0){
          onAxesDown(3)
          onAxesUp(2)
        }
        else{
          onAxesUp(2);
          onAxesUp(3);
        }

      }
      else{

        if(value<0){
          onAxesDown(0);
          onAxesUp(1);
        }
        else if(value>0){
          onAxesDown(1);
          onAxesUp(0);
        }
        else{
          onAxesUp(0);
          onAxesUp(1);
        }
        
        
      }
      /*if(value)
        onButtonDown(index);
      else
        onButtonUp(index);
        */
      //onAxesChange(index);
    }
  })  
  
  //update gamepad object
  gamepad.timestamp = p1.timestamp;
  gamepad.buttons = buttons;
  gamepad.axes = axes;
  
  //chain next update
  window.requestAnimationFrame(pollGamePad);
    
}


var onButtonDown = function(index){
  $('.button-'+buttonMap[index]).addClass('active');
}

var onButtonUp = function(index){
  $('.button-'+buttonMap[index]).removeClass('active');
}

var onAxesDown = function(index){
  $('.axes-'+axesMap[index]).addClass('active');
}

var onAxesUp = function(index){
  $('.axes-'+axesMap[index]).removeClass('active');
}

var onAxesChange = function(index){
  
  if(index){
    
  }
  //console.log('axis down '+index);
  console.log(index+' -> '+navigator.getGamepads()[0].axes[index]);
}

var onConnect = function(index){
  $('.status').text('CONNECTED!');
}

var onDisconnect = function(index){
  $('.status').text('NOT CONNECTED');
}





  // Creating the circular menu ---------------------
  var el = '.js-menu';
  var myMenu = cssCircleMenu(el);
  function cssCircleMenu(el) {
    var $menu = document.querySelector(el); 
    var $menuToggle = $menu ? $menu.querySelector('.js-menu-toggle') : undefined;
    var $menuMask = $menu ? $menu.querySelector('.js-menu-mask') : undefined;

    if (!$menu || !$menuToggle || !$menuMask) { 
      throw new Error('Invalid elements, check the structure.');
    } else {
      init();
    }

    return {
      openMenu: openMenu,
      closeMenu: closeMenu
    };

    function init() {
      $menuToggle.addEventListener('click', function(e) {
        e.preventDefault();
        toggleMenu();
      });
    }

    function toggleMenu() {
      $menuToggle.classList.contains('is-active')
        ? closeMenu()
        : openMenu();
    }

    function openMenu() {
      $menu.classList.add('is-active');
      $menuToggle.classList.add('is-active');
      $menuMask.classList.add('is-active');
    }

    function closeMenu() {
      $menu.classList.remove('is-active');
      $menuToggle.classList.remove('is-active');
      $menuMask.classList.remove('is-active');
    }
  };



function gameCircleMenuchild() {
  $("#joycontainer").toggleClass('active');
  if ($("#joycontainer").hasClass('active')) {
    load_joystick();
    pollGamePad();
  } 
}

  