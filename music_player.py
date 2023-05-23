import pygame
import os

# Function to initialize the music player
def initialize_player():
    pygame.init()
    pygame.mixer.init()

# Function to play music
def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Function to stop playing music
def stop_music():
    pygame.mixer.music.stop()

# Function to pause music
def pause_music():
    pygame.mixer.music.pause()

# Function to resume music
def resume_music():
    pygame.mixer.music.unpause()

# Function to display the menu
def display_menu():
    print("1. Play music")
    print("2. Stop music")
    print("3. Pause music")
    print("4. Resume music")
    print("5. Exit")

# Function to get user's choice
def get_choice():
    choice = input("Enter your choice (1-5): ")
    return int(choice)

# Main program
if __name__ == '__main__':
    initialize_player()

    while True:
        display_menu()
        choice = get_choice()

        if choice == 1:
            file_path = input("Enter the path of the music file: ")
            if os.path.exists(file_path):
                play_music(file_path)
            else:
                print("Invalid file path!")

        elif choice == 2:
            stop_music()

        elif choice == 3:
            pause_music()

        elif choice == 4:
            resume_music()

        elif choice == 5:
            stop_music()
            break

        else:
            print("Invalid choice!")

    pygame.quit()
