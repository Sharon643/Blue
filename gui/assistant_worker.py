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
import time
from integrations.notion_client import add_task 
from brain.task_parser import parse_task
from brain.job_parser import parse_job
from tools.task_tools import create_task , read_tasks
from integrations.job_client import add_job_application

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

                            stt_start = time.time()
                            total_start = time.time()

                            user_text = listen()

                            print(
                                "STT Time:",
                                round(time.time() - stt_start, 2),
                                "seconds"
                            )

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
                           
                            if intent == "memory_write":

                                print("MEMORY WRITE")

                                new_memory = extract_memory(user_text)

                                for key, value in new_memory.items():

                                    if value is not None:

                                        user_memory[key] = value

                                save_user_memory(user_memory)

                                response = "I'll remember that."

                                speak(response)

                                continue
                            # COMMANDS
                        
                            elif intent == "command":

                                command_executed = (
                                    execute_command(
                                        user_text
                                    )
                                )

                                if command_executed:

                                    continue
                            elif intent == "task":

                                task_name = parse_task(user_text)

                                add_task(task_name)

                                response = f"Task added: {task_name}"

                                speak(response)

                                continue
                            elif intent == "task_create":

                                task_data = parse_task(
                                    user_text
                                )
                                if not task_data["task"]:
                                    speak("I couldn't understand the task.")
                                    continue

                                response = create_task(task_data)

                                speak(response)

                                continue

                            elif intent == "task_read":

                                response = read_tasks()

                                speak(response)

                                continue
                            elif intent == "job_create":

                                job_data = parse_job(
                                    user_text
                                )

                                if not job_data:

                                    speak(
                                        "I couldn't understand the application."
                                    )

                                    continue

                                add_job_application(
                                    job_data["company"],
                                    job_data["role"]
                                )

                                speak(
                                    f"Application saved for {job_data['company']}"
                                )

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

                            ai_start = time.time()

                            ai_response = ask_ai(
                                conversation_history
                            )

                            print(
                                "AI Time:",
                                round(time.time() - ai_start, 2),
                                "seconds"
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

                            tts_start = time.time()

                            speak(ai_response)
                            print(
                                "TOTAL:",
                                round(time.time() - total_start, 2),
                                "seconds"
                            )

                            print(
                                "TTS Time:",
                                round(time.time() - tts_start, 2),
                                "seconds"
                            )

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