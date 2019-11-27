// Generated by gencpp from file path_server/SetPathNameResponse.msg
// DO NOT EDIT!


#ifndef PATH_SERVER_MESSAGE_SETPATHNAMERESPONSE_H
#define PATH_SERVER_MESSAGE_SETPATHNAMERESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace path_server
{
template <class ContainerAllocator>
struct SetPathNameResponse_
{
  typedef SetPathNameResponse_<ContainerAllocator> Type;

  SetPathNameResponse_()
    {
    }
  SetPathNameResponse_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::path_server::SetPathNameResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::path_server::SetPathNameResponse_<ContainerAllocator> const> ConstPtr;

}; // struct SetPathNameResponse_

typedef ::path_server::SetPathNameResponse_<std::allocator<void> > SetPathNameResponse;

typedef boost::shared_ptr< ::path_server::SetPathNameResponse > SetPathNameResponsePtr;
typedef boost::shared_ptr< ::path_server::SetPathNameResponse const> SetPathNameResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::path_server::SetPathNameResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::path_server::SetPathNameResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace path_server

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::path_server::SetPathNameResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::path_server::SetPathNameResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::path_server::SetPathNameResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::path_server::SetPathNameResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::path_server::SetPathNameResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::path_server::SetPathNameResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::path_server::SetPathNameResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::path_server::SetPathNameResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::path_server::SetPathNameResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "path_server/SetPathNameResponse";
  }

  static const char* value(const ::path_server::SetPathNameResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::path_server::SetPathNameResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
;
  }

  static const char* value(const ::path_server::SetPathNameResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::path_server::SetPathNameResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SetPathNameResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::path_server::SetPathNameResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::path_server::SetPathNameResponse_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // PATH_SERVER_MESSAGE_SETPATHNAMERESPONSE_H
