def cidr_to_subnet_mask(cidr: str):
    """
    Get subnet mask from CIDR format.

    Parameters:
    cidr (str) : cidr string (ex. 30, 16)

    Returns:
    string: The subnmet mask as string of bits (ex. 11111111 11111111 11111111 11111100)
    """

    cidr = int(cidr)
    if cidr < 0 or cidr > 32:
        raise ValueError("CIDR must be between 0 and 32.")
    
    network_value = 32 - cidr
    
    mask = (0xFFFFFFFF << network_value) & 0xFFFFFFFF
    mask_bytes = format(mask, '032b')
    return mask_bytes

def get_network_address(client_ip: str):
    """
    Get the network IP from the input of a client IP.

    Parameters: 
    client_ip (str): Client IP including CIDR (ex. /30)

    Return:
    network IP (str): The network IP based on client IP and CIDR.
    """

    ip , cidr = client_ip.split("/")
    octets = ip.split(".")
    int_cidr = int(cidr)

    mask_bin = (0xFFFFFFFF << (32 - int_cidr)) & 0xFFFFFFFF
    
    network_mask_octets = [
        str((mask_bin >> 24) & 0xFF),
        str((mask_bin >> 16) & 0xFF),
        str((mask_bin >> 8) & 0xFF),
        str(mask_bin & 0xFF)
    ]

    network_octets_str = ".".join(network_mask_octets)
    network_ip = []

    for i in range(0,4):
        octet_bytes = int(octets[i]).to_bytes(8, byteorder="big")
        network_bytes = int(network_mask_octets[i]).to_bytes(8, byteorder="big")

        network_ip.append(str(int.from_bytes(octet_bytes, byteorder="big",signed=True) & int.from_bytes(network_bytes, byteorder="big",signed=True)))
        
    network_ip_str = ".".join(network_ip)
    network_ip_str = network_ip_str + f"/{cidr}"
    
    return network_ip_str

print("network address: ", get_network_address("192.168.24.9/30"))
