from device import router, Switch

    

    #def model(self):

#router1 = router("cisco_5500", "cisco_1osv", "10.100.90.1")

#router1.desc()

#router1.desc = "virtual router"

#print(router1.desc)

router2 = router("ISR 9221", "16.9.5", "10.100.90.2")

# from router2 call attribute model and print it
print(router2.model)



rtr1 = router("iosV", "15.6.7","10.10.100.1")
rtr2 = router("isr4221", "16.9.5", "10.10.100.5")
switch1 = Switch("IOSl2V", "17.0.1", "10.10.100.6")

print("Router1\n", rtr1.desc(), '\n', sep=" ")

print("Router2\n",rtr2.desc())

print("\nSwitch1")
print(switch1.desc())
