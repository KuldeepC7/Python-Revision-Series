# 3. In your Coder's Loop platform, a course video is uploaded with the filename `"intro_to_python_programming"`. Use the `.replace()` method to change all underscores to spaces for the frontend display.

course_video_name = 'intro_to_python_programming'
new_name = course_video_name.replace('_', ' ')
print(new_name)