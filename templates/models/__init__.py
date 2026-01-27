"""
MCM/ICM 数学建模模板库
======================

包含 20+ 常用模型的 Python 实现模板，覆盖 A-F 全部题型。
所有模板包含详细中文注释，可直接复制到项目中使用。

Quick Start
-----------
>>> from templates.models import evaluation
>>> weights = evaluation.ahp_weights(comparison_matrix)
>>> scores = evaluation.topsis_score(data, weights, criteria_types)

Available Modules
-----------------
evaluation : 评价模型 (E/F 类必备)
    - ahp_weights() : 层次分析法权重计算
    - ewm_weights() : 熵权法权重计算
    - ahp_ewm_combined() : 主客观组合赋权
    - topsis_score() : TOPSIS 多准则排序
    - fuzzy_comprehensive() : 模糊综合评价

optimization : 优化模型 (B/D/E 类核心)
    - linear_programming() : 线性规划模板
    - nsga2_optimize() : NSGA-II 多目标优化
    - genetic_algorithm() : 遗传算法模板
    - simulated_annealing() : 模拟退火

time_series : 时间序列 (A/C 类预测)
    - arima_forecast() : ARIMA 时序预测
    - prophet_forecast() : Prophet 预测模板
    - grey_gm11() : 灰色预测 GM(1,1)
    - decompose_series() : 时序分解

dynamics : 动力学模型 (A/F 类)
    - lotka_volterra() : Lotka-Volterra 竞争/捕食模型
    - logistic_growth() : Logistic 增长模型
    - seir_model() : SEIR 传播模型
    - solve_ode() : 通用 ODE 求解器

monte_carlo : 蒙特卡洛模拟 (不确定性分析)
    - monte_carlo_simulate() : 蒙特卡洛模拟
    - bootstrap_ci() : Bootstrap 置信区间
    - latin_hypercube() : 拉丁超立方采样
    - sensitivity_analysis() : 敏感性分析

machine_learning : 机器学习 (C 类数据分析)
    - random_forest_model() : 随机森林分类/回归
    - xgboost_model() : XGBoost 模板
    - kmeans_clustering() : K-Means 聚类
    - feature_importance() : 特征重要性分析

network_analysis : 网络分析 (D 类)
    - pagerank() : PageRank 节点重要性
    - centrality_analysis() : 中心性分析
    - community_detection() : 社区发现
    - network_flow() : 网络流模型

Problem Type Mapping
--------------------
| 模块 | 适用题型 |
|------|----------|
| evaluation | E, F |
| optimization | B, D, E |
| time_series | A, C |
| dynamics | A, F |
| monte_carlo | All |
| machine_learning | C |
| network_analysis | D |

Version
-------
v1.3.0 - January 2026
"""

__version__ = "1.3.0"

# 延迟导入以避免依赖问题
def _lazy_import(module_name):
    """延迟导入模块"""
    import importlib
    return importlib.import_module(f".{module_name}", package=__name__)

# 公开 API
__all__ = [
    "__version__",
    "evaluation",
    "optimization", 
    "time_series",
    "dynamics",
    "monte_carlo",
    "machine_learning",
    "network_analysis",
]

# 延迟加载模块
def __getattr__(name):
    if name in __all__ and name != "__version__":
        return _lazy_import(name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
