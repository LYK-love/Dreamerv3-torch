# Installation

Pytorch implementation of paper [Mastering Diverse Domains through World Models](https://arxiv.org/abs/2301.04104v1), aka DreamerV3. DreamerV3 is a scalable algorithm that outperforms previous approaches across various domains with fixed hyperparameters.
This implementation is based on ctallec's codebase, where the dependencies are not precisely specified. I overcome this shortcoming by detailing the dependency version and testing it.

This implementation is based on [NM512's codebase](https://github.com/NM512/dreamerv3-torch), where the dependencies are not precisely specified. I overcome this shortcoming by detailing the dependency version and testing it.

Code tested on:

* Ubuntu22.04 or 20.04. x86_64.
* Nvidia Driver Version: 545.23.08 CUDA Version: 12.3
* Python3.9

You'll be safe to go if following this specification.

## Step1: Install OpenGL rendering backands packages 

MuJoCo/DMC supports three different OpenGL rendering backends: EGL (headless), GLFW (windowed), and OSMesa (headless). For each of them, you need to install some packages:

1. GLFW: sudo apt-get install libglfw3 libglew2.2 
2. EGL: sudo apt-get install libglew2.2 
3. OSMesa: sudo apt-get install libgl1-mesa-glx libosmesa6

Then, in order to use one of these rendering backends, you need to set the `MUJOCO_GL` environment variable to "glfw", "egl", "osmesa", respectively.
I've set it to `egl` in the code, so you don't need to set it manually if you also using `egl`.
Note:

> The `libglew2.2` could have a different name, based on your OS.
> In Ubuntu 22.04 LTS, it's `libglew2.2`. 
> In Ubuntu 20.04 LTS, it's `libglew2.1`. 

For more information: https://github.com/deepmind/dm_control and https://mujoco.readthedocs.io/en/stable/programming/index.html#using-opengl

## Step2: Install Python Dependencies

Get dependencies with python 3.9:

```sh
pip install setuptools==65.5.0 "wheel<0.40.0"
pip install -r requirements.txt
```

the first command is to avoid [this error](https://github.com/readthedocs/readthedocs.org/issues/10286).

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

# Acknowledgments

This code is heavily inspired by the following works:

- NM512's Dreamer-v3 PyTorch implementation: https://github.com/NM512/dreamerv3-torch
- danijar's Dreamer-v3 jax implementation: https://github.com/danijar/dreamerv3
