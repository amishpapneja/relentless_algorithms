import os
import requests
import markdown

# Function to get all Python file names in all subdirectories
def get_python_files(root_dir):
    python_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files

# Function to generate GitHub URLs from local file paths
# Function to generate GitHub URLs from local file paths
def generate_github_url(local_path):
    github_base_url = 'https://github.com/amishpapneja/relentless_algorithms/blob/master/'
    # Remove the first occurrence of 'relentless_algorithms/'
    # print("s", local_path)
    # parts = local_path.split('relentless_algorithms/', 1)
    local_path = local_path.lstrip('relentless_algorithms')
    print("p",local_path)
    # if len(parts) > 1:
    #     local_path = parts[1]
    # print(local_path.replace('\\', '/'))
    return github_base_url + local_path.replace('\\', '/')


# Function to generate Markdown table content for files with numbered rows and GitHub URLs
def generate_markdown_table(files):
    table_content = "| No. | Name | Link to the path |\n"
    table_content += "|:----:|:----:|------------------|\n"
    for i, file in enumerate(files, 1):
        filename = os.path.basename(file)
        github_url = generate_github_url(file)
        table_content += f"| {i} | {filename} | [{filename}]({github_url}) |\n"
    return table_content



# Edit a readme file
readme_path = 'relentless_algorithms\README.md'

# Go through files and folders
folder_path = 'relentless_algorithms\special_200'
python_files = get_python_files(folder_path)

# Access internet links
response = requests.get('https://google.com')
html_content = response.text

# Write effective Markdown
# markdown_content = markdown.markdown('# Header\nThis is *markdown* content.')

# Generate Markdown table for files
markdown_table = generate_markdown_table(python_files)

# Combine all Markdown content
final_markdown_content = f"{markdown_table}"

# Save the Markdown content to README.md file
with open(readme_path, 'w') as file:
    file.write(final_markdown_content)
