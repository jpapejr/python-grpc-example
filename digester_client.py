import grpc
import digestor_pb2
import digestor_pb2_grpc
import sys


class DigestorClient(object):
    """
    Client for accessing the gRPC functionality
    """

    def __init__(self):
        # configure the host and the
        # the port to which the client should connect
        # to.
        self.host = sys.argv[1]
        self.server_port = sys.argv[2]

        # sanity check
        print("Connecting to " + self.host + " on port " + str(self.server_port) + ".")

        # instantiate a communication channel
        self.channel = grpc.insecure_channel(
                        '{}:{}'.format(self.host, self.server_port))

        # bind the client to the server channel
        self.stub = digestor_pb2_grpc.DigestorStub(self.channel)

    def get_digest(self, message):
        """
        Client function to call the rpc for GetDigest
        """
        to_digest_message = digestor_pb2.DigestMessage(ToDigest=message)
        return self.stub.GetDigestor(to_digest_message)


client = DigestorClient()
print(client.get_digest(sys.argv[3]))