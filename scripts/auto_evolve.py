import os
import subprocess
import datetime
import sys

def run_command(command, cwd=None):
    try:
        result = subprocess.run(
            command, 
            cwd=cwd, 
            check=True, 
            text=True, 
            capture_output=True,
            shell=True  # Required for some git commands on Windows
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(f"Error output: {e.stderr}")
        return None

def auto_evolve():
    # Define the skill directory (current script is in ./scripts/, so we go up one level)
    skill_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    print(f"Starting auto-evolution for: {skill_dir}")
    
    # 1. Check for changes
    status = run_command("git status --porcelain", cwd=skill_dir)
    
    if not status:
        print("No changes detected. Nothing to evolve.")
        return
    
    print("Changes detected:")
    print(status)
    
    # 2. Stage all changes
    print("Staging changes...")
    run_command("git add .", cwd=skill_dir)
    
    # 3. Create commit message
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    commit_msg = f"feat(evolution): Absorb insights from session [{today}]"
    
    # Allow passing custom message via args
    if len(sys.argv) > 1:
        commit_msg = f"feat(evolution): {sys.argv[1]} [{today}]"
        
    print(f"Committing with message: '{commit_msg}'")
    run_command(f'git commit -m "{commit_msg}"', cwd=skill_dir)
    
    # 4. Push to remote
    print("Pushing to origin/main...")
    push_result = run_command("git push origin main", cwd=skill_dir)
    
    if push_result is not None:
        print("Evolution complete! Changes pushed to GitHub.")
    else:
        print("Push failed. Please check your network or git config.")

if __name__ == "__main__":
    auto_evolve()
