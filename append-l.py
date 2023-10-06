import bpy

count = 0
for bone in bpy.context.selected_bones:
    if not bone.name.endswith(".L"):
        bone.name = f"{bone.name}.L"
        count += 1
print(f"Changed {count} bones")