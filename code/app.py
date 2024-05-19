import streamlit as st

# Define the initial game state
game_state = {
    'current_room': 'start',
    'message': 'Welcome to the Text Adventure! Choose your path...',
}

# Define the rooms and their descriptions
rooms = {
    'start': {
        'description': 'You are in a dark room. There are two doors in front of you.',
        'choices': {
            'left': 'Go left',
            'right': 'Go right',
        }
    },
    'left': {
        'description': 'You chose the left door. You find a treasure chest!',
        'choices': {
            'start': 'Go back',
        }
    },
    'right': {
        'description': 'You chose the right door. You encounter a monster!',
        'choices': {
            'start': 'Go back',
        }
    },
    'treasure_room': {
        'description': 'You found the treasure room! There are gold coins everywhere.',
        'choices': {
            'start': 'Go back',
        }
    },
    'monster_room': {
        'description': 'You entered the monster room. A giant spider is blocking your way!',
        'choices': {
            'start': 'Go back',
        }
    },
}

def render_game():
    global game_state
    for choice, description in rooms[game_state['current_room']]['choices'].items():
        if st.button(description):
            if choice in rooms[game_state['current_room']]['choices']:
                game_state['current_room'] = choice
                game_state['message'] = rooms[game_state['current_room']]['description']
            else:
                game_state['message'] = 'Invalid choice!'
    st.markdown(f"### {game_state['message']}")

def main():
    st.title("Text Adventure Game")
    render_game()

if __name__ == '__main__':
    main()
