def cidr_to_subnet_mask(cidr: str):
    cidr = int(cidr)
    if cidr < 0 or cidr > 32:
        raise ValueError("CIDR must be between 0 and 32.")
    
    network_value = 32 - cidr
    #print(network_value)
    
    mask = (0xFFFFFFFF << network_value) & 0xFFFFFFFF
    mask_bytes = format(mask, '032b')
    return mask_bytes

def get_network_address(client_ip: str):
    ip , cidr = client_ip.split("/")
    octets = ip.split(".")
    network_mask = cidr_to_subnet_mask(cidr)

    first_octet = network_mask[0:8]
    second_octet = network_mask[8:16]
    third_octet = network_mask[16:24]
    fourth_octet = network_mask[24:32]

    print(first_octet)
    print(second_octet)
    print(third_octet)
    print(fourth_octet)
    
    #network_octets = [
    #    str((network_mask[0:8] >> 24) & 0xFF),
    #    str((network_mask >> 16) & 0xFF),
    #    str((network_mask >> 8) & 0xFF),
    #    str(network_mask & 0xFF)
    #]

    #".".join(network_octets)

#print("subnet mask 30: ", cidr_to_subnet_mask(30))
#print("subnet mask 24: ", cidr_to_subnet_mask(24))
#print("subnet mask 16: ", cidr_to_subnet_mask(16))

print("network address: ", get_network_address("192.168.24.245/32"))
#print("network address: ", get_network_address("192.168.24.245/30"))
#print("network address: ", get_network_address("192.168.24.245/16"))
