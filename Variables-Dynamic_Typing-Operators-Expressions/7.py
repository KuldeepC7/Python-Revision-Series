# 7. A FastAPI server has an available memory of 1024 MB. A background task requires 128 MB. Use the correct assignment operator to subtract and update the available memory variable in one step.

available_memory = 1024

print(available_memory)

background_tasks_memory_requirement = 128

available_memory = available_memory - background_tasks_memory_requirement

print(available_memory)