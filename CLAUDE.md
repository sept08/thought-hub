# CLAUDE.md

本文件为 Claude Code (claude.ai/code) 提供本仓库的使用指引。

## 仓库概览

这是一个基于 PARA 方法的个人知识管理系统，使用 Obsidian 进行管理。目的是将个人知识数字化，实现持续的自我迭代。

## PARA 结构

```
0-Inbox/      # 快速捕获 - 未分类笔记
1-Projects/   # 活跃项目，有截止日期和 OKR 跟踪
2-Areas/      # 责任领域（持续进行，无截止日期）
3-Resources/  # 参考资料（课程笔记, 读书笔记, 人物）
4-Archives/   # 已完成或不再活跃的内容
Templates/    # 包含 YAML frontmatter 的笔记模板
```

**PARA 规则**：项目有截止日期；领域没有。资源是参考资料；归档是已完成的内容。

## Obsidian 插件

使用三个核心插件：

### Dataview
动态列出相关内容。领域文件使用此模式：
```dataview
LIST
FROM "1-Projects"
WHERE contains(area, this.file.name)
```

### Tasks
任务管理使用 emoji 语法：
- `📅 YYYY-MM-DD` 表示截止日期
- `✅ YYYY-MM-DD` 表示完成日期
- `#tag` 用于标签

项目文件包含 Tasks 查询块：
```tasks
not done
path includes <project-name>
short mode
```

### Templater
模板存放在 `Templates/` 文件夹。新建笔记应使用对应模板。

## YAML Frontmatter 规范

所有笔记使用 frontmatter 记录元数据：

**项目**：`type: project`，`status: active/completed`，`area: <领域名>`，`created`，`deadline`
**领域**：`type: area`
**课程**：`type: course`，`status: learning/finished`，`instructor`，`platform`，`area`，`tags`
**书籍**：与课程类似，用 `author` 代替 `instructor`

`area` 字段通过 Dataview 查询将内容关联到领域。

## 笔记模式

### 领域文件
每个领域文件（`2-Areas/*.md`）包含 Dataview 查询，自动列出：
- 相关项目
- 相关课程笔记
- 相关读书笔记

### 项目文件
项目通过复选框跟踪进度，并包含未完成任务的 Tasks 查询。

### 课程/读书笔记

**文件位置**：`3-Resources/课程笔记/<课程名>.md` 或 `3-Resources/读书笔记/<书名>.md`

**笔记结构**：
1. YAML frontmatter（type: course/book, status, instructor/author, platform, area, tags）
2. `## 基本信息` — 表格形式记录元数据（主理人/作者、平台、更新频率、学习时间等）
3. `## 关联` — 相关领域、项目、课程/书籍
4. 分割线 `---`
5. `# 课程内容`（一级标题）— 下方按学习主题设二级标题（`## 主题名`），具体笔记内容由用户与 Claude 讨论后整理写入

**协作流程**：用户说"开始学习 XX"时，先在对应目录查找笔记文件；若不存在，询问用户是否需要创建。学习过程中，用户分享内容或观点，经讨论后由 Claude 整理成笔记写入对应主题的二级标题下。

## Claude 相关

### 技能文件夹
`.claude/skills/` 存放自定义技能。当前技能：`dedao-comment`，用于得到课程评论。

### 记忆系统
记忆文件存储于 `C:\Users\ZhuanZ\.claude\projects\D--Projects-mine-thought-hub\memory\`（仓库外部）。记忆类型：user, feedback, project, reference。

### Git 工作流
直接提交到 `main` 分支。除非明确要求，否则不使用 PR 流程。
