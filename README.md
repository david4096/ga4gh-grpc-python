# ga4gh-grpc-python

This is an implementation of the ga4gh-schemas using python generated gRPC bindings. The goal of this application is to present the bindings for implementing a GA4GH gateway. It does not provide an implementation to serve RPC requests or for adding genomics data to a datastore.

## Development

### Set up code/environment

This will download a script to install protocol buffers with gRPC plugins.

    curl -fsSL https://goo.gl/getgrpc | bash -s python

Then get a copy of the repository and create a virtual environment.

    git clone https://github.com/david4096/ga4gh-grpc-python.git
    cd ga4gh-grpc-python
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

### Regenerate schemas (optional)

The schemas are added as a submodule. For now, this means you can go to that directory and use `git pull` to get the latest from that repository. The protocol buffers bindings are currently checked in. To regenerate them you might run:

    protoc -I schemas/src/main/proto --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` schemas/src/main/proto/ga4gh/*

### Running

Start the read service with `python read_service.py`. Then, open another terminal and make sure to get back into the same virtual environment (`source env/bin/activate`).

Then you can run `python client.py` and you should see something like:

    D0801 18:58:32.494901000 140735095906304 ev_posix.c:101] Using polling engine: poll
    id: "echo"

    E0801 18:58:32.562562000 140735095906304 chttp2_transport.c:1810] close_transport: {"created":"@1470103112.562539000","description":"FD shutdown","file":"src/core/lib/iomgr/ev_poll_posix.c","file_line":427}
    
Here, we've issued a request to the server and it has responded back with a read_group_set with the `id` from our request.

### Implementing methods

In the file `read_service.py`, there isn't much. To implement a method to service an RPC request, you can simply add it to the function here:


    class ReadService(read_service_pb2.BetaReadServiceServicer):
    
      def SearchReadGroupSets(self, request, context):
        return read_service_pb2.SearchReadGroupSetsResponse()
    
      def GetReadGroupSet(self, request, context):
        return reads_pb2.ReadGroupSet(id=request.read_group_set_id)

For example, to change our response to include a name we could add:

        return reads_pb2.ReadGroupSet(id=request.read_group_set_id, name="my name")

We need to restart our server to reflect these changes (ctrl^c the tab with the server) and restart it using `python read_service.py`. Then rerunning `python client.py` we see something like:

    D0801 19:07:06.385810000 140735095906304 ev_posix.c:101] Using polling engine: poll
    id: "echo"
    name: "my name"

    E0801 19:07:06.454768000 140735095906304 chttp2_transport.c:1810] close_transport: {"created":"@1470103626.454738000","description":"FD shutdown","file":"src/core/lib/iomgr/ev_poll_posix.c","file_line":427}

