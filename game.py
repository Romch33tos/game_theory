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
    self.setup_ui()

  def setup_ui(self):
    self.root.title("Игра")
    self.root.geometry("370x320")
    self.root.resizable(width = False, height = False)
    set_appearance_mode("dark")
    set_default_color_theme("blue")

    self.target_label = CTkLabel(
      self.root, text = f"Нужно набрать: {self.target_score}", 
      font = ("Arial", 22), text_color = "white"
    )
    self.target_label.pack(anchor = 'nw', side = 'top', padx = 8, pady = 4)

    self.score_label = CTkLabel(
      self.root, text = self.current_score, 
      font = ("Arial", 42), text_color = "white"
    )
    self.score_label.pack(anchor = 'center', pady = 40, ipadx = 120)

    self.player_label = CTkLabel(
      self.root, text = "Ход первого игрока:", 
      font = ("Arial", 22), text_color = "white"
    )
    self.player_label.pack(anchor = 'w', padx = 8, pady = 4)

    self.add_button = CTkButton(
      self.root, width = 160, height = 60,
      text = f"+ {self.add_value}", font = ("Arial", 26),
      corner_radius = 8,
      fg_color = "#1a6bc4", text_color = "white", hover_color = "#1a4b8c"
    )
    self.add_button.pack(side = 'left', anchor = 'sw', padx = 10, pady = 10)

    self.multiply_button = CTkButton(
      self.root, width = 160, height = 60,
      text = f"× {self.multiply_value}", font = ("Arial", 26),
      corner_radius = 8,
      fg_color = "#1a6bc4", text_color = "white", hover_color = "#1a4b8c"
    )
    self.multiply_button.pack(side = 'right', anchor = 'se', padx = 10, pady = 10)

    self.restart_button = CTkButton(
      self.root, width = 180, height = 60,
      text = "Ещё раз?", font = ("Arial", 24),
      corner_radius = 8,
      fg_color = "#1a6bc4", text_color = "white", hover_color = "#1a4b8c"
    )
    self.restart_button.pack(anchor = 'center', padx = 8, pady = 10)
    self.restart_button.pack_forget()

if __name__ == "__main__":
  game = Game()
  game.root.mainloop()
