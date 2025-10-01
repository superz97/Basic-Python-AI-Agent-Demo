import os
import subprocess
import sys

def run_python_file(working_directory, file_path, args=[]):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        if os.path.isabs(file_path):
            abs_file_path = os.path.abspath(file_path)
        else:
            abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        if not os.path.commonprefix([abs_file_path, abs_working_dir]) == abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(abs_file_path):
            return f'Error: File "{file_path}" not found'
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        cmd = [sys.executable, file_path] + args
        completed_process = subprocess.run(
            cmd, 
            cwd=working_directory,
            timeout=30,
            capture_output=True,
            text=True
        )
        output_parts = []
        if completed_process.stdout:
            output_parts.append(f"STDOUT:\n{completed_process.stdout}")
        if completed_process.stderr:
            output_parts.append(f"STDERR:\n{completed_process.stderr}")
        if not output_parts:
            output_parts.append("No output produced.")
        if completed_process.returncode != 0:
            output_parts.append(f"Process exited with code {completed_process.returncode}")
        return "\n".join(output_parts)
    except subprocess.TimeoutExpired:
        return "Error: executing Python file: Process timed out after 30 seconds."
    except Exception as e:
        return f"Error: executing Python file: {e}"