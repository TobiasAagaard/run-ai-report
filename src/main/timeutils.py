from __future__ import annotations
from datetime import datetime, timedelta


def month_range(year: int, month: int) -> tuple[datetime, datetime]:
    start = datetime(year, month, 1)
    if month == 12:
        end = datetime(year + 1, 1, 1) - timedelta(seconds=1)
    else:
        end = datetime(year, month + 1, 1) - timedelta(seconds=1)
    return start, end

def quarter_range(year: int, quarter: int) -> tuple[datetime, datetime]:
    start_month = (quarter - 1) * 3 + 1
    start = datetime(year, start_month, 1)
    if quarter == 4:
        end = datetime(year + 1, 1, 1) - timedelta(seconds=1)
    else:
        end = datetime(year, start_month + 3, 1) - timedelta(seconds=1)
    return start, end

def year_range(year: int) -> tuple[datetime, datetime]:
    start = datetime(year, 1, 1)
    end = datetime(year + 1, 1, 1) - timedelta(seconds=1)
    return start, end
