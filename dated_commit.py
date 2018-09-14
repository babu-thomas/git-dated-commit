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
    print(out.decode(), error.decode())
    return out, error


def git_init(path):
    cmd = 'git init'
    return execute_shell_command(cmd, path)


def git_add(file_path, repo_path):
    cmd = 'git add ' + str(file_path.resolve())
    return execute_shell_command(cmd, repo_path)


if __name__ == '__main__':
    p = Path('D:/code/interviewbit')
    paths = get_file_paths(p)
    print(paths)
    times = get_modified_time(paths)
    print(times)
    execute_shell_command('git --version', p)
    git_init(p)
    git_add(paths[0], p)
