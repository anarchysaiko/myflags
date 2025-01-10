import re
from datetime import datetime
import pytz


def calculate_progress(tasks):
    if not tasks:
        return None
    total = len([t for t in tasks if t.strip().startswith("- [")])
    if total == 0:
        return None
    completed = len([t for t in tasks if t.strip().startswith("- [x]")])
    return (completed * 100 // total) if total > 0 else 0


# ... 其余 Python 代码 ...
