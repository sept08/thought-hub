# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a PARA-based personal knowledge management system using Obsidian. The purpose is to digitize personal knowledge and enable continuous self-iteration.

## PARA Structure

```
0-Inbox/      # Quick capture - unsorted notes
1-Projects/   # Active projects with deadlines and OKR tracking
2-Areas/      # Areas of responsibility (ongoing, no deadline)
3-Resources/  # Reference materials (课程笔记, 读书笔记, 人物)
4-Archives/   # Completed or inactive items
Templates/    # Note templates with YAML frontmatter
```

**PARA Rule**: Projects have deadlines; Areas do not. Resources are reference; Archives are done.

## Obsidian Plugins

Three core plugins are used:

### Dataview
Dynamically lists related content. Area files use this pattern:
```dataview
LIST
FROM "1-Projects"
WHERE contains(area, this.file.name)
```

### Tasks
Task management with emoji syntax:
- `📅 YYYY-MM-DD` for due date
- `✅ YYYY-MM-DD` for done date
- `#tag` for labels

Project files include a Tasks query block:
```tasks
not done
path includes <project-name>
short mode
```

### Templater
Templates in `Templates/` folder. New notes should use appropriate template.

## YAML Frontmatter Conventions

All notes use frontmatter for metadata:

**Project**: `type: project`, `status: active/completed`, `area: <area-name>`, `created`, `deadline`
**Area**: `type: area`
**Course**: `type: course`, `status: learning/finished`, `instructor`, `platform`, `area`, `tags`
**Book**: Similar to course with `author` instead of `instructor`

The `area` field links content to Areas via Dataview queries.

## Note Patterns

### Area Files
Each Area (`2-Areas/*.md`) contains Dataview queries that auto-list:
- Related projects
- Related course notes
- Related book notes

### Project Files
Projects track progress with checkboxes and include a Tasks query for unfinished tasks.

### Course/Book Notes
Structure includes: 基本信息, 核心观点, 精彩摘录, 我的思考, 行动项, 关联

## Claude-Specific

### Skills Folder
`.claude/skills/` contains custom skills. Current skill: `dedao-comment` for 得到课程评论.

### Memory System
Memory files stored at `C:\Users\ZhuanZ\.claude\projects\D--Projects-mine-thought-hub\memory\` (external to repo). Memory types: user, feedback, project, reference.

### Git Workflow
Direct commits to `main` branch. No PR workflow unless explicitly requested.