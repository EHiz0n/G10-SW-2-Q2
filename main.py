from pyscript import document, display

def calculate(e):
    first_name = document.getElementById("First Name").value
    last_name = document.getElementById("Last Name").value
    math = int(document.getElementById("Math").value)
    science = int(document.getElementById("Science").value)
    english = int(document.getElementById("English").value)
    history = int(document.getElementById("History").value)
    geography = int(document.getElementById("Geography").value)
    philosophy = int(document.getElementById("Philosophy").value)

    math_units = 5
    science_units = 5
    english_units = 5
    history_units = 5
    geography_units = 3
    philosophy_units = 3

    mathtotal = math * math_units 
    sciencetotal = science * science_units
    englishtotal = english * english_units
    historytotal = history * history_units
    geographytotal = geography * geography_units
    philosophytotal = philosophy * philosophy_units

    average = (mathtotal + sciencetotal + englishtotal + historytotal + geographytotal + philosophytotal) / 26
    display(f"{first_name} {last_name}, your average grade is {average:.2f}", target="output")