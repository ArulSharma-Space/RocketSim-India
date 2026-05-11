import numpy as np
import matplotlib.pyplot as plt

class RocketSimIndia:
    def __init__(self):
        # Rocket specs (realistic model rocket)
        self.mass = 5.0      # kg
        self.thrust = 100.0   # Newtons (JEE-level thrust)
        self.diameter = 0.06 # meters
        self.g = 9.81        # gravity
        
    def simulate(self, burn_time=3.0, sim_time=20.0):
        # Time steps
        dt = 0.01
        t = np.arange(0, sim_time, dt)
        
        # Initialize arrays
        altitude = np.zeros_like(t)
        velocity = np.zeros_like(t)
        thrust_active = np.zeros_like(t)
        drag_force = np.zeros_like(t)
        
        for i in range(1, len(t)):
            # Thrust phase (first 3 seconds)
            if t[i] <= burn_time:
                thrust_active[i] = self.thrust
            else:
                thrust_active[i] = 0
                
            # Drag force (simplified, JEE physics)
            air_density = 1.225 * np.exp(-altitude[i-1]/8000)  # atmosphere model
            area = np.pi * (self.diameter/2)**2
            drag = 0.5 * air_density * area * 0.75 * velocity[i-1]**2
            
            # Net force (Newton's 2nd law - your JEE chapter!)
            net_force = thrust_active[i] - self.mass * self.g - drag
            acceleration = net_force / self.mass
            
            # Update (Euler method - simple but works)
            velocity[i] = velocity[i-1] + acceleration * dt
            altitude[i] = altitude[i-1] + velocity[i] * dt
            
            drag_force[i] = drag
            
        return t, altitude, velocity, thrust_active, drag_force
    
    def plot(self, t, altitude, velocity, thrust_active, drag_force):
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))
        
        # Altitude vs time
        ax1.plot(t, altitude, 'b-', linewidth=2)
        ax1.set_ylabel('Altitude (m)')
        ax1.set_title('RocketSim-India: Your First Rocket Trajectory')
        ax1.grid(True)
        ax1.set_ylim(0, max(altitude)*1.1)
        
        # Velocity vs time
        ax2.plot(t, velocity, 'r-', linewidth=2)
        ax2.set_ylabel('Velocity (m/s)')
        ax2.set_xlabel('Time (s)')
        ax2.grid(True)
        
        # Forces
        ax3.plot(t, thrust_active, 'g-', label='Thrust', linewidth=2)
        ax3.plot(t, drag_force, 'orange', label='Drag', linewidth=2)
        ax3.plot(t, self.mass*self.g*np.ones_like(t), 'k--', label='Weight')
        ax3.set_xlabel('Time (s)')
        ax3.set_ylabel('Force (N)')
        ax3.legend()
        ax3.grid(True)
        
        plt.tight_layout()
        plt.savefig('rocket_sim_india.png', dpi=300, bbox_inches='tight')
        plt.show()
        print(f"Max altitude: {max(altitude):.0f} meters!")
        print("Screenshot saved as rocket_sim_india.png")
def interactive_launch(self):
    print("🚀 RocketSim-India Launcher")
    mass = float(input("Rocket mass (kg): 5"))
    thrust = float(input("Thrust (N): 100"))
    burn = float(input("Burn time (s): 4"))
    
    self.mass = mass
    sim = self.simulate(burn_time=burn)
    self.plot(*sim)

# RUN IT
if __name__ == "__main__":
    sim = RocketSimIndia()
    t, alt, vel, thrust, drag = sim.simulate(burn_time=3.0, sim_time=25.0)
    sim.plot(t, alt, vel, thrust, drag)