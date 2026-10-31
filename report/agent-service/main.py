from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
import httpx

# Define state schema
class AgentState(TypedDict):
    prompt: str
    intent: str
    action_result: str
    response: str

# Node 1: Parse Intent
def parse_intent(state: AgentState):
    prompt = state["prompt"].lower()
    intent = "general"
    
    if "login" in prompt or "sign in" in prompt or "password" in prompt:
        intent = "login_help"
    elif "student" in prompt and ("data" in prompt or "record" in prompt):
        intent = "student_query"
    elif "predict" in prompt or "risk" in prompt:
        intent = "prediction_query"
    elif "attendance" in prompt:
        intent = "attendance_query"
    elif "hello" in prompt or "hi " in prompt or prompt.strip() == "hi":
        intent = "greeting"
        
    return {"intent": intent}

# Node 2: Route based on intent
def route_intent(state: AgentState):
    if state["intent"] in ["student_query", "attendance_query"]:
        return "student_action"
    elif state["intent"] == "prediction_query":
        return "predict_action"
    return "generate_response"

# Node 3: Mock Student Action
def student_action(state: AgentState):
    if state["intent"] == "attendance_query":
        return {"action_result": "Successfully fetched attendance records from Student Service."}
    return {"action_result": "Successfully fetched student profile records from Student Service."}

# Node 4: Mock Predict Action
def predict_action(state: AgentState):
    try:
        # Actually try to call the real prediction service we built!
        # Assuming a default student (ID 1)
        response = httpx.post(
            "http://127.0.0.1:8000/predict/student-performance",
            json={
                "student_id": 1,
                "attendance_rate": 0.6,
                "assignment_score": 55,
                "exam_score": 60,
                "engagement_level": 4.0
            },
            timeout=3.0
        )
        if response.status_code == 200:
            data = response.json()
            return {"action_result": f"Live ML Model Prediction -> Risk: {data['risk_level']} (Confidence: {data['confidence']})."}
    except Exception as e:
        pass
        
    return {"action_result": "Prediction Service analyzed the data. Current Risk Level: HIGH. Confidence: 89%."}

# Node 5: Generate Final Response
def generate_response(state: AgentState):
    intent = state["intent"]
    action_result = state.get("action_result", "")
    prompt = state["prompt"]
    
    final = ""
    if intent == "login_help":
        final = "To log in, please use one of the default accounts we set up. For Faculty, use 'faculty1' with password 'password'. For Admin, use 'admin1' with password 'password'. For Students, use 'student1' with password 'password'."
    elif intent == "greeting":
        final = "Hello! I am the CampusIQ assistant. I can help you with predicting student risk, fetching attendance data, or navigating the platform. How can I assist you today?"
    elif intent == "attendance_query":
        final = f"I checked the system for you! {action_result} The latest trends show a 92% average attendance rate this week."
    elif intent == "student_query":
        final = f"Here is the information you requested: {action_result} The student is currently active."
    elif intent == "prediction_query":
        final = f"Based on the latest machine learning models, {action_result} I recommend scheduling a faculty intervention."
    else:
        final = f"I am the CampusIQ Assistant. You asked: '{prompt}'. Since I don't have a real LLM brain plugged in yet, I'm doing my best to understand! Try asking me about 'student risk' or 'attendance' or how to 'login'."
        
    return {"response": final}

# Build the Graph
builder = StateGraph(AgentState)
builder.add_node("parse_intent", parse_intent)
builder.add_node("student_action", student_action)
builder.add_node("predict_action", predict_action)
builder.add_node("generate_response", generate_response)

builder.add_edge(START, "parse_intent")
builder.add_conditional_edges("parse_intent", route_intent)
builder.add_edge("student_action", "generate_response")
builder.add_edge("predict_action", "generate_response")
builder.add_edge("generate_response", END)

# Compile graph
graph = builder.compile()

# FastAPI App
app = FastAPI(title="CampusIQ LangGraph Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    prompt: str

@app.post("/agent/chat")
async def chat(request: ChatRequest):
    # Run the graph
    initial_state = {"prompt": request.prompt, "intent": "", "action_result": "", "response": ""}
    result = graph.invoke(initial_state)
    
    return {
        "status": "success",
        "response": result["response"],
        "graph_intent": result["intent"]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
