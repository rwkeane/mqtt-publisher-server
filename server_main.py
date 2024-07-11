from server.parser import *
from server.server import *

if __name__ == "__main__":
    total_args = len(sys.argv)
    assert total_args == 2

    filepath = sys.argv[1]

    username, password = parse(filepath)
    server = ServiceImpl(username, password)
    serve(server)