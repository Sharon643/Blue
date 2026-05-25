import sys

from PyQt6.QtWidgets import QApplication

from gui.window import BlueWindow

from gui.assistant_worker import (AssistantWorker)


def start_gui():

    app = QApplication(sys.argv)

    # WINDOW
    window = BlueWindow()

    # WORKER
    worker = AssistantWorker()

    
    # CONNECT SIGNALS
    

    worker.status_signal.connect(
        window.set_status
    )

    worker.transcript_signal.connect(
        window.set_transcript
    )

    # START THREAD
    worker.start()

    # SHOW WINDOW
    window.show()

    sys.exit(app.exec())