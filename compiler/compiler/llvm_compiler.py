import subprocess

def compile_and_run(code, lang="python"):
    filename = "temp.py" if lang == "python" else "temp.cpp"
    
    with open(filename, "w") as f:
        f.write(code)

    if lang == "python":
        result = subprocess.run(["python", filename], capture_output=True, text=True)
        return result.stdout if result.stdout else result.stderr
    elif lang == "cpp":
        subprocess.run(["g++", filename, "-o", "output"])
        result = subprocess.run(["./output"], capture_output=True, text=True)
        return result.stdout if result.stdout else result.stderr
