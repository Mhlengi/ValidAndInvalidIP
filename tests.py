import os

from challenge import IPValidator


def test_valid_ip_address_ipv4():
    is_ip_valid, address, version = IPValidator.validate_ip_address(
        '10.10.1.1'
    )

    assert is_ip_valid
    assert address == '10.10.1.1'
    assert version == 'IPv4'


def test_invalid_ip_address():
    is_ip_valid, address, version = IPValidator.validate_ip_address(
        '902903920392'
    )

    assert not is_ip_valid
    assert address == '902903920392'


def test_ipv6_validate_ip_address():
    is_ip_valid, address, version = IPValidator.validate_ip_address(
        '2001:0db8:85a3:0000:0000:8a2e:0370:7334'
    )

    assert is_ip_valid
    assert address == '2001:0db8:85a3:0000:0000:8a2e:0370:7334'
    assert version == 'IPv6'


def test_remove_file():
    IPValidator.remove_file('test_1_ValidIPs.txt')

    assert True


def test_open_and_append_on_file_with_valid_ipv4_address():
    IPValidator.remove_file('test_file_ValidIPs.txt')
    valid_ips_file_name = 'test_file_ValidIPs.txt'
    address = '10.10.1.1'
    version = 'IPv4'
    IPValidator.open_and_append_on_file(valid_ips_file_name, address, version)
    file = IPValidator.file_append(
        address,
        valid_ips_file_name,
        version
    )

    assert file.close


def test_open_and_append_on_file_with_valid_ipv6_address():
    IPValidator.remove_file('test_file_ValidIPs.txt')
    valid_ips_file_name = 'test_file_ValidIPs.txt'
    address = '2001:0db8:85a3:0000:0000:8a2e:0370:7334'
    version = 'IPv6'
    IPValidator.open_and_append_on_file(valid_ips_file_name, address, version)
    file = IPValidator.file_append(
        address,
        valid_ips_file_name,
        version
    )

    assert file.close


def test_open_and_append_on_invalid_ip_address_file():
    IPValidator.remove_file('test_file_invalidIPs.txt')
    valid_ips_file_name = 'test_file_invalidIPs.txt'
    address = '902903920392'
    version = 'Invalid IP'
    IPValidator.open_and_append_on_file(valid_ips_file_name, address, version)
    file = IPValidator.file_append(
        address,
        valid_ips_file_name,
        version
    )

    assert file.close


def test_parser():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(current_dir, 'test_file.txt')
    parser = IPValidator.parse_args([my_file])
    file = IPValidator.create_file_from_parse_args(parser)
    IPValidator.close_file(file)

    assert file.closed
