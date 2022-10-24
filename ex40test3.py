class Exams(object):
    def __init__ (self, devcert, ccie):
        self.devcert = devcert
        self.ccie = ccie
        
    def write_devcert(self):
        for text in self.devcert:
            print(text)
        #print(self.devcert)
        #print(self.ccie)

    def write_ccie(self):
        print(self.ccie)
        print(self.devcert)

    
## set take_devcert to a class instance of Exams
take_devcert = Exams(["""Prepare well 
for the denet cert""", "USe cisco dev website"], "CCIE Later")

# from take_devcert, get function write_devcert
take_devcert.write_devcert()

#take_devcert.write_ccie()


print("#" * 50)

mylist = [ "champ", "Peter is here", "Khaled has left"]

for line in mylist:
    print(line)

take_devcert.write_ccie = Exams("Finish", "Yes")




