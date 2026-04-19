import os
from executor import execute_task

def process_command(user_input):
    user_input = user_input.lower()

    if "deploy" in user_input:
        return execute_task("deploy")

    elif "logs" in user_input:
        return execute_task("logs")

    elif "container" in user_input:
        return execute_task("container")

    else:
        return "❌ Unknown command"