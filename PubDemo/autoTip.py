import io


def bar(f):
    assert isinstance(f, io.IOBase)
    f.readlines()


def foo(a: str, b: int):
    a.split()


def bee(l):
    """
    :type l: list
    """

    l.append()