import time

import read_service_pb2
import reads_pb2

class ReadService(read_service_pb2.BetaReadServiceServicer):

  def SearchReadGroupSets(self, request, context):
    return read_service_pb2.SearchReadGroupSetsResponse()

  def GetReadGroupSet(self, request, context):
    return reads_pb2.ReadGroupSet(id=request.read_group_set_id)

  def SearchReads(self, request, context):
    return read_service_pb2.SearchReadsResponse()


import variant_service_pb2
import variants_pb2

class VariantService(variant_service_pb2.BetaVariantServiceServicer):

  def SearchVariantSets(self, request, context):
    return variant_service_pb2.SearchVariantSetsResponse()

  def SearchCallSets(self, request, context):
    return variant_service_pb2.SearchCallSetsResponse()

  def SearchVariants(self, request, context):
    return variant_service_pb2.SearchVariantsResponse()

  def GetCallSet(self, request, context):
    return variants_pb2.CallSet()

  def GetVariant(self, request, context):
    return variants_pb2.Variant()

  def GetVariantSet(self, request, context):
    return variants_pb2.VariantSet()


import metadata_service_pb2
import metadata_pb2

class MetadataService(metadata_service_pb2.BetaMetadataServiceServicer):

  def SearchDatasets(self, request, context):
    return metadata_service_pb2.SearchDatasetsResponse()

  def GetDataset(self, request, context):
    return metadata_pb2.Dataset()


import reference_service_pb2
import references_pb2

class ReferenceService(reference_service_pb2.BetaReferenceServiceServicer):

  def SearchReferences(self, request, context):
    return reference_service_pb2.SearchReferencesResponse()

  def SearchReferenceSets(self, request, context):
    return reference_service_pb2.SearchReferenceSetsResponse()

  def GetReferenceSet(self, request, context):
    return references_pb2.ReferenceSet()

  def GetReference(self, request, context):
    return references_pb2.Reference()

  def ListReferenceBases(self, request, context):
    return reference_service_pb2.ListReferenceBasesResponse()


class Server(VariantService, ReadService, MetadataService, ReferenceService):
  def __init__(self):
    return None

def serve():
  server = read_service_pb2.beta_create_ReadService_server(Server())
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(203948)
  except KeyboardInterrupt:
    server.stop()

if __name__ == '__main__':
  serve()