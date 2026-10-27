🏋️ Real-Time AI Gym Coach

An AI-powered fitness coaching application that uses real-time computer vision and pose estimation to help users monitor their workout form, track exercise repetitions, and maintain workout history.

📌 Overview

Real-Time AI Gym Coach is a Python-based fitness application designed to make workouts more interactive and data-driven. It uses MediaPipe Pose, OpenCV, and Streamlit to process video input and analyze body movements during exercise sessions.

The application tracks workout metrics and provides a foundation for personalized fitness guidance through AI-powered assistance.

✨ Features

Real-Time Pose Detection: Detects body landmarks from video input using MediaPipe.

Exercise Tracking: Supports exercise-specific monitoring, including squats, biceps curls, and shoulder presses.

Repetition Counting: Tracks repetitions using exercise-specific movement logic.

Workout Metrics: Displays exercise-related metrics and form indicators.

Workout Session History: Stores workout information and session records using SQLite.

Interactive Web Interface: Provides a user-friendly dashboard built with Streamlit.

AI-Powered Fitness Assistance: Integrates a Groq-hosted language model for conversational workout guidance.

Voice Interaction: Uses text-to-speech functionality to deliver spoken responses.

Modular Architecture: Separates exercise detection, application logic, services, and persistence components.

🛠️ Tech Stack

Technology

Purpose

Python

Core application development

Streamlit

Interactive web interface

MediaPipe

Pose estimation and body landmark detection

OpenCV

Video and image processing

streamlit-webrtc

Real-time video streaming

SQLite

Workout session and data persistence

Groq API

Language-model-powered fitness assistance

gTTS

Text-to-speech generation

Pandas

Data handling and processing

Git & GitHub

Version control and project hosting

🏗️ Project Architecture

The application follows a modular structure:

User Interface: Streamlit manages the dashboard and workout interaction.

Video Processing: streamlit-webrtc captures video frames for processing.

Pose Detection: MediaPipe identifies body landmarks, while OpenCV supports frame processing.

Exercise Analysis: Exercise-specific detector modules process movements and update workout metrics.

Data Persistence: SQLite stores user and workout session information.

AI and Voice Assistance: The Groq API generates responses, and gTTS converts supported responses into speech.
