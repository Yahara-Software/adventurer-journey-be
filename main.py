from adventure_path import run_simulation

directions_to_parse = "15F6B6B5L16R8B16F20L6F13F11R"
result = run_simulation(directions_to_parse)
print(f"You walked {str(result)} steps from where you started - what a journey!")