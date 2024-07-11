import socket

PORT = 10253

def getWyomingTopic(satellite_id : str, method : str):
    return "satellite/wyoming/{0}/{1}".format(satellite_id, method)

def getIP():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    result = s.getsockname()[0]
    s.close()

    return result