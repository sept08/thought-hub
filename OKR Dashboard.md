# OKR 看板

## 🎯 当前目标

```dataview
TABLE
  period as "周期",
  choice(status = "active", "🟢 进行中", choice(status = "completed", "✅ 已完成", "⏸️ 暂停")) as "状态",
  file.link as "目标"
FROM "1-Projects"
WHERE type = "okr"
SORT period DESC
```

## 📊 本周期进度汇总

```dataview
TABLE
  kr1_progress as "KR1",
  kr2_progress as "KR2",
  kr3_progress as "KR3"
FROM "1-Projects"
WHERE type = "okr" AND status = "active"
```

## ✅ 本周待办

```tasks
not done
due before today + 7 days
short mode
```

## ⏰ 今日任务

```tasks
not done
due on today
short mode
```

## 📥 收件箱待整理

```dataview
LIST
FROM "0-Inbox"
SORT file.ctime DESC
LIMIT 10
```

## 🔥 高优先级项目

```dataview
TABLE
  status as "状态",
  created as "创建时间"
FROM "1-Projects"
WHERE type = "project" AND status = "active"
SORT file.ctime DESC
```