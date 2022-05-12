# from kaggle_environments import make, evaluate
# from submission import TimeValueAgent, time_value_agent
# from random_agent import random_agent

# """Trainingsplatz zum testen der programmierten Bots."""


# def main(gegner="random"):
#     env = make("halite", debug=True)
#     # time_value_agent = TimeValueAgent()
#     env.agents = {
#         "timevalue": time_value_agent,
#         "random": random_agent,
#     }
#     env.run(["timevalue", "timevalue", "timevalue", "timevalue"])

#     out = env.render(mode="html")
#     f = open("wiederholung.html", "w")
#     f.write(out)
#     f.close
#     print("Spielende! Der Spielablauf befindet sich in der Datei wiederholung.html")


# if __name__ == "__main__":
#     main()

from kaggle_environments import evaluate, make

# pip install kaggle_environments
# pip install requests

"""Trainingsplatz zum testen der programmierten Bots."""


def Testspiel(submission, gegner="random"):

    # Erstellen des Spieles und Angabe der spielenden Submissions
    env = make("halite", debug=True)
    env.run([submission, gegner, gegner, gegner])

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
