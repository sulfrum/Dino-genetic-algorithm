"""
Author: Matheus Santos
Description: this class manage the entire game state.
"""
from tkinter import Canvas, Tk, mainloop
from PIL import Image, ImageTk
from classes.CollisionMonitor import ColisionMonitor
from classes.Dino import Dino
from classes.Cactus import Cactus
from classes.FlyingDino import FlyingDino
from classes.CollisionMonitor import ColisionMonitor
from classes.ObstacleGenerator import ObstacleGenerator

class GameController:
    def __init__(self, mode):
        #can be either a train or a game
        self.mode = mode
        self.master = Tk()
        self.canvas = Canvas(self.master, width=800, height=800, bg='#eee')
        self.colisionMonitor = ColisionMonitor(self.master, self.canvas)
        self.dinos = []
        self.obstacles = []
        self.colisionMonitor = None
        self.obstacleGenerator = None
    def run(self):
        if(self.mode == "game"):
            self.canvas.pack()
            self.prepareGame()
            mainloop()
    # create game elements
    def prepareGame(self):
        self.dinos.append(Dino(self.master, self.canvas))
        """ self.obstacles.append(Cactus(self.master, self.canvas))
        self.obstacles.append(FlyingDino(self.master, self.canvas)) """
        self.obstacleGenerator = ObstacleGenerator(self.master, self.canvas)
        self.obstacleGenerator.run()
        self.colisionMonitor = ColisionMonitor(self.master, self.canvas, self.dinos, self.obstacleGenerator.obstacles)
        self.colisionMonitor.start()