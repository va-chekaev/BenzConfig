from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                               QPushButton, QSizePolicy, QTabWidget, QWidget)
import files_rc


class Ui_root(object):
    def setupUi(self, root):
        if not root.objectName():
            root.setObjectName(u"root")

        root.resize(560, 450)
        root.setMinimumSize(QSize(560, 450))
        root.setMaximumSize(QSize(560, 670))
        root.setCursor(QCursor(Qt.ArrowCursor))
        root.setMouseTracking(False)
        icon = QIcon()
        icon.addFile(u":/icon/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        root.setWindowIcon(icon)
        root.setWindowOpacity(1.000000000000000)
        root.setAutoFillBackground(False)
        root.setStyleSheet(u"")
        root.setDocumentMode(False)
        root.setTabShape(QTabWidget.Rounded)

        self.grid_w = QWidget(root)
        self.grid_w.setObjectName(u"grid_w")
        self.grid_w.setStyleSheet(u"")

        self.inputSummer = QLineEdit(self.grid_w)
        self.inputSummer.setObjectName(u"inputSummer")
        self.inputSummer.setGeometry(QRect(20, 40, 241, 31))
        self.inputSummer.setLayoutDirection(Qt.LeftToRight)
        self.inputSummer.setStyleSheet(u"")
        self.inputSummer.setInputMethodHints(Qt.ImhNone)
        self.inputSummer.setMaxLength(32767)
        self.inputSummer.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.inputSummer.setDragEnabled(False)

        self.outSummer = QLabel(self.grid_w)
        self.outSummer.setObjectName(u"outSummer")
        self.outSummer.setGeometry(QRect(20, 130, 241, 281))
        self.outSummer.setStyleSheet(u"background-color: rgba(230, 230, 230, 230);")
        self.outSummer.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.btnSummer = QPushButton(self.grid_w)
        self.btnSummer.setObjectName(u"btnSummer")
        self.btnSummer.setGeometry(QRect(20, 80, 241, 41))
        self.btnSummer.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSummer.setStyleSheet(u"")
        self.btnSummer.setInputMethodHints(Qt.ImhNone)

        self.btnWinter = QPushButton(self.grid_w)
        self.btnWinter.setObjectName(u"btnWinter")
        self.btnWinter.setGeometry(QRect(300, 80, 241, 41))
        self.btnWinter.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnWinter.setStyleSheet(u"")

        self.outWinter = QLabel(self.grid_w)
        self.outWinter.setObjectName(u"outWinter")
        self.outWinter.setGeometry(QRect(300, 130, 241, 281))
        self.outWinter.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.outWinter.setInputMethodHints(Qt.ImhNone)
        self.outWinter.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.inputWinter = QLineEdit(self.grid_w)
        self.inputWinter.setObjectName(u"inputWinter")
        self.inputWinter.setGeometry(QRect(300, 40, 241, 31))
        self.inputWinter.setStyleSheet(u"")
        self.inputWinter.setMaxLength(10)

        self.label_s = QLabel(self.grid_w)
        self.label_s.setObjectName(u"label_s")
        self.label_s.setGeometry(QRect(20, 10, 241, 21))
        self.label_s.setStyleSheet(u"")

        self.lable_w = QLabel(self.grid_w)
        self.lable_w.setObjectName(u"lable_w")
        self.lable_w.setGeometry(QRect(300, 10, 241, 21))
        self.lable_w.setStyleSheet(u"")

        # about

        self.btnAbout = QPushButton(self.grid_w)
        self.btnAbout.setObjectName(u"btnAbout")
        self.btnAbout.setGeometry(QRect(20, 417, 29, 28))
        self.btnAbout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAbout.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"res/button/btn_about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAbout.setIcon(icon1)

        # help

        self.btnHelp = QPushButton(self.grid_w)
        self.btnHelp.setObjectName(u"btnHelp")
        self.btnHelp.setGeometry(QRect(53, 417, 29, 28))
        self.btnHelp.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnHelp.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"res/button/btn_help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnHelp.setIcon(icon2)
        self.btnHelp.setAutoDefault(False)
        self.btnHelp.setFlat(False)

        # setting

        self.btnSet = QPushButton(self.grid_w)
        self.btnSet.setObjectName(u"btnSet")
        self.btnSet.setGeometry(QRect(476, 417, 30, 28))
        self.btnSet.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSet.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"res/button/btn_setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSet.setIcon(icon3)

        # property

        self.btnGear = QPushButton(self.grid_w)
        self.btnGear.setObjectName(u"btnGear")
        self.btnGear.setGeometry(QRect(510, 417, 30, 28))
        self.btnGear.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnGear.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"res/button/btn_config.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnGear.setIcon(icon3)

        self.labelPropSummer = QLabel(self.grid_w)
        self.labelPropSummer.setObjectName(u"labelPropSummer")
        self.labelPropSummer.setGeometry(QRect(20, 470, 71, 16))

        self.applyPropCitySummer = QPushButton(self.grid_w)
        self.applyPropCitySummer.setObjectName(u"applyPropCitySummer")
        self.applyPropCitySummer.setGeometry(QRect(180, 490, 81, 31))
        self.applyPropCitySummer.setCursor(QCursor(Qt.PointingHandCursor))

        self.labelNormSummer = QLabel(self.grid_w)
        self.labelNormSummer.setObjectName(u"labelNormSummer")
        self.labelNormSummer.setGeometry(QRect(20, 570, 91, 16))

        self.applyNormHighwaySummer = QPushButton(self.grid_w)
        self.applyNormHighwaySummer.setObjectName(u"applyNormHighwaySummer")
        self.applyNormHighwaySummer.setGeometry(QRect(180, 630, 81, 31))
        self.applyNormHighwaySummer.setCursor(QCursor(Qt.PointingHandCursor))

        self.applyPropHighwaySummer = QPushButton(self.grid_w)
        self.applyPropHighwaySummer.setObjectName(u"applyPropHighwaySummer")
        self.applyPropHighwaySummer.setGeometry(QRect(180, 530, 81, 31))
        self.applyPropHighwaySummer.setCursor(QCursor(Qt.PointingHandCursor))

        self.applyNormCitySummer = QPushButton(self.grid_w)
        self.applyNormCitySummer.setObjectName(u"applyNormCitySummer")
        self.applyNormCitySummer.setGeometry(QRect(180, 590, 81, 31))
        self.applyNormCitySummer.setCursor(QCursor(Qt.PointingHandCursor))

        self.applyNormCityWinter = QPushButton(self.grid_w)
        self.applyNormCityWinter.setObjectName(u"applyNormCityWinter")
        self.applyNormCityWinter.setGeometry(QRect(460, 590, 81, 31))
        self.applyNormCityWinter.setCursor(QCursor(Qt.PointingHandCursor))

        self.applyNormHighwayWinter = QPushButton(self.grid_w)
        self.applyNormHighwayWinter.setObjectName(u"applyNormHighwayWinter")
        self.applyNormHighwayWinter.setGeometry(QRect(460, 630, 81, 31))
        self.applyNormHighwayWinter.setCursor(QCursor(Qt.PointingHandCursor))

        self.applyPropCityWinter = QPushButton(self.grid_w)
        self.applyPropCityWinter.setObjectName(u"applyPropCityWinter")
        self.applyPropCityWinter.setGeometry(QRect(460, 490, 81, 31))
        self.applyPropCityWinter.setCursor(QCursor(Qt.PointingHandCursor))

        self.applyPropHighwayWinter = QPushButton(self.grid_w)
        self.applyPropHighwayWinter.setObjectName(u"applyPropHighwayWinter")
        self.applyPropHighwayWinter.setGeometry(QRect(460, 530, 81, 31))
        self.applyPropHighwayWinter.setCursor(QCursor(Qt.PointingHandCursor))

        self.labelPropWinter = QLabel(self.grid_w)
        self.labelPropWinter.setObjectName(u"labelPropWinter")
        self.labelPropWinter.setGeometry(QRect(300, 470, 71, 16))

        self.labelNormWinter = QLabel(self.grid_w)
        self.labelNormWinter.setObjectName(u"labelNormWinter")
        self.labelNormWinter.setGeometry(QRect(300, 570, 91, 16))

        self.inputPropCitySummer = QLineEdit(self.grid_w)
        self.inputPropCitySummer.setObjectName(u"inputPropCitySummer")
        self.inputPropCitySummer.setGeometry(QRect(20, 491, 151, 31))

        self.inputPropHighwaySummer = QLineEdit(self.grid_w)
        self.inputPropHighwaySummer.setObjectName(u"inputPropHighwaySummer")
        self.inputPropHighwaySummer.setGeometry(QRect(20, 530, 151, 31))

        self.inputPropCityWinter = QLineEdit(self.grid_w)
        self.inputPropCityWinter.setObjectName(u"inputPropCityWinter")
        self.inputPropCityWinter.setGeometry(QRect(300, 490, 151, 31))

        self.inputPropHighwayWinter = QLineEdit(self.grid_w)
        self.inputPropHighwayWinter.setObjectName(u"inputPropHighwayWInter")
        self.inputPropHighwayWinter.setGeometry(QRect(300, 530, 151, 31))

        self.inputNormCitySummer = QLineEdit(self.grid_w)
        self.inputNormCitySummer.setObjectName(u"inputNormCitySummer")
        self.inputNormCitySummer.setGeometry(QRect(20, 590, 151, 31))

        self.inputNormHighwaySummer = QLineEdit(self.grid_w)
        self.inputNormHighwaySummer.setObjectName(u"inputNormHighwaySummer")
        self.inputNormHighwaySummer.setGeometry(QRect(20, 630, 151, 31))

        self.inputNormCityWinter = QLineEdit(self.grid_w)
        self.inputNormCityWinter.setObjectName(u"inputNormCityWinter")
        self.inputNormCityWinter.setGeometry(QRect(300, 590, 151, 31))

        self.inputNormHighwayWinter = QLineEdit(self.grid_w)
        self.inputNormHighwayWinter.setObjectName(u"inputNormHighwayWInter")
        self.inputNormHighwayWinter.setGeometry(QRect(300, 630, 151, 31))

        root.setCentralWidget(self.grid_w)
        self.retranslateUi(root)

        self.btnHelp.setDefault(False)
        self.btnGear.setDefault(False)

        QMetaObject.connectSlotsByName(root)

    # setupUi

    def retranslateUi(self, root):
        root.setWindowTitle(QCoreApplication.translate("root", u"BenzConfig", None))
        self.inputSummer.setInputMask("")
        self.inputSummer.setText("")
        self.inputSummer.setPlaceholderText(QCoreApplication.translate("root",
                                                                       u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435",
                                                                       None))
        self.outSummer.setText("")
        self.btnSummer.setText(
            QCoreApplication.translate("root", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        #if QT_CONFIG(shortcut)
        self.btnSummer.setShortcut(QCoreApplication.translate("root", u"Return", None))
        #endif // QT_CONFIG(shortcut)
        self.btnWinter.setText(
            QCoreApplication.translate("root", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        #if QT_CONFIG(shortcut)
        self.btnWinter.setShortcut(QCoreApplication.translate("root", u"Tab", None))
        #endif // QT_CONFIG(shortcut)
        self.outWinter.setText("")
        self.inputWinter.setText("")
        self.inputWinter.setPlaceholderText(QCoreApplication.translate("root",
                                                                       u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435",
                                                                       None))
        self.label_s.setText(QCoreApplication.translate("root", u"\u041b\u0435\u0442\u043d\u0438\u0439", None))
        self.lable_w.setText(QCoreApplication.translate("root", u"\u0417\u0438\u043c\u043d\u0438\u0439", None))
        self.btnAbout.setText("")
        self.btnHelp.setText("")
        self.btnGear.setText("")
        self.labelPropSummer.setText(
            QCoreApplication.translate("root", u"\u041f\u0440\u043e\u043f\u043e\u0440\u0446\u0438\u0438", None))
        self.applyPropCitySummer.setText(
            QCoreApplication.translate("root", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.labelNormSummer.setText(QCoreApplication.translate("root",
                                                                u"\u041d\u043e\u0440\u043c\u044b \u0440\u0430\u0441\u0445\u043e\u0434\u0430",
                                                                None))
        self.applyNormHighwaySummer.setText(
            QCoreApplication.translate("root", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.applyPropHighwaySummer.setText(
            QCoreApplication.translate("root", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.applyNormCitySummer.setText(
            QCoreApplication.translate("root", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.applyNormCityWinter.setText(
            QCoreApplication.translate("root", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.applyNormHighwayWinter.setText(
            QCoreApplication.translate("root", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.applyPropCityWinter.setText(
            QCoreApplication.translate("root", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.applyPropHighwayWinter.setText(
            QCoreApplication.translate("root", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.labelPropWinter.setText(
            QCoreApplication.translate("root", u"\u041f\u0440\u043e\u043f\u043e\u0440\u0446\u0438\u0438", None))
        self.labelNormWinter.setText(QCoreApplication.translate("root",
                                                                u"\u041d\u043e\u0440\u043c\u044b \u0440\u0430\u0441\u0445\u043e\u0434\u0430",
                                                                None))
        self.inputPropCitySummer.setPlaceholderText(
            QCoreApplication.translate("root", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.inputPropHighwaySummer.setPlaceholderText(
            QCoreApplication.translate("root", u"\u0422\u0440\u0430\u0441\u0441\u0430", None))
        self.inputPropCityWinter.setPlaceholderText(
            QCoreApplication.translate("root", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.inputPropHighwayWinter.setPlaceholderText(
            QCoreApplication.translate("root", u"\u0422\u0440\u0430\u0441\u0441\u0430", None))
        self.inputNormCitySummer.setPlaceholderText(
            QCoreApplication.translate("root", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.inputNormHighwaySummer.setPlaceholderText(
            QCoreApplication.translate("root", u"\u0422\u0440\u0430\u0441\u0441\u0430", None))
        self.inputNormCityWinter.setPlaceholderText(
            QCoreApplication.translate("root", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.inputNormHighwayWinter.setPlaceholderText(
            QCoreApplication.translate("root", u"\u0422\u0440\u0430\u0441\u0441\u0430", None))
    # retranslateUi
