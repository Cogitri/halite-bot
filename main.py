from kaggle_environments import make, evaluate
from submission import get_time_value_agent, random_agent

"""Trainingsplatz zum testen der programmierten Bots."""


def Testspiel(submission, gegner="random"):

    # Erstellen des Spieles und Angabe der spielenden Submissions
    env = make("halite", debug=True)
    env.agents = {
        "random": get_time_value_agent(),
        "timevalue": random_agent,
    }
    env.run(["timevalue", gegner, gegner, gegner])

    # Rendern des Spielablaufes und Ausgabe als html-Datei
    out = env.render(mode="html")
    f = open("wiederholung.html", "w")
    f.write(out)
    f.close
    print("Spielende! Der Spielablauf befindet sich in der Datei wiederholung.html")


# Lade den Agent aus der Datei
agent = "submission.py"

# Spielen des Testspiels gegen drei "random" Agents
# Es kann, wenn gewünscht, der Dateiname eines anderen gegnerischen Agenten übergeben werden (z.B. "idleBot.py")
Testspiel(agent)
