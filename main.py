import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QSettings
from construct import ui_root


class root(QMainWindow, ui_root):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # PROPERTY
        self.SummerPropCity = None
        self.SummerPropHighway = None
        self.SummerRatesCity = None
        self.SummerRatesHighway = None

        self.WinterPropCity = None
        self.WinterPropHighway = None
        self.WinterRatesCity = None
        self.WinterRatesHighway = None

        # CALCULATE
        self.btnSummer.clicked.connect(self.funcSummer)
        self.btnWinter.clicked.connect(self.funcWinter)

        # MENUBAR
        self.btnAbout.clicked.connect(self.funcAbout)
        self.btnHelp.clicked.connect(self.funcHelp)
        self.btnGear.setCheckable(True)
        self.btnGear.clicked.connect(self.funcGear)

        # PROPERTY SUMMER
        self.apSummerPropCity.clicked.connect(self.nSummerPropCity)
        self.apSummerRatesCity.clicked.connect(self.nSummerRatesCity)
        self.apSummerPropHighway.clicked.connect(self.nSummerPropHighway)
        self.apSummerRatesHighway.clicked.connect(self.nSummerRatesHighway)

        # PROPERTY WINTER
        self.apWinterPropCity.clicked.connect(self.nWinterPropCity)
        self.apWinterRatesCity.clicked.connect(self.nWinterRatesCity)
        self.apWinterPropHighway.clicked.connect(self.nWinterPropHighway)
        self.apWinterRatesHighway.clicked.connect(self.nWinterRatesHighway)

        # SETTINGS
        self.btnSaveSet.clicked.connect(self.saveSettings)
        self.loadSettings()

    # CONFIG
    def loadSettings(self):

        settings = QSettings("settings.ini", QSettings.IniFormat)

        self.inSummerPropCity.setText(settings.value('SummerPropCity', ""))
        self.inSummerPropHighway.setText(settings.value('SummerPropHighway', ""))
        self.inSummerRatesCity.setText(settings.value('SummerRatesCity', ""))
        self.inSummerRatesHighway.setText(settings.value('SummerRatesHighway', ""))

        if self.inSummerPropCity.text(): self.apSummerPropCity.click()
        if self.inSummerRatesCity.text(): self.apSummerRatesCity.click()
        if self.inSummerPropHighway.text(): self.apSummerPropHighway.click()
        if self.inSummerRatesHighway.text(): self.apSummerRatesHighway.click()

        self.inWinterPropCity.setText(settings.value('WinterProportionsCity', ""))
        self.inWinterRatesCity.setText(settings.value('WinterRatesCity', ""))
        self.inWinterPropHighway.setText(settings.value('WinterProportionsHighway', ""))
        self.inWinterRatesHighway.setText(settings.value('WinterRatesHighway', ""))

        if self.inWinterPropCity.text(): self.apWinterPropCity.click()
        if self.inWinterPropHighway.text(): self.apWinterPropHighway.click()
        if self.inWinterRatesCity.text(): self.apWinterRatesCity.click()
        if self.inWinterRatesHighway.text(): self.apWinterRatesHighway.click()

    def saveSettings(self):

        settings = QSettings("settings.ini", QSettings.IniFormat)

        settings.setValue("SummerPropCity", self.inSummerPropCity.text())
        settings.setValue("SummerPropHighway", self.inSummerPropHighway.text())
        settings.setValue("SummerRatesCity", self.inSummerRatesCity.text())
        settings.setValue("SummerRatesHighway", self.inSummerRatesHighway.text())

        settings.setValue("WinterInput", self.inputWinter.text())
        settings.setValue("WinterProportionsCity", self.inWinterPropCity.text())
        settings.setValue("WinterProportionsHighway", self.inWinterPropHighway.text())
        settings.setValue("WinterRatesCity", self.inWinterRatesCity.text())
        settings.setValue("WinterRatesHighway", self.inWinterRatesHighway.text())

        msg = QMessageBox.information(self, "Настройки", f"Новые параметры сохранены.")

    def funcGear(self):

        if self.btnGear.isChecked():
            self.resize(560, 670)
        else:
            self.resize(560, 450)

    # FUNC SUMMER
    def funcSummer(self):
        try:
            if self.SummerPropCity: SummerPropCity = self.SummerPropCity
            else: SummerPropCity = 0.3

            if self.SummerRatesCity: SummerRatesCity = self.SummerRatesCity
            else: SummerRatesCity = 11.5

            if self.SummerPropHighway: SummerPropHighway = self.SummerPropHighway
            else: SummerPropHighway = 0.7

            if self.SummerRatesHighway: SummerRatesHighway = self.SummerRatesHighway
            else: SummerRatesHighway = 8.5

            inSummer = float(self.inputSummer.text())
            roadCity = round(SummerPropCity * inSummer, 2)
            roadHighway = round(SummerPropHighway * inSummer, 2)
            resultCity = round(SummerPropCity * inSummer / 100 * SummerRatesCity, 2)
            resultHighway = round(SummerPropHighway * inSummer / 100 * SummerRatesHighway, 2)
            totalSummer = round((SummerPropCity * inSummer / 100 * SummerRatesCity) +
                                (SummerPropHighway * inSummer / 100 * SummerRatesHighway), 2)

            self.outSummer.setText(
                f' Ваш расход составил {totalSummer} литров\n\n'
                f' Детальная информация \n'
                f' Пробег по городу {roadCity} км \n'
                f' Расход по городу {resultCity} литров\n'
                f' Пробег по трассе {roadHighway} км \n'
                f' Расход по трассе {resultHighway} литров\n\n'
                f' Нормы расхода\n'
                f' Город {SummerRatesCity} на 100 км\n'
                f' Трасса {SummerRatesHighway} на 100 км\n\n'
                f' Пропорции\n'
                f' Коэф. по городу {SummerPropCity}\n'
                f' Коэф. по трассе {SummerPropHighway}'
            )

        except Exception as e: None

    def nSummerPropCity(self):
        try:
            self.SummerPropCity = float(self.inSummerPropCity.text())
            self.funcSummer()

        except Exception as e:
            self.SummerPropCity = None
            msg = QMessageBox.information(
                self,
                'Внимание', f"Что-то пошло не так."
                            f"Проверьте исходные данные.")

    def nSummerRatesCity(self):
        try:
            self.SummerRatesCity = float(self.inSummerRatesCity.text())
            self.funcSummer()

        except Exception as e:
            self.SummerRatesCity = None
            msg = QMessageBox.information(
                self,
                'Внимание', f"Что-то пошло не так."
                            f"Проверьте исходные данные.")

    def nSummerPropHighway(self):
        try:
            self.SummerPropHighway = float(self.inSummerPropHighway.text())
            self.funcSummer()

        except Exception as e:
            self.SummerPropHighway = None
            msg = QMessageBox.information(
                self,
                'Внимание', f"Что-то пошло не так."
                            f"Проверьте исходные данные.")

    def nSummerRatesHighway(self):
        try:
            self.SummerRatesHighway = float(self.inSummerRatesHighway.text())
            self.funcSummer()

        except Exception as e:
            self.SummerRatesHighway = None
            msg = QMessageBox.information(
                self,
                'Внимание', f"Что-то пошло не так."
                            f"Проверьте исходные данные.")

    # FUNC WINTER
    def funcWinter(self):

        try:
            if self.WinterPropCity: WinterPropCity = self.WinterPropCity
            else: WinterPropCity = 0.3

            if self.WinterRatesCity: WinterRatesCity = self.WinterRatesCity
            else: WinterRatesCity = 13.8

            if self.WinterPropHighway: WinterPropHighway = self.WinterPropHighway
            else: WinterPropHighway = 0.7

            if self.WinterRatesHighway: WinterRatesHighway = self.WinterRatesHighway
            else: WinterRatesHighway = 10.2

            inWinter = float(self.inputWinter.text())
            roadCity = round(WinterPropCity * inWinter, 2)
            roadHighway = round(WinterPropHighway * inWinter, 2)
            resultCity = round(WinterPropCity * inWinter / 100 * WinterRatesCity, 2)
            resultHighway = round(WinterPropHighway * inWinter / 100 * WinterRatesHighway, 2)
            totalWinter = round((WinterPropCity * inWinter / 100 * WinterRatesCity) +
                                (WinterPropHighway * inWinter / 100 * WinterRatesHighway), 2)

            self.outWinter.setText(
                f' Ваш расход составил {totalWinter} литров\n\n'
                f' Детальная информация \n'
                f' Пробег по городу {roadCity} км \n'
                f' Расход по городу {resultCity} литров\n'
                f' Пробег по трассе {roadHighway} км \n'
                f' Расход по трассе {resultHighway} литров\n\n'
                f' Нормы расхода\n'
                f' Город {WinterRatesCity} на 100 км\n'
                f' Трасса {WinterRatesHighway} на 100 км\n\n'
                f' Пропорции\n'
                f' Коэф. по городу {WinterPropCity}\n'
                f' Коэф. по трассе {WinterPropHighway}'
            )

        except Exception as e: None

    def nWinterPropCity(self):
        try:
            self.WinterPropCity = float(self.inWinterPropCity.text())
            self.funcWinter()

        except Exception as e:
            self.WinterPropCity = None
            msg = QMessageBox.information(
                self,
                'Внимание', f"Что-то пошло не так.\n"
                            f"Проверьте исходные данные.")

    def nWinterRatesCity(self):
        try:
            self.WinterRatesCity = float(self.inWinterRatesCity.text())
            self.funcWinter()

        except Exception as e:
            self.WinterRatesCity = None
            msg = QMessageBox.information(
                self,
                'Внимание', f"Что-то пошло не так.\n"
                            f"Проверьте исходные данные.")

    def nWinterPropHighway(self):
        try:
            self.WinterPropHighway = float(self.inWinterPropHighway.text())
            self.funcWinter()

        except Exception as e:
            self.WinterPropHighway = None
            msg = QMessageBox.information(
                self,
                'Внимание',
                f"Что-то пошло не так.\n"
                f"Проверьте исходные данные.")

    def nWinterRatesHighway(self):
        try:
            self.WinterRatesHighway = float(self.inWinterRatesHighway.text())
            self.funcWinter()

        except Exception as e:
            self.WinterRatesHighway = None
            msg = QMessageBox.information(
                self,
                'Внимание',
                f"Что-то пошло не так.\n"
                f"Проверьте исходные данные.")

    @staticmethod
    def funcAbout():
        strAbout = """
            BenzConfig ver. 1.1\n
            Copyright © Чекаев В.А.
            Ресурсы www.flaticon.com\n
            Лицензия
            GNU General Public License v3.0
            """

        msgAbout = QMessageBox()
        msgAbout.setWindowTitle("About")
        msgAbout.setWindowIcon(QIcon('res/context/about/icon_about_wi.svg'))
        msgAbout.setText(strAbout)
        msgAbout.setIconPixmap(QPixmap("res/context/about/icon_about.png"))
        msgAbout.setStandardButtons(QMessageBox.Ok)
        msgAbout.exec()

    @staticmethod
    def funcHelp():
        strAbout = """
        Параметры пропорций вносить 
        в формате от 0.1 до 0.9, чтобы сумма 
        летнего и зимнего составляла 1.0\n
        Параметры норм расхода вносить через точку 
        Пример: 10.5\n
        HOTKEYS
        Рассчет Летнего расхода клавиша "Enter"
        Рассчет Зимнего расхода клавиша "Tab"
        """

        msgAbout = QMessageBox()
        msgAbout.setWindowTitle("Help")
        msgAbout.setWindowIcon(QIcon('res/context/help/icon_help_wi.svg'))
        msgAbout.setText(strAbout)
        msgAbout.setIconPixmap(QPixmap("res/context/help/icon_help.png"))
        msgAbout.setStandardButtons(QMessageBox.Ok)
        msgAbout.exec()


if __name__ == "__main__":
    sys.argv += ['-platform', 'windows:darkmode=1']
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    w = root()
    w.show()
    sys.exit(app.exec())
