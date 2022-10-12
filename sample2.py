import atheris
import sys


@atheris.instrument_func
def TestOneInput(data):
    if data == b"bad":
        raise RuntimeError("Badness!")


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
