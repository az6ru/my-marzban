# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/router/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xray_api.proto.common.net import port_pb2 as common_dot_net_dot_port__pb2
from xray_api.proto.common.net import network_pb2 as common_dot_net_dot_network__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x61pp/router/config.proto\x12\x0fxray.app.router\x1a\x15\x63ommon/net/port.proto\x1a\x18\x63ommon/net/network.proto\"\x81\x02\n\x06\x44omain\x12*\n\x04type\x18\x01 \x01(\x0e\x32\x1c.xray.app.router.Domain.Type\x12\r\n\x05value\x18\x02 \x01(\t\x12\x34\n\tattribute\x18\x03 \x03(\x0b\x32!.xray.app.router.Domain.Attribute\x1aR\n\tAttribute\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x14\n\nbool_value\x18\x02 \x01(\x08H\x00\x12\x13\n\tint_value\x18\x03 \x01(\x03H\x00\x42\r\n\x0btyped_value\"2\n\x04Type\x12\t\n\x05Plain\x10\x00\x12\t\n\x05Regex\x10\x01\x12\n\n\x06\x44omain\x10\x02\x12\x08\n\x04\x46ull\x10\x03\"\"\n\x04\x43IDR\x12\n\n\x02ip\x18\x01 \x01(\x0c\x12\x0e\n\x06prefix\x18\x02 \x01(\r\"Y\n\x05GeoIP\x12\x14\n\x0c\x63ountry_code\x18\x01 \x01(\t\x12#\n\x04\x63idr\x18\x02 \x03(\x0b\x32\x15.xray.app.router.CIDR\x12\x15\n\rreverse_match\x18\x03 \x01(\x08\"2\n\tGeoIPList\x12%\n\x05\x65ntry\x18\x01 \x03(\x0b\x32\x16.xray.app.router.GeoIP\"H\n\x07GeoSite\x12\x14\n\x0c\x63ountry_code\x18\x01 \x01(\t\x12\'\n\x06\x64omain\x18\x02 \x03(\x0b\x32\x17.xray.app.router.Domain\"6\n\x0bGeoSiteList\x12\'\n\x05\x65ntry\x18\x01 \x03(\x0b\x32\x18.xray.app.router.GeoSite\"\xfc\x04\n\x0bRoutingRule\x12\r\n\x03tag\x18\x01 \x01(\tH\x00\x12\x17\n\rbalancing_tag\x18\x0c \x01(\tH\x00\x12\'\n\x06\x64omain\x18\x02 \x03(\x0b\x32\x17.xray.app.router.Domain\x12\'\n\x04\x63idr\x18\x03 \x03(\x0b\x32\x15.xray.app.router.CIDRB\x02\x18\x01\x12%\n\x05geoip\x18\n \x03(\x0b\x32\x16.xray.app.router.GeoIP\x12\x32\n\nport_range\x18\x04 \x01(\x0b\x32\x1a.xray.common.net.PortRangeB\x02\x18\x01\x12,\n\tport_list\x18\x0e \x01(\x0b\x32\x19.xray.common.net.PortList\x12\x36\n\x0cnetwork_list\x18\x05 \x01(\x0b\x32\x1c.xray.common.net.NetworkListB\x02\x18\x01\x12*\n\x08networks\x18\r \x03(\x0e\x32\x18.xray.common.net.Network\x12.\n\x0bsource_cidr\x18\x06 \x03(\x0b\x32\x15.xray.app.router.CIDRB\x02\x18\x01\x12,\n\x0csource_geoip\x18\x0b \x03(\x0b\x32\x16.xray.app.router.GeoIP\x12\x33\n\x10source_port_list\x18\x10 \x01(\x0b\x32\x19.xray.common.net.PortList\x12\x12\n\nuser_email\x18\x07 \x03(\t\x12\x13\n\x0binbound_tag\x18\x08 \x03(\t\x12\x10\n\x08protocol\x18\t \x03(\t\x12\x12\n\nattributes\x18\x0f \x01(\t\x12\x16\n\x0e\x64omain_matcher\x18\x11 \x01(\tB\x0c\n\ntarget_tag\"I\n\rBalancingRule\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x19\n\x11outbound_selector\x18\x02 \x03(\t\x12\x10\n\x08strategy\x18\x03 \x01(\t\"\xf6\x01\n\x06\x43onfig\x12?\n\x0f\x64omain_strategy\x18\x01 \x01(\x0e\x32&.xray.app.router.Config.DomainStrategy\x12*\n\x04rule\x18\x02 \x03(\x0b\x32\x1c.xray.app.router.RoutingRule\x12\x36\n\x0e\x62\x61lancing_rule\x18\x03 \x03(\x0b\x32\x1e.xray.app.router.BalancingRule\"G\n\x0e\x44omainStrategy\x12\x08\n\x04\x41sIs\x10\x00\x12\t\n\x05UseIp\x10\x01\x12\x10\n\x0cIpIfNonMatch\x10\x02\x12\x0e\n\nIpOnDemand\x10\x03\x42O\n\x13\x63om.xray.app.routerP\x01Z$github.com/xtls/xray-core/app/router\xaa\x02\x0fXray.App.Routerb\x06proto3')



_DOMAIN = DESCRIPTOR.message_types_by_name['Domain']
_DOMAIN_ATTRIBUTE = _DOMAIN.nested_types_by_name['Attribute']
_CIDR = DESCRIPTOR.message_types_by_name['CIDR']
_GEOIP = DESCRIPTOR.message_types_by_name['GeoIP']
_GEOIPLIST = DESCRIPTOR.message_types_by_name['GeoIPList']
_GEOSITE = DESCRIPTOR.message_types_by_name['GeoSite']
_GEOSITELIST = DESCRIPTOR.message_types_by_name['GeoSiteList']
_ROUTINGRULE = DESCRIPTOR.message_types_by_name['RoutingRule']
_BALANCINGRULE = DESCRIPTOR.message_types_by_name['BalancingRule']
_CONFIG = DESCRIPTOR.message_types_by_name['Config']
_DOMAIN_TYPE = _DOMAIN.enum_types_by_name['Type']
_CONFIG_DOMAINSTRATEGY = _CONFIG.enum_types_by_name['DomainStrategy']
Domain = _reflection.GeneratedProtocolMessageType('Domain', (_message.Message,), {

  'Attribute' : _reflection.GeneratedProtocolMessageType('Attribute', (_message.Message,), {
    'DESCRIPTOR' : _DOMAIN_ATTRIBUTE,
    '__module__' : 'app.router.config_pb2'
    # @@protoc_insertion_point(class_scope:xray.app.router.Domain.Attribute)
    })
  ,
  'DESCRIPTOR' : _DOMAIN,
  '__module__' : 'app.router.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.router.Domain)
  })
_sym_db.RegisterMessage(Domain)
_sym_db.RegisterMessage(Domain.Attribute)

CIDR = _reflection.GeneratedProtocolMessageType('CIDR', (_message.Message,), {
  'DESCRIPTOR' : _CIDR,
  '__module__' : 'app.router.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.router.CIDR)
  })
_sym_db.RegisterMessage(CIDR)

GeoIP = _reflection.GeneratedProtocolMessageType('GeoIP', (_message.Message,), {
  'DESCRIPTOR' : _GEOIP,
  '__module__' : 'app.router.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.router.GeoIP)
  })
_sym_db.RegisterMessage(GeoIP)

GeoIPList = _reflection.GeneratedProtocolMessageType('GeoIPList', (_message.Message,), {
  'DESCRIPTOR' : _GEOIPLIST,
  '__module__' : 'app.router.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.router.GeoIPList)
  })
_sym_db.RegisterMessage(GeoIPList)

GeoSite = _reflection.GeneratedProtocolMessageType('GeoSite', (_message.Message,), {
  'DESCRIPTOR' : _GEOSITE,
  '__module__' : 'app.router.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.router.GeoSite)
  })
_sym_db.RegisterMessage(GeoSite)

GeoSiteList = _reflection.GeneratedProtocolMessageType('GeoSiteList', (_message.Message,), {
  'DESCRIPTOR' : _GEOSITELIST,
  '__module__' : 'app.router.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.router.GeoSiteList)
  })
_sym_db.RegisterMessage(GeoSiteList)

RoutingRule = _reflection.GeneratedProtocolMessageType('RoutingRule', (_message.Message,), {
  'DESCRIPTOR' : _ROUTINGRULE,
  '__module__' : 'app.router.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.router.RoutingRule)
  })
_sym_db.RegisterMessage(RoutingRule)

BalancingRule = _reflection.GeneratedProtocolMessageType('BalancingRule', (_message.Message,), {
  'DESCRIPTOR' : _BALANCINGRULE,
  '__module__' : 'app.router.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.router.BalancingRule)
  })
_sym_db.RegisterMessage(BalancingRule)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'app.router.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.router.Config)
  })
_sym_db.RegisterMessage(Config)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.xray.app.routerP\001Z$github.com/xtls/xray-core/app/router\252\002\017Xray.App.Router'
  _ROUTINGRULE.fields_by_name['cidr']._options = None
  _ROUTINGRULE.fields_by_name['cidr']._serialized_options = b'\030\001'
  _ROUTINGRULE.fields_by_name['port_range']._options = None
  _ROUTINGRULE.fields_by_name['port_range']._serialized_options = b'\030\001'
  _ROUTINGRULE.fields_by_name['network_list']._options = None
  _ROUTINGRULE.fields_by_name['network_list']._serialized_options = b'\030\001'
  _ROUTINGRULE.fields_by_name['source_cidr']._options = None
  _ROUTINGRULE.fields_by_name['source_cidr']._serialized_options = b'\030\001'
  _DOMAIN._serialized_start=94
  _DOMAIN._serialized_end=351
  _DOMAIN_ATTRIBUTE._serialized_start=217
  _DOMAIN_ATTRIBUTE._serialized_end=299
  _DOMAIN_TYPE._serialized_start=301
  _DOMAIN_TYPE._serialized_end=351
  _CIDR._serialized_start=353
  _CIDR._serialized_end=387
  _GEOIP._serialized_start=389
  _GEOIP._serialized_end=478
  _GEOIPLIST._serialized_start=480
  _GEOIPLIST._serialized_end=530
  _GEOSITE._serialized_start=532
  _GEOSITE._serialized_end=604
  _GEOSITELIST._serialized_start=606
  _GEOSITELIST._serialized_end=660
  _ROUTINGRULE._serialized_start=663
  _ROUTINGRULE._serialized_end=1299
  _BALANCINGRULE._serialized_start=1301
  _BALANCINGRULE._serialized_end=1374
  _CONFIG._serialized_start=1377
  _CONFIG._serialized_end=1623
  _CONFIG_DOMAINSTRATEGY._serialized_start=1552
  _CONFIG_DOMAINSTRATEGY._serialized_end=1623
# @@protoc_insertion_point(module_scope)
