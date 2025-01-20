import pytest
from brutus import Cluster, Star


class TestCluster:
    def test_cluster_creation(self):
        # Create an example Star
        star = Star(identifier=0, position=(0, 0, 0), velocity=(0, 0, 0), mass=1)

        # Create a Cluster with the Star
        cluster = Cluster(name='test_cluster', stars=[star])

        assert cluster.name == 'test_cluster'
        assert len(cluster.stars) == 1
        assert cluster.stars[0].identifier == star.identifier
        assert cluster.stars[0].position == star.position
        assert cluster.stars[0].velocity == star.velocity
        assert cluster.stars[0].mass == star.mass
    
    def test_cluster_multiple_stars(self):
        # Create a Cluster with multiple Stars
        star1 = Star(identifier=0, position=(0, 0, 0), velocity=(0, 0, 0), mass=1)
        star2 = Star(identifier=1, position=(1, 1, 1), velocity=(1, 1, 1), mass=1)
        cluster = Cluster(name='test_cluster', stars=[star1, star2])

        assert cluster.name == 'test_cluster'
        assert len(cluster.stars) == 2
        assert cluster.stars[0].identifier == star1.identifier
        assert cluster.stars[0].position == star1.position
        assert cluster.stars[0].velocity == star1.velocity
        assert cluster.stars[0].mass == star1.mass
        assert cluster.stars[1].identifier == star2.identifier
        assert cluster.stars[1].position == star2.position
        assert cluster.stars[1].velocity == star2.velocity
        assert cluster.stars[1].mass == star2.mass

    def test_cluster_stars_with_same_identifier(self):
        # Create a Cluster with Stars with the same identifier
        star1 = Star(identifier=0, position=(0, 0, 0), velocity=(0, 0, 0), mass=1)
        star2 = Star(identifier=0, position=(1, 1, 1), velocity=(1, 1, 1), mass=1)

        with pytest.raises(ValueError):
            Cluster(name='test_cluster', stars=[star1, star2])
