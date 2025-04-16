import cv2
import dlib
from scipy.spatial import distance
import time
import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser
import subprocess

# Blink detection parameters
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

def detect_blink(triple_count=3, time_limit=3):
    print("Detecting blinks...")
    blink_counter = 0
    blink_times = []

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    (lStart, lEnd) = (42, 48)
    (rStart, rEnd) = (36, 42)

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 0)

        for rect in rects:
            shape = predictor(gray, rect)
            shape = [(shape.part(i).x, shape.part(i).y) for i in range(68)]

            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]

            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)
            ear = (leftEAR + rightEAR) / 2.0

            if ear < 0.21:
                blink_times.append(time.time())
                time.sleep(0.2)

                if len(blink_times) >= triple_count:
                    if blink_times[-1] - blink_times[-triple_count] <= time_limit:
                        cap.release()
                        cv2.destroyAllWindows()
                        return True

        cv2.imshow("Blink Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return False

# Audio command function
def listen_and_execute():
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    engine.say("Audio mode activated. I’m listening, melita")
    engine.runAndWait()

    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("Say something melita...")
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                command = recognizer.recognize_google(audio).lower()
                print(f"Command: {command}")

                if "i want to do shopping" in command:
                    engine.say("Opening Amazon.")
                    engine.runAndWait()
                    webbrowser.open("https://www.amazon.com")

                elif "open chrome" in command:
                    engine.say("Let me open Chrome for you.")
                    engine.runAndWait()
                    subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

                elif "play" in command:
                    song = command.replace("play", "").strip()
                    engine.say(f"Playing {song} on YouTube.")
                    engine.runAndWait()
                    pywhatkit.playonyt(song)

                elif "stop" in command:
                    engine.say("Alright, stopping audio mode.")
                    engine.runAndWait()
                    break

                else:
                    engine.say("I didn’t catch that, sorry.")
                    engine.runAndWait()

            except sr.UnknownValueError:
                engine.say("Speak clearly, melita.")
                engine.runAndWait()

            except sr.WaitTimeoutError:
                engine.say("You didn’t say anything, melita.")
                engine.runAndWait()

            except sr.RequestError:
                engine.say("Something’s wrong with your internet.")
                engine.runAndWait()

# Main flow
if __name__ == "__main__":
    if detect_blink():
        print("Triple blink detected .....Switching to audio mode...")
        listen_and_execute()

