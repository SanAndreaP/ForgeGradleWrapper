from __future__ import print_function

import threading
import time

from colorama.ansi import Fore, Style


__author__ = 'SanAndreasP'


class WorkingMsg(threading.Thread):
    def __init__(self, task, done_msg="[Done]", canceled_msg="[Cancelled]", error_msg="[Error]"):
        self._stopevent = threading.Event()
        self._output = 0
        self._task_name = task
        self._done_msg = done_msg
        self._cancel_msg = canceled_msg
        self._error_msg = error_msg
        threading.Thread.__init__(self, name="TestThread")

    def set_output(self, output):
        self._output = output

    def run(self):
        i = 0
        while not self._stopevent.isSet():
            print("\r" + self._task_name + "." * i + " " * (3 - i), end='')
            i += 1
            if i > 3:
                i = 0
            for j in range(1, 20):
                if self._stopevent.isSet():
                    break
                time.sleep(0.05)
        print("\r" + self._task_name + " - ", end="")
        if self._output == 0x00:
            print(self._done_msg)
        elif self._output == 0xff:
            print(Fore.YELLOW + Style.BRIGHT + self._cancel_msg)
        else:
            print(Fore.RED + Style.BRIGHT + self._error_msg + Fore.RESET + Style.NORMAL)

    def join(self, timeout=None):
        self._stopevent.set()
        threading.Thread.join(self, timeout)