import json

class Song:
    def __init__(self, name, interpreter, year, link):
        self.name = name
        self.interpreter = interpreter
        self.year = year
        self.link = link
    
    def get_name(self):
        return self.name
    
    def get_interpreter(self):
        return self.interpreter

    def to_json(self):
            return {
            "name": self.name,
            "interpreter": self.interpreter,
            "year": self.year,
            "link": self.link
            }
    
    def __str__(self):
        return f"{self.name}, {self.interpreter} ({self.year})"
    
    def __repr__(self):
        return f"Name: {self.name}, Interpreter: {self.interpreter}, Year: {self.year}, Link: {self.link}"
    
    def __eq__(self, other):
        if isinstance(other, Song):
            if other.name==self.name and other.interpreter == self.interpreter:
                return True
        return False
     
    def __hash__(self):
        return hash((self.name, self.interpreter))
    