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


def execute_shell_command(cmd, work_dir, env_vars={}):
    pipe = subprocess.Popen(cmd, shell=True, env={**os.environ, **env_vars}, cwd=work_dir,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, error = pipe.communicate()
    print(out.decode(), error.decode())
    return out, error


def git_init(path):
    cmd = 'git init'
    return execute_shell_command(cmd, path)


def git_add(file_path, repo_path):
    cmd = 'git add ' + str(file_path.resolve())
    return execute_shell_command(cmd, repo_path)


def git_commit_with_date(commit_msg, date, repo_path):
    env = {'GIT_AUTHOR_DATE': date, 'GIT_COMMITTER_DATE': date}
    cmd = f'git commit -m "{commit_msg}"'
    return execute_shell_command(cmd, repo_path, env)


def git_commit_all_files(dir_):
    paths = get_file_paths(dir_)
    paths.sort(key=lambda x: os.path.getmtime(x))
    times = get_modified_time(paths)
    git_init(dir_)
    for f, t in zip(paths, times):
        git_add(f, dir_)
        git_commit_with_date(f.name, t, dir_)


if __name__ == '__main__':
    p = Path()
    git_commit_all_files(p)
