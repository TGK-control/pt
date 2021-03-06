def get_trunk_list(trunk):
    trunk_template = [' switchport trunk encapsulation dot1q',
                      ' switchport mode trunk',
                      ' switchport trunk native vlan 999',
                      ' switchport trunk allowed vlan']
    result = dict.fromkeys(trunk.keys())
    for interface in trunk.items():
        result[interface[0]] = []
        result[interface[0]].append(trunk_template[0])
        result[interface[0]].append(trunk_template[1])
        result[interface[0]].append(trunk_template[2])
        result[interface[0]].append(trunk_template[3] + " " + str(interface[1])[1:-1])
    return result


trunk_dict = {'FastEthernet0/1': [10, 20, 30],
              'FastEthernet0/2': [11, 30],
              'FastEthernet0/4': [17]}
print(get_trunk_list(trunk_dict))
