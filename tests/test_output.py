import pytest
import os.path

from brutus import BaseOutput, RawOutput, PandasOutput, FileOutput, Star, Cluster


class TestBaseOutput:
    def test_init(self):
        output = BaseOutput('cluster')  # cluster is a placeholder (not a real cluster object)
        assert output.cluster == 'cluster'

    def test_receive_output_line(self):
        output = BaseOutput('cluster')
        with pytest.raises(NotImplementedError):
            output.receive_output_line('line')

    def test_finalize(self):
        output = BaseOutput('cluster')
        with pytest.raises(NotImplementedError):
            output.finalize()

    def test_result(self):
        output = BaseOutput('cluster')
        with pytest.raises(NotImplementedError):
            output.result()


class TestRawOutput:
    @pytest.fixture
    def cluster(self):
        return Cluster(name='test', stars=[
            Star(identifier=0, position=(0, 0, 0), velocity=(1, 1, 1), mass=2)
        ])
    
    @pytest.fixture
    def line(self):
        return "0,1,0,0,0,0,1,1,1,2,3,3,3"
    
    def test_init(self):
        output = RawOutput('cluster')
        assert output.cluster == 'cluster'

    def test_receive_output_line(self, cluster, line):
        output = RawOutput(cluster)
        output.receive_output_line(line)

        assert output.data == [line]

    def test_receive_output_line_multiple(self, cluster, line):
        output = RawOutput(cluster)
        output.receive_output_line(line)
        output.receive_output_line(line)

        assert output.data == [line, line]

    def test_finalize(self, cluster, line):
        output = RawOutput(cluster)
        output.receive_output_line(line)
        output.finalize()

        assert output.data == [line]

    def test_result(self, cluster, line):
        output = RawOutput(cluster)
        output.receive_output_line(line)
        output.finalize()

        assert output.result() == [line]


class TestPandasOutput:
    @pytest.fixture
    def cluster(self):
        return Cluster(name='test', stars=[
            Star(identifier=0, position=(0, 0, 0), velocity=(1, 1, 1), mass=1)
        ])
    
    @pytest.fixture
    def line(self):
        return "0,1,0,0,0,0,1,1,1,2,3,3,3"
    
    def test_init(self, cluster):
        output = PandasOutput(cluster)
        assert output.cluster == cluster
        assert output.data == []
        assert output.df is None

    def test_receive_output_line(self, cluster, line):
        output = PandasOutput(cluster)
        output.receive_output_line(line)

        data = output.data[0]

        assert data['time'] == 0.0
        assert data['star_count'] == 1
        assert data['star_0_pos'] == [0.0, 0.0, 0.0]
        assert data['star_0_vel'] == [1.0, 1.0, 1.0]
        assert data['star_0_mass'] == 2.0
        assert data['total_energy'] == 3.0
        assert data['kinetic_energy'] == 3.0
        assert data['potential_energy'] == 3.0

    def test_receive_output_line_multiple(self, cluster, line):
        output = PandasOutput(cluster)
        output.receive_output_line(line)
        output.receive_output_line(line)

        data = output.data[0]

        assert data['time'] == 0.0
        assert data['star_count'] == 1
        assert data['star_0_pos'] == [0.0, 0.0, 0.0]
        assert data['star_0_vel'] == [1.0, 1.0, 1.0]
        assert data['star_0_mass'] == 2.0
        assert data['total_energy'] == 3.0
        assert data['kinetic_energy'] == 3.0
        assert data['potential_energy'] == 3.0
        
        data = output.data[1]

        assert data['time'] == 0.0
        assert data['star_count'] == 1
        assert data['star_0_pos'] == [0.0, 0.0, 0.0]
        assert data['star_0_vel'] == [1.0, 1.0, 1.0]
        assert data['star_0_mass'] == 2.0
        assert data['total_energy'] == 3.0
        assert data['kinetic_energy'] == 3.0
        assert data['potential_energy'] == 3.0
    
    def test_finalize(self, cluster, line):
        output = PandasOutput(cluster)
        output.receive_output_line(line)
        output.finalize()

        assert output.df is not None
    
    def test_result(self, cluster, line):
        output = PandasOutput(cluster)
        output.receive_output_line(line)
        output.finalize()

        assert output.result().shape == (1, 8)
        assert output.result().iloc[0]['time'] == 0.0
        assert output.result().iloc[0]['star_count'] == 1
        assert output.result().iloc[0]['star_0_pos'] == [0.0, 0.0, 0.0]
        assert output.result().iloc[0]['star_0_vel'] == [1.0, 1.0, 1.0]
        assert output.result().iloc[0]['star_0_mass'] == 2.0
        assert output.result().iloc[0]['total_energy'] == 3.0
        assert output.result().iloc[0]['kinetic_energy'] == 3.0
        assert output.result().iloc[0]['potential_energy'] == 3.0


class TestFileOutput:    
    @pytest.fixture
    def cluster(self):
        return Cluster(name='test', stars=[
            Star(identifier=0, position=(0, 0, 0), velocity=(1, 1, 1), mass=1)
        ])
    
    @pytest.fixture
    def line(self):
        return "0,1,0,0,0,0,1,1,1,2,3,3,3"

    def test_init(self, cluster, tmp_path):
        output = FileOutput(cluster, tmp_path)
        assert output.cluster == cluster

    def test_receive_output_line(self, cluster, line, tmp_path):
        output = FileOutput(cluster, tmp_path)
        output.receive_output_line(line)

        assert output.data == [line]

    def test_receive_output_line_multiple(self, cluster, line, tmp_path):
        output = FileOutput(cluster, tmp_path)
        output.receive_output_line(line)
        output.receive_output_line(line)

        assert output.data == [line, line]

    def test_finalize_and_result(self, cluster, line, tmp_path):
        output = FileOutput(cluster, tmp_path)
        output.receive_output_line(line)
        output.finalize()

        assert output.data == [line]
        assert os.path.exists(output.path)
        
        with open(output.path, 'r') as f:
            assert f.read() == line

    def test_result(self, cluster, line, tmp_path):
        output = FileOutput(cluster, tmp_path)
        output.receive_output_line(line)
        output.finalize()
        assert output.result() == None
