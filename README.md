# Automate-everything-with-python

Folder Structure
AgendaRolePlayerAutomation

Libraries Used: FPDF, Pandas, Numpy, Datetime
Language Used: Python

Background: Automating the agenda making for weekly Toastmasters meetings. 
CAMTMagenda.xlsx is a google sheet that you can share with you club or VPE.
it contains two workbooks
1. Agenda : the agenda template for a weekly toastmaster
   
Structure

Time | Agenda | Role Player | Time Allotted

Time: The first row of the file needs to be the starting time of your TM meeting. the rest of the time will be calculated by "time allotted" for the particular activity
Agenda: description of activities planned
Role Player: the role player (eg, SAA, TTM) that is responsible for the agenda activity
Time Allotted: Time dedicated for that particular activity as per the agenda

2. Role Players: the role players list for the upcoming meeting

Structure

Role Name | Role Player Name
Role Name: the roles you wish to have for your TM meeting
Role Player Name: the members who are filling those roles

Caution! 

Make sure to do a spellcheck for your "Role Name" column. it should be same as you mention in the "Role Player" column in the Agenda workbook.

Execute main_file.py

it will automatically pick data from the excel and give you your agenda as pdf. Dive into the code for step by step explanation

Happy learning

