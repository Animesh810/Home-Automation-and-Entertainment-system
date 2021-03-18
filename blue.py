# bluetooth communication file
import bluetooth as bt
import os

NAME_DEVICE = "HomeAuto-123"
#ADDR_DEVICE = None
ADDR_DEVICE = '0C:9D:92:A1:36:B7'

def lookUpNearbyBluetoothDevices():
  nearby_devices = bt.discover_devices()
  for bdaddr in nearby_devices:
    print((bt.lookup_name( bdaddr )) + " [" + (bdaddr) + "]")
    
def findDevice():
    global ADDR_DEVICE
    nearby_devices = bt.discover_devices()
    for bdaddr in nearby_devices:
        if  NAME_DEVICE == bt.lookup_name( bdaddr ) :
            ADDR_DEVICE = bdaddr
            break
            
    #bt.pair(addr)
    #bt.connect(addr)
    if ADDR_DEVICE is not None:
        print('found')
        print(ADDR_DEVICE)
    else:
        findDevice()
            
def sendMsg(targetBluetoothMacAddress):
  port = 1
  sock=bt.BluetoothSocket( bt.RFCOMM )
  sock.connect((targetBluetoothMacAddress, port))
  sock.send("hello!!")
  sock.close()          
            

#actual code to test here
#findDevice()
print('ADDR_DEVICE: ')
print(ADDR_DEVICE)
#sendMsg(ADDR_DEVICE)

server_sock=bt.BluetoothSocket( bt.RFCOMM )

port = 1
print('now')
server_sock.bind(("",port))
server_sock.listen(1)

client_sock,address = server_sock.accept()
print ("Accepted connection from ")
print (address)

data = client_sock.recv(1024)
print ("received [%s]" % data)

client_sock.close()
server_sock.close()
