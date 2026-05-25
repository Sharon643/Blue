import math

from PyQt6.QtWidgets import QWidget

from PyQt6.QtCore import QTimer

from PyQt6.QtGui import (
    QPainter,
    QColor,
    QPen
)


class WaveformWidget(QWidget):

    def __init__(self):

        super().__init__()

        self.setFixedSize(320, 320)

        # VISUAL STATE


        self.phase = 0

        self.color = QColor("#2563eb")

        self.mode = "idle"

        # TIMER
  

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.animate
        )

        self.timer.start(16)

    # ANIMATION LOOP


    def animate(self):

        self.phase += 0.08

        self.update()


    # DRAW


    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        center_x = self.width() / 2

        center_y = self.height() / 2

   
        # WAVE SETTINGS
   

        if self.mode == "idle":

            amplitude = 4

            speed = 1

        elif self.mode == "listening":

            amplitude = 12

            speed = 2

        elif self.mode == "thinking":

            amplitude = 8

            speed = 3

        elif self.mode == "speaking":

            amplitude = 18

            speed = 4

        else:

            amplitude = 5

            speed = 1

  
        # DRAW RINGS
      

        for ring in range(3):

            radius = 60 + ring * 25

            alpha = 180 - ring * 50

            color = QColor(self.color)

            color.setAlpha(alpha)

            pen = QPen(color)

            pen.setWidth(3)

            painter.setPen(pen)

            points = []

            for angle in range(360):

                rad = math.radians(angle)

                wave = math.sin(
                    rad * 6
                    + self.phase * speed
                    + ring
                )

                dynamic_radius = (
                    radius
                    + wave * amplitude
                )

                x = (
                    center_x
                    + dynamic_radius
                    * math.cos(rad)
                )

                y = (
                    center_y
                    + dynamic_radius
                    * math.sin(rad)
                )

                points.append((x, y))

            # DRAW SHAPE
            for i in range(len(points) - 1):

                painter.drawLine(
                    int(points[i][0]),
                    int(points[i][1]),
                    int(points[i + 1][0]),
                    int(points[i + 1][1])
                )

  
    # STATES
    

    def set_state(self, state):

        self.mode = state

        if state == "idle":

            self.color = QColor("#2563eb")

        elif state == "listening":

            self.color = QColor("#06b6d4")

        elif state == "thinking":

            self.color = QColor("#9333ea")

        elif state == "speaking":

            self.color = QColor("#22c55e")