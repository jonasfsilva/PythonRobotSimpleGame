
# coding: utf-8

# In[1]:


class Point(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "<{0}, {1}>".format(self.y, self.x)
    
    def __repr__(self):
        return "{1}".format(str(self))


# In[2]:


class Robot(Point):
    
    def __init__(self, x, y):
        super(Robot, self).__init__(x, y)
        
    def move_up(self):
        if self.y + 1 > 10:
            print("Movimento Invalido!!!")
        else:
            self.y = self.y + 1
    
    def move_down(self):
        if self.y - 1 < 0:
            print("Movimento Invalido!!!")
        else:
            self.y = self.y - 1
    
    def move_left(self):
        if self.x + 1 > 10:
            print("Movimento Invalido!!!")
        else:
            self.x = self.x - 1
    
    def move_rigth(self):
        if self.x - 1 < 0:
            print("Movimento Invalido!!!")
        else:
            self.x = self.x + 1


# In[3]:


class Reward(Point):
    
    def __init__(self, x, y, name):
        super(Reward, self).__init__(x, y)
        self.name = name
    
    def __str__(self):
        return "<{0}, {1} | {2} >".format(self.y, self.x, self.name)
    
    def __repr__(self):
        return "<{0}, {1} | {2} >".format(self.y, self.x, self.name)


# In[4]:


def check_reward(robot, rewards):
    for reward in rewards:
        if reward.x == robot.x and reward.y == robot.y:
            print('Recompensa encontrada {0}'.format(reward.name))


# In[5]:


import random

choices = ('ouro', 'gasolina', 'prata', 'peruca',)
rewards = []
for _ in range(10):
    rewards.append(Reward(random.randint(0, 10), 
                          random.randint(0, 10), 
                          random.choice(choices)))

robot = Robot(random.randint(0, 10), random.randint(0, 10))


# In[10]:


for _ in range(10):
    mov = input("Digite up, down, left ou rigth para movimentar o robo: ")
    
    if mov in ['left', 'rigth', 'up', 'down']:
        method_name = 'move_{0}'.format(mov)
        getattr(robot, method_name)()
        check_reward(robot, rewards)
    else: 
        print("Comando invalido!!")

