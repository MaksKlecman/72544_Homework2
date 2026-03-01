import random

scenarios = [
    {
        "tool": "Microsoft 365",
        "situation": "MFA available but not enabled",
        "risk": "yes",
        "responsible": "customer",
        "explanation": "Customer must enable MFA"
    },
    {
        "tool": "Google Workspace",
        "situation": "Google encryptio n system has a bug",
        "risk": "yes",
        "responsible": "provider",
        "explanation": "Encryption implementation is provier responsibility"
    },
    {
        "tool": "Salesforce",
        "situation": "Admin sets customer data to public",
        "risk": "yes",
        "responsible": "customer",
        "explanation": "Data configuration is customer responsibility."
    },
    {
        "tool": "Zoom",
        "situation": "Meeting passwords not enforced",
        "risk": "yes",
        "responsible": "customer",
        "explanation": "Security settings must be configured by customer"
    },
    {
        "tool": "Slack",
        "situation": "Slack global outage due to infrastructure failure",
        "risk": "yes",
        "responsible": "provider",
        "explanation": "Availability is provider responsibility"
    },
    {
        "tool": "Dropbox",
        "situation": "User shares sensitive folder publicly",
        "risk": "yes",
        "responsible": "customer",
        "explanation": "User access control is customer responsibility."
    },
    {
        "tool": "GitHub",
        "situation": "Private repository accidentally made public",
        "risk": "yes",
        "responsible": "customer",
        "explanation": "Repository visibility controlled by customer"
    },
    {
        "tool": "Microsoft 365",
        "situation": "Data center physical breach",
        "risk": "yes",
        "responsible": "provider",
        "explanation": "Physical security is provider responsibility"
    }
]

def main():
    random.shuffle(scenarios)
    score = 0

    for i, s in enumerate(scenarios, 1):
        print(f"\nScenario {i}")
        print("Tool:", s["tool"])
        
        print("Situation:", s["situation"])

        risk = input("Is this a security risk?  ").lower()
        resp = input("Who is responsible?  ").lower()

        if risk == s["risk"]:
            score += 1
            
        if resp == s["responsible"]:
            score += 1

        print("Correct answer:", s["risk"], ",", s["responsible"])
        print("Explanation:", s["explanation"])

    print("\nFinal score:", score, "/ 16")

    if score <= 5:
        print("Level: Novice")
    elif score <= 10:
        print("Level: Developing")
        
    elif score <= 14:
        print("Level: Proficient")
    else:
        print("Level: Expert")

if __name__ == "__main__":
    main()