# 72544_Homework2

loud Computing – Part 2 Exercises
This repository contains my solutions for Part 2 of the Cloud Computing course.
All tasks are implemented in Python and run locally in the terminal.
No external libraries were used. The programs simulate cloud concepts without connecting to real cloud providers.
The goal of these exercises was to better understand:
Cloud deployment models (Public, Private, Hybrid, Community)
IaaS resource management
Shared Responsibility Model
SaaS security configuration risks
Files
The project contains three Python files:

exercise1.py
exercise2.py
exercise3.py

Each file corresponds to one exercise from Part 2
Exercise 1 – Deployment Model Advisor

This program asks the user five questions about an organisation, such as

Is the industry regulated?
Is the workload stable or variable?
Is there a dedicated IT team?
Is there a data location requirement?
Is the organisation part of a consortium?

Based on the answers, the program recommends one of the cloud deployment models:
Public Cloud
Private Cloud
Hybrid Cloud
Community Cloud

The program validates input (yes/no and stable/variable) If the usr enters something incorrect it asks again
The recommendation is generated using simple decision logic.

Exercise 2 – IaaS Resource Provisioning Simulator

This program simulates a basic Infrastructure as a Service console.
The user can:
Provision a virtual machine
List running instances
Terminate an instance
Show total bill
Exit

Each instance has:

Name
Type (micro, small, medium, large)
Operating system (Linux or Windows)
Start time

The program calculates running time using the datetime module and computes cost based on hourly pricing
Windows instances cost more than Linux instances
Billing is calculated using fractional hours (based on seconds)
All data exists only during program execution and is not saved permanently

Exercise 3 – SaaS Security Quiz
This program is a small quiz that checks understanding of the Shared Responsibility Model in SaaS.
It contains 8 scenarios related to common SaaS tools such as:
Microsoft 365
Google Workspace
Salesforce
Zoom
Slack
Dropbox
GitHub

For each scenario, the user must answer:
Is this a security risk? (yes/no)
Who is responsible? (provider/customer)
The program gives 1 point for correct risk identification and 1 point for correct responsibility identification 

At the end the program shows the final score and assigns a level:
Novice
Developing
Proficient
Expert
Scenarios are shuffled randomly each time the program runs


HOW TO TEST:              

Exercise 1:
Try different combinations of answers and check if the recommended model changes.
Enter invalid input (for example “abc” to verify that the program asks again

Exercise 2:
Create several instances with different configurations.
Wait some seconds and use the list option to check that the cost increases over time
Terminate one instance and verify that the final cost is shown.
Try terminating a non-existing instance to test error handling.ʼ

Exercise 3:
Answer some questions correctly and some incorrectly to verify scoring
Run the program multiple times to check that scenario order changes
