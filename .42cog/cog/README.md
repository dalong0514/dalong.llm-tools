---
name: project-cog
description: Cognitive model defining core entities and relationships
---

# 认知模型 (Cog)

> 认知模型基于人心系统模型（感性-智商-理商），核心框架是：**智能体 + 信息 + 上下文**
>
> **核心原则**：
> - 每个实体需要：**唯一编码**（如何被识别）、**分类方式**（人类明确，避免AI乱分类）
> - 不是让你掌握很多先验知识，而是让AI意识到你是什么样的人
> - 使用XML语义闭合标签

## 推荐：简明写法

**大多数项目推荐使用这种简洁的写法**，直接描述核心实体和关系：

<cog>
本系统包括以下关键实体：
- [实体1名称]：[简要说明]
  - [子类型1]：[说明]
  - [子类型2]：[说明]
- [实体2名称]：[简要说明]
- [实体3名称]：[简要说明]
</cog>

<[实体1名称]>
- 唯一编码：[如何唯一识别，例如：UUID、slug、日期编码等]
- 常见分类：[分类1]；[分类2]；[分类3]
</[实体1名称]>

<[实体2名称]>
- 唯一编码：[如何唯一识别]
- 常见分类：[分类1]；[分类2]
</[实体2名称]>

<rel>
- [实体1]-[实体2]：[关系类型，如：一对多、多对多]（[关系说明]）
- [实体2]-[实体3]：[关系类型]（[关系说明]）
</rel>

### 简明写法示例：咨询平台

<cog>
本系统包括以下关键实体：
- user：用户
  - counselor：咨询师，一种特殊的user
  - admin：管理员，一种特殊的user
- content：内容
</cog>

<user>
- 唯一编码：按照注册时间次序生成的UUID号
- 常见分类：游客；注册用户；来访者（短程、长程）
</user>

<counselor>
- 唯一编码：每个咨询师有个独立的slug，例如lintong
- 常见分类：咨询师（实习咨询师、助理咨询师、正式咨询师、资深咨询师）；咨询助理（配合咨询师接待来访者，但没有一些保密权限）
</counselor>

<content>
- 唯一编码：按照文章的日期编码，例如20251204
- 常见分类：咨询师专栏；东木动态
</content>

<rel>
- user-content：一对多（一个用户可创建多个内容）
- user-user：多对多（咨询关系、督导关系）
</rel>

---

## 可选：详细写法

**仅在需要更详细的属性定义和复杂关系时使用**：

### 核心实体

<entities>

<entity id="entity-001" type="[类型]">
  <name>[实体名称]</name>
  <description>[实体描述]</description>
  <attributes>
    <attribute name="[属性名]" type="[类型]">[描述]</attribute>
    <attribute name="[属性名]" type="[类型]">[描述]</attribute>
  </attributes>
  <identification>[如何唯一识别这个实体]</identification>
  <classification>[如何分类这个实体]</classification>
</entity>

<entity id="entity-002" type="[类型]">
  <name>[实体名称]</name>
  <description>[实体描述]</description>
  <attributes>
    <attribute name="[属性名]" type="[类型]">[描述]</attribute>
    <attribute name="[属性名]" type="[类型]">[描述]</attribute>
  </attributes>
  <identification>[如何唯一识别这个实体]</identification>
  <classification>[如何分类这个实体]</classification>
</entity>

</entities>

### 实体关系

<relationships>

<relationship id="rel-001" type="[关系类型]">
  <from>entity-001</from>
  <to>entity-002</to>
  <description>[关系描述]</description>
  <cardinality>[1:1 / 1:N / N:M]</cardinality>
</relationship>

<relationship id="rel-002" type="[关系类型]">
  <from>entity-002</from>
  <to>entity-003</to>
  <description>[关系描述]</description>
  <cardinality>[1:1 / 1:N / N:M]</cardinality>
</relationship>

</relationships>

### 上下文信息

<context>

#### 业务上下文
[描述项目的业务背景和领域知识]

#### 用户上下文
[描述目标用户的特征和使用场景]

#### 技术上下文
[描述技术选型和架构决策的背景]

</context>

## 示例：电商平台

<entities>

<entity id="user" type="actor">
  <name>用户</name>
  <description>在平台上购物的消费者</description>
  <attributes>
    <attribute name="userId" type="string">用户唯一标识</attribute>
    <attribute name="email" type="string">登录邮箱</attribute>
    <attribute name="role" type="enum">用户角色：customer/admin</attribute>
  </attributes>
  <identification>通过userId或email唯一识别</identification>
  <classification>按role分类：普通用户、管理员</classification>
</entity>

<entity id="product" type="resource">
  <name>商品</name>
  <description>平台上销售的商品</description>
  <attributes>
    <attribute name="productId" type="string">商品唯一标识</attribute>
    <attribute name="name" type="string">商品名称</attribute>
    <attribute name="price" type="number">商品价格</attribute>
    <attribute name="stock" type="number">库存数量</attribute>
  </attributes>
  <identification>通过productId唯一识别</identification>
  <classification>按类目分类：电子产品、服装、食品等</classification>
</entity>

<entity id="order" type="transaction">
  <name>订单</name>
  <description>用户的购买记录</description>
  <attributes>
    <attribute name="orderId" type="string">订单唯一标识</attribute>
    <attribute name="userId" type="string">下单用户</attribute>
    <attribute name="totalAmount" type="number">订单总金额</attribute>
    <attribute name="status" type="enum">订单状态</attribute>
  </attributes>
  <identification>通过orderId唯一识别</identification>
  <classification>按status分类：待支付、已支付、已发货、已完成、已取消</classification>
</entity>

</entities>

<relationships>

<relationship id="user-order" type="creates">
  <from>user</from>
  <to>order</to>
  <description>用户创建订单</description>
  <cardinality>1:N</cardinality>
</relationship>

<relationship id="order-product" type="contains">
  <from>order</from>
  <to>product</to>
  <description>订单包含商品</description>
  <cardinality>N:M</cardinality>
</relationship>

</relationships>

## 注意事项

1. **实体完整性**：每个核心实体都要定义清楚
2. **关系明确性**：实体间的关系要明确基数
3. **分类清晰**：分类方式要让AI能够理解
4. **唯一标识**：每个实体要有明确的识别方式
5. **上下文丰富**：提供足够的背景信息帮助AI理解
