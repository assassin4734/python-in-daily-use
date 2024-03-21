import numpy as np
import matplotlib.pyplot as plt


def plot_spatial_cone(a, theta):
    # Generate grid points
    resolution = 100
    x = np.linspace(0, 2*a, resolution)
    y = np.linspace(-a, a, resolution)
    X, Y = np.meshgrid(x, y)

    # Compute z values based on cone equation
    Z = np.sqrt(X**2 + Y**2) * np.tan(theta)

    # Plot the surface
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, alpha=0.5)

    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Spatial Cone Surface')

    # Show the plot
    plt.show()

# Specify apex coordinates (a = 5) and opening angle (theta = 0.5 radians)
apex_x = 5
opening_angle = 0.5

# Call the function to plot the spatial cone surface
plot_spatial_cone(apex_x, opening_angle)
input("done")