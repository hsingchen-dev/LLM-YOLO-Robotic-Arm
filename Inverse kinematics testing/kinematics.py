from configuration import l_1 as l1
from configuration import l_2 as l2
from configuration import l_3 as l3
from configuration import l_4 as l4

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from ipywidgets import interactive, FloatSlider, HBox, VBox, FloatText
from IPython.display import display


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# 计算连杆末端位置的正运动学函数
import numpy as np

def forward_kinematics_xz_plan(theta1, theta2, theta3):
    theta1 = np.radians(theta1)
    theta2 = np.radians(theta2)
    theta3 = np.radians(theta3)
    
    x1 = 0
    z1 = l1
    x2 = l2 * np.cos(theta1) + x1
    z2 = l2 * np.sin(theta1) + z1
    x3 = x2 + l3 * np.cos(theta2+theta1)
    z3 = z2 + l3 * np.sin(theta2+theta1)
    x4 = x3 + l4 * np.cos(theta3+theta2+theta1)
    z4 = z3 + l4 * np.sin(theta3+theta2+theta1)

    x_points = np.array([x1, x2, x3, x4])
    z_points = np.array([z1, z2, z3, z4])

    return x_points, z_points



def forward_kinematics(theta0, theta1, theta2, theta3):
    xs_tmp, zs = forward_kinematics_xz_plan(theta1, theta2, theta3)
    # 计算 xs 和 ys 并转换为 numpy 数组
    theta0_rad=np.radians(theta0)
    xs = np.array([i * np.cos(theta0_rad) for i in xs_tmp])
    ys = np.array([i * np.sin(theta0_rad) for i in xs_tmp])
    zs = np.array(zs)  # 将 zs 转换为 numpy 数组

    # 在数组开头插入 0
    xs = np.concatenate(([0], xs))
    ys = np.concatenate(([0], ys))
    zs = np.concatenate(([0], zs))


    return xs, ys, zs


def plot_robot_forward(theta0,theta1, theta2, theta3):
    xs,ys,zs= forward_kinematics(theta0,theta1, theta2, theta3)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')  # 指定projection='3d'以创建3D图
    # 绘制机器人连杆
    ax.plot(xs, ys,zs, '-',color="orange", lw=4)
    # 显示图像
    ultra=600
    ax.set_xlim(-ultra, ultra)
    ax.set_ylim(-ultra, ultra)
    ax.set_zlim(-ultra, ultra)
    ax.set_title(r'$x$: %.2f, $y$: %.2f, $z$: %.2f' % (xs[-1], ys[-1],zs[-1]))
    plt.show()
    
    
def inverse_kinematics(x,y,z,beta,type="lower"):
    beta=np.deg2rad(beta)
    theta_0=np.arctan2(y,x)
    theta_3=beta
    x_tmp=x/np.cos(theta_0)
    z_tmp=z     
    x_tmp=x_tmp-l4*np.cos(theta_3)
    z_tmp=z_tmp-l4*np.sin(theta_3)-l1
    r=np.sqrt(x_tmp**2+z_tmp**2)
    # 此时的theta_2是[0,pi]
    theta_2=np.arccos((r**2-l2**2-l3**2)/(2*l2*l3))
    if type=="upper":
        theta_2=-theta_2
    epsilon=np.arctan2(l3*np.sin(theta_2)/(l2+l3*np.cos(theta_2)))
    phi=np.arctan2(z_tmp,x_tmp)
    theta_1=phi-epsilon
    theta_3=theta_3-theta_2-theta_1
    return theta_0,theta_1,theta_2,theta_3
    # 后面就直接转换成了
    # 视频原理讲解
    # https://meeting.tencent.com/crm/KwLGYML244