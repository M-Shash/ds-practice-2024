# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Transaction_verification.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eTransaction_verification.proto\x12\x18transaction_verification\"D\n\x1eTransactionVerificationRequest\x12\x0e\n\x06\x63\x61rdID\x18\x01 \x01(\t\x12\x12\n\ncard_owner\x18\x02 \x01(\t\";\n\x1fTransactionVerificationResponse\x12\x18\n\x10validationResult\x18\x01 \x01(\x08\x32\xab\x01\n\x1eTransactionVerificationService\x12\x88\x01\n\x11VerifyTransaction\x12\x38.transaction_verification.TransactionVerificationRequest\x1a\x39.transaction_verification.TransactionVerificationResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Transaction_verification_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TRANSACTIONVERIFICATIONREQUEST']._serialized_start=60
  _globals['_TRANSACTIONVERIFICATIONREQUEST']._serialized_end=128
  _globals['_TRANSACTIONVERIFICATIONRESPONSE']._serialized_start=130
  _globals['_TRANSACTIONVERIFICATIONRESPONSE']._serialized_end=189
  _globals['_TRANSACTIONVERIFICATIONSERVICE']._serialized_start=192
  _globals['_TRANSACTIONVERIFICATIONSERVICE']._serialized_end=363
# @@protoc_insertion_point(module_scope)