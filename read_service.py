import time

import ga4gh.read_service_pb2 as read_service_pb2
import ga4gh.reads_pb2 as reads_pb2

class ReadService(read_service_pb2.BetaReadServiceServicer):

  def SearchReadGroupSets(self, request, context):
    return read_service_pb2.SearchReadGroupSetsResponse()

  def GetReadGroupSet(self, request, context):
    return reads_pb2.ReadGroupSet(id=request.read_group_set_id)

  def SearchReads(self, request, context):
    return read_service_pb2.SearchReadsResponse()

def serve():
  server = read_service_pb2.beta_create_ReadService_server(ReadService())
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(203948)
  except KeyboardInterrupt:
    server.stop()

if __name__ == '__main__':
  serve()