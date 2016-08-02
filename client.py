from grpc.beta import implementations

import ga4gh.read_service_pb2 as read_service_pb2
import ga4gh.reads_pb2 as reads_pb2

_TIMEOUT_SECONDS = 10


def run():
  channel = implementations.insecure_channel('localhost', 50051)
  stub = read_service_pb2.beta_create_ReadService_stub(channel)
  print stub.GetReadGroupSet(read_service_pb2.GetReadGroupSetRequest(read_group_set_id='echo'), _TIMEOUT_SECONDS)


if __name__ == '__main__':
  run()