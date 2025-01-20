
import brutus as br
import logging

logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    # Create a cluster of stars
    cluster1 = br.Cluster(
        name='example_cluster1',
        stars=[
            br.Star(identifier=0, position=[0, 0, 0], velocity=[0, 0, 0], mass=1),
            br.Star(identifier=1, position=[1, 0, 0], velocity=[0, 1, 0], mass=1),
            br.Star(identifier=2, position=[0, 1, 0], velocity=[0, 0, 1], mass=1),
        ],
    )

    cluster2 = br.Cluster(
        name='example_cluster2',
        stars=[
            br.Star(identifier=0, position=[0, 0, 0], velocity=[0, 0, 0], mass=1),
            br.Star(identifier=1, position=[1, 0, 0], velocity=[0, 1, 0], mass=1),
            br.Star(identifier=2, position=[0, 1, 0], velocity=[0, 0, 1], mass=1),
        ],
    )

    cluster3 = br.Cluster(
        name='example_cluster3',
        stars=[
            br.Star(identifier=0, position=[0, 0, 0], velocity=[0, 0, 0], mass=1),
            br.Star(identifier=1, position=[1, 0, 0], velocity=[0, 1, 0], mass=1),
            br.Star(identifier=2, position=[0, 1, 0], velocity=[0, 0, 1], mass=1),
        ],
    )

    # Create a Brutus simulation
    brutus = br.BrutusIntegrator(time_step=0.1, workers=2)
    brutus.add_cluster(cluster1, output_handler=br.PandasOutput(cluster1))
    brutus.add_cluster(cluster2, output_handler=br.PandasOutput(cluster2))
    brutus.add_cluster(cluster3, output_handler=br.PandasOutput(cluster3))

    results = brutus.evolve(1)

    for i, result in enumerate(results):
        print()
        print('--- Cluster', i, '---')
        print(results[i])
