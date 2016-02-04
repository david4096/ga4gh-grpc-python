TODO

curl -fsSL https://goo.gl/getgrpc | bash -s python

pip install grpcio

pip install grpc --upgrade

protoc -I /Users/david/ga4gh/schemas2/src/main/proto/ga4gh --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` /Users/david/ga4gh/schemas2/src/main/proto/ga4gh/*

