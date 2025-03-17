from game import Game

def get_user_menu_choice():
    """Displays a menu and gets the user's choice."""
    print("\nMenu:")
    print("1. Play a new game")
    print("2. Show scores")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice in ["1", "2", "3"]:
        return choice
    else:
        print("Invalid choice. Please try again.")
        return get_user_menu_choice() 

def print_results(results):
    """Displays the game results in a user-friendly format."""
    print("\nGame Summary:")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("Thanks for playing!")

def main():
    """Main function to handle game logic and menu."""
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == "1":  
            game = Game()
            result = game.play()
            results[result] += 1  

        elif choice == "2":  
            print_results(results)

        elif choice == "3":  
            print_results(results)
            break 

if __name__ == "__main__":
    main()
