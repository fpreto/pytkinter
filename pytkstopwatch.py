
from datetime import datetime, timedelta
from tkinter import *
from tkinter.font import Font
import time


class PyTkStopWatch:
    def __init__(self):
        self._window = Tk()
        self._window.title("PyTkStopWatch")

        self._timefont = Font(size=120)

        self._hourdescriptionlabel = Label(text="Current Time")
        self._hourdescriptionlabel.grid(row=0, column=1)

        self._hourlabel = Label(text="00:00:00")
        self._hourlabel['font'] = self._timefont
        self._hourlabel.grid(row=1, column=0, rowspan=1, columnspan=3)

        self._starthourdescriptionlabel = Label(text="Start Time")
        self._starthourdescriptionlabel.grid(row=2, column=1)

        self._starttimelabel = Label(text="00:00:00")
        self._starttimelabel['font'] = self._timefont
        self._starttimelabel.grid(row=3, column=0, rowspan=1, columnspan=3)

        self._timedescriptionlabel = Label(text="Elapsed Time")
        self._timedescriptionlabel.grid(row=4, column=1)

        self._timelabel = Label(text="00:00:00")
        self._timelabel['font'] = self._timefont
        self._timelabel.grid(row=5, column=0, rowspan=1, columnspan=3)

        self._startbutton = Button(text="START", command=self._on_start_click)
        self._startbutton.grid(row=6, column=0)

        self._stopbutton = Button(text="STOP", command=self._on_stop_click)
        self._stopbutton.grid(row=6, column=1)

        self._resetbutton = Button(text="RESET", command=self._on_reset_click)
        self._resetbutton.grid(row=6, column=2)

        self._timerrunning = False
        self._reset_before_start = True
        self._starttime = datetime.now()
        self._basedelta = timedelta()

    def run(self):
        self._update_clock()
        self._window.mainloop()

    def _on_start_click(self):
        if self._reset_before_start:
            now = time.strftime("%H:%M:%S")
            self._starttimelabel.configure(text=now)
            self._basedelta = timedelta()
            self._timelabel.configure(text="00:00:00")

        if not self._timerrunning:
            self._starttime = datetime.now()
            self._reset_before_start = False
            self._timerrunning = True

    def _on_stop_click(self):
        if self._timerrunning:
            self._basedelta += datetime.now() - self._starttime
            self._timerrunning = False

    def _on_reset_click(self):
        self._timerrunning = False
        self._starttimelabel.configure(text="00:00:00")
        self._timelabel.configure(text="00:00:00")
        self._reset_before_start = True
        self._basedelta = timedelta()

    def _update_clock(self):
        now = time.strftime("%H:%M:%S")
        self._hourlabel.configure(text=now)
        self._window.after(500, self._update_clock)

        if self._timerrunning:
            elapsedtime = datetime.now() - self._starttime + self._basedelta
            formatedtime = self._timeformat(elapsedtime.total_seconds(), elapsedtime.microseconds)
            self._timelabel.configure(text=formatedtime)

    def _timeformat(self, totalseconds:int, microseconds: int) -> str:
        miliseconds = microseconds % 1000
        decimal = miliseconds // 100
        seconds = totalseconds % 60
        minutes = (totalseconds // 60) % 60
        hours = (totalseconds // (60 * 60)) % 24

        return "%02d:%02d:%02d" % (hours, minutes, seconds)


if __name__ == '__main__':
    watch = PyTkStopWatch()
    watch.run()
