# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/dns/fakedns/fakedns.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x61pp/dns/fakedns/fakedns.proto\x12\x14xray.app.dns.fakedns\"/\n\x0b\x46\x61keDnsPool\x12\x0f\n\x07ip_pool\x18\x01 \x01(\t\x12\x0f\n\x07lruSize\x18\x02 \x01(\x03\"D\n\x10\x46\x61keDnsPoolMulti\x12\x30\n\x05pools\x18\x01 \x03(\x0b\x32!.xray.app.dns.fakedns.FakeDnsPoolB^\n\x18\x63om.xray.app.dns.fakednsP\x01Z)github.com/xtls/xray-core/app/dns/fakedns\xaa\x02\x14Xray.App.Dns.Fakednsb\x06proto3')



_FAKEDNSPOOL = DESCRIPTOR.message_types_by_name['FakeDnsPool']
_FAKEDNSPOOLMULTI = DESCRIPTOR.message_types_by_name['FakeDnsPoolMulti']
FakeDnsPool = _reflection.GeneratedProtocolMessageType('FakeDnsPool', (_message.Message,), {
  'DESCRIPTOR' : _FAKEDNSPOOL,
  '__module__' : 'app.dns.fakedns.fakedns_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.dns.fakedns.FakeDnsPool)
  })
_sym_db.RegisterMessage(FakeDnsPool)

FakeDnsPoolMulti = _reflection.GeneratedProtocolMessageType('FakeDnsPoolMulti', (_message.Message,), {
  'DESCRIPTOR' : _FAKEDNSPOOLMULTI,
  '__module__' : 'app.dns.fakedns.fakedns_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.dns.fakedns.FakeDnsPoolMulti)
  })
_sym_db.RegisterMessage(FakeDnsPoolMulti)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.xray.app.dns.fakednsP\001Z)github.com/xtls/xray-core/app/dns/fakedns\252\002\024Xray.App.Dns.Fakedns'
  _FAKEDNSPOOL._serialized_start=55
  _FAKEDNSPOOL._serialized_end=102
  _FAKEDNSPOOLMULTI._serialized_start=104
  _FAKEDNSPOOLMULTI._serialized_end=172
# @@protoc_insertion_point(module_scope)
