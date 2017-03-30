'''concrete game'''

from gametemplate import GameTemplate
class SteeringBehaviours(GameTemplate):
    
    '''need documentation'''

    def __init__(self, name):
        '''need documentation'''
        super(SteeringBehaviours, self).__init__()
        self._name = name
        self._gameobjects = []


    def addtobatch(self, gameobject):
        '''add gameobjects to this game'''
        self._gameobjects.append(gameobject)

    def update(self):
        '''update this games logic'''
        if not super(SteeringBehaviours, self)._update():
            return False
        for gameobject in self._gameobjects:
            gameobject.update(self._deltatime)
        return True

    def draw(self):
        '''draw all gameobjects added to this game'''
        super(SteeringBehaviours, self)._draw()
        for gameobject in self._gameobjects:
            gameobject.draw(self._screen)

    def run(self):
        '''need documentation'''
        if super(SteeringBehaviours, self)._startup():
            while self.update():
                self.draw()
        super(SteeringBehaviours, self)._shutdown()

class ConcreteGame(GameTemplate):
    '''need documentation'''

    def __init__(self, name):
        '''need documentation'''
        super(ConcreteGame, self).__init__()
        self._name = name
        self._gameobjects = []


    def addtobatch(self, gameobject):
        '''add gameobjects to this game'''
        self._gameobjects.append(gameobject)

    def update(self):
        '''update this games logic'''
        if not super(ConcreteGame, self)._update():
            return False
        return True

    def draw(self):
        '''draw all gameobjects added to this game'''
        super(ConcreteGame, self)._draw()

    def run(self):
        '''need documentation'''
        if super(ConcreteGame, self)._startup():
            while self.update():
                self.draw()
        super(ConcreteGame, self)._shutdown()