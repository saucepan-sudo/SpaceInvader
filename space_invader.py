"""Space Invader game module."""

class SpaceInvader:
    """Represents a single Space Invader enemy unit."""
    
    def __init__(self):
        self.alive = True
        self.x = 0
        self.y = 0
    
    def shoot(self):
        """Fire a projectile at the player."""
        print("SpaceInvader shoots!")
        return "projectile"
