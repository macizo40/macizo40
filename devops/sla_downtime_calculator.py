#!/usr/bin/env python3
"""Calculate maximum downtime allowed by an annual SLA target."""

import argparse
import calendar
from dataclasses import dataclass
from datetime import datetime


SECONDS_PER_DAY = 24 * 60 * 60


@dataclass(frozen=True)
class Downtime:
    days: int
    hours: int
    minutes: int
    seconds: int


def calculate_downtime(sla_percent: float, year: int) -> tuple[int, Downtime]:
    """Return days in the year and maximum downtime rounded to a second."""
    if not 0 <= sla_percent <= 100:
        raise ValueError("SLA percentage must be between 0 and 100.")
    if year < 1:
        raise ValueError("Year must be a positive number.")

    days_in_year = 366 if calendar.isleap(year) else 365
    total_seconds = days_in_year * SECONDS_PER_DAY
    downtime_seconds = round(total_seconds * (1 - sla_percent / 100))

    days, remainder = divmod(downtime_seconds, SECONDS_PER_DAY)
    hours, remainder = divmod(remainder, 60 * 60)
    minutes, seconds = divmod(remainder, 60)

    return days_in_year, Downtime(days, hours, minutes, seconds)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Calculate annual downtime allowed by an SLA target."
    )
    parser.add_argument(
        "--sla",
        type=float,
        default=99.50,
        help="SLA target percentage (default: 99.50)",
    )
    parser.add_argument(
        "--year",
        type=int,
        default=datetime.now().year,
        help="Calendar year; leap years contain 366 days",
    )
    args = parser.parse_args()

    try:
        days_in_year, downtime = calculate_downtime(args.sla, args.year)
    except ValueError as error:
        parser.error(str(error))

    total_hours = (
        downtime.days * 24
        + downtime.hours
        + downtime.minutes / 60
        + downtime.seconds / 3600
    )

    print("Annual SLA Downtime Calculator")
    print(f"Year: {args.year} ({days_in_year} days)")
    print(f"SLA goal: {args.sla:.5g}%")
    print(f"Unavailability: {100 - args.sla:.5g}%")
    day_label = "day" if downtime.days == 1 else "days"
    print(
        "Maximum downtime: "
        f"{downtime.days} {day_label}, {downtime.hours} hours, "
        f"{downtime.minutes} minutes, {downtime.seconds} seconds"
    )
    print(f"Maximum downtime in hours: {total_hours:.4f}")


if __name__ == "__main__":
    main()
