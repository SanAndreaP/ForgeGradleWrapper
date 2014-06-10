import json
import io
import os

from src import firstStart

__author__ = 'SanAndreasP'

# constants for config values
GRADLE_PATH = u"gradlePath"
IDE = u"ide"
JAVA_VER = u"javaVer"

# config data (use constants from above as keys)
data = dict()


def init_values():
    global data
    if os.path.isfile("gradlew"):
        data[GRADLE_PATH] = "."
    elif os.path.isfile("forge/gradlew"):
        data[GRADLE_PATH] = "forge"
    else:
        data[GRADLE_PATH] = None


def read_config():
    global data
    try:
        with io.open("config.json") as cfg_file:
            data = json.load(cfg_file, encoding="utf-8")
    except IOError:
        init_values()
        firstStart.call()
        write_config()


def write_config():
    global data
    try:
        with io.open("config.json", "w") as cfg_file:
            cfg_file.write(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))
    except IOError as ex:
        print(ex)