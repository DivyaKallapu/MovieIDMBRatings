"""
Author: Divya kallapu

This script converts speech to text and text to speech
Given a movie name via voice (microphone) it outputs the IDMB rating of the movie
"""

import speech_recognition as sr
import pyttsx3
from pythonProject.extract_ratings import GetRating

# Initialize the recognizer
r = sr.Recognizer()


# Function to convert text to
# speech
def text_to_audio(command):
    """
    Converts text to speech using pyttsx module in python
    :type command: str
    :return: text to speech
    """
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

try:
    # use the default microphone as the audio source
    with sr.Microphone() as source:

        # wait for 0.2 second to let the recognizer adjust the energy threshold based on
        # the surrounding noise level to catch speech right away
        r.adjust_for_ambient_noise(source, duration=0.2)

        # listen for user's input
        print("Which movie rating would you like to know?")
        text_to_audio("Which movie rating would you like to know?")
        audio = r.listen(source)

        # Google web speech api to recognize audio
        movie_name = r.recognize_google(audio)
        movie_name = movie_name.lower()

        print("Did you say " + movie_name)
        text_to_audio("Did you say " + movie_name)

        audio2 = r.listen(source)
        response = r.recognize_google(audio2)
        if response.lower() == "no":
            text_to_audio("Sorry! I didn't get the movie name please type it out here")
            movie_name = input("Sorry! I didn't get the movie name please type it out here: ")

        # Create GetRating object to get rating of given movie
        get_rating_obj = GetRating(movie_name)
        rating = get_rating_obj.get_rating()
        output = "Rating of {} is {}".format(movie_name, rating)
        print(output)
        text_to_audio(output)

except sr.RequestError as error:
    print("Unable to request the results {0}".format(error))

except sr.UnknownValueError:
    print("An unknown error occurred")
