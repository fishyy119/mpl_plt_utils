# pyright: reportUnknownMemberType=false
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.axes import Axes
from matplotlib.artist import Artist

from typing import List, Tuple


# * 在最一开始设置这个，保证后面的字体全部生效
plt.rcParams["font.family"] = ["Times New Roman", "SimSun"]
plt.rcParams.update({"axes.labelsize": 10.5, "xtick.labelsize": 10.5, "ytick.labelsize": 10.5})


def ax_remove_axis(ax: Axes) -> None:
    # 对于绘制地图，去除坐标轴，添加黑色边框
    ax.axis("off")
    ax_add_black_border(ax, (0, 501), (0, 501))


def ax_set_square_lim(
    ax: Axes,
    xlim: Tuple[float, float] | None = None,
    ylim: Tuple[float, float] | None = None,
    border: bool = False,
):
    if xlim is None or ylim is None:
        ax.margins(x=0.05, y=0.05)
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
    x0, x1 = xlim
    y0, y1 = ylim
    w_x = x1 - x0
    w_y = y1 - y0
    if w_x > w_y:
        ylim = (y0 - (w_x - w_y) / 2, y1 + (w_x - w_y) / 2)
    else:
        xlim = (x0 - (w_y - w_x) / 2, x1 + (w_y - w_x) / 2)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_aspect("equal")
    if border:
        ax_add_black_border(ax, xlim, ylim)


def ax_add_black_border(ax: Axes, xlim: Tuple[float, float], ylim: Tuple[float, float]) -> None:
    rect = patches.Rectangle(
        (xlim[0], ylim[0]),
        xlim[1] - xlim[0],
        ylim[1] - ylim[0],
        linewidth=2,
        edgecolor="black",
        facecolor="none",
        transform=ax.transData,
    )
    ax.add_patch(rect)


def ax_add_legend(
    ax: Axes,
    legend_handles: Artist | None = None,
    alpha: float = 1.0,
) -> None:
    # 自动设置图例样式
    # legend = ax.legend(handles=legend_handles, loc="upper right", title="")
    legend = ax.legend(
        handles=legend_handles,
        fontsize=10.5,
        prop={"family": ["SimSun", "Times New Roman"]},  # 中文宋体，西文 Times New Roman
        loc="best",
    )
    legend.get_frame().set_facecolor("white")
    legend.get_frame().set_alpha(alpha)
    legend.get_frame().set_edgecolor("black")


def axes_add_abc(
    axes: List[Axes],
    y_offset: float = -0.05,
) -> None:
    # 添加图注 (a), (b)
    for i, ax in enumerate(axes):
        ax.text(
            0.5,
            y_offset,
            f"({chr(97 + i)})",
            transform=ax.transAxes,
            fontsize=10.5,  # 五号字体，用于图注
            fontname="Times New Roman",
            ha="center",
            va="top",
        )


def plt_tight_show(factor: float = 1) -> None:
    # A4 尺寸
    left_margin_mm = 30
    right_margin_mm = 26
    usable_width_cm = (210 - left_margin_mm - right_margin_mm) / 10  # mm → cm
    # 转为英寸
    fig_width_in = usable_width_cm / 2.54

    for i in plt.get_fignums():
        fig = plt.figure(i)
        fig.tight_layout()
        _, fig_height_in = fig.get_size_inches()
        fig.set_size_inches(fig_width_in * factor, fig_height_in)
        # 限制宽度，便于预览论文上的字体大小效果

        plt.tight_layout()

    plt.show()


def plt_flat_axes(axes: List[List[Axes]]) -> List[Axes]:
    # 将二维数组展平为一维列表
    flat_axes = [ax for axs in axes for ax in axs]
    return flat_axes
