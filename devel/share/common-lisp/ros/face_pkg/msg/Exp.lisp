; Auto-generated. Do not edit!


(cl:in-package face_pkg-msg)


;//! \htmlinclude Exp.msg.html

(cl:defclass <Exp> (roslisp-msg-protocol:ros-message)
  ((seq
    :reader seq
    :initarg :seq
    :type cl:integer
    :initform 0)
   (time
    :reader time
    :initarg :time
    :type cl:real
    :initform 0)
   (action
    :reader action
    :initarg :action
    :type cl:string
    :initform "")
   (emotion
    :reader emotion
    :initarg :emotion
    :type cl:string
    :initform "")
   (auto_imit
    :reader auto_imit
    :initarg :auto_imit
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Exp (<Exp>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Exp>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Exp)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name face_pkg-msg:<Exp> is deprecated: use face_pkg-msg:Exp instead.")))

(cl:ensure-generic-function 'seq-val :lambda-list '(m))
(cl:defmethod seq-val ((m <Exp>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader face_pkg-msg:seq-val is deprecated.  Use face_pkg-msg:seq instead.")
  (seq m))

(cl:ensure-generic-function 'time-val :lambda-list '(m))
(cl:defmethod time-val ((m <Exp>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader face_pkg-msg:time-val is deprecated.  Use face_pkg-msg:time instead.")
  (time m))

(cl:ensure-generic-function 'action-val :lambda-list '(m))
(cl:defmethod action-val ((m <Exp>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader face_pkg-msg:action-val is deprecated.  Use face_pkg-msg:action instead.")
  (action m))

(cl:ensure-generic-function 'emotion-val :lambda-list '(m))
(cl:defmethod emotion-val ((m <Exp>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader face_pkg-msg:emotion-val is deprecated.  Use face_pkg-msg:emotion instead.")
  (emotion m))

(cl:ensure-generic-function 'auto_imit-val :lambda-list '(m))
(cl:defmethod auto_imit-val ((m <Exp>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader face_pkg-msg:auto_imit-val is deprecated.  Use face_pkg-msg:auto_imit instead.")
  (auto_imit m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Exp>) ostream)
  "Serializes a message object of type '<Exp>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'seq)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'seq)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'seq)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'seq)) ostream)
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'time)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'time) (cl:floor (cl:slot-value msg 'time)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'action))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'action))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'emotion))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'emotion))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'auto_imit) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Exp>) istream)
  "Deserializes a message object of type '<Exp>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'seq)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'seq)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'seq)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'seq)) (cl:read-byte istream))
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'time) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'action) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'action) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'emotion) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'emotion) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:slot-value msg 'auto_imit) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Exp>)))
  "Returns string type for a message object of type '<Exp>"
  "face_pkg/Exp")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Exp)))
  "Returns string type for a message object of type 'Exp"
  "face_pkg/Exp")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Exp>)))
  "Returns md5sum for a message object of type '<Exp>"
  "482c620b9db5aa1eb01410b3c618ded5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Exp)))
  "Returns md5sum for a message object of type 'Exp"
  "482c620b9db5aa1eb01410b3c618ded5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Exp>)))
  "Returns full string definition for message of type '<Exp>"
  (cl:format cl:nil "uint32 seq~%time time~%string action~%string emotion~%bool auto_imit~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Exp)))
  "Returns full string definition for message of type 'Exp"
  (cl:format cl:nil "uint32 seq~%time time~%string action~%string emotion~%bool auto_imit~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Exp>))
  (cl:+ 0
     4
     8
     4 (cl:length (cl:slot-value msg 'action))
     4 (cl:length (cl:slot-value msg 'emotion))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Exp>))
  "Converts a ROS message object to a list"
  (cl:list 'Exp
    (cl:cons ':seq (seq msg))
    (cl:cons ':time (time msg))
    (cl:cons ':action (action msg))
    (cl:cons ':emotion (emotion msg))
    (cl:cons ':auto_imit (auto_imit msg))
))
