# Turtle Crossing Game

This project is a Python implementation of a simple Turtle Crossing Game. The player controls a turtle character that must cross a road filled with moving cars to reach the finish line. As the player progresses, the speed of the cars increases, and the level is displayed on the screen.

---

## Features
- Player-controlled turtle character.
- Randomly generated moving cars.
- Level progression with increasing difficulty.
- Game over screen when the turtle collides with a car.

---

## Libraries Used

### 1. `turtle`
- Provides graphical interface and animation.
- Used for creating and controlling game objects such as the player, cars, and scoreboard.

### 2. `time`
- Used to manage game loop delays and create a smooth animation.

### 3. `random`
- Facilitates randomization of car colors and spawn locations.

---

## Code Explanation

### **1. `car_manager.py`**
This module handles the creation and movement of cars.
- **Key Classes and Methods:**
  - `CarManager`:
    - Manages a list of car objects.
    - Creates new cars randomly.
    - Moves all cars leftward and increases their speed as the player progresses.
  - `car_creation`: Creates a new car at a random vertical position with a random color.
  - `movement`: Moves cars leftward on the screen.
  - `speed_increase`: Increases car speed to make the game more challenging.

### **2. `player.py`**
This module manages the player's turtle character.
- **Key Classes and Methods:**
  - `Player`:
    - Initializes a turtle at the starting position.
    - Moves the turtle upward and checks if it reaches the finish line.
  - `go_up`: Moves the turtle forward.
  - `is_at_finish`: Checks if the turtle has reached the top of the screen.
  - `go_to_start`: Resets the turtle to the starting position.

### **3. `scoreboard.py`**
This module displays the player's level and game over message.
- **Key Classes and Methods:**
  - `Scoreboard`:
    - Displays the current level on the screen.
    - Increases the level when the player completes a crossing.
    - Displays a "Game Over" message when the game ends.
  - `increase_level`: Updates the level on the screen.
  - `game_over`: Displays the "Game Over" message.

### **4. `main.py`**
This is the main game loop and entry point of the program.
- **Key Functions:**
  - Sets up the game screen and initializes the player, cars, and scoreboard.
  - Listens for player input (`W` key to move up).
  - Manages game updates, including car creation, movement, and collision detection.
  - Ends the game when the player collides with a car.

---

## How to Run

1. **Install Python**:
   Ensure you have Python 3.x installed on your machine.

2. **Run the Game**:
   Execute the `main.py` script:
   ```bash
   python main.py
   ```

3. **Controls**:
   - Press `W` to move the turtle upward.

---

## Gameplay Instructions
- Your goal is to move the turtle to the top of the screen while avoiding cars.
- Each successful crossing increases the level and the speed of the cars.
- The game ends if the turtle collides with a car.

---

## File Structure

- **`main.py`**: The main script to initialize and run the game.
- **`car_manager.py`**: Handles car creation and movement.
- **`player.py`**: Manages the player's turtle character.
- **`scoreboard.py`**: Displays the game level and "Game Over" message.

---

## Notes
- This game is a fun project for learning Python and graphical programming using the `turtle` module.
- Extendable to include more features such as different levels, power-ups, or new obstacles.

---

## License
This project is open-source and available under the MIT License.
