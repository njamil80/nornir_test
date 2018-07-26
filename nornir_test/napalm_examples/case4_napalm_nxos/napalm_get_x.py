from nornir.core import InitNornir
from nornir.plugins.tasks.networking import napalm_get

from pprint import pprint
from nornir_test.nornir_utilities import nornir_set_creds, std_print

# Turn off self-signed cert warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def main():
    brg = InitNornir(config_file="./nornir.yml")
    nornir_set_creds(brg)
    result = brg.run(
        task=napalm_get,
        getters=["facts"],
    )

    std_print(result)


if __name__ == "__main__":
    main()
