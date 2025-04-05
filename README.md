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
This project is jointly developed by researchers from Kobe University, The University of Tokyo, and other institutions.


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

This project is developed by a multidisciplinary team of robotics researchers and engineers.

- **Hang Xingchen (Project Lead)** – Specializes in robotic arm control, inverse kinematics, YOLO integration, and LLM-based system design. Former research assistant with experience in government presentations and international collaboration. Recipient of JST recommendation.  
  *Master’s student, Kobe University.*

- **Li Tianyang** – Responsible for 3D modeling (CAD/SolidWorks), robot mechanical design, and prototyping. Also works on YOLO-based object grasping and inverse kinematics tuning.
  *Master’s student, Kobe University.*

- **Sun Yushan** – Focuses on system integration, socket communication, and backend development.  
  *Master’s student, Kobe University.*

- **Sun Yan** – Researcher in human behavior and robotic interaction, contributing to the behavioral logic behind the system.  
  *Ph.D. student, Kobe University.*

- **Haruki Maruyama** – Responsible for Japanese cultural adaptation of prompts in the project.  
  *Faculty of Liberal Arts, The University of Tokyo.*

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

# Notice
This repository is part of a job-seeking and partnership portfolio.  
Full source code is not publicly available.  
Please contact us directly for further discussion or collaboration.
