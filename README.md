# F.A.L.C.O. — Fully Adaptive Liaison and Companion Oracle

[![Python](https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![OpenAI GPT-4](https://img.shields.io/badge/LLM-GPT--4-412991?logo=openai&logoColor=white)](https://openai.com/)
[![OpenAI Whisper](https://img.shields.io/badge/STT-Whisper-412991?logo=openai&logoColor=white)](https://github.com/openai/whisper)
[![Piper TTS](https://img.shields.io/badge/TTS-Piper-00B4AB)](https://github.com/rhasspy/piper)
[![Live2D](https://img.shields.io/badge/Avatar-Live2D%20%2F%20VTube%20Studio-FF4081)](https://www.live2d.com/)

> **F.A.L.C.O. (Fully Adaptive Liaison and Companion Oracle)** is an intelligent virtual assistant (IVA) system designed to combine functional task support with emotional companionship[cite: 2, 3].

Unlike conventional virtual assistants that focus solely on task execution and lack a distinct personality or visual embodiment, F.A.L.C.O. integrates speech recognition (OpenAI Whisper), natural language processing (OpenAI GPT-4), real-time multilingual translation (Google Translate API), expressive text-to-speech synthesis (Piper TTS), and a lip-synced Live2D animated avatar[cite: 2, 3]. The system is built to support human-centered AI interaction and offer simulated companionship alongside practical everyday assistance[cite: 2, 3].

---

## ✨ Key Features

* **Context-Aware NLP:** Uses OpenAI GPT-4 to conduct context-aware dialogue and generate human-like responses[cite: 3, 4].
* **Speech Recognition (STT):** Integrates OpenAI Whisper to convert spoken user input into accurate transcribed text[cite: 2, 3].
* **Expressive Text-to-Speech (TTS):** Implements Piper TTS to synthesize natural and expressive vocal output[cite: 3, 5].
* **Automatic Multilingual Translation:** Incorporates the Google Translate API to handle multilingual input and output independent of the core NLP model[cite: 3].
* **Live2D Digital Embodiment:** Synchronizes avatar lip movements (`uLipSync`) with synthesized speech in VTube Studio for immersive visual interaction[cite: 3, 5].
* **Adaptive Personality Engine:** Adjusts the assistant's conversational tone and behavior (e.g., friendly, formal, or casual) to match user preferences[cite: 3].
* **Short-Term Conversational Memory:** Retains context across exchanges and logs conversation history to maintain continuity and familiarity[cite: 3, 5].
* **Streaming-Ready OBS Layout:** Organizes transcribed input, the central Live2D avatar, and generated response subtitles (formatted up to 10 words per line) within OBS Studio[cite: 5].

---

## 🛠️ Tech Stack

* **Language:** Python (modular components for STT, dialogue generation, translation, and TTS)[cite: 4]
* **Large Language Model & Evaluation:** OpenAI GPT-4 API, OpenAI Evals[cite: 4, 5]
* **Speech-to-Text (STT):** OpenAI Whisper[cite: 2, 5]
* **Text-to-Speech (TTS):** Piper TTS[cite: 3, 5]
* **Translation:** Google Translate API[cite: 3, 5]
* **Avatar & Lip-Sync:** Live2D, VTube Studio (`uLipSync`)[cite: 3, 5]
* **Audio Routing & Display:** Virtual Audio Cable, OBS Studio[cite: 5]

---

## 🏗️ System Architecture & Workflow

F.A.L.C.O. processes interactions across three core layers[cite: 5]:

### 1. Input Layer
* **Audio Capture:** Microphone speech input is routed through a Virtual Audio Cable into the Speech Recognition module[cite: 5].
* **Transcription & Identity Setup:** While defining the IVA's identity and personalities, OpenAI Whisper splits incoming audio into 30-second chunks, converts it into a log-Mel spectrogram, predicts tokens, and saves the completed transcription as a temporary `.txt` file[cite: 5].

### 2. Processing Layer
* **Dialogue Generation:** The transcribed text is sent as a prompt to the OpenAI GPT-4 API, which applies identity and short-term memory context to generate a response[cite: 5].
* **Translation:** When cross-language output is needed, the Google Translate API converts the response into the target language and saves the output as a temporary `.txt` file[cite: 5].

### 3. Output Layer
* **Speech Synthesis:** Piper TTS normalizes and tokenizes the text, maps graphemes to phonemes, and converts Mel-spectrograms into an audio waveform (automatically downloading the voice model on first run)[cite: 5].
* **Avatar Lip Synchronization:** The TTS audio output is routed through a Virtual Audio Cable into VTube Studio as a microphone input to drive `uLipSync` and avatar rendering[cite: 5].
* **OBS Studio Presentation & Logging:** Audio, rendered avatar video, and formatted `.txt` overlays are channeled into OBS Studio, after which the system saves the conversation history and deletes the temporary input/output `.txt` files[cite: 5].

---

## 🖥️ OBS Studio Visual Layout

The visual interface in OBS Studio follows a vertical hierarchy designed for readability and user engagement[cite: 5]:
1. **Top (`Transcribed Input`):** Displays the user's spoken query transcribed by the STT module, formatted into lines of up to 10 words[cite: 5].
2. **Center (`Live2D Avatar`):** Positions the digital avatar at the center of the canvas as the primary visual focal point[cite: 5].
3. **Bottom (`Generated Response`):** Displays the assistant's reply below the avatar, formatted into lines of up to 10 words[cite: 5].

---

## 🚀 Getting Started

### Prerequisites
* **Python 3.x** installed on your system[cite: 4].
* **API Keys:** OpenAI API key (with GPT-4 access) and Google Translate API credentials[cite: 4, 5].
* **External Software:**
  * **Virtual Audio Cable** for routing microphone and TTS audio streams[cite: 5].
  * **VTube Studio** with a configured Live2D model and `uLipSync` enabled[cite: 3, 5].
  * **OBS Studio** for scene composition and dynamic text overlays[cite: 5].

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Rheno25/Fully-Adaptive-Liaison-and-Companion-Oracle.git](https://github.com/Rheno25/Fully-Adaptive-Liaison-and-Companion-Oracle.git)
   cd Fully-Adaptive-Liaison-and-Companion-Oracle
   ```

2. **Configure API credentials and prompts:**
   * Set up your OpenAI GPT-4 and Google Translate API keys in your configuration[cite: 4, 5].
   * Define the assistant's persona and conversational style (friendly, formal, or casual) in the prompt templates[cite: 3, 4].

3. **Configure audio routing:**
   * Route your microphone input and Piper TTS output via Virtual Audio Cable so VTube Studio receives the synthesized speech as its microphone input[cite: 5].

4. **Set up OBS Studio:**
   * Add your VTube Studio capture to the center of the scene[cite: 5].
   * Add two text sources linked to the dynamic input and output `.txt` files for **"Transcribed Input"** (top) and **"Generated Response"** (bottom)[cite: 5].

---

## 📊 Evaluation & Performance Results

F.A.L.C.O. was evaluated with 12 participants across four testing dimensions[cite: 2, 4, 6]:

### 1. Primary Functionality (User Acceptance Testing)
Achieved an average UAT success rate of **87.52%** across six core scenarios[cite: 6, 7]:

| Test Scenario | Expected Result | Success Rate | Status |
| :--- | :--- | :---: | :---: |
| **Speech-to-Text** | Converts spoken query into text accurately[cite: 6] | 91.7%[cite: 6] | Success[cite: 6] |
| **Intent Identification** | Identifies user intent correctly from spoken query[cite: 6] | 91.7%[cite: 6] | Success[cite: 6] |
| **Contextual Response** | Provides contextually appropriate response (e.g., weather forecast)[cite: 6] | 91.7%[cite: 6] | Success[cite: 6] |
| **Noise Robustness** | Processes queries with minimal errors when background noise is present[cite: 6] | 91.7%[cite: 6] | Success[cite: 6] |
| **Avatar Lip-Sync** | Matches avatar lip movements with speech output[cite: 6] | 83.3%[cite: 6] | Success[cite: 6] |
| **Query Latency** | Processes queries within 2 seconds[cite: 6] | 75.0%[cite: 6] | Success[cite: 6] |

### 2. Personality Embodiment (OpenAI Evals)
* Tested using **OpenAI Evals** across 100 scenario-based multiple-choice prompts in JSONL format validated by a psychology expert[cite: 4, 6].
* Achieved **88% accuracy** in maintaining consistent personality traits (12 ideal matches, 76 partial matches, and 12 failures)[cite: 2, 6].

### 3. Avatar Integration
* Achieved a **70.00% average integration score**[cite: 6]:
  * **Perceived Engagement:** 80.00% (Score: 48)[cite: 6]
  * **Comprehension Enhancement:** 68.33% (Score: 41)[cite: 6]
  * **Aesthetic & Branding Impact:** 61.67% (Score: 37)[cite: 6]

### 4. Companionship Interaction Evaluation Metric (CIEM)
Achieved a total CIEM score of **16.50** (indicating good companionship interaction capabilities)[cite: 5, 7]:

| Test Criteria | Description | Total Score | Average Score |
| :--- | :--- | :---: | :---: |
| **Conversational Coherence** | Retains context across multiple exchanges[cite: 7] | 48[cite: 7] | 4.00 / 5[cite: 6, 7] |
| **Emotional Appropriateness** | Responds emotionally to user input[cite: 7] | 40[cite: 7] | 3.33 / 5[cite: 6, 7] |
| **Conversation Length** | Number of turns sustained before repetition[cite: 7] | 40[cite: 7] | 3.33 / 5[cite: 6, 7] |
| **Perceived Engagement** | Subjective rating of engagement and emotional support[cite: 7] | 70[cite: 7] | 5.83 / 10[cite: 6, 7] |
| **Total CIEM Score** | Combined companionship evaluation score[cite: 7] | — | **16.50**[cite: 7] |

---

## 🗺️ Future Roadmap

* **Richer Avatar Expressiveness:** Expand nonverbal cues and facial expressions beyond lip synchronization[cite: 2, 7].
* **Latency Optimization:** Reduce end-to-end processing time to consistently respond under 2 seconds[cite: 6, 7].
* **Persistent Long-Term Memory:** Introduce cross-session memory and adaptive personality development[cite: 2, 7].
* **Fine-Tuned Translation:** Upgrade translation accuracy with context-aware or fine-tuned models[cite: 7].
* **Expanded Use Cases:** Apply the framework to education, therapy, and empathy-driven customer service[cite: 2, 7].

---

## 👥 Authors & Acknowledgements

* **Authors:** Yoppy Yunhasnawa, Irsyad Arif Mashudi, and Rheno Rayhan Fayyaz Dhana Pramudya[cite: 1]
* **Institution:** Department of Information Technology, State Polytechnic of Malang, Malang, East Java, Indonesia[cite: 1]
* **Acknowledgements:** Sincere gratitude to Ms. Alviony Ave Yunan Firdaus Susanto (Psychology graduate, State University of Surabaya) for her collaboration during the personality evaluation phase, and to the 12 participants who took part in testing F.A.L.C.O.[cite: 1]
