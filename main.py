from kaggle_environments import make, evaluate
from submission import TimeValueAgent, time_value_agent
from random_agent import random_agent

"""Trainingsplatz zum testen der programmierten Bots."""


def main(gegner="random"):
    env = make("halite", debug=True)
    # time_value_agent = TimeValueAgent()
    env.agents = {
        "timevalue": time_value_agent,
        "random": random_agent,
    }
    env.run(["timevalue", "timevalue", "timevalue", "timevalue"])

    out = env.render(mode="html")
    f = open("wiederholung.html", "w")
    f.write(out)
    f.close
    print("Spielende! Der Spielablauf befindet sich in der Datei wiederholung.html")


if __name__ == "__main__":
    main()
