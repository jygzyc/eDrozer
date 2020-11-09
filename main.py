# -*- coding:utf-8 -*-
import logging
import subprocess

from drozer.console import Console
from mwr.common import logger

def local_cmd(cmd):
    pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout
    result = pipe.read()
    print(result)

if __name__ == '__main__':
    logger.setLevel(logging.DEBUG)
    logger.addStreamHandler()
    local_cmd('adb forward tcp:31415 tcp:31415')
    Console().run(["connect"])