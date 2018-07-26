from getpass import getpass
from pprint import pprint


def nornir_set_creds(brg, username=None, password=None):
    """Handler so credentials don't need stored in clear in inventory."""
    if not username:
        username = input("Enter username: ")
    if not password:
        password = getpass()

    for host_obj in brg.inventory.hosts.values():
        # host_obj.username = username
        # host_obj.password = password
        host_obj.data["nornir_username"] = username
        host_obj.data["nornir_password"] = password


def std_print(agg_result):
    print()
    for k, multi_result in agg_result.items():
        print('-' * 50)
        print(k)
        for result_obj in multi_result:
            pprint(result_obj.result)
        print('-' * 50)
        print()
    print()
