; Auto-generated. Do not edit!


(cl:in-package face_pkg-msg)


;//! \htmlinclude ActionHeader.msg.html

(cl:defclass <ActionHeader> (roslisp-msg-protocol:ros-message)
  ((seq
    :reader seq
    :initarg :seq
    :type cl:integer
    :initform 0)
   (stamp
    :reader stamp
    :initarg :stamp
    :type cl:real
    :initform 0)
   (command_type
    :reader command_type
    :initarg :command_type
    :type cl:string
    :initform ""))
)

(cl:defclass ActionHeader (<ActionHeader>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ActionHeader>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ActionHeader)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name face_pkg-msg:<ActionHeader> is deprecated: use face_pkg-msg:ActionHeader instead.")))

(cl:ensure-generic-function 'seq-val :lambda-list '(m))
(cl:defmethod seq-val ((m <ActionHeader>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader face_pkg-msg:seq-val is deprecated.  Use face_pkg-msg:seq instead.")
  (seq m))

(cl:ensure-generic-function 'stamp-val :lambda-list '(m))
(cl:defmethod stamp-val ((m <ActionHeader>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader face_pkg-msg:stamp-val is deprecated.  Use face_pkg-msg:stamp instead.")
  (stamp m))

(cl:ensure-generic-function 'command_type-val :lambda-list '(m))
(cl:defmethod command_type-val ((m <ActionHeader>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader face_pkg-msg:command_type-val is deprecated.  Use face_pkg-msg:command_type instead.")
  (command_type m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ActionHeader>) ostream)
  "Serializes a message object of type '<ActionHeader>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'seq)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'seq)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'seq)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'seq)) ostream)
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'stamp)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'stamp) (cl:floor (cl:slot-value msg 'stamp)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'command_type))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'command_type))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ActionHeader>) istream)
  "Deserializes a message object of type '<ActionHeader>"
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
      (cl:setf (cl:slot-value msg 'stamp) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'command_type) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'command_type) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ActionHeader>)))
  "Returns string type for a message object of type '<ActionHeader>"
  "face_pkg/ActionHeader")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ActionHeader)))
  "Returns string type for a message object of type 'ActionHeader"
  "face_pkg/ActionHeader")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ActionHeader>)))
  "Returns md5sum for a message object of type '<ActionHeader>"
  "8ac1cca4c394f260feb2e7efafd2f5dc")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ActionHeader)))
  "Returns md5sum for a message object of type 'ActionHeader"
  "8ac1cca4c394f260feb2e7efafd2f5dc")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ActionHeader>)))
  "Returns full string definition for message of type '<ActionHeader>"
  (cl:format cl:nil "~%  uint32 seq~%  time stamp~%  string command_type~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ActionHeader)))
  "Returns full string definition for message of type 'ActionHeader"
  (cl:format cl:nil "~%  uint32 seq~%  time stamp~%  string command_type~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ActionHeader>))
  (cl:+ 0
     4
     8
     4 (cl:length (cl:slot-value msg 'command_type))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ActionHeader>))
  "Converts a ROS message object to a list"
  (cl:list 'ActionHeader
    (cl:cons ':seq (seq msg))
    (cl:cons ':stamp (stamp msg))
    (cl:cons ':command_type (command_type msg))
))
