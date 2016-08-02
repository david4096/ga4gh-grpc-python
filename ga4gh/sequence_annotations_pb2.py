# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ga4gh/sequence_annotations.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ga4gh import common_pb2 as ga4gh_dot_common__pb2
from ga4gh import metadata_pb2 as ga4gh_dot_metadata__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ga4gh/sequence_annotations.proto',
  package='ga4gh',
  syntax='proto3',
  serialized_pb=_b('\n ga4gh/sequence_annotations.proto\x12\x05ga4gh\x1a\x12ga4gh/common.proto\x1a\x14ga4gh/metadata.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xee\x02\n\nAttributes\x12)\n\x04vals\x18\x01 \x03(\x0b\x32\x1b.ga4gh.Attributes.ValsEntry\x1a\x99\x01\n\x0e\x41ttributeValue\x12\x16\n\x0cstring_value\x18\x01 \x01(\tH\x00\x12\x38\n\x13\x65xternal_identifier\x18\x02 \x01(\x0b\x32\x19.ga4gh.ExternalIdentifierH\x00\x12,\n\rontology_term\x18\x03 \x01(\x0b\x32\x13.ga4gh.OntologyTermH\x00\x42\x07\n\x05value\x1a\x46\n\x12\x41ttributeValueList\x12\x30\n\x06values\x18\x01 \x03(\x0b\x32 .ga4gh.Attributes.AttributeValue\x1aQ\n\tValsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.ga4gh.Attributes.AttributeValueList:\x02\x38\x01\"\x9b\x02\n\x07\x46\x65\x61ture\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bgene_symbol\x18\x03 \x01(\t\x12\x11\n\tparent_id\x18\x04 \x01(\t\x12\x11\n\tchild_ids\x18\x05 \x03(\t\x12\x16\n\x0e\x66\x65\x61ture_set_id\x18\x06 \x01(\t\x12\x16\n\x0ereference_name\x18\x07 \x01(\t\x12\r\n\x05start\x18\x08 \x01(\x03\x12\x0b\n\x03\x65nd\x18\t \x01(\x03\x12\x1d\n\x06strand\x18\n \x01(\x0e\x32\r.ga4gh.Strand\x12)\n\x0c\x66\x65\x61ture_type\x18\x0b \x01(\x0b\x32\x13.ga4gh.OntologyTerm\x12%\n\nattributes\x18\x0c \x01(\x0b\x32\x11.ga4gh.Attributes\"\xdc\x01\n\nFeatureSet\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\x18\n\x10reference_set_id\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x12\n\nsource_uri\x18\x05 \x01(\t\x12)\n\x04info\x18\x06 \x03(\x0b\x32\x1b.ga4gh.FeatureSet.InfoEntry\x1aG\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.ListValue:\x02\x38\x01\x62\x06proto3')
  ,
  dependencies=[ga4gh_dot_common__pb2.DESCRIPTOR,ga4gh_dot_metadata__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ATTRIBUTES_ATTRIBUTEVALUE = _descriptor.Descriptor(
  name='AttributeValue',
  full_name='ga4gh.Attributes.AttributeValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='string_value', full_name='ga4gh.Attributes.AttributeValue.string_value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='external_identifier', full_name='ga4gh.Attributes.AttributeValue.external_identifier', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ontology_term', full_name='ga4gh.Attributes.AttributeValue.ontology_term', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='value', full_name='ga4gh.Attributes.AttributeValue.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=174,
  serialized_end=327,
)

_ATTRIBUTES_ATTRIBUTEVALUELIST = _descriptor.Descriptor(
  name='AttributeValueList',
  full_name='ga4gh.Attributes.AttributeValueList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='ga4gh.Attributes.AttributeValueList.values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=329,
  serialized_end=399,
)

_ATTRIBUTES_VALSENTRY = _descriptor.Descriptor(
  name='ValsEntry',
  full_name='ga4gh.Attributes.ValsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ga4gh.Attributes.ValsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='ga4gh.Attributes.ValsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=401,
  serialized_end=482,
)

_ATTRIBUTES = _descriptor.Descriptor(
  name='Attributes',
  full_name='ga4gh.Attributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vals', full_name='ga4gh.Attributes.vals', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ATTRIBUTES_ATTRIBUTEVALUE, _ATTRIBUTES_ATTRIBUTEVALUELIST, _ATTRIBUTES_VALSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=482,
)


_FEATURE = _descriptor.Descriptor(
  name='Feature',
  full_name='ga4gh.Feature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.Feature.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.Feature.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gene_symbol', full_name='ga4gh.Feature.gene_symbol', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_id', full_name='ga4gh.Feature.parent_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='child_ids', full_name='ga4gh.Feature.child_ids', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_set_id', full_name='ga4gh.Feature.feature_set_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_name', full_name='ga4gh.Feature.reference_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='ga4gh.Feature.start', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='ga4gh.Feature.end', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='strand', full_name='ga4gh.Feature.strand', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_type', full_name='ga4gh.Feature.feature_type', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='ga4gh.Feature.attributes', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=485,
  serialized_end=768,
)


_FEATURESET_INFOENTRY = _descriptor.Descriptor(
  name='InfoEntry',
  full_name='ga4gh.FeatureSet.InfoEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ga4gh.FeatureSet.InfoEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='ga4gh.FeatureSet.InfoEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=920,
  serialized_end=991,
)

_FEATURESET = _descriptor.Descriptor(
  name='FeatureSet',
  full_name='ga4gh.FeatureSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.FeatureSet.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='ga4gh.FeatureSet.dataset_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_set_id', full_name='ga4gh.FeatureSet.reference_set_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.FeatureSet.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_uri', full_name='ga4gh.FeatureSet.source_uri', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='ga4gh.FeatureSet.info', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_FEATURESET_INFOENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=771,
  serialized_end=991,
)

_ATTRIBUTES_ATTRIBUTEVALUE.fields_by_name['external_identifier'].message_type = ga4gh_dot_common__pb2._EXTERNALIDENTIFIER
_ATTRIBUTES_ATTRIBUTEVALUE.fields_by_name['ontology_term'].message_type = ga4gh_dot_metadata__pb2._ONTOLOGYTERM
_ATTRIBUTES_ATTRIBUTEVALUE.containing_type = _ATTRIBUTES
_ATTRIBUTES_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTES_ATTRIBUTEVALUE.fields_by_name['string_value'])
_ATTRIBUTES_ATTRIBUTEVALUE.fields_by_name['string_value'].containing_oneof = _ATTRIBUTES_ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTES_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTES_ATTRIBUTEVALUE.fields_by_name['external_identifier'])
_ATTRIBUTES_ATTRIBUTEVALUE.fields_by_name['external_identifier'].containing_oneof = _ATTRIBUTES_ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTES_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTES_ATTRIBUTEVALUE.fields_by_name['ontology_term'])
_ATTRIBUTES_ATTRIBUTEVALUE.fields_by_name['ontology_term'].containing_oneof = _ATTRIBUTES_ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTES_ATTRIBUTEVALUELIST.fields_by_name['values'].message_type = _ATTRIBUTES_ATTRIBUTEVALUE
_ATTRIBUTES_ATTRIBUTEVALUELIST.containing_type = _ATTRIBUTES
_ATTRIBUTES_VALSENTRY.fields_by_name['value'].message_type = _ATTRIBUTES_ATTRIBUTEVALUELIST
_ATTRIBUTES_VALSENTRY.containing_type = _ATTRIBUTES
_ATTRIBUTES.fields_by_name['vals'].message_type = _ATTRIBUTES_VALSENTRY
_FEATURE.fields_by_name['strand'].enum_type = ga4gh_dot_common__pb2._STRAND
_FEATURE.fields_by_name['feature_type'].message_type = ga4gh_dot_metadata__pb2._ONTOLOGYTERM
_FEATURE.fields_by_name['attributes'].message_type = _ATTRIBUTES
_FEATURESET_INFOENTRY.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._LISTVALUE
_FEATURESET_INFOENTRY.containing_type = _FEATURESET
_FEATURESET.fields_by_name['info'].message_type = _FEATURESET_INFOENTRY
DESCRIPTOR.message_types_by_name['Attributes'] = _ATTRIBUTES
DESCRIPTOR.message_types_by_name['Feature'] = _FEATURE
DESCRIPTOR.message_types_by_name['FeatureSet'] = _FEATURESET

Attributes = _reflection.GeneratedProtocolMessageType('Attributes', (_message.Message,), dict(

  AttributeValue = _reflection.GeneratedProtocolMessageType('AttributeValue', (_message.Message,), dict(
    DESCRIPTOR = _ATTRIBUTES_ATTRIBUTEVALUE,
    __module__ = 'ga4gh.sequence_annotations_pb2'
    # @@protoc_insertion_point(class_scope:ga4gh.Attributes.AttributeValue)
    ))
  ,

  AttributeValueList = _reflection.GeneratedProtocolMessageType('AttributeValueList', (_message.Message,), dict(
    DESCRIPTOR = _ATTRIBUTES_ATTRIBUTEVALUELIST,
    __module__ = 'ga4gh.sequence_annotations_pb2'
    # @@protoc_insertion_point(class_scope:ga4gh.Attributes.AttributeValueList)
    ))
  ,

  ValsEntry = _reflection.GeneratedProtocolMessageType('ValsEntry', (_message.Message,), dict(
    DESCRIPTOR = _ATTRIBUTES_VALSENTRY,
    __module__ = 'ga4gh.sequence_annotations_pb2'
    # @@protoc_insertion_point(class_scope:ga4gh.Attributes.ValsEntry)
    ))
  ,
  DESCRIPTOR = _ATTRIBUTES,
  __module__ = 'ga4gh.sequence_annotations_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.Attributes)
  ))
_sym_db.RegisterMessage(Attributes)
_sym_db.RegisterMessage(Attributes.AttributeValue)
_sym_db.RegisterMessage(Attributes.AttributeValueList)
_sym_db.RegisterMessage(Attributes.ValsEntry)

Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), dict(
  DESCRIPTOR = _FEATURE,
  __module__ = 'ga4gh.sequence_annotations_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.Feature)
  ))
_sym_db.RegisterMessage(Feature)

FeatureSet = _reflection.GeneratedProtocolMessageType('FeatureSet', (_message.Message,), dict(

  InfoEntry = _reflection.GeneratedProtocolMessageType('InfoEntry', (_message.Message,), dict(
    DESCRIPTOR = _FEATURESET_INFOENTRY,
    __module__ = 'ga4gh.sequence_annotations_pb2'
    # @@protoc_insertion_point(class_scope:ga4gh.FeatureSet.InfoEntry)
    ))
  ,
  DESCRIPTOR = _FEATURESET,
  __module__ = 'ga4gh.sequence_annotations_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.FeatureSet)
  ))
_sym_db.RegisterMessage(FeatureSet)
_sym_db.RegisterMessage(FeatureSet.InfoEntry)


_ATTRIBUTES_VALSENTRY.has_options = True
_ATTRIBUTES_VALSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_FEATURESET_INFOENTRY.has_options = True
_FEATURESET_INFOENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
import abc
import six
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
