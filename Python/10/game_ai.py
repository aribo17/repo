"""
Game AI -- this is for you to complete
"""

import requests
import time
import random
from cw.board import Board

SERVER = "http://127.0.0.1:5000"  # this will not change
TEAM_ID = "test"  # this can be your default team_id; must contain only alphanumerical chars (max length 10)

print()

def reg():
    # register using a fixed team_id
    resp = requests.get(SERVER + "/reg/" + TEAM_ID).json()  # register 1st team

    if resp["response"] == "OK":
        # save which player we are
        print("Registered successfully as Player {}".format(resp["player"]))
        return resp["player"]
    else:
        # TODO handle the case where the response was ERROR
        T




def play(player):
    game_over = False
    while not game_over:
        time.sleep(0.2)  # wait a bit before making a new status request
        status = requests.get(SERVER + "/status").json()  # request the status of the game
        if status["status_code"] > 300:
            game_over = True
        elif status["status_code"] == 200 + player:  # it's our turn
            print("It's our turn ({}ms left)".format(status["time_left"]))
            # we make a random move => note that this might be an invalid move (segment may be occupied)
            # TODO: figure out a smart move
            border = ["top", "right", "bottom", "left"][random.randint(0,3)]
            for y in range(7):
              for x in range(7):
                  if Board().is_occupied(x, y) > 15:
                      continue
                  else:
                      if Board().is_occupied(x, y) != 1:
                          border == "top"
                      elif Board().is_occupied(x, y) != 2:
                          border == "right"
                      elif Board().is_occupied(x, y) != 4:
                          border == "bottom"
                      elif Board().is_occupied(x, y) != 8:
                          border == "left"
                      else:
                          print("Woops something went wrong...")

            print("This border is taken: ({},{}) {}".format(x, y, border))

            move = str(x) + "," + str(y) + "," + border
            status = requests.get(SERVER + "/move/" + TEAM_ID + "/" + move).json()


if __name__ == "__main__":
    player = reg()
    play(player)
