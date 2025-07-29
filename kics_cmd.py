import subprocess

def run_kics_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        print("Output:\n", result.stdout)
        
        if result.stderr:
            print("Errors:\n", result.stderr)
        return result.returncode
    
    except subprocess.SubprocessError as e:
        print(f"Command failed with error: {e}")
        return 1