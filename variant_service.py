import time

import ga4gh.variant_service_pb2 as variant_service_pb2
import ga4gh.variants_pb2 as variants_pb2

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

def serve():
  server = variant_service_pb2.beta_create_VariantService_server(VariantService())
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(203948)
  except KeyboardInterrupt:
    server.stop()

if __name__ == '__main__':
  serve()