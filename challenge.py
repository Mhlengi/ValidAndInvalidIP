import argparse
import ipaddress
import os
import sys

# define valid ip's file name
ValidIpsFileName = 'validIPs.txt'
# define invalid ip's file name
InvalidIpsFileName = 'invalidIPs.txt'


# ip's address validator class.
class IPValidator:
    # static method function class to validate an IP address on the file.
    @staticmethod
    def validate_ip_address(address):
        try:
            ip_address = ipaddress.ip_address(address)
            ip_version = 'IPv{0}'.format(ip_address.version)
            return 1, address, ip_version
        except Exception as error:
            return 0, address, error

    # static method function class to remove a file if does exists.
    @staticmethod
    def remove_file(name):
        os.remove(name) if os.path.exists(name) else None

    # static method function class to close a file if open.
    @staticmethod
    def close_file(opened_file):
        if not opened_file.closed:
            opened_file.close()

    # static method function class to open and append into a file.
    @staticmethod
    def open_and_append_on_file(file_name, address, version):
        file = IPValidator.file_append(address, file_name, version)
        IPValidator.close_file(file)

    # static method function class to append into a file.
    @staticmethod
    def file_append(address, file_name, version):
        with open(file_name, 'a') as file:
            file.write('{0} :-> {1}\n'.format(address, version))
        return file

    # static method function class to return file from parse argument.
    @staticmethod
    def create_file_from_parse_args(args):
        with open(args.fileName) as file:
            for line in file.readlines():
                ip_address_as_line = line.strip()
                is_ip_valid, address, version = \
                    IPValidator.validate_ip_address(ip_address_as_line)
                if is_ip_valid:
                    IPValidator.open_and_append_on_file(
                        ValidIpsFileName, address, version
                    )
                else:
                    IPValidator.open_and_append_on_file(
                        InvalidIpsFileName, address, version
                    )
        return file

    # static method function class to create parse argument.
    @staticmethod
    def parse_args(args):
        parser = argparse.ArgumentParser()
        parser.add_argument('fileName')
        return parser.parse_args(args)


# main process function
def main():
    IPValidator.remove_file(ValidIpsFileName)
    IPValidator.remove_file(InvalidIpsFileName)
    args = IPValidator.parse_args(sys.argv[1:])
    file = IPValidator.create_file_from_parse_args(args)
    IPValidator.close_file(file)


if __name__ == '__main__':
    main()
