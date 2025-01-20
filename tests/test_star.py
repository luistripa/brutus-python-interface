import pytest
from brutus import Star


class TestStar:
    def test_star_creation(self):
        star = Star(identifier=0, position=(0, 0, 0), velocity=(0, 0, 0), mass=1)
        assert star.identifier == 0
        assert star.position == (0, 0, 0)
        assert star.velocity == (0, 0, 0)
        assert star.mass == 1
    
    def test_star_invalid_position(self):
        with pytest.raises(ValueError):
            Star(identifier=0, position=(0, 0), velocity=(0, 0, 0), mass=1)
    
    def test_star_invalid_velocity(self):
        with pytest.raises(ValueError):
            Star(identifier=0, position=(0, 0, 0), velocity=(0, 0), mass=1)

    def test_star_invalid_mass(self):
        with pytest.raises(ValueError):
            Star(identifier=0, position=(0, 0, 0), velocity=(0, 0, 0), mass=0)
        
        with pytest.raises(ValueError):
            Star(identifier=0, position=(0, 0, 0), velocity=(0, 0, 0), mass=-1)
