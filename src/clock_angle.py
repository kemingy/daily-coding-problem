# Given a clock time in hh:mm format, determine, to the nearest degree, the
# angle between the hour and the minute hands.

# Bonus: When, during the course of a day, will the angle be zero?


def clock_angle(time: str) -> float:
    hour, minute = time.split(':')
    assert hour.isdigit() and minute.isdigit()
    hour, minute = int(hour), int(minute)
    degree_h = (360 / 12) * (hour % 12 + minute / 60)
    degree_m = (360 / 60) * minute
    degree = max(degree_h, degree_m) - min(degree_h, degree_m)
    return degree if degree < 180 else 360 - degree


if __name__ == '__main__':
    for time in ['00:00', '22:18', '04:29', '11:11']:
        print(clock_angle(time))
