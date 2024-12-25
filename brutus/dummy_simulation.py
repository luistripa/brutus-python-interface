import time
import sys


args = sys.argv[1:]

sim_final_time = args[0]
time_step = args[1]
bulirsch_stoer_tolerance = args[2]
word_length = args[3]

star_count = args[4]

# Stars have a 3D position and velocity, and a mass. These are present in the args list
stars = []
for i in range(int(star_count)):
    stars.append({
        'identifier': i,
        'position': [float(args[5 + i * 7]), float(args[5 + i * 7 + 1]), float(args[5 + i * 7 + 2])],
        'velocity': [float(args[5 + i * 7 + 3]), float(args[5 + i * 7 + 4]), float(args[5 + i * 7 + 5])],
        'mass': float(args[5 + i * 7 + 6])
    })

# Simulate the star cluster
t = 0
while t < float(sim_final_time):
    # Print the state of the star cluster at each time step
    out_str = ""
    out_str += str(t) + " "

    star_count = len(stars)
    out_str += str(star_count) + " "

    for star in stars:
        out_str += str(star['identifier']) + " " + str(star['position'][0]) + " " + str(star['position'][1]) + " " + str(star['position'][2]) + " " + str(star['velocity'][0]) + " " + str(star['velocity'][1]) + " " + str(star['velocity'][2]) + " " + str(star['mass']) + " "

    # Total energy, kinetic energy, and potential energy
    out_str += "0 0 0"

    print(out_str)

    # Update the position and velocity of each star
    for star in stars:
        # Update the velocity of each star
        star['velocity'][0] += 0.1
        star['velocity'][1] += 0.1
        star['velocity'][2] += 0.1

        # Update the position of each star
        star['position'][0] += star['velocity'][0] * float(time_step)
        star['position'][1] += star['velocity'][1] * float(time_step)
        star['position'][2] += star['velocity'][2] * float(time_step)

    t += float(time_step)

print()
