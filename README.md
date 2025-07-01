# Particle Simulator

This repository contains a Python-based particle simulator built with Pygame, modeling the physics-based motion and collisions of 30 particles in a 600x600 pixel 2D environment. Each particle moves under gravity, experiences air drag, and collides with walls and other particles, with velocity updates based on vector mathematics and elasticity. The system supports interactive features like mouse-based particle selection and is applicable to modeling dynamic systems in manufacturing, such as material flow or robotic interactions.

## Table of Contents
- [Particle Simulator](#particle-simulator)
  - [Project Overview](#project-overview)
  - [Approach](#approach)
  - [Tools and Technologies](#tools-and-technologies)
  - [Results](#results)
  - [Skills Demonstrated](#skills-demonstrated)
  - [Setup and Usage](#setup-and-usage)
  - [References](#references)

## Project Overview
The Particle Simulator models 30 particles moving in a 600x600 pixel 2D environment, each with a random initial position, velocity (magnitude 0–30 pixels, direction 0–2π radians), and color. Particles are subject to constant gravity (magnitude 1.1, downward), air drag (0.999 decay), and elastic collisions (0.75 elasticity) with walls and other particles. The simulation runs at 30 FPS for up to 1000 frames, supporting interactive particle selection via mouse clicks. Collision detection and vector-based movement make the system suitable for modeling dynamic processes, such as material interactions in manufacturing.

## Approach
The project is structured as a modular simulation system:
- **Vector Class**: Represents velocity with magnitude and direction (radians), with a static method for vector addition using trigonometric calculations (`sin`, `cos`, `atan2`) to combine velocities.
- **Pixel Class**: Represents a particle with a Pygame `Rect` (30x30 pixels), color, and velocity vector. Handles movement by updating position based on velocity components (`dx`, `dy`).
- **Game Class**:
  - **Initialization**: Creates a 600x600 Pygame window and spawns 30 particles with random positions (50–500 pixels), velocities, and RGB colors.
  - **Physics Simulation**: Applies gravity (downward vector) and air drag (0.999 velocity decay) per frame. Handles wall collisions (left, right, top, bottom) by reflecting velocity direction and reducing magnitude by elasticity (0.75). Detects particle-particle collisions using Euclidean distance (`math.hypot`), resolving overlaps with angle-based displacement and swapping velocities with elasticity.
  - **Rendering**: Draws particles as colored rectangles and displays the frame count using Pygame’s font system. Updates at 30 FPS.
  - **Interaction**: Supports mouse-based particle selection, changing the selected particle’s color to red for visual feedback.
- **Collision Detection**: Uses pairwise distance checks (`math.hypot`) to identify particle collisions (distance ≤ particle size) and resolves them by reflecting velocities along the collision tangent and adjusting positions to prevent overlap.
- **Main Loop**: Runs for 1000 frames or until the user quits, processing events (e.g., mouse clicks, window close), updating particle states, and rendering the scene.

The system simulates realistic particle dynamics with continuous physics updates and user interaction, suitable for modeling complex interactions.

## Tools and Technologies
- **Python**: Core language for simulation logic and physics calculations.
- **Pygame**: Rendering the 2D environment, handling user input, and drawing particles.
- **math**: Trigonometric and geometric calculations for vector operations and collision resolution.
- **random**: Generating initial particle positions, velocities, and colors.

## Results
- **Simulation**: Successfully simulated 30 particles over 1000 frames at 30 FPS, modeling gravity, drag, and elastic collisions in a 600x600 pixel environment.
- **Physics**: Achieved realistic particle dynamics, with accurate wall and particle-particle collision responses (0.75 elasticity, velocity swaps).
- **Interaction**: Enabled mouse-based particle selection, with visual feedback (color change to red) for user engagement.
- **Scalability**: Supported efficient collision detection and rendering for 30 particles, suitable for small-scale dynamic system simulations.

## Skills Demonstrated
- **Physics Simulation**: Implemented vector-based movement, gravity, drag, and elastic collisions, applicable to manufacturing process modeling (e.g., material flow).
- **Game Development**: Built a real-time 2D simulation environment with Pygame, handling rendering and user input.
- **Collision Detection**: Designed efficient pairwise distance checks and angle-based collision resolution.
- **Mathematical Modeling**: Used trigonometry (`sin`, `cos`, `atan2`) for vector operations and physics calculations.
- **Interactive Design**: Developed mouse-based interaction for dynamic particle selection.

## Setup and Usage
1. **Prerequisites**:
   - Clone the repository: `git clone <repository-url>` (replace with actual URL if available).
   - Install dependencies: `pip install pygame`
   - Python 3.6+ required.
2. **Running**:
- Run the simulation: `python main.py`
- Adjust parameters in `main.py`:
  - `screen_dimensions`: Window size (default: 600x600 pixels).
  - `pixel_size`: Particle size (default: 30 pixels).
  - `fps_limit`: Frame rate (default: 30 FPS).
  - `gravity`: Gravity vector (default: magnitude 1.1, downward).
  - `drag`: Air drag coefficient (default: 0.999).
  - `elasticity`: Collision elasticity (default: 0.75).
- Click to select/unselect particles (selected particles turn red).
- Close the window or wait for 1000 frames to end the simulation.
3. **Notes**:
- The simulation runs for 1000 frames or until the user quits.
- Ensure sufficient CPU resources for real-time rendering and collision detection.

## References
- [Pygame Documentation](https://www.pygame.org/docs/)
- [Python math Module](https://docs.python.org/3/library/math.html)
