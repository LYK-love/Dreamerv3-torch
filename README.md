# Installation
Env:
1. ubuntu22.04
2. X86_64
3. Python3.9
## Step1: Install OpenGL rendering backands packages 

MuJoCo/DMC supports three different OpenGL rendering backends: EGL (headless), GLFW (windowed), and OSMesa (headless). For each of them, you need to install some packages:

1. GLFW: sudo apt-get install libglfw3 libglew2.2 
2. EGL: sudo apt-get install libglew2.2 
3. OSMesa: sudo apt-get install libgl1-mesa-glx libosmesa6

Then, in order to use one of these rendering backends, you need to set the `MUJOCO_GL` environment variable to "glfw", "egl", "osmesa", respectively.

Note:

> The libglew2.2 could have a different name, based on your OS (e.g., libglew2.2 is for Ubuntu 22.04.2 LTS).

For more information: https://github.com/deepmind/dm_control and https://mujoco.readthedocs.io/en/stable/programming/index.html#using-opengl

## Step2: Install Python Dependencies

Get dependencies with python 3.9:

```sh
pip install -r requirements.txt
```

Check if all dependencies are OK:

```sh
python test.py
```

# Usage

Run training on DMC Vision:

```sh
python3 dreamer.py --configs dmc_vision --task dmc_walker_walk --logdir ./logdir/dmc_walker_walk
```

Monitor results:

```sh
tensorboard --logdir ./logdir
```

# Benchmarks

So far, the following benchmarks can be used for testing.

# Results

## DMC Proprio

## DMC Vision

## Atari 100k


## Crafter

<img src="https://github.com/NM512/dreamerv3-torch/assets/70328564/a0626038-53f6-4300-a622-7ac257f4c290" width="300" height="150" />

# Acknowledgments

This code is heavily inspired by the following works:

- NM512's Dreamer-v3 PyTorch implementation: https://github.com/NM512/dreamerv3-torch
- danijar's Dreamer-v3 jax implementation: https://github.com/danijar/dreamerv3