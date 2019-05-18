import os
import subprocess
import sys


def main(argv):
    script_filename = argv[0]

    assert os.path.exists(script_filename)

    p = subprocess.Popen([sys.executable, script_filename], 
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding='utf-8',
    )

    first_output = p.stdout.read(1)
    print(f"first_output = {repr(first_output)}")

    stdout, stderr = p.communicate(input='a\nb\n')

    print(f"stdout={repr(stdout)}")
    print(f"stderr={repr(stderr)}")


if "__main__" == __name__:
    main(sys.argv[1:])
