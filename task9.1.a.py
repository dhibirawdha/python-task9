def generate_access_config(intf_vlan_mapping, access_template, psecurity=None):
    access_config = []

    for intf, vlan in intf_vlan_mapping.items():
        access_config.append(f"interface {intf}")
        for command in access_template:
            if command.endswith("access vlan"):
                access_config.append(f"{command} {vlan}")
            else:
                access_config.append(command)
        if psecurity:
            access_config.extend(psecurity)
    return access_config
