# EduMentor-Capstone-Project.
Enter Autonomous Multi-Agent Study Planner for the Kaggle Capstone.

# EduMentor: An Autonomous Multi-Agent Study Planner

## Project Summary
This project implements the **EduMentor** agent, a sophisticated, autonomous system designed to guide users from a broad learning goal (e.g., "Master Python") to mastery. It achieves this by replacing manual planning and generic instruction with a stateful, adaptive agentic workflow.

## Architecture and Key Concepts Used
EduMentor is built on the Google Agent Development Kit (ADK) using Python.

**1. Multi-Agent System (Sequential & Loop):**
The core is a `SequentialAgent` that orchestrates the workflow: Planner -> Teacher -> Evaluator. This loop ensures continuous, adaptive learning.

**2. Sessions & Memory:**
The agent uses a persistent Memory Bank (`PreloadMemoryTool`) to store the student’s quiz scores and identified weaknesses, allowing the **Planner** and **Teacher** agents to tailor subsequent lessons specifically to the student's needs.

**3. Custom Tools:**
* `QuizGeneratorTool`: Used by the Evaluator to generate targeted assessments.
* `CalendarTool`: Used by the Planner to simulate scheduling study sessions.

## Setup and Running (For Judges)
1.  **Dependencies:** Ensure `google-adk` and `python-dotenv` are installed.
2.  **Files:** The solution is contained in `agents.py`, `tools.py`, and `main.py` (which orchestrates the services).
3.  **Run:** Execute `python main.py` to start the command-line chat demo.

## Value Proposition
The agent provides highly personalized 24/7 coaching and eliminates 100% of the manual time a student would spend planning their study schedule, significantly boosting learning efficiency.
