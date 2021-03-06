# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ga4gh/reference_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ga4gh import references_pb2 as ga4gh_dot_references__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ga4gh/reference_service.proto',
  package='ga4gh',
  syntax='proto3',
  serialized_pb=_b('\n\x1dga4gh/reference_service.proto\x12\x05ga4gh\x1a\x16ga4gh/references.proto\"\x80\x01\n\x1aSearchReferenceSetsRequest\x12\x13\n\x0bmd5checksum\x18\x01 \x01(\t\x12\x11\n\taccession\x18\x02 \x01(\t\x12\x13\n\x0b\x61ssembly_id\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t\"c\n\x1bSearchReferenceSetsResponse\x12+\n\x0ereference_sets\x18\x01 \x03(\x0b\x32\x13.ga4gh.ReferenceSet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"2\n\x16GetReferenceSetRequest\x12\x18\n\x10reference_set_id\x18\x01 \x01(\t\"\x82\x01\n\x17SearchReferencesRequest\x12\x18\n\x10reference_set_id\x18\x01 \x01(\t\x12\x13\n\x0bmd5checksum\x18\x02 \x01(\t\x12\x11\n\taccession\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t\"Y\n\x18SearchReferencesResponse\x12$\n\nreferences\x18\x01 \x03(\x0b\x32\x10.ga4gh.Reference\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"+\n\x13GetReferenceRequest\x12\x14\n\x0creference_id\x18\x01 \x01(\t\"a\n\x19ListReferenceBasesRequest\x12\x14\n\x0creference_id\x18\x01 \x01(\t\x12\r\n\x05start\x18\x02 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x03 \x01(\x03\x12\x12\n\npage_token\x18\x04 \x01(\t\"W\n\x1aListReferenceBasesResponse\x12\x0e\n\x06offset\x18\x01 \x01(\x03\x12\x10\n\x08sequence\x18\x02 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t2\xa5\x03\n\x10ReferenceService\x12\\\n\x13SearchReferenceSets\x12!.ga4gh.SearchReferenceSetsRequest\x1a\".ga4gh.SearchReferenceSetsResponse\x12\x45\n\x0fGetReferenceSet\x12\x1d.ga4gh.GetReferenceSetRequest\x1a\x13.ga4gh.ReferenceSet\x12S\n\x10SearchReferences\x12\x1e.ga4gh.SearchReferencesRequest\x1a\x1f.ga4gh.SearchReferencesResponse\x12<\n\x0cGetReference\x12\x1a.ga4gh.GetReferenceRequest\x1a\x10.ga4gh.Reference\x12Y\n\x12ListReferenceBases\x12 .ga4gh.ListReferenceBasesRequest\x1a!.ga4gh.ListReferenceBasesResponseb\x06proto3')
  ,
  dependencies=[ga4gh_dot_references__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SEARCHREFERENCESETSREQUEST = _descriptor.Descriptor(
  name='SearchReferenceSetsRequest',
  full_name='ga4gh.SearchReferenceSetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='md5checksum', full_name='ga4gh.SearchReferenceSetsRequest.md5checksum', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accession', full_name='ga4gh.SearchReferenceSetsRequest.accession', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='assembly_id', full_name='ga4gh.SearchReferenceSetsRequest.assembly_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.SearchReferenceSetsRequest.page_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.SearchReferenceSetsRequest.page_token', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=65,
  serialized_end=193,
)


_SEARCHREFERENCESETSRESPONSE = _descriptor.Descriptor(
  name='SearchReferenceSetsResponse',
  full_name='ga4gh.SearchReferenceSetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reference_sets', full_name='ga4gh.SearchReferenceSetsResponse.reference_sets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.SearchReferenceSetsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=195,
  serialized_end=294,
)


_GETREFERENCESETREQUEST = _descriptor.Descriptor(
  name='GetReferenceSetRequest',
  full_name='ga4gh.GetReferenceSetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reference_set_id', full_name='ga4gh.GetReferenceSetRequest.reference_set_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=296,
  serialized_end=346,
)


_SEARCHREFERENCESREQUEST = _descriptor.Descriptor(
  name='SearchReferencesRequest',
  full_name='ga4gh.SearchReferencesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reference_set_id', full_name='ga4gh.SearchReferencesRequest.reference_set_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='md5checksum', full_name='ga4gh.SearchReferencesRequest.md5checksum', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accession', full_name='ga4gh.SearchReferencesRequest.accession', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.SearchReferencesRequest.page_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.SearchReferencesRequest.page_token', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=349,
  serialized_end=479,
)


_SEARCHREFERENCESRESPONSE = _descriptor.Descriptor(
  name='SearchReferencesResponse',
  full_name='ga4gh.SearchReferencesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='references', full_name='ga4gh.SearchReferencesResponse.references', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.SearchReferencesResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=481,
  serialized_end=570,
)


_GETREFERENCEREQUEST = _descriptor.Descriptor(
  name='GetReferenceRequest',
  full_name='ga4gh.GetReferenceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reference_id', full_name='ga4gh.GetReferenceRequest.reference_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=572,
  serialized_end=615,
)


_LISTREFERENCEBASESREQUEST = _descriptor.Descriptor(
  name='ListReferenceBasesRequest',
  full_name='ga4gh.ListReferenceBasesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reference_id', full_name='ga4gh.ListReferenceBasesRequest.reference_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='ga4gh.ListReferenceBasesRequest.start', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='ga4gh.ListReferenceBasesRequest.end', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.ListReferenceBasesRequest.page_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=617,
  serialized_end=714,
)


_LISTREFERENCEBASESRESPONSE = _descriptor.Descriptor(
  name='ListReferenceBasesResponse',
  full_name='ga4gh.ListReferenceBasesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='offset', full_name='ga4gh.ListReferenceBasesResponse.offset', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sequence', full_name='ga4gh.ListReferenceBasesResponse.sequence', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.ListReferenceBasesResponse.next_page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=716,
  serialized_end=803,
)

_SEARCHREFERENCESETSRESPONSE.fields_by_name['reference_sets'].message_type = ga4gh_dot_references__pb2._REFERENCESET
_SEARCHREFERENCESRESPONSE.fields_by_name['references'].message_type = ga4gh_dot_references__pb2._REFERENCE
DESCRIPTOR.message_types_by_name['SearchReferenceSetsRequest'] = _SEARCHREFERENCESETSREQUEST
DESCRIPTOR.message_types_by_name['SearchReferenceSetsResponse'] = _SEARCHREFERENCESETSRESPONSE
DESCRIPTOR.message_types_by_name['GetReferenceSetRequest'] = _GETREFERENCESETREQUEST
DESCRIPTOR.message_types_by_name['SearchReferencesRequest'] = _SEARCHREFERENCESREQUEST
DESCRIPTOR.message_types_by_name['SearchReferencesResponse'] = _SEARCHREFERENCESRESPONSE
DESCRIPTOR.message_types_by_name['GetReferenceRequest'] = _GETREFERENCEREQUEST
DESCRIPTOR.message_types_by_name['ListReferenceBasesRequest'] = _LISTREFERENCEBASESREQUEST
DESCRIPTOR.message_types_by_name['ListReferenceBasesResponse'] = _LISTREFERENCEBASESRESPONSE

SearchReferenceSetsRequest = _reflection.GeneratedProtocolMessageType('SearchReferenceSetsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHREFERENCESETSREQUEST,
  __module__ = 'ga4gh.reference_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchReferenceSetsRequest)
  ))
_sym_db.RegisterMessage(SearchReferenceSetsRequest)

SearchReferenceSetsResponse = _reflection.GeneratedProtocolMessageType('SearchReferenceSetsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHREFERENCESETSRESPONSE,
  __module__ = 'ga4gh.reference_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchReferenceSetsResponse)
  ))
_sym_db.RegisterMessage(SearchReferenceSetsResponse)

GetReferenceSetRequest = _reflection.GeneratedProtocolMessageType('GetReferenceSetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETREFERENCESETREQUEST,
  __module__ = 'ga4gh.reference_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.GetReferenceSetRequest)
  ))
_sym_db.RegisterMessage(GetReferenceSetRequest)

SearchReferencesRequest = _reflection.GeneratedProtocolMessageType('SearchReferencesRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHREFERENCESREQUEST,
  __module__ = 'ga4gh.reference_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchReferencesRequest)
  ))
_sym_db.RegisterMessage(SearchReferencesRequest)

SearchReferencesResponse = _reflection.GeneratedProtocolMessageType('SearchReferencesResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHREFERENCESRESPONSE,
  __module__ = 'ga4gh.reference_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchReferencesResponse)
  ))
_sym_db.RegisterMessage(SearchReferencesResponse)

GetReferenceRequest = _reflection.GeneratedProtocolMessageType('GetReferenceRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETREFERENCEREQUEST,
  __module__ = 'ga4gh.reference_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.GetReferenceRequest)
  ))
_sym_db.RegisterMessage(GetReferenceRequest)

ListReferenceBasesRequest = _reflection.GeneratedProtocolMessageType('ListReferenceBasesRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTREFERENCEBASESREQUEST,
  __module__ = 'ga4gh.reference_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.ListReferenceBasesRequest)
  ))
_sym_db.RegisterMessage(ListReferenceBasesRequest)

ListReferenceBasesResponse = _reflection.GeneratedProtocolMessageType('ListReferenceBasesResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTREFERENCEBASESRESPONSE,
  __module__ = 'ga4gh.reference_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.ListReferenceBasesResponse)
  ))
_sym_db.RegisterMessage(ListReferenceBasesResponse)


import abc
import six
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

class BetaReferenceServiceServicer(object):
  def SearchReferenceSets(self, request, context):
    """Gets a list of `ReferenceSet` matching the search criteria.

    `POST /referencesets/search` must accept a JSON version of
    `SearchReferenceSetsRequest` as the post body and will return a JSON
    version of `SearchReferenceSetsResponse`.
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def GetReferenceSet(self, request, context):
    """Gets a `ReferenceSet` by ID.

    `GET /referencesets/{reference_set_id}` will return a JSON version of
    `ReferenceSet`.
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def SearchReferences(self, request, context):
    """Gets a list of `Reference` matching the search criteria.

    `POST /references/search` must accept a JSON version of
    `SearchReferencesRequest` as the post body and will return a JSON
    version of `SearchReferencesResponse`.
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def GetReference(self, request, context):
    """Gets a `Reference` by ID.

    `GET /references/{reference_id}` will return a JSON version of
    `Reference`.
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def ListReferenceBases(self, request, context):
    """Lists `Reference` bases by ID and optional range.

    `GET /references/{id}/bases` will return a JSON version of
    `ListReferenceBasesResponse`.
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)

class BetaReferenceServiceStub(object):
  def SearchReferenceSets(self, request, timeout):
    """Gets a list of `ReferenceSet` matching the search criteria.

    `POST /referencesets/search` must accept a JSON version of
    `SearchReferenceSetsRequest` as the post body and will return a JSON
    version of `SearchReferenceSetsResponse`.
    """
    raise NotImplementedError()
  SearchReferenceSets.future = None
  def GetReferenceSet(self, request, timeout):
    """Gets a `ReferenceSet` by ID.

    `GET /referencesets/{reference_set_id}` will return a JSON version of
    `ReferenceSet`.
    """
    raise NotImplementedError()
  GetReferenceSet.future = None
  def SearchReferences(self, request, timeout):
    """Gets a list of `Reference` matching the search criteria.

    `POST /references/search` must accept a JSON version of
    `SearchReferencesRequest` as the post body and will return a JSON
    version of `SearchReferencesResponse`.
    """
    raise NotImplementedError()
  SearchReferences.future = None
  def GetReference(self, request, timeout):
    """Gets a `Reference` by ID.

    `GET /references/{reference_id}` will return a JSON version of
    `Reference`.
    """
    raise NotImplementedError()
  GetReference.future = None
  def ListReferenceBases(self, request, timeout):
    """Lists `Reference` bases by ID and optional range.

    `GET /references/{id}/bases` will return a JSON version of
    `ListReferenceBasesResponse`.
    """
    raise NotImplementedError()
  ListReferenceBases.future = None

def beta_create_ReferenceService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  import ga4gh.reference_service_pb2
  import ga4gh.reference_service_pb2
  import ga4gh.reference_service_pb2
  import ga4gh.references_pb2
  import ga4gh.reference_service_pb2
  import ga4gh.reference_service_pb2
  import ga4gh.reference_service_pb2
  import ga4gh.references_pb2
  import ga4gh.reference_service_pb2
  import ga4gh.reference_service_pb2
  request_deserializers = {
    ('ga4gh.ReferenceService', 'GetReference'): ga4gh.reference_service_pb2.GetReferenceRequest.FromString,
    ('ga4gh.ReferenceService', 'GetReferenceSet'): ga4gh.reference_service_pb2.GetReferenceSetRequest.FromString,
    ('ga4gh.ReferenceService', 'ListReferenceBases'): ga4gh.reference_service_pb2.ListReferenceBasesRequest.FromString,
    ('ga4gh.ReferenceService', 'SearchReferenceSets'): ga4gh.reference_service_pb2.SearchReferenceSetsRequest.FromString,
    ('ga4gh.ReferenceService', 'SearchReferences'): ga4gh.reference_service_pb2.SearchReferencesRequest.FromString,
  }
  response_serializers = {
    ('ga4gh.ReferenceService', 'GetReference'): ga4gh.references_pb2.Reference.SerializeToString,
    ('ga4gh.ReferenceService', 'GetReferenceSet'): ga4gh.references_pb2.ReferenceSet.SerializeToString,
    ('ga4gh.ReferenceService', 'ListReferenceBases'): ga4gh.reference_service_pb2.ListReferenceBasesResponse.SerializeToString,
    ('ga4gh.ReferenceService', 'SearchReferenceSets'): ga4gh.reference_service_pb2.SearchReferenceSetsResponse.SerializeToString,
    ('ga4gh.ReferenceService', 'SearchReferences'): ga4gh.reference_service_pb2.SearchReferencesResponse.SerializeToString,
  }
  method_implementations = {
    ('ga4gh.ReferenceService', 'GetReference'): face_utilities.unary_unary_inline(servicer.GetReference),
    ('ga4gh.ReferenceService', 'GetReferenceSet'): face_utilities.unary_unary_inline(servicer.GetReferenceSet),
    ('ga4gh.ReferenceService', 'ListReferenceBases'): face_utilities.unary_unary_inline(servicer.ListReferenceBases),
    ('ga4gh.ReferenceService', 'SearchReferenceSets'): face_utilities.unary_unary_inline(servicer.SearchReferenceSets),
    ('ga4gh.ReferenceService', 'SearchReferences'): face_utilities.unary_unary_inline(servicer.SearchReferences),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)

def beta_create_ReferenceService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  import ga4gh.reference_service_pb2
  import ga4gh.reference_service_pb2
  import ga4gh.reference_service_pb2
  import ga4gh.references_pb2
  import ga4gh.reference_service_pb2
  import ga4gh.reference_service_pb2
  import ga4gh.reference_service_pb2
  import ga4gh.references_pb2
  import ga4gh.reference_service_pb2
  import ga4gh.reference_service_pb2
  request_serializers = {
    ('ga4gh.ReferenceService', 'GetReference'): ga4gh.reference_service_pb2.GetReferenceRequest.SerializeToString,
    ('ga4gh.ReferenceService', 'GetReferenceSet'): ga4gh.reference_service_pb2.GetReferenceSetRequest.SerializeToString,
    ('ga4gh.ReferenceService', 'ListReferenceBases'): ga4gh.reference_service_pb2.ListReferenceBasesRequest.SerializeToString,
    ('ga4gh.ReferenceService', 'SearchReferenceSets'): ga4gh.reference_service_pb2.SearchReferenceSetsRequest.SerializeToString,
    ('ga4gh.ReferenceService', 'SearchReferences'): ga4gh.reference_service_pb2.SearchReferencesRequest.SerializeToString,
  }
  response_deserializers = {
    ('ga4gh.ReferenceService', 'GetReference'): ga4gh.references_pb2.Reference.FromString,
    ('ga4gh.ReferenceService', 'GetReferenceSet'): ga4gh.references_pb2.ReferenceSet.FromString,
    ('ga4gh.ReferenceService', 'ListReferenceBases'): ga4gh.reference_service_pb2.ListReferenceBasesResponse.FromString,
    ('ga4gh.ReferenceService', 'SearchReferenceSets'): ga4gh.reference_service_pb2.SearchReferenceSetsResponse.FromString,
    ('ga4gh.ReferenceService', 'SearchReferences'): ga4gh.reference_service_pb2.SearchReferencesResponse.FromString,
  }
  cardinalities = {
    'GetReference': cardinality.Cardinality.UNARY_UNARY,
    'GetReferenceSet': cardinality.Cardinality.UNARY_UNARY,
    'ListReferenceBases': cardinality.Cardinality.UNARY_UNARY,
    'SearchReferenceSets': cardinality.Cardinality.UNARY_UNARY,
    'SearchReferences': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'ga4gh.ReferenceService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
