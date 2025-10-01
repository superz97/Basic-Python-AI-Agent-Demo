import os

def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.join(working_directory, directory)
        abs_full_path = os.path.abspath(full_path)
        abs_working_directory = os.path.abspath(working_directory)

        if not abs_full_path.startswith(abs_working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(abs_full_path):
            return f'Error: "{directory}" is not a directory'
        
        entries = os.listdir(abs_full_path)
        result_lines = []
        for entry in entries:
            entry_path = os.path.join(abs_full_path, entry)
            if os.path.isdir(entry_path):
                size = os.path.getsize(entry_path)
                result_lines.append(f'- {entry}: file_size={size} bytes, is_dir=True')
            else:
                size = os.path.getsize(entry_path)
                result_lines.append(f'- {entry}: file_size={size} bytes, is_dir=False')
        
        return '\n'.join(result_lines)
    
    except Exception as e:
        return f'Error: {str(e)}'
    
def get_file_content(working_directory, file_path):
    try:
        abs_working = os.path.abspath(working_directory)
        abs_file = os.path.abspath(os.path.join(working_directory, file_path))
        if not abs_file.startswith(abs_working):
            return f'Error: Cannot read "{file_path} as it is outside the permitted working directory'
        if not os.path.isfile(abs_file):
            return f'Error: File not found or is not a regular file: "{file_path}'
        with open(abs_file, 'r') as file:
            content = file.read()
        if len(content) > 10000:
            content = content[:10000] + f'\n...File "{file_path}" truncated at 10000 characters.'
        return content
    except Exception as e:
        return f'Error: {str(e)}'