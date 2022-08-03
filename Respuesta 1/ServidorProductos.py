from xmlrpc.server import SimpleXMLRPCServer

def products(nome):
    if nome == 'router':
        return 'Tenda AC10 Asus - RT-AC53 - TP-Link Archer C7Tenda RX3 WiFi 6'
    elif nome == 'antena':
        return 'MOTOROLA SOLUTIONS - KENWOOD - ICOM - WOUXUN'
    elif nome == 'cable':
        return 'Ethernet Cat 5 - Ethernet Cat 5e - Ethernet Cat 6 - Ethernet Cat 6a'
    elif nome == 'exit':
        return '0'
    else:
        return '1'

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(products, "products")
server.serve_forever()