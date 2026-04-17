# Resume Builder

AI 简历生成工具。本项目参考/灵感来自 [typst-pdf-gen](https://github.com/OGoodness/typst-pdf-gen) 的 Typst 简历模板。根据你的个人经历和目标岗位 JD，生成符合招聘标准的专业简历，并导出 PDF。

**核心原则**：严格基于真实信息，不虚构、不夸大。

---

## 环境要求

- Python 3.10+
- Typst（首次使用自动安装）

---

## 安装

### 1. 安装依赖

```bash
python scripts/install_deps.py
```

这会将 Typst 编译器下载到 `assets/bin/`。

### 2. 验证

```bash
typst --version
```

---

## 使用方法

### Claude Code

```bash
claude
```

启动后对 Claude 说：

> "用 resume-builder 技能帮我生成简历"

Claude 会自动加载 SKILL.md 并引导你完成信息收集、简历生成和 PDF 导出。

### Cursor

在 Cursor 的 AI 面板或 Composer 中，引用 `SKILL.md` 文件即可触发技能。

或者直接告诉 Cursor：

> "根据 `SKILL.md`，帮我整理简历并生成 PDF"

### OpenCode

```bash
opencode
```

启动后加载技能：

> "加载 SKILL.md，然后帮我生成简历"

---

## 工作流程

1. **信息收集** — 提供个人背景、项目经历、目标岗位 JD
2. **简历生成** — AI 使用 STAR 法则优化表述，匹配 JD 关键词
3. **PDF 导出** — Typst 渲染生成 PDF 文件

---

## 目录结构

```
resume-builder/
├── SKILL.md                      # 技能定义（Claude Code / Cursor / OpenCode 加载此文件）
├── CLAUDE.md                      # 项目说明
├── README.md                      # 本文件
├── scripts/
│   ├── install_deps.py            # 安装 Typst 编译器
│   └── make_resume.py             # 将 .typ 文件编译为 PDF
├── assets/
│   ├── bin/                       # Typst 编译器（安装后生成）
│   ├── typst-pdf-gen/             # Typst 简历模板（git submodule）
│   └── reference/
│       └── resume.typ             # 简历模板示例
└── references/                    # 岗位专属简历指南
    ├── unreal-engine-engineer.md
    ├── quant-finance-pm.md
    └── recommendation-system-engineer.md
```

---

## 常见问题

**Q: 报错 "typst: command not found"**

运行 `python scripts/install_deps.py` 安装 Typst 编译器。

**Q: 如何指定目标岗位？**

在描述经历时说明你想要的岗位名称，如"虚幻游戏引擎工程师"或"推荐系统工程师"，AI 会自动加载对应的岗位专属简历指南。

**Q: 支持哪些 IDE？**

支持 Claude Code、Cursor、OpenCode，以及任何引用 `SKILL.md` 的 AI 助手。
