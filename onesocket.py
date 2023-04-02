import socket
import json

class OneSocketAPI:

    def __init__(self, port, endpoint_objects):
        
        # server init
        HOST, PORT = '', port
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.bind((HOST, PORT))
        listen_socket.listen(1)
        print('Serving HTTP on PORT: ' + str(PORT))

        # main loop
        while True:
            
            # parse raw request, get json data
            client_connection, client_address = listen_socket.accept()
            request_data_arr = client_connection.recv(1024).decode('utf-8').split('\n')
            request_data = ''
            json_data = {}
            for element in request_data_arr:
                if len(element) > 0 and element[0] == '{':
                    request_data = element
                    break
            if request_data != '':
                json_data = json.loads(request_data)

            # handle response
            endpoint = json_data['endpoint']
            endpoint_object = endpoint_objects[endpoint]
            res = ''
            try:
                res = endpoint_object.handle(json_data)
            except Exception as e:
                res = str(e)
            
            # format and send response
            http_response = b"""\
        HTTP/1.1 200 OK
        Access-Control-Allow-Origin: *

        """ + bytes(str(res), 'utf-8')
            client_connection.sendall(http_response)
            client_connection.close()