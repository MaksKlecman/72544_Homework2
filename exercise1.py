def get_yes_no(question):
    while True:
        answer = input(question + " (yes/no): ").strip().lower()
        if answer in ["yes", "no"]:
            return answer
        print("Invalid input Please type 'yes' or 'no'")

def get_stability():
    while True:
        answer = input("Is workload stable or variable?  ").strip().lower()
        if answer in ["stable", "variable"]:
            return answer
        print("Invalid input. Please type 'stable' or 'variable'")

def recommend_model(answers):
    regulated = answers["regulated"]
    workload = answers["workload"]
    it_team = answers["it_team"]
    location_req = answers["location_req"]
    consortium = answers["consortium"]

    if regulated == "yes" and consortium == "yes":
        return "Community Cloud", "Regulated industry + consortium suggests shared controlled infrastructure"
    
    if regulated == "yes" and it_team == "yes":
        return "Private Cloud", "Regulated industry with internal IT team favors maximum contro"
    
    if workload == "variable":
        return "Public Cloud", "Highly variable workload benefits from elastic scaling"
    
    if workload == "stable" and it_team == "yes":
        return "Private Cloud", "Stable workload and IT team make private cost-effective"
    
    return "Hybrid Cloud", "Combination of requirements suggests hybrid flexibility"

def main():
    print("=== Cloud Deployment Model Advisor ===")

    answers = {
        "regulated": get_yes_no("Is your organisation in a heavily regulated industry?"),
        "workload": get_stability(),
        "it_team": get_yes_no("Do you have a dedicated IT operations team"),
        "location_req": get_yes_no("Is data location restriction require?"),
        "consortium": get_yes_no("Are you part of an industry consortium?")
    }

    model, reason = recommend_model(answers)

    print("\nRecommendation", model)
    print("Reason", reason)

if __name__ == "__main__":
    main()