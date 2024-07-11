import grpc
import sys

from proto.gen.service_pb2_grpc import *
from proto.gen.service_pb2 import *
from common.constants import *

def send_message(client_name, command_name, content):
    with grpc.insecure_channel('localhost:{0}'.format(PORT)) as channel:
        stub = SatelliteServiceStub(channel)

        message = StatusMessage(client_name=client_name,
                                command_name=command_name,
                                content=content)
        stub.SendStatusUpdate(message)  # No response expected

if __name__ == '__main__':
    total_args = len(sys.argv)
    assert total_args == 3
    client_name = sys.argv[1]
    command_name = sys.argv[2]

    if not sys.stdin.isatty():  # Check if there's input from a pipe
        content = sys.stdin.read().rstrip()  # Read all input from stdin
        # Process input_data here 
    else:
        content = None

    send_message(client_name, command_name, content)