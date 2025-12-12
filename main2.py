from pyscript import document

club_info = {
    "Advanced Math": """
    Explore higher-level math, solve challenging problems, and prepare for competitions. Perfect for students who love logic and numbers.
    """,

    "Advanced Science": """
    Dive deeper into biology, chemistry, physics, and experiments. Great for curious learners who enjoy hands-on science.
    """,

    "Advanced Research": """
    Learn how to research properly, write academically, and analyze data. Ideal for future scholars and critical thinkers.
    """,

    "Advanced Med": """
    Study the basics of medicine, anatomy, and health science. Best for students interested in medical careers.
    """,

    "Faculty Aid": """
    Assist teachers, organize materials, and help with school tasks. Builds responsibility, leadership, and service skills.
    """
}

def getinfo(event=None):
    selected = document.querySelector("select").value
    info_text = club_info.get(selected, "Club not found.")
    document.getElementById("output").innerText = info_text