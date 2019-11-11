from __future__ import print_function
import sys


def trace_calls(frame, event, args):
    print("calling %s in %s at line %d" % (
        frame.f_code.co_name, frame.f_code.co_filename, frame.f_lineno))


def f():
    print("in f()")


def g():
    print("in g()")


def h():
    print("in h()")
    f()
    g()


if __name__ == '__main__':
    sys.settrace(trace_calls)
    h()
