Languages: [日本語](README_ja.md) | [English](README.md) 


# LLM-YOLO-Robotic-Arm
Robotic arm system powered by LLM (ChatGPT) and YOLO for voice-controlled object manipulation.

# Introduction
We are an interdisciplinary team dedicated to exploring the integration of generative AI with Japan’s traditional automation technologies.
The goal of this project is to combine ChatGPT, YOLO, and inverse kinematics to enable a robotic arm to understand natural language commands and execute appropriate actions in coordination with Japan’s advanced automation systems.
The main research themes include:
Natural Language Processing (NLP): Semantic analysis using large language models (LLMs)
Computer Vision (CV): Object recognition using YOLO
Robot Control: Motion calculation of a robotic arm through inverse kinematics
Human-Robot Interaction: Optimization of voice input and action instructions



#  Agent-SKYNET
Sky Net is a modular software agent developed by our team to bridge large language models (LLMs) and real-world robotic control.
Acting as an intelligent interface between natural language and machine execution, Sky Net uses ChatGPT as its core reasoning engine. Upon receiving voice or text commands, the agent performs semantic parsing, context understanding, and decision-making. It then coordinates with the perception module (YOLO object detection) and the control layer (inverse kinematics, servo drivers) to execute the appropriate physical actions via a 6-DOF robotic arm.
This architecture allows real-time, intuitive human-robot interaction, enabling language-driven manipulation tasks in real environments. Sky Net represents a step toward embodied AI — where machines not only understand language but act meaningfully in the physical world.

# Overview
LLM-Robotic-Arm integrates object detection (YOLO) and LLM-based natural language understanding (ChatGPT) to enable voice-guided control of a 6-DOF robotic arm. The system supports real-time object detection, socket-based communication, and inverse kinematics for precise motion execution.

# Features

- Voice-based object manipulation  
- YOLO-powered real-time object detection  
- LLM (ChatGPT) for natural language understanding  
- Raspberry Pi-based deployment  
- Inverse kinematics and servo control  
 
# Team

This project is organized by an interdisciplinary team of doctoral and master's students, with each member contributing based on their respective areas of expertise.

- **Hang Xingchen (Project Lead)** – Specializes in robotic arm control, inverse kinematics, YOLO integration, and LLM-based system design. Former research assistant with experience in government presentations.
  *Kobe University.*
  
- **Haruki Maruyama**  –  In charge of prompt design and adjustment of dialogue style in Japanese. Supports the generation of natural Japanese responses and understanding of cultural context.
  *The University of Tokyo.*

- **Li Tianyang** – Responsible for 3D modeling (CAD/SolidWorks), robot mechanical design, and prototyping. Also works on YOLO-based object grasping and inverse kinematics tuning.
  *Kobe University.*

- **Sun Yushan** – Focuses on system integration, socket communication, and backend development.  
  *Kobe University.*

- **Sun Yan** – Researcher in human behavior and robotic interaction, contributing to the behavioral logic behind the system.  
  *Kobe University.*

- **Jiang Qilong** – In charge of the Streamlit interface and user interaction design, ensuring smooth UI/UX experience.  
  *Background in design and software engineering.*

We are committed to building intelligent and accessible robotic systems, with experience in academic research, competitive robotics, and early-stage commercialization.

## Demo Video SKYNET-5
https://www.youtube.com/watch?v=69e78PqmeNM&t=3s
[This version of the system demonstrates basic language understanding capabilities, allowing the robotic arm to interpret simple human commands and respond with corresponding physical actions.]

## Demo Video  SKYNET-6
https://www.youtube.com/watch?v=lS7rUFcXonQ
[In this version, the large language model is guided to learn from human behavior, robotic cognition, and psychology, simulating aspects of human-like consciousness. It also incorporates understanding of Japanese honorific language.]

## Demo Video  SKYNET-6.1
https://www.youtube.com/watch?v=jr8Sl4M8Fsw
[This version of the system adds voice control]

## Demo Video  SKYNET-8
https://www.youtube.com/watch?v=Eo-8q8rrNC4
[This version also incorporates YOLO-based object detection and inverse kinematics, enabling the system to recognize simple objects and perform basic grasping actions based on their detected coordinates.]

## Demo Video  SKYNET-10
[https://www.youtube.com/watch?v=Eo-8q8rrNC4](https://www.youtube.com/watch?v=zrWmjCPV1bM)
[
The latest version of our system, SKYNET 10, marks the official release of a stable model built upon our previous proof-of-concept version. Compared to the initial prototype, SKYNET 10 delivers significant technological advancements and system-level optimizations across multiple domains.

Local Deployment of Large Language Model (LLM)
The previously cloud-based ChatGPT API has been completely replaced with a lightweight, locally deployed LLM model. Additionally, we have developed a domain-specific prompt system to dramatically improve system stability, response speed, and privacy protection—ensuring reliable performance even in offline environments.

On-Device ASR and TTS Modules
The system is now fully independent from external APIs. Both Automatic Speech Recognition (ASR) and Text-to-Speech (TTS) are processed locally, enabling enhanced real-time responsiveness, multi-language support, and customizable voice synthesis for more natural and flexible voice interaction.

Proprietary User Interface (UI)
To enhance usability and user experience, a custom-built UI interface has been implemented. It allows for real-time control of multiple system parameters, offering a more intuitive and interactive user environment tailored to various use cases.

Distributed Architecture: Master & Slave Systems
SKYNET 10 adopts a distributed architecture consisting of a master system and a slave system.

The master system is responsible for natural language understanding, speech processing, overall system orchestration, and also executes YOLO-based visual object recognition, enabling intelligent decision-making by integrating both spoken and visual inputs.

The slave system, running on a Raspberry Pi, handles real-time robotic arm control, inverse kinematics computation, and direct actuator execution. This architecture ensures high responsiveness and modular deployment flexibility.]





# Notice 
Full source code is not publicly available.  
Please contact us directly for further discussion or collaboration.
