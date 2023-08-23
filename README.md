# OpenCV Project - Virtual Quiz
---
#### This is an interactive multiple-choice question (MCQ) quiz application that uses hand gestures to answer questions. It utilizes the `cv2` (OpenCV) library along with the `cvzone` and `csv` modules to create an engaging quiz-taking experience.


## Features
- The quiz is presented as a series of questions with multiple-choice options.
- Users can use hand gestures to select their answers.
- A progress bar visually indicates the user's progress through the quiz.
- Upon completing the quiz, the user's score is displayed.

## Requirements
- Python 3.x
- OpenCV (`cv2`) library
- `cvzone` library
- `csv` library

## Usage
1. When the application starts, it accesses the webcam (usually ID 0).
2. The questions, choices, and correct answers are loaded from a CSV file named Quiz.csv.
3. Users can use their hand gestures to select the answers by hovering over the options.
4. The progress bar indicates the user's progress through the quiz.
5. Once the quiz is completed, the user's score is displayed

## Credits
- The hand detection and tracking functionality is provided by the cvzone.HandTrackingModule module.
- The cvzone library simplifies various computer vision tasks, including hand tracking and drawing.

---
