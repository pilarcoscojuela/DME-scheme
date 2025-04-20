#This python script run compute_equations.txt several times (3 in this case) and print into a file the linear
#systems,generated at each iteration, that relates varibles Rti,Sti,Kti,Lti,Zti,Wti,Xti,Yti with Ri,Si,Ki,Li,Zi,Wi,Xi,Yi
import subprocess
import re

outputs = []

# Run the Magma file 3 times.
for i in range(3):
    # Run the Magma code.
    result = subprocess.run(["magma", "compute_equations.txt"], capture_output=True, text=True)
    
   
    #print(f"Iteration {i+1} Magma stdout:\n{result.stdout}\n")
  
    try:
        with open("linear_system.txt", "r") as f:
            file_content = f.read().strip()
    except Exception as e:
        print(f"Error reading output file in iteration {i+1}: {e}")
        file_content = ""
    
    print(f"Iteration {i+1} file content:\n{file_content}\n")
    
    match = re.search(r'\[\n\[.*?\]\n\]', file_content, re.DOTALL)
    if match:
        list_text = match.group(0)
        outputs.append(list_text)
    else:
        print(f"No list block found in iteration {i+1}.")


linear_system_text = "linear_system:=[\n" + ",\n".join(outputs) + "\n];"


with open("linear_system.txt", "w") as f:
    f.write(linear_system_text)

print("Final linear_system written to linear_system.txt")
