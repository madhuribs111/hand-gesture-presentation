# Hand Gesture Presentation using Python and OpenCV 👋💻

This project is a Python-based application that allows users to control a slideshow presentation using hand gestures, powered by OpenCV and the `cvzone` library for hand tracking. By detecting hand gestures through a webcam, the application enables users to navigate through slides, draw annotations, erase them, and show a pointer, all without the need for a physical input device like a mouse or keyboard.

## Features 🎯

- **Hand Gesture Control**: 
    - Navigate slides with hand gestures:
        - Left swipe to go to the previous slide.
        - Right swipe to move to the next slide.
    - Show a pointer on the current slide by holding up two fingers.
    - Draw annotations using one finger, making presentations interactive.
    - Erase annotations using three fingers.
- **Seamless Slide Navigation**: Navigate between slides without touching your keyboard or mouse.
- **Real-Time Hand Detection**: Uses `cvzone` and OpenCV for accurate hand and finger detection.
- **Overlay Webcam Feed**: Displays the webcam feed on the current slide, making it useful for live presentations.

## How It Works 🛠️

1. **Gesture Detection**: 
    - The application uses a webcam feed to detect your hand using `cvzone.HandTrackingModule`.
    - Different gestures (e.g., number of raised fingers) are mapped to specific actions:
        - **Swipe Left**: Move to the previous slide.
        - **Swipe Right**: Move to the next slide.
        - **Two Fingers**: Show a pointer.
        - **One Finger**: Start drawing on the slide.
        - **Three Fingers**: Erase the most recent annotation.
2. **Slide Display**: 
    - The slides are stored in a local folder named `Presentation`, and they are displayed one by one based on the detected gestures.
    - The current slide is overlaid with the webcam feed in the corner for better interaction.
3. **Annotations**: You can draw on slides with gestures and save these annotations per slide.
4. **Webcam Integration**: The application captures the webcam feed and overlays it on the slides, which can be useful during virtual presentations.

### Prerequisites:
- Python 3.x
- OpenCV (`opencv-python`)
- `cvzone` (for hand detection)

