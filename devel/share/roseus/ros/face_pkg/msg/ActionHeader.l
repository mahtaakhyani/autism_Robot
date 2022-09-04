;; Auto-generated. Do not edit!


(when (boundp 'face_pkg::ActionHeader)
  (if (not (find-package "FACE_PKG"))
    (make-package "FACE_PKG"))
  (shadow 'ActionHeader (find-package "FACE_PKG")))
(unless (find-package "FACE_PKG::ACTIONHEADER")
  (make-package "FACE_PKG::ACTIONHEADER"))

(in-package "ROS")
;;//! \htmlinclude ActionHeader.msg.html


(defclass face_pkg::ActionHeader
  :super ros::object
  :slots (_seq _stamp _command_type ))

(defmethod face_pkg::ActionHeader
  (:init
   (&key
    ((:seq __seq) 0)
    ((:stamp __stamp) (instance ros::time :init))
    ((:command_type __command_type) "")
    )
   (send-super :init)
   (setq _seq (round __seq))
   (setq _stamp __stamp)
   (setq _command_type (string __command_type))
   self)
  (:seq
   (&optional __seq)
   (if __seq (setq _seq __seq)) _seq)
  (:stamp
   (&optional __stamp)
   (if __stamp (setq _stamp __stamp)) _stamp)
  (:command_type
   (&optional __command_type)
   (if __command_type (setq _command_type __command_type)) _command_type)
  (:serialization-length
   ()
   (+
    ;; uint32 _seq
    4
    ;; time _stamp
    8
    ;; string _command_type
    4 (length _command_type)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint32 _seq
       (write-long _seq s)
     ;; time _stamp
       (write-long (send _stamp :sec) s) (write-long (send _stamp :nsec) s)
     ;; string _command_type
       (write-long (length _command_type) s) (princ _command_type s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint32 _seq
     (setq _seq (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; time _stamp
     (send _stamp :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _stamp :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; string _command_type
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _command_type (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get face_pkg::ActionHeader :md5sum-) "8ac1cca4c394f260feb2e7efafd2f5dc")
(setf (get face_pkg::ActionHeader :datatype-) "face_pkg/ActionHeader")
(setf (get face_pkg::ActionHeader :definition-)
      "
  uint32 seq
  time stamp
  string command_type


")



(provide :face_pkg/ActionHeader "8ac1cca4c394f260feb2e7efafd2f5dc")


