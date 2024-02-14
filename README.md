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
conda create -n DreamerTorch python=3.9
activate DreamerTorch
pip install setuptools==65.5.0 "wheel<0.40.0"
pip install -r requirements.txt
```
The first command is to avoid [this error](https://github.com/readthedocs/readthedocs.org/issues/10286).

Check if all dependencies are OK:

```sh
python test.py
```
In addition, you need to install Atari ROMs to run Atari envs, follow [here](https://github.com/openai/atari-py#roms) to download and install ROM:
```sh
wget http://www.atarimania.com/roms/Atari-2600-VCS-ROM-Collection.zip ./
unzip ./Atari-2600-VCS-ROM-Collection.zip
python -m atari_py.import_roms ./ROMS
```
This should print out the names of ROMs as it imports them.  The ROMs will be copied to your `atari_py` installation directory.

You need to 

For example, to make `Alien` env, you need to call `atari_alie`
# Usage
The script for training has the format of:
```sh
python3 dreamer.py --configs <env> --task <suite>_<task> --logdir ./logdir/<suite>_<task>
```
* `<env>`: see `./configs.yaml`
* `<job>`: see `make_env` function in `./dreamer.py`
* `<task>`: the camel case of the task name.

* For atari env, the task name is in the `atari_roms` dir:
```
$ ls  /home/lyk/miniconda3/envs/DreamerTorch/lib/python3.9/site-packages/atari_py/atari_roms
adventure.bin    beam_rider.bin       demon_attack.bin     gopher.bin           koolaid.bin            phoenix.bin      sir_lancelot.bin    tutankham.bin
air_raid.bin     berzerk.bin          donkey_kong.bin      gravitar.bin         krull.bin              pitfall.bin      skiing.bin          up_n_down.bin
alien.bin        bowling.bin          double_dunk.bin      hero.bin             kung_fu_master.bin     pong.bin         solaris.bin         venture.bin
amidar.bin       boxing.bin           elevator_action.bin  ice_hockey.bin       laser_gates.bin        pooyan.bin       space_invaders.bin  video_pinball.bin
assault.bin      breakout.bin         enduro.bin           jamesbond.bin        lost_luggage.bin       private_eye.bin  star_gunner.bin     wizard_of_wor.bin
asterix.bin      carnival.bin         fishing_derby.bin    journey_escape.bin   montezuma_revenge.bin  qbert.bin        surround.bin        yars_revenge.bin
asteroids.bin    centipede.bin        freeway.bin          kaboom.bin           mr_do.bin              riverraid.bin    tennis.bin          zaxxon.bin
atlantis.bin     chopper_command.bin  frogger.bin          kangaroo.bin         ms_pacman.bin          road_runner.bin  tetris.bin
bank_heist.bin   crazy_climber.bin    frostbite.bin        keystone_kapers.bin  name_this_game.bin     robotank.bin     time_pilot.bin
battle_zone
```

Run training on DMC Vision:

```sh
python3 dreamer.py --configs dmc_vision --task dmc_walker_walk --logdir ./logdir/dmc_walker_walk
```

If you have multiple GPUs:
```sh
python3 dreamer.py --configs atari100k --task atari_video_pinball --logdir ./logdir/atari_VideoPinball --device cuda:0
python3 dreamer.py --configs atari100k --task atari_alien --logdir ./logdir/atari_alien --device cuda:1
...
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

# Note
Currently not support `box2d` envs such as `CarRacing`.

# Acknowledgments

This code is heavily inspired by the following works:

- NM512's Dreamer-v3 PyTorch implementation: https://github.com/NM512/dreamerv3-torch
- danijar's Dreamer-v3 jax implementation: https://github.com/danijar/dreamerv3
