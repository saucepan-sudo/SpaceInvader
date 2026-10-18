"""Tests for the Space Invader game module."""

import sys
sys.path.insert(0, '/Users/serenalyla/SpaceInvader')

from space_invader import SpaceInvader

def test_space_invader_creation():
    """Test that a SpaceInvader can be created."""
    invader = SpaceInvader()
    assert invader.alive is True
    print("✓ SpaceInvader creation test passed")

def test_shoot_method():
    """Test the shoot method returns a projectile."""
    invader = SpaceInvader()
    result = invader.shoot()
    assert result == "projectile"
    print("✓ Shoot method test passed")

if __name__ == "__main__":
    test_space_invader_creation()
    test_shoot_method()
