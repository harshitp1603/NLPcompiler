from nlp_processing import parser
from code_generator import python_generator
from compiler import llvm_compiler

def main():
    user_input = input("Enter your instruction: ")
    
    # Debugging output
    info = parser.extract_info(user_input)
    print("\n[DEBUG] Extracted Info:", info)  # Check what extract_info() returns

    # Ensure info contains required keys
    if not isinstance(info, dict) or "operation" not in info or "variables" not in info:
        print("[ERROR] Invalid NLP Output. Please check extract_info().")
        return

    # Generate Python Code
    code = python_generator.generate_python_code(info["operation"], info["variables"])
    print("\nGenerated Code:\n", code)

    # Compile and Run
    llvm_compiler.compile_and_run(code, lang="python")

if __name__ == "__main__":
    main()
