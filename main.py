import agent
import datetime
from concretegame import SteeringBehaviours
from agent import Agent
from target import Target
from vectorlib import Vector2

def main():

    game = SteeringBehaviours("Blane Game")
    # make gameobjects to participate in game


    tstagent = Agent(Vector2(350, 400), Vector2(25, 25))
    tsttarget = Target(Vector2(300, 350), Vector2(10, -10))
    game.addtobatch(tstagent)
    game.addtobatch(tsttarget)
    tstagent.seek(tsttarget)
    tsttarget.flee(tstagent)
    tstagent.update(1)
    tsttarget.update(1)
    game.run()

if __name__ == "__main__":
    main()