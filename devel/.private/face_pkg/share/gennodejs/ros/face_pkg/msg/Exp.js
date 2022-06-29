// Auto-generated. Do not edit!

// (in-package face_pkg.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Exp {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.seq = null;
      this.time = null;
      this.action = null;
      this.emotion = null;
      this.auto_imit = null;
    }
    else {
      if (Object.prototype.hasOwnProperty.call(initObj, 'seq')) {
        this.seq = initObj.seq
      }
      else {
        this.seq = 0;
      }
      if (Object.prototype.hasOwnProperty.call(initObj, 'time')) {
        this.time = initObj.time
      }
      else {
        this.time = {secs: 0, nsecs: 0};
      }
      if (Object.prototype.hasOwnProperty.call(initObj, 'action')) {
        this.action = initObj.action
      }
      else {
        this.action = '';
      }
      if (Object.prototype.hasOwnProperty.call(initObj, 'emotion')) {
        this.emotion = initObj.emotion
      }
      else {
        this.emotion = '';
      }
      if (Object.prototype.hasOwnProperty.call(initObj, 'auto_imit')) {
        this.auto_imit = initObj.auto_imit
      }
      else {
        this.auto_imit = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Exp
    // Serialize message field [seq]
    bufferOffset = _serializer.uint32(obj.seq, buffer, bufferOffset);
    // Serialize message field [time]
    bufferOffset = _serializer.time(obj.time, buffer, bufferOffset);
    // Serialize message field [action]
    bufferOffset = _serializer.string(obj.action, buffer, bufferOffset);
    // Serialize message field [emotion]
    bufferOffset = _serializer.string(obj.emotion, buffer, bufferOffset);
    // Serialize message field [auto_imit]
    bufferOffset = _serializer.bool(obj.auto_imit, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Exp
    let len;
    let data = new Exp(null);
    // Deserialize message field [seq]
    data.seq = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [time]
    data.time = _deserializer.time(buffer, bufferOffset);
    // Deserialize message field [action]
    data.action = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [emotion]
    data.emotion = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [auto_imit]
    data.auto_imit = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.action);
    length += _getByteLength(object.emotion);
    return length + 21;
  }

  static datatype() {
    // Returns string type for a message object
    return 'face_pkg/Exp';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '482c620b9db5aa1eb01410b3c618ded5';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint32 seq
    time time
    string action
    string emotion
    bool auto_imit
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Exp(null);
    if (msg.seq !== undefined) {
      resolved.seq = msg.seq;
    }
    else {
      resolved.seq = 0
    }

    if (msg.time !== undefined) {
      resolved.time = msg.time;
    }
    else {
      resolved.time = {secs: 0, nsecs: 0}
    }

    if (msg.action !== undefined) {
      resolved.action = msg.action;
    }
    else {
      resolved.action = ''
    }

    if (msg.emotion !== undefined) {
      resolved.emotion = msg.emotion;
    }
    else {
      resolved.emotion = ''
    }

    if (msg.auto_imit !== undefined) {
      resolved.auto_imit = msg.auto_imit;
    }
    else {
      resolved.auto_imit = false
    }

    return resolved;
    }
};

module.exports = Exp;
