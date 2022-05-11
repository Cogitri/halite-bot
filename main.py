from kaggle_environments import make, evaluate
from submission import TimeValueAgent, random_agent

"""Trainingsplatz zum testen der programmierten Bots."""


def main(gegner="timevalue"):
    env = make("halite", debug=True)
    time_value_agent = TimeValueAgent()
    env.agents = {
        "timevalue": lambda obs, config: time_value_agent.run(obs, config),
        "random": random_agent,
    }
    env.run(["timevalue", gegner, gegner, gegner])

    out = env.render(mode="html")
    f = open("wiederholung.html", "w")
    f.write(out)
    f.close
    print("Spielende! Der Spielablauf befindet sich in der Datei wiederholung.html")


if __name__ == "__main__":
    main()
