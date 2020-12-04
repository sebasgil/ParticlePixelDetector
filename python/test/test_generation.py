import generation
import numpy

def test_unifrom_sphere_generator():
    """
    Verify properties of the UniformSphereGenerator
    """
    rng = generation.UniformSphereGenerator(0)
    for _ in range(50):
        point = rng.generate_random_point()
        # verify it's a numpy array
        assert isinstance(point, numpy.ndarray)
        # verify it's 3d point
        assert point.shape == (3,)
        # verify it's on the surface of the unit sphere
        assert numpy.isclose(numpy.linalg.norm(point), 1)
