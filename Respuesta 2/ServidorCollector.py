from xmlrpc.server import SimpleXMLRPCServer

import gc 

class RPC:

    #methods = ['get','set','delete','exists', 'keys', 'calc']
    methods = ['isValid', 'calc']
    operators = {
        '+':'+'
    }
    def __init__(self, direction, port):
        self.server = SimpleXMLRPCServer((direction, port), allow_none=True)
        
        for method in self.methods:
            self.server.register_function(getattr(self, method))
    
    def isValid(self, oper):
        return oper in self.operators
    
    def calc(self, oper):
        c = 0
        if oper == self.operators['+']:
            i = 0 
            def refcycle(): 
                x = { } 
                x[i] = x 
                print(x) 
                
            collected = gc.collect()
            print( "Creating cycles...")
            for i in range(20): 
                refcycle() 
            collected = gc.collect()
            return( "Garbage collector: collected %d objects." % (collected))

        else:
            return 'invalid key'

    def run(self):
        self.server.serve_forever()
        print("server starting !!!")
    
if __name__ == '__main__':
    rpc = RPC('', 20064)
    print('server starting !!!!')
    rpc.run()