from google.adk.tools import FunctionTool
from google.adk.tools.tool_context import ToolContext
from typing import Dict, Any

# --- Tool 1: Quiz Generator Tool (Custom Tool) ---
def generate_quiz(tool_context: ToolContext, topic: str, difficulty: str = "medium") -> Dict[str, Any]:
  """
  Generates a 5-question multiple-choice quiz on a specific topic and difficulty 
  level to test the student's understanding.

  Args:
    topic: The subject matter for the quiz (e.g., 'Python dicts' or 'Cloud Computing architecture').
    difficulty: The required difficulty level: 'easy', 'medium', or 'hard'.
  
  Returns:
    A structured quiz string or JSON that the Evaluator Agent can use.
  """
  # Placeholder for the actual quiz generation logic (LLM call)
  return {
      "status": "success",
      "quiz_content": f"Quiz on {topic} ({difficulty}): Question 1: What is X? (A) Y, (B) Z..."
  }

# --- Tool 2: Calendar Management Tool (Custom Tool) ---
def schedule_study_session(tool_context: ToolContext, topic: str, date_time: str) -> Dict[str, Any]:
  """
  Schedules a study session or exam time in the user's calendar.

  Args:
    topic: The subject of the scheduled session.
    date_time: The specific date and time for the event (e.g., '2025-12-05 10:00 AM').

  Returns:
    A status confirming the event was scheduled.
  """
  # Placeholder for calendar integration
  return {
      "status": "scheduled",
      "message": f"Successfully scheduled a 90-minute session on {topic} for {date_time}."
  }

# Create the FunctionTool wrappers
QuizGeneratorTool = FunctionTool(generate_quiz)
CalendarTool = FunctionTool(schedule_study_session)

# List of all custom tools
CUSTOM_TOOLS = [QuizGeneratorTool, CalendarTool]
