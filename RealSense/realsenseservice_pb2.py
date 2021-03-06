# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: realsenseservice.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='realsenseservice.proto',
  package='RealSense',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16realsenseservice.proto\x12\tRealSense\"L\n\x0cRequestVideo\x12\x12\n\nleft_image\x18\x01 \x01(\x08\x12\x13\n\x0bright_image\x18\x02 \x01(\x08\x12\x13\n\x0b\x64\x65pth_image\x18\x03 \x01(\x08\"$\n\x13RealSenseVideoFrame\x12\r\n\x05\x66rame\x18\x01 \x01(\x0c\x32U\n\tRealSense\x12H\n\x0bStreamVideo\x12\x17.RealSense.RequestVideo\x1a\x1e.RealSense.RealSenseVideoFrame0\x01\x62\x06proto3'
)




_REQUESTVIDEO = _descriptor.Descriptor(
  name='RequestVideo',
  full_name='RealSense.RequestVideo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='left_image', full_name='RealSense.RequestVideo.left_image', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='right_image', full_name='RealSense.RequestVideo.right_image', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='depth_image', full_name='RealSense.RequestVideo.depth_image', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=113,
)


_REALSENSEVIDEOFRAME = _descriptor.Descriptor(
  name='RealSenseVideoFrame',
  full_name='RealSense.RealSenseVideoFrame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame', full_name='RealSense.RealSenseVideoFrame.frame', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=151,
)

DESCRIPTOR.message_types_by_name['RequestVideo'] = _REQUESTVIDEO
DESCRIPTOR.message_types_by_name['RealSenseVideoFrame'] = _REALSENSEVIDEOFRAME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestVideo = _reflection.GeneratedProtocolMessageType('RequestVideo', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTVIDEO,
  '__module__' : 'realsenseservice_pb2'
  # @@protoc_insertion_point(class_scope:RealSense.RequestVideo)
  })
_sym_db.RegisterMessage(RequestVideo)

RealSenseVideoFrame = _reflection.GeneratedProtocolMessageType('RealSenseVideoFrame', (_message.Message,), {
  'DESCRIPTOR' : _REALSENSEVIDEOFRAME,
  '__module__' : 'realsenseservice_pb2'
  # @@protoc_insertion_point(class_scope:RealSense.RealSenseVideoFrame)
  })
_sym_db.RegisterMessage(RealSenseVideoFrame)



_REALSENSE = _descriptor.ServiceDescriptor(
  name='RealSense',
  full_name='RealSense.RealSense',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=153,
  serialized_end=238,
  methods=[
  _descriptor.MethodDescriptor(
    name='StreamVideo',
    full_name='RealSense.RealSense.StreamVideo',
    index=0,
    containing_service=None,
    input_type=_REQUESTVIDEO,
    output_type=_REALSENSEVIDEOFRAME,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_REALSENSE)

DESCRIPTOR.services_by_name['RealSense'] = _REALSENSE

# @@protoc_insertion_point(module_scope)
