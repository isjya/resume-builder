# Typst 简历模板注意事项

本文档记录 Typst 简历模板的实际使用经验和常见问题，帮助你在生成简历时避免这些坑。

## 一、符号转义问题（最重要）

Typst 会将某些符号解析为代码语法，导致编译失败。**使用反斜杠转义**：

### 1.1 C++ 转义写法

- ❌ 错误：`C++`（`++` 被解析为递增运算符）
- ✅ 正确：`C\+\+`

**示例**：
```typst
- *编程语言*: C\+\+ 精通, Python 熟悉
```

### 1.2 C# 转义写法

- ❌ 错误：`C#`（`#` 被解析为特殊字符）
- ✅ 正确：`C\#`

**示例**：
```typst
- *编程语言*: C\+\+ 精通, C\# 熟练, Python 熟悉
```

### 1.3 括号使用

Typst 在 list item 中对括号有一定兼容性，但建议谨慎使用：

- ❌ 错误：`C\+\+ (精通)` 或 `C\+\+（精通）`
- ✅ 正确：`C\+\+ 精通`（用空格代替括号）

### 1.4 避免在 list item 末尾使用逗号后跟空格

如果 list item 中某项以 `,` 结尾且后面有空格，Typst 可能误解析。

- ❌ 错误：`精通C\+\+和C\#, 具备Unity能力`
- ✅ 正确：`精通C\+\+和C\# 具备Unity能力` 或 `精通C\+\+及C\# 具备Unity能力`

## 二、中文标点问题

### 2.1 全角括号在某些场景下有问题

虽然模板示例使用了全角括号 `（）`，但在 **list item 中**，全角括号会导致解析错误。

**解决方案**：在 list item 中使用逗号或空格代替括号。

### 2.2 建议统一使用半角标点

为避免歧义，建议：
- 括号改用逗号：`C++（精通）` → `C++ 精通`
- 顿号改用逗号：`引擎性能优化、渲染管线` → `引擎性能优化, 渲染管线`

## 三、Typst 模板函数参考

### 3.1 必须的模板结构

```typst
#import "@preview/resume-ng:1.0.0": *

#show: project.with(
  title: "姓名",
  author: (name: "姓名"),
  contacts: (
    "电话",
    link("mailto:邮箱", "邮箱"),
  )
)
```

### 3.2 简历模块函数

```typst
#resume-section("标题")

#resume-education(
  university: "学校",
  degree: "学位",
  school: "专业",
  start: "2020-09",
  end: "2023-07"
)[
  可选的补充描述文字
]

#resume-work(
  company: "公司",
  duty: "职位",
  start: "2023-07",
  end: "至今"
)[
  - 工作内容列表
]

#resume-project(
  title: "项目名",
  duty: "角色",
  start: "2023-07"
)[
  - 项目内容列表
]
```

### 3.3 内容块规则

- `#resume-education`、`#resume-work`、`#resume-project` 后的 `[...]` 内容块中可以自由使用中文标点和格式
- list item `-` 开头的行中，避免使用括号和特殊符号

## 四、常见错误排查

### 4.1 错误信息：`expected expression`

通常是因为 `++`、`#`、`,` 等符号在 list item 中被误解析。检查并替换这些符号。

### 4.2 错误信息：`the character is not valid in code`

通常是文件编码问题或存在特殊字符。确保文件为 UTF-8 编码。

### 4.3 错误信息：`cannot access fields on type array`

`project.with()` 中的 `author` 参数格式错误，应该是 `(name: "姓名")` 格式。

### 4.4 错误信息：`failed to write PDF file`

Windows 下 PDF 文件被占用。先关闭 PDF 阅读器，或使用新的文件名。

## 五、文件编码注意事项

生成 `.typ` 文件时，确保：
- 使用纯 UTF-8 编码（无 BOM）
- 不要使用 Windows 记事本编辑，可能添加 BOM 导致问题
- 建议使用 Python 写入文件确保编码正确

## 六、编译命令

```bash
# 使用脚本编译
python scripts/make_resume.py resume.typ

# 直接编译
assets/bin/typst.exe compile resume.typ resume.pdf
```

## 七、快速检查清单

生成简历前，逐项检查：

- [ ] `C++` 改为 `C\+\+`
- [ ] `C#` 改为 `C\#`
- [ ] list item 中的括号改为逗号或空格
- [ ] 文件保存为 UTF-8 无 BOM 编码
- [ ] `author` 参数格式为 `(name: "姓名")`
- [ ] PDF 文件未被其他程序占用

---

**核心原则**：在 list item（`-` 开头的行）中，使用 `\+` 和 `\#` 转义特殊符号。
