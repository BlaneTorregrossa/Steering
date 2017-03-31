import agent
from concretegame import SteeringBehaviours
from agent import Agent
from target import Target
from vectorlib import Vector2

def main():

    game = SteeringBehaviours("Blane Game")
    # make gameobjects to participate in game
    
    tstagent = Agent(Vector2(400, 400), Vector2(25, 25))
    game.addtobatch(tstagent)
    tsttarget = Target(Vector2(600, 400), Vector2(10, -10))
    game.addtobatch(tsttarget)
    tstagent.seek(tsttarget)
    game.run()
if __name__ == "__main__":
    main()