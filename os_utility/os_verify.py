# Openstack clients imports
from config.auth_config import glance, nova, neutron, cinder
# Miscellanea imports
from os_utility.miscellanea import get_param, printout
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)
#TODO get defaults parameters via openstack clients

""" All these functions verifies the parameters existence (image, flavor, security group, key pair, network, volume, 
port inside the openstack server """
#################################################
#              Verify GLANCE images             #
#################################################
def verify_images(images, doc, yamlfile):
    printout(">> Verifying the image existence...\n", CYAN)
    # It executes a call via glance client to get all the images [images are Image class objects]
    images_list = glance.images.list()
    search_by_id = []
    search_by_name = []
    # It saves them by name and by ID
    for item in images_list:
        search_by_id.append(item.id)
        search_by_name.append(item.name)
    # It iterates the list images
    for image in images:
        # If the image string it will directly check for that image with a glance.images.get() function
        if type(image) == str:
            # If the image is in one of the two glance lists it means it exists
            if image in search_by_id or image in search_by_name:
                print("     The image '{}' used in the template '{}' exists".format(image, yamlfile))
            else:
                print("     The image '{}' used in the template '{}' does not exist".format(image, yamlfile))
        # If the image is a dictionary it means the parameter has to be found in the parameters or resources of the template
        else:
            image = get_param(image, doc)
            # If the return from the function is a dict it means the parameter has not be found/it will be allocated automatically
            if type(image) == dict:
                for k, v in image.items():
                    print(v)
            # If the template image is in the images list of glance then the value exists
            elif image in search_by_id or image in search_by_name:
                print("     The image '{}' used in the template '{}' exists".format(image, yamlfile))
            else:
                print("     The image '{}' used in the template '{}' does not exist".format(image, yamlfile))

#################################################
#              Verify NOVA flavors              #
#################################################
def verify_flavors(flavors, doc, yamlfile):
    # It saves the list of flavors of the openstack server [flavors are Flavor class objects]
    flavors_list = nova.flavors.list()
    search_by_id = []
    search_by_name = []
    # It saves them by name and by ID
    for item in flavors_list:
        search_by_name.append(item.name)
        search_by_id.append(item.id)
    printout(">> Verifying the flavor existence...\n", CYAN)
    # For every flavor in the flavors list it checks its existence
    for flavor in flavors:
        if type(flavor) == str:
            # It checks if the flavor appears in the list of flavors of our openstack
            if flavor in search_by_name or flavor in search_by_id:
                print("     The flavor '{}' used in the template '{}' exists".format(flavor, yamlfile))
            else:
                print("     The flavor '{}' used in the template '{}' does not exist".format(flavor, yamlfile))
        # If the flavor is a dict it will look for its value in the parameters of the template
        else:
            flavor = get_param(flavor, doc)
            # If the return from the function is a dict it means the parameter has not be found/it will be allocated automatically
            if type(flavor) == dict:
                for k, v in flavor.items():
                    print(v)
            elif flavor in search_by_name or flavor in search_by_id:
                print("     The flavor '{}' used in the template '{}' exists".format(flavor, yamlfile))
            else:
                print("     The flavor '{}' used in the template '{}' does not exist".format(flavor, yamlfile))

#################################################
#        Verify NEUTRON security groups         #
#################################################
def verify_secgroups(sec_groups, doc, yamlfile):
    printout(">> Verifying the security group existence...\n", CYAN)
    # It saves the list of security groups of our openstack [security groups are dicts]
    security_list = neutron.list_security_groups()
    security_id_list = []
    security_name_list = []
    # It saves in two separate lists: IDs and names all the security groups of our openstack
    for item in security_list['security_groups']:
        security_id_list.append(item['id'])
        security_name_list.append(item['name'])
    # For every item of the list sec_groups it checks for its existence
    for sec_group in sec_groups:
        if type(sec_group) == str:
            # It checks if the security group appears in the list of security groups of our openstack
            if sec_group in security_id_list or sec_group in security_name_list:
                print("     The security group '{}' used in the template '{}' exists".format(sec_group, yamlfile))
            else:
                print("     The security group '{}' used in the template '{}' does not exist".format(sec_group,yamlfile))
        else:
            sec_group = get_param(sec_group, doc)
            # If the return from the function is a dict it means the parameter has not be found/it will be allocated automatically
            if type(sec_group) == dict:
                for k, v in sec_group.items():
                    print(v)
            elif sec_group in security_id_list or sec_group in security_name_list:
                print("     The security group '{}' used in the template '{}' exists".format(sec_group, yamlfile))
            else:
                print("     The security group '{}' used in the template '{}' does not exist".format(sec_group,yamlfile))

#################################################
#             Verify NEUTRON networks           #
#################################################
def verify_networks(networks, doc, yamlfile):
    printout(">> Verifying the networks existence...\n", CYAN)
    for network in networks:
        if type(network) == str:
            # If the network is a str and the neutron.list_networks() function works then the network exists
            search_by_name = neutron.list_networks(name=network)
            search_by_id = neutron.list_networks(id=network)
            if search_by_name['networks'] or search_by_id['networks']:
                print("     The network '{}' used in the template '{}' exists".format(network, yamlfile))
            else:
                print("     The network '{}' used in the template '{}' does not exist".format(network, yamlfile))
        # If it is a dictionary it has to find the parameter in the template
        elif type(network) == dict:
            network = get_param(network, doc)
            # If the return from the function is a dict it means the parameter has not be found/it will be allocated automatically
            if type(network) == dict:
                for k, v in network.items():
                    print(v)
            else:
                search_by_name = neutron.list_networks(name=network)
                search_by_id = neutron.list_networks(id=network)
                if search_by_name['networks'] or search_by_id['networks']:
                    print("     The network '{}' used in the template '{}' exists".format(network, yamlfile))
                else:
                    print("     The network '{}' used in the template '{}' does not exist".format(network, yamlfile))
        # If it is a list it might have different keys/values
        elif type(network) == list:
            if 'port' in network[0]:
                # If it is a port it will do the neutron.list_ports to check its existence
                port = network[0]['port']
                if type(port) == str:
                    search_by_id = neutron.list_ports(id=port)
                    search_by_name = neutron.list_ports(name=port)
                    if search_by_id['ports'] or search_by_name['ports']:
                        print("     The network with port '{}' used in the template '{}' exists".format(port, yamlfile))
                    else:
                        print("     The network with port '{}' used in the template '{}' does not exist".format(port, yamlfile))
                elif type(port) == dict:
                    port = get_param(port, doc)
                    # If the return from the function is a dict it means the parameter has not be found/it will be allocated automatically
                    if type(port) == dict:
                        for k, v in port.items():
                            print(v)
                    else:
                        search_by_id = neutron.list_ports(id=port)
                        search_by_name = neutron.list_ports(name=port)
                        if search_by_id['ports'] or search_by_name['ports']:
                            print("     The network with port '{}' used in the template '{}' exists".format(port, yamlfile))
                        else:
                            print("     The network with port '{}' used in the template '{}' does not exist".format(port, yamlfile))
            elif 'allocate_network' in network[0]:
                # If it has 'allocate_network' it will be probably allocated automatically along with the template
                allocate_network = network[0]['allocate_network']
                if allocate_network == 'auto':
                    print("     The network will be allocated automatically")
                else:
                    pass
            elif 'subnet' in network[0]:
                # If it is a subnet it will do the neutron.list_subnets to check its existence
                subnet = network[0]['subnet']
                search_by_id = []
                search_by_name = []
                subnets = neutron.list_subnets()
                # It saves two lists, one for the subnets IDs and one for the subnets' names
                for item in subnets['subnets']:
                    # subnets['subnets'] is made of dictionaries
                    search_by_id.append(item['id'])
                    search_by_name.append(item['name'])
                # If our subnet is in one or in the other list then it exists
                if subnet in search_by_id or subnet in search_by_name:
                    print("     The subnet '{}' used in the template '{}' exists".format(subnet, yamlfile))
                else:
                    print("     The subnet '{}' used in the template '{}' does not exist".format(subnet, yamlfile))

#################################################
#              Verify NEUTRON ports             #
#################################################
def verify_ports(ports, doc, yamlfile):
    printout(">> Verifying the ports existence...", CYAN)
    # For every port in the ports list it checks for its existence
    for port in ports:
        if type(port) == str:
            # It does the neutron.list_ports function to check the port existence
            search_by_id = neutron.list_ports(id=port)
            search_by_name = neutron.list_ports(name=port)
            if search_by_id['ports'] or search_by_name['ports']:
                print("     The port '{}' used in the template '{}' exists".format(port, yamlfile))
            # If there is the key "get_resource" it means the port'll be directly allocated in another resource
            elif 'get_resource' in port:
                print("     The port will be allocated through another resource".format(port, yamlfile))
            else:
                print("     The port used in the template '{}' does not exist".format(yamlfile))
        elif type(port) == dict:
            port = get_param(port, doc)
            # If the return from the function is a dict it means the parameter has not be found/it will be allocated automatically
            if type(port) == dict:
                for k, v in port.items():
                    print(v)
            else:
                search_by_id = neutron.list_ports(id=port)
                search_by_name = neutron.list_ports(name=port)
                if search_by_id['ports'] or search_by_name['ports']:
                    print("     The port '{}' used in the template '{}' exists".format(port, yamlfile))
                else:
                    print("     The port used in the template '{}' does not exist".format(yamlfile))

#################################################
#             Verify NOVA key pairs             #
#################################################
def verify_keypairs(keypairs, doc, yamlfile):
    printout(">> Verifying the keypairs existence...\n", CYAN)
    # It gets all the keypairs through the function nova.keypairs.list()
    keypairs_list = nova.keypairs.list()
    search_by_id = []
    search_by_name = []
    # It saves in the keypairs_list all the keypairs' IDs of our openstack
    for item in keypairs_list:
        search_by_id.append(item.id)
        search_by_name.append(item.name)
    # For every keypair in the keypairs list it checks for its existence in the nova keypairs list
    for keypair in keypairs:
        if type(keypair) == str:
            if keypair in search_by_id or keypair in search_by_name:
                print("     The keypair '{}' used in the template '{}' exists".format(keypair, yamlfile))
            else:
                print("     The keypair '{}' used in the template '{}' does not exist".format(keypair, yamlfile))
        elif type(keypair) == dict:
            keypair = get_param(keypair, doc)
            # If the return from the function is a dict it means the parameter has not be found/it will be allocated automatically
            if type(keypair) == dict:
                for k, v in keypair.items():
                    print(v)
            else:
                if keypair in search_by_id or keypair in search_by_name:
                    print("     The keypair '{}' used in the template '{}' exists".format(keypair, yamlfile))
                else:
                    print("     The keypair '{}' used in the template '{}' does not exist".format(keypair, yamlfile))

#################################################
#             Verify CINDER volumes             #
#################################################
def verify_volumes(volumes, doc, yamlfile):
    printout(">> Verifying the volumes existence...\n", CYAN)
    # It gets all the volumes through the function cinder.volume.list()
    volumes_list = cinder.volumes.list()
    search_by_id = []
    search_by_name = []
    # It saves in the volumes_list all the volume' IDs and names of our openstack
    for item in volumes_list:
        search_by_id.append(item.id)
        search_by_name.append(item.name)
    # For every volume in the volumes list it checks for its existence in the cinder volumes list
    for volume in volumes:
        if type(volume) == str:
            if volume in search_by_id or volume in search_by_name:
                print("     The volume '{}' used in the template '{}' exists".format(volume, yamlfile))
            else:
                print("     The volume '{}' used in the template '{}' does not exist".format(volume, yamlfile))
        elif type(volume) == dict:
            volume = get_param(volume, doc)
            # If the return from the function is a dict it means the parameter has not be found/it will be allocated automatically
            if type(volume) == dict:
                for k, v in volume.items():
                    print(v)
            else:
                if volume in search_by_id or volume in search_by_name:
                    print("     The volume '{}' used in the template '{}' exists".format(volume, yamlfile))
                else:
                    print("     The volume '{}' used in the template '{}' does not exist".format(volume, yamlfile))
