import time

import read_service_pb2
import reads_pb2


class Server(read_service_pb2.BetaReadServiceServicer):

  def SearchReadGroupSets(self, request, context):
    print(read_service_pb2.SearchReadGroupSetsResponse)
    return read_service_pb2.SearchReadGroupSetsResponse

  def GetReadGroupSet(self, request, context):
    print(request)

    return reads_pb2.ReadGroupSet(id=request.read_group_set_id)

  def SearchReads(self, request, context):
    return True


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