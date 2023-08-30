import os
import shutil

# Create HTML directory if it doesn't exist
if not os.path.exists('HTML'):
    os.makedirs('HTML')

# Walk through current directory
for dir_path, dir_names, file_names in os.walk('.'):
    for filename in file_names:
        if filename.endswith('.html') or filename.endswith('.html.tmp'):
            # Rename .html.tmp to .html
            if filename.endswith('.html.tmp'):
                new_name = filename.replace('.html.tmp', '.html')
                os.rename(os.path.join(dir_path, filename), os.path.join(dir_path, new_name))
                filename = new_name

            # Move .html files to HTML directory
            shutil.move(os.path.join(dir_path, filename), os.path.join('HTML', filename))