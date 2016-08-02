# ga4gh-grpc-python

This is an implementation of the ga4gh-schemas using python generated gRPC bindings. The goal of this application is to present the bindings for implementing a GA4GH gateway. It does not provide an implementation to serve RPC requests or for adding genomics data to a datastore.

## Development

This will download a script to install protocol buffers with gRPC plugins.

    curl -fsSL https://goo.gl/getgrpc | bash -s python

Then get a copy of the repository and create a virtual environment.

    git clone https://github.com/david4096/ga4gh-grpc-python.git
    cd ga4gh-grpc-python
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

Then start the read service with `python read_service.py`. Open another terminal and make sure to get back into the same virtual environment (`source env/bin/activate`).

The schemas are added as a submodule and the protocol buffers bindings are currently checked in. To regenerate them you might run:

    protoc -I schemas/src/main/proto --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` schemas/src/main/proto/ga4gh/*

