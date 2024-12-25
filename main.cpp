#include <iostream>
#include <fstream>

#include <vector>
#include <cmath>
#include <numeric> 
#include <cstdlib>
#include <fstream>

#include "lib/mpreal/mpreal.h"

#include "brutus_code/Star.h"
#include "brutus_code/Cluster.h"
#include "brutus_code/Bulirsch_Stoer.h"
#include "brutus_code/Brutus.h"


#define MAX_TIME_PRECISION 1e10


// The Cluster object is stored here. It is created in the initCluster() function that is called from the Python code
std::unique_ptr<Cluster> cl;
std::vector<int> star_identifiers;


std::string result_string(Brutus b)
{
    mpreal t_current = b.get_t();
    std::vector<mpreal> data = b.get_data();
    Cluster cl(data);

    // Get energies
    std::vector<mpreal> energies = cl.energies();
    mpreal energy_total = energies[0];
    mpreal energy_kinetic = energies[1];
    mpreal energy_potential = energies[2];

    // Create string with the current state of the simulation
    std::string result = std::to_string(t_current.toDouble()) + ",";

    // Size of the star vector
    result += std::to_string(cl.s.size()) + ",";

    // Add the star data to the string
    for (int i = 0; i < cl.s.size(); i++) {
        result += std::to_string(star_identifiers[i]) + ","
        + std::to_string(cl.s[i].r[0].toDouble()) + ","
        + std::to_string(cl.s[i].r[1].toDouble()) + ","
        + std::to_string(cl.s[i].r[2].toDouble()) + ","
        + std::to_string(cl.s[i].v[0].toDouble()) + ","
        + std::to_string(cl.s[i].v[1].toDouble()) + ","
        + std::to_string(cl.s[i].v[2].toDouble()) + ","
        + std::to_string(cl.s[i].m.toDouble()) + ",";
    }
    
    // Add the energy data to the string
    result += std::to_string(energy_total.toDouble()) + ","
        + std::to_string(energy_kinetic.toDouble()) + ","
        + std::to_string(energy_potential.toDouble());

    return result;
}


// The external interface used by the Python code
extern "C" {

    /**
     * Initializes a Cluster object for the simulation
     */
    void initCluster(const char *seed)
    {
        hash<string> hasher;
        mpfr::random(hasher(seed));  // This line seeds the random number generator

        cl = std::make_unique<Cluster>();   
    }
    
    /**
     * Adds a start to the configured Cluster object.
     * initCluster() must be called before this function.
     */
    void addStar(int identifier, double m, double r[3], double v[3])
    {   
        if (cl == nullptr) {
            std::cout << "Cluster object is null" << std::endl;
            return;
        }
        cl->s.push_back(Star(m, {r[0], r[1], r[2]}, {v[0], v[1], v[2]}));
        star_identifiers.push_back(identifier);
    }

    /**
     * Evolves the simulation to the specified end time.
     * initCluster() and addStar() must be called before this function.
     * 
     * The callback function is called when a simulation step is finished.
     * This function is used to update the Python code with the current state of the simulation.
     */
    void evolve(double t_end, double t_step, void (*callback)(const char*))
    {   
        if (cl == nullptr) {
            std::cout << "Cluster object is null" << std::endl;
            return;
        }
        mpreal t = "0";
        mpreal tolerance = "1e-10";
        int numBits = 88;

        std::vector<mpreal> data = cl->get_data();

        Brutus b(t, data, tolerance, numBits);

        mpreal current_evolve_time = 0;

        callback(result_string(b).c_str());

        do
        {
            current_evolve_time += t_step;
            if (current_evolve_time >= t_end)
            {
                current_evolve_time = t_end;
            }

            // Round the current time to avoid floating point errors
            current_evolve_time = round(current_evolve_time * MAX_TIME_PRECISION) / MAX_TIME_PRECISION;

            b.evolve(current_evolve_time);

            callback(result_string(b).c_str());
        
        } while (current_evolve_time < t_end);
    }

    /**
     * Cleans up the Cluster object. This function should be called when the simulation is finished.
     */
    void cleanup()
    {
        cl.reset();
        star_identifiers.clear();
    }
}
