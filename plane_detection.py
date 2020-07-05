from utils import *


def DetectMultiPlanes(points, min_ratio=0.05, threshold=0.01):
    """ Detect multiple planes from given point clouds

    Args:
        points (np.ndarray): 
        min_ratio (float, optional): The minimum left points ratio to end the Detection. Defaults to 0.05.
        threshold (float, optional): RANSAC threshold in (m). Defaults to 0.01.

    Returns:
        [List[tuple(np.ndarray, List)]]: Plane equation and plane point index
    """

    plane_list = []
    N = len(points)
    count = 0

    while count < (1 - min_ratio) * N:
        w, index = PlaneRegression(points, threshold=threshold)
        plane = points[index]
        points[index] = float('inf') 
        count += len(index)
        plane_list.append((w, index))
    
    return plane_list


if __name__ == "__main__":
    import random

    points = ReadPlyPoint('Data/wash.ply')

    # pre-processing
    points = RemoveNan(points)
    points = DownSample(points,voxel_size=0.003)
    points = RemoveNoiseStatistical(points, nb_neighbors=50, std_ratio=0.5)

    #DrawPointCloud(points, color=(0.4, 0.4, 0.4))

    results = DetectMultiPlanes(points.copy(), min_ratio=0.05, threshold=0.01)

    planes = []
    colors = []
    for _, index in results:
        plane = points[index]

        r = random.random()
        g = random.random()
        b = random.random()

        color = np.zeros((plane.shape[0], plane.shape[1]))
        color[:, 0] = r
        color[:, 1] = g
        color[:, 2] = b

        planes.append(plane)
        colors.append(color)
    
    planes = np.concatenate(planes, axis=0)
    colors = np.concatenate(colors, axis=0)
    DrawResult(planes, colors)
