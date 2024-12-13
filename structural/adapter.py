class Application:
    def send_request(self):
        return 'data.xml '

class Analytic:
    def recieve_data(self,file):
        return f'file is {file} json'

class Adapter:
    def convert_xml_json(self,xml_file):
        json_file = xml_file.replace('.xml','.json')
        return json_file

def client_adapter():
    sender = Application().send_request()
    converted_data = Adapter().convert_xml_json(sender)
    receiver = Analytic().recieve_data(converted_data)
    return receiver

print(client_adapter())



