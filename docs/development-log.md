# MCM-Analysis Skill 开发日志

> 开发日期：2026年1月24日  
> 开发者：chenqiyukkk + Claude (Antigravity/OpenCode)  
> 目的：为美赛新手团队打造 O 奖级论文辅助工具

---

## 一、项目背景

### 1.1 需求来源
用户即将参加 MCM/ICM（美国大学生数学建模竞赛），团队全是新手。希望开发一个 OpenCode Skill，能够：
- 自动分析美赛题目
- 给出做题思路和建模方向
- 辅助论文写作，产出评委友好的高质量论文

### 1.2 目标用户
- **建模手**：需要问题分析、模型推荐
- **编程手**：需要代码模板、实现指导
- **写作手**：需要论文结构、写作风格指南

### 1.3 核心价值主张
> "帮助新手团队产出 O 奖级别的论文"

---

## 二、开发过程

### 2.1 资料准备阶段

#### 使用 Gemini 3 Flash 预处理 PDF
由于直接用 Claude 解析大量 PDF 会消耗过多上下文和 Token，采用了**预处理 Pipeline**策略：

```
原始 PDF (80+篇) → Gemini 3 Flash 解析 → 结构化 Markdown → Claude 读取精华
                    (批量处理，低成本)      (标准格式)        (低 token 消耗)
```

#### 解析 Prompt 模板
为 Gemini 设计了两套标准化 Prompt：
1. **O奖论文解析模板**：提取模型、方法、优缺点、关键词
2. **真题解析模板**：提取背景、问题分解、隐含要求、推荐建模方向

#### 最终数据规模
- **年份覆盖**：2020-2024（5年）
- **题型覆盖**：A/B/C/D/E/F（6种）
- **解析文件**：60个 Markdown 文件
  - `D:\ICM\解析结果\papers\` - 30篇 O奖论文解析
  - `D:\ICM\解析结果\problems\` - 30道真题解析

### 2.2 在线调研阶段

#### COMAP 官网调研
从 `https://www.comap.com/contests/mcm-icm` 和 `https://www.contest.comap.com/undergraduate/contests/mcm/instructions.php` 获取：
- 官方评判标准（6个等级定义）
- Summary Sheet 的重要性
- 25页限制规则
- AI 使用声明要求

#### 经验分享调研
通过 Task 子代理搜索 COMAP Blog、Wikipedia 等来源，汇总：
- O奖论文的共同特征
- 常见错误和避坑指南
- 团队协作建议

### 2.3 深度分析阶段

#### 6篇 2024 O奖论文原文分析
选取每题型1篇代表性论文进行 PDF 原文深度分析：
```
D:\ICM\2024年美赛O奖论文\2024年美赛A题O奖论文\2425397.pdf
D:\ICM\2024年美赛O奖论文\2024年美赛B题O奖论文\2419984.pdf
D:\ICM\2024年美赛O奖论文\2024年美赛C题O奖论文\2425454.pdf
D:\ICM\2024年美赛O奖论文\2024年美赛D题O奖论文\2417831.pdf
D:\ICM\2024年美赛O奖论文\2024年美赛E题O奖论文\2401102.pdf
D:\ICM\2024年美赛O奖论文\2024年美赛F题O奖论文\2413565.pdf
```

提取内容：
- 论文结构和页面分配
- 句式模式和学术表达
- 人性化写作特征（用于 Anti-AI）

### 2.4 并行开发阶段

采用 **3个子代理 + 主对话** 并行工作模式：

| Agent | 任务 | 产出 |
|-------|------|------|
| Agent 1 | PDF 写作风格分析 | `paper-structure.md`, `writing-guide.md`, `anti-ai-patterns.md` |
| Agent 2 | 汇总60个解析文件 | `models-library.md`, `problem-types.md` |
| Agent 3 | 开发辅助脚本 | 4个 Python 脚本 |
| 主对话 | 编写核心文件 | `SKILL.md`, `judging-criteria.md` |

---

## 三、核心设计决策

### 3.1 语言策略

| 场景 | 语言 | 原因 |
|------|------|------|
| Skill 文件本身 | 英文 | 国际兼容性，符合 OpenCode 规范 |
| 生成的论文内容 | **中文** | 让团队能看懂、能修改，翻译另行处理 |
| 技术术语 | 中英混合 | 如：灵敏度分析 (Sensitivity Analysis) |

### 3.2 反 AI 策略 (Anti-AI)

**核心理念**：让 AI 辅助的内容更接近人类自然写作风格，而非"欺骗"评委。

#### 需要避免的 AI 典型模式
| AI 痕迹 | 人性化替代 |
|--------|-----------|
| "It is important to note that..." | 直接陈述 |
| "Furthermore, moreover, additionally" (过度使用) | 减少或省略连接词 |
| 完美的三段式结构 | 自然段落变化 |
| 所有句子长度相似 | 长短句交替 |
| 过于完美的语法 | 允许轻微口语化 |

#### 推荐的人性化技巧
1. 使用具体数字："23.7% improvement" 而非 "significant improvement"
2. 展示思考过程："We initially considered X, but found Y more suitable..."
3. 承认局限性："Due to time constraints..."
4. 句子长度变化：20% 短句 + 60% 中句 + 20% 长句

### 3.3 数据驱动设计

所有参考资料都基于**真实 O奖论文**提取，而非凭空生成：
- `models-library.md`：从60篇论文中提取的50+模型
- `problem-types.md`：5年30道题的规律总结
- `paper-structure.md`：6篇2024论文的结构分析
- `anti-ai-patterns.md`：实际论文中的人性化写作模式

### 3.4 工具选择

| 组件 | 选择 | 原因 |
|------|------|------|
| 论文模板 | LaTeX | 美赛标准，专业排版 |
| 代码语言 | Python | 数据处理、ML 生态最强 |
| 脚本设计 | 独立可运行 | 新手友好，最小依赖 |

---

## 四、最终架构

```
mcm-analysis/
├── SKILL.md                          # 主指令文件
│
├── references/
│   ├── models-library.md             # 50+ 模型分类库
│   ├── problem-types.md              # 6种题型规律
│   ├── paper-structure.md            # O奖论文结构模板
│   ├── writing-guide.md              # 学术写作指南
│   ├── anti-ai-patterns.md           # AI痕迹规避指南
│   └── judging-criteria.md           # COMAP 评判标准
│
├── scripts/
│   ├── init_project.py               # 项目初始化（含 LaTeX 模板）
│   ├── generate_outline.py           # 论文大纲生成
│   ├── check_format.py               # 格式合规检查
│   └── humanize_text.py              # 文本人性化处理
│
├── docs/
│   └── development-log.md            # 本文档
│
├── README.md                         # 项目说明
└── .gitignore                        # Git 忽略配置
```

---

## 五、使用指南

### 5.1 触发 Skill
在 OpenCode 对话中提到以下关键词时自动触发：
- MCM, ICM, 美赛, 数学建模竞赛, COMAP

### 5.2 典型工作流

```
1. 初始化项目
   python scripts/init_project.py --problem C --year 2026 --team "YourTeam"

2. 分析题目
   用户: 这是2026年C题，帮我分析 [题目内容]
   AI: [用中文输出分析结果]

3. 建模指导
   用户: C题应该用什么模型？
   AI: [推荐模型 + Python代码框架]

4. 写作辅助
   用户: 帮我写 Introduction
   AI: [用中文生成草稿，符合O奖结构]

5. 格式检查
   python scripts/check_format.py paper.pdf

6. 人性化处理
   python scripts/humanize_text.py --input draft.md --output humanized.md
```

---

## 六、扩展指南

### 6.1 添加新年份数据

1. 获取新年份的 O奖论文和真题 PDF
2. 使用 Gemini 按照原有 Prompt 模板解析
3. 将解析结果放入 `D:\ICM\解析结果\` 对应目录
4. 更新 `models-library.md` 和 `problem-types.md`

### 6.2 添加新模型

编辑 `references/models-library.md`，按现有格式添加：
```markdown
### X.X 新模型名称
- **When to use**: ...
- **Problem types**: A, B, C
- **Example applications**: ...
- **Key considerations**: ...
```

### 6.3 添加新脚本

在 `scripts/` 目录下创建新 Python 文件，并在 `SKILL.md` 的 Quick Start 部分添加使用说明。

---

## 七、集成的 Skills

本 Skill 设计时参考并可与以下 Skills 协同：

| Skill | 用途 |
|-------|------|
| `pdf` | 读取题目 PDF、生成论文 |
| `research-lookup` | 实时搜索相关文献 |
| `scientific-writing` | 学术写作规范 |
| `scientific-visualization` | 专业图表生成 |
| `planning-with-files` | 任务规划和进度追踪 |

---

## 八、关键提醒

### 8.1 比赛规则
- **25页限制**：包括摘要、正文、参考文献、附录、代码
- **无身份信息**：论文中不能出现姓名、学校名
- **AI声明**：必须在正文引用 + 参考文献 + 附加 "Report on Use of AI"

### 8.2 评判重点
> "The judges place considerable weight on the summary, and winning papers are often distinguished from other papers based on the quality of the summary."

**Summary 是最重要的！最后写，但要写最好。**

---

## 九、致谢

感谢以下资源的支持：
- COMAP 官方网站和比赛指南
- 历年 O奖论文作者们的优秀工作
- Gemini 3 Flash 在 PDF 预处理中的贡献
- OpenCode 和 Claude Scientific Skills 生态

---

# 更新日志：2026年1月25日 - 可视化能力增强

> 开发者：Antigravity (Claude Opus/Sonnet) + 子代理集群
> 目标：提供 O 奖级的 Python 绘图模板和可视化指南

## 1. 深度实证分析
启动了 6 个并行子代理，对 **2020-2024 年 30 篇 O 奖论文**（A-F 全题型）进行了图表分析。
- 产出分析报告：`references/analysis_data/type_[A-F]_analysis.md`
- 汇总发现：`references/analysis_data/visualization_findings.md`

## 2. 核心成果

### 2.1 样式标准化 (`templates/visualization/`)
- 创建 `mcm_style.mplstyle`: 集成了 Okabe-Ito 色盲友好配色、出版级 DPI、Arial 字体。

### 2.2 核心绘图模板
根据实证分析，开发了 5 个核心 Python 模板：
1. **`phase_portrait.py`**: A 类专用。支持流场、零一片线、轨迹模拟（微分方程稳定性分析）。
2. **`time_series.py`**: A/C 类专用。支持置信区间阴影、双 Y 轴、预测对比。
3. **`network_graph.py`**: B/D/F 类专用。支持网络拓扑、树形结构、Spring 布局。
4. **`heatmap.py`**: C/E 类专用。支持相关性矩阵、混淆矩阵、空间热力图。
5. **`multi_panel.py`**: 通用型。自动化生成 (a)(b)(c)(d) 多子图布局。

### 2.3 可视化指南
- 新增 `references/visualization-guide.md`:
  - 提供了基于题型的图表选择表。
  - 总结了 O 奖图表的 "黄金法则"（如：必画模型示意图）。

## 3. 架构变更
- **文件结构更新**:
  ```
  mcm-analysis/
  ├── templates/
  │   └── visualization/        # [新增] 可视化引擎
  └── references/
      └── analysis_data/        # [新增] 原始分析数据归档
  ```
- **流程集成**: `SKILL.md` 新增 Phase 4 Visualization 环节。

---

**祝美赛顺利，拿下 O 奖！** 🏆
