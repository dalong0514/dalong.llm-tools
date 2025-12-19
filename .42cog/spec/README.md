# 规约文档 (Spec)

规约文档是基于现实约束(Real)和认知模型(Cog)生成的具体实现规范。

## 目录结构

```
spec/
├── user/           # 用户角色规约
│   ├── user.spec.md      # 用户模拟使用
│   └── admin.spec.md     # 管理员功能
├── pm/             # 产品经理规约
│   ├── pr.spec.md        # 产品需求文档
│   └── userstory.spec.md # 用户故事
├── dev/            # 开发规约
│   ├── sys.spec.md       # 系统架构设计
│   ├── db.spec.md        # 数据库设计
│   ├── code.spec.md      # 实际编码
│   ├── qa.spec.md        # 质量保证
│   └── devops.spec.md    # 部署运维
└── design/         # 设计规约
    ├── ui.spec.md        # 交互设计
    └── graphic.spec.md   # 平面设计
```

## 11个核心技能

> **技能安装位置**: 所有技能安装在 `../.42plugin/42edu/` 目录下
>
> 例如：
> - 产品需求技能: `../.42plugin/42edu/pm-pr/`
> - 用户故事技能: `../.42plugin/42edu/pm-userstory/`
> - 系统架构技能: `../.42plugin/42edu/dev-sys/`

### 用户角色 (2个)
- **user**: 用户模拟使用 - 从用户视角描述产品使用流程
- **admin**: 管理员功能 - 定义后台管理功能需求

### 产品经理 (2个)
- **pr**: 产品需求文档 - 完整的PRD文档
- **userstory**: 用户故事 - 敏捷开发的用户故事

### 开发 (5个)
- **sys**: 系统架构设计 - 技术架构和系统设计
- **db**: 数据库设计 - 数据模型和表结构
- **code**: 实际编码 - 代码实现规范
- **qa**: 质量保证 - 测试策略和用例
- **devops**: 部署运维 - 部署流程和运维规范

### 设计 (2个)
- **ui**: 交互设计 - UI/UX设计规范
- **graphic**: 平面设计 - 视觉设计规范

## 使用流程

1. **定义现实约束** (.42cog/real/real.md)
2. **建立认知模型** (.42cog/cog/cog.md)
3. **生成规约文档** (使用.42plugin/42edu/下的技能)
4. **实现作品** (基于规约文档开发)

## 规约文档格式

所有规约文档使用 **Markdown + XML语义闭合标签** 格式：

```markdown
---
name: feature-name
description: Feature description
---

# 功能名称

<spec>
  <section name="概述">
    内容...
  </section>

  <section name="需求">
    内容...
  </section>
</spec>
```

## 注意事项

1. **引用约束**: 规约文档中要引用real.md中的约束
2. **保持一致**: 所有规约要与cog.md中的认知模型保持一致
3. **可执行性**: 规约要足够具体，AI能够直接生成代码
4. **可验证性**: 规约要包含验收标准，便于测试验证
