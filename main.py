from kaggle_environments import make, evaluate
from submission import get_time_value_agent, random_agent

"""Trainingsplatz zum testen der programmierten Bots."""


def main(gegner="random"):
    env = make("halite", debug=True)
    env.agents = {
        "random": get_time_value_agent(),
        "timevalue": random_agent,
    }
    env.run(["timevalue", gegner, gegner, gegner])

    out = env.render(mode="html")
    f = open("wiederholung.html", "w")
    f.write(out)
    f.close
    print("Spielende! Der Spielablauf befindet sich in der Datei wiederholung.html")


if __name__ == "__main__":
    main()
