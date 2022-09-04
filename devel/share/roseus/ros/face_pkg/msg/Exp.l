;; Auto-generated. Do not edit!


(when (boundp 'face_pkg::Exp)
  (if (not (find-package "FACE_PKG"))
    (make-package "FACE_PKG"))
  (shadow 'Exp (find-package "FACE_PKG")))
(unless (find-package "FACE_PKG::EXP")
  (make-package "FACE_PKG::EXP"))

(in-package "ROS")
;;//! \htmlinclude Exp.msg.html


(defclass face_pkg::Exp
  :super ros::object
  :slots (_seq _time _action _emotion _auto_imit ))

(defmethod face_pkg::Exp
  (:init
   (&key
    ((:seq __seq) 0)
    ((:time __time) (instance ros::time :init))
    ((:action __action) "")
    ((:emotion __emotion) "")
    ((:auto_imit __auto_imit) nil)
    )
   (send-super :init)
   (setq _seq (round __seq))
   (setq _time __time)
   (setq _action (string __action))
   (setq _emotion (string __emotion))
   (setq _auto_imit __auto_imit)
   self)
  (:seq
   (&optional __seq)
   (if __seq (setq _seq __seq)) _seq)
  (:time
   (&optional __time)
   (if __time (setq _time __time)) _time)
  (:action
   (&optional __action)
   (if __action (setq _action __action)) _action)
  (:emotion
   (&optional __emotion)
   (if __emotion (setq _emotion __emotion)) _emotion)
  (:auto_imit
   (&optional (__auto_imit :null))
   (if (not (eq __auto_imit :null)) (setq _auto_imit __auto_imit)) _auto_imit)
  (:serialization-length
   ()
   (+
    ;; uint32 _seq
    4
    ;; time _time
    8
    ;; string _action
    4 (length _action)
    ;; string _emotion
    4 (length _emotion)
    ;; bool _auto_imit
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint32 _seq
       (write-long _seq s)
     ;; time _time
       (write-long (send _time :sec) s) (write-long (send _time :nsec) s)
     ;; string _action
       (write-long (length _action) s) (princ _action s)
     ;; string _emotion
       (write-long (length _emotion) s) (princ _emotion s)
     ;; bool _auto_imit
       (if _auto_imit (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint32 _seq
     (setq _seq (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; time _time
     (send _time :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _time :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; string _action
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _action (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _emotion
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _emotion (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; bool _auto_imit
     (setq _auto_imit (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get face_pkg::Exp :md5sum-) "482c620b9db5aa1eb01410b3c618ded5")
(setf (get face_pkg::Exp :datatype-) "face_pkg/Exp")
(setf (get face_pkg::Exp :definition-)
      "uint32 seq
time time
string action
string emotion
bool auto_imit
")



(provide :face_pkg/Exp "482c620b9db5aa1eb01410b3c618ded5")


