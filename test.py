#!/usr/bin/env python
# coding: utf-8

# In[16]:


print('hola mund111o')


# In[17]:


# #subir a github automaticamente
# ejecutar esto en el CRM
#> git config --global credential.helper cache
# Set the cache to timeout after 1 hour (3600 seconds); adjust as needed
#> git config --global credential.helper 'cache --timeout=3600'
import os
import subprocess

def notebook_to_script(notebook_name, repo_url):
    script_name = f"{notebook_name}.py"
    convert_command = f"jupyter nbconvert --to script {notebook_name}.ipynb"
    
    try:
        subprocess.run(convert_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Failed to convert notebook:", e)
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
    
    commit_message = "Add script generated from Jupyter Notebook"
    subprocess.run(f'git commit -m "{commit_message}"', shell=True, check=True)
    
    try:
        subprocess.run("git push -u origin master", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Failed to push to GitHub:", e.stderr.decode())

# Usage example commented out
notebook_to_script('test', 'https://github.com/ferranfont/inter.git')


# In[ ]:





# In[11]:




