from PyQt6.QtWidgets import (QWidget,QLabel,QVBoxLayout,QFrame)
from PyQt6.QtCore import (Qt,QPropertyAnimation,QEasingCurve)
from PyQt6.QtGui import QFont
from gui.widgets.waveform import WaveformWidget


class BlueWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Blue")

        self.setGeometry(100, 100, 500, 500)

        self.setStyleSheet("""
            background-color: #020617;
            color: white;
        """)

        layout = QVBoxLayout()

        # ORB
       
        self.orb = WaveformWidget()

        self.orb.setFixedSize(150, 150)

        self.orb.setStyleSheet("""
            background-color: #2563eb;
            border-radius: 75px;
        """)

        # STATUS LABEL
       
        self.status_label = QLabel("Idle")

        self.status_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.status_label.setFont(
            QFont("Arial", 18)
        )

      
        # TRANSCRIPT
      

        self.transcript_label = QLabel("")

        self.transcript_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.transcript_label.setWordWrap(True)

        self.transcript_label.setFont(
            QFont("Arial", 13)
        )

      
        # LAYOUT
      
        layout.addStretch()

        layout.addWidget(
            self.orb,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        layout.addSpacing(20)

        layout.addWidget(self.status_label)

        layout.addSpacing(20)

        layout.addWidget(self.transcript_label)

        layout.addStretch()

        self.setLayout(layout)

       
        # ANIMATION
       

        self.animation = QPropertyAnimation(
            self.orb,
            b"maximumSize"
        )

        self.animation.setDuration(800)

        self.animation.setStartValue(
            self.orb.size()
        )

        self.animation.setEndValue(
            self.orb.size() + self.orb.size()/8
        )

        self.animation.setLoopCount(-1)

        self.animation.setEasingCurve(
            QEasingCurve.Type.InOutQuad
        )

    
    # STATUS
    

    def set_status(self, text):

        self.status_label.setText(text)

        # IDLE
        if "Waiting" in text:

            self.orb.set_state("idle")

        # LISTENING
        elif "Listening" in text:

            self.orb.set_state("listening")

        # THINKING
        elif "Thinking" in text:

            self.orb.set_state("thinking")

        # SPEAKING
        elif "Speaking" in text:

            self.orb.set_state("speaking")

    
    # TRANSCRIPT
    

    def set_transcript(self, text):

        self.transcript_label.setText(text)