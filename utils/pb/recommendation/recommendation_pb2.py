# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: recommendation.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14recommendation.proto\x12\x0erecommendation\";\n\x15RecommendationRequest\x12\x10\n\x08userName\x18\x01 \x01(\t\x12\x10\n\x08itemName\x18\x02 \x01(\t\"U\n\x16RecommendationResponse\x12;\n\x0frecommendations\x18\x01 \x03(\x0b\x32\".recommendation.RecommendationItem\"6\n\x12RecommendationItem\x12\x0e\n\x06itemId\x18\x01 \x01(\t\x12\x10\n\x08itemName\x18\x02 \x01(\t2|\n\x15RecommendationService\x12\x63\n\x12GetRecommendations\x12%.recommendation.RecommendationRequest\x1a&.recommendation.RecommendationResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'recommendation_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_RECOMMENDATIONREQUEST']._serialized_start=40
  _globals['_RECOMMENDATIONREQUEST']._serialized_end=99
  _globals['_RECOMMENDATIONRESPONSE']._serialized_start=101
  _globals['_RECOMMENDATIONRESPONSE']._serialized_end=186
  _globals['_RECOMMENDATIONITEM']._serialized_start=188
  _globals['_RECOMMENDATIONITEM']._serialized_end=242
  _globals['_RECOMMENDATIONSERVICE']._serialized_start=244
  _globals['_RECOMMENDATIONSERVICE']._serialized_end=368
# @@protoc_insertion_point(module_scope)
