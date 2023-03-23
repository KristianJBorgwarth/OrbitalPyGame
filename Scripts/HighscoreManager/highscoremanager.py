import os
import globals
import json


class HighScoreManager:
    def __init__(self, file_name="highscore.json"):
        self.file_name = file_name
        self.leaderboard = []

        if os.path.exists(self.file_name):
            self.load_leaderboard()
            globals.high_score = self.leaderboard[0]["score"]

    def increase_score(self, points):
        globals.score += points

    def update_high_score(self):
        if globals.score > globals.high_score:
            globals.high_score = globals.score

    def add_score(self, player_tag):
        original_tag = player_tag
        counter = 1

        while True:
            tag_exists = any(entry["tag"] == player_tag for entry in self.leaderboard)
            if not tag_exists:
                break
            else:
                print(f"Tag '{player_tag}' already exists in the leaderboard. Please choose a different tag.")
                player_tag = original_tag + "-" + str(counter)
                counter += 1
                print(player_tag)

        new_entry = {"tag": player_tag, "score": globals.score}
        self.leaderboard.append(new_entry)
        self.leaderboard.sort(key=lambda x: x["score"], reverse=True)

    def load_leaderboard(self):
        with open(self.file_name, "r") as file:
            self.leaderboard = json.load(file)

    def save_leaderboard(self):
        with open(self.file_name, "w") as file:
            json.dump(self.leaderboard, file)

    def reset_score(self):
        globals.score = 0
