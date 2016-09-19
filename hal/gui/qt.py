# !/usr/bin/python
# coding: utf_8

# Copyright 2016 Stefano Fogarollo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


""" pre-built methods to create beautiful apps with qt """


import os
from PyQt4.QtCore import *
from PyQt4 import QtGui
from PyQt4 import QtCore


class Window(QtGui.QMainWindow):
    """ classic window in qt """

    def __init__(self):
        QtGui.QMainWindow.__init__(self, parent=None)

        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 800, 440  # default width, height
        self.setup_actions()  # actions
        self.status_bar = QtGui.QStatusBar(self)  # status bar
        self.setStatusBar(self.status_bar)
        self.setup_ui()  # main layout
        self.show()  # show

    def setup_ui(self):
        """
        :return: setup layout
        """

        self.setObjectName('main_window')
        self.setWindowTitle('Window')
        self.resize(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)  # size
        self.setMinimumSize(QtCore.QSize(400, 400))
        self.status_bar.showMessage('Ready')  # status bar
        self.setStatusBar(self.status_bar)

    def setup_actions(self):
            """
            :return: main actions: file > new, save, open, close
            """
            
            menu_bar = self.menuBar()  # menu
            
            new_action = QtGui.QAction('New', self)  # file action
            new_action.setShortcut('Ctrl+N')
            new_action.setStatusTip('Create new file')
            new_action.triggered.connect(self.new_file)

            open_action = QtGui.QAction('Open', self)
            open_action.setShortcut('Ctrl+O')
            open_action.setStatusTip('Open a file')
            open_action.triggered.connect(self.open_file)

            save_action = QtGui.QAction('Save', self)
            save_action.setShortcut('Ctrl+S')
            save_action.setStatusTip('Save current file')
            save_action.triggered.connect(self.save_file)

            close_action = QtGui.QAction('Quit', self)
            close_action.setShortcut('Ctrl+Q')
            close_action.setStatusTip('Close program')
            close_action.triggered.connect(self.close)

            file_menu = menu_bar.addMenu('&File')
            file_menu.addAction(new_action)
            file_menu.addAction(open_action)
            file_menu.addAction(save_action)
            file_menu.addAction(close_action)

            get_help = QtGui.QAction('Help', self)  # help action
            get_help.setStatusTip('Show help')
            get_help.triggered.connect(self.show_help)

            get_about = QtGui.QAction('About', self)
            get_about.setStatusTip('About this program')
            get_about.triggered.connect(self.show_about)

            help_menu = menu_bar.addMenu('&Help')
            help_menu.addAction(get_help)
            help_menu.addAction(get_about)

    def new_file(self):
        """
        :return: open new file menu
        """

        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))

    def new_folder(self):
        """
        :return: let user chose new folder
        """

        path = str(QtGui.QFileDialog.getExistingDirectory(self, 'Select Directory'))

    def save_file(self):
        """
        :return: save current file
        """

        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))

    def open_file(self):
        """
        :return: open-file menu
        """
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))

    def show_help(self):
        """
        :return: show help dialog
        """

        class HelpWindow(QtGui.QMainWindow):
            """ help dialog """
            def __init__(self, parent):
                QtGui.QMainWindow.__init__(self, parent)

                self.setup_ui()
                self.show_help()

            def setup_ui(self):
                """
                :return: setup layout
                """

                self.setObjectName('help_window')
                self.setWindowTitle('Help me')
                self.resize(300, 200)
                self.setMinimumSize(300, 200)

            def show_help(self):
                """
                :return: show help dialog
                """

                # label
                label = QtGui.QLabel('', self)
                label.setGeometry(0, 0, self.frameGeometry().width() - 10, self.frameGeometry().height() - 10)
                label.setAlignment(Qt.AlignVCenter)
                label.setText('Basic commands:'
                              '<br><i>File > New</i>: new istance'
                              '<br><i>File > Open</i>: open folder'
                              '<br><i>File > Save</i>: save current job'
                              '<br><i>File > Quit</i>: quit program'
                              '<br><i>Help > Help</i>: show this help dialog'
                              '<br><i>Help > About</i>: show about dialog')

                # margin around label
                label.setStyleSheet('margin:10px;')

        dialog = HelpWindow(self)
        dialog.show()
        self.status_bar.showMessage('Help')

    def show_about(self):
        """
        :return: show about dialog
        """

        class AboutWindow(QtGui.QMainWindow):
            """ about dialog """

            def __init__(self, parent):
                QtGui.QMainWindow.__init__(self, parent)

                self.setup_ui()
                self.show_about()

            def setup_ui(self):
                """
                :return: setup main layout
                """

                self.setObjectName('about_window')
                self.setWindowTitle('About this program')
                self.resize(300, 150)
                self.setMinimumSize(304, 150)

            def show_about(self):
                """
                :return: show about dialog
                """
                
                # label
                label = QtGui.QLabel('', self)
                label.resize(self.frameGeometry().width(), self.frameGeometry().height())
                label.setAlignment(Qt.AlignHCenter)
                label.setText('Copyright (C) 2016 Stefano Fogarollo'
                              '<br>Do you want to pay me a coffee?'
                              '<br>Contact me! sirfoga@protonmail.com')

                # frame around label
                label.setStyleSheet('margin:10px;')

        dialog = AboutWindow(self)
        dialog.show()
        self.status_bar.showMessage('About')
