# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".

def defangIPaddr(address):
    """
    :type address: str
    :rtype: str
    """
    build_up = ""
    for character in address:
        if (character != "."):
            build_up += character
        else:
            build_up += "[.]"

    return build_up

address = "1.1.1.1"
new_address = defangIPaddr(address)
print(new_address)

