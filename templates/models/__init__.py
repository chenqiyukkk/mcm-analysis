"""
MCM/ICM 数学建模模板库
======================

模型实现模块（开发中）
当前版本仅包含框架，具体模型实现将在后续版本中添加。

Planned Modules
---------------
evaluation : 评价模型 (E/F 类必备)
    - ahp_weights() : 层次分析法权重计算
    - ewm_weights() : 熵权法权重计算
    - topsis_score() : TOPSIS 多准则排序

optimization : 优化模型 (B/D/E 类核心)
    - linear_programming() : 线性规划模板
    - nsga2_optimize() : NSGA-II 多目标优化

time_series : 时间序列 (A/C 类预测)
    - arima_forecast() : ARIMA 时序预测
    - grey_gm11() : 灰色预测 GM(1,1)

dynamics : 动力学模型 (A/F 类)
    - lotka_volterra() : Lotka-Volterra 模型
    - seir_model() : SEIR 传播模型

monte_carlo : 蒙特卡洛模拟
    - monte_carlo_simulate() : 蒙特卡洛模拟
    - sensitivity_analysis() : 敏感性分析

machine_learning : 机器学习 (C 类)
    - random_forest_model() : 随机森林
    - kmeans_clustering() : K-Means 聚类

network_analysis : 网络分析 (D 类)
    - pagerank() : PageRank 节点重要性
    - community_detection() : 社区发现

Version
-------
v1.2.2 - January 2026
"""

__version__ = "1.2.2"

# 当前仅导出版本号
__all__ = ["__version__"]

# TODO: 在 v1.3.0 中实现具体模型模块
# 模块列表（待实现）:
# - evaluation
# - optimization
# - time_series
# - dynamics
# - monte_carlo
# - machine_learning
# - network_analysis
