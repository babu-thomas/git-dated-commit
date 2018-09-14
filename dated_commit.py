import datetime as dt
import os
import subprocess
from pathlib import Path

from dateutil.tz import gettz


def get_file_paths(dir_):
    if not dir_.is_dir:
        return list(dir_.resolve())
    return [path.resolve() for path in dir_.iterdir() if not path.is_dir()]


def get_modified_time(files):
    unix_times = [os.path.getmtime(f) for f in files]
    return [dt.datetime.fromtimestamp(t, gettz()).isoformat() for t in unix_times]


def execute_shell_command(cmd, work_dir):
    pipe = subprocess.Popen(cmd, shell=True, cwd=work_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, error = pipe.communicate()
    return out, error


if __name__ == '__main__':
    p = Path()
    out, error = execute_shell_command('git --version', p)
    print(out.decode(), error.decode())
    paths = get_file_paths(p)
    print(paths)
    times = get_modified_time(paths)
    print(times)
