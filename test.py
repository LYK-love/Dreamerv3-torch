
import os
import subprocess
def torch_info():
    import torch

    if (torch.cuda.is_available()):
        # Print the number of available GPUs
        print(torch.cuda.device_count(), "GPU(s) available.")

        # Print the name of the current GPU
        print("Current GPU:", torch.cuda.get_device_name(0))
    else:
        print("No GPU available. Switching to CPU.")
        device = torch.device("cpu")

def os_info():
    import platform
    # 获取操作系统名称
    os_name = platform.system()

    # 获取操作系统版本
    os_version = platform.version()

    # 获取操作系统位数（32位或64位）
    os_architecture = platform.architecture()
    # 打印操作系统信息
    print(f"Operating System: {os_name}")
    print(f"Operating System Version: {os_version}")
    print(f"Architecture: {os_architecture}")

def python_info():
    import sys

    print("Python version")
    print(sys.version)
    print("Version info.")
    print(sys.version_info)

if __name__ == "__main__":
    python_info()
    torch_info()

    if subprocess.run('nvidia-smi').returncode:
        raise RuntimeError(
            'Cannot communicate with GPU. '
            'Make sure you are using a GPU Colab runtime. '
            'Go to the Runtime menu and select Choose runtime type.')

    # Add an ICD config so that glvnd can pick up the Nvidia EGL driver.
    # This is usually installed as part of an Nvidia driver package, but the Colab
    # kernel doesn't install its driver via APT, and as a result the ICD is missing.
    # (https://github.com/NVIDIA/libglvnd/blob/master/src/EGL/icd_enumeration.md)
    # NVIDIA_ICD_CONFIG_PATH = '/usr/share/glvnd/egl_vendor.d/10_nvidia.json'
    # if not os.path.exists(NVIDIA_ICD_CONFIG_PATH):
    #     with open(NVIDIA_ICD_CONFIG_PATH, 'w') as f:
    #         f.write("""{
    #     "file_format_version" : "1.0.0",
    #     "ICD" : {
    #         "library_path" : "libEGL_nvidia.so.0"
    #     }
    # }
    # """)

    os.environ["MUJOCO_GL"] = "egl"


    print('Checking that the dm_control installation succeeded...')
    try:
        from dm_control import suite

        env = suite.load('walker', 'walk')
        pixels = env.physics.render()
    except Exception as e:
        raise e from RuntimeError(
            'Something went wrong during installation. Check the shell output above '
            'for more information.\n'
            'If using a hosted Colab runtime, make sure you enable GPU acceleration '
            'by going to the Runtime menu and selecting "Choose runtime type".')
    else:
        del pixels, suite

    # print('Checking that the dm_control installation succeeded...')
    # try:
    #     from dm_control import suite
    #
    #     env = suite.load('cartpole', 'swingup')
    #     pixels = env.physics.render()
    # except Exception as e:
    #     raise e from RuntimeError(
    #         'Something went wrong during installation. Check the shell output above '
    #         'for more information.\n'
    #         'If using a hosted Colab runtime, make sure you enable GPU acceleration '
    #         'by going to the Runtime menu and selecting "Choose runtime type".')
    # else:
    #     del pixels, suite



