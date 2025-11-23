# 🎙️ Video Communication Analyzer

A powerful Python application that analyzes a speaker's communication skills from any public video URL. This project demonstrates a full-stack approach to AI, integrating media processing, speech-to-text, and large language model (LLM) analysis to provide actionable insights.

## ✨ Key Features

-   **Video URL Input:** Seamlessly accepts public video URLs from platforms like YouTube.
-   **Audio Extraction & Transcription:** Automatically downloads the video, extracts the audio, and transcribes it into a high-accuracy text transcript using OpenAI's Whisper.
-   **AI-Powered Analysis:** Leverages a local LLM to intelligently analyze the transcript and provide:
    -   **Clarity Score:** A numerical score (0-100%) that evaluates the speaker's fluency, grammar, and speaking pace.
    -   **Communication Focus:** A single, concise sentence summarizing the core topic of the video.
-   **Simple & Interactive UI:** A clean and user-friendly interface built with Streamlit for an excellent user experience.

## 🧠 Architectural Choice: A Cost-Effective & Private Approach

Many AI applications rely on paid cloud APIs (like OpenAI's GPT API) for analysis. While powerful, these services can be expensive and require managing sensitive API keys.

To demonstrate resourcefulness and build a self-sufficient solution, this application was designed to run **entirely on local hardware** using open-source models.

-   **No API Keys Needed:** By using `Ollama` to run the `llama3` model locally, this project completely eliminates the need for external API keys and recurring costs.
-   **Data Privacy:** All video and audio data is processed locally on the user's machine, ensuring complete privacy and data security.
-   **Offline Capability:** Once the models are downloaded, the core analysis functionality can work without an internet connection.

This choice highlights a practical and scalable approach to building AI-powered tools, making it an ideal solution for real-world applications where cost and privacy are major concerns.

## 🛠️ Tech Stack

-   **Backend:** Python
-   **AI & Machine Learning:**
    -   `Ollama` (for running local LLMs)
    -   `Whisper` (for Speech-to-Text)
    -   `llama3` (the LLM for analysis)
-   **Libraries:** `streamlit`, `yt-dlp`, `pydub`, `requests`
-   **Audio Processing:** `FFmpeg`

## 🚀 Getting Started: Setup Guide

Follow these steps to get the application running on your local machine.

### Prerequisites

-   Python 3.8 or higher
-   Git

### Step 1: Set Up the Local AI Engine (Ollama)

Ollama is the engine that runs our AI model.

1.  **Install Ollama:** Download and install the application for your operating system from [https://ollama.com/](https://ollama.com/).
2.  **Pull the AI Model:** After installation, open your Terminal (macOS) or Command Prompt/PowerShell (Windows) and run the following command to download the `llama3` model:
    ```bash
    ollama pull llama3
    ```
3.  **Verify Ollama is Running:** Run `ollama list` in your terminal. You should see `llama3` in the list if it was successful.

### Step 2: Set Up the Python Application

1.  **Clone this repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Create and activate a virtual environment:**
    -   **macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    -   **Windows:**
        ```bash
        python -m venv newenv
        .\venv\Scripts\activate
        ```

3.  **Install Python dependencies:**
    The `requirements.txt` file contains all the necessary Python libraries.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Install FFmpeg:**
    Whisper requires FFmpeg for audio processing.
    -   **macOS (using Homebrew):** `brew install ffmpeg`
    -   **Ubuntu/Debian:** `sudo apt update && sudo apt install ffmpeg`
    -   **Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add the `bin` folder to your system's PATH.

## ▶️ How to Run

1.  Ensure your Ollama application is running in the background.
2.  Make sure your virtual environment is active (you should see `(newenv)` in your terminal).
3.  Run the Streamlit app from your terminal:
    ```bash
    streamlit run app.py
    ```

The application will open in your web browser, typically at `http://localhost:8501`.

## 🌐 Deployment

To get a public link for this project:

1.  Push your code to a public GitHub repository.
2.  Go to [Streamlit Community Cloud](https://share.streamlit.io/).
3.  Connect your GitHub account and deploy the app, pointing to your `app.py` file.
4.  I designed the project to work fully offline using Whisper and yt_dlp.
This avoids expensive API costs and keeps user data private.
It runs completely on a local computer — no internet or API key required.
So the Streamlit Cloud version will only work partially because it blocks audio processing.
But on any local system, it works 100%.

## 📁 Project Structure

Your project folder should look like this:

```
video_analyzer/
├── app.py
├── requirements.txt
├── README.md
└── newenv/
    ... (virtual environment files)
```

