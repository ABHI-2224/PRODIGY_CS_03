import re
from colorama import Fore, Style, init
import pyfiglet

init(autoreset=True)

def password_strength(password):
    length = len(password)
    complexity = 0
    suggestions = []
    
    if length >= 8:
        complexity += 1
    else:
        suggestions.append("🔸 " + Fore.YELLOW + "Make your password at least 8 characters long.")

    if re.search(r"[a-z]", password):
        complexity += 1
    else:
        suggestions.append("🔸 " + Fore.YELLOW + "Include at least one lowercase letter.")

    if re.search(r"[A-Z]", password):
        complexity += 1
    else:
        suggestions.append("🔸 " + Fore.YELLOW + "Include at least one uppercase letter.")

    if re.search(r"\d", password):
        complexity += 1
    else:
        suggestions.append("🔸 " + Fore.YELLOW + "Include at least one digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        complexity += 1
    else:
        suggestions.append("🔸 " + Fore.YELLOW + "Include at least one special character (e.g., !, @, #, $, etc.).")

    if re.search(r"(.)\1{2,}", password):
        complexity -= 1
        suggestions.append("🔸 " + Fore.YELLOW + "Avoid sequences of the same character (e.g., 'aaa').")

    if complexity == 0:
        strength = "Very Weak"
        color = Fore.RED
        emoji = "🔴"
    elif complexity == 1:
        strength = "Weak"
        color = Fore.RED
        emoji = "🟠"
    elif complexity == 2:
        strength = "Moderate"
        color = Fore.YELLOW
        emoji = "🟡"
    elif complexity == 3:
        strength = "Strong"
        color = Fore.GREEN
        emoji = "🟢"
    elif complexity == 4:
        strength = "Very Strong"
        color = Fore.GREEN
        emoji = "🟢"
    else:
        strength = "Excellent"
        color = Fore.CYAN
        emoji = "🔵"
    
    return f"{color}Password Strength: {strength} {emoji}", suggestions

def main():
    tool_name = "PassChecker"
    ascii_art = pyfiglet.figlet_format(tool_name, font="drpepper")
    colored_ascii = f"{Fore.BLUE}{Style.BRIGHT}{ascii_art}"
    print(colored_ascii)

    
    while True:
        user_password = input(Fore.GREEN + "Enter your password to check its strength (or press 'e' to exit): " + Style.RESET_ALL)
        
        if user_password.lower() == 'e':
            print(Fore.CYAN + "exiting.....")
            break
        
        print()  
        
        strength, suggestions = password_strength(user_password)
        print(strength + "\n")  
        
        if suggestions:
            print("Suggestions to improve your password:")
            for suggestion in suggestions:
                print(suggestion)
        else:
            print(Fore.GREEN + "✅ Your password is strong enough.")
        
        print()  

if __name__ == "__main__":
    main()