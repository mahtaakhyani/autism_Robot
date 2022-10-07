
(cl:in-package :asdf)

(defsystem "face_pkg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ActionHeader" :depends-on ("_package_ActionHeader"))
    (:file "_package_ActionHeader" :depends-on ("_package"))
    (:file "Exp" :depends-on ("_package_Exp"))
    (:file "_package_Exp" :depends-on ("_package"))
  ))