"""
Usage: python lines_debugger.py <file>
"""
from __future__ import print_function
import sys


def trace_dispatch(frame, event, arg):
    if event == "call":
        print("calling %s in %s at line %d" % (
            frame.f_code.co_name, frame.f_code.co_filename, frame.f_lineno))
        return trace_dispatch
    elif event == "line":
        print("at line %d in %s" % (frame.f_lineno, frame.f_code.co_name))


if __name__ == '__main__':
    sys.settrace(trace_dispatch)
    file = sys.argv[1]
    with open(file) as f:
        contents = f.read()
    exec(compile(contents, file, "exec"), globals(), locals())
