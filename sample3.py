import atheris
import pytest
import sys

# from .utils import reach_api

import requests


URL = "https://pokeapi.co/api/v2/{}"


def reach_api(path, json):
    # add params
    param = URL.format(path)

    try:
        r = requests.get(url=param, json=json)
        r.raise_for_status()
        print(r)
    except requests.HTTPError as e:
        if e.response.status_code not in [404, 200, 301]:
            raise e


@atheris.instrument_func
# def test_ability():
def get_ability(name):
    reach_api("ability", {"name": str(name)})


# atheris.instrument_all()
# atheris.Setup(sys.argv, get_ability)
# atheris.Fuzz()

reach_api("ability", {"name": str("\0")})

# test_ability()
