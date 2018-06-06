import Pyro4

uri="PYRO:Get.systeminfo@192.168.19.130:38535"
greeting_maker=Pyro4.Proxy(uri)
print greeting_maker.get_sysinfo('cpu')
