from PyQt6.QtWidgets import QWidget

from PyQt6.QtCore import (
    QTimer
)

from PyQt6.QtGui import (
    QPainter,
    QColor,
    QRadialGradient,
    QBrush
)


class OrbWidget(QWidget):

    def __init__(self):

        super().__init__()

        self.setFixedSize(220, 220)

    
        # ORB STATE
    
        self.base_radius = 55

        self.radius = self.base_radius

        self.growing = True

        self.color = QColor("#2563eb")

        
        # TIMER
        

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.animate
        )

        self.timer.start(30)

   
    # ANIMATION
    

    def animate(self):

        if self.growing:

            self.radius += 0.4

            if self.radius >= 65:

                self.growing = False

        else:

            self.radius -= 0.4

            if self.radius <= 55:

                self.growing = True

        self.update()

   
    # PAINT
  

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        center_x = self.width() / 2

        center_y = self.height() / 2

       
        # GLOW
      

        gradient = QRadialGradient(
            center_x,
            center_y,
            self.radius * 2
        )

        glow_color = QColor(self.color)

        glow_color.setAlpha(80)

        gradient.setColorAt(
            0,
            glow_color
        )

        transparent = QColor(self.color)

        transparent.setAlpha(0)

        gradient.setColorAt(
            1,
            transparent
        )

        painter.setBrush(
            QBrush(gradient)
        )

        painter.setPen(
            QColor(0, 0, 0, 0)
        )

        painter.drawEllipse(
            int(center_x - self.radius * 1.5),
            int(center_y - self.radius * 1.5),
            int(self.radius * 3),
            int(self.radius * 3)
        )

      
        # MAIN ORB
      

        painter.setBrush(self.color)

        painter.drawEllipse(
            int(center_x - self.radius),
            int(center_y - self.radius),
            int(self.radius * 2),
            int(self.radius * 2)
        )

    # STATE COLORS
    

    def set_state(self, state):

        if state == "idle":

            self.color = QColor("#2563eb")

        elif state == "listening":

            self.color = QColor("#06b6d4")

        elif state == "thinking":

            self.color = QColor("#9333ea")

        elif state == "speaking":

            self.color = QColor("#22c55e")