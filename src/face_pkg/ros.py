#!/usr/bin/env python
import rospy
import rosnode
from std_msgs.msg import String

class ROS:

    def __init__(self, num_of_parrots):
        self.parrot_publishers = []
        for i in range(num_of_parrots):
            self.__init_parrot_publishers(i)

        rospy.init_node('multi_parrot', anonymous=False, disable_signals=True)

    def get_parrot_publisher(self, id):
        return self.parrot_publishers[id]

    def get_parrot_publishers_count(self):
        return len(self.parrot_publishers)

    def __init_parrot_publishers(self, id):
        prefix = 'parrot/%s/' % id

        publisher_group = {}
        publisher_group['cmd_name'] = rospy.Publisher(prefix + 'parrot_command_name', String, queue_size=10)
        publisher_group['cmd_arg'] = rospy.Publisher(prefix + 'parrot_commands', String, queue_size=10)
        publisher_group['voice_path'] = rospy.Publisher(prefix + 'audio_player', String, queue_size=10)

        self.parrot_publishers.append(publisher_group)


