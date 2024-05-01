#!/usr/bin/env python
# coding: utf-8

# In[24]:


print('testjdd55kdk')


# In[25]:


import os
import subprocess

def notebook_to_script(notebook_name, repo_url):
    script_name = f"{notebook_name}.py"
    convert_command = f"jupyter nbconvert --to script {notebook_name}.ipynb"
    
    try:
        subprocess.run(convert_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Failed to convert notebook:", e.stderr.decode() if e.stderr else "No error details available.")
        return  # Exit if conversion fails

    if not os.path.exists('.git'):
        subprocess.run("git init", shell=True, check=True)

    # Ensure the main branch is created or switched to it if it exists
    subprocess.run("git checkout -B main", shell=True, check=True)
    
    # Check current remote URL
    existing_url = subprocess.run("git remote get-url origin", shell=True, capture_output=True, text=True)
    if existing_url.returncode == 0 and existing_url.stdout.strip() == repo_url:
        print("Remote 'origin' is already set to the correct URL.")
    else:
        if existing_url.returncode == 0:
            print("Remote 'origin' already exists, resetting to new URL")
            subprocess.run(f"git remote set-url origin {repo_url}", shell=True, check=True)
        else:
            print("Adding new remote 'origin'.")
            subprocess.run(f"git remote add origin {repo_url}", shell=True, check=True)

    subprocess.run(f"git add {script_name}", shell=True, check=True)
    
    # Check if there are any changes to commit
    status_result = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True)
    if status_result.stdout:
        commit_message = "Add script generated from Jupyter Notebook"
        subprocess.run(f'git commit -m "{commit_message}"', shell=True, check=True)
    else:
        print("No changes to commit.")
        return  # Exit if no changes

    # Push changes to the 'main' branch
    try:
        subprocess.run("git push -u origin main", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Failed to push to GitHub:", e.stderr.decode() if e.stderr else "No error details available.")

# Usage example uncommented for actual use
notebook_to_script('test', 'https://github.com/ferranfont/IES_poblenou.git')


# In[23]:


import os
import subprocess

def notebook_to_script(notebook_name, repo_url):
    script_name = f"{notebook_name}.py"
    convert_command = f"jupyter nbconvert --to script {notebook_name}.ipynb"
    
    try:
        subprocess.run(convert_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Failed to convert notebook:", e.stderr if e.stderr else "No error details available.")
        return  # Exit if conversion fails

    if not os.path.exists('.git'):
        subprocess.run("git init", shell=True, check=True)
    
    # Check current remote URL
    existing_url = subprocess.run("git remote get-url origin", shell=True, capture_output=True, text=True)
    if existing_url.returncode == 0 and existing_url.stdout.strip() == repo_url:
        print("Remote 'origin' is already set to the correct URL.")
    else:
        if existing_url.returncode == 0:
            print("Remote 'origin' already exists, resetting to new URL")
            subprocess.run(f"git remote set-url origin {repo_url}", shell=True, check=True)
        else:
            print("Adding new remote 'origin'.")
            subprocess.run(f"git remote add origin {repo_url}", shell=True, check=True)

    subprocess.run(f"git add {script_name}", shell=True, check=True)
    
    # Checking for staged changes
    status_result = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True)
    if status_result.stdout:
        commit_message = "Add script generated from Jupyter Notebook"
        try:
            subprocess.run(f'git commit -m "{commit_message}"', shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print("Failed to commit:", e.stderr if e.stderr else "No error details available.")
            return  # Exit if commit fails
    else:
        print("No changes to commit.")
        return  # Exit if no changes

    # Push to remote repository
    try:
        subprocess.run("git push -u origin master", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Failed to push to GitHub:", e.stderr if e.stderr else "No error details available.")

# Usage example uncommented for actual use
notebook_to_script('test', 'https://github.com/ferranfont/IES_poblenou.git')


# In[ ]:





# In[ ]:





# In[11]:




