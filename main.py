def greet(name, language="en"):
    if language == "sv":
        return f"Hej, {name}! Välkommen."
    return f"Hello, {name}! Welcome to GitHub practice."

if __name__ == "__main__":
    print(greet("Jane"))
    print(greet("Jane", "sv"))
    