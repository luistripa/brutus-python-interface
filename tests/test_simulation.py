import pytest
from brutus import Star, Cluster, BrutusIntegrator, PandasOutput


class TestSimulation:
    @pytest.fixture
    def cluster(self):
        return Cluster(name='test', stars=[
            Star(identifier=0, position=[0, 0, 0], velocity=[0, 0, 0], mass=1),
            Star(identifier=1, position=[1, 0, 0], velocity=[0, 1, 0], mass=1),
            Star(identifier=2, position=[0, 1, 0], velocity=[0, 0, 1], mass=1),
        ])

    def test_simulation_init(self, cluster):
        integrator = BrutusIntegrator(time_step=0.2)
        assert integrator.time_step == 0.2
        assert integrator.bulirsch_stoer_tolerance == 1e-11
        assert integrator.word_length == 128
        assert integrator.workers == 1
    
    def test_simulation_add_cluster(self, cluster):
        integrator = BrutusIntegrator(time_step=0.2)
        integrator.add_cluster(cluster, output_handler=PandasOutput(cluster))
        assert integrator.clusters == [cluster]
        assert isinstance(integrator.output_handlers[0], PandasOutput)

    def test_simulation_evolve(self, cluster):
        integrator = BrutusIntegrator(time_step=0.2)
        integrator.add_cluster(cluster, output_handler=PandasOutput(cluster))
        results = integrator.evolve(1)
        
        assert len(results) == 1

        result = results[0]
        
        assert len(result) == 6
        assert 'time' in result.columns
        assert 'star_count' in result.columns
        assert 'star_0_pos' in result.columns
        assert 'star_0_vel' in result.columns
        assert 'star_0_mass' in result.columns
        assert 'star_1_pos' in result.columns
        assert 'star_1_vel' in result.columns
        assert 'star_1_mass' in result.columns
        assert 'star_2_pos' in result.columns
        assert 'star_2_vel' in result.columns
        assert 'star_2_mass' in result.columns
        assert 'total_energy' in result.columns
        assert 'kinetic_energy' in result.columns
        assert 'potential_energy' in result.columns

    def test_simulation_evolve_multiple_clusters(self, cluster):
        integrator = BrutusIntegrator(time_step=0.2)
        integrator.add_cluster(cluster, output_handler=PandasOutput(cluster))
        integrator.add_cluster(cluster, output_handler=PandasOutput(cluster))
        results = integrator.evolve(1)
        
        assert len(results) == 2

        result = results[0]
        
        assert len(result) == 6
        assert 'time' in result.columns
        assert 'star_count' in result.columns
        assert 'star_0_pos' in result.columns
        assert 'star_0_vel' in result.columns
        assert 'star_0_mass' in result.columns
        assert 'star_1_pos' in result.columns
        assert 'star_1_vel' in result.columns
        assert 'star_1_mass' in result.columns
        assert 'star_2_pos' in result.columns
        assert 'star_2_vel' in result.columns
        assert 'star_2_mass' in result.columns
        assert 'total_energy' in result.columns
        assert 'kinetic_energy' in result.columns
        assert 'potential_energy' in result.columns

        result = results[1]
        
        assert len(result) == 6
        assert 'time' in result.columns
        assert 'star_count' in result.columns
        assert 'star_0_pos' in result.columns
        assert 'star_0_vel' in result.columns
        assert 'star_0_mass' in result.columns
        assert 'star_1_pos' in result.columns
        assert 'star_1_vel' in result.columns
        assert 'star_1_mass' in result.columns
        assert 'star_2_pos' in result.columns
        assert 'star_2_vel' in result.columns
        assert 'star_2_mass' in result.columns
        assert 'total_energy' in result.columns
        assert 'kinetic_energy' in result.columns
        assert 'potential_energy' in result.columns
