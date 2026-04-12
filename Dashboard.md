# Dashboard

## 📂 当前项目

```dataview
TABLE
  choice(status = "active", "🟢 进行中", choice(status = "completed", "✅ 已完成", "⏸️ 暂停")) as "状态",
  area as "领域",
  deadline as "截止"
FROM "1-Projects"
WHERE type = "project"
SORT deadline DESC
```

## ✅ 今日任务

```tasks
not done
due on today
short mode
```

## 📅 本周待办

```tasks
not done
due before today + 7 days
short mode
```

## 📥 收件箱

```dataview
LIST
FROM "0-Inbox"
SORT file.ctime DESC
LIMIT 10
```

## 🎯 领域重点

```dataview
TABLE
  file.link as "领域"
FROM "2-Areas"
SORT file.name
```