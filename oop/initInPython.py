class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
        self.company =  "HP"
    def config(self):
        print("Config is",self.cpu,self.ram,self.company)

    def compare(self,other):
        if self.cpu == other.cpu:
            return True
        else:
            return False

com1 = Computer("i5","8gb")
com1.config()

com2 = Computer("i5","8gb")
com2.company = "Apple"
com2.cpu = "M1"
com2.config()
print(com1.compare(com2))

