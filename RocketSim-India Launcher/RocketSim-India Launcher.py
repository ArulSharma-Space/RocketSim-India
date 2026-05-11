import numpy as np
import matplotlib.pyplot as plt


class RocketSimIndia:
    def __init__(self, mass=2.0, thrust=50.0, diameter=0.04):
        self.mass = mass
        self.thrust = thrust
        self.diameter = diameter
        self.g = 9.81

    def simulate(self, burn_time=3.0, sim_time=25.0, dt=0.01):
        t = np.arange(0, sim_time, dt)
        altitude = np.zeros_like(t)
        velocity = np.zeros_like(t)
        thrust_force = np.zeros_like(t)
        drag_force = np.zeros_like(t)

        area = np.pi * (self.diameter / 2) ** 2

        for i in range(1, len(t)):
            if altitude[i - 1] < 0:
                altitude[i - 1] = 0
                velocity[i - 1] = 0
                break

            if t[i] <= burn_time:
                thrust_force[i] = self.thrust
            else:
                thrust_force[i] = 0

            air_density = 1.225 * np.exp(-altitude[i - 1] / 8000)
            drag = 0.5 * air_density * area * 0.75 * velocity[i - 1] ** 2

            if velocity[i - 1] > 0:
                drag = -drag
            else:
                drag = drag

            net_force = thrust_force[i] - self.mass * self.g - drag
            acceleration = net_force / self.mass

            velocity[i] = velocity[i - 1] + acceleration * dt
            altitude[i] = altitude[i - 1] + velocity[i] * dt
            drag_force[i] = abs(drag)

        return t, altitude, velocity, thrust_force, drag_force

    def plot(self, t, altitude, velocity, thrust_force, drag_force):
        fig, axes = plt.subplots(3, 1, figsize=(10, 12))

        axes[0].plot(t, altitude, color="blue", linewidth=2)
        axes[0].set_title("RocketSim-India")
        axes[0].set_ylabel("Altitude (m)")
        axes[0].grid(True)

        axes[1].plot(t, velocity, color="red", linewidth=2)
        axes[1].set_ylabel("Velocity (m/s)")
        axes[1].set_xlabel("Time (s)")
        axes[1].grid(True)

        axes[2].plot(t, thrust_force, label="Thrust", color="green", linewidth=2)
        axes[2].plot(t, drag_force, label="Drag", color="orange", linewidth=2)
        axes[2].plot(t, np.full_like(t, self.mass * self.g), label="Weight", linestyle="--", color="black")
        axes[2].set_xlabel("Time (s)")
        axes[2].set_ylabel("Force (N)")
        axes[2].legend()
        axes[2].grid(True)

        plt.tight_layout()
        plt.show()

    def interactive_launch(self):
        print("RocketSim-India Launcher")
        mass = float(input("Rocket mass (kg): "))
        thrust = float(input("Thrust (N): "))
        burn_time = float(input("Burn time (s): "))

        self.mass = mass
        self.thrust = thrust

        result = self.simulate(burn_time=burn_time)
        self.plot(*result)


if __name__ == "__main__":
    sim = RocketSimIndia()
    sim.interactive_launch()
