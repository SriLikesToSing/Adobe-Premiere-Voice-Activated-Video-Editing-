# Adobe Voice-Activated Video Editing

## Introduction

Welcome to the Adobe Voice-Activated Video Editing project! This project enhances video editing in Adobe Premiere Pro by integrating voice commands for various editing tasks. Below, you'll find information on how to set up and use the system.

<img src="https://github.com/SriLikesToSing/Adobe-Premiere-Voice-Activated-Video-Editing-/blob/master/Voice_Video_editor/demonstration2.gif">

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)

- [Usage](#usage)
  - [Voice Commands List](#Voice-Commands-List)

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- [Adobe Premiere Pro](https://www.adobe.com/products/premiere.html)
- [Python](https://www.python.org/downloads/) 
- [Google Cloud Speech-To-Text installation](https://cloud.google.com/speech-to-text/docs/speech-to-text-client-libraries#client-libraries-install-python) 

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/SriLikesToSing/Adobe-Premiere-Voice-Activated-Video-Editing-

2. Install the requirements using
   ```bash
   pip install -r requirements.txt

3. After downloading the google cloud services CLI locally and setting up credentials from [this link](https://cloud.google.com/docs/authentication/provide-credentials-adc), download enable the [speech to text API](https://console.cloud.google.com/marketplace/product/google/speech.googleapis.com?q=search&referrer=search)

4.  Edit the .bat file and change the path of main.exe and adobepremire.exe (wherever you stored it)

5.  double click on the .bat file and run.

## Voice Commands List

These commands are voice-activated. Simply speak the following phrases to control the application:

1. **"select"** - Presses the 'd' key.

2. **"unselect"** - Deselects by pressing 'Ctrl' + 'Shift' + 'a' keys.

3. **"frame"** - Navigates one frame forward using voice command.

4. **"back frame"** - Navigates one frame backward using voice command.

5. **"play"** or **"pause"** - Toggles play/pause with voice command.

6. **"cut"** - Cuts selected content with voice command.

7. **"previous"** - Goes back 5 seconds.

8. **"forward"** - Moves forward 5 seconds.

9. **"undo"** - undo's action.

10. **"save"** - Saves the current file using voice command.

11. **"quit"** or **"exit"** - Quits the program using voice command.

This is a minimum viable product. Meaning tons of specific word commands can be added to make complex edits.
  
