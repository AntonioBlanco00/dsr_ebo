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

sys.path.append('/opt/robocomp/lib')
console = Console(highlight=False)

from pydsr import *


# If RoboComp was compiled with Python bindings you can use InnerModel in Python
# import librobocomp_qmat
# import librobocomp_osgviewer
# import librobocomp_innermodel


class SpecificWorker(GenericWorker):
    def __init__(self, proxy_map, startup_check=False):
        super(SpecificWorker, self).__init__(proxy_map)
        self.Period = 2000

        # YOU MUST SET AN UNIQUE ID FOR THIS AGENT IN YOUR DEPLOYMENT. "_CHANGE_THIS_ID_" for a valid unique integer
        self.agent_id = 6
        self.g = DSRGraph(0, "pythonAgent", self.agent_id)

        try:
            #signals.connect(self.g, signals.UPDATE_NODE_ATTR, self.update_node_att)
            #signals.connect(self.g, signals.UPDATE_NODE, self.update_node)
            #signals.connect(self.g, signals.DELETE_NODE, self.delete_node)
            #signals.connect(self.g, signals.UPDATE_EDGE, self.update_edge)
            #signals.connect(self.g, signals.UPDATE_EDGE_ATTR, self.update_edge_att)
            #signals.connect(self.g, signals.DELETE_EDGE, self.delete_edge)
            console.print("signals connected")
        except RuntimeError as e:
            print(e)

        #Botón para hablar
        self.ui.pushButton.clicked.connect(self.button_clicked)

        #Botones de emociones
        self.ui.feliz.clicked.connect(lambda: self.emotion_clicked("Feliz"))
        self.ui.asco.clicked.connect(lambda: self.emotion_clicked("Asco"))
        self.ui.sorpresa.clicked.connect(lambda: self.emotion_clicked("Sorpresa"))
        self.ui.triste.clicked.connect(lambda: self.emotion_clicked("Triste"))
        self.ui.enfado.clicked.connect(lambda: self.emotion_clicked("Enfado"))
        self.ui.miedo.clicked.connect(lambda: self.emotion_clicked("Miedo"))

        # Movimiento asociado a emociones
        self.ui.feliz.clicked.connect(lambda: self.move_clicked("Feliz"))
        self.ui.asco.clicked.connect(lambda: self.move_clicked("Asco"))
        self.ui.sorpresa.clicked.connect(lambda: self.move_clicked("Sorpresa"))
        self.ui.triste.clicked.connect(lambda: self.move_clicked("Triste"))
        self.ui.enfado.clicked.connect(lambda: self.move_clicked("Enfado"))
        self.ui.miedo.clicked.connect(lambda: self.move_clicked("Miedo"))

        #Botones de movimiento
        self.ui.adelante.clicked.connect(lambda: self.move_clicked("Adelante"))
        self.ui.izquierda.clicked.connect(lambda: self.move_clicked("Izquierda"))
        self.ui.derecha.clicked.connect(lambda: self.move_clicked("Derecha"))
        self.ui.atras.clicked.connect(lambda: self.move_clicked("Atras"))
        self.ui.quieto.clicked.connect(lambda: self.move_clicked("Quieto"))


        if startup_check:
            self.startup_check()
        else:
            self.timer.timeout.connect(self.compute)
            self.timer.start(self.Period)

        self.gui = Ui_guiDlg()
        self.gui.setupUi(QMainWindow())

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
        print('SpecificWorker.compute...')


        return True

    def button_clicked(self):
        # Aquí puedes poner la lógica para manejar el botón "Enviar"
        texto = self.ui.plainTextEdit.toPlainText()
        print("Texto enviado:", texto)
        self.ui.plainTextEdit.clear()
        tts_node = self.g.get_node("TTS")

        if tts_node is None:
            print("No TTS")
            return False
        else:
            tts_node.attrs["to_say"] = Attribute(texto, self.agent_id)
            print("Atributo modificado")
            self.g.update_node(tts_node)

    def emotion_clicked(self, emo):
        emotion_node = self.g.get_node("Emotion")
        if emotion_node is None:
            print("No TTS")
            return False
        else:
            emotion_node.attrs["Emotion"] = Attribute(emo, self.agent_id)
            print("Atributo modificado")
            self.g.update_node(emotion_node)

    def move_clicked(self, mov):
        move_node = self.g.get_node("Move")
        if move_node is None:
            print("No TTS")
            return False
        else:
            move_node.attrs["Move"] = Attribute(mov, self.agent_id)
            print("Atributo modificado")
            self.g.update_node(move_node)


    def startup_check(self):
        QTimer.singleShot(200, QApplication.instance().quit)




    ######################
    # From the RoboCompSpeech you can call this methods:
    # self.speech_proxy.isBusy(...)
    # self.speech_proxy.say(...)
    # self.speech_proxy.setPitch(...)
    # self.speech_proxy.setTempo(...)



    # =============== DSR SLOTS  ================
    # =============================================

    def update_node_att(self, id: int, attribute_names: [str]):
        console.print(f"UPDATE NODE ATT: {id} {attribute_names}", style='green')

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
