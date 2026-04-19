import os

def execute_task(task):
    if task == "deploy":
        return "🚀 App deployed (simulated)"

    elif task == "logs":
        return "📄 Logs checked"

    elif task == "container":
        return "🐳 Docker checked"

    else:
        return "❌ Unknown task"