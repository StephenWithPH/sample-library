# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: foo.proto

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
  name='foo.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\tfoo.proto\",\n\x03\x46oo\x12\x0b\n\x03\x66oo\x18\x01 \x01(\x05\x12\x0b\n\x03\x62\x61r\x18\x02 \x01(\x02\x12\x0b\n\x03\x62\x61z\x18\x03 \x01(\x08\x62\x06proto3')
)




_FOO = _descriptor.Descriptor(
  name='Foo',
  full_name='Foo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='foo', full_name='Foo.foo', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bar', full_name='Foo.bar', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='baz', full_name='Foo.baz', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=13,
  serialized_end=57,
)

DESCRIPTOR.message_types_by_name['Foo'] = _FOO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Foo = _reflection.GeneratedProtocolMessageType('Foo', (_message.Message,), dict(
  DESCRIPTOR = _FOO,
  __module__ = 'foo_pb2'
  # @@protoc_insertion_point(class_scope:Foo)
  ))
_sym_db.RegisterMessage(Foo)


# @@protoc_insertion_point(module_scope)
