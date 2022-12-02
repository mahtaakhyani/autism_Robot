
(cl:in-package :asdf)

(defsystem "face_pkg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ActionHeader" :depends-on ("_package_ActionHeader"))
    (:file "_package_ActionHeader" :depends-on ("_package"))
    (:file "Exp" :depends-on ("_package_Exp"))
    (:file "_package_Exp" :depends-on ("_package"))
    (:file "Motor" :depends-on ("_package_Motor"))
    (:file "_package_Motor" :depends-on ("_package"))
    (:file "Trans" :depends-on ("_package_Trans"))
    (:file "_package_Trans" :depends-on ("_package"))
  ))