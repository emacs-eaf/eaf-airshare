#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2018 Andy Stewart
#
# Author:     Andy Stewart <lazycat.manatee@gmail.com>
# Maintainer: Andy Stewart <lazycat.manatee@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from core.buffer import Buffer
from core.utils import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget


class AppBuffer(Buffer):
    def __init__(self, buffer_id, url, arguments):
        Buffer.__init__(self, buffer_id, url, arguments, False)

        self.add_widget(AirShareWidget(url, self.theme_foreground_color))

    @interactive
    def update_theme(self):
        super().update_theme()

        self.buffer_widget.change_color(self.theme_background_color, self.theme_foreground_color)

class AirShareWidget(QWidget):
    def __init__(self, url, foreground_color):
        QWidget.__init__(self)
        self.setStyleSheet("background-color: transparent;")

        self.file_name_font = QFont()
        self.file_name_font.setPointSize(48)

        self.file_name_label = QLabel(self)
        self.file_name_label.setText(url)
        self.file_name_label.setFont(self.file_name_font)
        self.file_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.file_name_label.setStyleSheet("color: {}".format(foreground_color))

        self.qrcode_label = QLabel(self)

        self.notify_font = QFont()
        self.notify_font.setPointSize(24)
        self.notify_label = QLabel(self)
        self.notify_label.setText("Scan QR code above to copy data.")
        self.notify_label.setFont(self.notify_font)
        self.notify_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.notify_label.setStyleSheet("color: {}".format(foreground_color))

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch()
        layout.addWidget(self.qrcode_label, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addSpacing(20)
        layout.addWidget(self.file_name_label, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addSpacing(40)
        layout.addWidget(self.notify_label, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()

        self.qrcode_label.setPixmap(get_qrcode_pixmap(url))

    def change_color(self, background_color, foreground_color):
        self.setStyleSheet("background-color: {};".format(background_color))
        self.file_name_label.setStyleSheet("color: {}".format(foreground_color))
        self.notify_label.setStyleSheet("color: {}".format(foreground_color))
