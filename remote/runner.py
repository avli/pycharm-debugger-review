import pydevd_pycharm

pydevd_pycharm.settrace('10.211.55.2', port=12345, stdoutToServer=True,
                        stderrToServer=True)

if __name__ == '__main__':
    file = "quadratic_equation.py"
    with open(file) as f:
        contents = f.read()
    exec(compile(contents, file, "exec"), globals(), locals())
