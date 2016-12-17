from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_dhcp_service(Service, Socket, SystemInfo):
    if SystemInfo.type == 'openbsd':
        service = Service('dhcpd')
    elif SystemInfo.type == 'debian':
        service = Service('isc-dhcp-server')
    assert service.is_running
    try:
        assert service.is_enabled
    except NotImplementedError:
        pass
    assert Socket('tcp://0.0.0.0:80').is_listening
