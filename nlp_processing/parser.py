import spacy

nlp = spacy.load("en_core_web_sm")

def extract_info(sentence):
    doc = nlp(sentence)
    
    operations_map = {
        "add": ["add", "plus", "sum"],
        "subtract": ["subtract", "minus"],
        "multiply": ["multiply", "times"],
        "divide": ["divide"],
        "palindrome": ["palindrome", "is palindrome", "check palindrome"],
        "odd_even": ["odd", "even", "odd or even", "check if odd", "check if even"],
        "armstrong": ["armstrong", "is armstrong", "check armstrong"]
    }

    operation = None
    variables = []

    # Check for special operations first
    if any(word in sentence.lower() for word in ["palindrome", "is palindrome", "check palindrome"]):
        operation = "palindrome"
        # Extract numbers for palindrome check
        for token in doc:
            if token.pos_ in ["NUM"]:
                variables.append(token.text)
                break
    elif any(word in sentence.lower() for word in ["odd", "even", "odd or even"]):
        operation = "odd_even"
        # Extract numbers for odd/even check
        for token in doc:
            if token.pos_ in ["NUM"]:
                variables.append(token.text)
                break
    elif any(word in sentence.lower() for word in ["armstrong", "is armstrong", "check armstrong"]):
        operation = "armstrong"
        # Extract numbers for armstrong check
        for token in doc:
            if token.pos_ in ["NUM"]:
                variables.append(token.text)
                break
    else:
        # Existing operation extraction logic
        for token in doc:
            word = token.text.lower()
            
            # Ignore 'by' to avoid misinterpretation
            if word == "by":
                continue

            # Identify mathematical operations
            for key, synonyms in operations_map.items():
                if word in synonyms:
                    operation = key
                    break
            
            # Extract numbers
            if token.pos_ in ["NUM"]:
                variables.append(token.text)

    return {"operation": operation, "variables": variables}

# Example Usage
if __name__ == "__main__":
    print(extract_info("Multiply 4 by 6"))  # Expected: {'operation': 'multiply', 'variables': ['4', '6']}
    print(extract_info("Divide 100 by 4"))  # Expected: {'operation': 'divide', 'variables': ['100', '4']}
