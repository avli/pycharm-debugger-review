"""
An example script for debugging by `calls_debugger.py` and `lines_debugger.py`.
"""


def f():
    print("in f()")


def g():
    print("in g()")


def h():
    print("in h()")
    f()
    g()


h()
