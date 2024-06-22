import re

def check_password_strength(password):
    
    score = 0
    feedback = []
    min_length = 8  
    has_uppercase = False
    has_lowercase = False
    has_number = False
    has_special = False

    if len(password) >= min_length:
        score += 1
    else:
        feedback.append("Password should be at least {} characters long.".format(min_length))

    
    if any(c.isupper() for c in password):
        has_uppercase = True
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    
    if any(c.islower() for c in password):
        has_lowercase = True
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

   
    if any(c.isdigit() for c in password):
        has_number = True
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

  
    if any(c in '!@#$%^&*()-_=+[{]}\\|;:\'",<.>/?' for c in password):
        has_special = True
        score += 1
    else:
        feedback.append("Password should contain at least one special character (e.g., !@#$%^&*).")

   
    if len(password) >= 12:
        score += 1
        feedback.append("Consider using a longer password for added security.")

   
    if score <= 3:
        strength = "Weak"
    elif score <= 5:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedbac
password = "MyPa$$w0rd"
strength_level, feedback_messages = check_password_strength(password)

print("Password Strength: {}".format(strength_level))
if feedback_messages:
    print("\nSuggestions and Feedback:")
    for message in feedback_messages:
        print("- {}".format(message))
        
