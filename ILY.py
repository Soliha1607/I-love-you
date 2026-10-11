import sys
import math

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QFont, QColor
from PyQt6.QtCore import QTimer

class HeartWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("I Love You ❤️")
        self.showFullScreen()

        self.setStyleSheet("""
            QWidget {
                background-color: black;
            }
        """)

        self.words = [
            "I love you",
            "Я тебя люблю",
            "Men seni sevaman",
            "Ich liebe dich",
            "Je t'aime",
            "Te amo",
            "Ti amo",
            "Eu te amo",
            "愛してる",
            "사랑해",
            "我爱你",
            "أحبك",
            "אני אוהב אותך",
            "Seni seviyorum",
            "Ik hou van jou",
            "Jeg elsker deg",
            "Jeg elsker dig",
            "Jag älskar dig",
            "Rakastan sinua",
            "Kocham cię",
            "Miluji tě",
            "Ľúbim ťa",
            "Szeretlek",
            "Te iubesc",
            "Volim te",
            "Ljubim te",
            "Волим те",
            "Обичам те",
            "Σ' αγαπώ",
            "Te quiero",
            "Ma armastan sind",
            "Es tevi mīlu",
            "Aš tave myliu",
            "Maite zaitut",
            "Ma armastan sind",
            "Tiako ianao",
            "Mahal kita",
            "Iniibig kita",
            "Saya cinta kamu",
            "Aku cinta padamu",
            "Saya sayang kamu",
            "ฉันรักคุณ",
            "Tôi yêu bạn",
            "ฉันรักเธอ",
            "मैं तुमसे प्यार करता हूँ",
            "मुझे तुमसे प्यार है",
            "আমি তোমাকে ভালোবাসি",
            "আমি তোমায় ভালোবাসি",
            "میں تم سے محبت کرتا ہوں",
            "ਮੈਂ ਤੈਨੂੰ ਪਿਆਰ ਕਰਦਾ ਹਾਂ",
            "હું તને પ્રેમ કરું છું",
            "నేను నిన్ను ప్రేమిస్తున్నాను",
            "ನಾನು ನಿನ್ನನ್ನು ಪ್ರೀತಿಸುತ್ತೇನೆ",
            "ഞാൻ നിന്നെ സ്നേഹിക്കുന്നു",
            "මම ඔයාට ආදරෙයි",
            "Ես քեզ սիրում եմ",
            "Ես քեզ սիրում եմ",
            "მიყვარხარ",
            "Səni sevirəm",
            "Mən səni sevirəm",
            "Мен сені сүйемін",
            "Мен сени сүйөм",
            "Мен сені жақсы көремін",
            "Мен сени сүйем",
            "Мен сени яратаман",
            "Ман туро дӯст медорам",
            "زه تا سره مینه لرم",
            "Ég elska þig",
            "T'estimo",
            "Amo-te",
            "Te iubesc",
            "Ndimakukonda",
            "Ngiyakuthanda",
            "Ndiyakuthanda",
            "Nalingi yo",
            "Nakupenda",
            "Ndinokuda",
            "Mo nifẹ rẹ",
            "Ina son ka",
            "Mi amas vin",
            "Ik hâld fan dy",
            "Ech hunn dech gär",
            "Ik hou van je",
            "T'estimo molt",
            "Te sakam",
            "Волим те",
            "Kocham ciebie",
            "Miluji tě",
            "Ljubim te",
            "Aš tave myliu",
            "Es mīlu tevi",
            "Ma armastan sind",
            "Të dua",
            "Të dashuroj",
            "Unë të dua",
            "Te sakam",
            "Volim te",
            "Szeretlek",
            "Miluji tě",
            "Ti amo",
            "Te amo",
            "Je t'aime",
            "I love you",
        ]

        self.positions = self.create_heart_positions()

        self.current_index = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.add_next_word)

        self.timer.start(100)

    def create_heart_positions(self):
        positions = []

        scale = min(self.width(), self.height()) * 0.022

        for i in range(100):
            t = 2 * math.pi * i / 100

            x = 16 * math.sin(t) ** 3

            y = (
                    13 * math.cos(t)
                    - 5 * math.cos(2 * t)
                    - 2 * math.cos(3 * t)
                    - math.cos(4 * t)
            )

            x *= scale
            y *= -scale

            x += self.width() / 2
            y += self.height() / 2

            positions.append((x, y))

        return positions

    def add_next_word(self):
        if self.current_index < len(self.words):
            self.current_index += 1
            self.update()

        else:
            self.timer.stop()

    def resizeEvent(self, event):

        self.positions = self.create_heart_positions()

        super().resizeEvent(event)

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        for i in range(self.current_index):

            if i >= len(self.positions):
                break

            x, y = self.positions[i]

            painter.setPen(QColor(255, 80, 130))

            font = QFont("Arial", 10)
            font.setBold(True)

            painter.setFont(font)

            painter.drawText(
                int(x - 40),
                int(y),
                self.words[i]
            )


app = QApplication(sys.argv)

window = HeartWindow()
window.show()

sys.exit(app.exec())
