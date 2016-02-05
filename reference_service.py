import time

import schemas.reference_service_pb2 as reference_service_pb2
import schemas.references_pb2 as references_pb2

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

def serve():
  server = reference_service_pb2.beta_create_ReferenceService_server(ReferenceService())
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(203948)
  except KeyboardInterrupt:
    server.stop()

if __name__ == '__main__':
  serve()