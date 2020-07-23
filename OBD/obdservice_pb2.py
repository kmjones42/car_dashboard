# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: obdservice.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='obdservice.proto',
  package='OBD',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10obdservice.proto\x12\x03OBD\"-\n\x0fObdRequestTypes\x12\r\n\x05speed\x18\x01 \x01(\x08\x12\x0b\n\x03rpm\x18\x02 \x01(\x08\")\n\x0bObdResponse\x12\r\n\x05speed\x18\x01 \x01(\r\x12\x0b\n\x03rpm\x18\x02 \x01(\r2>\n\x03Obd\x12\x37\n\tStreamObd\x12\x14.OBD.ObdRequestTypes\x1a\x10.OBD.ObdResponse\"\x00\x30\x01\x62\x06proto3'
)




_OBDREQUESTTYPES = _descriptor.Descriptor(
  name='ObdRequestTypes',
  full_name='OBD.ObdRequestTypes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='speed', full_name='OBD.ObdRequestTypes.speed', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rpm', full_name='OBD.ObdRequestTypes.rpm', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=25,
  serialized_end=70,
)


_OBDRESPONSE = _descriptor.Descriptor(
  name='ObdResponse',
  full_name='OBD.ObdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='speed', full_name='OBD.ObdResponse.speed', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rpm', full_name='OBD.ObdResponse.rpm', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=72,
  serialized_end=113,
)

DESCRIPTOR.message_types_by_name['ObdRequestTypes'] = _OBDREQUESTTYPES
DESCRIPTOR.message_types_by_name['ObdResponse'] = _OBDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObdRequestTypes = _reflection.GeneratedProtocolMessageType('ObdRequestTypes', (_message.Message,), {
  'DESCRIPTOR' : _OBDREQUESTTYPES,
  '__module__' : 'obdservice_pb2'
  # @@protoc_insertion_point(class_scope:OBD.ObdRequestTypes)
  })
_sym_db.RegisterMessage(ObdRequestTypes)

ObdResponse = _reflection.GeneratedProtocolMessageType('ObdResponse', (_message.Message,), {
  'DESCRIPTOR' : _OBDRESPONSE,
  '__module__' : 'obdservice_pb2'
  # @@protoc_insertion_point(class_scope:OBD.ObdResponse)
  })
_sym_db.RegisterMessage(ObdResponse)



_OBD = _descriptor.ServiceDescriptor(
  name='Obd',
  full_name='OBD.Obd',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=115,
  serialized_end=177,
  methods=[
  _descriptor.MethodDescriptor(
    name='StreamObd',
    full_name='OBD.Obd.StreamObd',
    index=0,
    containing_service=None,
    input_type=_OBDREQUESTTYPES,
    output_type=_OBDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_OBD)

DESCRIPTOR.services_by_name['Obd'] = _OBD

# @@protoc_insertion_point(module_scope)
