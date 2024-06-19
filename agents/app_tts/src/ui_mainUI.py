# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_guiDlg(object):
    def setupUi(self, guiDlg):
        if not guiDlg.objectName():
            guiDlg.setObjectName(u"guiDlg")
        guiDlg.resize(800, 600)
        guiDlg.setCursor(QCursor(Qt.ArrowCursor))
        guiDlg.setMouseTracking(True)
        guiDlg.setWindowOpacity(1.000000000000000)
        guiDlg.setAutoFillBackground(False)
        guiDlg.setLocale(QLocale(QLocale.Spanish, QLocale.Spain))
        self.pushButton = QPushButton(guiDlg)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(650, 150, 89, 41))
        self.plainTextEdit = QPlainTextEdit(guiDlg)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(30, 120, 581, 101))
        self.plainTextEdit.setFrameShape(QFrame.StyledPanel)
        self.plainTextEdit.setFrameShadow(QFrame.Sunken)
        self.plainTextEdit.setLineWidth(1)
        self.textEdit = QTextEdit(guiDlg)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 80, 381, 31))
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.setStyleSheet(u"background-color: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setFrameShadow(QFrame.Sunken)
        self.textEdit.setReadOnly(True)
        self.feliz = QPushButton(guiDlg)
        self.feliz.setObjectName(u"feliz")
        self.feliz.setGeometry(QRect(40, 320, 90, 60))
        self.feliz.setStyleSheet(u"")
        self.feliz.setIconSize(QSize(88, 58))
        self.asco = QPushButton(guiDlg)
        self.asco.setObjectName(u"asco")
        self.asco.setGeometry(QRect(150, 320, 90, 60))
        self.asco.setStyleSheet(u"")
        self.asco.setIconSize(QSize(88, 58))
        self.sorpresa = QPushButton(guiDlg)
        self.sorpresa.setObjectName(u"sorpresa")
        self.sorpresa.setGeometry(QRect(260, 400, 90, 60))
        self.sorpresa.setStyleSheet(u"")
        self.sorpresa.setIconSize(QSize(88, 58))
        self.triste = QPushButton(guiDlg)
        self.triste.setObjectName(u"triste")
        self.triste.setGeometry(QRect(150, 400, 90, 60))
        self.triste.setStyleSheet(u"")
        self.triste.setIconSize(QSize(88, 58))
        self.enfado = QPushButton(guiDlg)
        self.enfado.setObjectName(u"enfado")
        self.enfado.setGeometry(QRect(40, 400, 90, 60))
        self.enfado.setStyleSheet(u"")
        self.enfado.setIconSize(QSize(88, 58))
        self.miedo = QPushButton(guiDlg)
        self.miedo.setObjectName(u"miedo")
        self.miedo.setGeometry(QRect(260, 320, 90, 60))
        self.miedo.setStyleSheet(u"")
        self.miedo.setIconSize(QSize(88, 58))
        self.textEdit_2 = QTextEdit(guiDlg)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(40, 270, 381, 31))
        self.textEdit_2.setAutoFillBackground(True)
        self.textEdit_2.setStyleSheet(u"background-color: transparent;")
        self.textEdit_2.setFrameShape(QFrame.NoFrame)
        self.textEdit_2.setFrameShadow(QFrame.Sunken)
        self.textEdit_2.setReadOnly(True)
        self.adelante = QPushButton(guiDlg)
        self.adelante.setObjectName(u"adelante")
        self.adelante.setGeometry(QRect(558, 320, 101, 25))
        self.izquierda = QPushButton(guiDlg)
        self.izquierda.setObjectName(u"izquierda")
        self.izquierda.setGeometry(QRect(500, 350, 89, 25))
        self.derecha = QPushButton(guiDlg)
        self.derecha.setObjectName(u"derecha")
        self.derecha.setGeometry(QRect(620, 350, 89, 25))
        self.atras = QPushButton(guiDlg)
        self.atras.setObjectName(u"atras")
        self.atras.setGeometry(QRect(560, 380, 101, 25))
        self.quieto = QPushButton(guiDlg)
        self.quieto.setObjectName(u"quieto")
        self.quieto.setGeometry(QRect(550, 420, 121, 25))
        self.textEdit_3 = QTextEdit(guiDlg)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(460, 270, 381, 31))
        self.textEdit_3.setAutoFillBackground(True)
        self.textEdit_3.setStyleSheet(u"background-color: transparent;")
        self.textEdit_3.setFrameShape(QFrame.NoFrame)
        self.textEdit_3.setFrameShadow(QFrame.Sunken)
        self.textEdit_3.setReadOnly(True)

        self.retranslateUi(guiDlg)

        QMetaObject.connectSlotsByName(guiDlg)
    # setupUi

    def retranslateUi(self, guiDlg):
        guiDlg.setWindowTitle(QCoreApplication.translate("guiDlg", u"Aplicaci\u00f3n TTS", None))
        self.pushButton.setText(QCoreApplication.translate("guiDlg", u"Enviar", None))
        self.textEdit.setHtml(QCoreApplication.translate("guiDlg", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Escribe aqu\u00ed lo que quieres que diga EBO:</span></p></body></html>", None))
        self.feliz.setText(QCoreApplication.translate("guiDlg", u"ALEGRE", None))
        self.asco.setText(QCoreApplication.translate("guiDlg", u"ASCO", None))
        self.sorpresa.setText(QCoreApplication.translate("guiDlg", u"SORPRESA", None))
        self.triste.setText(QCoreApplication.translate("guiDlg", u"TRISTEZA", None))
        self.enfado.setText(QCoreApplication.translate("guiDlg", u"ENFADO", None))
        self.miedo.setText(QCoreApplication.translate("guiDlg", u"MIEDO", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("guiDlg", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Controla el estado de \u00e1nimo de EBO:</span></p></body></html>", None))
        self.adelante.setText(QCoreApplication.translate("guiDlg", u"Adelante", None))
        self.izquierda.setText(QCoreApplication.translate("guiDlg", u"Izquierda", None))
        self.derecha.setText(QCoreApplication.translate("guiDlg", u"Derecha", None))
        self.atras.setText(QCoreApplication.translate("guiDlg", u"Atr\u00e1s", None))
        self.quieto.setText(QCoreApplication.translate("guiDlg", u"STOP", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("guiDlg", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Controla el movimiento de EBO:</span></p></body></html>", None))
    # retranslateUi

