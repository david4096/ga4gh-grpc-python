from grpc.beta import implementations

import read_service_pb2
import reads_pb2

_TIMEOUT_SECONDS = 10


def run():
  channel = implementations.insecure_channel('localhost', 50051)
  stub = read_service_pb2.beta_create_ReadService_stub(channel)
  response = stub.GetReadGroupSet(read_service_pb2.GetReadGroupSetRequest(read_group_set_id='you'), _TIMEOUT_SECONDS)
  response = stub.GetReadGroupSet(read_service_pb2.SearchReadsRequest(read_group_ids=['a'], reference_id="1", start=0, end=100))
  print response


if __name__ == '__main__':
  run()