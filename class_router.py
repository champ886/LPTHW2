class router(object):

    def __init__(self, model, swversion, ip_addr):
        self.model = model
        self.swversion = swversion
        self.ip_addr = ip_addr

    def desc(self):
        print(self.model,  self.swversion,   self.ip_addr)

router1 = router("cisco_5500", "cisco_1osv", "10.100.90.1")

router1.desc()

