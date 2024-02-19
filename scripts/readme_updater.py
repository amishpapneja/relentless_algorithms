import os
import re
import requests
import markdown

file_name_pattern = re.compile(r'(\d+)-([\w-]+)\.py')

# Function to get all Python file names in all subdirectories
def get_python_files(root_dir):
    python_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files

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
    table_content = "| No. | Name | LeetCode Link | Link to the path |\n"
    table_content += "|:----:|:----:|:-------------:|------------------|\n"
    for i, file in enumerate(files, 1):
        filename = os.path.basename(file)
        github_url = generate_github_url(file)
        # table_content += f"| {i} | {filename} | [{filename}]({github_url}) |\n"
        leetcode_link = generate_leetcode_link(filename)
        table_content += f"| {i} | {filename} | [LeetCode]({leetcode_link}) | [{filename}]({github_url}) |\n"
    return table_content

def generate_leetcode_link(filename):
    print(filename)
    leetcode_id = file_name_pattern.match(filename).group(2)
    return f"https://leetcode.com/problems/{leetcode_id}/"


# Edit a readme file
readme_path = 'relentless_algorithms\README.md'

# Go through files and folders
folder_path = 'relentless_algorithms\special_200'
matching_count = 0
non_matching_count = 0

python_files = get_python_files(folder_path)
leet_code_files = []
# Iterate through the files
for file_path in python_files:
    # Extract file name
    og = file_path
    file_name = os.path.basename(file_path)
    # Check if the file name matches the pattern
    if file_name_pattern.match(file_name):
        matching_count += 1
        leet_code_files.append(og)
    else:
        non_matching_count += 1
print(matching_count, non_matching_count)
# Generate Markdown content for the counts
counts_markdown = f"# Total Leetcode Count: {matching_count}\n\n" \
                  f"# Miscellaneous Count: {non_matching_count}\n\n"

# Access internet links
response = requests.get('https://google.com')
html_content = response.text

# Write effective Markdown
# markdown_content = markdown.markdown('# Header\nThis is *markdown* content.')

# Generate Markdown table for files
markdown_table = generate_markdown_table(leet_code_files)

# Combine all Markdown content
final_markdown_content = f"{counts_markdown}{markdown_table}"

# Save the Markdown content to README.md file
with open(readme_path, 'w') as file:
    file.write(final_markdown_content)
