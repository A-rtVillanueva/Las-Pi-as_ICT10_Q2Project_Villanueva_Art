from pyscript import document

def getinfo(event):
    first_name = document.getElementById("first_name").value

    last_name = document.getElementById("last_name").value

    english = float(document.getElementById("eng").value)

    science = float(document.getElementById("sci").value)

    math = float(document.getElementById("math").value)

    social_studies = float(document.getElementById("soc").value)

    medicine = float(document.getElementById("med").value)

    result = (english + science + math + social_studies + medicine) / 5

    output = f"""
    {first_name} {last_name} has graduated with a GWA of {round(result, 2)}."""

    

    document.getElementById("output").innerText = output