from lerobot.robots import Robot
from .galaxea_r1_lite_config import r1_lite_config


class r1_lite(Robot):
    config_class = r1_lite_config
    name = "galaxea r1 lite"

    def __init__(self, config: r1_lite_config):
        super().__init__(config)  #sets up robot with spefic config


        #arms using ros2


