import os
import binascii

filename = 'C:\\Users\\ltoma\\Documents\\Hex\\Payloadpy.exe' 

with open(filename, 'rb') as file:
    binary_data = file.read()
    hex_code = binascii.hexlify(binary_data).decode()

print(hex_code)