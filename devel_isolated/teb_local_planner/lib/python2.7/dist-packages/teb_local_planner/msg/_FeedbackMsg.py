# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from teb_local_planner/FeedbackMsg.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import costmap_converter.msg
import teb_local_planner.msg
import geometry_msgs.msg
import genpy
import std_msgs.msg

class FeedbackMsg(genpy.Message):
  _md5sum = "e8086148d3a39de24ca2cc423f1e94e6"
  _type = "teb_local_planner/FeedbackMsg"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# Message that contains intermediate results 
# and diagnostics of the (predictive) planner.

std_msgs/Header header

# The planned trajectory (or if multiple plans exist, all of them)
teb_local_planner/TrajectoryMsg[] trajectories

# Index of the trajectory in 'trajectories' that is selected currently
uint16 selected_trajectory_idx

# List of active obstacles
costmap_converter/ObstacleArrayMsg obstacles_msg



================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: teb_local_planner/TrajectoryMsg
# Message that contains a trajectory for mobile robot navigation

std_msgs/Header header
teb_local_planner/TrajectoryPointMsg[] trajectory



================================================================================
MSG: teb_local_planner/TrajectoryPointMsg
# Message that contains single point on a trajectory suited for mobile navigation.
# The trajectory is described by a sequence of poses, velocities,
# accelerations and temporal information.

# Why this message type?
# nav_msgs/Path describes only a path without temporal information.
# trajectory_msgs package contains only messages for joint trajectories.

# The pose of the robot
geometry_msgs/Pose pose

# Corresponding velocity
geometry_msgs/Twist velocity

# Corresponding acceleration
geometry_msgs/Twist acceleration

duration time_from_start




================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: geometry_msgs/Twist
# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: costmap_converter/ObstacleArrayMsg
# Message that contains a list of polygon shaped obstacles.
# Special types:
# Polygon with 1 vertex: Point obstacle
# Polygon with 2 vertices: Line obstacle
# Polygon with more than 2 vertices: First and last points are assumed to be connected

std_msgs/Header header

costmap_converter/ObstacleMsg[] obstacles


================================================================================
MSG: costmap_converter/ObstacleMsg
# Special types:
# Polygon with 1 vertex: Point obstacle (you might also specify a non-zero value for radius)
# Polygon with 2 vertices: Line obstacle
# Polygon with more than 2 vertices: First and last points are assumed to be connected

std_msgs/Header header

# Obstacle footprint (polygon descriptions)
geometry_msgs/Polygon polygon

# Specify the radius for circular/point obstacles
float64 radius

# Obstacle ID
# Specify IDs in order to provide (temporal) relationships
# between obstacles among multiple messages.
int64 id

# Individual orientation (centroid)
geometry_msgs/Quaternion orientation

# Individual velocities (centroid)
geometry_msgs/TwistWithCovariance velocities


================================================================================
MSG: geometry_msgs/Polygon
#A specification of a polygon where the first and last points are assumed to be connected
Point32[] points

================================================================================
MSG: geometry_msgs/Point32
# This contains the position of a point in free space(with 32 bits of precision).
# It is recommeded to use Point wherever possible instead of Point32.  
# 
# This recommendation is to promote interoperability.  
#
# This message is designed to take up less space when sending
# lots of points at once, as in the case of a PointCloud.  

float32 x
float32 y
float32 z
================================================================================
MSG: geometry_msgs/TwistWithCovariance
# This expresses velocity in free space with uncertainty.

Twist twist

# Row-major representation of the 6x6 covariance matrix
# The orientation parameters use a fixed-axis representation.
# In order, the parameters are:
# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)
float64[36] covariance
"""
  __slots__ = ['header','trajectories','selected_trajectory_idx','obstacles_msg']
  _slot_types = ['std_msgs/Header','teb_local_planner/TrajectoryMsg[]','uint16','costmap_converter/ObstacleArrayMsg']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,trajectories,selected_trajectory_idx,obstacles_msg

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(FeedbackMsg, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.trajectories is None:
        self.trajectories = []
      if self.selected_trajectory_idx is None:
        self.selected_trajectory_idx = 0
      if self.obstacles_msg is None:
        self.obstacles_msg = costmap_converter.msg.ObstacleArrayMsg()
    else:
      self.header = std_msgs.msg.Header()
      self.trajectories = []
      self.selected_trajectory_idx = 0
      self.obstacles_msg = costmap_converter.msg.ObstacleArrayMsg()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.trajectories)
      buff.write(_struct_I.pack(length))
      for val1 in self.trajectories:
        _v1 = val1.header
        buff.write(_get_struct_I().pack(_v1.seq))
        _v2 = _v1.stamp
        _x = _v2
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v1.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.trajectory)
        buff.write(_struct_I.pack(length))
        for val2 in val1.trajectory:
          _v3 = val2.pose
          _v4 = _v3.position
          _x = _v4
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
          _v5 = _v3.orientation
          _x = _v5
          buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
          _v6 = val2.velocity
          _v7 = _v6.linear
          _x = _v7
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
          _v8 = _v6.angular
          _x = _v8
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
          _v9 = val2.acceleration
          _v10 = _v9.linear
          _x = _v10
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
          _v11 = _v9.angular
          _x = _v11
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
          _v12 = val2.time_from_start
          _x = _v12
          buff.write(_get_struct_2i().pack(_x.secs, _x.nsecs))
      _x = self
      buff.write(_get_struct_H3I().pack(_x.selected_trajectory_idx, _x.obstacles_msg.header.seq, _x.obstacles_msg.header.stamp.secs, _x.obstacles_msg.header.stamp.nsecs))
      _x = self.obstacles_msg.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.obstacles_msg.obstacles)
      buff.write(_struct_I.pack(length))
      for val1 in self.obstacles_msg.obstacles:
        _v13 = val1.header
        buff.write(_get_struct_I().pack(_v13.seq))
        _v14 = _v13.stamp
        _x = _v14
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v13.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _v15 = val1.polygon
        length = len(_v15.points)
        buff.write(_struct_I.pack(length))
        for val3 in _v15.points:
          _x = val3
          buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
        _x = val1
        buff.write(_get_struct_dq().pack(_x.radius, _x.id))
        _v16 = val1.orientation
        _x = _v16
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
        _v17 = val1.velocities
        _v18 = _v17.twist
        _v19 = _v18.linear
        _x = _v19
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v20 = _v18.angular
        _x = _v20
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        buff.write(_get_struct_36d().pack(*_v17.covariance))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.trajectories is None:
        self.trajectories = None
      if self.obstacles_msg is None:
        self.obstacles_msg = costmap_converter.msg.ObstacleArrayMsg()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.trajectories = []
      for i in range(0, length):
        val1 = teb_local_planner.msg.TrajectoryMsg()
        _v21 = val1.header
        start = end
        end += 4
        (_v21.seq,) = _get_struct_I().unpack(str[start:end])
        _v22 = _v21.stamp
        _x = _v22
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v21.frame_id = str[start:end].decode('utf-8')
        else:
          _v21.frame_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.trajectory = []
        for i in range(0, length):
          val2 = teb_local_planner.msg.TrajectoryPointMsg()
          _v23 = val2.pose
          _v24 = _v23.position
          _x = _v24
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v25 = _v23.orientation
          _x = _v25
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
          _v26 = val2.velocity
          _v27 = _v26.linear
          _x = _v27
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v28 = _v26.angular
          _x = _v28
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v29 = val2.acceleration
          _v30 = _v29.linear
          _x = _v30
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v31 = _v29.angular
          _x = _v31
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v32 = val2.time_from_start
          _x = _v32
          start = end
          end += 8
          (_x.secs, _x.nsecs,) = _get_struct_2i().unpack(str[start:end])
          val1.trajectory.append(val2)
        self.trajectories.append(val1)
      _x = self
      start = end
      end += 14
      (_x.selected_trajectory_idx, _x.obstacles_msg.header.seq, _x.obstacles_msg.header.stamp.secs, _x.obstacles_msg.header.stamp.nsecs,) = _get_struct_H3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.obstacles_msg.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.obstacles_msg.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.obstacles_msg.obstacles = []
      for i in range(0, length):
        val1 = costmap_converter.msg.ObstacleMsg()
        _v33 = val1.header
        start = end
        end += 4
        (_v33.seq,) = _get_struct_I().unpack(str[start:end])
        _v34 = _v33.stamp
        _x = _v34
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v33.frame_id = str[start:end].decode('utf-8')
        else:
          _v33.frame_id = str[start:end]
        _v35 = val1.polygon
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v35.points = []
        for i in range(0, length):
          val3 = geometry_msgs.msg.Point32()
          _x = val3
          start = end
          end += 12
          (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
          _v35.points.append(val3)
        _x = val1
        start = end
        end += 16
        (_x.radius, _x.id,) = _get_struct_dq().unpack(str[start:end])
        _v36 = val1.orientation
        _x = _v36
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        _v37 = val1.velocities
        _v38 = _v37.twist
        _v39 = _v38.linear
        _x = _v39
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v40 = _v38.angular
        _x = _v40
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        start = end
        end += 288
        _v37.covariance = _get_struct_36d().unpack(str[start:end])
        self.obstacles_msg.obstacles.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.trajectories)
      buff.write(_struct_I.pack(length))
      for val1 in self.trajectories:
        _v41 = val1.header
        buff.write(_get_struct_I().pack(_v41.seq))
        _v42 = _v41.stamp
        _x = _v42
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v41.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.trajectory)
        buff.write(_struct_I.pack(length))
        for val2 in val1.trajectory:
          _v43 = val2.pose
          _v44 = _v43.position
          _x = _v44
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
          _v45 = _v43.orientation
          _x = _v45
          buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
          _v46 = val2.velocity
          _v47 = _v46.linear
          _x = _v47
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
          _v48 = _v46.angular
          _x = _v48
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
          _v49 = val2.acceleration
          _v50 = _v49.linear
          _x = _v50
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
          _v51 = _v49.angular
          _x = _v51
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
          _v52 = val2.time_from_start
          _x = _v52
          buff.write(_get_struct_2i().pack(_x.secs, _x.nsecs))
      _x = self
      buff.write(_get_struct_H3I().pack(_x.selected_trajectory_idx, _x.obstacles_msg.header.seq, _x.obstacles_msg.header.stamp.secs, _x.obstacles_msg.header.stamp.nsecs))
      _x = self.obstacles_msg.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.obstacles_msg.obstacles)
      buff.write(_struct_I.pack(length))
      for val1 in self.obstacles_msg.obstacles:
        _v53 = val1.header
        buff.write(_get_struct_I().pack(_v53.seq))
        _v54 = _v53.stamp
        _x = _v54
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v53.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _v55 = val1.polygon
        length = len(_v55.points)
        buff.write(_struct_I.pack(length))
        for val3 in _v55.points:
          _x = val3
          buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
        _x = val1
        buff.write(_get_struct_dq().pack(_x.radius, _x.id))
        _v56 = val1.orientation
        _x = _v56
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
        _v57 = val1.velocities
        _v58 = _v57.twist
        _v59 = _v58.linear
        _x = _v59
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v60 = _v58.angular
        _x = _v60
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        buff.write(_v57.covariance.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.trajectories is None:
        self.trajectories = None
      if self.obstacles_msg is None:
        self.obstacles_msg = costmap_converter.msg.ObstacleArrayMsg()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.trajectories = []
      for i in range(0, length):
        val1 = teb_local_planner.msg.TrajectoryMsg()
        _v61 = val1.header
        start = end
        end += 4
        (_v61.seq,) = _get_struct_I().unpack(str[start:end])
        _v62 = _v61.stamp
        _x = _v62
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v61.frame_id = str[start:end].decode('utf-8')
        else:
          _v61.frame_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.trajectory = []
        for i in range(0, length):
          val2 = teb_local_planner.msg.TrajectoryPointMsg()
          _v63 = val2.pose
          _v64 = _v63.position
          _x = _v64
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v65 = _v63.orientation
          _x = _v65
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
          _v66 = val2.velocity
          _v67 = _v66.linear
          _x = _v67
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v68 = _v66.angular
          _x = _v68
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v69 = val2.acceleration
          _v70 = _v69.linear
          _x = _v70
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v71 = _v69.angular
          _x = _v71
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v72 = val2.time_from_start
          _x = _v72
          start = end
          end += 8
          (_x.secs, _x.nsecs,) = _get_struct_2i().unpack(str[start:end])
          val1.trajectory.append(val2)
        self.trajectories.append(val1)
      _x = self
      start = end
      end += 14
      (_x.selected_trajectory_idx, _x.obstacles_msg.header.seq, _x.obstacles_msg.header.stamp.secs, _x.obstacles_msg.header.stamp.nsecs,) = _get_struct_H3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.obstacles_msg.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.obstacles_msg.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.obstacles_msg.obstacles = []
      for i in range(0, length):
        val1 = costmap_converter.msg.ObstacleMsg()
        _v73 = val1.header
        start = end
        end += 4
        (_v73.seq,) = _get_struct_I().unpack(str[start:end])
        _v74 = _v73.stamp
        _x = _v74
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v73.frame_id = str[start:end].decode('utf-8')
        else:
          _v73.frame_id = str[start:end]
        _v75 = val1.polygon
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v75.points = []
        for i in range(0, length):
          val3 = geometry_msgs.msg.Point32()
          _x = val3
          start = end
          end += 12
          (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
          _v75.points.append(val3)
        _x = val1
        start = end
        end += 16
        (_x.radius, _x.id,) = _get_struct_dq().unpack(str[start:end])
        _v76 = val1.orientation
        _x = _v76
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        _v77 = val1.velocities
        _v78 = _v77.twist
        _v79 = _v78.linear
        _x = _v79
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v80 = _v78.angular
        _x = _v80
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        start = end
        end += 288
        _v77.covariance = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=36)
        self.obstacles_msg.obstacles.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_36d = None
def _get_struct_36d():
    global _struct_36d
    if _struct_36d is None:
        _struct_36d = struct.Struct("<36d")
    return _struct_36d
_struct_H3I = None
def _get_struct_H3I():
    global _struct_H3I
    if _struct_H3I is None:
        _struct_H3I = struct.Struct("<H3I")
    return _struct_H3I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_3f = None
def _get_struct_3f():
    global _struct_3f
    if _struct_3f is None:
        _struct_3f = struct.Struct("<3f")
    return _struct_3f
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_4d = None
def _get_struct_4d():
    global _struct_4d
    if _struct_4d is None:
        _struct_4d = struct.Struct("<4d")
    return _struct_4d
_struct_dq = None
def _get_struct_dq():
    global _struct_dq
    if _struct_dq is None:
        _struct_dq = struct.Struct("<dq")
    return _struct_dq
_struct_2i = None
def _get_struct_2i():
    global _struct_2i
    if _struct_2i is None:
        _struct_2i = struct.Struct("<2i")
    return _struct_2i
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
