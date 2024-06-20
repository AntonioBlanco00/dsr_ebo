#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#    Copyright (C) 2024 by YOUR NAME HERE
#
#    This file is part of RoboComp
#
#    RoboComp is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    RoboComp is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with RoboComp.  If not, see <http://www.gnu.org/licenses/>.
#

from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QApplication
from rich.console import Console
from genericworker import *
import interfaces as ifaces

import time
import sys
from random import *
import json
import pandas as pd
import threading
import cv2

sys.path.append('/opt/robocomp/lib')
console = Console(highlight=False)

from pydsr import *


# If RoboComp was compiled with Python bindings you can use InnerModel in Python
# import librobocomp_qmat
# import librobocomp_osgviewer
# import librobocomp_innermodel

class Movements(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.accionaleatoria = False
        self.randomfunctions = False
        self.instlastaction = time.time()
        self.start_time = self.instlastaction
        self.timemax = 1
        self.timemin = 1
        self.velmax = 20
        self.velmin = 20
        self.quieto = True
        self.angmax = 90
        self.angmin = -self.angmax
        self.frecmovementmin = 1
        self.frecmovementmax = 3
        self.desvio_respect_start = 0
        self.sec = randint(self.frecmovementmin, self.frecmovementmax)
        self.robot = None
        self.stopped = False
        self.posestadoactual = 4
        self.estadoactual = "Neutral"
        self.v_rad = 0.6


    def run(self):
        start = time.time()

        while not self.stopped:
            if self.quieto != True:
                if time.time() - start > self.sec:
                    #if not self.accionaleatoria:
                        # self.randomMovementrotate()
                    choice([self.randomMovementbackfront(), self.randomMovementrotate()])
                    start = time.time()
                    self.sec = uniform(self.frecmovementmin, self.frecmovementmax)

    def randomMovementrotate(self):

        randomtime = uniform(self.timemin, self.timemax)
        # speed = randint(self.velmin, self.velmax)
        angle = randint(self.angmin, self.angmax)
        tact = time.time()
        while (time.time() <= tact + randomtime):
            self.robot.setBaseSpeed(0, angle)
        self.desvio_respect_start += angle*randomtime
        # tact = time.time()
        # while (time.time() <= tact + randomtime):
        #     self.robot.setBaseSpeed(-speed, angle)
        self.robot.setBaseSpeed(0, 0)
        self.start_time = time.time()
        self.sec = uniform(self.frecmovementmin, self.frecmovementmax)

    def randomMovementbackfront(self):
        tact = time.time()
        randomtime = uniform(self.timemin, self.timemax)
        speed = randint(self.velmin, self.velmax)
        while (time.time() <= tact + randomtime):
            self.robot.setBaseSpeed(speed, 0)
            self.robot.setBaseSpeed(-speed, 0)
        self.robot.setBaseSpeed(0, 0)
        self.start_time = time.time()
        self.sec = uniform(self.frecmovementmin, self.frecmovementmax)

    def afirmacion(self):
        tact = time.time()
        while (time.time() <= tact + 0.15):
            self.robot.setBaseSpeed(100, 0)
        tact = time.time()
        while (time.time() <= tact + 0.3):
            self.robot.setBaseSpeed(-100, 0)
        tact = time.time()
        while (time.time() <= tact + 0.15):
            self.robot.setBaseSpeed(100, 0)
        self.robot.setBaseSpeed(0, 0)
        self.instlastaction = time.time()

    def negacion(self):
        tact = time.time()
        while (time.time() <= tact + 0.15):
            self.robot.setBaseSpeed(100, 90)
        tact = time.time()
        while (time.time() <= tact + 0.3):
            self.robot.setBaseSpeed(100, -90)
        tact = time.time()
        while (time.time() <= tact + 0.15):
            self.robot.setBaseSpeed(100, 90)
        self.robot.setBaseSpeed(0,0)
        self.instlastaction = time.time()

    def vuelta(self):
        tact = time.time()
        while (time.time() <= tact + 4):
            self.robot.setBaseSpeed(0,90)
        self.robot.setBaseSpeed(0,0)

    def giro_ocho(self):
        tact = time.time()
        while (time.time() <= tact + 0.7):
            self.robot.setBaseSpeed(-100, 60)
        tact = time.time()
        while (time.time() <= tact + 0.7):
            self.robot.setBaseSpeed(-100, -60)
        tact = time.time()
        while (time.time() <= tact + 4):
            self.robot.setBaseSpeed(0, 90)
        tact = time.time()
        while (time.time() <= tact + 1):
            self.robot.setBaseSpeed(60,0)
        self.robot.setBaseSpeed(0,0)

    def girito(self):
        tact = time.time()
        while (time.time() <= tact + 0.3):
            self.robot.setBaseSpeed(0, 100)
        tact = time.time()
        while (time.time() <= tact + 0.6):
            self.robot.setBaseSpeed(0, -100)
        tact = time.time()
        while (time.time() <= tact + 0.6):
            self.robot.setBaseSpeed(0, 100)
        tact = time.time()
        while (time.time() <= tact + 0.6):
            self.robot.setBaseSpeed(0, -100)
        tact = time.time()
        while (time.time() <= tact + 0.3):
            self.robot.setBaseSpeed(0, 100)
        self.robot.setBaseSpeed(0,0)


    def adelante(self):
        self.robot.setBaseSpeed(50, 0)
    def atras(self):
        self.robot.setBaseSpeed(-50, 0)
    def izquierda(self):
        self.robot.setBaseSpeed(0, -45)
    def derecha(self):
        self.robot.setBaseSpeed(0, 45)

    def posicion_inicial(self):
        tiempo_rot = abs(self.desvio_respect_start)/90
        if(self.desvio_respect_start > 0):
            tact = time.time()
            while (time.time() <= tact + tiempo_rot):
                self.robot.setBaseSpeed(0, -90)
            self.robot.setBaseSpeed(0, 0)
        else:
            tact = time.time()
            while (time.time() <= tact + tiempo_rot):
                self.robot.setBaseSpeed(0, 90)
            self.robot.setBaseSpeed(0, 0)
        self.desvio_respect_start = 0

    def stop(self):
        self.stopped = True
        self.join()

class SpecificWorker(GenericWorker):
    def __init__(self, proxy_map, startup_check=False):
        super(SpecificWorker, self).__init__(proxy_map)
        self.Period = 2000

        # YOU MUST SET AN UNIQUE ID FOR THIS AGENT IN YOUR DEPLOYMENT. "_CHANGE_THIS_ID_" for a valid unique integer
        self.agent_id = 9
        self.g = DSRGraph(0, "pythonAgent", self.agent_id)
        self.movements = Movements()
        try:
            signals.connect(self.g, signals.UPDATE_NODE_ATTR, self.update_node_att)
            #signals.connect(self.g, signals.UPDATE_NODE, self.update_node)
            #signals.connect(self.g, signals.DELETE_NODE, self.delete_node)
            #signals.connect(self.g, signals.UPDATE_EDGE, self.update_edge)
            #signals.connect(self.g, signals.UPDATE_EDGE_ATTR, self.update_edge_att)
            #signals.connect(self.g, signals.DELETE_EDGE, self.delete_edge)
            console.print("signals connected")
        except RuntimeError as e:
            print(e)

        if startup_check:
            self.startup_check()
        else:
            self.timer.timeout.connect(self.compute)
            self.timer.start(self.Period)

        # Se leen los valores de inicio de los atributos, y se almacenan para que funcione el código.
        print("Leyendo valores iniciales de los atributos de Emoción y Movimiento")
        if self.g.get_id_from_name("Emotion") is not None:
            emotion_node = self.g.get_node("Emotion")
        else:
            pass

        if self.g.get_id_from_name("Move") is not None:
            move_node = self.g.get_node("Move")
        else:
            pass
        
        print("Cargando valores iniciales de los atributos de Emoción y Movimiento")
        self.last_emotion = emotion_node.attrs["Emotion"].value
        self.last_move = move_node.attrs["Move"].value
        
        if self.last_emotion == emotion_node.attrs["Emotion"].value and self.last_move == move_node.attrs["Move"].value:
            print("Valores iniciales cargados correctamente")
        else:
            print("Valores iniciales error al cargar (Puede afectar al inicio del programa, pero no es un problema grave)")

    def __del__(self):
        """Destructor"""

    def setParams(self, params):
        # try:
        #	self.innermodel = InnerModel(params["InnerModelPath"])
        # except:
        #	traceback.print_exc()
        #	print("Error reading config params")
        return True


    @QtCore.Slot()
    def compute(self):
        #print('SpecificWorker.compute...')
        # computeCODE
        return True

    def estadoQuieto(self):
        self.movements.quieto = True
        if self.movements.robot == None:
            self.differentialrobot_proxy.setSpeedBase(0, 0)
        else:
            self.movements.robot.setBaseSpeed(0, 0)

    def mover_adelante(self):
        print("Iniciando movimiento")
        if self.movements.robot == None:
            self.differentialrobot_proxy.setSpeedBase(160, 0)
        else:
            self.movements.adelante()

    def mover_atras(self):
        if self.movements.robot == None:
            self.differentialrobot_proxy.setSpeedBase(-160, 0)
        else:
            self.movements.atras()

    def mover_izquierda(self):
        print("Izquierda pulsado")
        if self.movements.robot == None:
            self.differentialrobot_proxy.setSpeedBase(0, -self.movements.v_rad)
        else:
            self.movements.izquierda()

    def mover_derecha(self):
        if self.movements.robot == None:
            self.differentialrobot_proxy.setSpeedBase(0, self.movements.v_rad)
        else:
            self.movements.derecha()

    def mover_enfado(self):
        move_node = self.g.get_node("Move")
        vel = 160
        time.sleep(1.3)
        self.differentialrobot_proxy.setSpeedBase(vel, 0)
        time.sleep(0.5)
        self.differentialrobot_proxy.setSpeedBase(0, -vel)
        time.sleep(0.5)
        self.differentialrobot_proxy.setSpeedBase(0, 0)
        time.sleep(1)
        self.differentialrobot_proxy.setSpeedBase(0, vel)
        time.sleep(1)
        self.differentialrobot_proxy.setSpeedBase(0, 0)
        time.sleep(1)
        self.differentialrobot_proxy.setSpeedBase(0, -vel)
        time.sleep(0.5)
        self.differentialrobot_proxy.setSpeedBase(0, 0)
        time.sleep(1)
        self.differentialrobot_proxy.setSpeedBase(-vel, 0)
        time.sleep(0.5)
        move_node.attrs["Move"] = Attribute("Quieto", self.agent_id)
        self.g.update_node(move_node)

    def mover_triste(self):
        move_node = self.g.get_node("Move")
        vel = 1
        time.sleep(1.3)
        self.differentialrobot_proxy.setSpeedBase(-20, 0)
        time.sleep(2)
        self.differentialrobot_proxy.setSpeedBase(0, 0)
        time.sleep(1)
        self.differentialrobot_proxy.setSpeedBase(0, vel)
        time.sleep(4)
        self.differentialrobot_proxy.setSpeedBase(0, 0)
        time.sleep(1)
        self.differentialrobot_proxy.setSpeedBase(0, -vel)
        time.sleep(4)
        self.differentialrobot_proxy.setSpeedBase(20, 0)
        time.sleep(2)
        move_node.attrs["Move"] = Attribute("Quieto", self.agent_id)
        self.g.update_node(move_node)

    def mover_feliz(self):
        move_node = self.g.get_node("Move")
        vel = 160
        time.sleep(1.3)
        self.differentialrobot_proxy.setSpeedBase(0, vel)
        time.sleep(3.7)
        self.differentialrobot_proxy.setSpeedBase(vel, 0)
        time.sleep(1)
        self.differentialrobot_proxy.setSpeedBase(-vel, 0)
        time.sleep(1)
        self.differentialrobot_proxy.setSpeedBase(vel, 0)
        time.sleep(1)
        self.differentialrobot_proxy.setSpeedBase(0, 0)
        time.sleep(1)
        self.differentialrobot_proxy.setSpeedBase(-vel, 0)
        time.sleep(1)
        move_node.attrs["Move"] = Attribute("Quieto", self.agent_id)
        self.g.update_node(move_node)

    def mover_miedo(self):
        move_node = self.g.get_node("Move")
        vel = 160
        time.sleep(1.3)
        self.differentialrobot_proxy.setSpeedBase(-vel, 0)
        time.sleep(1)
        ###
        i = 0
        while i < 10:
            self.differentialrobot_proxy.setSpeedBase(0, vel)
            time.sleep(0.1)
            self.differentialrobot_proxy.setSpeedBase(0, -vel)
            time.sleep(0.1)
            i = i+1
        ###
        self.differentialrobot_proxy.setSpeedBase(vel, 0)
        time.sleep(1)
        move_node.attrs["Move"] = Attribute("Quieto", self.agent_id)
        self.g.update_node(move_node)

    def mover_sorpresa(self):
        move_node = self.g.get_node("Move")
        vel = 160
        time.sleep(1.3)

        self.differentialrobot_proxy.setSpeedBase(vel, 0)
        time.sleep(0.5)
        self.differentialrobot_proxy.setSpeedBase(0, -vel)
        time.sleep(0.5)
        self.differentialrobot_proxy.setSpeedBase(0, 0)
        time.sleep(1)
        self.differentialrobot_proxy.setSpeedBase(0, vel)
        time.sleep(1)
        self.differentialrobot_proxy.setSpeedBase(0, 0)
        time.sleep(1)
        self.differentialrobot_proxy.setSpeedBase(0, -vel)
        time.sleep(0.5)
        self.differentialrobot_proxy.setSpeedBase(0, 0)
        time.sleep(1)
        self.differentialrobot_proxy.setSpeedBase(-vel, 0)
        time.sleep(0.5)

        move_node.attrs["Move"] = Attribute("Quieto", self.agent_id)
        self.g.update_node(move_node)

    def mover_asco(self):
        move_node = self.g.get_node("Move")
        vel = 30
        time.sleep(1.3)
        self.differentialrobot_proxy.setSpeedBase(-vel, 0)
        time.sleep(1.2)
        ###
        i = 0
        while i < 2:
            self.differentialrobot_proxy.setSpeedBase(0, vel)
            time.sleep(0.3)
            self.differentialrobot_proxy.setSpeedBase(0, -vel)
            time.sleep(0.3)
            i = i+1
        i = 0

        while i < 8:
            self.differentialrobot_proxy.setSpeedBase(0, 160)
            time.sleep(0.1)
            self.differentialrobot_proxy.setSpeedBase(0, -160)
            time.sleep(0.1)
            i = i+1
        ###
        self.differentialrobot_proxy.setSpeedBase(vel, 0)
        time.sleep(1.2)
        move_node.attrs["Move"] = Attribute("Quieto", self.agent_id)
        self.g.update_node(move_node)

    def startup_check(self):
        print(f"Testing RoboCompDifferentialRobot.TMechParams from ifaces.RoboCompDifferentialRobot")
        test = ifaces.RoboCompDifferentialRobot.TMechParams()
        QTimer.singleShot(200, QApplication.instance().quit)


    def actualizar_move(self, move_node):
        if move_node.attrs["Move"].value == "Adelante":
            self.mover_adelante()
        elif move_node.attrs["Move"].value == "Izquierda":
            self.mover_izquierda()
        elif move_node.attrs["Move"].value == "Derecha":
            self.mover_derecha()
        elif move_node.attrs["Move"].value == "Atras":
            self.mover_atras()
        elif move_node.attrs["Move"].value == "Quieto":
            self.estadoQuieto()

        # Movimientos de emociones
        elif move_node.attrs["Move"].value == "Enfado":
            self.mover_enfado()
        elif move_node.attrs["Move"].value == "Triste":
            self.mover_triste()
        elif move_node.attrs["Move"].value == "Feliz":
            self.mover_feliz()
        elif move_node.attrs["Move"].value == "Miedo":
            self.mover_miedo()
        elif move_node.attrs["Move"].value == "Sorpresa":
            self.mover_sorpresa()
        elif move_node.attrs["Move"].value == "Asco":
            self.mover_asco()
        else:
            self.estadoQuieto()
            pass

    def actualizar_cara(self, emotion_node):
        if emotion_node.attrs["Emotion"].value == "Triste":
            self.emotionalmotor_proxy.expressSadness()
        elif emotion_node.attrs["Emotion"].value == "Asco":
            self.emotionalmotor_proxy.expressDisgust()
        elif emotion_node.attrs["Emotion"].value == "Sorpresa":
            self.emotionalmotor_proxy.expressSurprise()
        elif emotion_node.attrs["Emotion"].value == "Enfado":
            self.emotionalmotor_proxy.expressAnger()
        elif emotion_node.attrs["Emotion"].value == "Miedo":
            self.emotionalmotor_proxy.expressFear()
        elif emotion_node.attrs["Emotion"].value == "Feliz":
            self.emotionalmotor_proxy.expressJoy()
        else:
            pass

    ######################
    # From the RoboCompDifferentialRobot you can call this methods:
    # self.differentialrobot_proxy.correctOdometer(...)
    # self.differentialrobot_proxy.getBasePose(...)
    # self.differentialrobot_proxy.getBaseState(...)
    # self.differentialrobot_proxy.resetOdometer(...)
    # self.differentialrobot_proxy.setOdometer(...)
    # self.differentialrobot_proxy.setOdometerPose(...)
    # self.differentialrobot_proxy.setSpeedBase(...)
    # self.differentialrobot_proxy.stopBase(...)

    ######################
    # From the RoboCompDifferentialRobot you can use this types:
    # RoboCompDifferentialRobot.TMechParams

    ######################
    # From the RoboCompEmotionalMotor you can call this methods:
    # self.emotionalmotor_proxy.expressAnger(...)
    # self.emotionalmotor_proxy.expressDisgust(...)
    # self.emotionalmotor_proxy.expressFear(...)
    # self.emotionalmotor_proxy.expressJoy(...)
    # self.emotionalmotor_proxy.expressSadness(...)
    # self.emotionalmotor_proxy.expressSurprise(...)
    # self.emotionalmotor_proxy.isanybodythere(...)
    # self.emotionalmotor_proxy.listening(...)
    # self.emotionalmotor_proxy.pupposition(...)
    # self.emotionalmotor_proxy.talking(...)



    # =============== DSR SLOTS  ================
    # =============================================

    def update_node_att(self, id: int, attribute_names: [str]):
        emotion_node = self.g.get_node("Emotion")
        if emotion_node.attrs["Emotion"].value != self.last_emotion:
            self.actualizar_cara(emotion_node)
            self.last_emotion = emotion_node.attrs["Emotion"].value
            console.print(f"UPDATE NODE ATT: {id} {attribute_names}", style='green')
        else:
            pass

        move_node = self.g.get_node("Move")
        if "Move" in move_node.attrs:
            if move_node.attrs["Move"].value != self.last_move:
                self.actualizar_move(move_node)
                self.last_move = move_node.attrs["Move"].value
                console.print(f"UPDATE NODE ATT: {id} {attribute_names}", style='green')
            else:
                pass
        else:
            pass

    def update_node(self, id: int, type: str):
        console.print(f"UPDATE NODE: {id} {type}", style='green')

    def delete_node(self, id: int):
        console.print(f"DELETE NODE:: {id} ", style='green')

    def update_edge(self, fr: int, to: int, type: str):
        console.print(f"UPDATE EDGE: {fr} to {type}", type, style='green')

    def update_edge_att(self, fr: int, to: int, type: str, attribute_names: [str]):
        console.print(f"UPDATE EDGE ATT: {fr} to {type} {attribute_names}", style='green')

    def delete_edge(self, fr: int, to: int, type: str):
        console.print(f"DELETE EDGE: {fr} to {type} {type}", style='green')
