import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QSettings
from design_beta import Ui_root

sys.argv += ['-platform', 'windows:darkmode=1']


class MainWindow(QMainWindow, Ui_root):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # setting
        self.btnSet.clicked.connect(self.saveSettings)
        self.btnSet.setShortcut(QApplication.translate("root", u"Ctrl+S", None))

        # property
        self.propCity = None
        self.propHighway = None
        self.normCity = None
        self.normHighway = None

        self.propCityWinter = None
        self.normCityWinter = None
        self.propHighwayWinter = None
        self.normHighwayWinter = None

        # function
        self.btnSummer.clicked.connect(self.funcSummer)
        self.btnWinter.clicked.connect(self.funcWinter)

        # menubar
        self.btnAbout.clicked.connect(self.funcAbout)
        self.btnHelp.clicked.connect(self.funcHelp)
        self.btnGear.setCheckable(True)
        self.btnGear.clicked.connect(self.funcGear)

        # summer
        self.applyPropCitySummer.clicked.connect(self.newPropCitySummer)
        self.applyNormCitySummer.clicked.connect(self.newNormCitySummer)
        self.applyPropHighwaySummer.clicked.connect(self.newPropHighwaySummer)
        self.applyNormHighwaySummer.clicked.connect(self.newNormHighwaySummer)

        # winter
        self.applyPropCityWinter.clicked.connect(self.newPropCityWinter)
        self.applyNormCityWinter.clicked.connect(self.newNormCityWinter)
        self.applyPropHighwayWinter.clicked.connect(self.newPropHighwayWinter)
        self.applyNormHighwayWinter.clicked.connect(self.newNormHighwayWinter)

        self.loadSettings()

    # settings
    def loadSettings(self):

        settings = QSettings("settings.ini", QSettings.IniFormat)

        self.inputPropCitySummer.setText(settings.value('SummerPropCity', ""))
        self.inputPropHighwaySummer.setText(settings.value('SummerPropHighway', ""))
        self.inputNormCitySummer.setText(settings.value('SummerRatesCity', ""))
        self.inputNormHighwaySummer.setText(settings.value('SummerRatesHighway', ""))

        if self.inputPropCitySummer.text(): self.applyPropCitySummer.click()
        if self.inputPropHighwaySummer.text(): self.applyPropHighwaySummer.click()
        if self.inputNormCitySummer.text(): self.applyNormCitySummer.click()
        if self.inputNormHighwaySummer.text(): self.applyNormHighwaySummer.click()

        self.inputPropCityWinter.setText(settings.value('WinterProportionsCity', ""))
        self.inputPropHighwayWinter.setText(settings.value('WinterProportionsHighway', ""))
        self.inputNormCityWinter.setText(settings.value('WinterRatesCity', ""))
        self.inputNormHighwayWinter.setText(settings.value('WinterRatesHighway', ""))

        if self.inputPropCityWinter.text(): self.applyPropCityWinter.click()
        if self.inputNormCityWinter.text(): self.applyNormCityWinter.click()
        if self.inputPropHighwayWinter.text(): self.applyPropHighwayWinter.click()
        if self.inputNormHighwayWinter.text(): self.applyNormHighwayWinter.click()

    def saveSettings(self):

        settings = QSettings("settings.ini", QSettings.IniFormat)

        settings.setValue("SummerPropCity", self.inputPropCitySummer.text())
        settings.setValue("SummerPropHighway", self.inputPropHighwaySummer.text())
        settings.setValue("SummerRatesCity", self.inputNormCitySummer.text())
        settings.setValue("SummerRatesHighway", self.inputNormHighwaySummer.text())

        settings.setValue("WinterInput", self.inputWinter.text())
        settings.setValue("WinterProportionsCity", self.inputPropCityWinter.text())
        settings.setValue("WinterProportionsHighway", self.inputPropHighwayWinter.text())
        settings.setValue("WinterRatesCity", self.inputNormCityWinter.text())
        settings.setValue("WinterRatesHighway", self.inputNormHighwayWinter.text())

        msg = QMessageBox.information(self, "Настройки", f"Новые параметры сохранены.")

    # summer
    def funcSummer(self):
        try:
            if self.propCity:
                propCity = self.propCity
            else:
                propCity = 0.3
            if self.normCity:
                normCity = self.normCity
            else:
                normCity = 11.5
            if self.propHighway:
                propHighway = self.propHighway
            else:
                propHighway = 0.7
            if self.normHighway:
                normHighway = self.normHighway
            else:
                normHighway = 8.5

            inSummer = float(self.inputSummer.text())
            roadCity = round(propCity * inSummer, 2)
            roadHighway = round(propHighway * inSummer, 2)
            resultCity = round(propCity * inSummer / 100 * normCity, 2)
            resultHighway = round(propHighway * inSummer / 100 * normHighway, 2)
            totalSummer = round((propCity * inSummer / 100 * normCity) +
                                (propHighway * inSummer / 100 * normHighway), 2)

            self.outSummer.setText(
                f' Ваш расход составил {totalSummer} литров\n\n'
                f' Детальная информация \n'
                f' Пробег по городу {roadCity} км \n'
                f' Расход по городу {resultCity} литров\n'
                f' Пробег по трассе {roadHighway} км \n'
                f' Расход по трассе {resultHighway} литров\n\n'
                f' Нормы расхода\n'
                f' Город {normCity} на 100 км\n'
                f' Трасса {normHighway} на 100 км\n\n'
                f' Пропорции\n'
                f' Коэф. по городу {propCity}\n'
                f' Коэф. по трассе {propHighway}'
            )

        except Exception as e:
            None

    def newPropCitySummer(self):
        try:
            self.propCity = float(self.inputPropCitySummer.text())
            self.funcSummer()

        except Exception as e:

            self.propCity = None
            msg = QMessageBox.information(
                self,
                'Внимание', f"Что-то пошло не так."
                            f"Проверьте исходные данные.")

    def newNormCitySummer(self):
        try:
            self.normCity = float(self.inputNormCitySummer.text())
            self.funcSummer()

        except Exception as e:

            self.normCity = None
            msg = QMessageBox.information(
                self,
                'Внимание', f"Что-то пошло не так."
                            f"Проверьте исходные данные.")

    def newPropHighwaySummer(self):
        try:
            self.propHighway = float(self.inputPropHighwaySummer.text())
            self.funcSummer()

        except Exception as e:

            self.propHighway = None
            msg = QMessageBox.information(
                self,
                'Внимание', f"Что-то пошло не так."
                            f"Проверьте исходные данные.")

    def newNormHighwaySummer(self):
        try:
            self.normHighway = float(self.inputNormHighwaySummer.text())
            self.funcSummer()

        except Exception as e:

            self.normHighway = None
            msg = QMessageBox.information(
                self,
                'Внимание', f"Что-то пошло не так."
                            f"Проверьте исходные данные.")

    # winter
    def funcWinter(self):

        try:
            if self.propCityWinter:
                propCityWinter = self.propCityWinter
            else:
                propCityWinter = 0.3
            if self.normCityWinter:
                normCityWinter = self.normCityWinter
            else:
                normCityWinter = 13.8
            if self.propHighwayWinter:
                propHighwayWinter = self.propHighwayWinter
            else:
                propHighwayWinter = 0.7
            if self.normHighwayWinter:
                normHighwayWinter = self.normHighwayWinter
            else:
                normHighwayWinter = 10.2

            inWinter = float(self.inputWinter.text())
            roadCity = round(propCityWinter * inWinter, 2)
            roadHighway = round(propHighwayWinter * inWinter, 2)
            resultCity = round(propCityWinter * inWinter / 100 * normCityWinter, 2)
            resultHighway = round(propHighwayWinter * inWinter / 100 * normHighwayWinter, 2)
            totalWinter = round((propCityWinter * inWinter / 100 * normCityWinter) +
                                (propHighwayWinter * inWinter / 100 * normHighwayWinter), 2)

            self.outWinter.setText(
                f' Ваш расход составил {totalWinter} литров\n\n'
                f' Детальная информация \n'
                f' Пробег по городу {roadCity} км \n'
                f' Расход по городу {resultCity} литров\n'
                f' Пробег по трассе {roadHighway} км \n'
                f' Расход по трассе {resultHighway} литров\n\n'
                f' Нормы расхода\n'
                f' Город {normCityWinter} на 100 км\n'
                f' Трасса {normHighwayWinter} на 100 км\n\n'
                f' Пропорции\n'
                f' Коэф. по городу {propCityWinter}\n'
                f' Коэф. по трассе {propHighwayWinter}'
            )

        except Exception as e:

            None

    def newPropCityWinter(self):
        try:
            self.propCityWinter = float(self.inputPropCityWinter.text())
            self.funcWinter()

        except Exception as e:

            self.propCityWinter = None
            msg = QMessageBox.information(
                self,
                'Внимание', f"Что-то пошло не так.\n"
                            f"Проверьте исходные данные.")

    def newNormCityWinter(self):
        try:
            self.normCityWinter = float(self.inputNormCityWinter.text())
            self.funcWinter()

        except Exception as e:

            self.normCityWinter = None
            msg = QMessageBox.information(
                self,
                'Внимание', f"Что-то пошло не так.\n"
                            f"Проверьте исходные данные.")

    def newPropHighwayWinter(self):
        try:
            self.propHighwayWinter = float(self.inputPropHighwayWinter.text())
            self.funcWinter()

        except Exception as e:

            self.propHighwayWinter = None
            msg = QMessageBox.information(
                self,
                'Внимание',
                f"Что-то пошло не так.\n"
                f"Проверьте исходные данные.")

    def newNormHighwayWinter(self):
        try:
            self.normHighwayWinter = float(self.inputNormHighwayWinter.text())
            self.funcWinter()

        except Exception as e:

            self.normHighwayWinter = None
            msg = QMessageBox.information(
                self,
                'Внимание',
                f"Что-то пошло не так.\n"
                f"Проверьте исходные данные.")

    def funcGear(self):

        if self.btnGear.isChecked():
            self.resize(560, 670)
        else:
            self.resize(560, 450)

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
        Сохранение новых норм клавиша "Ctrl+S"
        """

        msgAbout = QMessageBox()
        msgAbout.setWindowTitle("Help")
        msgAbout.setWindowIcon(QIcon('res/context/help/icon_help_wi.svg'))
        msgAbout.setText(strAbout)
        msgAbout.setIconPixmap(QPixmap("res/context/help/icon_help.png"))
        msgAbout.setStandardButtons(QMessageBox.Ok)
        msgAbout.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
