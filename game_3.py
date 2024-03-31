# 玩家的初始状态
player_status = {
    'health': 100,
    'wealth': 0,
    'location': 'entrance'
}

# 定义游戏房间和事件
rooms = {
    'entrance': {
        'description': 'You stand at the entrance of a dark, foreboding castle.',
        'actions': ['enter the castle', 'leave']
    },
    'throne_room': {
        'description': 'You are in a magnificent throne room. A treasure chest sits in the corner.',
        'actions': ['open the chest', 'explore further', 'return to entrance']
    },
    # 可以根据需要添加更多房间
}

def get_room_actions(location):
    """Prints the current room's description and available actions."""
    room = rooms[location]
    print(room['description'])
    for action in room['actions']:
        print(f"- {action}")

def move_to_room(choice):
    """Updates the player's location based on their choice."""
    # 这里你需要根据选择更新位置
    pass

# 这只是一个框架，我们还需要填充逻辑。
def game_loop():
    game_running = True
    while game_running:
        current_location = player_status['location']
        get_room_actions(current_location)
        
        choice = input("What do you want to do? ").strip().lower()
        if choice == 'leave':
            print("You've chosen to leave the adventure. Game over.")
            game_running = False
        else:
            # 这里需要一个函数来处理玩家的选择和移动
            move_to_room(choice)

# 启动游戏循环
game_loop()
