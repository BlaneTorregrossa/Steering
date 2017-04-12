import datetime

from agent import Agent
from centertarget import CenterTarget
from concretegame import SteeringBehaviours
from target import Target
from vectorlib import Vector2


def main():

    game = SteeringBehaviours("Blane Game")
    # make gameobjects to participate in game

    #stays
    tstagent = Agent(Vector2(300, 400), Vector2(20, 20))
    tsttarget = Target(Vector2(300, 350), Vector2(-11, 11))
    tstcenter = CenterTarget(Vector2(400, 300))
    game.addtobatch(tstcenter)
    game.addtobatch(tstagent)
    game.addtobatch(tsttarget)
    

   
    

    game.run()

if __name__ == "__main__":
    main()
