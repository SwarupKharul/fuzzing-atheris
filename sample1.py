import sys
import atheris


@atheris.instrument_func
def TestOneInput(data):
    print(data)
    if len(data) != 8:
        return

    if chr(data[0]) == "f":
        if chr(data[1]) == "u":
            if chr(data[2]) == "z":
                if chr(data[3]) == "z":
                    if chr(data[4]) == "i":
                        if chr(data[5]) == "n":
                            if chr(data[6]) == "g":
                                if chr[data[7]] == "!":
                                    raise RuntimeError("Error input found!")


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
