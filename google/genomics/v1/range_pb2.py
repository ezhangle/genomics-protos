# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/genomics/v1/range.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/genomics/v1/range.proto',
  package='google.genomics.v1',
  syntax='proto3',
  serialized_pb=_b('\n\x1egoogle/genomics/v1/range.proto\x12\x12google.genomics.v1\";\n\x05Range\x12\x16\n\x0ereference_name\x18\x01 \x01(\t\x12\r\n\x05start\x18\x02 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x03 \x01(\x03\x42\x03\xf8\x01\x01\x62\x06proto3')
)




_RANGE = _descriptor.Descriptor(
  name='Range',
  full_name='google.genomics.v1.Range',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reference_name', full_name='google.genomics.v1.Range.reference_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='google.genomics.v1.Range.start', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='google.genomics.v1.Range.end', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=113,
)

DESCRIPTOR.message_types_by_name['Range'] = _RANGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Range = _reflection.GeneratedProtocolMessageType('Range', (_message.Message,), dict(
  DESCRIPTOR = _RANGE,
  __module__ = 'google.genomics.v1.range_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.Range)
  ))
_sym_db.RegisterMessage(Range)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\370\001\001'))
# @@protoc_insertion_point(module_scope)