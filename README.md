# F.A.L.C.O. — Fully Adaptive Liaison and Companion Oracle

[![Python](https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![OpenAI GPT-4](https://img.shields.io/badge/LLM-GPT--4-412991?logo=openai&logoColor=white)](https://openai.com/)
[![OpenAI Whisper](https://img.shields.io/badge/STT-Whisper-412991?logo=openai&logoColor=white)](https://github.com/openai/whisper)
[![Piper TTS](https://img.shields.io/badge/TTS-Piper-00B4AB)](https://github.com/rhasspy/piper)
[![Live2D](https://img.shields.io/badge/Avatar-Live2D%20%2F%20VTube%20Studio-FF4081)](https://www.live2d.com/)

> **F.A.L.C.O. (Fully Adaptive Liaison and Companion Oracle)** is an intelligent virtual assistant (IVA) system designed to combine functional task support with emotional companionship.

Unlike conventional virtual assistants that focus solely on task execution and lack a distinct personality or visual embodiment, F.A.L.C.O. integrates speech recognition (OpenAI Whisper), natural language processing (OpenAI GPT-4), real-time multilingual translation (Google Translate API), expressive text-to-speech synthesis (Piper TTS), and a lip-synced Live2D animated avatar. The system is built to support human-centered AI interaction and offer simulated companionship alongside practical everyday assistance.

---

## ✨ Key Features

* **Context-Aware NLP:** Uses OpenAI GPT-4 to conduct context-aware dialogue and generate human-like responses.
* **Speech Recognition (STT):** Integrates OpenAI Whisper to convert spoken user input into accurate transcribed text.
* **Expressive Text-to-Speech (TTS):** Implements Piper TTS to synthesize natural and expressive vocal output.
* **Automatic Multilingual Translation:** Incorporates the Google Translate API to handle multilingual input and output independent of the core NLP model.
* **Live2D Digital Embodiment:** Synchronizes avatar lip movements (`uLipSync`) with synthesized speech in VTube Studio for immersive visual interaction.
* **Adaptive Personality Engine:** Adjusts the assistant's conversational tone and behavior (e.g., friendly, formal, or casual) to match user preferences.
* **Short-Term Conversational Memory:** Retains context across exchanges and logs conversation history to maintain continuity and familiarity.
* **Streaming-Ready OBS Layout:** Organizes transcribed input, the central Live2D avatar, and generated response subtitles (formatted up to 10 words per line) within OBS Studio.

---

## 🛠️ Tech Stack

* **Language:** Python (modular components for STT, dialogue generation, translation, and TTS)
* **Large Language Model & Evaluation:** OpenAI GPT-4 API, OpenAI Evals
* **Speech-to-Text (STT):** OpenAI Whisper
* **Text-to-Speech (TTS):** Piper TTS
* **Translation:** Google Translate API
* **Avatar & Lip-Sync:** Live2D, VTube Studio (`uLipSync`)
* **Audio Routing & Display:** Virtual Audio Cable, OBS Studio

---

## 🏗️ System Architecture & Workflow

F.A.L.C.O. processes interactions across three core layers:

### 1. Input Layer
* **Audio Capture:** Microphone speech input is routed through a Virtual Audio Cable into the Speech Recognition module.
* **Transcription & Identity Setup:** While defining the IVA's identity and personalities, OpenAI Whisper splits incoming audio into 30-second chunks, converts it into a log-Mel spectrogram, predicts tokens, and saves the completed transcription as a temporary `.txt` file.

### 2. Processing Layer
* **Dialogue Generation:** The transcribed text is sent as a prompt to the OpenAI GPT-4 API, which applies identity and short-term memory context to generate a response.
* **Translation:** When cross-language output is needed, the Google Translate API converts the response into the target language and saves the output as a temporary `.txt` file.

### 3. Output Layer
* **Speech Synthesis:** Piper TTS normalizes and tokenizes the text, maps graphemes to phonemes, and converts Mel-spectrograms into an audio waveform (automatically downloading the voice model on first run).
* **Avatar Lip Synchronization:** The TTS audio output is routed through a Virtual Audio Cable into VTube Studio as a microphone input to drive `uLipSync` and avatar rendering.
* **OBS Studio Presentation & Logging:** Audio, rendered avatar video, and formatted `.txt` overlays are channeled into OBS Studio, after which the system saves the conversation history and deletes the temporary input/output `.txt` files.

---

## 🖥️ OBS Studio Visual Layout

The visual interface in OBS Studio follows a vertical hierarchy designed for readability and user engagement:
1. **Top (`Transcribed Input`):** Displays the user's spoken query transcribed by the STT module, formatted into lines of up to 10 words.
2. **Center (`Live2D Avatar`):** Positions the digital avatar at the center of the canvas as the primary visual focal point.
3. **Bottom (`Generated Response`):** Displays the assistant's reply below the avatar, formatted into lines of up to 10 words.

---

## 🚀 Getting Started

### Prerequisites
* **Python 3.x** installed on your system.
* **API Keys:** OpenAI API key (with GPT-4 access) and Google Translate API credentials.
* **External Software:**
  * **Virtual Audio Cable** for routing microphone and TTS audio streams.
  * **VTube Studio** with a configured Live2D model and `uLipSync` enabled.
  * **OBS Studio** for scene composition and dynamic text overlays.

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Rheno25/Fully-Adaptive-Liaison-and-Companion-Oracle.git](https://github.com/Rheno25/Fully-Adaptive-Liaison-and-Companion-Oracle.git)
   cd Fully-Adaptive-Liaison-and-Companion-Oracle
   ```

2. **Configure API credentials and prompts:**
   * Set up your OpenAI GPT-4 and Google Translate API keys in your configuration.
   * Define the assistant's persona and conversational style (friendly, formal, or casual) in the prompt templates.

3. **Configure audio routing:**
   * Route your microphone input and Piper TTS output via Virtual Audio Cable so VTube Studio receives the synthesized speech as its microphone input.

4. **Set up OBS Studio:**
   * Add your VTube Studio capture to the center of the scene.
   * Add two text sources linked to the dynamic input and output `.txt` files for **"Transcribed Input"** (top) and **"Generated Response"** (bottom).

---

## 📊 Evaluation & Performance Results

F.A.L.C.O. was evaluated with 12 participants across four testing dimensions:

### 1. Primary Functionality (User Acceptance Testing)
Achieved an average UAT success rate of **87.52%** across six core scenarios:

| Test Scenario | Expected Result | Success Rate | Status |
| :--- | :--- | :---: | :---: |
| **Speech-to-Text** | Converts spoken query into text accurately | 91.7% | Success |
| **Intent Identification** | Identifies user intent correctly from spoken query | 91.7% | Success |
| **Contextual Response** | Provides contextually appropriate response (e.g., weather forecast) | 91.7% | Success |
| **Noise Robustness** | Processes queries with minimal errors when background noise is present | 91.7% | Success |
| **Avatar Lip-Sync** | Matches avatar lip movements with speech output | 83.3% | Success |
| **Query Latency** | Processes queries within 2 seconds | 75.0% | Success |

### 2. Personality Embodiment (OpenAI Evals)
* Tested using **OpenAI Evals** across 100 scenario-based multiple-choice prompts in JSONL format validated by a psychology expert.
* Achieved **88% accuracy** in maintaining consistent personality traits (12 ideal matches, 76 partial matches, and 12 failures).

### 3. Avatar Integration
* Achieved a **70.00% average integration score**:
  * **Perceived Engagement:** 80.00% (Score: 48)
  * **Comprehension Enhancement:** 68.33% (Score: 41)
  * **Aesthetic & Branding Impact:** 61.67% (Score: 37)

### 4. Companionship Interaction Evaluation Metric (CIEM)
Achieved a total CIEM score of **16.50** (indicating good companionship interaction capabilities):

| Test Criteria | Description | Total Score | Average Score |
| :--- | :--- | :---: | :---: |
| **Conversational Coherence** | Retains context across multiple exchanges | 48 | 4.00 / 5 |
| **Emotional Appropriateness** | Responds emotionally to user input | 40 | 3.33 / 5 |
| **Conversation Length** | Number of turns sustained before repetition | 40 | 3.33 / 5 |
| **Perceived Engagement** | Subjective rating of engagement and emotional support | 70 | 5.83 / 10 |
| **Total CIEM Score** | Combined companionship evaluation score | — | **16.50** |

---

## 🗺️ Future Roadmap

* **Richer Avatar Expressiveness:** Expand nonverbal cues and facial expressions beyond lip synchronization.
* **Latency Optimization:** Reduce end-to-end processing time to consistently respond under 2 seconds.
* **Persistent Long-Term Memory:** Introduce cross-session memory and adaptive personality development.
* **Fine-Tuned Translation:** Upgrade translation accuracy with context-aware or fine-tuned models.
* **Expanded Use Cases:** Apply the framework to education, therapy, and empathy-driven customer service.

---

## 👥 Authors & Acknowledgements

* **Authors:** Yoppy Yunhasnawa, Irsyad Arif Mashudi, and Rheno Rayhan Fayyaz Dhana Pramudya
* **Institution:** Department of Information Technology, State Polytechnic of Malang, Malang, East Java, Indonesia
* **Acknowledgements:** Sincere gratitude to Ms. Alviony Ave Yunan Firdaus Susanto (Psychology graduate, State University of Surabaya) for her collaboration during the personality evaluation phase, and to the 12 participants who took part in testing F.A.L.C.O.
