# PY04021 - TÍNH TOÁN THỜI GIAN

import re

class Time:
    def __init__(self, h, m):
        self.h = h
        self.m = m
    def __sub__(self, other):
        if self.m < other.m:
            self.m = self.m + 60
            self.h = self.h - 1
        return Time(self.h-other.h, self.m-other.m)
    def change_to_minutes(self):
        return self.h*60 + self.m
    def __repr__(self):
        return f"{self.h} gio {self.m} phut"

class Gamer:
    def __init__(self, code, name, time_start, time_end):
        self.code = code
        self.name = name
        self.time_start = time_start
        self.time_end = time_end
        self.format()
        self.time_play = self.time_end - self.time_start
    def format(self):
        time_start = re.findall("\d\d", self.time_start)
        time_end = re.findall("\d\d", self.time_end)
        self.time_start = Time(int(time_start[0]), int(time_start[1]))
        self.time_end = Time(int(time_end[0]), int(time_end[1]))

    def change_to_minutes(self):
        return self.time_play.change_to_minutes()
    def __repr__(self):
        return f"{self.code} {self.name} {self.time_play}"

times = int(input())
gamers = []
for i in range(times):
    code = input()
    name = input()
    time_start = input()
    time_end = input()
    gamer = Gamer(code, name, time_start, time_end)
    gamers.append(gamer)
gamers.sort(key=Gamer.change_to_minutes, reverse=True)
for gamer in gamers:
    print(gamer)


