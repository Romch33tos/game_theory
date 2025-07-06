import random
from customtkinter import CTk, CTkButton, CTkLabel, set_appearance_mode, set_default_color_theme
from tkinter import messagebox

class Game:
  def __init__(self):
    self.current_score = 1
    self.move_count = 1
    self.target_score = random.randint(128, 1024)
    self.add_value = random.randint(1, 5)
    self.multiply_value = random.randint(2, 5)
    self.root = CTk()
    self.setup_ui()

  def is_winning_position(self, score, moves_left):
    if score >= self.target_score:
      return moves_left % 2 == 0
    if moves_left == 0:
      return False
    options = [
      self.is_winning_position(score + self.add_value, moves_left - 1),
      self.is_winning_position(score * self.multiply_value, moves_left - 1)
    ]
    return any(options) if (moves_left - 1) % 2 == 0 else all(options)

  def show_hint(self, event):
    winning_moves = [s for s in range(0, self.target_score) if self.is_winning_position(s, 1)]
    if winning_moves:
      self.score_label.configure(text = winning_moves[0])
      self.root.after(200, self.clear_hint)

  def clear_hint(self):
    self.score_label.configure(text = self.current_score)

  def make_add_move(self):
    self.move_count += 1
    self.current_score += self.add_value
    self.update_game_state()

  def make_multiply_move(self):
    self.move_count += 1
    self.current_score *= self.multiply_value
    self.update_game_state()

  def update_game_state(self):
    self.score_label.configure(text = self.current_score)
    player_text = "Ход первого игрока:" if self.move_count % 2 != 0 else "Ход второго игрока:"
    self.player_label.configure(text = player_text)
    self.check_winner()

  def check_winner(self):
    if self.current_score >= self.target_score:
      winner_text = "Первый игрок победил!" if self.move_count % 2 == 0 else "Второй игрок победил!"
      self.player_label.configure(text = winner_text)
      self.add_button.destroy()
      self.multiply_button.destroy()
      self.restart_button.pack(pady = 15)

  def restart_game(self):
    self.restart_button.pack_forget()
    self.current_score = 1
    self.move_count = 1
    self.target_score = random.randint(128, 1024)
    self.add_value = random.randint(1, 5)
    self.multiply_value = random.randint(2, 5)

    self.target_label.configure(text = f"Нужно набрать: {self.target_score}")
    self.player_label.configure(text = "Ход первого игрока:")
    self.score_label.configure(text = self.current_score)

    self.add_button = CTkButton(
      self.root, width = 160, height = 60,
      text = f"+ {self.add_value}", font = ("Arial", 26),
      corner_radius = 8, command = self.make_add_move,
      fg_color = "#1a6bc4", text_color = "white", hover_color = "#1a4b8c"
    )
    self.add_button.pack(side = 'left', anchor = 'sw', padx = 10, pady = 10)

    self.multiply_button = CTkButton(
      self.root, width = 160, height = 60,
      text = f"× {self.multiply_value}", font = ("Arial", 26),
      corner_radius = 8, command = self.make_multiply_move,
      fg_color = "#1a6bc4", text_color = "white", hover_color = "#1a4b8c"
    )
    self.multiply_button.pack(side = 'right', anchor = 'se', padx = 10, pady = 10)

  def show_rules(self):
    messagebox.showinfo(title = "Справка", message = "Правила игры", detail = "1. Два игрока делают ходы по очереди\n" \
    "2. За каждый ход можно:\n    - Добавить к счету + N\n    - Умножить счет на × M\n3. Значения N и M генерируются случайно\n4. Для победы нужно достичь или превысить\n    целевое значение раньше соперника")

  def setup_ui(self):
    self.root.title("Игра")
    self.root.geometry("370x320")
    self.root.resizable(width = False, height = False)
    set_appearance_mode("dark")
    set_default_color_theme("blue")

    self.help_button = CTkButton(
      self.root, width = 80, height = 30,
      text = "Справка", font = ("Arial", 14),
      corner_radius = 4, command = self.show_rules,
      fg_color = "#2b2b2b", text_color = "white", hover_color = "#3b3b3b"
    )
    self.help_button.pack(anchor = 'nw', padx = 8, pady = 8)

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
    self.score_label.bind("<Button-1>", self.show_hint)

    self.player_label = CTkLabel(
      self.root, text = "Ход первого игрока:", 
      font = ("Arial", 22), text_color = "white"
    )
    self.player_label.pack(anchor = 'w', padx = 8, pady = 4)

    self.add_button = CTkButton(
      self.root, width = 160, height = 60,
      text = f"+ {self.add_value}", font = ("Arial", 26),
      corner_radius = 8, command = self.make_add_move,
      fg_color = "#1a6bc4", text_color = "white", hover_color = "#1a4b8c"
    )
    self.add_button.pack(side = 'left', anchor = 'sw', padx = 10, pady = 10)

    self.multiply_button = CTkButton(
      self.root, width = 160, height = 60,
      text = f"× {self.multiply_value}", font = ("Arial", 26),
      corner_radius = 8, command = self.make_multiply_move,
      fg_color = "#1a6bc4", text_color = "white", hover_color = "#1a4b8c"
    )
    self.multiply_button.pack(side = 'right', anchor = 'se', padx = 10, pady = 10)

    self.restart_button = CTkButton(
      self.root, width = 180, height = 60,
      text = "Ещё раз?", font = ("Arial", 24),
      corner_radius = 8, command = self.restart_game,
      fg_color = "#1a6bc4", text_color = "white", hover_color = "#1a4b8c"
    )
    self.restart_button.pack(anchor = 'center', padx = 8, pady = 10)
    self.restart_button.pack_forget()

if __name__ == "__main__":
  game = Game()
  game.root.mainloop()
