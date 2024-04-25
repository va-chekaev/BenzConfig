from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QCursor, QIcon)
from PySide6.QtWidgets import (QLabel, QLineEdit, QPushButton, QTabWidget, QWidget)
import files_rc


class ui_root(object):
    def setupUi(self, root):
        if not root.objectName():
            root.setObjectName(u"root")

        # ROOT
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
        root.setDocumentMode(False)
        root.setTabShape(QTabWidget.Rounded)

        self.grid_w = QWidget(root)
        self.grid_w.setObjectName(u"grid_w")

        # INPUT SUMMER
        self.inputSummer = QLineEdit(self.grid_w)
        self.inputSummer.setObjectName(u"inputSummer")
        self.inputSummer.setGeometry(QRect(20, 40, 241, 31))
        self.inputSummer.setLayoutDirection(Qt.LeftToRight)
        self.inputSummer.setInputMethodHints(Qt.ImhNone)
        self.inputSummer.setMaxLength(16)

        # OUTPUT SUMMER
        self.outSummer = QLabel(self.grid_w)
        self.outSummer.setObjectName(u"outSummer")
        self.outSummer.setGeometry(QRect(20, 130, 241, 281))
        self.outSummer.setStyleSheet(u"background-color: rgba(230, 230, 230, 230);")
        self.outSummer.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        # BUTTON CALCULATE SUMMER
        self.btnSummer = QPushButton(self.grid_w)
        self.btnSummer.setObjectName(u"btnSummer")
        self.btnSummer.setGeometry(QRect(20, 80, 241, 41))
        self.btnSummer.setCursor(QCursor(Qt.PointingHandCursor))

        # BUTTON CALCULATE WINTER
        self.btnWinter = QPushButton(self.grid_w)
        self.btnWinter.setObjectName(u"btnWinter")
        self.btnWinter.setGeometry(QRect(300, 80, 241, 41))
        self.btnWinter.setCursor(QCursor(Qt.PointingHandCursor))

        # OUTPUT WINTER
        self.outWinter = QLabel(self.grid_w)
        self.outWinter.setObjectName(u"outWinter")
        self.outWinter.setGeometry(QRect(300, 130, 241, 281))
        self.outWinter.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.outWinter.setInputMethodHints(Qt.ImhNone)
        self.outWinter.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        # INPUT WINTER
        self.inputWinter = QLineEdit(self.grid_w)
        self.inputWinter.setObjectName(u"inputWinter")
        self.inputWinter.setGeometry(QRect(300, 40, 241, 31))
        self.inputWinter.setMaxLength(16)

        # LABEL SUMMER
        self.SummerLabel = QLabel(self.grid_w)
        self.SummerLabel.setObjectName(u"SummerLabel")
        self.SummerLabel.setGeometry(QRect(20, 10, 241, 21))

        # LABEL WINTER
        self.WinterLabel = QLabel(self.grid_w)
        self.WinterLabel.setObjectName(u"WinterLabel")
        self.WinterLabel.setGeometry(QRect(300, 10, 241, 21))

        # BUTTON ABOUT
        self.btnAbout = QPushButton(self.grid_w)
        self.btnAbout.setObjectName(u"btnAbout")
        self.btnAbout.setGeometry(QRect(20, 417, 29, 28))
        self.btnAbout.setCursor(QCursor(Qt.PointingHandCursor))

        icon1 = QIcon()
        icon1.addFile(u"res/button/btn_about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAbout.setIcon(icon1)

        # BUTTON HELP
        self.btnHelp = QPushButton(self.grid_w)
        self.btnHelp.setObjectName(u"btnHelp")
        self.btnHelp.setGeometry(QRect(53, 417, 29, 28))
        self.btnHelp.setCursor(QCursor(Qt.PointingHandCursor))

        icon2 = QIcon()
        icon2.addFile(u"res/button/btn_help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnHelp.setIcon(icon2)

        # BUTTON SAVE SETTING
        self.btnSaveSet = QPushButton(self.grid_w)
        self.btnSaveSet.setObjectName(u"btnSet")
        self.btnSaveSet.setGeometry(QRect(476, 417, 30, 28))
        self.btnSaveSet.setCursor(QCursor(Qt.PointingHandCursor))

        icon3 = QIcon()
        icon3.addFile(u"res/button/btn_setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSaveSet.setIcon(icon3)

        # BUTTON PROPERTY
        self.btnGear = QPushButton(self.grid_w)
        self.btnGear.setObjectName(u"btnGear")
        self.btnGear.setGeometry(QRect(510, 417, 30, 28))
        self.btnGear.setCursor(QCursor(Qt.PointingHandCursor))

        icon3 = QIcon()
        icon3.addFile(u"res/button/btn_config.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnGear.setIcon(icon3)

        # LABEL PROP SUMMER
        self.labelPropSummer = QLabel(self.grid_w)
        self.labelPropSummer.setObjectName(u"labelPropSummer")
        self.labelPropSummer.setGeometry(QRect(20, 470, 71, 16))

        # LABEL RATES SUMMER
        self.labelRatesSummer = QLabel(self.grid_w)
        self.labelRatesSummer.setObjectName(u"labelRatesSummer")
        self.labelRatesSummer.setGeometry(QRect(20, 570, 91, 16))

        # APPLY SUMMER PROP CITY
        self.apSummerPropCity = QPushButton(self.grid_w)
        self.apSummerPropCity.setObjectName(u"apSummerPropCity")
        self.apSummerPropCity.setGeometry(QRect(180, 490, 81, 31))
        self.apSummerPropCity.setCursor(QCursor(Qt.PointingHandCursor))

        # APPLY RATES SUMMER CITY
        self.apSummerRatesCity = QPushButton(self.grid_w)
        self.apSummerRatesCity.setObjectName(u"apSummerRatesCity")
        self.apSummerRatesCity.setGeometry(QRect(180, 590, 81, 31))
        self.apSummerRatesCity.setCursor(QCursor(Qt.PointingHandCursor))

        # APPLY PROP SUMMER HIGHWAY
        self.apSummerPropHighway = QPushButton(self.grid_w)
        self.apSummerPropHighway.setObjectName(u"apSummerPropHighway")
        self.apSummerPropHighway.setGeometry(QRect(180, 530, 81, 31))
        self.apSummerPropHighway.setCursor(QCursor(Qt.PointingHandCursor))

        # APPLY RATES SUMMER HIGHWAY
        self.apSummerRatesHighway = QPushButton(self.grid_w)
        self.apSummerRatesHighway.setObjectName(u"applyNormHighwaySummer")
        self.apSummerRatesHighway.setGeometry(QRect(180, 630, 81, 31))
        self.apSummerRatesHighway.setCursor(QCursor(Qt.PointingHandCursor))

        # APPLY RATES WINTER CITY
        self.apWinterRatesCity = QPushButton(self.grid_w)
        self.apWinterRatesCity.setObjectName(u"apWinterRatesCity")
        self.apWinterRatesCity.setGeometry(QRect(460, 590, 81, 31))
        self.apWinterRatesCity.setCursor(QCursor(Qt.PointingHandCursor))

        # APPLY RATES WINTER HIGHWAY
        self.apWinterRatesHighway = QPushButton(self.grid_w)
        self.apWinterRatesHighway.setObjectName(u"apWinterRatesHighway")
        self.apWinterRatesHighway.setGeometry(QRect(460, 630, 81, 31))
        self.apWinterRatesHighway.setCursor(QCursor(Qt.PointingHandCursor))

        # APPLY PROP WINTER CITY
        self.apWinterPropCity = QPushButton(self.grid_w)
        self.apWinterPropCity.setObjectName(u"apWinterPropCity")
        self.apWinterPropCity.setGeometry(QRect(460, 490, 81, 31))
        self.apWinterPropCity.setCursor(QCursor(Qt.PointingHandCursor))

        # APPLY PROP WINTER HIGHWAY
        self.apWinterPropHighway = QPushButton(self.grid_w)
        self.apWinterPropHighway.setObjectName(u"apWinterPropHighway")
        self.apWinterPropHighway.setGeometry(QRect(460, 530, 81, 31))
        self.apWinterPropHighway.setCursor(QCursor(Qt.PointingHandCursor))

        # LABEL PROP WINTER
        self.labelPropWinter = QLabel(self.grid_w)
        self.labelPropWinter.setObjectName(u"labelPropWinter")
        self.labelPropWinter.setGeometry(QRect(300, 470, 71, 16))

        # LABEL RATES WINTER
        self.labelRatesWinter = QLabel(self.grid_w)
        self.labelRatesWinter.setObjectName(u"labelRatesWinter")
        self.labelRatesWinter.setGeometry(QRect(300, 570, 91, 16))

        # INPUT PROP SUMMER CITY
        self.inSummerPropCity = QLineEdit(self.grid_w)
        self.inSummerPropCity.setObjectName(u"inSummerPropCity")
        self.inSummerPropCity.setGeometry(QRect(20, 491, 151, 31))

        # INPUT PROP SUMMER HIGHWAY
        self.inSummerPropHighway = QLineEdit(self.grid_w)
        self.inSummerPropHighway.setObjectName(u"inSummerPropHighway")
        self.inSummerPropHighway.setGeometry(QRect(20, 530, 151, 31))

        # INPUT RATES SUMMER CITY
        self.inSummerRatesCity = QLineEdit(self.grid_w)
        self.inSummerRatesCity.setObjectName(u"inSummerRatesCity")
        self.inSummerRatesCity.setGeometry(QRect(20, 590, 151, 31))

        # INPUT RATES SUMMER HIGHWAY
        self.inSummerRatesHighway = QLineEdit(self.grid_w)
        self.inSummerRatesHighway.setObjectName(u"inSummerRatesHighway")
        self.inSummerRatesHighway.setGeometry(QRect(20, 630, 151, 31))

        # INPUT PROP WINTER CITY
        self.inWinterPropCity = QLineEdit(self.grid_w)
        self.inWinterPropCity.setObjectName(u"inWinterPropCity")
        self.inWinterPropCity.setGeometry(QRect(300, 490, 151, 31))

        # INPUT PROP WINTER HIGHWAY
        self.inWinterPropHighway = QLineEdit(self.grid_w)
        self.inWinterPropHighway.setObjectName(u"inWinterPropHighway")
        self.inWinterPropHighway.setGeometry(QRect(300, 530, 151, 31))

        # INPUT RATES WINTER CITY
        self.inWinterRatesCity = QLineEdit(self.grid_w)
        self.inWinterRatesCity.setObjectName(u"inWinterRatesCity")
        self.inWinterRatesCity.setGeometry(QRect(300, 590, 151, 31))

        # INPUT RATES WINTER HIGHWAY
        self.inWinterRatesHighway = QLineEdit(self.grid_w)
        self.inWinterRatesHighway.setObjectName(u"inWinterRatesHighway")
        self.inWinterRatesHighway.setGeometry(QRect(300, 630, 151, 31))

        root.setCentralWidget(self.grid_w)
        self.retranslateUi(root)

        QMetaObject.connectSlotsByName(root)

    def retranslateUi(self, root):
        root.setWindowTitle(QCoreApplication.translate("root", u"BenzConfig", None))

        # SUMMER
        self.inputSummer.setText("")
        self.inputSummer.setPlaceholderText(QCoreApplication.translate("root", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))

        self.outSummer.setText("")
        self.btnSummer.setText(QCoreApplication.translate("root", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.btnSummer.setShortcut(QCoreApplication.translate("root", u"Return", None))

        self.SummerLabel.setText(QCoreApplication.translate("root", u"\u041b\u0435\u0442\u043d\u0438\u0439", None))

        # WINTER
        self.inputWinter.setText("")
        self.inputWinter.setPlaceholderText(QCoreApplication.translate("root", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))

        self.outWinter.setText("")
        self.btnWinter.setText(QCoreApplication.translate("root", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.btnWinter.setShortcut(QCoreApplication.translate("root", u"Tab", None))

        self.WinterLabel.setText(QCoreApplication.translate("root", u"\u0417\u0438\u043c\u043d\u0438\u0439", None))

        # MENUBAR
        self.btnAbout.setText("")
        self.btnHelp.setText("")
        self.btnGear.setText("")

        # RETRANSLATE
        self.labelPropSummer.setText(QCoreApplication.translate("root", u"\u041f\u0440\u043e\u043f\u043e\u0440\u0446\u0438\u0438", None))
        self.labelRatesSummer.setText(QCoreApplication.translate("root", u"\u041d\u043e\u0440\u043c\u044b \u0440\u0430\u0441\u0445\u043e\u0434\u0430", None))
        self.labelPropWinter.setText(QCoreApplication.translate("root", u"\u041f\u0440\u043e\u043f\u043e\u0440\u0446\u0438\u0438", None))
        self.labelRatesWinter.setText(QCoreApplication.translate("root", u"\u041d\u043e\u0440\u043c\u044b \u0440\u0430\u0441\u0445\u043e\u0434\u0430", None))

        self.apSummerPropCity.setText(QCoreApplication.translate("root", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.apSummerRatesHighway.setText(QCoreApplication.translate("root", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.apSummerPropHighway.setText(QCoreApplication.translate("root", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.apSummerRatesCity.setText(QCoreApplication.translate("root", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))

        self.apWinterRatesCity.setText(QCoreApplication.translate("root", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.apWinterRatesHighway.setText(QCoreApplication.translate("root", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.apWinterPropCity.setText(QCoreApplication.translate("root", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.apWinterPropHighway.setText(QCoreApplication.translate("root", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))

        self.inSummerPropCity.setPlaceholderText(QCoreApplication.translate("root", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.inSummerPropHighway.setPlaceholderText(QCoreApplication.translate("root", u"\u0422\u0440\u0430\u0441\u0441\u0430", None))
        self.inWinterPropCity.setPlaceholderText(QCoreApplication.translate("root", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.inWinterPropHighway.setPlaceholderText(QCoreApplication.translate("root", u"\u0422\u0440\u0430\u0441\u0441\u0430", None))

        self.inSummerRatesCity.setPlaceholderText(QCoreApplication.translate("root", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.inSummerRatesHighway.setPlaceholderText(QCoreApplication.translate("root", u"\u0422\u0440\u0430\u0441\u0441\u0430", None))
        self.inWinterRatesCity.setPlaceholderText(QCoreApplication.translate("root", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.inWinterRatesHighway.setPlaceholderText(QCoreApplication.translate("root", u"\u0422\u0440\u0430\u0441\u0441\u0430", None))