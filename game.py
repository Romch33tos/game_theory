import random
from customtkinter import CTk, CTkButton, CTkLabel, set_appearance_mode, set_default_color_theme

class Game:
  def __init__(self):
    self.current_score = 1
    self.move_count = 1
    self.target_score = random.randint(128, 1024)
    self.add_value = random.randint(1, 5)
    self.multiply_value = random.randint(2, 5)
    self.root = CTk()

if __name__ == "__main__":
  game = Game()
  game.root.mainloop()
