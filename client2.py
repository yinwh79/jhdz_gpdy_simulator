from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('218.60.8.153')
client.write_coil(1, True)
result = client.read_coils(1,1)
print(result.bits[0])
client.close()



