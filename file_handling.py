class file:
    def __init__(self,filename):
        self.filename=filename
        
    def read(self,mode):
        self.mode=mode
        f=open(self.filename,self.mode)
        data=f.read()
        print(data)
        f.close()
    def write(self,mode):
        self.mode=mode
        f=open(self.filename,self.mode)
        f.write('Writing on the file')
        f.close()
    def append(self,mode):
        self.mode=mode
        f=open(self.filename,self.mode)
        f.write('Appending on the file')
        f.close()