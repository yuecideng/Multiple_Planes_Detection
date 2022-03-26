# Multiple Planes Detection

**(New) A new implementation with both C++ and Python API can be found at  [Misc3D](https://github.com/yuecideng/Misc3D). The RANSAC is implemented to support parallel computing which makes it more faster than before. You can also use code in this repo with parallel ransac by build my [Open3D fork](https://github.com/yuecideng/Open3D/tree/yuecideng/MultiThreadPlaneSegmentation), and build Open3D from source. I already PR this improvement and maybe it will be merged into Open3D official branch in the nearly future.**

A fast and simple method for multi-planes detection from point clouds using iterative RANSAC plane fitting.

## Pre-requisite
- Python >= 3.5
- Numpy
- Open3D

You can install numpy and open3d by:
```
pip3 install -r requirements.txt
```

## Usage
You can copy the functions in `utils.py` and `plane_detection.py` into your Python script and use function `DetectMultiPlanes` directly.

An example code can be found by running:
```
python3 plane_detection.py
```

## Results
<img src="Data/result1.jpg" width="800">
<img src="Data/result2.jpg" width="800">
