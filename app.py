import os

maze_map = [
    list("#######"),
    list("#S  # #"),
    list("### # #"),
    list("#    E#"),
    list("# ### #"),
    list("#    ##"),
    list("#######")
]

def find_start(maze):
    for y, row in enumerate(maze):
        for x, val in enumerate(row):
            if val == 'S':
                return x, y

player_x, player_y = find_start(maze_map)

def draw_maze(maze, px, py):
    os.system("cls" if os.name == "nt" else "clear")
    for y, row in enumerate(maze):
        line = ""
        for x, char in enumerate(row):
            line += 'P' if (x, y) == (px, py) else char
        print(line)

def is_valid_move(maze, x, y):
    if 0 <= y < len(maze) and 0 <= x < len(maze[0]):
        return maze[y][x] != '#'
    return False

def play():
    global player_x, player_y
    while True:
        draw_maze(maze_map, player_x, player_y)
        move = input("Ход (W/A/S/D): ").strip().lower()

        dx, dy = 0, 0
        if move == 'w': dy = -1
        elif move == 's': dy = 1
        elif move == 'a': dx = -1
        elif move == 'd': dx = 1
        else:
            print("Неверная команда.")
            continue

        new_x, new_y = player_x + dx, player_y + dy

        if is_valid_move(maze_map, new_x, new_y):
            player_x, player_y = new_x, new_y
        else:
            print("Там стена.")

        if maze_map[player_y][player_x] == 'E':
            draw_maze(maze_map, player_x, player_y)
            print("🎉 Победа! Вы нашли выход!")
            break

if __name__ == "__main__":
    play()
