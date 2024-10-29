import random

def simulate_dog_flea():
    n = 20
    initial_state = (n, 0)
    total_iterations = 0
    counter = 0

    for simulation in range(0, 20):
        state = list(initial_state)
        iterations = 0


        while True:
            iterations += 1
            r_i = random.random()

            # Transition logic
            if r_i < 0.2 and state[0] > 0:
                state[0] -= 1
                state[1] += 1
            elif r_i >= 0.2 and state[1] > 0:
                state[0] += 1
                state[1] -= 1


            print(
                f"Simulation {simulation+1}, Iteration {iterations}, Random number: {r_i:.2f}, State: X({iterations}) = {state}")


            if state == list(initial_state):
                counter += 1
                break

        total_iterations += iterations
        if total_iterations > 19:
            break


    average_return_time = counter / 20
    print(f"\nAverage number of iterations to return to initial state: {average_return_time:.2f}")

# Run the simulation
simulate_dog_flea()
