



import os
import json
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, END, START

from app.services.parse_and_generate_tests import main as generate_tests
from app.services.impl_from_tests import main as generate_implementations
from app.services.run_tests_and_retry import main as run_tests
from app.services.zipper import zip_project
from app.services.docx_parser import extract_text_from_docx
from app.srs_parser import analyze_srs_content

class OrchestratorState(TypedDict):
    srs_path: str
    project_name: str
    analysis: dict
    tests_passed: bool
    zip_path: str

# 🧠 Step 1: Analyze SRS → aim.json
def srs_analysis_node(state: OrchestratorState):
    text = extract_text_from_docx(state["srs_path"])
    analysis_result = analyze_srs_content(text)

    os.makedirs("generated_project/utils", exist_ok=True)
    aim_path = "generated_project/utils/aim.json"
    with open(aim_path, "w", encoding="utf-8") as f:
        json.dump(analysis_result, f, indent=4)

    # Create app/models and app/routes based on aim.json
    models_dir = os.path.join("generated_project", "app", "models")
    routes_dir = os.path.join("generated_project", "app", "routes")
    os.makedirs(models_dir, exist_ok=True)
    os.makedirs(routes_dir, exist_ok=True)

    # --- Models ---
    models_code = ""
    for table in analysis_result.get("database_schema", []):
        if not isinstance(table, dict):
            continue
        class_name = table.get("name", "Model").title().replace("_", "")
        models_code += f"class {class_name}(BaseModel):\n"
        for col in table.get("columns", []):
            if isinstance(col, dict):
                models_code += f"    {col.get('name', 'field')}: {col.get('type', 'str')}\n"
        models_code += "\n\n"

    with open(os.path.join(models_dir, "models.py"), "w") as f:
        f.write("from pydantic import BaseModel\n\n")
        f.write(models_code.strip())

    # --- Routes ---
    for endpoint in analysis_result.get("api_endpoints", []):
        if not isinstance(endpoint, dict):
            print(f"⚠️ Skipping malformed endpoint: {endpoint}")
            continue

        path = endpoint.get("path", "/").strip("/").replace("/", "_") or "default_route"
        route_code = f"""
from fastapi import APIRouter

router = APIRouter()

@router.{endpoint.get('method', 'get').lower()}("{endpoint.get('path', '/')}") 
async def {path}():
    return {{"message": "This is a stub for {endpoint.get('description', 'an endpoint')}"}} 
"""
        with open(os.path.join(routes_dir, f"{path}.py"), "w") as f:
            f.write(route_code.strip())

    return {"analysis": analysis_result}

# 📁 Step 2: Generate unit tests
def test_generation_node(state: OrchestratorState):
    generate_tests()
    return {}

# ⚙️ Step 3: Generate implementation from tests
def implementation_node(state: OrchestratorState):
    generate_implementations()
    return {}

# 🧪 Step 4: Run + Retry tests
def testing_node(state: OrchestratorState):
    passed = run_tests()
    return {"tests_passed": passed}

# 📦 Step 5: Zip project folder
def packaging_node(state: OrchestratorState):
    zip_path = zip_project("generated_project")
    return {"zip_path": zip_path}

# 🚀 Build Graph
graph = StateGraph(OrchestratorState)
graph.add_node("analyze", srs_analysis_node)
graph.add_node("generate_tests", test_generation_node)
graph.add_node("generate_code", implementation_node)
graph.add_node("run_tests", testing_node)
graph.add_node("zip", packaging_node)

graph.add_edge(START, "analyze")
graph.add_edge("analyze", "generate_tests")
graph.add_edge("generate_tests", "generate_code")
graph.add_edge("generate_code", "run_tests")
graph.add_conditional_edges("run_tests", lambda x: "zip")  # Always go to zip
graph.add_edge("zip", END)

compiled_graph = graph.compile()

def run_full_generation(srs_path: str) -> str:
    name = os.path.splitext(os.path.basename(srs_path))[0]
    state = compiled_graph.invoke({"srs_path": srs_path, "project_name": name})
    return state["zip_path"]


