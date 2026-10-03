Languages: [日本語](README_ja.md) | [English](README.md)

# LLM-YOLO-Robotic-Arm

## A Hierarchical Robotic Manipulation System Integrating Visual Perception, Geometric Information, and LLMs/VLMs

**Select a target, assess occlusion, and translate decisions into physical robot actions.**

This project is a research prototype for a 5-DOF robot arm, built on conventional embedded robot-arm control and extended with image recognition and higher-level decision-making using LLMs/VLMs.

The robot arm’s mechanical structure, kinematics, and embedded control form the core of the system. YOLO-based visual perception and LLM/VLM-based instruction understanding, target selection, and occlusion assessment are integrated as higher-level functions.

Rather than allowing LLMs/VLMs to directly control the robot, the system connects their high-level decisions to coordinate transformations, inverse kinematics, and servo control. This supports target selection among multiple objects and the execution of grasping and occluder-removal actions on the physical robot.

This README focuses on the hierarchical architecture of **SKYNET-16**, introducing the system design, individual responsibilities, development history, and scope of the publicly available information.

| Item | Description |
| :--- | :--- |
| Main application | Object manipulation and grasping with a robot arm |
| Research focus | Target selection among multiple objects, occlusion assessment using geometric information, and connecting decisions to physical robot actions |
| High-level decision-making | Instruction understanding, target selection, and action-strategy decisions using LLMs/VLMs |
| Physical execution | Coordinate transformations, inverse kinematics, Raspberry Pi, and servo control |
| Public release | A technical portfolio centered on research descriptions and physical demonstrations; some source code is not publicly available |

**[Watch the SKYNET-16 demonstration](https://www.youtube.com/watch?v=7S0SW6Wzqks)** · **[Watch the multi-object target-selection demonstration](https://www.youtube.com/watch?v=l8yuPjlxAhg)**

---

## 1. Research Objectives

Robot-arm manipulation is organized around three questions:

1. **What should the robot manipulate?** Select the target using natural-language instructions and visual information.
2. **Can the target be manipulated directly?** Examine the spatial relationships between the target and surrounding objects to determine whether an occluding object needs to be removed first.
3. **How should the decision be translated into motion?** Pass the selected target and action strategy to the physical robot through coordinate transformations and inverse kinematics.

The research focuses not on conversation with an LLM itself, but on **connecting perception, decision-making, and motion within a robot-arm manipulation system**.

Early versions examined the connection between language instructions and physical actions. Subsequent versions extended the system to vision-guided grasping, target selection among multiple candidates, and occlusion assessment using geometric information.

---

## 2. Featured Demonstration: SKYNET-16

**[Open the demonstration video](https://www.youtube.com/watch?v=7S0SW6Wzqks)**

SKYNET-16 does not treat an LLM/VLM as a single end-to-end controller. Instead, it uses LLMs/VLMs as higher-level reasoning components for target selection and occlusion assessment. An execution layer handles the subsequent motion calculations using coordinate transformations and inverse kinematics.

### Layer 1 — Target Selection and Feature Interpretation

YOLO detection results and image information are used to examine object categories, visual characteristics, and suitability as manipulation targets.

LLMs/VLMs receive the user’s instructions and target-selection criteria to select an object from multiple candidates. Prompt design is used to make the selected target and the reasons for that selection explicit.

### Layer 2 — Occlusion and Obstacle Assessment Using Geometric Information

After selecting a target, the system examines its spatial relationships with surrounding objects. Rather than relying solely on unconstrained reasoning over images, this stage uses the following structured inputs:

- Whether the target object’s center point is covered.
- Relative spatial relationships between objects.
- Bounding-box overlap.

LLMs/VLMs reference these geometric inputs together with image information to assess whether the target is occluded and whether an occluding object should be removed before grasping.

This stage addresses **occlusion assessment using relationships in the image plane**. It does not demonstrate full-robot collision checking in three-dimensional space or guarantee the safety of a motion path.

### Layer 3 — Physical Execution Through Coordinate Transformations and Inverse Kinematics

The position of the selected target or occluding object is transformed into the robot coordinate frame. Inverse kinematics is then used to calculate joint angles. These results are passed to the control layer to carry out grasping or occluder-removal actions.

This division of responsibilities **separates high-level decisions from the calculations and control processes that move the physical robot**.

---

## 3. System Architecture

### 3.1 Processing Flow from Perception to Execution

```text
User voice / text instruction          Camera image
             |                             |
             |                    YOLO object detection
             |                             |
             +--------------+--------------+
                            |
                            v
              LLM/VLM-based target selection
                            |
                            v
           Occlusion / action-strategy assessment
                 using geometric information
                            |
                            v
                 Coordinate transformations
                            |
                            v
                     Inverse kinematics
                            |
                            v
              Servo control / robot-arm motion
```

**Perception → Reasoning → Decision → Execution**

The diagram is a conceptual representation of the processing flow. It does not show every implementation-level call sequence or all details of post-execution observation, success assessment, and retry handling.

### 3.2 Role of Agent-SKYNET

Agent-SKYNET is a modular software agent that connects natural-language instructions, visual perception, high-level decision-making, and robot control.

It receives voice or text instructions and coordinates LLM/VLM-based decision processes, YOLO-based perception, communication with hardware, and action execution.

In this project, the agent is positioned not as a single model that directly controls every aspect of the robot, but as **a software layer that connects perception, decision-making, and execution modules**.

### 3.3 Division of Responsibilities Between the Host and Embedded Controller

During the development of SKYNET-10, the system adopted a separation between a host computer and an embedded controller.

| Component | Main responsibilities |
| :--- | :--- |
| Host computer | Voice/text input, user interface, YOLO-based image recognition, language understanding and decision-making, and overall system coordination |
| Communication | Information exchange between the host and embedded controller through socket communication |
| Embedded controller: Raspberry Pi | Robot motion control, inverse-kinematics calculations, and execution of actuator commands |
| Physical hardware | A 5-DOF robot arm, gripper, and servo drive system |

This architecture separates perception, interaction, and decision-making from physical motion execution, allowing the modules to be developed and adjusted individually.

### 3.4 Technologies and Differences Between Versions

| Area | Technologies and processing |
| :--- | :--- |
| Object recognition | YOLO-based image recognition; detection coordinates, confidence scores, and visual information from images |
| High-level decision-making | LLMs/VLMs, prompt design, target selection, and occlusion assessment |
| Output and communication | Structured JSON selection results and socket communication |
| Kinematics and control | Coordinate transformations, inverse kinematics, and servo control |
| Hardware implementation | Raspberry Pi and a distributed host/embedded-controller architecture |
| User interface | Speech recognition, speech synthesis, and a Streamlit UI |
| Mechanical design and prototyping | CAD, SolidWorks, mechanical design, and prototyping |

Early versions used ChatGPT. SKYNET-10 explored a transition to a local LLM and local speech processing, while SKYNET-11 and SKYNET-16 introduce decision-making using LLMs/VLMs that process visual information.

**Model and speech-processing configurations must be distinguished by version.** This README does not specify the model names, API usage, or conditions for fully offline operation in SKYNET-11 or SKYNET-16. The description of local processing in SKYNET-10 should not be treated as a specification shared by all subsequent versions.

---

## 4. Individual Responsibilities and Team Development

My work centers on the robot arm, with responsibilities in the following areas:

- **Robot-arm control and inverse kinematics:** Development of motion calculations and robot-control components.
- **YOLO integration:** Connecting object-recognition results to robot manipulation processes.
- **LLM-based system design:** Designing the architecture that connects language understanding and high-level decision-making with perception and control modules.
- **Project coordination:** Coordinating development with team members responsible for different parts of the project.

This is a collaborative project. Overall system outcomes are distinguished from the responsibilities of individual contributors.

### Team


| Member | Main responsibilities | Affiliation / Background |
| :--- | :--- | :--- |
| **HANG Xingchen** | Project Lead. Embedded robotic systems, robot-arm control, inverse kinematics, YOLO-based image recognition, LLM/VLM-based high-level decision integration, and overall system design. | Kobe University |
| **MARUYAMA Haruki** | Prompt design, Japanese dialogue-style refinement, response wording, and adaptation to cultural context. | The University of Tokyo |
| **LI Tianyang** | CAD/SolidWorks-based 3D modeling, mechanical design, prototyping, and tuning of YOLO-based grasping and inverse kinematics. | Kobe University |
| **TASAKA Fuzuki** | Market and user research, AI-function implementation and evaluation, agent-behavior evaluation, usability testing, and prototype-improvement proposals. | Kobe University |
| **SUN Yushan** | System integration, socket communication, and backend development. | Kobe University |
| **SUN Yan** | Human behavior and robot interaction, prompt processing, and system behavior-logic design. | Kobe University |
| **JIANG Qilong** | Streamlit UI design and improvements to usability and user experience. | The University of Tokyo / Design and Software Engineering |
| **USUKI SEIYA** | Support for system development and research activities. | Kobe University |



---

## 5. Demonstrations and Scope of Validation

The publicly available material focuses on **the implementation and demonstration of a research prototype** connecting language, vision, and control.

### Presented Capabilities

| Capability | Development stage |
| :--- | :--- |
| Connecting language instructions to physical actions | SKYNET-5 |
| Voice input and control | SKYNET-6.1 |
| Grasping with YOLO and inverse kinematics | SKYNET-8 |
| Local processing, UI, and host/embedded-controller architecture | SKYNET-10 |
| Target selection among multiple candidates and structured output | SKYNET-11 |
| Hierarchical target selection, geometry-based occlusion assessment, and physical execution | SKYNET-16 |

### Quantitative Evaluation

This README does not report quantitative results such as trial counts, grasping success rates, target-selection accuracy, occlusion-assessment accuracy, processing time, or position errors.

The demonstration videos should therefore be viewed as individual examples of system behavior. They are not presented as comparative tests establishing a specific success rate, superiority over other methods, or reliability during extended continuous operation.

### Scope and Limitations

The public materials do not provide guarantees regarding:

- Operation with arbitrary objects, lighting conditions, camera arrangements, or unfamiliar environments.
- Comprehensive three-dimensional collision avoidance, reachability, or grasp stability.
- Hard real-time control, deployment in industrial facilities, integration with PLCs, or compliance with industrial safety requirements.

Details of post-execution observation, success/failure assessment, and retry handling are also not included in this README. The processing flow above should not be interpreted as evidence that all of these functions have been implemented.

---

## 6. Development History and Demonstration Videos

The following records are arranged by version. Dates are not assigned to versions for which publication or development dates are not provided.

### SKYNET-5 — Connecting Language Instructions to Physical Actions

**[Demonstration video](https://www.youtube.com/watch?v=69e78PqmeNM&t=3s)**

An early validation stage in which the system interprets simple language instructions and executes corresponding physical actions. This version establishes the foundation for connecting natural language to robot motion.

### SKYNET-6 — Dialogue Expression and Japanese Responses

**[Demonstration video](https://www.youtube.com/watch?v=lS7rUFcXonQ)**

This version addresses dialogue and response wording for human interaction, including the use of Japanese honorific language.

### SKYNET-6.1 — Voice Input and Control

**[Demonstration video](https://www.youtube.com/watch?v=jr8Sl4M8Fsw)**

Voice input and control are added, connecting spoken user instructions to robot operation.

### SKYNET-8 — Grasping Through Visual Recognition and Inverse Kinematics

**[Demonstration video](https://www.youtube.com/watch?v=Eo-8q8rrNC4)**

YOLO-based object detection is integrated with inverse kinematics to recognize simple objects and initiate grasping actions. In addition to language instructions, this stage introduces manipulation using target positions obtained from images.

### SKYNET-10 — Local Processing, UI, and Distributed Architecture

**[Demonstration video](https://www.youtube.com/watch?v=zrWmjCPV1bM)**

The development record for this version describes the following changes:

- **Local LLM processing:** A transition from a configuration using the ChatGPT cloud API to a lightweight local LLM with domain-specific prompts.
- **Local speech processing:** A transition to locally processed ASR and TTS.
- **User interface:** A team-developed UI that brings configuration and operation together.
- **Host/embedded-controller separation:** The host handles perception, interaction, and decision-making, while the Raspberry Pi handles kinematics calculations and actuator control.

These descriptions apply to the SKYNET-10 configuration. This README does not report measurements quantifying improvements in response time or stability.

### SKYNET-11 — Target Selection Among Multiple Objects

**[Demonstration video](https://www.youtube.com/watch?v=l8yuPjlxAhg)**

This version evaluates multiple detected candidates against user-specified selection criteria.

It processes target coordinates, confidence scores, and color information. Annotated images, detection results in JSON format, and prompts describing the selection criteria are provided to a vision-capable LLM.

Example selection criteria include prioritizing clean and undamaged objects, prioritizing objects near the center of the image, and applying tie-breaking rules when candidates receive the same priority.

The result is returned as **structured JSON containing the target label, coordinates, and reasons for selection**. Target selection here refers to decision-making based on the specified criteria; it does not guarantee physical grasping performance or mathematical optimality.

### SKYNET-16 — Hierarchical Target Selection, Occlusion Assessment, and Physical Execution

**[Demonstration video](https://www.youtube.com/watch?v=7S0SW6Wzqks)**

This version separates target selection, occlusion assessment, and inverse-kinematics-based execution into a hierarchical architecture.

High-level decisions made by LLMs/VLMs are connected to grasping or occluder-removal actions through transformations into the robot coordinate frame and kinematics calculations. See “Featured Demonstration: SKYNET-16” for details.

---

## 7. Source-Code Availability, Research Outcomes, and Contact

This repository forms part of a technical portfolio concerning technology for which a patent application is being prepared. For this reason, not all source code is publicly available.

The core research outcomes of this project belong to the graduate school.

This README introduces the research objectives, system architecture, demonstrations, development history, and individual responsibilities. It does not guarantee that the complete system can be reproduced using only the publicly available information.

For inquiries regarding research collaboration, technical details, or potential adoption, please contact:

- **Contact:** HANG XINGCHEN / 杭 星辰
- **GitHub:** [hsingchen-dev](https://github.com/hsingchen-dev)
- **E-mail:** [hsingchen.hang@outlook.jp](mailto:hsingchen.hang@outlook.jp)

---

**Robotic Manipulation — Grounded in mechanics and kinematics, connecting perception and high-level decisions to physical robot actions.**
