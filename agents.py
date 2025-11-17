from google.adk.agents import LlmAgent, SequentialAgent, Agent
from google.adk.tools import PreloadMemoryTool
from google.adk.models.gemini import GeminiFlash
from tools import CUSTOM_TOOLS
import json

# Define the model and memory
MODEL = GeminiFlash() 
MEMORY_TOOL = PreloadMemoryTool() # Provides long-term memory access

# ----------------- 1. The Evaluator Agent -----------------
EvaluatorAgent = LlmAgent(
    name="EvaluatorAgent",
    model=MODEL,
    instruction="""You are the test administrator. Your job is to call the 'generate_quiz' 
    tool with the current 'topic' and 'difficulty' to test the student. After the tool returns, 
    present the quiz questions to the user. Do NOT provide answers or explanations. 
    Store the final score (e.g., 75%) in the session state for the Planner to access.
    """,
    tools=[MEMORY_TOOL, CUSTOM_TOOLS[0]] # QuizGeneratorTool
)

# ----------------- 2. The Teacher Agent -----------------
TeacherAgent = LlmAgent(
    name="TeacherAgent",
    model=MODEL,
    instruction="""You are a patient and encouraging tutor. Your goal is to teach the 
    user the subject matter provided by the Planner Agent. Use the context from the 
    Memory Bank to address their past weaknesses. Only proceed to the next step when 
    the user confirms they are ready for the quiz.
    """,
    tools=[MEMORY_TOOL]
)

# ----------------- 3. The Planner Agent -----------------
PlannerAgent = LlmAgent(
    name="PlannerAgent",
    model=MODEL,
    instruction="""You are the goal-oriented Study Planner. Your first action is to 
    get the user's overall learning goal (e.g., 'Learn Python'). Based on this goal 
    and any weaknesses in the Memory Bank, call the 'schedule_study_session' tool 
    and break down the goal into the first sub-topic ('topic') and 'difficulty'. 
    Pass the 'topic' and 'difficulty' to the Teacher Agent. If a quiz score is in 
    the session state, use it to adapt the next lesson plan.
    """,
    tools=[MEMORY_TOOL, CUSTOM_TOOLS[1]] # CalendarTool
)

# ----------------- 4. The Orchestrator (Root Agent) -----------------
EduMentor = SequentialAgent(
    name="EduMentor",
    description="Orchestrates the study process: planning the lesson, teaching the subject, and testing the student's knowledge.",
    sub_agents=[
        PlannerAgent,
        TeacherAgent,
        EvaluatorAgent
    ],
    max_iterations=10 
)

ROOT_AGENT = EduMentor
