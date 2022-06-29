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

class ActionHeader {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.seq = null;
      this.stamp = null;
      this.command_type = null;
    }
    else {
      if (Object.prototype.hasOwnProperty.call(initObj, 'seq')) {
        this.seq = initObj.seq
      }
      else {
        this.seq = 0;
      }
      if (Object.prototype.hasOwnProperty.call(initObj, 'stamp')) {
        this.stamp = initObj.stamp
      }
      else {
        this.stamp = {secs: 0, nsecs: 0};
      }
      if (Object.prototype.hasOwnProperty.call(initObj, 'command_type')) {
        this.command_type = initObj.command_type
      }
      else {
        this.command_type = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ActionHeader
    // Serialize message field [seq]
    bufferOffset = _serializer.uint32(obj.seq, buffer, bufferOffset);
    // Serialize message field [stamp]
    bufferOffset = _serializer.time(obj.stamp, buffer, bufferOffset);
    // Serialize message field [command_type]
    bufferOffset = _serializer.string(obj.command_type, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ActionHeader
    let len;
    let data = new ActionHeader(null);
    // Deserialize message field [seq]
    data.seq = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [stamp]
    data.stamp = _deserializer.time(buffer, bufferOffset);
    // Deserialize message field [command_type]
    data.command_type = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.command_type);
    return length + 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'face_pkg/ActionHeader';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8ac1cca4c394f260feb2e7efafd2f5dc';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
      uint32 seq
      time stamp
      string command_type
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ActionHeader(null);
    if (msg.seq !== undefined) {
      resolved.seq = msg.seq;
    }
    else {
      resolved.seq = 0
    }

    if (msg.stamp !== undefined) {
      resolved.stamp = msg.stamp;
    }
    else {
      resolved.stamp = {secs: 0, nsecs: 0}
    }

    if (msg.command_type !== undefined) {
      resolved.command_type = msg.command_type;
    }
    else {
      resolved.command_type = ''
    }

    return resolved;
    }
};

module.exports = ActionHeader;
