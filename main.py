import cv2
import pyttsx3
import time
import speech_recognition as sr

# Initialize voice engine
engine = pyttsx3.init()

# Load Haar cascades for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Start webcam
cap = cv2.VideoCapture(0)
blink_times = []

def speak(text):
    engine.say(text)
    engine.runAndWait()

def activate_audio_mode():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        speak("I'm listening to you...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            if "hi" in command:
                speak("hi, whats up?")
            elif "what are u doing" in command:
                speak("i am listening to u.....")
            else:
                speak("Mmm, didn’t catch that, say it again slow")
        except:
            speak("Oops, couldn’t hear you, try again later")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        if len(eyes) == 0:
            blink_times.append(time.time())
            blink_times = [t for t in blink_times if time.time() - t < 3]
            if len(blink_times) >= 3:
                speak("Audio mode activated")
                activate_audio_mode()
                blink_times.clear()

    cv2.imshow('Blink Detector', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
