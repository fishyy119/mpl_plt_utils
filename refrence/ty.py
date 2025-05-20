from plot_utils import *


# 定义横轴 R（从 0 到 10 米）
R = np.linspace(0, 1, 500)  # 从 0.01 开始以避免对数或零的问题

# 定义两个函数
t1 = 6e-4 * R**1.76
t2 = R / 1900

# 找到交点
from scipy.optimize import fsolve


def equation(r):
    return 6e-4 * r**1.76 - r / 1900


r_intersect = fsolve(equation, 1)[0]
t_intersect = r_intersect / 1900

# 绘图
fig, ax = plt.subplots()
ax.plot(R, t1, label=r"$t = 6\times10^{-4} \cdot R^{1.76}$")
ax.plot(R, t2, label=r"$t =  R / 1900$", linestyle="--")

# 标注交点
ax.plot(r_intersect, t_intersect, "ro")  # 红点
ax.annotate(
    f"({r_intersect:.2f}, {t_intersect:.2e})",
    xy=(r_intersect, t_intersect),
    xytext=(r_intersect - 0.43, t_intersect),
    arrowprops=dict(arrowstyle="->"),
)

# # 虚线延伸
# plt.axhline(y=t_intersect, xmin=0, xmax=r_intersect / 10, color="gray", linestyle=":")
# plt.axvline(x=r_intersect, ymin=0, ymax=t_intersect / plt.ylim()[1], color="gray", linestyle=":")

# 设置纵轴为科学计数法（仅顶部标注倍率）
ax.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
ax.yaxis.get_offset_text().set_position((0, 1.02))  # 调整偏移文字位置
ax.yaxis.get_offset_text().set_fontsize(10.5)

# 图例与标签
ax.set_xlabel("R (m)")
ax.set_ylabel("t (s)")
ax.legend()
ax.grid(True)

plt_tight_show()
