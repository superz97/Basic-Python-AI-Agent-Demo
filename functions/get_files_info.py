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
    
