# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: bakery.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC, 5, 27, 2, "", "bakery.proto"
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0c\x62\x61kery.proto\x12\x06\x62\x61kery"\x1d\n\x0cOrderRequest\x12\r\n\x05order\x18\x01 \x01(\t"%\n\rOrderResponse\x12\x14\n\x0corder_status\x18\x01 \x01(\t2C\n\x06\x42\x61kery\x12\x39\n\x08GetOrder\x12\x14.bakery.OrderRequest\x1a\x15.bakery.OrderResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "bakery_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals["_ORDERREQUEST"]._serialized_start = 24
    _globals["_ORDERREQUEST"]._serialized_end = 53
    _globals["_ORDERRESPONSE"]._serialized_start = 55
    _globals["_ORDERRESPONSE"]._serialized_end = 92
    _globals["_BAKERY"]._serialized_start = 94
    _globals["_BAKERY"]._serialized_end = 161
# @@protoc_insertion_point(module_scope)