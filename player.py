#!/usr/bin/env python3
"""Player module for Space Invader game."""

class Player:
    """Represents the player character."""
    
    def __init__(self):
        self.x = 50
        self.y = 100
        self.alive = True
    
    def move(self, direction):
        """Move the player left or right."""
        if direction == "left":
            self.x = max(0, self.x - 10)
        elif direction == "right":
            self.x = min(100, self.x + 10)
        print(f"Player moved to x={self.x}")
    
    def shoot(self):
        """Fire a projectile upward."""
        return {"x": self.x, "y": self.y, "direction": -1}

if __name__ == "__main__":
    player = Player()
    player.move("right")
    print(player.shoot())