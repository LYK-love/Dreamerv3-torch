
import os
import subprocess
def torch_info():
    import torch
    if torch.cuda.is_available():
        num_gpus = torch.cuda.device_count()
        print(f"{num_gpus} GPU(s) available.")

        for i in range(num_gpus):
            print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
    else:
        print("No GPU available. Switching to CPU.")


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

def env_variable_info():
    value = os.getenv("MUJOCO_GL")
    print(f"Environment variable `MUJOCO_GL` = {value}")
if __name__ == "__main__":

    python_info()
    torch_info()
    os_info()
    env_variable_info()



    if subprocess.run('nvidia-smi').returncode:
        raise RuntimeError(
            'Cannot communicate with GPU. '
            'Make sure you are using a GPU Colab runtime. '
            'Go to the Runtime menu and select Choose runtime type.')


    # print('Checking that the dm_control installation succeeded...')
    # try:
    #     from dm_control import suite
    #
    #     env = suite.load('walker', 'walk')
    #     pixels = env.physics.render()
    # except Exception as e:
    #     raise e from RuntimeError(
    #         'Something went wrong during installation. Check the shell output above '
    #         'for more information.\n'
    #         'If using a hosted Colab runtime, make sure you enable GPU acceleration '
    #         'by going to the Runtime menu and selecting "Choose runtime type".')
    # else:
    #     del pixels, suite

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



