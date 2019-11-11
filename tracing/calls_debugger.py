"""
Usage: python calls_debugger.py <file>
"""
from __future__ import print_function
import sys


def trace_calls(frame, event, arg):
    print("calling %s in %s at line %d" % (
        frame.f_code.co_name, frame.f_code.co_filename, frame.f_lineno))


if __name__ == '__main__':
    sys.settrace(trace_calls)
    file = sys.argv[1]
    with open(file) as f:
        contents = f.read()
    exec(compile(contents, file, "exec"), globals(), locals())
