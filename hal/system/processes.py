# -*- coding: utf-8 -*-

"""OS tools """

import os
import shlex
from subprocess import PIPE, STDOUT, Popen, call

import psutil


class Process:
    """OS process"""

    def __init__(self, cmd):
        self.cmd = cmd

    def get_simple_cmd_output(self, stderr=STDOUT):
        """Execute a simple external command and get its output
    
        The command contains no pipes. Error messages are
        redirected to the standard output by default
        """
        args = shlex.split(self.cmd)
        proc = Popen(args, stdout=PIPE, stderr=stderr)
        return proc.communicate()[0].decode("utf8")

    def get_complex_cmd_output(self, stderr=STDOUT):
        """
        Execute a piped command and get the lines of the output in a list
        """
        proc = Popen(self.cmd, shell=True, stdout=PIPE, stderr=stderr)
        return proc.stdout.readlines()

    def get_cmd_output_input_from_stdin(self, input_file):
        """Execute an external command and get its output. The command
        receives its input_file from the stdin through a pipe
    
        Example: 'echo test | grep es'."""
        args = shlex.split(self.cmd)
        p = Popen(args, stdout=PIPE, stdin=PIPE)  # | grep es
        p.stdin.write(bytearray(input_file.encode("utf8")))  # echo test |
        return p.communicate()[0].decode("utf8")

    def get_return_code_of_simple_cmd(self, stderr=STDOUT):
        """Execute a simple external command and return its exit status."""
        args = shlex.split(self.cmd)
        return call(args, stdout=PIPE, stderr=stderr)

    def get_exit_code_stdout_stderr(self):
        """
        Execute the external command and get its exitcode, stdout and stderr
        """
        args = shlex.split(self.cmd)

        proc = Popen(args, stdout=PIPE, stderr=PIPE)
        out, err = proc.communicate()
        out, err = out.decode("utf8"), err.decode("utf8")
        exitcode = proc.returncode
        #
        return exitcode, out, err

    def execute_cmd(self):
        """Execute a simple external command."""
        args = shlex.split(self.cmd)
        call(args)

    def execute_cmd_in_background(self):
        """Execute a (shell) command in the background
    
        Returns the process' pid."""
        # http://stackoverflow.com/questions/1605520
        args = shlex.split(self.cmd)
        p = Popen(args)
        return p.pid

    def keep_alive(self):
        """
        Keep a process alive
    
        If the process terminates, it will restart it
        The terminated processes become zombies. They
        die when their parent terminates
        """
        while True:
            pid = self.execute_cmd_in_background()
            p = psutil.Process(pid)
            while p.is_running() and str(p.status) != 'zombie':
                os.system('sleep 5')

    @staticmethod
    def get_process_list():
        """Get the list of running processes
    
        Example:
            PROCNAME = "python.exe"
    
            for proc in psutil.process_iter():
                if proc.name == PROCNAME:
                    proc.kill()
        """
        return psutil.process_iter()
