import time

import ga4gh.metadata_service_pb2 as metadata_service_pb2
import ga4gh.metadata_pb2 as metadata_pb2

class MetadataService(metadata_service_pb2.BetaMetadataServiceServicer):

  def SearchDatasets(self, request, context):
    return metadata_service_pb2.SearchDatasetsResponse()

  def GetDataset(self, request, context):
    return metadata_pb2.Dataset()

def serve():
  server = metadata_service_pb2.beta_create_MetadataService_server(MetadataService())
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(203948)
  except KeyboardInterrupt:
    server.stop()

if __name__ == '__main__':
  serve()