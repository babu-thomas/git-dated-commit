import datetime as dt
import os
from pathlib import Path

from dateutil.tz import gettz


def get_file_paths(dir_):
    if not dir_.is_dir:
        return list(dir_.resolve())
    return [path.resolve() for path in dir_.iterdir() if not path.is_dir()]


def get_modified_time(files, timezone):
    unix_times = [os.path.getmtime(f) for f in files]
    return [dt.datetime.fromtimestamp(t, timezone).isoformat() for t in unix_times]


if __name__ == '__main__':
    p = Path('.')
    paths = get_file_paths(p)
    print(paths)
    tz = gettz('Asia/Calcutta')
    times = get_modified_time(paths, tz)
    print(times)
