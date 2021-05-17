#Creating a simple class to wark with data
class Lesson:
    def __init__(self, name, time, link):
        self.name = name
        self.time = time
        self.link = link

    def give_link(self):
        return (f"{self.name} lesson starts at {self.time}\nLink to {self.name} is: {self.link}")

#Creating objects to represent lessons
Turkish_OTH = Lesson(
    "Turkish OTH",
    "9:00",
    "https://zoom.us/j/97174914268")

Turkish_KTL = Lesson(
    "Turkish KTL",
    "9:00",
    "https://zoom.us/j/3473699064")

Dmath = Lesson(
    "Discrete math",
    "10:40",
    "https://zoom.us/j/4654536993")

life_safety = Lesson(
    "Life safety",
    "14:40",
    "https://us04web.zoom.us/j/2784975745?pwd=SUFPZVlHMkhrb2F0RGVYak1MSTVhQT09 \nPassword: 1234")

OOP = Lesson(
    "Object Oriented  Programming",
    "95:0",
    "https://ocs.iaau.edu.kg/course/view.php?id=85 \nGo to latest BBB class")

Calculus = Lesson(
    "Calculus",
    "13:00",
    "https://zoom.us/j/4654536993")

English = Lesson(
    "English",
    "16:20",
    "https://meet.google.com/nyx-pcwi-vwz")

Algebra = Lesson(
    "Algebra and Geometry",
    "9:00",
    "https://zoom.us/j/5856122793 \nPassword : @MATHMAN")

Russian_Suralan = Lesson(
    "Russian language Surakan",
    "13:50",
    "https://zoom.us/j/96966924568")

Russian_Gulina = Lesson(
    "Russian language Gulina",
    "13:50",
    "https://zoom.us/j/8314051374?pwd=TVBDanAvYllTVEp6VkRiZ21Kempwdz09 \nPassword: astra123!")

Phy_girls = Lesson(
    "Physical training for girls",
    "15:30",
    "https://zoom.us/j/95827906871?pwd=MGRsWGVRVmM1MVFSb29ZMUVsZ1JUZz09")

Phy_boys = Lesson(
    "Physical training for boys",
    "15:30 or 15:40 or 16:20",
    "https://zoom.us/j/95304954695?pwd=cWFMcXcwemdoVG5PLzJwZWNEZUxwdz09")