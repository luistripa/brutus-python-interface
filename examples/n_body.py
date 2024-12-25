
import brutus as br

if __name__ == '__main__':
    # Create a cluster of stars
    cluster = br.Cluster(
        stars=[
            br.Star(identifier=0, position=[0, 0, 0], velocity=[0, 0, 0], mass=1),
            br.Star(identifier=1, position=[1, 0, 0], velocity=[0, 1, 0], mass=1),
            br.Star(identifier=2, position=[0, 1, 0], velocity=[-1, 0, 0], mass=1),
            br.Star(identifier=3, position=[0, -1, 0], velocity=[0, -1, 0], mass=1),
            br.Star(identifier=4, position=[-1, 0, 0], velocity=[1, 1, 0], mass=1),
        ],
    )

    # Create a Brutus simulation
    brutus = br.BrutusIntegrator(time_step=0.1)
    brutus.add_cluster(cluster, output_handler=br.PandasOutput(cluster))

    results = brutus.evolve(1)

    print(results[0])
