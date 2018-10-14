# -*- coding: utf-8 -*-

"""OS tools """

import os
import shlex
from subprocess import PIPE, STDOUT, Popen, call

import psutil


class Process:
    """OS process"""

    def __init__(self, cmd):
        """
        :param cmd: Command to execute
        """
        self.cmd = cmd

    def get_simple_output(self, stderr=STDOUT):
        """Executes a simple external command and get its output
        The command contains no pipes. Error messages are
        redirected to the standard output by default

        :param stderr: where to put stderr
        :return: output of command
        """
        args = shlex.split(self.cmd)
        proc = Popen(args, stdout=PIPE, stderr=stderr)
        return proc.communicate()[0].decode("utf8")

    def get_complex_output(self, stderr=STDOUT):
        """Executes a piped command and get the lines of the output in a list

        :param stderr: where to put stderr
        :return: output of command
        """
        proc = Popen(self.cmd, shell=True, stdout=PIPE, stderr=stderr)
        return proc.stdout.readlines()

    def get_output_from_pipe(self, input_file):
        """Executes an external command and get its output. The command
        receives its input_file from the stdin through a pipe
        
        :param input_file: input file
        :return: output of command
        """
        args = shlex.split(self.cmd)
        p = Popen(args, stdout=PIPE, stdin=PIPE)  # | grep es
        p.stdin.write(bytearray(input_file.encode("utf8")))  # echo test |
        return p.communicate()[0].decode("utf8")

    def get_return_code(self, stderr=STDOUT):
        """Executes a simple external command and return its exit status
        
        :param stderr: where to put stderr
        :return: return code of command
        """
        args = shlex.split(self.cmd)
        return call(args, stdout=PIPE, stderr=stderr)

    def get_exit_code(self):
        """Executes the external command and get its exitcode, stdout and stderr
        
        :return: exit code of command
        """
        args = shlex.split(self.cmd)

        proc = Popen(args, stdout=PIPE, stderr=PIPE)
        out, err = proc.communicate()
        out, err = out.decode("utf8"), err.decode("utf8")
        exitcode = proc.returncode
        #
        return exitcode, out, err

    def execute(self):
        """Executes a simple external command"""
        args = shlex.split(self.cmd)
        call(args)

    def execute_in_background(self):
        """Executes a (shell) command in the background

        :return: the process' pid
        """
        # http://stackoverflow.com/questions/1605520
        args = shlex.split(self.cmd)
        p = Popen(args)
        return p.pid

    def keep_alive(self):
        """Keeps a process alive. If the process terminates, it will restart it
        The terminated processes become zombies. They die when their parent
        terminates
        """
        while True:
            pid = self.execute_in_background()
            p = psutil.Process(pid)
            while p.is_running() and str(p.status) != 'zombie':
                os.system('sleep 5')

    @staticmethod
    def get_process_list():
        """Gets the list of running processes

        :return: (generator of) running processes
        """
        return psutil.process_iter()
