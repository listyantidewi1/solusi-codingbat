"""
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".
alarm_clock(1, False) → '7:00'
alarm_clock(5, False) → '7:00'
alarm_clock(0, False) → '10:00'

Diberikan satu nama hari
0=Sun
1=Mon
2=Tue
dst
6=Sat
dan sebuah nilai boolean (true atau false) yang menandakan bahwa hari tersebut adalah hari liburan. Kembalikan sebuah string yang berupa "7:00" yang mengindikasikan jam berapa alarm harus berbunyi. Alarm harus berbunyi jam 07.00 di hari aktif, dan jam 10.00 di hari minggu, kecuali sedang berlibur
alarm_clock(1, False) → '7:00'
alarm_clock(5, False) → '7:00'
alarm_clock(0, False) → '10:00'
alarm_clock(1, True) → '10:00'
"""


def alarm_clock(day, vacation):
    # week_day didefinisikan sebagai hari yang tidak termasuk di hari pertama (0 / minggu) dan terakhir (6 / sabtu)
    week_day = day not in (0, 6)

    if vacation:  # jika vacation atau liburan = true
        return '10:00' if week_day else 'off'  # alarm = 10:00

    # selain itu alarm 7:00 jika week_day, selain weekday = 10:00
    return '7:00' if week_day else '10:00'
