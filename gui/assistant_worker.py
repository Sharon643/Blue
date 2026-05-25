from PyQt6.QtCore import (
    QThread,
    pyqtSignal
)

from voice.listen import listen
from voice.speak import speak

from brain.ai import ask_ai

from memory.memory import (
    conversation_history,
    save_chat_memory,
    user_memory,
    save_user_memory
)

from brain.memory_extractor import (
    extract_memory
)

from brain.router import detect_intent

from commands.actions import execute_command

from config.settings import WAKE_WORD


class AssistantWorker(QThread):


    # SIGNALS

    status_signal = pyqtSignal(str)

    transcript_signal = pyqtSignal(str)


    # MAIN THREAD LOOP


    def run(self):

        while True:

            try:

                self.status_signal.emit(
                    "Waiting for wake word..."
                )

                wake_text = listen().lower()

                print("Heard:", wake_text)

                if WAKE_WORD in wake_text:

                    self.status_signal.emit(
                        "Speaking..."
                    )

                    speak("Yes?")

                    # SESSION LOOP
                    while True:

                        try:

                            self.status_signal.emit(
                                "Listening..."
                            )

                            user_text = listen()

                            print("You:", user_text)

                            self.transcript_signal.emit(
                                f"You: {user_text}"
                            )

                            intent = detect_intent(
                                user_text
                            )

                            print(
                                "Intent:",
                                intent
                            )

                            
                            # MEMORY
                           
                            if intent == "memory":

                                new_memory = (
                                    extract_memory(
                                        user_text
                                    )
                                )

                                if new_memory:

                                    # SAFE MEMORY MERGE

                                    for key, value in new_memory.items():

                                        if value is not None:

                                            user_memory[key] = value

                                    save_user_memory(
                                        user_memory
                                    )

                           
                            # COMMANDS
                        
                            elif intent == "command":

                                command_executed = (
                                    execute_command(
                                        user_text
                                    )
                                )

                                if command_executed:

                                    continue

                            # EMPTY
                            if user_text == "":

                                speak(
                                    "Please repeat that."
                                )

                                continue

                            # EXIT
                            if "goodbye" in user_text.lower():

                                speak("Goodbye.")

                                break

                            # SAVE USER
                            conversation_history.append(
                                f"User: {user_text}"
                            )

                            save_chat_memory(
                                conversation_history
                            )

                            # THINKING
                            self.status_signal.emit(
                                "Thinking..."
                            )

                            ai_response = ask_ai(
                                conversation_history
                            )

                            # SAVE AI
                            conversation_history.append(
                                f"Blue: {ai_response}"
                            )

                            save_chat_memory(
                                conversation_history
                            )

                            print(
                                "\nBlue:",
                                ai_response
                            )

                            self.transcript_signal.emit(
                                f"Blue: {ai_response}"
                            )

                            self.status_signal.emit(
                                "Speaking..."
                            )

                            speak(ai_response)

                        except Exception as e:

                            print(
                                "Conversation Error:",
                                e
                            )

            except Exception as e:

                print(
                    "Wake Word Error:",
                    e
                )