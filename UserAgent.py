#!/usr/bin/env python
from random import choice
user_agent_list = []
resource_file = '/home/shici/Documents/.rsrc/user-agents.txt'
def return_ua():
    with open(resource_file,'r') as user_agent_file:
        for user_agent in user_agent_file.readlines():
            user_agent_list.append(user_agent)
        user_agent_file.close()
    return(choice(user_agent_list))


