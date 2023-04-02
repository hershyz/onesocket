# import library:
import onesocket


# create handler object:
class Add:

    # create handler method, take json data:
    def handle(self, json_data):
        a = float(json_data['a'])
        b = float(json_data['b'])
        return a + b


# define handler object instance and endpoint map:
add_obj = Add()
endpoint_map = {
    'add': add_obj
}

# initialize api with port and endpoint object mappings:
api = onesocket.OneSocketAPI(8080, endpoint_map)