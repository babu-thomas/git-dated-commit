import datetime as dt
import os
from pathlib import Path

from dateutil.tz import gettz

p = Path('.')
files = [x.resolve() for x in p.iterdir() if not x.is_dir()]
print(files)
unix_times = [os.path.getmtime(x) for x in files]
times = [dt.datetime.fromtimestamp(x, gettz('Asia/Calcutta')).isoformat() for x in unix_times]
print(times)
