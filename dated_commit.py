import datetime as dt
import os
from pathlib import Path

from dateutil.tz import gettz


def get_file_paths(dir_):
    if not dir_.is_dir:
        return list(dir_.resolve())
    return [path.resolve() for path in dir_.iterdir() if not path.is_dir()]


def get_modified_time(files):
    unix_times = [os.path.getmtime(f) for f in files]
    return [dt.datetime.fromtimestamp(t, gettz()).isoformat() for t in unix_times]


if __name__ == '__main__':
    p = Path()
    paths = get_file_paths(p)
    print(paths)
    times = get_modified_time(paths)
    print(times)
