
class router(object):

    def __init__(self, model, swversion, ip_addr):
        self.model = model
        self.swversion = swversion
        self.ip_addr = ip_addr

    def desc(self):
       # print(self.model,  self.swversion,   self.ip_addr)

        desc =  (f"Router Model   :{self.model}\n"\
                    f"Software version  :{self.swversion}\n"\
                    f"Router Management Address :{self.ip_addr}")
        return desc

class Switch(router):
    def desc(self):
       attrib = (f"Switch Model   :{self.model}\n"\
            f"Software version  :{self.swversion}\n"\
            f"Switch Management Address :{self.ip_addr}")
       return attrib
