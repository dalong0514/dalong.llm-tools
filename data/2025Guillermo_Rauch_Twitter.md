# Guillermo Rauch Twitter 2025

本文件包含Guillermo Rauch在2025年的所有推文。

总计推文数量: 612


### 600

作者: @Guillermo-Rauch
时间: 2025-10-18
链接: https://x.com/rauchg/status/1979352896857870448
互动: Likes: 786; Retweets: 54; Replies: 28; Quotes: 5; Views: 47,368; Bookmarks: 648; isReply: 0

▲ ~/ 𝚗𝚙𝚡 𝚌𝚛𝚎𝚊𝚝𝚎-𝚡𝚖𝚌𝚙-𝚊𝚙𝚙  
https://t.co/mrgKtauOSd: easiest way to deploy an MCP server https://t.co/FpfnhdHKzk

▲ ~/ 𝚗𝚙𝚡 𝚌𝚛𝚎𝚊𝚝𝚎-𝚡𝚖𝚌𝚙-𝚊𝚙𝚙
链接 https://t.co/mrgKtauOSd 展示了：部署 MCP（Model Context Protocol）服务器的最简单方法 https://t.co/FpfnhdHKzk

### 601

作者: @Guillermo-Rauch
时间: 2025-10-18
链接: https://x.com/rauchg/status/1979355355596595662
互动: Likes: 955; Retweets: 14; Replies: 46; Quotes: 5; Views: 112,884; Bookmarks: 59; isReply: 0

POV: your runtime is about to get lapped https://t.co/aa1Z9OQqlx

想象一下：你的运行速度快要被人套圈了 https://t.co/aa1Z9OQqlx

### 602

作者: @Guillermo-Rauch
时间: 2025-10-18
链接: https://x.com/rauchg/status/1979555035865559227
互动: Likes: 11; Retweets: 0; Replies: 2; Quotes: 0; Views: 11,101; Bookmarks: 3; isReply: 1

It’s guaranteed in that Fluid will run it. It’s not guaranteed in that the machine or process can still crash right before it for any reason (distributed system), so it’s not durable. 

For mission critical things you want to avoid eg: making a db write and then a split world scenario where waitUntil’s actions didn’t finalize

从 Fluid 框架会执行它的角度来看，这是有保证的。但从持久性的角度来看，这又是没有保证的，因为机器或进程仍可能在此之前因任何原因崩溃（尤其是在分布式系统中），因此该操作不具备数据持久性。

对于关键任务，你需要避免此类情况，例如：先向数据库写入数据，随后却因系统故障（如网络分区导致的数据分裂场景）使得 `waitUntil` 中设定的后续操作未能最终完成。

### 603

作者: @Guillermo-Rauch
时间: 2025-10-18
链接: https://x.com/rauchg/status/1979557009839268210
互动: Likes: 2; Retweets: 0; Replies: 0; Quotes: 0; Views: 133; Bookmarks: 0; isReply: 1

@BcZsalba @joshmanders It was sarcastic. It’s quite easy to accidentally overload the critical path, but it usually takes work to process that asynchronously. We intend to make that extremely easy

@BcZsalba @joshmanders 那是句反话。意外让关键路径过载是很容易发生的，但要想异步处理这种过载，通常得费点功夫。而我们的目标，就是让这件事变得极其简单。

### 604

作者: @Guillermo-Rauch
时间: 2025-10-18
链接: https://x.com/rauchg/status/1979557111014260814
互动: Likes: 69; Retweets: 0; Replies: 3; Quotes: 0; Views: 11,111; Bookmarks: 2; isReply: 1

@joshmanders Agree and it’s a big missing piece. Excited to show you our take on it

@joshmanders 同意，这确实是个关键的缺失环节。等不及想让你看看我们的方案了。

### 605

作者: @Guillermo-Rauch
时间: 2025-10-18
链接: https://x.com/rauchg/status/1979584494643597490
互动: Likes: 1,030; Retweets: 57; Replies: 82; Quotes: 11; Views: 54,121; Bookmarks: 143; isReply: 0

The highest highs in life are free and accessible to everyone. The feeling of finishing a hard workout, acing a test, shipping great work, having a child, watching the next generation blossom.

生命中最美好的体验无需花费，人人可得。例如，完成一次酣畅淋漓的锻炼，考出一个优异的成绩，交付一份杰出的工作，迎来一个新生命，或是看着下一代茁壮成长。

### 606

作者: @Guillermo-Rauch
时间: 2025-10-18
链接: https://x.com/rauchg/status/1979590878416257216
互动: Likes: 486; Retweets: 22; Replies: 60; Quotes: 9; Views: 60,426; Bookmarks: 202; isReply: 0

Vibe coding vs Vibe engineering:

🅰️ Using AI to operate on the 𝘱𝘳𝘰𝘥𝘶𝘤𝘵
🆚 
🅱️ Using AI to operate on the 𝘤𝘰𝘥𝘦

The former is vibing the later is engineering.

Obviously you might be thinking: “the code is the means to operate on the product! These are the same!”

I believe on a long enough lifetime, for the vast majority of software, they will be.

Products like @v0 and @lovable_dev exist in the former category. At @vercel however our heart is in engineering the best possible products, with the highest possibly quality, which means also having clean ejection and interoperability points with formal engineering tools.

I believe there’ll be ample success and large markets for both vibing and engineering. It’s very likely vibing will become more *opinionated* over time, to make the reliability, security and quality bar *everyone* wants. 

As an example, just yesterday I watched a demo of a highly opinionated full-vibing platform being built on Vercel that delivers better outcomes than engineers, due to the constraints and opinions it imposes.

AI in the service of slop is a temporary, “AI interest rates phenomenon” (AIRP), a period in time where people paid for the fascination of using AI even though the outcome looks like deformed Will Smith in software form.

Our focus at @vercel continues to be AI in the service of quality, not just productivity alone.

氛围编码（Vibe Coding）vs 氛围工程（Vibe Engineering)：

🅰️ 使用 AI 直接操作 * 产品 *
🆚
🅱️ 使用 AI 直接操作 * 代码 *

前者是「氛围式开发」(Vibing），后者是「工程化开发」(Engineering）。

你可能会立刻想到：「代码不就是用来操作产品的工具吗？这俩是一回事！」

我认为，从足够长的时间维度来看，对于绝大多数软件而言，它们最终会趋同。

像 @v0 和 @lovable_dev 这类产品属于前者（直接操作产品）。然而，在 @vercel，我们的核心在于以工程化的方式打造最优秀的产品，追求极致质量。这意味着我们同样注重提供清晰的迁移路径，并与正式的工程工具保持良好的互操作性。

我相信，「氛围式开发」和「工程化开发」都将取得巨大成功并拥有广阔市场。随着时间的推移，「氛围式开发」很可能会变得更加 * 强约束 *（Opinionated），以满足 * 所有人 * 都期望的可靠性、安全性和质量标准。

举一个例子，就在昨天，我观看了一个演示：一个基于 Vercel 构建的、高度强约束的「全氛围」开发平台。由于其施加的严格约束和明确设计主张，它产出的结果甚至优于工程师。

服务于粗制滥造（Slop）的 AI 只是一种暂时的现象，我称之为「AI 新奇溢价期」(AI Interest Rates Phenomenon，AIRP）。在这个阶段，人们为使用 AI 的新奇感买单，尽管其产出结果看起来像是软件形态的、扭曲怪异的威尔·史密斯。

@vercel 的持续关注点，始终是服务于 * 质量 * 的 AI，而不仅仅是生产力。

### 607

作者: @Guillermo-Rauch
时间: 2025-10-18
链接: https://x.com/rauchg/status/1979593865821843563
互动: Likes: 4; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,809; Bookmarks: 1; isReply: 1

@PatLynk_ I like this! Yeah both will succeed but lots of refinement will happen, as well as underlying model improvement

@PatLynk_ 我很赞同！是的，两者最终都会成功，但这中间会经历大量的优化和打磨，同时底层模型也会不断改进。

### 608

作者: @Guillermo-Rauch
时间: 2025-10-18
链接: https://x.com/rauchg/status/1979593949196234778
互动: Likes: 4; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,160; Bookmarks: 0; isReply: 1

@kettanaito Like everything 😁

@kettanaito 万事皆如此 😁

### 609

作者: @Guillermo-Rauch
时间: 2025-10-18
链接: https://x.com/rauchg/status/1979602285161545787
互动: Likes: 6; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,999; Bookmarks: 0; isReply: 1

@RhysSullivan High entropy string filter as defense-in-depth before the tokens are streamed to client

@RhysSullivan 在将 Token 流式传输到客户端之前，设置一道高熵字符串过滤器，作为纵深防御措施。

### 610

作者: @Guillermo-Rauch
时间: 2025-10-18
链接: https://x.com/rauchg/status/1979609210473365938
互动: Likes: 2; Retweets: 0; Replies: 1; Quotes: 0; Views: 729; Bookmarks: 0; isReply: 1

@RhysSullivan base64 would be a high entropy string :P not recommending this approach but curious about it

@RhysSullivan Base64 编码出来的会是一串看起来像高熵的随机字符 :P 虽然不推荐这种做法，不过还挺好奇的。

### 611

作者: @Guillermo-Rauch
时间: 2025-10-18
链接: https://x.com/rauchg/status/1979612793478533508
互动: Likes: 595; Retweets: 12; Replies: 18; Quotes: 3; Views: 135,215; Bookmarks: 302; isReply: 0

Vercel started out similarly, but imagine these Nginx servers being all around the globe, and the metadata (hostnames, routing) being incredibly dynamic. 

Each git push creates a new entry in this metaphorical “config”, and there’s a billion entries. The write throughput is constant, as people can roll back, push, and even change routes dynamically via our Firewall.

Because all these entries can’t possibly fit in one server, you have the problem of creating tiered caches that don’t introduce performance bottlenecks for old entries (otherwise you get “cold boots” of metadata itself).

An additional complexity is that the “origin database” of this system should be able to be offline. If a CDN region gets partitioned from the network, it should still be able to serve production traffic.

This metadata system has had to be re-architected 4 times as we’ve reached different levels of scale and also ambition. We actually set out to make the original design as monolithic as possible, but scale will push you, for good reason, into services (whether we can call them “micro” or “macro” is debatable).

If you’re interested in working on the infrastructure that accelerates the deployment rate of the world, my DMs are open!

Vercel 的起点与此相似，但请想象一下，这些 Nginx 服务器遍布全球，而其元数据（主机名、路由规则）又是极其动态的。

每一次 git push 都会在这个比喻中的「配置」里新增一个条目，这样的条目高达数十亿个。写入吞吐量持续不断，因为开发者们可以进行回滚、推送，甚至通过我们的防火墙动态地更改路由规则。

由于所有这些条目显然无法存放在单一服务器上，这就引出了一个挑战：如何构建分层缓存体系，使其不会对旧有条目造成性能瓶颈（否则元数据本身就会遭遇「冷启动（cold boot）」问题）。

另一个复杂之处在于，该系统的「源数据库」必须具备离线能力。即使某个 CDN 区域与网络断开连接，它也应该能够继续处理生产流量。

随着我们发展到不同的规模阶段并怀有更高的目标，这套元数据系统已经不得不进行了四次重新架构。实际上，我们最初的目标是尽可能将原始设计做成单体式，但规模的增长 —— 以及充分的理由 —— 会推动你转向服务化架构（至于该称之为「微」服务还是「宏」服务，尚有讨论空间）。

如果你对开发能够加速全球部署速度的基础设施感兴趣，欢迎私信我交流！

### 612

作者: @Guillermo-Rauch
时间: 2025-10-18
链接: https://x.com/rauchg/status/1979650234641985974
互动: Likes: 906; Retweets: 32; Replies: 199; Quotes: 14; Views: 153,261; Bookmarks: 76; isReply: 0

We now support NestJS, NextJS, NuxtJS. Let me know what we should support next

目前，我们已经支持了 NestJS、NextJS 和 NuxtJS。接下来，欢迎大家告诉我们希望我们支持什么。

### 613

作者: @Guillermo-Rauch
时间: 2025-10-18
链接: https://x.com/rauchg/status/1979651318617969087
互动: Likes: 5; Retweets: 0; Replies: 0; Quotes: 0; Views: 2,696; Bookmarks: 0; isReply: 1

@awpthorp NTML

@awpthorp NTML

### 614

作者: @Guillermo-Rauch
时间: 2025-10-18
链接: https://x.com/rauchg/status/1979660103675687157
互动: Likes: 1,189; Retweets: 56; Replies: 57; Quotes: 27; Views: 377,784; Bookmarks: 446; isReply: 0

We're benchmarking a bunch of models for one of our internal agents. 🤯 Kimi K2 is up to 5x faster and 50% more accurate than frontier proprietary models…

And it took very little work to switch out the models via @aisdk / @vercel ai gateway 😬 (served by @groqinc) https://t.co/vA3yWAuiLI

我们正在为内部的一个 AI 智能体对一系列模型进行性能评估。🤯 结果发现，Kimi K2 的速度可比顶尖的专有模型快上 5 倍之多，准确率也高出 50%...

而通过 @aisdk / @vercel 的 AI 网关（由 @groqinc 提供算力支持）来更换模型，整个过程几乎不费吹灰之力 😬 https://t.co/vA3yWAuiLI

### 615

作者: @Guillermo-Rauch
时间: 2025-10-18
链接: https://x.com/rauchg/status/1979697020475736398
互动: Likes: 94; Retweets: 1; Replies: 11; Quotes: 0; Views: 5,231; Bookmarks: 1; isReply: 1

@Madisonkanna Best game ever

@Madisonkanna 这游戏简直封神了！/ 这游戏是史上最佳！

### 616

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979707408592372115
互动: Likes: 0; Retweets: 0; Replies: 1; Quotes: 0; Views: 98; Bookmarks: 1; isReply: 1

@y_nk @BriansAngles yes but it turns out it's an issue with a proprietary runtime… you can't repro this jump in latency in node.js

@y_nk @BriansAngles 对，但后来发现是某个专有运行时（runtime）的问题…… 你在 Node.js 里是没法复现这种延迟飙升的情况的。

### 617

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979707570903564514
互动: Likes: 2; Retweets: 0; Replies: 0; Quotes: 0; Views: 136; Bookmarks: 0; isReply: 1

@oalexdoda @Madisonkanna never got into it, same with warcraft. AoE ride-or-die

@oalexdoda @Madisonkanna 我也没玩过《魔兽世界》，这类游戏都没接触过。但《帝国时代》（AoE）是我的本命游戏，死忠粉一枚。

### 618

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979718869871886591
互动: Likes: 20; Retweets: 0; Replies: 0; Quotes: 0; Views: 2,936; Bookmarks: 1; isReply: 1

@yusukebe congrats, amazing project

@yusukebe 恭喜，项目太棒了！

### 619

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979730089400222185
互动: Likes: 783; Retweets: 16; Replies: 62; Quotes: 5; Views: 72,566; Bookmarks: 29; isReply: 0

▲🕸️🎃 
This year I’m going as a useEffect loop https://t.co/pbexIKFvVm

▲🕸️🎃
今年我的万圣节装扮是 `useEffect` 循环。https://t.co/pbexIKFvVm

### 620

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979730442288075219
互动: Likes: 5; Retweets: 0; Replies: 0; Quotes: 0; Views: 447; Bookmarks: 0; isReply: 1

@srd2o Crawley McCrawlface

@srd2o Crawley McCrawlface

### 621

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979730937400459343
互动: Likes: 16; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,354; Bookmarks: 0; isReply: 1

@ryandavogel It’s real we just made it 😁

@ryandavogel 是真的！我们刚搞定 / 刚做出来！😁
（注：根据上下文，「搞定」更口语化且带成就感，「做出来」更侧重于制作完成，两者皆可，视具体所指事物而定。）

### 622

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979732029869900093
互动: Likes: 16; Retweets: 1; Replies: 2; Quotes: 0; Views: 1,472; Bookmarks: 0; isReply: 1

@ryandavogel Up close to prove no ai 😆 https://t.co/66Wj6iiuVV

@ryandavogel 来个特写，证明这可不是 AI 做的哦 😆 https://t.co/66Wj6iiuVV

### 623

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979742615450071284
互动: Likes: 1; Retweets: 0; Replies: 1; Quotes: 0; Views: 103; Bookmarks: 0; isReply: 1

@GavrielTech @anthonysheww super curious for your feedback! our DMs are open 😁🤗

@GavrielTech @anthonysheww 非常期待你们的反馈！欢迎随时私信交流 😁🤗

### 624

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979774317434228798
互动: Likes: 365; Retweets: 4; Replies: 27; Quotes: 3; Views: 47,103; Bookmarks: 37; isReply: 0

It’s so enthralling to be able to watch the greatest human alive, at whatever discipline. 

There’re over 8B people but there’s one guy or gal out there that’s at the top of the game. Like Maradona in ‘86.
https://t.co/ZUfNq4XBta

能够亲眼见证当世最杰出人物的风采，无论他身处哪个领域，都令人无比着迷。

全球有超过 80 亿人，但总会有那么一个人，在其领域内登峰造极。就像 1986 年的马拉多纳那样。
https://t.co/ZUfNq4XBta

### 625

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979774627066052921
互动: Likes: 5; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,548; Bookmarks: 1; isReply: 1

@iamcheercheung It can, I’ll share the code. I used the libsdl wasm build from https://t.co/YtUfA7fIyM repo

@iamcheercheung 可以的，我来分享代码。我用的是从 https://t.co/YtUfA7fIyM 这个代码库构建的 libsdl wasm 版本。

### 626

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979776735639171196
互动: Likes: 4; Retweets: 0; Replies: 2; Quotes: 0; Views: 1,093; Bookmarks: 0; isReply: 1

@abhiaiyer We should acquire him for the Giants tbh

@abhiaiyer 讲真，我们该把他签来巨人队。

### 627

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979779758738329981
互动: Likes: 20; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,367; Bookmarks: 0; isReply: 1

@jamonholmgren New bar is to be great like Shohei

@jamonholmgren 新的标杆是，要像大谷翔平一样出色。

### 628

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979794264143081589
互动: Likes: 29; Retweets: 0; Replies: 1; Quotes: 0; Views: 3,297; Bookmarks: 0; isReply: 1

@tmikov There’s interest

@tmikov 对此有兴趣。

### 629

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979932696005541941
互动: Likes: 85; Retweets: 0; Replies: 5; Quotes: 0; Views: 14,608; Bookmarks: 2; isReply: 1

@ChristoRibeiro @vercel_support We should bump to 1.3

@ChristoRibeiro @vercel_support 我们该升级到 1.3 版本了。

### 630

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979932949156872619
互动: Likes: 70; Retweets: 0; Replies: 4; Quotes: 0; Views: 12,725; Bookmarks: 1; isReply: 1

@ChristoRibeiro @vercel_support Realistically though we should let customers choose based on some versioning guidelines ala @nodejs cc @bunjavascript

@ChristoRibeiro @vercel_support 不过说实在的，我们应该让客户能够依据一套版本管理规范来做选择，可以效仿 @nodejs 的做法。cc @bunjavascript

### 631

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979933993114968340
互动: Likes: 3; Retweets: 0; Replies: 2; Quotes: 0; Views: 635; Bookmarks: 0; isReply: 1

@ChristoRibeiro @ryandavogel @vercel_support @nodejs @bunjavascript Concerned that some dev bumps Bun locally, installs a dep, and then that changes the prod runtime version unexpectedly? Is that how it’d play out?

@ChristoRibeiro @ryandavogel @vercel_support @nodejs @bunjavascript 是否担心有开发者在本地更新了 Bun 版本，安装某个依赖后，会导致生产环境的运行时版本被意外更改？实际情况会是这样吗？

### 632

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979934769766134116
互动: Likes: 6; Retweets: 0; Replies: 2; Quotes: 0; Views: 649; Bookmarks: 0; isReply: 1

@ryandavogel @ChristoRibeiro @vercel_support @nodejs @bunjavascript I was addressing the idea that we’d get it from the lockfile

@ryandavogel @ChristoRibeiro @vercel_support @nodejs @bunjavascript 我是在澄清那种认为我们可以从锁文件（lockfile）中获取它的说法。

### 633

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979937138805182785
互动: Likes: 0; Retweets: 0; Replies: 1; Quotes: 0; Views: 294; Bookmarks: 0; isReply: 1

@GustavoValverde @ChristoRibeiro @vercel_support Where specifically?

@GustavoValverde @ChristoRibeiro @vercel_support 具体是哪里呢？

### 634

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979941039717949583
互动: Likes: 1; Retweets: 0; Replies: 1; Quotes: 0; Views: 63; Bookmarks: 0; isReply: 1

@kofiwusuachiaw This goes beyond queues, which have their own drawbacks when used heavily. Tune in 😁

@kofiwusuachiaw 这不仅仅是队列的问题，队列本身在重度使用时也有弊端。等着瞧吧 😁

### 635

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979943265656074427
互动: Likes: 1; Retweets: 0; Replies: 0; Quotes: 0; Views: 191; Bookmarks: 0; isReply: 1

@GustavoValverde @ChristoRibeiro @vercel_support Good one, will fix

@GustavoValverde @ChristoRibeiro @vercel_support 收到，问题已确认，会尽快修复。

### 636

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979956812586881378
互动: Likes: 1,296; Retweets: 85; Replies: 65; Quotes: 16; Views: 133,784; Bookmarks: 642; isReply: 0

I love @karpathy’s idea of stripping the LLM down to a “cognitive core”, rather than a memorization machine.

The three ideal ingredients of a successful agent seem to be:
▫Cognition
▫Knowledge 
▫Skills

As a metaphor, great engineers transcend language. You can write Python, TypeScript, and Rust in the same codebase due to how good your base cognition has gotten.

Knowledge and facts should be retrieved via search. I expect @exaailabs, @perplexity API and @p0 to only get more important. (The LLM should still have in Karpathy’s terms “a base curriculum of knowledge)

I’m a fan of the arrival of Skills. That same Rust engineer will likely struggle a bit to write “idiomatic React”. That’s a skill. That’s important. Skills are likely the most interesting piece of what will make agents really stand out at certain domains and codebases.

What we hear frequently is that @v0 particularly stands out at aesthetic and UI skills, obviously around @nextjs

我很赞同 @karpathy 的观点，即应将大语言模型精简为一个「认知核心」，而非单纯的记忆机器。

一个成功的 AI 智能体似乎包含三大理想要素：
▫认知
▫知识
▫技能打个比方，顶尖的工程师能超越特定编程语言的限制。正是由于你的基础认知能力足够强大，你才能在同一个代码库中游刃有余地使用 Python、TypeScript 和 Rust。

知识和事实应当通过搜索来获取。我预计 @exaailabs、@perplexity API 和 @p0 这类服务只会愈发重要。（用 Karpathy 的话说，大语言模型本身仍应具备「一套基础的知识课程」。）

我很看好「技能」这一要素的出现。同一位精通 Rust 的工程师，在编写「符合 React 范式」的代码时可能就会感到有些吃力。这就是技能。它至关重要。技能很可能是一个最有趣的要素，它将决定 AI 智能体能否在特定领域和代码库中真正脱颖而出。

我们常听到的一种反馈是，@v0 在美学和用户界面技能方面尤其出众，这显然是在 @nextjs 框架的语境下展现的。

### 637

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979957799955407026
互动: Likes: 85; Retweets: 2; Replies: 6; Quotes: 0; Views: 21,346; Bookmarks: 26; isReply: 1

Two other skills I love that some people at @vercel have in spades:

▫Security engineering. It’s a “reverse engineering”, “think outside the box”, adversarial mindset applied to the analysis of a codebase 

▫Incident response. There’s a set of playbooks and way of doing almost detective-like, forensic investigations of a “crime scene” of infrastructure 😆 

I’ve noticed excellent engineers from a cognitive or knowledge perspective still struggle with these. That’s fine, humans have certainly not mastered every single skill nor are they expected to.

Excited to see the generation of “skill retrieval” and training for agents.

还有两项技能我特别欣赏，而 @vercel 的一些同事在这方面堪称高手：

▫** 安全工程 **。这需要一种「逆向工程」和「跳出思维定式」的对抗性思维，并将其运用到代码库的分析中。

▫** 事件响应 **。这需要遵循一套应急预案和操作流程，对基础设施出现的「案发现场」进行近乎侦探式的取证调查 😆。

我注意到，有些工程师在认知或专业知识上非常出色，但在这些技能上仍感到困难。这很正常，人类本就不可能、也无需精通所有技能。

我很期待看到，未来为 AI 智能体进行「技能检索」和训练这方面的发展。

### 638

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979958756667728105
互动: Likes: 7; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,655; Bookmarks: 1; isReply: 1

@adityab_tech @karpathy Maybe that’s too simplistic but certainly a good mental model for where agents can spike, especially when combined with the right interfaces and tooling

@adityab_tech @karpathy 也许这个想法过于简单，但它无疑是一个很好的心智模型，有助于理解 AI 智能体（AI Agent）能在哪些方面实现突破性进展，尤其是在配备了合适的界面和工具时。

### 639

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979959424644178382
互动: Likes: 5; Retweets: 0; Replies: 2; Quotes: 1; Views: 662; Bookmarks: 0; isReply: 1

@Ma_jrz Yes. Our infra on top of EC2. It’s like collocating at Flexential but more reliable, secure, and scalable. And crucially it’s where basically all the Internet services are 1ms away (Stripe, Snowflake, Supabase, etc)

是的。我们的基础设施运行在 EC2 之上。这类似于在 Flexential 进行机柜托管，但更加可靠、安全且可扩展。关键在于，这里基本上所有主要的互联网服务（例如 Stripe，Snowflake，Supabase 等）的网络延迟都在 1 毫秒以内。

### 640

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979969550381940841
互动: Likes: 1,284; Retweets: 11; Replies: 126; Quotes: 25; Views: 204,167; Bookmarks: 92; isReply: 0

I had my first BJJ “fight” the other day. I see what the hype is all about now. All my boys are insta-enrolled. Brazil cooked. https://t.co/oFMzWe6gTu

前几天我体验了人生第一次巴西柔术（BJJ）「实战」。我现在可算明白为啥大家都这么狂热了。我的兄弟们全都秒速报名了。巴西柔术，真有你的！https://t.co/oFMzWe6gTu

### 641

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979978804245528807
互动: Likes: 36; Retweets: 0; Replies: 1; Quotes: 0; Views: 8,569; Bookmarks: 1; isReply: 1

@daniipreneur Wooo woo wooah 😆

@daniipreneur 哇哦！哇！哇啊！😆

### 642

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979990513844716017
互动: Likes: 1,834; Retweets: 35; Replies: 56; Quotes: 7; Views: 225,809; Bookmarks: 47; isReply: 0

This was a great day

今天真是美好的一天。

### 643

作者: @Guillermo-Rauch
时间: 2025-10-19
链接: https://x.com/rauchg/status/1979995184999043411
互动: Likes: 2; Retweets: 0; Replies: 1; Quotes: 1; Views: 882; Bookmarks: 0; isReply: 1

@maxthoon @OpenAI @AnthropicAI This is a benchmark of answers where those models failed catastrophically. And to be fair, all models are doing poorly, 60% is not good enough

@maxthoon @OpenAI @AnthropicAI 这是一项基准测试，展示了这些模型在回答上出现的灾难性失败。平心而论，所有模型的表现都很糟糕，60% 的准确率远未达标。

### 644

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980069425379455426
互动: Likes: 5; Retweets: 0; Replies: 2; Quotes: 0; Views: 5,202; Bookmarks: 1; isReply: 1

@trashh_dev Let’s

@trashh_dev 来，我们

### 645

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980101636057100460
互动: Likes: 148; Retweets: 0; Replies: 12; Quotes: 2; Views: 24,969; Bookmarks: 11; isReply: 0

They shipped something so great it needed no fluff. Just pure signal https://t.co/a7y7YU1rMi

他们推出的东西太棒了，根本无需吹嘘。全是硬核干货。https://t.co/a7y7YU1rMi

### 646

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980137827770962149
互动: Likes: 10; Retweets: 0; Replies: 0; Quotes: 0; Views: 2,499; Bookmarks: 0; isReply: 1

@RaillyHugo @v0 Cool

@RaillyHugo @v0 酷！

### 647

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980209008981188957
互动: Likes: 132; Retweets: 2; Replies: 9; Quotes: 2; Views: 28,102; Bookmarks: 7; isReply: 1

@marc_louvion @andrewqu_ @vercel Catching up to the incident logs. Vercel teams have failed over a number of services. Our recovery is significant, and impact lessened, due to our distributed nature. Still sad to see. Sorry about this and sharing more detail soon. https://t.co/6TR5WlkIZq is up to date.

@marc_louvion @andrewqu_ @vercel 我们正在跟进事件日志的最新情况。Vercel 团队已对多项服务执行了故障转移。得益于我们分布式的系统架构，恢复工作取得了显著进展，事件影响也已减弱。我们对发生这样的事件深表遗憾，并将很快分享更多细节。您可以查看实时更新的链接以获取最新信息：https://t.co/6TR5WlkIZq。

### 648

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980214247532704165
互动: Likes: 688; Retweets: 31; Replies: 57; Quotes: 14; Views: 116,530; Bookmarks: 85; isReply: 0

Like many others, Vercel is seeing impact from the AWS outage in us-east-1 (IAD).

Our service is global in nature, which means the impact from this outage has varied by customer and region.

We’ve taken steps to fail over a number of services. The IAD CDN region was rerouted, and customers with Function failover or Functions deployed to  multiple regions should be seeing healthy invocations.

A lot of IAD-dependent services have been failed over and are seeing recovery. The underlying upstream issue is also seeing significant improvement.

While painful, this will be instructive of a  number of massive improvements we can deliver on Vercel to continue to improve global resilience for all our customers.

Please check out https://t.co/vL40eQQwrK for details on recovery and future posts-mortem.

与许多其他公司一样，Vercel 也受到了 AWS 弗吉尼亚北部（us-east-1，IAD）区域服务中断的影响。

我们的服务具有全球性，因此此次中断对不同客户和地区的影响程度各不相同。

我们已经执行了多项服务的故障转移。IAD 区域的 CDN 流量已被重新路由，对于启用了函数故障转移或将函数部署在多个区域的客户，其函数调用应已恢复正常。

大部分依赖 IAD 区域的服务已完成故障转移并正在恢复。上游的根本问题也已得到显著改善。

此次事件虽然带来了挑战，但也极具指导意义，它将推动我们在 Vercel 平台上实施一系列重大改进，持续为所有客户增强全球服务的韧性。

详情及后续的事故复盘报告，请查看：https://t.co/vL40eQQwrK。

### 649

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980274758869717362
互动: Likes: 18; Retweets: 0; Replies: 2; Quotes: 0; Views: 6,076; Bookmarks: 1; isReply: 1

@johnjameswow1 DM me your account id and we we will follow up

@johnjameswow1 私信我你的账户 ID，我们会联系你。

### 650

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980296042118836659
互动: Likes: 2; Retweets: 0; Replies: 1; Quotes: 0; Views: 921; Bookmarks: 0; isReply: 1

@kylewhocodes i'm down

@kylewhocodes 我加入 / 算我一个。

### 651

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980314641613091318
互动: Likes: 1,668; Retweets: 61; Replies: 114; Quotes: 19; Views: 249,855; Bookmarks: 251; isReply: 0

This is what the AWS us-east-1 outage looked like on our graphs. Despite its catastrophic and rare nature, Vercel was still able to successfully serve billions of requests.

But let me be clear: our goal is for zero requests to fail. I'm really sorry to our customers and developers for this unacceptable degradation in availability.

We’ve designed the Vercel platform with multiple layers of redundancy. Functions execute in multiple availability zones and support failover regions. There are multiple global tiers of metadata replication. Multiple tiers of caches in our CDN that shield the access to origins (e.g.: us-east-1).

But there's more to do. The silver lining: this is as good of a chaos engineering exercise as it gets. A multi-service failure of this nature is exceedingly rare (85 impacted services), especially with a global service failure (IAM).

Looking forward to sharing our plans for further enhancement of our global resilience and a comprehensive post-mortem.

从我们的监控图表来看，这就是 AWS 的 us-east-1 区域发生中断时的情况。尽管这次中断影响巨大且十分罕见，Vercel 仍然成功处理了数十亿次请求。

但我要明确一点：我们的目标是实现零请求失败。对于这次不可接受的可用性下降，我向我们的客户和开发者致以诚挚的歉意。

Vercel 平台在设计上就具备多层冗余。函数在多个可用区执行，并支持故障转移区域。元数据复制也设有多个全球层级。此外，我们的 CDN 设有多级缓存，用以屏蔽对源站（例如 us-east-1 区域）的直接访问。

但我们深知，这还不够。一个积极的方面是：这堪称一次绝佳的混沌工程实践。这种波及多项服务（85 项服务受影响）的故障极其罕见，尤其当它还伴随着 IAM 这样的全球性服务故障时，就更为罕见了。

我们期待与大家分享我们关于进一步提升全球服务韧性的计划，并提供一份全面的事故分析报告。

### 652

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980316868184535292
互动: Likes: 948; Retweets: 15; Replies: 63; Quotes: 145; Views: 1,219,887; Bookmarks: 236; isReply: 1

I want to specially thank the @vercel team for working around the clock to keep customers safe and available.

In fact, I was sleeping, it was 2am~ ish, and I was alerted about this issue because my internet mattress (which I love, shoutout to @eightsleep) was warm 😅, which led me to opening the app…

I notice there's an ongoing AWS outage. I open HN and it's there too. I go to our incidents channel. A dozen incidents had been automatically filed by our systems, later merged, and failover and service restoration was well underway by on-call teams.

us-east-1 is not fully back. There are lingering networking issues and throttled creation of resources (e.g.: EC2). These incidents take a lot of work to recover from, which the Vercel team is taking care of right now. I'm extremely thankful to them and our partners at AWS.

我想特别感谢 @vercel 团队，他们为了保障客户的安全与服务的稳定，一直在昼夜不停地工作。

说起来，我当时其实正在睡觉，大概凌晨两点左右，之所以被这个问题惊醒，是因为我那张智能床垫（我超爱它，给 @eightsleep 点个赞）变得很暖和 😅，于是我就顺手打开了手机应用…

接着我注意到 AWS 正在发生服务中断。我又打开了 Hacker News（HN），发现上面也在讨论这件事。于是我点开了我们内部的事件响应频道。系统已经自动创建了十几个相关事件（后来合并了），而值班团队早已启动了故障转移和服务恢复流程，一切都在有序进行中。

目前，us-east-1 区域尚未完全恢复正常。仍然存在一些网络问题，并且创建资源（例如 EC2 实例）受到了限流。从这类事件中恢复需要大量的协调与处理工作，Vercel 团队此刻正在全力应对。我对他们以及我们在 AWS 的合作伙伴表示由衷的感谢。

### 653

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980321402566926440
互动: Likes: 9; Retweets: 0; Replies: 0; Quotes: 0; Views: 3,349; Bookmarks: 0; isReply: 1

@BlackPill_1 Not in this fashion. Details matter in engineering.

@BlackPill_1 不是这么回事。工程上，细节决定成败。

### 654

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980321631865376955
互动: Likes: 110; Retweets: 0; Replies: 11; Quotes: 1; Views: 16,048; Bookmarks: 0; isReply: 1

@natemcgrady @vercel so excited to have you… lfg

@natemcgrady @vercel 太激动了，你能加入…… 冲啊！(lfg)

### 655

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980322104089407701
互动: Likes: 29; Retweets: 0; Replies: 2; Quotes: 0; Views: 9,124; Bookmarks: 1; isReply: 1

@cipriancaba Impact varied dramatically by customer. Not making any excuses and this will be the area where we put our most effort in remediation. A full post-mortem will follow explaining the cascading failures that occurred.

对各个客户造成的影响差异极大。我们不会寻找任何借口，并且这将是我们在补救工作中投入最多精力的环节。后续将提供一份完整的事故分析报告，详细说明发生的级联故障。

### 656

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980323004728111462
互动: Likes: 9; Retweets: 0; Replies: 1; Quotes: 0; Views: 5,217; Bookmarks: 0; isReply: 1

@destinydinam Thanks for your trust. We will do right by you and all our customers.

@destinydinam 感谢您的信任。我们定会不负所托，服务好您以及我们所有的客户。

### 657

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980325404113359304
互动: Likes: 106; Retweets: 1; Replies: 5; Quotes: 0; Views: 51,471; Bookmarks: 12; isReply: 1

@josepchetrit12 @vercel @eightsleep life-changing product

@josepchetrit12 @vercel @eightsleep 这产品简直改变了我的生活。

### 658

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980328849507512376
互动: Likes: 31; Retweets: 0; Replies: 3; Quotes: 1; Views: 6,337; Bookmarks: 5; isReply: 1

@ryandavogel i'm highly confident. the bed was rly warm, and i have it set to -6 🥶. but it's possible i also had to tune it? and that's when I saw the aws status message on the app 😁

@ryandavogel 我相当确定。床确实特别暖和，虽然我设的是零下 6 度 🥶。不过，会不会是我当时还得微调一下？就在这当口，我瞅见应用里弹出了 AWS 的状态消息 😁。

### 659

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980330045894951365
互动: Likes: 16; Retweets: 0; Replies: 2; Quotes: 0; Views: 5,149; Bookmarks: 0; isReply: 1

@AntoniGusto I can be proud of the hard work of my team even if temporarily the outcomes are not great. We will get through this stronger. Like I said, customers have varied profiles of downtime, and we will do right by everyone.

@AntoniGusto 即使暂时的成果还不理想，我依然为团队的辛勤付出感到骄傲。我们会一起挺过去，并且变得更强大。就像我说的，客户遇到的停机问题各有不同，我们一定会妥善处理，对每一位客户负责。

### 660

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980349354033791462
互动: Likes: 4; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,717; Bookmarks: 0; isReply: 1

@gzlvl Are you using Middleware (globally deployed) or targeting IAD? Still impact in us-east-1. We’re shipping mitigations for the former

@gzlvl 你们使用的是（全局部署的）中间件，还是针对 IAD（AWS 的 us-east-1 区域内部代码）的方案？问题在 us-east-1 区域仍然存在影响。我们正在为第一种情况（全局中间件）部署修复方案。

### 661

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980363153927204995
互动: Likes: 12; Retweets: 0; Replies: 2; Quotes: 0; Views: 2,360; Bookmarks: 1; isReply: 1

@CreatedByJannn It's a very fluid incident. Some aspects of us-east-1 have improved and some have worsened. We're all-hands on deck on mitigations

@CreatedByJannn 这是一个情况快速变化的事件。我们 us-east-1 区域的部分指标有所改善，但部分指标出现恶化。我们正在全员投入，全力进行缓解工作。

### 662

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980365654495752411
互动: Likes: 2; Retweets: 0; Replies: 2; Quotes: 0; Views: 383; Bookmarks: 2; isReply: 1

@sillydarket @CreatedByJannn @Railway We have an insane amount of control. In fact, far more control than companies that pre-bake and pre-purcahse their hardware and location decisions.

We've re-routed IAD. Customers, services, etc, however, have hard IAD dependencies, so we're working hard on its restoration.

我们拥有惊人的控制权。事实上，我们的自主权远比那些需要预先敲定硬件采购和选址决策的公司要大得多。

我们已经对依赖 IAD 的服务进行了重新调度。但由于客户、服务等方面对 IAD 存在强依赖，我们正在全力恢复其正常运行。

### 663

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980367186607898952
互动: Likes: 137; Retweets: 6; Replies: 49; Quotes: 1; Views: 24,561; Bookmarks: 15; isReply: 0

Both https://t.co/MKF1RbJJyF and https://t.co/EcF4k5IhdV are sold out, but I'd hate to miss cracked community members / engineers / startups / customers who really really want to attend. 

Plz reply if you're around Wed or Thu this week in San Francisco and really want to attend! We're making some really cool announcements 🫶

https://t.co/MKF1RbJJyF 和 https://t.co/EcF4k5IhdV 的门票都已售罄，但我实在不忍心错过那些真心渴望参与的、顶尖的社区成员、工程师、初创公司和客户们。

如果你本周三或周四正好在旧金山，并且真的非常想参加，请务必回复我！我们准备了一些超酷的发布要宣布 🫶

### 664

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980368213142835698
互动: Likes: 51; Retweets: 2; Replies: 1; Quotes: 0; Views: 3,744; Bookmarks: 0; isReply: 1

@saltyAom Already on the roadmap. Native Elysia support coming.

@saltyAom 已经在我们的路线图中了。对 Elysia 的原生支持即将推出。

### 665

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980372157302809051
互动: Likes: 4; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,526; Bookmarks: 0; isReply: 1

@imbereket Done, check DM 😁

@imbereket 搞定了，看下 DM 😁

### 666

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980377103511253229
互动: Likes: 1; Retweets: 0; Replies: 1; Quotes: 0; Views: 119; Bookmarks: 0; isReply: 1

@grumpypcodes Due to one cascading component impacted by us-east-1, Vercel APIs are impacted. No production traffic impact.

由于 us-east-1 区域的一个组件发生级联故障，Vercel API 服务受到影响。生产流量不受影响。

### 667

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980378135377113171
互动: Likes: 56; Retweets: 0; Replies: 8; Quotes: 0; Views: 8,554; Bookmarks: 1; isReply: 1

@sandrin_joy A us-east-1 component has caused a cascading failure on our APIs. Prod workloads unaffected. Working on asap restoration

@sandrin_joy 我们的一个 us-east-1 区域组件发生了故障，并引发了 API 的连锁故障。生产环境工作负载未受影响。我们正在全力进行紧急修复。

### 668

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980394710461211084
互动: Likes: 8; Retweets: 0; Replies: 2; Quotes: 0; Views: 3,266; Bookmarks: 1; isReply: 1

@erayyocak All production workloads are up. We're all hands on deck on restoring dashboard access. Sorry for the inconvenience

@erayyocak 所有生产环境的工作负载均已恢复正常。我们正在全力抢修，以恢复仪表板的访问。给您带来不便，深表歉意。

### 669

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980395869246832719
互动: Likes: 0; Retweets: 0; Replies: 1; Quotes: 0; Views: 116; Bookmarks: 0; isReply: 1

@arthuryuzbashew Recurring DMCA issues, which, if we don't take swift action around, risks broad platform downtime. 

We've sent plenty of communication (from dmca@vercel.com). Support team will reach out again.

@arthuryuzbashew 关于反复出现的 DMCA（数字千年版权法案）问题，如果我们不迅速采取行动，可能会导致大范围的平台服务中断。

我们已经通过 dmca@vercel.com 邮箱进行了多次沟通。支持团队将再次与您联系。

### 670

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980397700228215278
互动: Likes: 0; Retweets: 0; Replies: 0; Quotes: 0; Views: 104; Bookmarks: 0; isReply: 1

@RousuPhillip Production traffic is very healthy right now. We're working through unexpected downtime on the dashboard and control plane. Apologies.

@RousuPhillip 生产环境流量目前一切正常。我们正在处理仪表板和控制平面发生的意外服务中断。深表歉意。

### 671

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980397745774248126
互动: Likes: 1; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,035; Bookmarks: 0; isReply: 1

@sirlonlilokli All hands on deck 🙏

急需大家帮忙 / 支援 🙏
（或根据上下文更口语化的表达：兄弟们，赶紧来搭把手！🙏 / 各位，紧急求助！🙏）

### 672

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980399480131449242
互动: Likes: 0; Retweets: 0; Replies: 1; Quotes: 0; Views: 983; Bookmarks: 0; isReply: 1

@clkbsfth @erayyocak Mind DM'ing me more details about what you're seeing? If it's a prod workload should be healthy. Apologies for the disruption.

@clkbsfth @erayyocak 方便私信告诉我更多细节吗？如果是生产环境的工作负载，按理应该运行正常。对这次服务中断深感抱歉。

### 673

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980399570606780467
互动: Likes: 7; Retweets: 0; Replies: 1; Quotes: 0; Views: 274; Bookmarks: 0; isReply: 1

@james_r_perkins @RhysSullivan @_heyglassy On it 🫡

收到，马上办 🫡

### 674

作者: @Guillermo-Rauch
时间: 2025-10-20
链接: https://x.com/rauchg/status/1980415126911246837
互动: Likes: 0; Retweets: 0; Replies: 1; Quotes: 0; Views: 143; Bookmarks: 0; isReply: 1

@arthuryuzbashew Thanks. For posterity, you'll have to treat inbound legal warnings as high-SEV tickets with SLAs. That's how we do it at Vercel. If we don't abide but these strict SLAs, we risk broad downtime.

@arthuryuzbashew 谢谢。为了以后有据可查，你必须把收到的法律警告当作高 SEV（严重性）级别的工单来处理，并且要满足相应的服务等级协议（SLA）要求。我们 Vercel 就是这么做的。如果不遵守这些严格的 SLA，就可能导致大范围的服务中断。

### 675

作者: @Guillermo-Rauch
时间: 2025-10-21
链接: https://x.com/rauchg/status/1980424117771010476
互动: Likes: 1; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,557; Bookmarks: 0; isReply: 1

@Thomasmarkelly That's not degradation. That's off-peak hours traffic. Traffic was ramping up as daytime Monday in US began

@Thomasmarkelly 那不是服务降级。那是非高峰时段的流量。随着美国周一白天的到来，流量正在快速攀升。

### 676

作者: @Guillermo-Rauch
时间: 2025-10-21
链接: https://x.com/rauchg/status/1980436503445795010
互动: Likes: 764; Retweets: 4; Replies: 8; Quotes: 7; Views: 390,760; Bookmarks: 45; isReply: 1

@PrayagBhakar No, there were dozens of engineers and support staff in the call and incident channels. They were likely expecting me to wake up and learn at a normal time. You don’t want to rely on a CEO for technical disaster recovery work (though I enjoy chiming in 😁)

@PrayagBhakar 不是的，当时通话和事件处理频道里有好几十位工程师和支持人员呢。他们大概以为我会按正常作息时间醒来才知道这事。技术性的灾难恢复工作，本来也不该指望 CEO 来做（当然，我个人倒是很乐意凑个热闹 😁）。

### 677

作者: @Guillermo-Rauch
时间: 2025-10-21
链接: https://x.com/rauchg/status/1980436690629194058
互动: Likes: 269; Retweets: 6; Replies: 29; Quotes: 3; Views: 46,844; Bookmarks: 47; isReply: 0

Civilization advances by the number of 3-letter acronyms of cognitive load we delete from between you and shipping a great application. RSC, SSR, CSR, SSG, PPR, ISR, SPA, MPA have their days "numbered".

As @nextjs evolves, it'll look more and more like RoR and friends. What the world w̵a̵n̵t̵s̵ needs is easy to use. What React adds in an insanely high bar on interactivity, richness and quality (not to mention the 'mobile native' option value with RN).

Excited to ship a big chunk of this vision at https://t.co/MKF1RbJJyF – tune in to the livestream.

文明的进步，体现在我们移除了多少横亘在开发者与打造出色应用之间的、那些增加认知负荷的三字母缩写。服务器组件（RSC）、服务端渲染（SSR）、客户端渲染（CSR）、静态站点生成（SSG）、部分预渲染（PPR）、增量静态再生（ISR）、单页应用（SPA）、多页应用（MPA）这些概念的日子已经「屈指可数」了。

随着 Next.js 的发展，它会越来越像 Ruby on Rails（RoR）这类框架。这个世界（表面上）想要的、（实际上）需要的，是易于使用的工具。React 在交互性、丰富性和应用质量方面树立了极高的标准（更不用说它通过 React Native（RN）带来的「移动端原生」开发选项价值）。

我们很高兴能在 https://t.co/MKF1RbJJyF 实现这一愿景的很大一部分 —— 敬请关注直播。

### 678

作者: @Guillermo-Rauch
时间: 2025-10-21
链接: https://x.com/rauchg/status/1980440504631455980
互动: Likes: 7; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,195; Bookmarks: 0; isReply: 1

@kirso_ @nextjs i'm in 😁

@kirso_ @nextjs 算我一个！😁

### 679

作者: @Guillermo-Rauch
时间: 2025-10-21
链接: https://x.com/rauchg/status/1980441285506052267
互动: Likes: 18; Retweets: 0; Replies: 2; Quotes: 0; Views: 1,799; Bookmarks: 0; isReply: 1

@ImHermes_ @nextjs We've been in communication non-stop (via our status page, official channels, and myself on X). We're working on post-mortem comms and more official messages around the clock. Curious what piece of the puzzle you're missing. Apologies for the disruption 🫤

我们一直保持不间断的沟通（通过状态页面、官方渠道，以及我本人在 X 上的更新）。团队正在日夜赶工，准备详细的事故报告和更正式的公告。想知道您还有哪些地方不太清楚？对于此次服务中断，我们深感抱歉 🫤

### 680

作者: @Guillermo-Rauch
时间: 2025-10-21
链接: https://x.com/rauchg/status/1980499387873919086
互动: Likes: 3; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,292; Bookmarks: 0; isReply: 1

@birch_js It’s fast!

@birch_js 速度真快！

### 681

作者: @Guillermo-Rauch
时间: 2025-10-21
链接: https://x.com/rauchg/status/1980632841055825940
互动: Likes: 1,378; Retweets: 201; Replies: 105; Quotes: 32; Views: 170,162; Bookmarks: 188; isReply: 0

The long way is actually the shortcut

看似绕远的路，往往是真正的捷径。

### 682

作者: @Guillermo-Rauch
时间: 2025-10-21
链接: https://x.com/rauchg/status/1980642558402523163
互动: Likes: 575; Retweets: 42; Replies: 44; Quotes: 8; Views: 42,361; Bookmarks: 31; isReply: 0

Me every day https://t.co/Y6C8BxuPTh

我的日常 https://t.co/Y6C8BxuPTh

### 683

作者: @Guillermo-Rauch
时间: 2025-10-21
链接: https://x.com/rauchg/status/1980699518657261970
互动: Likes: 558; Retweets: 21; Replies: 44; Quotes: 11; Views: 83,175; Bookmarks: 226; isReply: 0

Using ChatGPT Atlas to 'find domain ideas for my IoT mattress startup' on https://t.co/YIforiRlgo. Both the agent and the site are so fast that this is actually a surprisingly good experience https://t.co/GJPIlAMiTV

我在 https://t.co/YIforiRlgo 上使用 ChatGPT Atlas 为我的物联网（IoT）床垫创业公司寻找业务领域创意。这个 AI 智能体（AI Agent）和网站的速度都非常快，整体体验出乎意料地流畅。https://t.co/GJPIlAMiTV

### 684

作者: @Guillermo-Rauch
时间: 2025-10-21
链接: https://x.com/rauchg/status/1980700833840001185
互动: Likes: 8; Retweets: 0; Replies: 1; Quotes: 1; Views: 8,339; Bookmarks: 7; isReply: 1

@goutham_kamath @PrayagBhakar @eightsleep I wouldn't mind vibration and dramatic music feature for SEV0 😂 https://t.co/dt3icJgIU3 integration

@goutham_kamath @PrayagBhakar @eightsleep 要是给 SEV0 配上振动和震撼音效，我也不介意啊 😂 集成链接：https://t.co/dt3icJgIU3

### 685

作者: @Guillermo-Rauch
时间: 2025-10-21
链接: https://x.com/rauchg/status/1980707097059946587
互动: Likes: 84; Retweets: 1; Replies: 9; Quotes: 2; Views: 13,078; Bookmarks: 22; isReply: 1

I had ChatGPT Atlas build me a 'minimalistic website for my IoT mattress startup' using @v0. (It wrote a nice prompt and v0 did the rest 😅) https://t.co/f6fvuf2owZ

我请 ChatGPT Atlas 用 @v0 帮我做了一个「为我的物联网（IoT）床垫创业公司打造的极简风格网站」。（它负责生成了一段很棒的提示词，剩下的就交给 v0 搞定了 😅）https://t.co/f6fvuf2owZ

### 686

作者: @Guillermo-Rauch
时间: 2025-10-21
链接: https://x.com/rauchg/status/1980715524515631193
互动: Likes: 0; Retweets: 0; Replies: 1; Quotes: 0; Views: 129; Bookmarks: 0; isReply: 1

@manishrc @RhysSullivan i love domain hacks but no the pathname kind

@manishrc @RhysSullivan 我喜欢域名巧用（Domain Hacks），但不是指那种带路径的。

### 687

作者: @Guillermo-Rauch
时间: 2025-10-21
链接: https://x.com/rauchg/status/1980784546036740258
互动: Likes: 349; Retweets: 18; Replies: 20; Quotes: 4; Views: 73,627; Bookmarks: 222; isReply: 0

We've written up our initial report of yesterday's us-east-1 outage. 

The "life of a request" section gives you the POV of a single request traveling across the globe through our network, CDN, routing, caching, and compute infrastructure, detailing what failed and what worked. https://t.co/XWVDOn3m2t

我们已就昨天 us-east-1 区域的服务中断完成了初步报告。

报告中的「一个请求的生命周期」部分，会带您跟随一个单一请求的视角，看它如何环游世界，穿越我们的网络、内容分发网络（CDN）、路由、缓存和计算基础设施，并详细揭示其中哪些环节出了故障，哪些环节依然工作正常。https://t.co/XWVDOn3m2t

### 688

作者: @Guillermo-Rauch
时间: 2025-10-22
链接: https://x.com/rauchg/status/1980795600594694323
互动: Likes: 1,212; Retweets: 58; Replies: 24; Quotes: 3; Views: 122,316; Bookmarks: 459; isReply: 0

📱 Next.js 🤝 React Native &amp; Expo

📱 Next.js 与 React Native & Expo 携手

### 689

作者: @Guillermo-Rauch
时间: 2025-10-22
链接: https://x.com/rauchg/status/1980807255709847909
互动: Likes: 8; Retweets: 0; Replies: 1; Quotes: 0; Views: 688; Bookmarks: 0; isReply: 1

@bmdavis419 @hernan_yadiel pages/ has ~zero overhead over app/ and vice-versa (unless using both, v uncommon)

It’s like saying React has the “bloat” of supporting class components. Backwards compatibility is a good trait actually. That’s like, how the web and JavaScript work.

@bmdavis419 @hernan_yadiel pages/ 目录的开销相比 app/ 几乎可以忽略不计，反过来也一样（除非两者混用，但这很少见）。

这就好比有人说 React 支持类组件是一种「累赘」。其实，向后兼容是个优点。这本来就是网络和 JavaScript 的常态。

### 690

作者: @Guillermo-Rauch
时间: 2025-10-22
链接: https://x.com/rauchg/status/1980824638222660051
互动: Likes: 1; Retweets: 0; Replies: 0; Quotes: 0; Views: 270; Bookmarks: 0; isReply: 1

@marcusotsuji Down

@marcusotsuji 已赞 / 支持

### 691

作者: @Guillermo-Rauch
时间: 2025-10-22
链接: https://x.com/rauchg/status/1980988944604086385
互动: Likes: 976; Retweets: 32; Replies: 149; Quotes: 21; Views: 82,428; Bookmarks: 21; isReply: 0

Next.js

Next.js

### 692

作者: @Guillermo-Rauch
时间: 2025-10-22
链接: https://x.com/rauchg/status/1980993978112868794
互动: Likes: 23; Retweets: 0; Replies: 2; Quotes: 0; Views: 4,378; Bookmarks: 1; isReply: 1

@peturgeorgievv Taking a look

@peturgeorgievv 我来看看

### 693

作者: @Guillermo-Rauch
时间: 2025-10-22
链接: https://x.com/rauchg/status/1980995500246696129
互动: Likes: 7; Retweets: 0; Replies: 2; Quotes: 0; Views: 5,282; Bookmarks: 0; isReply: 1

@_VladanIlic Nice name 😁

@_VladanIlic 名字不错嘛 😁

### 694

作者: @Guillermo-Rauch
时间: 2025-10-22
链接: https://x.com/rauchg/status/1980997444520591396
互动: Likes: 4; Retweets: 0; Replies: 1; Quotes: 0; Views: 362; Bookmarks: 1; isReply: 1

@peturgeorgievv Reading up on the logs, the Chrome team that was maintaining these was disbanded “to focus on AI initiatives.”

We need to figure out how to get someone from GTM in the loop so we can make sound updates and decisions

Meantime tagging @_ijjk to take a look at this one

@peturgeorgievv 根据日志记录来看，原先负责维护这些内容的 Chrome 团队已经解散，以便「集中精力推进 AI 项目」。

我们需要设法让 GTM（Go-to-Market）的同事也参与进来，这样我们才能做出稳妥的更新和决策。

同时，也请 @_ijjk 看一下这个情况。

### 695

作者: @Guillermo-Rauch
时间: 2025-10-22
链接: https://x.com/rauchg/status/1980999205176201625
互动: Likes: 5; Retweets: 0; Replies: 1; Quotes: 0; Views: 4,585; Bookmarks: 0; isReply: 1

@ggofri Subsequent could be a cool project name fr 😆

@ggofri「Subsequent」没准儿会是个超酷的项目名，真的 😆

### 696

作者: @Guillermo-Rauch
时间: 2025-10-22
链接: https://x.com/rauchg/status/1981006172649083335
互动: Likes: 3; Retweets: 0; Replies: 0; Quotes: 0; Views: 159; Bookmarks: 0; isReply: 1

@BurnedChris @peturgeorgievv Love this

@BurnedChris @peturgeorgievv 太棒了！

### 697

作者: @Guillermo-Rauch
时间: 2025-10-22
链接: https://x.com/rauchg/status/1981006592926711989
互动: Likes: 0; Retweets: 0; Replies: 1; Quotes: 0; Views: 93; Bookmarks: 0; isReply: 1

@KunchamSathwik @saltcod @vercel @v0 Mind sending us the generation link so we can take a look?

@KunchamSathwik @saltcod @vercel @v0 方便把生成结果的链接发我们看看吗？

### 698

作者: @Guillermo-Rauch
时间: 2025-10-22
链接: https://x.com/rauchg/status/1981007432701907013
互动: Likes: 18; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,699; Bookmarks: 1; isReply: 1

@adityasm_x npx create-next-app --previous would be sick 😆

@adityasm_x 用 `npx create-next-app --previous` 这个命令应该会很爽 😆

### 699

作者: @Guillermo-Rauch
时间: 2025-10-22
链接: https://x.com/rauchg/status/1981017032574607677
互动: Likes: 201; Retweets: 13; Replies: 18; Quotes: 2; Views: 17,931; Bookmarks: 16; isReply: 0

Tune in for some good news for devs, ecosystem, and even LLMs 😉 
https://t.co/gcie7dOgiH

开发者、开发生态，甚至是大语言模型（LLM）都有好消息，敬请期待 😉
https://t.co/gcie7dOgiH

### 700

作者: @Guillermo-Rauch
时间: 2025-10-22
链接: https://x.com/rauchg/status/1981037270624076092
互动: Likes: 563; Retweets: 37; Replies: 47; Quotes: 17; Views: 64,495; Bookmarks: 224; isReply: 0

Frameworks are only as good as the LLM's and agents' ability to wield them.

Today we're announcing https://t.co/aporqgINxP, open-source "exams" for the AIs to pass and get trained on. Excited for open and closed models to compete.

The best part: we'll ship evals for other open source projects we support like @nuxt_js, @sveltejs, @turborepo, @aisdk, and the rest of the ecosystem.

I believe this can significantly impact the future of open source and open models. If you're interested in joining this effort, let me know!

一个框架是否出色，完全取决于大语言模型和 AI 智能体驾驭它的能力。

今天，我们正式推出 https://t.co/aporqgINxP，这是一套开源的 AI「考题」，旨在让 AI 进行测试和训练。我们非常期待开源模型与闭源模型在这些测试中同台竞技。

最精彩的部分在于：我们还将为我们支持的其他开源项目发布评估套件，例如 @nuxt_js，@sveltejs，@turborepo，@aisdk 以及整个生态中的其他成员。

我相信，这将对开源软件和开源模型的未来产生深远影响。如果你对此感兴趣并愿意贡献力量，请随时联系我！

### 701

作者: @Guillermo-Rauch
时间: 2025-10-22
链接: https://x.com/rauchg/status/1981043344580235695
互动: Likes: 309; Retweets: 1; Replies: 15; Quotes: 2; Views: 42,293; Bookmarks: 6; isReply: 1

@v0 @grok is this real

@v0 @grok 这是真的吗？

### 702

作者: @Guillermo-Rauch
时间: 2025-10-22
链接: https://x.com/rauchg/status/1981059147346169937
互动: Likes: 566; Retweets: 23; Replies: 28; Quotes: 8; Views: 39,451; Bookmarks: 36; isReply: 0

Next.js 16 is good. I think it’s going to age like a Cheval Blanc 1947.

Extreme gratitude to the @nextjs &amp; Turbopack teams, and the broader ecosystem, including @reactjs and all the partners whose feedback culminated in Deployment Adapters.

https://t.co/g0gxwJh16N

Next.js 16 非常棒。我认为它会像 1947 年的白马酒庄（Cheval Blanc）佳酿一样，历久弥香。

衷心感谢 @nextjs 和 Turbopack 团队，以及更广阔的生态系统，包括 @reactjs 和所有合作伙伴，正是大家的反馈汇集，最终催生了部署适配器（Deployment Adapters）。

https://t.co/g0gxwJh16N

### 703

作者: @Guillermo-Rauch
时间: 2025-10-22
链接: https://x.com/rauchg/status/1981077563725533472
互动: Likes: 323; Retweets: 8; Replies: 15; Quotes: 2; Views: 55,267; Bookmarks: 27; isReply: 0

Webpack:
○ single-core

Turbopack:
◉◉◉◉◉◉◉◉ multi-core

Turbopack production builds get faster with the size of your build machine. So @vercel how gives you turbo build machines ⚡️

Webpack:
○ 单核

Turbopack:
◉◉◉◉◉◉◉◉ 多核

Turbopack 的生产版本构建速度会随着你构建服务器的核心数量增加而提升。因此，@vercel 为你提供了 Turbo 构建实例 ⚡️

### 704

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981154341777265128
互动: Likes: 6; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,685; Bookmarks: 0; isReply: 1

@bnj @designertom_ @TukiFromKL Credit to @martunalong hehe

@bnj @designertom_ @TukiFromKL 功劳归 @martunalong 哈哈

### 705

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981154650880688486
互动: Likes: 4; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,611; Bookmarks: 0; isReply: 1

@bnj @designertom_ @TukiFromKL @martunalong Congrats you guys on the TBPN feature too 😁

@bnj @designertom_ @TukiFromKL @martunalong 也恭喜你们获得了 TBPN 功能 😁

### 706

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981154926681321525
互动: Likes: 1; Retweets: 0; Replies: 0; Quotes: 0; Views: 176; Bookmarks: 1; isReply: 1

@eter_inquirer @m_franceschetti Ez https://t.co/dt3icJgIU3 → sev0/1 webhook → eightsleep api

@eter_inquirer @m_franceschetti 很简单：访问 https://t.co/dt3icJgIU3 -> 配置 sev0/1 的 Webhook -> 连接 Eight Sleep API。

### 707

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981336979871846601
互动: Likes: 6; Retweets: 0; Replies: 2; Quotes: 0; Views: 768; Bookmarks: 7; isReply: 1

You should try out our products built with the app router. https://t.co/kU6hfG6iGt https://t.co/gA0Xy5pjJV https://t.co/NOIfpQhs3W https://t.co/C2q4ESzL6K. Docs do talk about optimistic updates and we frequently implement them. 

We should probably start talking about product things you want to accomplish. All the tools are there.

The nice thing about Next is that it’s backing real world products and it’s not theoretical.

不妨试试我们基于 App Router 构建的产品。https://t.co/kU6hfG6iGt https://t.co/gA0Xy5pjJV https://t.co/NOIfpQhs3W https://t.co/C2q4ESzL6K。文档中确实提到了乐观更新（Optimistic Updates），我们也经常在实践中应用它。

我们或许可以开始聊聊你想要实现哪些产品目标。所需的工具都已准备就绪。

Next 的一大优势在于，它有真实的产品作为支撑，而非纸上谈兵。

### 708

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981369081724096535
互动: Likes: 18; Retweets: 0; Replies: 2; Quotes: 0; Views: 1,936; Bookmarks: 0; isReply: 1

@Delmo_dev My twin

我的双胞胎兄弟 / 姐妹（根据上下文）

### 709

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981394075552288921
互动: Likes: 449; Retweets: 15; Replies: 40; Quotes: 9; Views: 26,225; Bookmarks: 22; isReply: 0

The ultimate agent loop https://t.co/9NXCWh2sMH

智能体的核心循环 https://t.co/9NXCWh2sMH

### 710

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981397061405987069
互动: Likes: 118; Retweets: 3; Replies: 6; Quotes: 0; Views: 20,683; Bookmarks: 23; isReply: 0

Humans shouldering the burden of every alert and failure is a thing of the past.

Every anomaly on Vercel’s AI cloud is now investigated by our agent. Incident response will never look the same https://t.co/MJRYrvUpE5

由人类来承担每一个警报和故障处理负担的时代，已经结束了。

如今，Vercel 人工智能云（AI Cloud）上的每一个异常，都由我们的 AI 智能体自动调查。事件响应的方式，从此将彻底改变。https://t.co/MJRYrvUpE5

### 711

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981397691671466064
互动: Likes: 264; Retweets: 10; Replies: 18; Quotes: 4; Views: 55,437; Bookmarks: 27; isReply: 0

Vercel is the Vercel for Python

（对于 Python 领域而言，）它就像 Vercel 一样。

### 712

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981401018320769405
互动: Likes: 881; Retweets: 36; Replies: 79; Quotes: 27; Views: 299,265; Bookmarks: 687; isReply: 0

The “React of the backend”.

It’s hard to put into words how many backend, queue, microservice, Kafka, SQS, and other complexities this removes.

And you just learned it on this tweet… "𝚞𝚜𝚎 𝚠𝚘𝚛𝚔𝚏𝚕𝚘𝚠" + "𝚞𝚜𝚎 𝚜𝚝𝚎𝚙" is all you need. Just https://t.co/tOVJiPK51X

堪称「后端领域的 React」。

简直难以言表，这省去了多少后端、队列、微服务、Kafka、SQS 以及其他方面的复杂性。

而你，仅仅通过这条推文就掌握了精髓…… 你只需要「𝚞𝚜𝚎 𝚠𝚘𝚛𝚔𝚏𝚕𝚘𝚠」+「𝚞𝚜𝚎 𝚜𝚝𝚎𝚙」这两句指令。详情请见：https://t.co/tOVJiPK51X

### 713

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981402936355016861
互动: Likes: 38; Retweets: 0; Replies: 7; Quotes: 1; Views: 15,014; Bookmarks: 10; isReply: 1

@chribjel To remove the complexity of microservices and to enforce the right semantics for determinism &amp; resumption (with good DX!) we need compiler cooperation

The nice thing is the compiler is super simple and framework-agnostic. Works with Next, Nitro, Hono &amp; more to come. Even Python!

@chribjel 为了消除微服务的复杂性，并确保确定性（Determinism）与执行状态恢复（Resumption）具有正确的语义（同时提供优秀的开发者体验（DX）），我们需要编译器的协同工作。

令人欣慰的是，这款编译器极其简单，且与框架无关。它能够与 Next、Nitro、Hono 及更多其他框架协同工作。甚至连 Python 也不例外！

### 714

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981404928519340277
互动: Likes: 214; Retweets: 17; Replies: 23; Quotes: 4; Views: 42,715; Bookmarks: 69; isReply: 0

We’re not building the AI Cloud alone.

In 2 clicks, get an Agent-as-a-Service like @coderabbitai, or infra services like @onkernel browsers for agents you build yourself.

If you’re building AI services and want to reach millions of devs and over 100,000+ paying teams, reach out

我们并非在孤军奋战地构建 AI 云平台。

只需点击两下，您就能获得类似 @coderabbitai 的 AI 智能体即服务（Agent-as-a-Service），或是像 @onkernel 这样为您自建智能体提供的基础设施服务（如浏览器环境）。

如果您正在开发 AI 服务，并希望触达数百万开发者以及超过 10 万个付费团队，欢迎与我们联系。

### 715

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981417027526152386
互动: Likes: 1,393; Retweets: 41; Replies: 139; Quotes: 65; Views: 335,911; Bookmarks: 552; isReply: 0

This is real life 🧵

𝚊𝚜𝚢𝚗𝚌 𝚏𝚞𝚗𝚌𝚝𝚒𝚘𝚗 𝚜𝚒𝚐𝚗𝚞𝚙(𝚎𝚖𝚊𝚒𝚕) {
  "𝚞𝚜𝚎 𝚠𝚘𝚛𝚔𝚏𝚕𝚘𝚠";

  𝚊𝚠𝚊𝚒𝚝 𝚌𝚛𝚎𝚊𝚝𝚎𝚄𝚜𝚎𝚛(𝚎𝚖𝚊𝚒𝚕);
  𝚊𝚠𝚊𝚒𝚝 𝚜𝚎𝚗𝚍𝚆𝚎𝚕𝚌𝚘𝚖𝚎𝙴𝚖𝚊𝚒𝚕(𝚎𝚖𝚊𝚒𝚕);

  // 🤯
  𝚊𝚠𝚊𝚒𝚝 𝚜𝚕𝚎𝚎𝚙("7 𝚍𝚊𝚢𝚜");
  𝚊𝚠𝚊𝚒𝚝 𝚜𝚎𝚗𝚍𝙲𝚑𝚎𝚌𝚔𝙸𝚗𝙴𝚖𝚊𝚒𝚕(𝚎𝚖𝚊𝚒𝚕);
}

现实生活写照 🧵

```javascript
async function signup（email）{
「use workflow";

 await createUser（email);
 await sendWelcomeEmail（email);

 // 🤯
 await sleep（"7 days");
 await sendCheckInEmail（email);
}
```

### 716

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981417030847963189
互动: Likes: 90; Retweets: 0; Replies: 4; Quotes: 0; Views: 42,496; Bookmarks: 10; isReply: 1

Last but not least, scheduling. 𝚜𝚕𝚎𝚎𝚙 is a helper provided by the Workflow Development Kit:

𝚒𝚖𝚙𝚘𝚛𝚝 { 𝚜𝚕𝚎𝚎𝚙 } 𝚏𝚛𝚘𝚖 "𝚠𝚘𝚛𝚔𝚏𝚕𝚘𝚠";

By calling it in your workflow, you can succinctly express computation … from the future.

最后一点，关于调度。`sleep` 是工作流开发套件提供的一个辅助工具：

`import {sleep} from"workflow";`

在你的工作流中调用它，就能以一种简洁的方式来安排未来要执行的计算任务。

### 717

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981417029208068586
互动: Likes: 87; Retweets: 0; Replies: 1; Quotes: 1; Views: 50,249; Bookmarks: 12; isReply: 1

There’s so much goodness going on in that little function.

𝚜𝚎𝚗𝚍𝚆𝚎𝚕𝚌𝚘𝚖𝚎𝙴𝚖𝚊𝚒𝚕 itself is a reliable step. If the process or server or network died after 𝚌𝚛𝚎𝚊𝚝𝚎𝚄𝚜𝚎𝚛, the workflow would resume from that point.

𝚏𝚞𝚗𝚌𝚝𝚒𝚘𝚗 𝚜𝚎𝚗𝚍𝚆𝚎𝚕𝚌𝚘𝚖𝚎𝙴𝚖𝚊𝚒𝚕(…) {
  "𝚞𝚜𝚎 𝚜𝚝𝚎𝚙";

  𝚊𝚠𝚊𝚒𝚝 𝚛𝚎𝚜𝚎𝚗𝚍.𝚎𝚖𝚊𝚒𝚕𝚜.𝚜𝚎𝚗𝚍({
    // …
  }
}

这个小函数的设计着实精妙。

`sendWelcomeEmail` 本身是一个具备容错能力的步骤。如果在 `createUser` 操作之后进程、服务器或网络崩溃了，整个工作流将会从这个步骤开始自动恢复执行。

```javascript
function sendWelcomeEmail（...）{
「use step";

 await resend.emails.send（{//...}
}
```

### 718

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981418045903163810
互动: Likes: 36; Retweets: 0; Replies: 3; Quotes: 0; Views: 18,820; Bookmarks: 0; isReply: 1

@_fqnn_ It already works self-hosted, with more providers in the works

@_fqnn_ 它已经支持自托管了，而且还有更多服务提供商正在接入中。

### 719

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981421313505022402
互动: Likes: 10; Retweets: 0; Replies: 3; Quotes: 0; Views: 4,664; Bookmarks: 2; isReply: 1

@laander1901 Directives have precedence in “use strict” and are foundational to the JS runtime ecosystem. Not scary!

@laander1901 在「use strict」中，指令具有更高的优先级，并且是 JavaScript 运行时生态的基石。没什么好怕的！

### 720

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981421946798821509
互动: Likes: 5; Retweets: 0; Replies: 2; Quotes: 0; Views: 7,749; Bookmarks: 0; isReply: 1

@_maxscn Most likely you’ll find yourself wanting functions that are both steps and normal functions. No need to deduplicate. You can just call them.

@_maxscn 你很可能会有这样的需求：某些函数既作为独立步骤使用，又是普通的工具函数。这完全没问题，无需特意去重写或区分，直接调用即可。

### 721

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981423262262612226
互动: Likes: 5; Retweets: 0; Replies: 1; Quotes: 0; Views: 988; Bookmarks: 1; isReply: 1

@_maxscn It won’t let you call normal async functions from the main workflow function 😉 Because the async yield points are the serializable enqueuing boundaries.

@_maxscn 主工作流函数不允许调用普通的异步函数哦 😉 这是因为那些异步的 yield 点（即工作流暂停点）构成了可序列化的任务入队边界。

### 722

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981423416864624726
互动: Likes: 76; Retweets: 0; Replies: 1; Quotes: 1; Views: 23,070; Bookmarks: 1; isReply: 1

@dolevkle 💯 and design decisions. Great prompt. “You’re absolutely right.” We’ll cook.

@dolevkle 💯（满分）以及设计决策。这个提示太棒了。「你说得完全正确。」我们稳了。/ 我们能成。

### 723

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981423695894892894
互动: Likes: 5; Retweets: 0; Replies: 0; Quotes: 0; Views: 2,956; Bookmarks: 1; isReply: 1

@sa_han47 Yes. You’ll be responsible for the runtime and hosting a database for it but should work great

是的。你需要负责运行环境，并为其托管数据库，不过运行起来应该会很顺利。

### 724

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981423911444307993
互动: Likes: 346; Retweets: 14; Replies: 12; Quotes: 1; Views: 34,765; Bookmarks: 94; isReply: 0

work-flow balance, at last https://t.co/66NKDYmATX

工作流程总算平衡了，最后附上链接：https://t.co/66NKDYmATX

### 725

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981426366982824387
互动: Likes: 243; Retweets: 8; Replies: 31; Quotes: 13; Views: 74,256; Bookmarks: 77; isReply: 1

You can 

𝚊𝚜𝚢𝚗𝚌 𝚏𝚞𝚗𝚌𝚝𝚒𝚘𝚗 𝚍𝚊𝚒𝚕𝚢() {
  "𝚞𝚜𝚎 𝚠𝚘𝚛𝚔𝚏𝚕𝚘𝚠";
  𝚠𝚑𝚒𝚕𝚎 (𝚝𝚛𝚞𝚎) {
    𝚊𝚠𝚊𝚒𝚝 𝚜𝚕𝚎𝚎𝚙("1 𝚍𝚊𝚢");
    𝚊𝚠𝚊𝚒𝚝 𝚢𝚘𝚞𝚛𝚃𝚑𝚒𝚗𝚐();
  }
}

It’s wild how robust the model is. It seems magical but it’s ackchually super consistent

That said, we will make the cron use case nicer. You can also drop the second 𝚊𝚠𝚊𝚒𝚝 to adjust the periodicity and not let the duration of 𝚢𝚘𝚞𝚛𝚃𝚑𝚒𝚗𝚐 influence the time of the day the job starts at.

你可以这样写：

异步函数 daily（）{
「use workflow"; // 使用工作流
 while（true）{await sleep（"1 天");
  await yourThing（);}
}

这个模型的健壮性简直离谱。看起来像魔法，但实际上（ackchually）超级稳定。

不过，我们会进一步优化这种类似 cron 定时任务的使用场景。你也可以省略第二个 `await`，来调整任务的周期频率，这样就不会让 `yourThing（)` 函数执行所需的时间，影响到该任务每天具体的启动时刻了。

### 726

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981427368242925942
互动: Likes: 401; Retweets: 5; Replies: 40; Quotes: 1; Views: 35,910; Bookmarks: 38; isReply: 0

Some of my kids came to the conf 😁 
Get your own at Ship AI Photo Booth! https://t.co/Zzq1P3R9kr

我的几个小伙伴也来大会啦 😁
快来 Ship AI 照片亭，生成你的专属照片吧！https://t.co/Zzq1P3R9kr

### 727

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981436089463427499
互动: Likes: 7; Retweets: 0; Replies: 0; Quotes: 0; Views: 180; Bookmarks: 0; isReply: 1

@mixedbreadai @vercel Welcome! Time to cook on the fastest, highest-quality AI search experiences together 😁

@mixedbreadai @vercel 欢迎！是时候一起打造最快、最高质量的 AI 搜索体验了，让我们大干一场吧！😁

### 728

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981442229458915523
互动: Likes: 7; Retweets: 0; Replies: 3; Quotes: 0; Views: 3,444; Bookmarks: 0; isReply: 1

@meabed @_fqnn_ Call start() to run that workflow once, and it’ll run forever. It’ll sleep for 24 hours and then re-enqueue yourThing()

@meabed @_fqnn_ 调用 start（）来执行该工作流一次，之后它便会一直运行。它会先休眠 24 小时，然后重新排队执行 yourThing（）。

### 729

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981445346221052240
互动: Likes: 1; Retweets: 0; Replies: 1; Quotes: 0; Views: 109; Bookmarks: 0; isReply: 1

@pascowebdesigns Sick

@pascowebdesigns 太酷了！

### 730

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981453998252314939
互动: Likes: 29; Retweets: 0; Replies: 2; Quotes: 0; Views: 3,300; Bookmarks: 0; isReply: 1

@dolevkle lol I mean that it’s a great idea to blog about the design and decisions. We’ll follow up

@dolevkle 哈哈，我是说把设计和决策过程写成博客真是个绝佳的主意。我们会持续关注的。

### 731

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981457322338881570
互动: Likes: 8; Retweets: 0; Replies: 1; Quotes: 0; Views: 721; Bookmarks: 0; isReply: 1

@ken_wheeler @MelkeyDev “use freedom”

@ken_wheeler @MelkeyDev「use freedom」

### 732

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981466366927573322
互动: Likes: 247; Retweets: 5; Replies: 23; Quotes: 3; Views: 91,536; Bookmarks: 99; isReply: 0

This is funny but also spot-on. 

Developers have typically been able to “ship anything” in modern organizations, especially relative to their go-to-market (sales & marketing) counterparts.

Except for, paradoxically, workflows. I’d argue a non-dev can run laps around an engineer in shipping complex pipelines involving data and integrations across multiple systems.

Until now. "𝚞𝚜𝚎 𝚠𝚘𝚛𝚔𝚏𝚕𝚘𝚠" truly changes the game. Reliability meets ergonomics. This might just be one of the most important open source projects we’ve ever worked on, and it’ll benefit the entire ecosystem whether you use @vercel or not. Kudos @pranaygp

这说法很有趣，但也确实切中要害。

在现代企业里，开发者通常拥有「交付一切」的能力，尤其是相较于他们的市场推广（销售与营销）同事而言。

但矛盾的是，工作流（workflow）却是个例外。我认为，在部署那些涉及多系统数据和集成的复杂管道（pipeline）时，非开发人员甚至能比工程师快上好几拍。

直到现在。「𝚞𝚜𝚎 𝚠𝚘𝚛𝚔𝚏𝚕𝚘𝚠」真正改变了游戏规则。它实现了可靠性与开发者体验的融合。这很可能将成为我们迄今所参与过的最重要的开源项目之一，无论你是否使用 @vercel，整个生态系统都将从中受益。向 @pranaygp 致敬！

### 733

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981473095262281958
互动: Likes: 0; Retweets: 0; Replies: 0; Quotes: 0; Views: 639; Bookmarks: 0; isReply: 1

@laander1901 The good thing is that there’s common infrastructure on top of which we can create lots of API expressions. I think lots of people will enjoy this one and others can be built too

@laander1901 好在有一个通用的基础设施，我们可以基于它构建出各种各样的 API 功能。我想很多人会喜欢这个（现有的）功能，而且基于它还能开发出更多其他的功能。

### 734

作者: @Guillermo-Rauch
时间: 2025-10-23
链接: https://x.com/rauchg/status/1981475332948709541
互动: Likes: 4; Retweets: 0; Replies: 0; Quotes: 0; Views: 331; Bookmarks: 0; isReply: 1

@TooTallNate Damn. Incredible

@TooTallNate 哇，太牛了。

### 735

作者: @Guillermo-Rauch
时间: 2025-10-24
链接: https://x.com/rauchg/status/1981563541825212680
互动: Likes: 9; Retweets: 0; Replies: 2; Quotes: 0; Views: 5,763; Bookmarks: 2; isReply: 1

@XLoeraFlores It’s very efficient especially because of Fluid compute!

@XLoeraFlores 它的效率非常高，这尤其要归功于 Fluid Compute 技术！

### 736

作者: @Guillermo-Rauch
时间: 2025-10-24
链接: https://x.com/rauchg/status/1981567268103598452
互动: Likes: 1,829; Retweets: 65; Replies: 88; Quotes: 11; Views: 112,754; Bookmarks: 586; isReply: 0

fully generated w/ veo 3.1
https://t.co/kUiLwdLel0

使用 veo 3.1 完全生成
https://t.co/kUiLwdLel0

### 737

作者: @Guillermo-Rauch
时间: 2025-10-24
链接: https://x.com/rauchg/status/1981760120750231627
互动: Likes: 1; Retweets: 0; Replies: 1; Quotes: 0; Views: 29; Bookmarks: 0; isReply: 1

@tomsiwik yes. Falconry class in Big Sur, CA

是的。在加州大苏尔有一个驯鹰课程。

### 738

作者: @Guillermo-Rauch
时间: 2025-10-24
链接: https://x.com/rauchg/status/1981760776173130156
互动: Likes: 1; Retweets: 0; Replies: 1; Quotes: 0; Views: 97; Bookmarks: 0; isReply: 1

@tomsiwik Super chill. The peregrine falcon was freaking out though

@tomsiwik 我这边超级淡定。倒是那只游隼，慌得不行。

### 739

作者: @Guillermo-Rauch
时间: 2025-10-24
链接: https://x.com/rauchg/status/1981834532212166737
互动: Likes: 84; Retweets: 0; Replies: 3; Quotes: 0; Views: 5,014; Bookmarks: 0; isReply: 1

@ianhildy Yes, or “Ignore all” for this category of notification button. Thx for the nudge!

是的，或者这类通知按钮可以设成「全部忽略」。多谢提醒！

### 740

作者: @Guillermo-Rauch
时间: 2025-10-24
链接: https://x.com/rauchg/status/1981839620431393157
互动: Likes: 5; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,862; Bookmarks: 0; isReply: 1

@stressandvest Brilliant

@stressandvest 太棒了

### 741

作者: @Guillermo-Rauch
时间: 2025-10-24
链接: https://x.com/rauchg/status/1981850740453974402
互动: Likes: 216; Retweets: 8; Replies: 34; Quotes: 2; Views: 39,771; Bookmarks: 42; isReply: 0

I can’t think of a better tool to start learning how to ship than @v0

要开始学习如何发布产品，我想不出比 @v0 更好的入门工具了。

### 742

作者: @Guillermo-Rauch
时间: 2025-10-24
链接: https://x.com/rauchg/status/1981862859731792218
互动: Likes: 7; Retweets: 0; Replies: 4; Quotes: 1; Views: 1,653; Bookmarks: 2; isReply: 1

@pucchkaa Practically, yes. Instead of manually creating, populating, and subscribing to queues, most of the time you’ll be writing workflows.

Technically, no. This builds on top of queuing primitives.

从实践角度讲，确实如此。在大多数情况下，您需要编写的是工作流，而非手动去创建、填充和订阅队列。

但从技术原理上看，则并非如此。这些工作流的功能，是构建在队列原语（queuing primitives）之上的。

### 743

作者: @Guillermo-Rauch
时间: 2025-10-24
链接: https://x.com/rauchg/status/1981864471045005410
互动: Likes: 26; Retweets: 0; Replies: 1; Quotes: 0; Views: 10,408; Bookmarks: 2; isReply: 1

@pqoqubbw @vercel Curious what the error for this looks like with Turbopack?

@pqoqubbw @vercel 想看看这个错误在 Turbopack 里长什么样？

### 744

作者: @Guillermo-Rauch
时间: 2025-10-24
链接: https://x.com/rauchg/status/1981872287919034688
互动: Likes: 17; Retweets: 0; Replies: 2; Quotes: 0; Views: 2,834; Bookmarks: 1; isReply: 1

@linuz90 @typefully It’s so good!

@linuz90 @typefully 太棒了！

### 745

作者: @Guillermo-Rauch
时间: 2025-10-25
链接: https://x.com/rauchg/status/1981893276178506029
互动: Likes: 242; Retweets: 8; Replies: 15; Quotes: 3; Views: 36,799; Bookmarks: 18; isReply: 0

▲ 🤝 🇰🇷 

It was an honor to host Ally Kim and the team from GS Holdings yesterday at our inaugural Ship AI conference and announce our strategic partnership.

GS has chosen @v0 to power their AI transformation across 36,000 employees and integrate the v0 Platform API with their internal MISO platform.

The goal is to use v0 to generate production-grade apps that solve real-world problems. During a recent hackathon, over 250 ideas were explored, and 20 use cases are now live in the field (including a Biomass Chemical Dispatch System)

▲ 🤝 🇰🇷

昨天，在我们的首届 Ship AI 大会上，我们非常荣幸地接待了 Ally Kim 和 GS Holdings 的团队，并共同宣布了双方的战略合作伙伴关系。

GS 集团已选择 @v0 作为其 AI 转型的核心引擎，服务于旗下 36,000 名员工，并将 v0 平台 API 深度集成到其内部的 MISO 平台中。

此举旨在利用 v0 快速生成能够解决实际业务问题的、可直接投入使用的应用程序。在近期的一次内部黑客马拉松活动中，团队探索了超过 250 个创意想法，目前已有 20 个用例成功落地并投入实际使用（其中包括一个生物质化学调度系统）。

### 746

作者: @Guillermo-Rauch
时间: 2025-10-25
链接: https://x.com/rauchg/status/1981898975499505913
互动: Likes: 2; Retweets: 0; Replies: 0; Quotes: 0; Views: 169; Bookmarks: 0; isReply: 1

@_hannahahn @annietma We’ll record an ep next time

我们下次录一集。

### 747

作者: @Guillermo-Rauch
时间: 2025-10-25
链接: https://x.com/rauchg/status/1981941067550208496
互动: Likes: 54; Retweets: 0; Replies: 2; Quotes: 0; Views: 8,021; Bookmarks: 2; isReply: 1

@colinhacks It’s more so about giving people examples of how to integrate the workflow toolkit. 

It should probably say Svelte𝑲𝒊𝒕. And while Bun is a runtime, it also comes with framework primitives unlike Node.

Nitro can be used standalone to power an api server, so it’s a good fit.

@colinhacks 这主要是想给大家展示一下，如何将工作流工具包集成到项目中。

这里提到的工具可能更适合叫 Svelte𝑲𝒊𝒕。另外，Bun 虽然是一个运行时环境，但它也内置了一些框架基础组件（framework primitives），这点和 Node 不一样。

Nitro 本身就能作为一个独立的 API 服务器来使用，因此用它来集成非常合适。

### 748

作者: @Guillermo-Rauch
时间: 2025-10-25
链接: https://x.com/rauchg/status/1981941280289779766
互动: Likes: 6; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,373; Bookmarks: 1; isReply: 1

@igghera This has nothing to do with Next. It’s a standalone toolkit and compiler. You can use it to make durable functions across all frameworks

@igghera 这和 Next 没有关系。它是一个独立的工具包和编译器。你可以用它来在各种框架中构建 Durable Functions。

### 749

作者: @Guillermo-Rauch
时间: 2025-10-25
链接: https://x.com/rauchg/status/1982107165918908427
互动: Likes: 70; Retweets: 3; Replies: 1; Quotes: 0; Views: 5,569; Bookmarks: 1; isReply: 1

@cramforce Real backends are the friends we made along the way

我们一路走来，收获的真正后端，是那些结交的朋友。

### 750

作者: @Guillermo-Rauch
时间: 2025-10-25
链接: https://x.com/rauchg/status/1982114433213345989
互动: Likes: 1; Retweets: 0; Replies: 1; Quotes: 0; Views: 235; Bookmarks: 0; isReply: 1

@mrhameljr @rodrigoehlers @nextjs @reactjs Our job is specifically not to police content and deployments. We take reports very seriously and act on violations expediently as we can. Banning *.vercel is a bit like banning *.com, it’s a public suffix

@mrhameljr @rodrigoehlers @nextjs @reactjs 我们的职责具体而言并非审查内容和部署。对于收到的报告，我们高度重视，并会尽快对违规行为采取行动。封禁 *.vercel 域名有点类似于封禁 *.com，因为 .vercel 本身是一个公共后缀（public suffix）。

### 751

作者: @Guillermo-Rauch
时间: 2025-10-25
链接: https://x.com/rauchg/status/1982124481985577196
互动: Likes: 0; Retweets: 0; Replies: 1; Quotes: 0; Views: 221; Bookmarks: 0; isReply: 1

@mrhameljr @rodrigoehlers @nextjs @reactjs 2 of those links seem to have already been flagged. What makes the link suspicious in a way that can be automatically determined in your mind?

@mrhameljr @rodrigoehlers @nextjs @reactjs 其中有两个链接好像已经被系统标记了。你觉得这些链接具体有哪些特征，能让它们被自动检测出来呢？

### 752

作者: @Guillermo-Rauch
时间: 2025-10-25
链接: https://x.com/rauchg/status/1982125933999132770
互动: Likes: 4; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,232; Bookmarks: 1; isReply: 1

@mrhameljr @rodrigoehlers @nextjs @reactjs There’s nothing Vercel can do to stop people from sharing .vercel.app URLs on Discords. And we have to be careful because people deploy lots of legitimate crypto things. What we can do (and are doing) is accelerating our reviewing of reports and making fast, quality decisions

@mrhameljr @rodrigoehlers @nextjs @reactjs Vercel 无法阻止人们在 Discord 上分享 .vercel.app 链接。我们对此必须谨慎，因为用户部署了大量合法的加密货币相关项目。我们目前能采取（并且正在实施）的措施是：加快处理相关报告的流程，并确保做出快速且优质的处理决定。

### 753

作者: @Guillermo-Rauch
时间: 2025-10-25
链接: https://x.com/rauchg/status/1982126229592678883
互动: Likes: 1; Retweets: 0; Replies: 0; Quotes: 0; Views: 2,157; Bookmarks: 0; isReply: 1

@mrhameljr @rodrigoehlers @nextjs @reactjs If you’re disproportionally affected by this issue I’d love to connect you with our Safety team and we can act quicker on these targeted attacks. Feel free to DM me to connect. Appreciate your feedback

@mrhameljr @rodrigoehlers @nextjs @reactjs 如果您受到此问题的严重影响，我很乐意帮您联系我们的安全团队，以便我们能加快处理这些针对性攻击。欢迎随时私信我。感谢您的反馈。

### 754

作者: @Guillermo-Rauch
时间: 2025-10-25
链接: https://x.com/rauchg/status/1982126865880846540
互动: Likes: 1; Retweets: 0; Replies: 1; Quotes: 0; Views: 78; Bookmarks: 0; isReply: 1

@mrhameljr @rodrigoehlers @nextjs @reactjs Without giving away too much, you’re wrong about this. People that conduct phishing are very good at evading “obvious” heuristics. And being too simplistic in who we ban actually poses a serious threat to the platform and a censorship risk.

@mrhameljr @rodrigoehlers @nextjs @reactjs 话说得直接一点，你在这件事上可能弄错了。那些搞网络钓鱼的人，非常擅长绕过那些「显而易见」的规则。如果我们封禁账号的标准定得太简单粗暴，反而会给平台带来严重威胁，甚至引发误判和不当审查的风险。

### 755

作者: @Guillermo-Rauch
时间: 2025-10-25
链接: https://x.com/rauchg/status/1982128617753649530
互动: Likes: 3; Retweets: 0; Replies: 1; Quotes: 0; Views: 90; Bookmarks: 1; isReply: 1

@mrhameljr @rodrigoehlers @nextjs @reactjs It’s not about losing money. I want to minimize friction to the millions of developers who join our Hobby tier, including students who’re learning to code and deploy for the first time, or someone dreaming up the next big thing. We can’t let the abusers ruin it for everyone

@mrhameljr @rodrigoehlers @nextjs @reactjs 这并非关乎金钱损失。我们的目标是，为加入我们 Hobby 免费计划（Hobby tier）的数百万开发者最大限度地减少使用阻力 —— 这其中包括初次学习编程和部署的学生，也包括正在构思下一个伟大创意的梦想家。我们绝不能任由少数滥用者破坏大家共有的良好环境。

### 756

作者: @Guillermo-Rauch
时间: 2025-10-25
链接: https://x.com/rauchg/status/1982129922173984990
互动: Likes: 3; Retweets: 0; Replies: 0; Quotes: 0; Views: 191; Bookmarks: 0; isReply: 1

@Dev07Exp @igghera No, “use cache” is for Next.

@Dev07Exp @igghera 不对，「use cache」这个选项是给 Next 用的。

### 757

作者: @Guillermo-Rauch
时间: 2025-10-25
链接: https://x.com/rauchg/status/1982144794727227463
互动: Likes: 550; Retweets: 25; Replies: 55; Quotes: 14; Views: 95,789; Bookmarks: 335; isReply: 0

Anytime your API endpoint performs a bunch of 𝚊𝚠𝚊𝚒𝚝 side effects, it’s a sign it should “𝚞𝚜𝚎 𝚠𝚘𝚛𝚔𝚏𝚕𝚘𝚠”.

Anytime you find bad state in your database, like pending unfinished jobs, it’s a sign you should “𝚞𝚜𝚎 𝚠𝚘𝚛𝚔𝚏𝚕𝚘𝚠”

Anytime you talk to a bunch of unreliable or rate-limited third-party services, it’s sign you should “𝚞𝚜𝚎 𝚠𝚘𝚛𝚔𝚏𝚕𝚘𝚠”.

Anytime you’re trying to do too much work in-band and reply with 𝟸𝟶𝟶, it’s a sign you should 𝟸𝟶𝟸 𝙰𝚌𝚌𝚎𝚙𝚝𝚎𝚍 instead and “𝚞𝚜𝚎 𝚠𝚘𝚛𝚔𝚏𝚕𝚘𝚠”

Anytime the business starts relying on critical ad-hoc workflows not defined in code, not version-controlled, without o11y and SLAs, it’s sign you should “𝚞𝚜𝚎 𝚠𝚘𝚛𝚔𝚏𝚕𝚘𝚠”.

tl;DR: Anytime you care about asynchronous reliability, it’s sign you should “𝚞𝚜𝚎 𝚠𝚘𝚛𝚔𝚏𝚕𝚘𝚠”.

当你的 API 端点需要执行大量异步等待（await）的副作用操作时，这就意味着你应该考虑「采用工作流（use workflow）」。

当你在数据库中发现异常状态，例如存在挂起或未完成的任务时，这就意味着你应该考虑「采用工作流」。

当你需要与一系列不可靠或存在速率限制的第三方服务交互时，这就意味着你应该考虑「采用工作流」。

当你试图在同步请求响应过程中处理过多工作，并直接返回 200（OK）状态码时，更好的做法是返回 202（Accepted）状态码以示请求已被接受，并「采用工作流」进行后续处理。

当业务开始依赖那些未在代码中定义、缺乏版本控制、没有可观测性（Observability）和服务水平协议（SLA）保障的关键临时流程时，这就意味着你应该考虑「采用工作流」。

简而言之：每当你需要关注异步操作的可靠性时，这就意味着你应该考虑「采用工作流」。

### 758

作者: @Guillermo-Rauch
时间: 2025-10-25
链接: https://x.com/rauchg/status/1982155024961589384
互动: Likes: 11; Retweets: 0; Replies: 1; Quotes: 0; Views: 4,534; Bookmarks: 1; isReply: 1

@codeandsleep I think the primary question devs and AIs will deal with is the granularity of the step. Like how many sub tasks do you perform per step etc. There’s no right answer per se, it’s app and business specific. But it’s also not a big deal.

@codeandsleep 我认为，开发者和 AI 需要解决的核心问题将是步骤的粒度。比如，每个步骤应该包含多少个子任务等等。这本身并没有标准答案，完全取决于具体的应用和业务需求。不过，这也不是什么大不了的事。

### 759

作者: @Guillermo-Rauch
时间: 2025-10-25
链接: https://x.com/rauchg/status/1982155394022551866
互动: Likes: 39; Retweets: 1; Replies: 1; Quotes: 0; Views: 5,623; Bookmarks: 3; isReply: 1

@jacobmparis Wow. Spot on

@jacobmparis 哇塞。说得太准了。

### 760

作者: @Guillermo-Rauch
时间: 2025-10-25
链接: https://x.com/rauchg/status/1982165454585213008
互动: Likes: 19; Retweets: 0; Replies: 3; Quotes: 0; Views: 7,006; Bookmarks: 0; isReply: 1

@xhinte cool

@xhinte 厉害

### 761

作者: @Guillermo-Rauch
时间: 2025-10-25
链接: https://x.com/rauchg/status/1982197195479650714
互动: Likes: 872; Retweets: 14; Replies: 57; Quotes: 6; Views: 49,482; Bookmarks: 45; isReply: 0

The USA 🇺🇸 is such a blessed and special place. I had an unforgettable time today, exploring its beautiful canyons and getting to know the Navajo people and their amazing history. Recommend! 🏜️ https://t.co/9Sr7HuAjp6

美国 🇺🇸 真是个得天独厚的福地。今天令我难忘，探索了壮丽的峡谷，还结识了纳瓦霍人，了解了他们精彩的历史。强烈推荐！ 🏜️ https://t.co/9Sr7HuAjp6

### 762

作者: @Guillermo-Rauch
时间: 2025-10-25
链接: https://x.com/rauchg/status/1982208434834743417
互动: Likes: 833; Retweets: 17; Replies: 28; Quotes: 4; Views: 43,927; Bookmarks: 48; isReply: 1

@Cowboycodey Having lots of kids should be the norm. Families rise to the occasion instinctively. Our forefathers managed to do it!

@Cowboycodey 多生孩子应当成为常态。家庭本能地就能适应并应对。我们的祖辈们当年就是这么过来的！

### 763

作者: @Guillermo-Rauch
时间: 2025-10-26
链接: https://x.com/rauchg/status/1982239871499436465
互动: Likes: 4; Retweets: 0; Replies: 2; Quotes: 0; Views: 316; Bookmarks: 0; isReply: 1

@heinenbros @marvinvonhagen That’s spot on 😂

说得太对了 😂

### 764

作者: @Guillermo-Rauch
时间: 2025-10-26
链接: https://x.com/rauchg/status/1982252150240825414
互动: Likes: 3; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,480; Bookmarks: 0; isReply: 1

@franmoretti_ @aisdk Nice

@franmoretti_ @aisdk 不错

### 765

作者: @Guillermo-Rauch
时间: 2025-10-26
链接: https://x.com/rauchg/status/1982257314465038762
互动: Likes: 354; Retweets: 6; Replies: 31; Quotes: 1; Views: 33,966; Bookmarks: 22; isReply: 0

Today is @timneutkens’ 8th anniversary of working at Vercel and leading Next.js. I’ve learned a lot from him, as he’s always been wise beyond his years. 

He brought customer obsession to open source, always striving to read every Next.js issue and GH notification, taking everyone seriously whether you’re anon anime pfp or someone at a huge company shipping with Next.

Thank you Tim!

今天是 @timneutkens 加入 Vercel 并领导 Next.js 项目的八周年纪念。我从他身上获益良多，因为他总是展现出超越年龄的智慧。

他将「客户至上」（Customer Obsession）的理念带入了开源世界，总是尽力阅读每一个 Next.js 的问题反馈和 GitHub 通知，并且平等、认真地对待每一个人 —— 无论你是使用动漫头像的匿名网友，还是某家正在用 Next.js 构建产品的大型公司员工。

感谢你，Tim！

### 766

作者: @Guillermo-Rauch
时间: 2025-10-26
链接: https://x.com/rauchg/status/1982285063644709096
互动: Likes: 1; Retweets: 0; Replies: 1; Quotes: 0; Views: 204; Bookmarks: 0; isReply: 1

@krutikkkkkkkkk @sonofalli Hundreds 😆

@krutikkkkkkkkk @sonofalli 好几百个呢 😆

### 767

作者: @Guillermo-Rauch
时间: 2025-10-26
链接: https://x.com/rauchg/status/1982287908712390860
互动: Likes: 233; Retweets: 10; Replies: 27; Quotes: 5; Views: 48,613; Bookmarks: 86; isReply: 0

Why is “𝚞𝚜𝚎 𝚜𝚝𝚎𝚙” needed?

Someone pointed out steps in a workflow are like “spawn checkpoints” in a video game. Good analogy.

An interesting consequence of marking a function “𝚞𝚜𝚎 𝚠𝚘𝚛𝚔𝚏𝚕𝚘𝚠” is that you’re not allowed to do I/O other than steps.

Workflows need to be side-effect free and deterministic. Each time you 𝚊𝚠𝚊𝚒𝚝 that function must be a step. 

These function calls can be thought of as serializable continuations. The inputs and outputs of these functions are committed to a log. Think JSON.

If you have a workflow with 3 steps and the last one fails, we have to be able to “re-run” the entire function and have a perfect handle on the state of the world.

In this way, “𝚞𝚜𝚎 𝚜𝚝𝚎𝚙” is actually very similar to “𝚞𝚜𝚎 𝚌𝚊𝚌𝚑𝚎” or “𝚐𝚎𝚝𝚂𝚝𝚊𝚝𝚒𝚌𝙿𝚛𝚘𝚙𝚜” — functions that can be externalized and isolated in space and time, running in different “computers”.

为什么需要「使用步骤」（use step）？

有人打了个比方：工作流中的步骤，就像电子游戏里的「存档点」。这个类比非常贴切。

当你把一个函数标记为「使用工作流」（use workflow）时，一个有趣的影响就出现了：除了执行定义好的「步骤」，你无法进行其他任何输入 / 输出（I/O）操作。

这是因为工作流必须是无副作用且确定性的。每次你等待（`await`）这个函数时，它都必须是一个「步骤」。

你可以把这些函数调用想象成「可序列化的断点」。每个步骤的输入和输出都会被记录到一个日志里，就像 JSON 数据一样。

假设一个工作流有 3 个步骤，如果最后一步执行失败了，我们必须能够「重新运行」整个函数，并且精确地恢复到失败前的状态。

这样一来，「使用步骤」（use step）的功能，其实和「使用缓存」（use cache）或「获取静态属性」（getStaticProps）非常相似 —— 它们都是一些可以从主程序中「剥离」出来的函数，能够在不同的「计算机」上，独立于原来的时间和空间运行。

### 768

作者: @Guillermo-Rauch
时间: 2025-10-26
链接: https://x.com/rauchg/status/1982290023472156800
互动: Likes: 13; Retweets: 0; Replies: 2; Quotes: 0; Views: 1,920; Bookmarks: 2; isReply: 1

@jponsvega There’s arguments for and against syntax and conventions. I don’t agree with the lock in argument. It’s not like I can run a TanStack createServerFn in Next today. And as far as interop goes, I’m all for it. That’s why WDK is framework agnostic and provider / backend agnostic

@jponsvega 关于语法和规范，存在支持和反对两种观点。我不同意那种关于技术锁定的论点。毕竟，我现在也没法在 Next.js 里直接运行 TanStack 的 createServerFn。说到互操作性，我举双手赞成。正因如此，WDK 的设计才是框架无关的，并且与具体的提供商或后端无关。

### 769

作者: @Guillermo-Rauch
时间: 2025-10-26
链接: https://x.com/rauchg/status/1982291989446922263
互动: Likes: 10; Retweets: 0; Replies: 1; Quotes: 0; Views: 798; Bookmarks: 0; isReply: 1

@karthikkalyan90 @jponsvega Dope. There was probably better, less click baity language to make some good arguments about ecosystem-wide interop but here we are!

We’re participating in TC39 and down to explore language-level syntax constructs and interop

@karthikkalyan90 @jponsvega 酷。本来或许可以用更好、不那么标题党的说法，来深入探讨整个生态系统的互操作性，但现状如此！

我们正在参与 TC39 委员会，并且乐于探索语言层面的语法结构和互操作性。

### 770

作者: @Guillermo-Rauch
时间: 2025-10-26
链接: https://x.com/rauchg/status/1982295113205534840
互动: Likes: 4; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,040; Bookmarks: 2; isReply: 1

@_alexsm_ The classic example is: something happens (think someone places a crypto trade), and you likely need to do a bunch of stuff to fulfill it. It’s crucial all those steps happen reliably.

Post-signup stuff, market orders, requesting an uber, are all examples of complex workflows

@_alexsm_ 一个经典的例子是：当某个事件触发时（例如，有人发起了一笔加密货币交易），你很可能需要执行一系列操作来最终完成它。确保所有这些步骤都可靠地执行，这一点至关重要。

诸如用户注册后的后续流程、执行市价订单、打一辆优步（Uber）等，都是复杂工作流（Workflow）的典型例子。

### 771

作者: @Guillermo-Rauch
时间: 2025-10-26
链接: https://x.com/rauchg/status/1982296276839596447
互动: Likes: 7; Retweets: 0; Replies: 2; Quotes: 0; Views: 1,437; Bookmarks: 3; isReply: 1

@themattmayfield Great Q. It’s best to be explicit because a lot of async functions are *not* serializable. They might expect parameters like a db connection handle. Also, steps are like mini-queues behind the scenes, so it gives you a sense of the resulting infrastructure and the “hops” involved

@themattmayfield 问得好。最好明确说明这一点，因为许多异步任务函数是 * 无法 * 序列化（serializable）的。例如，它们可能需要像数据库连接句柄这类特定的参数。此外，每个步骤在底层都像一个微型队列，这有助于你理解最终构建的基础设施以及其中涉及的「中间环节」。

### 772

作者: @Guillermo-Rauch
时间: 2025-10-26
链接: https://x.com/rauchg/status/1982476318639079784
互动: Likes: 4,455; Retweets: 461; Replies: 192; Quotes: 75; Views: 217,267; Bookmarks: 1,442; isReply: 0

Learn to ship. Shipping is a skill distinct from coding. Shipping is designing, coding, QAing, story-telling, teaching, marketing, selling, pivoting, iterating…

It used to be that coding dominated in importance because of coding ability scarcity. AI will push you to go further.

学会将产品推向市场。产品交付是一项与单纯写代码截然不同的技能。它涵盖了产品设计、编码实现、质量测试、故事叙述、用户教育、市场营销、销售推广、战略转向（Pivoting）以及持续迭代……

在过去，由于编程人才稀缺，编码能力显得尤为重要。而人工智能（AI）将助你突破这一局限，走得更远。

### 773

作者: @Guillermo-Rauch
时间: 2025-10-26
链接: https://x.com/rauchg/status/1982478223305998571
互动: Likes: 38; Retweets: 0; Replies: 2; Quotes: 0; Views: 4,933; Bookmarks: 1; isReply: 1

@MichaelArnaldi @vercel Appreciate that 🙌 the best side effect of this workflow release is the healthy debate and interest it’s sparked in reliability-as-code 😁

@MichaelArnaldi @vercel 非常感谢 🙌 这次工作流发布带来的一个意外收获是，它引发了关于可靠性即代码（reliability-as-code）的积极讨论和广泛关注 😁

### 774

作者: @Guillermo-Rauch
时间: 2025-10-26
链接: https://x.com/rauchg/status/1982580694997205243
互动: Likes: 45; Retweets: 0; Replies: 1; Quotes: 0; Views: 6,485; Bookmarks: 3; isReply: 1

@GergelyOrosz I think it’s a must-have for them and they’re likely building it. Our goal is to make an otherwise complex and costly AWS setup, the default for @vercel customers, with ~zero config.

@GergelyOrosz 我认为这（功能）对他们（Vercel）来说是必备的，而且他们很可能已经在开发了。我们的目标，就是要把一个通常既复杂又昂贵的 AWS 配置，变成 @vercel 客户开箱即用的默认方案，实现近乎零配置。

### 775

作者: @Guillermo-Rauch
时间: 2025-10-26
链接: https://x.com/rauchg/status/1982583886522773880
互动: Likes: 58; Retweets: 1; Replies: 1; Quotes: 0; Views: 9,275; Bookmarks: 12; isReply: 1

@GergelyOrosz True. Customers can deploy to multiple regions with built in resilience and redundancy with one line of vercel.json config or a couple clicks.

We’re also bringing single-region but with fallback region to self-serve (also 1LOC)

https://t.co/8osGCJinBx

@GergelyOrosz 确实如此。客户只需一行 `vercel.json` 配置或点击几下，就能将应用部署到多个区域，并获得内置的高可用性（High Availability）与冗余保障。

我们也将为自助服务用户推出支持故障转移区域的单区域部署方案（同样只需一行代码即可配置）。

https://t.co/8osGCJinBx

### 776

作者: @Guillermo-Rauch
时间: 2025-10-26
链接: https://x.com/rauchg/status/1982585941320741222
互动: Likes: 39; Retweets: 1; Replies: 2; Quotes: 0; Views: 7,463; Bookmarks: 1; isReply: 1

@james_r_perkins We’re debugging 🫡 thx for sending the details over 🫶

@james_r_perkins 我们正在排查问题 🫡 多谢你把详细情况发过来 🫶

### 777

作者: @Guillermo-Rauch
时间: 2025-10-27
链接: https://x.com/rauchg/status/1982604469104939169
互动: Likes: 1; Retweets: 0; Replies: 2; Quotes: 0; Views: 305; Bookmarks: 0; isReply: 1

@pranaygp @AzianMike When you pass a `Date` it’s effectively “sleepUntil”? Wonder if it should be 2 utilities

@pranaygp @AzianMike 当你传入一个 `Date` 参数时，这本质上不就是 `sleepUntil` 的功能吗？我在想，这是否应该拆分成两个独立的工具函数？

### 778

作者: @Guillermo-Rauch
时间: 2025-10-27
链接: https://x.com/rauchg/status/1982634029884346616
互动: Likes: 54; Retweets: 0; Replies: 6; Quotes: 1; Views: 10,005; Bookmarks: 2; isReply: 1

@ragojose Wrong https://t.co/ChI3ZkrZ3k

@ragojose 不对 / 错了 https://t.co/ChI3ZkrZ3k

### 779

作者: @Guillermo-Rauch
时间: 2025-10-27
链接: https://x.com/rauchg/status/1982654090850259068
互动: Likes: 46; Retweets: 0; Replies: 2; Quotes: 0; Views: 5,607; Bookmarks: 0; isReply: 1

@ethanniser I love the Rust attribute syntax

@ethanniser 我超爱 Rust 的属性（attribute）！

### 780

作者: @Guillermo-Rauch
时间: 2025-10-27
链接: https://x.com/rauchg/status/1982656685513859320
互动: Likes: 1; Retweets: 0; Replies: 0; Quotes: 0; Views: 101; Bookmarks: 0; isReply: 1

@gengjiawen You already can!
https://t.co/19y5N8YVb4

@gengjiawen 你现在就能用了！
https://t.co/19y5N8YVb4

### 781

作者: @Guillermo-Rauch
时间: 2025-10-27
链接: https://x.com/rauchg/status/1982661188677996574
互动: Likes: 276; Retweets: 3; Replies: 22; Quotes: 2; Views: 46,639; Bookmarks: 19; isReply: 1

@joshtriedcoding Before this gets a 1T likes. This is no different from eg GCC’s attribute syntax to opt out of compiler optimizations

__𝚊𝚝𝚝𝚛𝚒𝚋𝚞𝚝𝚎__((𝚗𝚘𝚒𝚗𝚕𝚒𝚗𝚎))
𝚟𝚘𝚒𝚍 𝚖𝚢_𝚏𝚞𝚗𝚌𝚝𝚒𝚘𝚗() {
    // 𝚌𝚘𝚍𝚎
}

Directives can annotate functions / modules for compiler passes

@joshtriedcoding 趁这条推文还没被点上一万亿个赞之前，我得说，这其实和 GCC 的 attribute 语法（比如用来禁用内联优化的那种）没什么两样。

__𝚊𝚝𝚝𝚛𝚒𝚋𝚞𝚝𝚎__((𝚗𝚘𝚒𝚗𝚕𝚒𝚗𝚎))
𝚟𝚘𝚒𝚍 𝚖𝚢_𝚏𝚞𝚗𝚌𝚝𝚒𝚘𝚗(）{// 𝚌𝚘𝚍𝚎}

这些指令的作用就是给函数或模块加上注解，好让编译器在相应的处理阶段（compiler passes）识别并执行特定操作。

### 782

作者: @Guillermo-Rauch
时间: 2025-10-27
链接: https://x.com/rauchg/status/1982777580236448009
互动: Likes: 35; Retweets: 1; Replies: 4; Quotes: 0; Views: 4,687; Bookmarks: 1; isReply: 1

@theteknosaur Interesting

@theteknosaur 有意思。

### 783

作者: @Guillermo-Rauch
时间: 2025-10-27
链接: https://x.com/rauchg/status/1982779227691962617
互动: Likes: 0; Retweets: 0; Replies: 1; Quotes: 0; Views: 93; Bookmarks: 0; isReply: 1

@Oztraiker Oops. Thx for the report. Browser?

@Oztraiker 抱歉，谢谢你的反馈。请问你用的是哪个浏览器？

### 784

作者: @Guillermo-Rauch
时间: 2025-10-27
链接: https://x.com/rauchg/status/1982801333091459219
互动: Likes: 50; Retweets: 0; Replies: 0; Quotes: 0; Views: 5,308; Bookmarks: 0; isReply: 1

@hichaelmart Thank you for contributing

@hichaelmart 感谢您的贡献

### 785

作者: @Guillermo-Rauch
时间: 2025-10-27
链接: https://x.com/rauchg/status/1982818632104038653
互动: Likes: 2; Retweets: 0; Replies: 0; Quotes: 0; Views: 79; Bookmarks: 0; isReply: 1

@Oztraiker It's been fixed

@Oztraiker 已经修复了。

### 786

作者: @Guillermo-Rauch
时间: 2025-10-27
链接: https://x.com/rauchg/status/1982870146147631398
互动: Likes: 1; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,321; Bookmarks: 0; isReply: 1

@awpthorp Deploy API servers to Vercel zero-config. Everything just works. And with Workflows and Queues, you can handle all the "deeper backend" stuff (asynchronous tasks)

@awpthorp 在 Vercel 上零配置部署 API 服务器，开箱即用。此外，借助 Workflows 和 Queues，你还能处理所有「更深层的后端」任务（异步任务）。

### 787

作者: @Guillermo-Rauch
时间: 2025-10-27
链接: https://x.com/rauchg/status/1982876569141235919
互动: Likes: 6; Retweets: 0; Replies: 3; Quotes: 0; Views: 1,947; Bookmarks: 1; isReply: 1

@Anonymo32257610 Absolutely! cc @pranaygp

@Anonymo32257610 当然！也转给 @pranaygp 看看。

### 788

作者: @Guillermo-Rauch
时间: 2025-10-27
链接: https://x.com/rauchg/status/1982876978303906001
互动: Likes: 193; Retweets: 5; Replies: 22; Quotes: 1; Views: 45,640; Bookmarks: 9; isReply: 0

I’ll be on @tbpn today to talk about JavaScript directives

今天我会在 @tbpn 上聊聊 JavaScript 指令。

### 789

作者: @Guillermo-Rauch
时间: 2025-10-27
链接: https://x.com/rauchg/status/1982883570030129351
互动: Likes: 13; Retweets: 1; Replies: 2; Quotes: 0; Views: 3,301; Bookmarks: 4; isReply: 1

@ronphaestas @nextjs amazing

@ronphaestas @nextjs 太棒了！

### 790

作者: @Guillermo-Rauch
时间: 2025-10-27
链接: https://x.com/rauchg/status/1982889633701867673
互动: Likes: 41; Retweets: 1; Replies: 2; Quotes: 0; Views: 5,116; Bookmarks: 1; isReply: 1

@thdxr Everyone always use workflow, but nobody asking how workflow

@thdxr 人人都在用工作流，却没人问过工作流到底是个啥。

### 791

作者: @Guillermo-Rauch
时间: 2025-10-27
链接: https://x.com/rauchg/status/1982889783161667933
互动: Likes: 0; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,246; Bookmarks: 0; isReply: 1

@HanifCarroll 🫶 for sure! Let me know if I missed anything

@HanifCarroll 🫶 没问题！有什么遗漏的随时告诉我。

### 792

作者: @Guillermo-Rauch
时间: 2025-10-27
链接: https://x.com/rauchg/status/1982891220704878943
互动: Likes: 277; Retweets: 21; Replies: 22; Quotes: 3; Views: 51,168; Bookmarks: 84; isReply: 0

Vercel AI Gateway's stats are a great glimpse into the market share of LLMs for agent developers, startups, and enterprises (as opposed to IDEs and coding CLIs)

Anthropic is dominating with over 50% of the token volume: https://t.co/5riTzi0qr0 https://t.co/HMqS2MRgUS

Vercel AI Gateway 的统计数据为观察大语言模型（LLM）在智能体开发者、初创公司及企业中的市场份额提供了一个绝佳的视角（这与主要面向 IDE 和编码 CLI 的使用场景不同）。

Anthropic 占据着主导地位，其 Token 使用量占比超过了 50%：https://t.co/5riTzi0qr0 https://t.co/HMqS2MRgUS

### 793

作者: @Guillermo-Rauch
时间: 2025-10-27
链接: https://x.com/rauchg/status/1982911313530761615
互动: Likes: 143; Retweets: 0; Replies: 12; Quotes: 5; Views: 19,840; Bookmarks: 10; isReply: 1

@hanebox only some of the biggest backends in the world. but obviously prior to workflow / queues it was just the api part, now it can be the entire thing

@hanebox 它（最初）支撑的只是世界上一些规模最大的后端系统。不过显然，在引入工作流和队列功能之前，它只提供了 API 部分；而现在，它已经能够提供完整的解决方案了。

### 794

作者: @Guillermo-Rauch
时间: 2025-10-27
链接: https://x.com/rauchg/status/1982941856817385748
互动: Likes: 1,329; Retweets: 64; Replies: 100; Quotes: 34; Views: 275,534; Bookmarks: 427; isReply: 0

▲ ~/𝚛𝚊𝚞𝚌𝚑𝚐/𝚘𝚜𝚜-𝚐𝚛𝚊𝚗𝚝𝚜/  𝚕𝚜▐

I'm announcing 22 $1,000USD grants for foundational open source projects.

I selected a set of amazing contributors who are working on diverse problems in the JS/TS ecosystem. 

Since I've mostly spent time on React (web) and Next, I've specifically chosen to support people working in other areas: Bun, Nitro, Vue, Nuxt, React Native, Vite… 

… but also the foundations often overlooked, like the people quietly maintaining half the Node.js ecosystem, testing infrastructure, inheriting mature projects like Lodash, or contributing to TC39.

I plan to do more of these over time. There are a ton of people who deserve these and I haven't gotten around to yet, so expect more soon. I'm also always on the lookout for supporting the lesser-known up-and-comers, tips welcome 😁 

Part of this is the financial contribution, but also very importantly: recognition. (PS: these are personal, not affiliated with Vercel, and fully unconditional)

https://t.co/GH17tOB1dg

▲ ~/𝚛𝚊𝚞𝚌𝚑𝚐/𝚘𝚜𝚜-𝚐𝚛𝚊𝚗𝚝𝚜/ 𝚕𝚜▐

我公布了 22 笔、每笔 1000 美元的资助，用于支持从事基础性开源工作的贡献者。

我挑选了一批优秀的贡献者，他们正在 JavaScript/TypeScript 生态系统中解决各种各样的问题。

由于我个人的时间主要投入在 React（Web）和 Next 上，所以我特别选择了支持其他技术领域的开发者：比如 Bun、Nitro、Vue、Nuxt、React Native、Vite…

… 同时也包括了那些常常被忽视的基础性工作，例如：默默维护着 Node.js 生态系统中大量模块的人们、测试基础设施的维护者、接手维护像 Lodash 这样成熟项目的人，以及为 TC39（ECMAScript 标准委员会）做出贡献的人。

我打算今后继续开展这类资助。还有非常多值得资助的人我这次还没能顾及，所以请期待不久后的下一批。我也一直在留意并希望支持那些不太知名但很有潜力的后起之秀，欢迎大家给我推荐 😁

这份资助的一部分是金钱上的支持，但同样（甚至更）重要的是：对贡献者工作的认可。（注：这是个人行为，与 Vercel 公司无关，且没有任何附加条件）

https://t.co/GH17tOB1dg

### 795

作者: @Guillermo-Rauch
时间: 2025-10-27
链接: https://x.com/rauchg/status/1982953016522354872
互动: Likes: 29; Retweets: 0; Replies: 3; Quotes: 0; Views: 6,618; Bookmarks: 1; isReply: 1

@Sikandar_Bhide Yes, look forward to supporting projects in the Svelte ecosystem. Stay tuned for the next one

@Sikandar_Bhide 是的，我们很期待能支持 Svelte 生态系统中的项目。敬请期待下一个吧！

### 796

作者: @Guillermo-Rauch
时间: 2025-10-28
链接: https://x.com/rauchg/status/1982973728423325803
互动: Likes: 553; Retweets: 24; Replies: 27; Quotes: 7; Views: 99,537; Bookmarks: 178; isReply: 0

GLM 4.6 is an astonishingly good model. The 3rd best on https://t.co/SnZ54XoRWV, and the only open model in the top 5.

Vercel AI Gateway now offers the lowest https://t.co/C6DMISpWEq GLM 4.6 pricing anywhere. Just set 𝚖𝚘𝚍𝚎𝚕: "𝚣𝚊𝚒/𝚐𝚕𝚖-𝟺.𝟼". https://t.co/wUK9bIpW8q

GLM 4.6 是一款性能极其出色的模型。它在 https://t.co/SnZ54XoRWV 榜单上高居第三，并且是前五名中唯一的开源模型。

Vercel AI Gateway 现已提供全网最低的 GLM 4.6 调用价格，详情可见 https://t.co/C6DMISpWEq。您只需在配置中将 `model` 参数设置为 `"zai/glm-4.6"` 即可使用。了解更多：https://t.co/wUK9bIpW8q

### 797

作者: @Guillermo-Rauch
时间: 2025-10-28
链接: https://x.com/rauchg/status/1982980474298622027
互动: Likes: 5; Retweets: 0; Replies: 1; Quotes: 0; Views: 173; Bookmarks: 1; isReply: 1

@unnoqcom @pinesheet Maybe next batch!

@unnoqcom @pinesheet 可能下一批会有！

### 798

作者: @Guillermo-Rauch
时间: 2025-10-28
链接: https://x.com/rauchg/status/1982986464465203257
互动: Likes: 6; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,960; Bookmarks: 0; isReply: 1

@pranaygp Incredible writeup fr

@pranaygp 写得真棒，真心话！

### 799

作者: @Guillermo-Rauch
时间: 2025-10-28
链接: https://x.com/rauchg/status/1983000322084876576
互动: Likes: 8; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,357; Bookmarks: 0; isReply: 1

@jrysana All else being equal, for the same exact model and latency, cheaper is definitely better, and we love to offer that to our customers

在模型性能和延迟表现完全相同的前提下，价格更低当然更具优势。为客户提供这样的优势，正是我们所致力追求的。

### 800

作者: @Guillermo-Rauch
时间: 2025-10-28
链接: https://x.com/rauchg/status/1983220603600461995
互动: Likes: 19; Retweets: 0; Replies: 2; Quotes: 0; Views: 4,340; Bookmarks: 0; isReply: 1

@nutlope nice typeface 🤩

@nutlope 字体真好看！🤩

### 801

作者: @Guillermo-Rauch
时间: 2025-10-28
链接: https://x.com/rauchg/status/1983296946954744094
互动: Likes: 350; Retweets: 8; Replies: 22; Quotes: 2; Views: 53,061; Bookmarks: 14; isReply: 0

Open always wins

开放者胜

### 802

作者: @Guillermo-Rauch
时间: 2025-10-29
链接: https://x.com/rauchg/status/1983342042077114687
互动: Likes: 0; Retweets: 0; Replies: 0; Quotes: 0; Views: 66; Bookmarks: 0; isReply: 1

@ClipGod1 No, actually never once thought that. Usually it’s the opposite but I concede we have lots to improve and more work to do!

@ClipGod1 不，其实我压根没这么想过。通常情况恰恰相反，不过我也承认，我们确实还有很多需要改进和努力的地方！

### 803

作者: @Guillermo-Rauch
时间: 2025-10-29
链接: https://x.com/rauchg/status/1983345626827165717
互动: Likes: 15; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,760; Bookmarks: 0; isReply: 1

@mrlubos lmao @ the pic 😂

@mrlubos 笑死（lmao），这图😂

### 804

作者: @Guillermo-Rauch
时间: 2025-10-29
链接: https://x.com/rauchg/status/1983389232367579472
互动: Likes: 4; Retweets: 0; Replies: 2; Quotes: 0; Views: 423; Bookmarks: 0; isReply: 1

@warlord1000000 Definitely open to it if there’s demand

@warlord1000000 如果有需求的话，当然可以啊。

### 805

作者: @Guillermo-Rauch
时间: 2025-10-29
链接: https://x.com/rauchg/status/1983558972637581533
互动: Likes: 3; Retweets: 0; Replies: 1; Quotes: 0; Views: 120; Bookmarks: 0; isReply: 1

@headphoneDas We're adding new models every week and it 4x'd in usage over the last couple weeks. We share your enthusiasm 😁
https://t.co/vT0MxVZoUu

@headphoneDas 我们每周都在添加新模型，并且过去几周的使用量已经增长到了原来的四倍。我们和您一样兴奋！😁
https://t.co/vT0MxVZoUu

### 806

作者: @Guillermo-Rauch
时间: 2025-10-29
链接: https://x.com/rauchg/status/1983581975777833398
互动: Likes: 8; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,871; Bookmarks: 0; isReply: 1

@pranaygp Exciting. This felt like a big missing piece!

@pranaygp 太棒了。这感觉就像是补上了关键的一块拼图！

### 807

作者: @Guillermo-Rauch
时间: 2025-10-29
链接: https://x.com/rauchg/status/1983583750698233988
互动: Likes: 65; Retweets: 2; Replies: 3; Quotes: 0; Views: 4,041; Bookmarks: 0; isReply: 1

@preetsuthar17 @vercel Will get faster

@preetsuthar17 @vercel 会变快的。

### 808

作者: @Guillermo-Rauch
时间: 2025-10-29
链接: https://x.com/rauchg/status/1983595028565176444
互动: Likes: 5; Retweets: 0; Replies: 0; Quotes: 0; Views: 191; Bookmarks: 0; isReply: 1

@waytopulkit @preetsuthar17 @vercel Yes by upgrading it gets faster but it can get fasterer

@waytopulkit @preetsuthar17 @vercel 没错，升级后确实会变快，但它还能变得更快（甚至快上加快）。

### 809

作者: @Guillermo-Rauch
时间: 2025-10-29
链接: https://x.com/rauchg/status/1983610295240290519
互动: Likes: 47; Retweets: 0; Replies: 4; Quotes: 0; Views: 4,072; Bookmarks: 0; isReply: 1

@RhysSullivan Not having starlink everywhere is decelerationist

@RhysSullivan 星链没有实现全球覆盖，这本身就是一种（技术）减速主义。

### 810

作者: @Guillermo-Rauch
时间: 2025-10-29
链接: https://x.com/rauchg/status/1983617107976974722
互动: Likes: 2; Retweets: 0; Replies: 1; Quotes: 0; Views: 123; Bookmarks: 0; isReply: 1

@tymzap On it

@tymzap 收到，马上处理！

### 811

作者: @Guillermo-Rauch
时间: 2025-10-29
链接: https://x.com/rauchg/status/1983626251949822194
互动: Likes: 181; Retweets: 9; Replies: 32; Quotes: 8; Views: 29,868; Bookmarks: 29; isReply: 0

Breakdown of most popular TLDs on the new https://t.co/7pvISXPEtI. Domain purchases are up +34.6%, traffic +39.4%.

The main innovation? Speed. When you make something fast, customers reward you. https://t.co/JqGMP2lx18

新平台 https://t.co/7pvISXPEtI 上最热门顶级域名（TLD）的数据分析。域名购买量同比增长 34.6%，流量增长 39.4%。

核心创新是什么？是速度。用户体验一旦提速，市场自然会给予回报。https://t.co/JqGMP2lx18

### 812

作者: @Guillermo-Rauch
时间: 2025-10-29
链接: https://x.com/rauchg/status/1983627599688691974
互动: Likes: 8; Retweets: 1; Replies: 0; Quotes: 0; Views: 682; Bookmarks: 2; isReply: 1

@webmaster 😂 true. Cooking on this with @mixedbreadai and @upstash Search.

@webmaster 😂 确实。正和 @mixedbreadai 与 @upstash Search 一起捣鼓这个呢。

### 813

作者: @Guillermo-Rauch
时间: 2025-10-29
链接: https://x.com/rauchg/status/1983644430893772906
互动: Likes: 146; Retweets: 6; Replies: 10; Quotes: 0; Views: 18,781; Bookmarks: 75; isReply: 0

Our background coding agent OSS template now supports @cursor_ai’s new Composer model.

Powered by @vercel AI Gateway &amp; Sandbox.

⮕ https://t.co/jDw9HoGWfs https://t.co/QEV9kQwTD1

我们的开源编码 AI 智能体模板现已支持 @cursor_ai 推出的全新 Composer 模型。

底层由 @vercel AI Gateway & Sandbox 驱动。

⮕ https://t.co/jDw9HoGWfs https://t.co/QEV9kQwTD1

### 814

作者: @Guillermo-Rauch
时间: 2025-10-29
链接: https://x.com/rauchg/status/1983645148363014391
互动: Likes: 3; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,228; Bookmarks: 0; isReply: 1

@thdxr @cursor_ai @vercel @ctatedev Via their CLI

通过他们的命令行界面（CLI)

### 815

作者: @Guillermo-Rauch
时间: 2025-10-29
链接: https://x.com/rauchg/status/1983645959704998398
互动: Likes: 4; Retweets: 0; Replies: 0; Quotes: 0; Views: 370; Bookmarks: 1; isReply: 1

@KavolisJ @cursor_ai @vercel @ctatedev Yes. But if you want a synchronous vibe coding interface try this one
https://t.co/OX26QwtSOL

是的。不过，如果你想要一种同步感更强的编码界面，可以试试这个：
https://t.co/OX26QwtSOL

### 816

作者: @Guillermo-Rauch
时间: 2025-10-29
链接: https://x.com/rauchg/status/1983647904192720973
互动: Likes: 46; Retweets: 1; Replies: 22; Quotes: 0; Views: 12,703; Bookmarks: 2; isReply: 1

@RhysSullivan @dillon_mulroy @Dillon @Rhys @g same question

@RhysSullivan @dillon_mulroy @Dillon @Rhys @g 同问

### 817

作者: @Guillermo-Rauch
时间: 2025-10-29
链接: https://x.com/rauchg/status/1983649081923875027
互动: Likes: 54; Retweets: 1; Replies: 4; Quotes: 0; Views: 11,252; Bookmarks: 0; isReply: 1

@RhysSullivan @dillon_mulroy @Dillon @Rhys @g I will open a vercel office in Arkansas

@RhysSullivan @dillon_mulroy @Dillon @Rhys @g 我打算在阿肯色州开一个 Vercel 的办公室。

### 818

作者: @Guillermo-Rauch
时间: 2025-10-29
链接: https://x.com/rauchg/status/1983651971308659116
互动: Likes: 25; Retweets: 0; Replies: 2; Quotes: 0; Views: 4,120; Bookmarks: 1; isReply: 1

@v0 Nice

@v0 很棒

### 819

作者: @Guillermo-Rauch
时间: 2025-10-29
链接: https://x.com/rauchg/status/1983652279338332364
互动: Likes: 7; Retweets: 0; Replies: 0; Quotes: 0; Views: 489; Bookmarks: 0; isReply: 1

@linstobias @RhysSullivan @dillon_mulroy @Dillon @Rhys @g @tobi @tobi we will migrate Liquid to @nextjs for the handle

@linstobias @RhysSullivan @dillon_mulroy @Dillon @Rhys @g @tobi @tobi 我们将把 Liquid 迁移到 @nextjs 框架上。

### 820

作者: @Guillermo-Rauch
时间: 2025-10-30
链接: https://x.com/rauchg/status/1983713103457218639
互动: Likes: 757; Retweets: 14; Replies: 52; Quotes: 7; Views: 154,999; Bookmarks: 121; isReply: 0

Hard to believe the @v0 iPhone app is built with React. It’s so… native. Bullish https://t.co/SPeiGTwpb3

真不敢相信 @v0 的 iPhone 应用是用 React 开发的。它的体验如此原生…… 前景一片光明。https://t.co/SPeiGTwpb3

### 821

作者: @Guillermo-Rauch
时间: 2025-10-30
链接: https://x.com/rauchg/status/1983930884563595778
互动: Likes: 4; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,669; Bookmarks: 0; isReply: 1

@devmuzzaiyyan @hey_api 😍🫶 thank you!

@devmuzzaiyyan @hey_api 😍🫶 太感谢啦！

### 822

作者: @Guillermo-Rauch
时间: 2025-10-30
链接: https://x.com/rauchg/status/1983931664687362162
互动: Likes: 18; Retweets: 0; Replies: 0; Quotes: 0; Views: 5,121; Bookmarks: 3; isReply: 1

@shuding @nextjs @vercel 🔥 same for https://t.co/g5xfWex2IP

@shuding @nextjs @vercel 🔥 这个链接也一样：https://t.co/g5xfWex2IP

### 823

作者: @Guillermo-Rauch
时间: 2025-10-30
链接: https://x.com/rauchg/status/1983945320972128687
互动: Likes: 441; Retweets: 10; Replies: 47; Quotes: 2; Views: 41,760; Bookmarks: 24; isReply: 0

The reason I'm so bullish on X @chat is that on every other platform I find myself talking to random phone numbers. It's a bizarre user experience.

X @⁠handles are the perfect global chat identifier. No address book shenanigans, no phone number changes when you travel, etc.

我如此看好 X @chat 的原因是，在其他所有平台上，我发现自己总是在和一堆随机的电话号码聊天。这种用户体验相当别扭。

X @⁠handles 是理想的全球聊天标识符。没有通讯录的繁琐操作，没有出国旅行需要换手机号的麻烦，诸如此类。

### 824

作者: @Guillermo-Rauch
时间: 2025-10-30
链接: https://x.com/rauchg/status/1983952689848274999
互动: Likes: 209; Retweets: 9; Replies: 17; Quotes: 2; Views: 18,605; Bookmarks: 15; isReply: 0

Stanford is now powered by @nextjs &amp; @vercel. Many tell me it's the world's best university.

https://t.co/6yPsn4otPD (more departments coming!) https://t.co/Lt6KXpi5WW

斯坦福大学官网现已基于 @nextjs 和 @vercel 构建。好多人跟我说，这可是全球顶尖的大学。

https://t.co/6yPsn4otPD（更多院系页面即将上线！）https://t.co/Lt6KXpi5WW

### 825

作者: @Guillermo-Rauch
时间: 2025-10-30
链接: https://x.com/rauchg/status/1983956846034534551
互动: Likes: 19; Retweets: 0; Replies: 1; Quotes: 0; Views: 7,784; Bookmarks: 10; isReply: 1

Funding secured, all donations have been sent. Couple awesome reactions this has had so far:
◆ I've learned about a lot of cool new projects and up-and-coming contributors 
◆ One of the recipients told me this will help pay for the contributors getting together and enjoying in-person time
◆ This has brought much-needed attention to projects and some have gotten new contributions (e.g.: @devmuzzaiyyan contributing to https://t.co/GxjjHTIEtq)

资金已到位，所有捐款均已发放。目前已经产生了一些非常积极的反馈：
◆ 我借此机会了解到了许多出色的新项目和潜力十足的贡献者。
◆ 一位受赠者告诉我，这笔款项将用于资助贡献者们线下聚会，享受面对面交流的时光。
◆ 这为相关项目带来了急需的关注度，其中一些已经获得了新的贡献（例如：@devmuzzaiyyan 为 https://t.co/GxjjHTIEtq 做出了贡献）。

### 826

作者: @Guillermo-Rauch
时间: 2025-10-30
链接: https://x.com/rauchg/status/1983957815686525097
互动: Likes: 8; Retweets: 0; Replies: 4; Quotes: 0; Views: 671; Bookmarks: 1; isReply: 1

@CitiZenSleuthX @josephstein @v0 @FernandoTheRojo We'll do a tech writeup on our blog

@CitiZenSleuthX @josephstein @v0 @FernandoTheRojo 我们会在我们的博客上发布一篇技术详解文章。

### 827

作者: @Guillermo-Rauch
时间: 2025-10-30
链接: https://x.com/rauchg/status/1983967510467633327
互动: Likes: 1,045; Retweets: 65; Replies: 141; Quotes: 81; Views: 619,001; Bookmarks: 276; isReply: 0

The world runs on TypeScript & JavaScript. 

Our bet is that AI engineering will follow suit. The growth in @aisdk downloads and adoption has been astonishing.

When we wrote the Ship AI keynote it was at 3.4M weekly downloads. A couple weeks later, it’s now at 4.1M 😳 

https://t.co/NnTzKYc2go

当今世界建立在 TypeScript 和 JavaScript 的基础之上。

我们预测，AI 工程的发展也将走上同样的道路。@aisdk 的下载量与采用率增长迅猛，令人惊叹。

在我们撰写 Ship AI 主题演讲时，其周下载量为 340 万。仅仅几周之后，这个数字已经攀升至 410 万 😳

https://t.co/NnTzKYc2go

### 828

作者: @Guillermo-Rauch
时间: 2025-10-30
链接: https://x.com/rauchg/status/1983972888295436707
互动: Likes: 11; Retweets: 0; Replies: 2; Quotes: 0; Views: 1,678; Bookmarks: 0; isReply: 1

@ZachWarunek @chat Have you heard of XChat

@ZachWarunek @chat 你们知道 XChat 吗？

### 829

作者: @Guillermo-Rauch
时间: 2025-10-30
链接: https://x.com/rauchg/status/1983979769281892618
互动: Likes: 1; Retweets: 1; Replies: 0; Quotes: 0; Views: 80; Bookmarks: 0; isReply: 1

@metapog @v0 @FernandoTheRojo Driving under the influence of v0. W

@metapog @v0 @FernandoTheRojo 这简直是在 v0 的「加持」下飙车啊。

### 830

作者: @Guillermo-Rauch
时间: 2025-10-30
链接: https://x.com/rauchg/status/1983982600726442338
互动: Likes: 115; Retweets: 0; Replies: 7; Quotes: 0; Views: 13,226; Bookmarks: 63; isReply: 1

What would it take for react-strict-dom to be good enough for this app?

What API changes on the v0 side did introducing a non-@nextjs client drive? What role did @mrlubos’ https://t.co/GxjjHTJciY play?

What’s the ideal monorepo starter kit for this trifecta of next + rn/expo + api w/ sdk?

What were the codesharing opportunities if any? Which ones are the most immediate future ones?

How many times did Apple reject our submission and why? 😡

要让 react-strict-dom 足够适用于这个应用，需要满足哪些条件？

引入一个非 @nextjs 的客户端，给 v0 端带来了哪些 API 变更？@mrlubos 的链接（https://t.co/GxjjHTJciY）在其中起到了什么作用？

对于 Next.js + React Native/Expo + 带 SDK 的 API 这套技术组合，理想的 monorepo 启动模板是什么？

存在哪些代码共享的机会（如果有的话）？其中哪些是近期最直接的机会？

苹果拒绝了我们多少次上架申请？原因是什么？😡

### 831

作者: @Guillermo-Rauch
时间: 2025-10-30
链接: https://x.com/rauchg/status/1983983092705673313
互动: Likes: 20; Retweets: 0; Replies: 3; Quotes: 0; Views: 3,633; Bookmarks: 0; isReply: 1

@FernandoTheRojo @v0 @nextjs @mrlubos How do I get that Gengar wallpaper?

@FernandoTheRojo @v0 @nextjs @mrlubos 那个耿鬼的壁纸怎么弄啊？

### 832

作者: @Guillermo-Rauch
时间: 2025-10-30
链接: https://x.com/rauchg/status/1983984554345111957
互动: Likes: 2; Retweets: 0; Replies: 2; Quotes: 0; Views: 7,475; Bookmarks: 1; isReply: 1

@ZachWarunek @XHandles @zach how much for your handle

@ZachWarunek @XHandles @zach 你的（用户）名卖多少钱？

### 833

作者: @Guillermo-Rauch
时间: 2025-10-30
链接: https://x.com/rauchg/status/1983984950786584911
互动: Likes: 11; Retweets: 0; Replies: 2; Quotes: 0; Views: 3,116; Bookmarks: 0; isReply: 1

@ethanniser had a huge love affair with it over 10 years ago. Was great in theory

@ethanniser 在十多年前曾对它痴迷不已。从理论上讲，它当时确实很出色。

### 834

作者: @Guillermo-Rauch
时间: 2025-10-30
链接: https://x.com/rauchg/status/1983985761243525437
互动: Likes: 9; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,141; Bookmarks: 0; isReply: 1

@ethanniser Ripped it out a few months later :P hard to debug, niche ecosystem, bad support for JS clients at the time

@ethanniser 几个月后我就弃用了 :P 主要是太难调试、生态小众，而且当时对 JavaScript 客户端的支持也很差。

### 835

作者: @Guillermo-Rauch
时间: 2025-10-30
链接: https://x.com/rauchg/status/1983988395471958217
互动: Likes: 17; Retweets: 0; Replies: 0; Quotes: 0; Views: 3,592; Bookmarks: 0; isReply: 1

@raul_dronca @motiondotdev V cool

@raul_dronca @motiondotdev 太酷了

### 836

作者: @Guillermo-Rauch
时间: 2025-10-30
链接: https://x.com/rauchg/status/1983989301869519284
互动: Likes: 2; Retweets: 0; Replies: 0; Quotes: 0; Views: 221; Bookmarks: 0; isReply: 1

@hoeg_jakob @FernandoTheRojo @v0 @nextjs @mrlubos Who isn’t!?

@hoeg_jakob @FernandoTheRojo @v0 @nextjs @mrlubos 谁不是啊！？

### 837

作者: @Guillermo-Rauch
时间: 2025-10-30
链接: https://x.com/rauchg/status/1983995447309123839
互动: Likes: 10; Retweets: 0; Replies: 1; Quotes: 0; Views: 3,661; Bookmarks: 0; isReply: 1

@RhysSullivan @blimptracker account powered by @WorkflowDevKit — you have 5 minutes

@RhysSullivan @blimptracker 这个账户由 @WorkflowDevKit 驱动 — 你还有 5 分钟时间。

### 838

作者: @Guillermo-Rauch
时间: 2025-10-30
链接: https://x.com/rauchg/status/1983996109740785961
互动: Likes: 72; Retweets: 1; Replies: 3; Quotes: 1; Views: 14,766; Bookmarks: 6; isReply: 1

@ScottMcMullan10 @aisdk Because it’s not in the top 5 is my guess https://t.co/wkpfhsfVwf

@ScottMcMullan10 @aisdk 我猜是因为它没进前五名吧 https://t.co/wkpfhsfVwf

### 839

作者: @Guillermo-Rauch
时间: 2025-10-30
链接: https://x.com/rauchg/status/1983999114175304161
互动: Likes: 27; Retweets: 0; Replies: 5; Quotes: 1; Views: 3,116; Bookmarks: 3; isReply: 1

@ScottMcMullan10 @aisdk I can’t think of a better indicator than GitHub. Detecting the stack on websites is incredibly unreliable. Most languages and backends don’t show up in headers

@ScottMcMullan10 @aisdk 我实在想不出比 GitHub 更好的指标了。检测网站所用的技术栈是极其不可靠的。大多数编程语言和后端技术都不会在 HTTP 头部信息中暴露。

### 840

作者: @Guillermo-Rauch
时间: 2025-10-30
链接: https://x.com/rauchg/status/1984007994150175210
互动: Likes: 171; Retweets: 0; Replies: 8; Quotes: 2; Views: 38,625; Bookmarks: 12; isReply: 1

@marc_louvion How do you ship so fast

@marc_louvion 你的交付速度怎么这么快？

### 841

作者: @Guillermo-Rauch
时间: 2025-10-31
链接: https://x.com/rauchg/status/1984061493785325663
互动: Likes: 82; Retweets: 0; Replies: 7; Quotes: 0; Views: 4,055; Bookmarks: 1; isReply: 1

@samirande_ you may have started a mini design trend

@samirande_ 你可能引领了一股设计小风潮。

### 842

作者: @Guillermo-Rauch
时间: 2025-10-31
链接: https://x.com/rauchg/status/1984087679433142675
互动: Likes: 1,137; Retweets: 62; Replies: 122; Quotes: 42; Views: 230,048; Bookmarks: 785; isReply: 0

We should not try to make AI agents into something more complex than they are.

Technically speaking, an agent is a workflow. Many agents are crons, of which workflows are a superset.

Because agents are workflows, we’ve seen a renaissance of workflow builders: Zapier, n8n, etc

Whether you build an agent visually or with code, underpinning the workflow there must be an engine and infrastructure that makes it reliable. A workflow is a different kind of software than a web server. It’s not request-response. It consists of many steps, can fail a lot and is expected to recover, it can run for a very long time.

This is why we’re so excited about @WorkflowDevKit. An agent is just “𝚞𝚜𝚎 𝚠𝚘𝚛𝚔𝚏𝚕𝚘𝚠”. Pair it with @aisdk (where each tool call is an “𝚞𝚜𝚎 𝚜𝚝𝚎𝚙”), AI Gateway for token reliability, and Fluid for efficient compute… and you have all you need to build the future of software.

我们不应试图将 AI 智能体（AI Agent）过度复杂化。

从技术本质上看，一个智能体就是一个工作流。许多智能体实际上是定时任务（cron），而工作流则是这类定时任务的超集。

正因为智能体即工作流，我们见证了工作流构建工具的再度兴起：例如 Zapier、n8n 等平台。

无论你通过可视化界面还是编写代码来构建智能体，其底层都需要一个确保工作流可靠运行的引擎和基础设施。工作流是一种不同于 Web 服务器的软件形态，它并非简单的请求 - 响应模式。一个工作流通常包含多个步骤，可能频繁出错但需具备恢复能力，并且往往需要长时间运行。

这正是我们对 @WorkflowDevKit 感到如此兴奋的原因。构建一个智能体，本质上就是「运用工作流」。将其与 @aisdk 结合（其中每次工具调用都视为一个「步骤」），再通过 AI Gateway 确保 Token 调用的稳定性，并利用 Fluid 实现高效计算…… 如此一来，你便拥有了构建未来软件所需的全部核心要素。

### 843

作者: @Guillermo-Rauch
时间: 2025-10-31
链接: https://x.com/rauchg/status/1984116978995622081
互动: Likes: 339; Retweets: 5; Replies: 21; Quotes: 3; Views: 292,102; Bookmarks: 41; isReply: 1

@ZachWarunek I’m seeing it. There’s something about @nikitabier’s new webview that makes webapps feel native to the platform. True “everything app” material.

@ZachWarunek 我也注意到了。@nikitabier 的新 webview 确实有它的独到之处，能让网页应用获得近乎原生的平台体验。这真有成为「万能应用」的潜质。

### 844

作者: @Guillermo-Rauch
时间: 2025-10-31
链接: https://x.com/rauchg/status/1984246185838915946
互动: Likes: 39; Retweets: 0; Replies: 7; Quotes: 1; Views: 4,104; Bookmarks: 1; isReply: 1

@maelus_ @AnthropicAI Whether the steps are dynamically generated or not doesn’t change the fact that you’ll need reliable orchestration under the hood. Still a workflow :/

@maelus_ @AnthropicAI 步骤是不是动态生成的，都改变不了你底下总得有一套可靠的编排机制。说到底，它还是个工作流啊 :/

### 845

作者: @Guillermo-Rauch
时间: 2025-10-31
链接: https://x.com/rauchg/status/1984292782639296897
互动: Likes: 1; Retweets: 0; Replies: 1; Quotes: 0; Views: 91; Bookmarks: 0; isReply: 1

@lukerramsden @thefubhy Correct

@lukerramsden @thefubhy 对的。

### 846

作者: @Guillermo-Rauch
时间: 2025-10-31
链接: https://x.com/rauchg/status/1984307649668645320
互动: Likes: 106; Retweets: 1; Replies: 9; Quotes: 1; Views: 17,149; Bookmarks: 5; isReply: 1

@jpschroeder Both, but TS has a much higher ceiling. Will unlock tens of millions of developers to ship AI and build agents

两者都是，但 TypeScript 的潜力要大得多。它将使数千万开发者能够轻松部署 AI 应用并构建 AI 智能体。

### 847

作者: @Guillermo-Rauch
时间: 2025-10-31
链接: https://x.com/rauchg/status/1984333557775434047
互动: Likes: 176; Retweets: 11; Replies: 14; Quotes: 0; Views: 56,704; Bookmarks: 80; isReply: 0

Ship the org chart.
(without the drawbacks)

Now powering @vercel & @v0, @cursor_ai, @weatherchannel, @onepeloton, @aetv, and 250+ teams.

I was once upon a time a microfrontends skeptic. But as companies grow, the need to slice up workloads and unblock teams & departments is undeniable.

Our CDN and CI/CD teams have done a fantastic job at mitigating the DX and UX pitfalls, while allowing these companies to ship fast.

交付「组织架构图」方案。
（且规避了其常见缺陷）

目前，该方案正为 @vercel & @v0，@cursor_ai，@weatherchannel，@onepeloton，@aetv 以及超过 250 个团队提供支持。

我曾经也是微前端（Microfrontends）架构的怀疑者。但随着企业规模的增长，分割工作负载、打通团队与部门间协作壁垒的需求变得毋庸置疑。

我们的 CDN 和 CI/CD 团队做出了卓越的贡献，他们有效地缓解了微前端在开发体验（DX）和用户体验（UX）上的潜在问题，从而助力这些公司实现了快速交付。

### 848

作者: @Guillermo-Rauch
时间: 2025-10-31
链接: https://x.com/rauchg/status/1984335212999032889
互动: Likes: 6; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,468; Bookmarks: 0; isReply: 1

@puppeteer_0 @vercel @v0 @cursor_ai @weatherchannel @onepeloton @AETV It’s framework-agnostic. 

The codebase itself remains fully portable. The CDN and CI/CD portions are part of the Vercel platform.

We open sourced the local DX as part of @turborepo:
https://t.co/DswfSeeqvl

@puppeteer_0 @vercel @v0 @cursor_ai @weatherchannel @onepeloton @AETV 它是框架无关的。

其代码库本身是完全可移植的。CDN 和 CI/CD 功能则属于 Vercel 平台的一部分。

我们已将本地开发体验（DX）作为 @turborepo 的一部分开源：
https://t.co/DswfSeeqvl

### 849

作者: @Guillermo-Rauch
时间: 2025-10-31
链接: https://x.com/rauchg/status/1984335658538902006
互动: Likes: 3; Retweets: 0; Replies: 0; Quotes: 0; Views: 781; Bookmarks: 2; isReply: 1

@yungbzz @vercel @v0 @cursor_ai @weatherchannel @onepeloton @AETV You can unblock teams to build and deploy parts of an application independently. Ship faster.

To the end user, we deliver one cohesive experience. To the developers and operators, we merge them under one DX that “feels” like a monolith.

@yungbzz @vercel @v0 @cursor_ai @weatherchannel @onepeloton @AETV 您可以解除团队间的协作限制，让各团队能够独立构建和部署应用程序的不同模块，从而加快交付速度。

对于最终用户，我们交付的是一个完整、统一的无缝体验。对于开发与运维人员，我们则将这些独立模块整合到一个「感觉」上如同单体应用的统一开发者体验（DX）之中。

### 850

作者: @Guillermo-Rauch
时间: 2025-10-31
链接: https://x.com/rauchg/status/1984352666252607813
互动: Likes: 9; Retweets: 0; Replies: 3; Quotes: 1; Views: 3,453; Bookmarks: 2; isReply: 1

@HanchungLee In the rigorous definition sense, and in the pragmatic sense. OpenAI's new "Agent Builder" is a… workflow builder. https://t.co/3zROfwcxqg

无论是从严格的定义来看，还是从实际应用的角度来说，OpenAI 新推出的「Agent Builder」都是一个… 工作流构建工具。https://t.co/3zROfwcxqg

### 851

作者: @Guillermo-Rauch
时间: 2025-10-31
链接: https://x.com/rauchg/status/1984366735059755133
互动: Likes: 3; Retweets: 0; Replies: 2; Quotes: 0; Views: 2,025; Bookmarks: 0; isReply: 1

◆ Definitionally, a workflow doesn't have to have a fixed or static set of steps
◆ What users think when they think of "agent" is the entire workflow from event that kicks it off (prompt, sales form, phone call) to outcome

◆ 从定义上讲，一个工作流并不必须包含一系列固定或静态的步骤。
◆ 用户心目中的「AI 智能体（AI Agent）」，指的是从触发事件（例如：提示词（prompt）、销售表单、电话呼入）开始，直至产生最终结果的完整工作流程。

### 852

作者: @Guillermo-Rauch
时间: 2025-10-31
链接: https://x.com/rauchg/status/1984375395517677964
互动: Likes: 1; Retweets: 0; Replies: 1; Quotes: 0; Views: 76; Bookmarks: 0; isReply: 1

@HenriHelvetica @youngbloodcyb We almost *died on that hill* 😆

我们当时差点就 * 固执到底了 * 😆

### 853

作者: @Guillermo-Rauch
时间: 2025-10-31
链接: https://x.com/rauchg/status/1984382955670945993
互动: Likes: 196; Retweets: 14; Replies: 16; Quotes: 3; Views: 17,436; Bookmarks: 31; isReply: 0

"The details are not the details. They make the design"
― Charles Eames

"细节并非琐碎，它们铸就了设计。"
― Charles Eames

### 854

作者: @Guillermo-Rauch
时间: 2025-10-31
链接: https://x.com/rauchg/status/1984387156669018314
互动: Likes: 25; Retweets: 0; Replies: 3; Quotes: 0; Views: 10,557; Bookmarks: 0; isReply: 1

@AIbrahmiRealm @aisdk The chart is number of developers on github chief

这张图表显示的是 GitHub 上的开发者数量。

### 855

作者: @Guillermo-Rauch
时间: 2025-10-31
链接: https://x.com/rauchg/status/1984392683650007232
互动: Likes: 110; Retweets: 5; Replies: 5; Quotes: 1; Views: 32,909; Bookmarks: 36; isReply: 0

Awesome behind-the-scenes of how Vercel's BotID detects anomalies in browser fingerprints, uncovering a sophisticated botnet.

In realtime, we re-classify traffic from human 🟣 to bot 🔵. Subsequent attacks are thwarted for everyone.

To protect yourself:
◆ Turn on Vercel Bot Protection for instant filtering of basic bots (e.g.: 𝚠𝚛𝚔, 𝚏𝚎𝚝𝚌𝚑, 𝚙𝚢𝚝𝚑𝚘𝚗 scripts, clients lying about being real web browsers, etc)
◆ Use the BotID SDK to protect high-value routes (e.g. checkout, signup, free AI demos, etc) from advanced attacks like this one.

深入幕后：揭秘 Vercel 的 BotID 如何通过检测浏览器指纹异常，揪出一个复杂的僵尸网络。

该系统能够实时将流量从人类用户 🟣 重新判定为恶意机器人 🔵。这样一来，后续的攻击便能被拦截，保护所有用户。

如何进行防护：
◆ 启用 Vercel Bot Protection，即可实时过滤基础机器人（例如：使用 𝚠𝚛𝚔、𝚏𝚎𝚝𝚌𝚑、𝚙𝚢𝚝𝚑𝚘𝚗 脚本的工具，或伪装成真实浏览器的客户端等）。
◆ 使用 BotID SDK 保护你的关键业务路径（例如：支付结算、用户注册、免费 AI 演示等），抵御此类高级攻击。

### 856

作者: @Guillermo-Rauch
时间: 2025-10-31
链接: https://x.com/rauchg/status/1984401440417194194
互动: Likes: 780; Retweets: 6; Replies: 53; Quotes: 5; Views: 83,012; Bookmarks: 24; isReply: 0

Who’s going as Soham Parekh tonight? 👻

今晚谁来扮 Soham Parekh 呀？👻

### 857

作者: @Guillermo-Rauch
时间: 2025-10-31
链接: https://x.com/rauchg/status/1984404920297296321
互动: Likes: 54; Retweets: 0; Replies: 2; Quotes: 0; Views: 11,521; Bookmarks: 4; isReply: 1

@fede_intern Peak satire 😂 but most replies seem to believe it?

&gt; We had 47 active connections during peak traffic.

And

&gt; 127,000USD

@fede_intern 这讽刺效果拉满了 😂 但好像大多数回复都当真了？

&gt; 我们在流量最高峰的时候，也只有 47 个活跃连接。

以及

&gt; 127,000 美元

### 858

作者: @Guillermo-Rauch
时间: 2025-10-31
链接: https://x.com/rauchg/status/1984405147934449749
互动: Likes: 349; Retweets: 0; Replies: 4; Quotes: 0; Views: 10,970; Bookmarks: 1; isReply: 1

@RhysSullivan I liked thinking it was bait, but it’s really nice

@RhysSullivan 我本来还觉得这是个钓鱼帖呢，不过结果还真不错。

### 859

作者: @Guillermo-Rauch
时间: 2025-10-31
链接: https://x.com/rauchg/status/1984405831144570883
互动: Likes: 12; Retweets: 0; Replies: 2; Quotes: 0; Views: 999; Bookmarks: 1; isReply: 1

@fede_intern It seems to be a novel kind of ai bait that’s almost-plausible and builds on existing biases / memes to grab eyeballs.

Hard to reconcile Tokio being bad at handling barely any traffic and the db query “blocking”. 1) What.

@fede_intern 这看起来像是一种新型的 AI 炒作噱头，它利用现有的偏见或网络迷因，制造出一种乍看还挺可信的效果来博取关注。

一方面说 Tokio 在流量极低的情况下都表现糟糕，另一方面又说数据库查询会「阻塞」，这很难说得通。1）什么情况？

### 860

作者: @Guillermo-Rauch
时间: 2025-10-31
链接: https://x.com/rauchg/status/1984406742621397354
互动: Likes: 8; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,003; Bookmarks: 3; isReply: 1

@fede_intern Mixing and matching async I/O and blocking I/O is a universal footgun. This sounds precisely what Tokio was conceived to address: https://t.co/tUgFD30dHY

@fede_intern 将异步 I/O 和阻塞 I/O 混用，是个普遍存在的「自找麻烦」的陷阱。这听起来正是 Tokio 设计之初要解决的问题：https://t.co/tUgFD30dHY

### 861

作者: @Guillermo-Rauch
时间: 2025-10-31
链接: https://x.com/rauchg/status/1984407733144093078
互动: Likes: 3; Retweets: 0; Replies: 0; Quotes: 0; Views: 492; Bookmarks: 0; isReply: 1

@fede_intern Yeah I was mostly reminiscing on the nature of bait 😆

@fede_intern 哈哈，我主要是在琢磨「钓鱼」这事儿到底啥意思 😆

### 862

作者: @Guillermo-Rauch
时间: 2025-11-01
链接: https://x.com/rauchg/status/1984410719182356776
互动: Likes: 100; Retweets: 0; Replies: 3; Quotes: 0; Views: 7,492; Bookmarks: 1; isReply: 1

@v0intern Too far v0 intern

@v0intern 太过火了吧 v0 实习生

### 863

作者: @Guillermo-Rauch
时间: 2025-11-01
链接: https://x.com/rauchg/status/1984428579606634758
互动: Likes: 614; Retweets: 27; Replies: 23; Quotes: 3; Views: 166,934; Bookmarks: 421; isReply: 0

Cache Components bring back one of the fundamental insights and Ws of Pages Router.

In Pages Router, data fetching confronted you with an explicit choice: to 𝚐𝚎𝚝𝚂𝚝𝚊𝚝𝚒𝚌𝙿𝚛𝚘𝚙𝚜 or to 𝚐𝚎𝚝𝚂𝚎𝚛𝚟𝚎𝚛𝚂𝚒𝚍𝚎𝙿𝚛𝚘𝚙𝚜.

Now, <𝚂𝚞𝚜𝚙𝚎𝚗𝚜𝚎> or "𝚞𝚜𝚎 𝚌𝚊𝚌𝚑𝚎" is your choice, prompted by an error when you do dynamic I/O. The most delightful "error" of all time, if you ask me. It's an error that makes you or your agent choose.

What's more, gSSP had a fatal flaw: no instant 'loading' state to navigate to. Using <𝚂𝚞𝚜𝚙𝚎𝚗𝚜𝚎> gives you the opportunity to set a 𝚏𝚊𝚕𝚕𝚋𝚊𝚌𝚔={} (or 𝚕𝚘𝚊𝚍𝚒𝚗𝚐.𝚝𝚜𝚡).

Combined with single-roundtrip data fetching and streaming, I believe this achieves the pinnacle of performance. We're so back.

Cache Components 重新引入了 Pages Router 的一个核心理念及其优势。

在 Pages Router 中，数据获取要求你做出一个明确的抉择：是使用 `getStaticProps` 还是 `getServerSideProps`。

如今，在 App Router 中，`<Suspense>` 或「使用缓存（use cache）」成为了你的选择，当你进行动态数据操作时会触发一个错误提示。要我说，这简直是有史以来最贴心的「错误」。它是一个促使你（或你的 AI 智能体（AI Agent)）做出决策的错误。

更重要的是，`getServerSideProps`（gSSP）曾有一个致命缺陷：在页面导航时，没有即时的「加载中（loading）」状态可以显示。而使用 `<Suspense>` 则让你能够设置一个 `fallback={}`（或 `loading.tsx`）作为回退界面。

结合单次往返的数据获取与流式渲染，我相信这实现了性能的巅峰。我们终于强势回归了。

### 864

作者: @Guillermo-Rauch
时间: 2025-11-01
链接: https://x.com/rauchg/status/1984435527307968733
互动: Likes: 327; Retweets: 12; Replies: 16; Quotes: 4; Views: 68,615; Bookmarks: 53; isReply: 0

One of my favorite recent additions in @nextjs is the precise time attribution of compiler/framework vs userspace.

Basically 🔵 framework code vs 🔴 your code.

One of the consequences of @nextjs being so popular (13M weekly downloads) is that you get to field a *lot* of 𝕏 posts and feedback on performance that's a bit… light on details.

Prior to this change, it was very easy to conflate:
▪️ the compiler taking long
▪️ your 𝚙𝚛𝚘𝚡𝚢.𝚝𝚜 being slow
▪️ your database being slow
▪️ your internet being slow
▪️ rendering a huge component tree
▪️ … 
you get the gist.

Subtleties like this are make-or-break for devtools and platforms. Attribute time wisely.

我最近特别喜欢 @nextjs 新增的一个功能：能够精确划分编译器 / 框架代码与用户代码的执行时间。

简单来说，就是区分 🔵 框架代码和 🔴 你的代码。

@nextjs 非常流行（每周下载量达 1300 万次），这带来一个结果：你会看到大量关于性能的 𝕏 帖子和反馈，但这些反馈往往缺乏具体细节。

在此功能推出之前，很容易将以下原因混为一谈：
▪️ 编译器本身耗时过长
▪️ 你的 `proxy.ts` 文件运行缓慢
▪️ 你的数据库响应慢
▪️ 你的网络连接速度不佳
▪️ 渲染一个庞大的组件树
▪️ ……
诸如此类。

对于开发工具和平台而言，能否厘清这些细微差别至关重要。必须准确地进行时间归因。

### 865

作者: @Guillermo-Rauch
时间: 2025-11-01
链接: https://x.com/rauchg/status/1984439132492546149
互动: Likes: 22; Retweets: 0; Replies: 0; Quotes: 0; Views: 4,032; Bookmarks: 0; isReply: 1

That's right! But independent of your code. Whereas render is your code (and proxy.ts, if it's there).

The point is that you can ~mostly¹ blame us for "compile", but the rest is on you.

Previously people would come to me with "you $&#)! Next.js is not fast!" and then it'd be their database. Like a dev making 20 db roundtrips from a remote country to us-east-1.

¹ This will be 100% true once the incremental persistent caches are enabled, bc technically you have *some* to blame if you import massive module trees etc.

说得对！但这不关你写的代码的事。而渲染（render）这部分，可是你的代码（以及 proxy.ts，如果有的话）负责的。

重点是，对于「编译（compile）」环节，你大可以 ¹ 把锅甩给我们，但剩下的部分就得你自己背了。

以前总有人跑来跟我说：「你们 $&#)！Next.js 太慢了！」结果问题出在他们的数据库上。就好比有个开发者，从遥远的国家连接到 us-east-1 数据中心，却发起了 20 次数据库往返查询。

¹ 等增量持久化缓存（incremental persistent caches）启用后，这话就 100% 正确了。因为到那时，如果你引入了庞大的模块树之类的，那责任可就在你这边了。

### 866

作者: @Guillermo-Rauch
时间: 2025-11-01
链接: https://x.com/rauchg/status/1984441024362795039
互动: Likes: 1; Retweets: 0; Replies: 0; Quotes: 0; Views: 308; Bookmarks: 0; isReply: 1

@beantown_man @vercel @v0 @cursor_ai @weatherchannel @onepeloton @AETV Regardless of 'methodology' or abstraction, this completely decouples the build &amp; deploy pipelines of each team. It disentangles dependencies and creates hard boundaries.

In simple terms, it helps teams ship w/o obstructions.

@beantown_man @vercel @v0 @cursor_ai @weatherchannel @onepeloton @AETV 无论采用何种「方法论」或抽象概念，这种做法都能将每个团队的构建和部署流水线彻底分离开来。它消除了团队间的依赖，并划出了清晰的界限。

简单来说，这能让各个团队顺畅地发布产品，不受阻碍。

### 867

作者: @Guillermo-Rauch
时间: 2025-11-01
链接: https://x.com/rauchg/status/1984442317076644107
互动: Likes: 6; Retweets: 0; Replies: 1; Quotes: 0; Views: 248; Bookmarks: 0; isReply: 1

@DanielPetroAI @RhysSullivan 😂 same to you

@DanielPetroAI @RhysSullivan 😂 彼此彼此！

### 868

作者: @Guillermo-Rauch
时间: 2025-11-01
链接: https://x.com/rauchg/status/1984442828207042739
互动: Likes: 686; Retweets: 21; Replies: 55; Quotes: 7; Views: 48,594; Bookmarks: 39; isReply: 0

Happy Halloween! 👻 https://t.co/sHZF527NjG

万圣节快乐！👻 https://t.co/sHZF527NjG

### 869

作者: @Guillermo-Rauch
时间: 2025-11-01
链接: https://x.com/rauchg/status/1984461230850130280
互动: Likes: 6; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,968; Bookmarks: 0; isReply: 1

@alanaagoyal So good 😆

@alanaagoyal 太棒了 😆

### 870

作者: @Guillermo-Rauch
时间: 2025-11-01
链接: https://x.com/rauchg/status/1984462112257949817
互动: Likes: 4; Retweets: 0; Replies: 1; Quotes: 0; Views: 3,323; Bookmarks: 0; isReply: 1

@garyfung For real. New beginning

@garyfung 确实。全新的开始。

### 871

作者: @Guillermo-Rauch
时间: 2025-11-01
链接: https://x.com/rauchg/status/1984465768101347811
互动: Likes: 16; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,008; Bookmarks: 0; isReply: 1

@zayn_harris_dev @nextjs More to come — just the beginning for prod builds

敬请期待更多 —— 这仅仅是生产构建的起点。

### 872

作者: @Guillermo-Rauch
时间: 2025-11-01
链接: https://x.com/rauchg/status/1984654068959314046
互动: Likes: 226; Retweets: 3; Replies: 30; Quotes: 0; Views: 17,996; Bookmarks: 3; isReply: 0

Nothing better than analyzing your Halloween haul the following day 😆 https://t.co/TOCnBDZMfA

节后清点万圣节「战利品」，没有比这更开心的事了 😆 https://t.co/TOCnBDZMfA

### 873

作者: @Guillermo-Rauch
时间: 2025-11-01
链接: https://x.com/rauchg/status/1984682377193652554
互动: Likes: 85; Retweets: 7; Replies: 3; Quotes: 0; Views: 15,022; Bookmarks: 66; isReply: 1

@marc_louvion Check out @corridorsecure who just joined our marketplace and they do security analyses that run before a Vercel deployment can be promoted to prod:
https://t.co/PmVMMPeFID

@marc_louvion 快来看看刚刚加入我们市场的 @corridorsecure，他们能在 Vercel 部署上线生产前，自动运行安全分析：
https://t.co/PmVMMPeFID

### 874

作者: @Guillermo-Rauch
时间: 2025-11-01
链接: https://x.com/rauchg/status/1984691112049873068
互动: Likes: 2; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,517; Bookmarks: 2; isReply: 1

@infodusha No because you might not always want Suspense everywhere. You might want to cache! Which can give you really really fast *contentful* transitions (think docs, marketing pages, marketplaces, etc). And opts you into partial pre-rendering. 

Hence why the explicit choice is good

@infodusha 不，因为你可能并不总是希望到处都用 Suspense。你可能想要的是缓存！缓存能带来极快、** 内容完整 ** 的页面过渡（想想文档站、营销页、电商平台页面等等）。并且它能让你启用部分预渲染（partial pre-rendering）功能。

因此，提供一个明确的选择是件好事。

### 875

作者: @Guillermo-Rauch
时间: 2025-11-01
链接: https://x.com/rauchg/status/1984691830890643631
互动: Likes: 28; Retweets: 0; Replies: 3; Quotes: 0; Views: 3,970; Bookmarks: 0; isReply: 1

@eaoliver @vercel @v0 Yes, being fixed

@eaoliver @vercel @v0 是的，问题正在修复中。

### 876

作者: @Guillermo-Rauch
时间: 2025-11-01
链接: https://x.com/rauchg/status/1984692162731393340
互动: Likes: 1; Retweets: 0; Replies: 1; Quotes: 0; Views: 261; Bookmarks: 0; isReply: 1

@infodusha Yeah the power of this paradigm is being able to mix and match cached vs dynamic in one screen

@infodusha 确实，这种模式（范式）的强大之处在于，它能让我们在同一个界面里，灵活地组合使用缓存内容和动态内容。

### 877

作者: @Guillermo-Rauch
时间: 2025-11-01
链接: https://x.com/rauchg/status/1984731736094490892
互动: Likes: 554; Retweets: 24; Replies: 26; Quotes: 2; Views: 79,457; Bookmarks: 263; isReply: 0

All you have to learn to make the fastest application in the world: 𝚊𝚠𝚊𝚒𝚝, &lt;𝚂𝚞𝚜𝚙𝚎𝚗𝚜𝚎&gt; and “𝚞𝚜𝚎 𝚌𝚊𝚌𝚑𝚎”. https://t.co/zlp9OYdo6C

要开发出世界上最快的应用，你只需掌握三样东西：𝚊𝚠𝚊𝚒𝚝，&lt;𝚂𝚞𝚜𝚙𝚎𝚗𝚜𝚎&gt; 和「𝚞𝚜𝚎 𝚌𝚊𝚌𝚑𝚎」。https://t.co/zlp9OYdo6C

### 878

作者: @Guillermo-Rauch
时间: 2025-11-01
链接: https://x.com/rauchg/status/1984754453304742147
互动: Likes: 1; Retweets: 0; Replies: 0; Quotes: 0; Views: 123; Bookmarks: 0; isReply: 1

@nomoredevwork @MichaelFrieze Would love to hear a concrete product use case and would love to see how to solve it with RSC!

@nomoredevwork @MichaelFrieze 非常期待能听到一个具体的产品应用场景，并且很想看看如何用 RSC（React Server Components）来实现它！

### 879

作者: @Guillermo-Rauch
时间: 2025-11-01
链接: https://x.com/rauchg/status/1984756744955035998
互动: Likes: 11; Retweets: 0; Replies: 1; Quotes: 0; Views: 669; Bookmarks: 0; isReply: 1

Quite the opposite, the framework is not perfect, so this brings clarity to us as well. e.g: someone reached out with a very large “compile” time and the Turbopack team is helping.

I also mentioned at the end that there’s more work to do for us. Once persistent caching is enabled by default, the numbers will drop even further especially for super large apps.

恰恰相反，这个框架并不完美，所以这也让我们更清楚地看到了问题所在。例如，有用户反馈遇到了极长的「编译」时间，目前 Turbopack 团队正在协助解决。

我在结尾处也提到，我们还有很多工作要做。一旦持久缓存（persistent caching）被默认启用，各项性能指标（尤其是编译时间）还会进一步下降，对于超大型应用来说效果将尤为明显。

### 880

作者: @Guillermo-Rauch
时间: 2025-11-02
链接: https://x.com/rauchg/status/1985017631162945920
互动: Likes: 5; Retweets: 0; Replies: 3; Quotes: 0; Views: 1,139; Bookmarks: 0; isReply: 1

@complex_maths @AdamRackis @leerob We briefly used workers for middleware and edge functions. Hit too many limitations. It’s actually worse DX and worse perf. Some thoughts here:

@complex_maths @AdamRackis @leerob 我们曾短暂使用 Workers（特指 Cloudflare Workers 等服务）来处理中间件和边缘函数。但遇到的限制实在太多了。实际上，无论是开发体验（Developer Experience，简称 DX）还是运行性能（Performance，简称 perf）都变得更差。以下是我的一些看法：

### 881

作者: @Guillermo-Rauch
时间: 2025-11-02
链接: https://x.com/rauchg/status/1985035562882114042
互动: Likes: 993; Retweets: 44; Replies: 93; Quotes: 11; Views: 387,758; Bookmarks: 661; isReply: 0

We’re making a new https://t.co/C2q4ESzL6K built on latest Next 16 features (𝚌𝚊𝚌𝚑𝚎𝙲𝚘𝚖𝚙𝚘𝚗𝚎𝚗𝚝𝚜).

Think of it as an OSS amazon.​com

The focus will be on extraordinary performance and push even further on complexity (i18n, experiments, ai search, UGC…). Even 🍪 banners.

Very excited bc most demos err on being too simplistic. TODO lists ain’t it. Ignoring requirements whose voids teams fill with third-party script slot ain’t it.

我们正在利用最新的 Next.js 16 特性（缓存组件，cacheComponents）打造一个全新的网站（链接：https://t.co/C2q4ESzL6K）。

你可以把它想象成一个开源版的 Amazon.com。

我们的核心目标是实现非凡的性能，并在处理复杂性方面更进一步，例如国际化（i18n）、A/B 测试、AI 搜索、用户生成内容（UGC）… 甚至包括 Cookie（🍪）提示横幅。

对此我感到非常兴奋，因为大多数技术演示都过于简单化了。只做个待办事项列表可不行。忽视实际需求、让开发团队不得不引入第三方脚本片段来填补功能空缺的做法，也同样不可取。

### 882

作者: @Guillermo-Rauch
时间: 2025-11-02
链接: https://x.com/rauchg/status/1985050946372788246
互动: Likes: 30; Retweets: 0; Replies: 1; Quotes: 0; Views: 5,421; Bookmarks: 0; isReply: 1

@ayaboch 💯 will be a focus

@ayaboch 💯（满分 / 太棒了）会是重点关注对象。

### 883

作者: @Guillermo-Rauch
时间: 2025-11-02
链接: https://x.com/rauchg/status/1985052131070775441
互动: Likes: 115; Retweets: 1; Replies: 3; Quotes: 0; Views: 9,701; Bookmarks: 7; isReply: 1

@benktz I’d love to see it. We like TanStack, support it on our platform, and competition is good for everyone

@benktz 我很期待。我们喜欢 TanStack，在我们的平台上支持它，竞争对大家都有好处。

### 884

作者: @Guillermo-Rauch
时间: 2025-11-02
链接: https://x.com/rauchg/status/1985053303890493916
互动: Likes: 5; Retweets: 0; Replies: 1; Quotes: 0; Views: 585; Bookmarks: 0; isReply: 1

@ykosyakov @benktz No, they’re 1:1. But it’s good to run small experiments across technologies and see how they feel. And that extends beyond React

不，它们是一一对应的。不过，最好在不同技术栈间做些小实验，亲自体验一下。而且，这个建议并不仅限于 React。

### 885

作者: @Guillermo-Rauch
时间: 2025-11-02
链接: https://x.com/rauchg/status/1985055334785011961
互动: Likes: 63; Retweets: 0; Replies: 5; Quotes: 0; Views: 22,790; Bookmarks: 3; isReply: 1

This website feels so good inside the new @x webviews 🤤 bullish on the web!

在新的 @x WebView 里浏览这个网站，体验太棒了 🤤 我看好 Web 的未来！

### 886

作者: @Guillermo-Rauch
时间: 2025-11-02
链接: https://x.com/rauchg/status/1985056889550574070
互动: Likes: 1; Retweets: 0; Replies: 0; Quotes: 0; Views: 428; Bookmarks: 0; isReply: 1

@AtharvaXDevs @X they cooked

@AtharvaXDevs @X 他们干得漂亮 / 他们太强了

### 887

作者: @Guillermo-Rauch
时间: 2025-11-02
链接: https://x.com/rauchg/status/1985057993722040610
互动: Likes: 13; Retweets: 0; Replies: 1; Quotes: 0; Views: 3,974; Bookmarks: 1; isReply: 1

@YashSolanki_ There are very few meaningful optimizations left. Imagine the world if every e-commerce site was this fast. 

What we’ll do is turn up complexity to demonstrate the paradigm holds up and scales.

It’s already highly dynamic on purpose, and has a huge catalog of products

@YashSolanki_ 有意义的优化已经所剩无几了。想象一下，如果每个电商网站都能这么快，世界会变成什么样。

接下来，我们将提升系统的复杂度，以此来验证这套架构不仅可行，而且具备良好的扩展性。

这个系统本身就是特意设计成高度动态的，并且拥有海量的产品。

### 888

作者: @Guillermo-Rauch
时间: 2025-11-02
链接: https://x.com/rauchg/status/1985058095891190253
互动: Likes: 10; Retweets: 0; Replies: 3; Quotes: 0; Views: 2,164; Bookmarks: 0; isReply: 1

@Sidlavio You likely tripped firewall. There are no rate limits

@Sidlavio 你的请求很可能被防火墙拦截了。我们这边没有设置速率限制。

### 889

作者: @Guillermo-Rauch
时间: 2025-11-02
链接: https://x.com/rauchg/status/1985058224874394067
互动: Likes: 3; Retweets: 0; Replies: 2; Quotes: 0; Views: 945; Bookmarks: 0; isReply: 1

@Sidlavio (Or at least, no implicit rate limits to the platform)

@Sidlavio （或者至少，平台本身没有隐性的速率限制。）

### 890

作者: @Guillermo-Rauch
时间: 2025-11-02
链接: https://x.com/rauchg/status/1985058457599561732
互动: Likes: 4; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,131; Bookmarks: 2; isReply: 1

@antonmoiseev That’s the point though. If you read from the request, you can’t pre-render the CDN shell of the page. You likely want to use &lt;inline&gt; scripts or rewrites/proxy if you want to personalize the shell

@antonmoiseev 不过，关键点就在这里。如果（你的程序）需要从请求中读取信息，那么就无法预先渲染页面的 **CDN 外壳 **（即通过 CDN 交付的页面基础框架）。如果你希望对这层外壳进行个性化处理，那么很可能需要考虑使用 **&lt;inline&gt;**（内联）脚本，或者通过重写规则 / 代理服务器来实现。

### 891

作者: @Guillermo-Rauch
时间: 2025-11-02
链接: https://x.com/rauchg/status/1985058833006571609
互动: Likes: 4; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,939; Bookmarks: 0; isReply: 1

@carnotengine273 The logged in state, cart and orders are all personalized on every page. It’s no different from a dashboard, only that there’s more to cache on the pre-render layer (the items’ content like descriptions and titles).

@carnotengine273 用户的登录状态、购物车和订单信息在每个页面都是个性化的。这其实和一个仪表板（dashboard）的原理没什么不同，只不过在预渲染（pre-render）层需要缓存的内容更多了（主要是商品详情，比如描述和标题这些信息）。

### 892

作者: @Guillermo-Rauch
时间: 2025-11-02
链接: https://x.com/rauchg/status/1985110533151089007
互动: Likes: 3; Retweets: 0; Replies: 0; Quotes: 0; Views: 112; Bookmarks: 0; isReply: 1

@CeolinWill @dobroslav_dev For sure. That one has 1M pages btw

没问题。顺便提一下，那个数据集有 100 万页。

### 893

作者: @Guillermo-Rauch
时间: 2025-11-02
链接: https://x.com/rauchg/status/1985114511976935656
互动: Likes: 7; Retweets: 0; Replies: 2; Quotes: 0; Views: 4,402; Bookmarks: 0; isReply: 1

@gabrielbuzziv Those are authenticated. Try signing up and logging in. Fully personalizable

@gabrielbuzziv 这些功能需要认证。请先注册并登录。支持完全自定义。

### 894

作者: @Guillermo-Rauch
时间: 2025-11-02
链接: https://x.com/rauchg/status/1985131711060193634
互动: Likes: 17; Retweets: 0; Replies: 6; Quotes: 0; Views: 2,561; Bookmarks: 0; isReply: 1

@kacemmmmmm You can always turn prefetching off and make the site slower. Why would you do that though?

@kacemmmmmm 你随时可以关闭预取（prefetching）功能，但这会让网站加载变慢。不过，通常有什么理由要这样做呢？

### 895

作者: @Guillermo-Rauch
时间: 2025-11-03
链接: https://x.com/rauchg/status/1985134856490369297
互动: Likes: 2; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,041; Bookmarks: 0; isReply: 1

@matijagrcic Good summary! thank you

@matijagrcic 总结得很棒！感谢。

### 896

作者: @Guillermo-Rauch
时间: 2025-11-03
链接: https://x.com/rauchg/status/1985162784196501713
互动: Likes: 24; Retweets: 0; Replies: 0; Quotes: 0; Views: 4,168; Bookmarks: 0; isReply: 1

@0interestrates True

@0interestrates 说得对。

### 897

作者: @Guillermo-Rauch
时间: 2025-11-03
链接: https://x.com/rauchg/status/1985174565857959940
互动: Likes: 0; Retweets: 0; Replies: 0; Quotes: 0; Views: 148; Bookmarks: 0; isReply: 1

@chhornponleu @kacemmmmmm It really isn’t. Full cost breakdown on the README (and has since gone down). Drop in the bucket for an ecom site (like it costs one item to pay for the hosting) and this site has gone viral multiple times

@chhornponleu @kacemmmmmm 真不是这样。完整的成本明细都在 README 里写着呢（而且后来成本还降低了）。这点费用对一个电商网站来说根本不算什么（比如，卖出一件商品的收入就足够覆盖托管费了），况且这个网站已经火过好几次了。

### 898

作者: @Guillermo-Rauch
时间: 2025-11-03
链接: https://x.com/rauchg/status/1985177200941998313
互动: Likes: 0; Retweets: 0; Replies: 0; Quotes: 0; Views: 153; Bookmarks: 0; isReply: 1

@PierreArowana @Sidlavio @vercel We posted the costs of the site when it went viral. I just checked for this one and it’s unlikely it’ll go over the $20 bucks per month.

@PierreArowana @Sidlavio @vercel 之前网站流量暴增时，我们公布过它的成本。我刚查了一下这个（网站）的情况，每月成本应该不会超过 20 美元。

### 899

作者: @Guillermo-Rauch
时间: 2025-11-03
链接: https://x.com/rauchg/status/1985190426442428915
互动: Likes: 39; Retweets: 0; Replies: 4; Quotes: 1; Views: 121,887; Bookmarks: 1; isReply: 1

@catnose99 So good. Congrats

@catnose99 太棒了！恭喜恭喜！

### 900

作者: @Guillermo-Rauch
时间: 2025-11-03
链接: https://x.com/rauchg/status/1985201352650391858
互动: Likes: 1; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,157; Bookmarks: 0; isReply: 1

@NikilKuruvilla Can’t repro https://t.co/bYXjV7Hw2v

@NikilKuruvilla 我这边无法复现你提到的问题。链接：https://t.co/bYXjV7Hw2v

### 901

作者: @Guillermo-Rauch
时间: 2025-11-03
链接: https://x.com/rauchg/status/1985203538977526032
互动: Likes: 1; Retweets: 0; Replies: 0; Quotes: 0; Views: 271; Bookmarks: 0; isReply: 1

@NikilKuruvilla That makes sense, they’re likely making it ephemeral

@NikilKuruvilla 有道理，他们很可能就是把它设计成临时性的。

### 902

作者: @Guillermo-Rauch
时间: 2025-11-03
链接: https://x.com/rauchg/status/1985333103393755481
互动: Likes: 1; Retweets: 0; Replies: 1; Quotes: 0; Views: 72; Bookmarks: 0; isReply: 1

@dhruvvjangidd Pretty good, the transitions after pressing Discover and the loading state are a bit odd

@dhruvvjangidd 做得相当不错，不过点击 Discover 按钮后的过渡动画和加载状态感觉有点怪怪的。

### 903

作者: @Guillermo-Rauch
时间: 2025-11-03
链接: https://x.com/rauchg/status/1985366624892051869
互动: Likes: 4; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,783; Bookmarks: 7; isReply: 1

@jcbages Yes, this is on our list. Something like this should be easy to ship:
https://t.co/0cR76GzHzP

@jcbages 是的，这个功能已经在我们的计划中了。类似这样的功能应该很容易上线：
https://t.co/0cR76GzHzP

### 904

作者: @Guillermo-Rauch
时间: 2025-11-03
链接: https://x.com/rauchg/status/1985368781267623951
互动: Likes: 352; Retweets: 14; Replies: 9; Quotes: 7; Views: 72,033; Bookmarks: 86; isReply: 1

@GergelyOrosz After building the @v0 mobile app in React Native &amp; Expo we’re never looking back. Look out for the incoming eng blog post by @FernandoTheRojo

@GergelyOrosz 在用 React Native 和 Expo 开发了 @v0 的移动应用后，我们就彻底「弃暗投明」了。敬请期待 @FernandoTheRojo 即将发布的技术博客！

### 905

作者: @Guillermo-Rauch
时间: 2025-11-03
链接: https://x.com/rauchg/status/1985371200181444773
互动: Likes: 25; Retweets: 0; Replies: 2; Quotes: 0; Views: 2,615; Bookmarks: 0; isReply: 1

@vashishtaditya_ @GergelyOrosz @v0 @FernandoTheRojo 😁 we've arrived

@vashishtaditya_ @GergelyOrosz @v0 @FernandoTheRojo 😁 我们到了！

### 906

作者: @Guillermo-Rauch
时间: 2025-11-03
链接: https://x.com/rauchg/status/1985375890487071206
互动: Likes: 5; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,221; Bookmarks: 0; isReply: 1

@thiago_peres @GergelyOrosz @v0 @FernandoTheRojo Agreed

@thiago_peres @GergelyOrosz @v0 @FernandoTheRojo 同意

### 907

作者: @Guillermo-Rauch
时间: 2025-11-03
链接: https://x.com/rauchg/status/1985375955574300822
互动: Likes: 14; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,822; Bookmarks: 0; isReply: 1

@davidtsolheim @nextjs @vercel @cursor_ai @leerob Amazing combo 🫶

@davidtsolheim @nextjs @vercel @cursor_ai @leerob 强强联合，太棒了！🫶

### 908

作者: @Guillermo-Rauch
时间: 2025-11-03
链接: https://x.com/rauchg/status/1985446031128215968
互动: Likes: 14; Retweets: 0; Replies: 1; Quotes: 0; Views: 3,069; Bookmarks: 0; isReply: 1

@timothyjordan @vercel @tomocchino welcome 🫡

@timothyjordan @vercel @tomocchino 欢迎 🫡

### 909

作者: @Guillermo-Rauch
时间: 2025-11-03
链接: https://x.com/rauchg/status/1985448508284158092
互动: Likes: 972; Retweets: 34; Replies: 68; Quotes: 8; Views: 99,957; Bookmarks: 245; isReply: 0

Vercel is 𝘰𝘧𝘧𝘪𝘤𝘪𝘢𝘭𝘭𝘺 10 years old, according to the State of Delaware, the first US 🇺🇸 state 🫡 Some reflections from the journey:

1️⃣ You can just incorporate things
"In America, they let you start companies easily". It's magical how fast you can get your ', 𝙸𝚗𝚌', your bank account, your LOIs, your payroll set up… 

Docusigns fly, investors are eager to take risk, there's an overwhelming sense of optimism around technology. Business owners are the heroes of this society. We must preserve this company-building culture at all costs. Thankful to San Francisco for being the epitome of it.

2️⃣ 10 years is the baseline 
It's wild to me that it feels like Vercel is just getting started. I remember prior to starting the company looking at the statistics on the median time from inception to IPO for tech companies. It was 8-10 years then and now looking like 10-14.

There are many tough moments while building a company. But what's a bad day or quarter going to do if you know this is a 15 year journey?

3️⃣ It's always day zero
When I registered the domain name and shipped the first company landing page, there was no Next.js. No Git integration. No CDN. No Turborepo. No AI SDK. No v0. At one point, Jamstack and static sites were all the rage. Now, agents and AI.

The only way to survive in this game is to have tremendous adaptability and appetite for shipping. Our first name was "Zeit", because the only way to win is to capture the Zeitgeist. As @cramforce likes to say, iteration velocity and shipping is the solution to all known s̶o̶f̶t̶w̶a̶r̶e̶ ̶e̶n̶g̶i̶n̶e̶e̶r̶i̶n̶g̶ problems in the world.

按照美国特拉华州（美国第一个州🇺🇸🫡）的官方记录，Vercel 正式迎来十周岁生日。关于这段旅程，我有一些感想：

1️⃣ 开公司，可以很简单
「在美国，创业开公司很容易。」这确实很神奇：你很快就能搞定「股份有限公司（Inc.）」的注册、银行账户、投资意向书（LOI）、薪资设置……

电子签名（Docusign）满天飞，投资者乐于承担风险，整个科技圈弥漫着一种压倒性的乐观情绪。企业主被视为这个社会的英雄。我们必须不惜一切代价，保护好这种鼓励创业的文化。感谢旧金山，它是这种文化的完美代表。

2️⃣ 十年，只是起点令我感到不可思议的是，Vercel 仿佛才刚刚起步。记得创业前，我查过科技公司从创立到上市（IPO）所需时间的中位数统计。那时是 8-10 年，而现在看来是 10-14 年。

创业途中难免遇到许多艰难时刻。但如果你深知这是一场至少 15 年的马拉松，那么糟糕的一天甚至一个季度，又算得了什么呢？

3️⃣ 永远保持「第零天」心态当初我注册域名、发布公司第一个着陆页时，还没有 Next.js，没有 Git 集成，没有 CDN，没有 Turborepo，没有 AI SDK，也没有 v0。曾经，Jamstack 和静态网站风靡一时；如今，潮流变成了 AI 智能体（AI Agent）和人工智能（AI）。

要想在这场游戏中生存下来，唯一的办法就是拥有极强的适应能力和持续交付（Shipping）的渴望。我们最初取名「Zeit」，因为取胜之道就在于捕捉时代精神（Zeitgeist）。正如 @cramforce 常说的：迭代速度和持续交付，是世界上所有已知的～软件工程～问题的解决方案。

### 910

作者: @Guillermo-Rauch
时间: 2025-11-03
链接: https://x.com/rauchg/status/1985449267071500604
互动: Likes: 2; Retweets: 0; Replies: 1; Quotes: 0; Views: 110; Bookmarks: 0; isReply: 1

@puf @timothyjordan @vercel @tomocchino There's an approved list of accent colors here 😆
https://t.co/mYQ17awH7V

@puf @timothyjordan @vercel @tomocchino 看，这里有一份官方认可的强调色列表 😆
https://t.co/mYQ17awH7V

### 911

作者: @Guillermo-Rauch
时间: 2025-11-03
链接: https://x.com/rauchg/status/1985453325605880212
互动: Likes: 2; Retweets: 0; Replies: 1; Quotes: 0; Views: 286; Bookmarks: 1; isReply: 1

@yann_birba It's prefetching the ISR shells, which shield you from accessing the database and reduce backend load (dogpiling). It's an extremely efficient website chief.

@yann_birba 它是在预取 ISR（增量静态再生）页面，这能避免直接访问数据库，从而减轻后端负载（防止请求堆积）。这是个非常高效的网站优化策略。

### 912

作者: @Guillermo-Rauch
时间: 2025-11-03
链接: https://x.com/rauchg/status/1985459913070690675
互动: Likes: 5; Retweets: 0; Replies: 0; Quotes: 0; Views: 2,502; Bookmarks: 0; isReply: 1

@thallescomumh Cooking

@thallescomumh 下厨中

### 913

作者: @Guillermo-Rauch
时间: 2025-11-03
链接: https://x.com/rauchg/status/1985494756571693418
互动: Likes: 114; Retweets: 2; Replies: 8; Quotes: 0; Views: 17,481; Bookmarks: 12; isReply: 0

So excited about my ❄️ Snowflake Luminary session at BUILD. 

Unlike other talks I’ve given this one will be a bit more… philosophical. What are the key human skills in the AI future? What happens once the cloud and coding are fully autonomous?

https://t.co/3AebioGKKp https://t.co/dhlsbKipek

真让人兴奋，我将在 BUILD 大会上主持 ❄️ Snowflake Luminary 环节！

与我以往的其他演讲不同，这次的内容会更具... 哲学思辨色彩。在人工智能（AI）的未来，人类的关键技能是什么？当云计算和编程完全实现自主化后，世界又会变成怎样？

https://t.co/3AebioGKKp https://t.co/dhlsbKipek

### 914

作者: @Guillermo-Rauch
时间: 2025-11-04
链接: https://x.com/rauchg/status/1985688357310251342
互动: Likes: 0; Retweets: 0; Replies: 0; Quotes: 0; Views: 61; Bookmarks: 0; isReply: 1

@irfanrosandi @vercel True

@irfanrosandi @vercel 是的 / 对的
（根据常见社交媒体用语，将「True」意译为表示肯定赞同的「是的」或「对的」，更符合中文表达习惯。）

### 915

作者: @Guillermo-Rauch
时间: 2025-11-04
链接: https://x.com/rauchg/status/1985719230260789725
互动: Likes: 525; Retweets: 34; Replies: 69; Quotes: 5; Views: 55,649; Bookmarks: 66; isReply: 0

America is losing the real battle: truly open⎵AI. Everyone knows that in the fullness of time, open wins.

Open is crucial to a thriving and competitive ecosystem. You see this with the proliferation of Chinese model finetunes among US startups. They’ve done a great job.

This has been true for kernels and operating systems (Linux), compilers (GCC and Clang), browsers (Chromium and Blink), runtimes (v8 and Node.js), frameworks (React and Next.js), and it has to be true for AI. 

AI is too important to remain closed, because the future of civilization will be built on it.

美国正在输掉一场真正的战役：真正开源的人工智能（AI）。众所周知，假以时日，开放终将胜出。

开放对于一个繁荣且充满竞争力的生态系统至关重要。这一点从美国初创公司广泛采用并微调中国模型的现象中便可见一斑。他们在这方面做得非常出色。

这一规律早已在内核与操作系统（Linux）、编译器（GCC 和 Clang）、浏览器（Chromium 和 Blink）、运行时（v8 和 Node.js）、框架（React 和 Next.js）等领域得到验证，对于 AI 领域也必定如此。

人工智能（AI）至关重要，绝不能固步自封，因为人类文明的未来将构建于其上。

### 916

作者: @Guillermo-Rauch
时间: 2025-11-04
链接: https://x.com/rauchg/status/1985719780398285178
互动: Likes: 46; Retweets: 2; Replies: 2; Quotes: 0; Views: 4,656; Bookmarks: 1; isReply: 1

@thdxr I think it’ll play out like proprietary Unix → Linux. Early closed-source-mover advantage cannot outcompete the momentum of an open ecosystem.

@thdxr 我觉得这事的走向会像当年的商业 Unix 转向 Linux 一样。早期的闭源先行者优势，终究敌不过一个开放生态系统的强大势头。

### 917

作者: @Guillermo-Rauch
时间: 2025-11-04
链接: https://x.com/rauchg/status/1985733302465269817
互动: Likes: 536; Retweets: 29; Replies: 46; Quotes: 3; Views: 48,230; Bookmarks: 268; isReply: 0

v0 is so good for creating data &amp; BI dashboards that… actually look nice 🔥
https://t.co/oyZSPJ0NI8 https://t.co/xDR6mWl6QV

v0 在创建数据与 BI 仪表板方面表现卓越，其成果... 颜值确实在线 🔥
https://t.co/oyZSPJ0NI8 https://t.co/xDR6mWl6QV

### 918

作者: @Guillermo-Rauch
时间: 2025-11-04
链接: https://x.com/rauchg/status/1985734646039294057
互动: Likes: 8; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,733; Bookmarks: 0; isReply: 1

@ajaymalikpro They're definitely more open than the status quo. Definitely think it could be even better

@ajaymalikpro 他们确实比现状开放得多。当然，我认为开放程度还可以更进一步。

### 919

作者: @Guillermo-Rauch
时间: 2025-11-04
链接: https://x.com/rauchg/status/1985787761887199735
互动: Likes: 21; Retweets: 0; Replies: 2; Quotes: 1; Views: 6,807; Bookmarks: 0; isReply: 1

@smr1337 @leerob Seems like several of my team mates already replied but lmk if you need any further help. DMs open also for more meta-feedback

@smr1337 @leerob 看起来我这边已经有几位同事回复了，不过如果还需要其他帮助，随时告诉我。我的私信也开放，欢迎就此事（或更宏观的方面）进一步交流。

### 920

作者: @Guillermo-Rauch
时间: 2025-11-04
链接: https://x.com/rauchg/status/1985822294930067925
互动: Likes: 9,529; Retweets: 568; Replies: 263; Quotes: 185; Views: 1,720,383; Bookmarks: 4,751; isReply: 0

This marvel is built in TypeGPU, a TypeScript WebGPU library [1/2]

Among other coolness, it features a "𝚞𝚜𝚎 𝚐𝚙𝚞" directive that compiles JS to WSGL, to run on the GPU:

𝚌𝚘𝚗𝚜𝚝 𝚊𝚍𝚍 = (𝚊, 𝚋) =&gt; {
  "𝚞𝚜𝚎 𝚐𝚙𝚞";
  𝚛𝚎𝚝𝚞𝚛𝚗 𝚊 + 𝚋;
}
https://t.co/0i3TlWoeTd

这一精巧之作构建于 TypeGPU 之上，这是一个 TypeScript 的 WebGPU 库 [1/2]。

除了其他亮点，它还有一个 `"use gpu"` 指令，能够将 JavaScript 代码编译成 WGSL（WebGPU Shading Language），从而在 GPU 上执行：

```javascript
const add =（a，b）=> {
「use gpu";
 return a + b;
}
```
https://t.co/0i3TlWoeTd

### 921

作者: @Guillermo-Rauch
时间: 2025-11-04
链接: https://x.com/rauchg/status/1985822687613370437
互动: Likes: 335; Retweets: 9; Replies: 13; Quotes: 0; Views: 80,583; Bookmarks: 190; isReply: 1

Timely illustration of the power and need for directives. JavaScript is now a meta-language, helping you express code that will run *in other computers*.

"𝚞𝚜𝚎 𝚜𝚎𝚛𝚟𝚎𝚛" and "𝚞𝚜𝚎 𝚌𝚕𝚒𝚎𝚗𝚝", as Dan Abramov eloquently put, unlocked React for Two Computers¹. It’s helpful to think of "𝚞𝚜𝚎 𝚌𝚊𝚌𝚑𝚎" as designating yet another worker or realm, where computation can be memoized.

Similarly, "𝚞𝚜𝚎 𝚠𝚘𝚛𝚔𝚏𝚕𝚘𝚠" and "𝚞𝚜𝚎 𝚜𝚝𝚎𝚙" mark functions that will run with specific semantics (like replayability and resumption).

Are directives the end-all-be-all syntax? Not necessarily. But they rightly address the need to express to a compiler that computation will happen sometime and somewhere else.

¹
https://t.co/k95WFLfs8B

一个关于指令（Directives）威力和必要性的生动例证。如今的 JavaScript 已然成为一种元语言（meta-language），能够帮助你编写最终在 * 其他计算机 * 上执行的代码。

正如 Dan Abramov 精辟地描述的那样，`use server` 和 `use client` 这两条指令，为 React 实现了「双端计算」（React for Two Computers）¹。我们不妨将 `use cache` 理解为指定了另一个「工作域」或「计算领域」，在此领域内执行的计算结果可以被缓存（Memoized）起来。

类似地，`use workflow` 和 `use step` 则用于标记那些将以特定语义（例如，支持重放和断点续传）运行的函数。

那么，指令是解决所有问题的终极语法吗？倒也未必。但它们确实精准地满足了这样一个需求：向编译器明确声明，某段计算将在未来的某个时刻、在另一个地方执行。

¹
https://t.co/k95WFLfs8B

### 922

作者: @Guillermo-Rauch
时间: 2025-11-04
链接: https://x.com/rauchg/status/1985824253254754703
互动: Likes: 91; Retweets: 6; Replies: 0; Quotes: 0; Views: 64,929; Bookmarks: 70; isReply: 1

Source. h/t @reczko_konrad 
https://t.co/cJ34kBE47m

来源：致谢 @reczko_konrad。
链接：https://t.co/cJ34kBE47m

### 923

作者: @Guillermo-Rauch
时间: 2025-11-04
链接: https://x.com/rauchg/status/1985825828211736912
互动: Likes: 46; Retweets: 0; Replies: 2; Quotes: 0; Views: 44,006; Bookmarks: 32; isReply: 1

@brennendav1s Nope, just like Workflow ("𝚞𝚜𝚎 𝚠𝚘𝚛𝚔𝚏𝚕𝚘𝚠") is framework-agnostic. These things compose quite well.
https://t.co/YwKk8YhdEr

@brennendav1s 不会，就像 Workflow（"𝚞𝚜𝚎 𝚠𝚘𝚛𝚔𝚏𝚕𝚘𝚠"）一样，它不依赖特定框架。它们之间可以很好地协同工作。
https://t.co/YwKk8YhdEr

### 924

作者: @Guillermo-Rauch
时间: 2025-11-04
链接: https://x.com/rauchg/status/1985829547749884332
互动: Likes: 168; Retweets: 12; Replies: 12; Quotes: 4; Views: 41,488; Bookmarks: 30; isReply: 0

You can now “𝚞𝚜𝚎 𝚠𝚘𝚛𝚔𝚏𝚕𝚘𝚠” with @sveltejs. 

You can start workflows from Remote Functions and +𝚜𝚎𝚛𝚟𝚎𝚛.𝚝𝚜 API routes. SvelteKit is all you need.

https://t.co/KM6uyVTUjx https://t.co/9lQqEoOVA3

现在，你可以在 @sveltejs 中「使用工作流（use workflow）」了。

你可以从远程函数（Remote Functions）和 `+server.ts` API 路由启动工作流。你只需要 SvelteKit 就够了。

https://t.co/KM6uyVTUjx https://t.co/9lQqEoOVA3

### 925

作者: @Guillermo-Rauch
时间: 2025-11-04
链接: https://x.com/rauchg/status/1985830253965819946
互动: Likes: 5; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,185; Bookmarks: 0; isReply: 1

@colin_digital @sveltejs @adriandlam_ @pranaygp Should work, but we haven't documented / worked on an integration yet. cc @tootallnate our resident Workflow &amp; Remix expert. I suspect the integration will be similar to Svelte's

@colin_digital @sveltejs @adriandlam_ @pranaygp 理论上应该可行，但我们尚未对此集成进行文档记录或具体开发。在此请教我们的 Workflow 和 Remix 专家 @tootallnate。我推测该集成方式会与 Svelte 框架的类似。

### 926

作者: @Guillermo-Rauch
时间: 2025-11-05
链接: https://x.com/rauchg/status/1985870196293464325
互动: Likes: 173; Retweets: 0; Replies: 5; Quotes: 1; Views: 32,711; Bookmarks: 6; isReply: 1

@RudolphHill9 Making WebGPU safe and practical

@RudolphHill9 构建安全实用的 WebGPU

### 927

作者: @Guillermo-Rauch
时间: 2025-11-05
链接: https://x.com/rauchg/status/1985890264704303181
互动: Likes: 52; Retweets: 1; Replies: 7; Quotes: 1; Views: 8,398; Bookmarks: 1; isReply: 1

@pranaygp @WorkflowDevKit @vercel Directive engineers

@pranaygp @WorkflowDevKit @vercel 的 Directive 工程师们

### 928

作者: @Guillermo-Rauch
时间: 2025-11-05
链接: https://x.com/rauchg/status/1986048284453216742
互动: Likes: 352; Retweets: 21; Replies: 38; Quotes: 5; Views: 128,786; Bookmarks: 161; isReply: 0

Before / after “𝚞𝚜𝚎 𝚠𝚘𝚛𝚔𝚏𝚕𝚘𝚠”:

&gt; before:
&gt; - scheduling service
&gt; - queues
&gt; - workers
&gt; - cron jobs

&gt; now:
&gt; - 5 functions in one file

Another customer told us they were able to delete 4000 lines of code.

采用工作流模式前后的变化：

> 之前需要：
> - 调度服务
> - 队列
> - 工作进程
> - 定时任务

> 现在仅需：
> - 一个文件中的 5 个函数另一位客户告诉我们，他们借此成功删减了 4000 行代码。

### 929

作者: @Guillermo-Rauch
时间: 2025-11-05
链接: https://x.com/rauchg/status/1986048679745294425
互动: Likes: 16; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,341; Bookmarks: 2; isReply: 1

@agenticist No, a legal AI platform in production with thousands of customers

@agenticist 不是的，这是一个已投入实际应用的法律 AI（Artificial Intelligence）平台，服务着数千家客户。

### 930

作者: @Guillermo-Rauch
时间: 2025-11-05
链接: https://x.com/rauchg/status/1986134155319713839
互动: Likes: 1,161; Retweets: 23; Replies: 98; Quotes: 11; Views: 149,037; Bookmarks: 52; isReply: 0

The billionth (1,000,000,000) @vercel deployment has been made.

We've contacted the developer behind it to offer a unique prize and commemoration 😁

Vercel 平台的第一百亿次（1,000,000,000）部署已经达成！

我们已经联系了这位幸运的开发者，准备为他送上一份独特的奖品和纪念 😁。

### 931

作者: @Guillermo-Rauch
时间: 2025-11-05
链接: https://x.com/rauchg/status/1986148083605119377
互动: Likes: 169; Retweets: 2; Replies: 11; Quotes: 0; Views: 32,078; Bookmarks: 32; isReply: 0

Vercel's goal is to build the fastest, most dev-friendly, "white-labable", and observable CDN in the world.

⬥ Dynamic and streaming-first
Our CDN doesn't stop at static workloads (i.e.: partial pre-rendering gives you hybrid in one roundtrip). Static is an own-goal bc it forces client JS.

⬥ Previewable and Git-driven
Many outages are caused because of config changes. Vercel lets you 'virtualize' the CDN. Branching is free and instant. 𝚟𝚎𝚛𝚌𝚎𝚕.𝚓𝚜𝚘𝚗 is all you need.

⬥ Blazing-fast purges and TLS issuance
We've obsessed over how fast and reliably we globally propagate changes and purge caches. SSL issuance and sync speed is world-leading, which is 🔑 for platforms.

⬥ No domain limits 
Our CDN serves individual projects with hundreds of thousands of domains. We give you APIs to add, delete, configure them with no limits or per-domain prices.

⬥ Fully observable
We let you observe every aspect of the request lifecycle, as well as drain it to other 3p observability platforms with one click. We just made this better, read on:

Vercel 的目标是构建全球最快、最开发者友好、支持白标（white-label）且具备高度可观测性的内容分发网络（CDN）。

⬥ 动态优先，支持流式传输我们的 CDN 不仅限于处理静态内容（例如：部分预渲染技术可让您在单次往返中实现混合渲染）。局限于静态内容无异于作茧自缚，因为它会强制客户端执行 JavaScript。

⬥ 支持预览，由 Git 驱动许多服务中断都是由配置变更引发的。Vercel 允许您对 CDN 进行「虚拟化」。分支创建免费且即时，您只需一个 `𝚟𝚎𝚛𝚌𝚎𝚕.𝚓𝚜𝚘𝚗` 配置文件即可管理一切。

⬥ 极速缓存清除与 TLS 证书签发我们始终致力于提升全球范围内变更传播与缓存清除的速度和可靠性。我们的 SSL/TLS 证书签发与同步速度位居世界前列，这对平台而言至关重要。

⬥ 无域名数量限制我们的 CDN 支持单个项目关联数十万个域名。我们提供 API 供您添加、删除和配置域名，没有数量限制，也不按域名单独收费。

⬥ 全面的可观测性您能够观测请求生命周期的每一个环节，并可一键将数据导出到其他第三方可观测性平台。我们近期进一步优化了此项功能，详情如下：

### 932

作者: @Guillermo-Rauch
时间: 2025-11-05
链接: https://x.com/rauchg/status/1986153892405739727
互动: Likes: 7; Retweets: 0; Replies: 1; Quotes: 0; Views: 498; Bookmarks: 4; isReply: 1

@MontyDevX If it's a single project setup, the hostname becomes a dynamic slug segment `/[siteId]/`, and then it's just another "param". 

We're going to be publishing a guide soon with architecture recommendations, @RhysSullivan can follow up for early access.

@MontyDevX 在单项目架构中，主机名会成为一个动态的 slug 段，即 `/[siteId]/`，此时它本质上就只是一个路由「参数」了。

我们很快会发布一份包含架构设计建议的指南，@RhysSullivan 可以联系我们获取抢先体验资格。

### 933

作者: @Guillermo-Rauch
时间: 2025-11-05
链接: https://x.com/rauchg/status/1986221252365926697
互动: Likes: 7; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,785; Bookmarks: 0; isReply: 1

@solgrenk i love this

@solgrenk 太赞了！

### 934

作者: @Guillermo-Rauch
时间: 2025-11-05
链接: https://x.com/rauchg/status/1986221308234113142
互动: Likes: 0; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,407; Bookmarks: 0; isReply: 1

@lmdev How so? The syntax?

@lmdev 具体是指哪方面？是语法问题吗？

### 935

作者: @Guillermo-Rauch
时间: 2025-11-06
链接: https://x.com/rauchg/status/1986241296349192317
互动: Likes: 1,070; Retweets: 33; Replies: 133; Quotes: 5; Views: 88,039; Bookmarks: 52; isReply: 0

We're looking for engineers with 10+ years of "𝚞𝚜𝚎 𝚠𝚘𝚛𝚔𝚏𝚕𝚘𝚠" or "𝚞𝚜𝚎 𝚐𝚙𝚞" experience. DMs open.

诚聘拥有 10 年以上「工作流应用」或「GPU 开发」经验的工程师。欢迎私信联系。

### 936

作者: @Guillermo-Rauch
时间: 2025-11-06
链接: https://x.com/rauchg/status/1986245800624787649
互动: Likes: 34; Retweets: 0; Replies: 3; Quotes: 0; Views: 4,064; Bookmarks: 0; isReply: 1

@freddier It was 🔥

@freddier 太火了！🔥

### 937

作者: @Guillermo-Rauch
时间: 2025-11-06
链接: https://x.com/rauchg/status/1986248411239301382
互动: Likes: 12; Retweets: 0; Replies: 0; Quotes: 0; Views: 3,831; Bookmarks: 0; isReply: 1

@matiasbaldanza Straight to top of the queue

@matiasbaldanza 必须前排安排！/ 直接置顶！

### 938

作者: @Guillermo-Rauch
时间: 2025-11-06
链接: https://x.com/rauchg/status/1986248820993499269
互动: Likes: 20; Retweets: 0; Replies: 0; Quotes: 0; Views: 4,581; Bookmarks: 0; isReply: 1

@wongmjane Always the goal

@wongmjane 一直是我们的目标 / 方向！

### 939

作者: @Guillermo-Rauch
时间: 2025-11-06
链接: https://x.com/rauchg/status/1986249525389140188
互动: Likes: 3; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,740; Bookmarks: 1; isReply: 1

@romanbuildsaas @marc_louvion What’s cool about this is that if the target site uses https://t.co/Bf43JlbS8b I’m assuming the attribution Just Works™, based on the outgoing link?

@romanbuildsaas @marc_louvion 这件事很酷的地方在于：如果目标网站使用了 https://t.co/Bf43JlbS8b，那么我猜，仅凭这个出站链接，来源追踪（Attribution）功能就能直接生效（Just Works™）了？

### 940

作者: @Guillermo-Rauch
时间: 2025-11-06
链接: https://x.com/rauchg/status/1986282932504567889
互动: Likes: 0; Retweets: 0; Replies: 0; Quotes: 0; Views: 146; Bookmarks: 0; isReply: 1

@Shanshrew @en_JS Thank you so much for the clarification. Respect 🫡

@Shanshrew @en_JS 非常感谢你的澄清。Respect！🫡

### 941

作者: @Guillermo-Rauch
时间: 2025-11-06
链接: https://x.com/rauchg/status/1986284251940331885
互动: Likes: 7; Retweets: 0; Replies: 0; Quotes: 0; Views: 2,372; Bookmarks: 0; isReply: 1

@BenjDicken Not only that but the prefetching and loading experience is so delightful

不仅如此，预加载和读取的体验也相当流畅顺滑。

### 942

作者: @Guillermo-Rauch
时间: 2025-11-06
链接: https://x.com/rauchg/status/1986289893157576946
互动: Likes: 199; Retweets: 7; Replies: 18; Quotes: 1; Views: 19,591; Bookmarks: 24; isReply: 0

We’ve shipped support for Fastify on @vercel.

Adds to Express.js, Hono, NestJS, Nitro, xmcp, FastAPI, Flask, and Bun as choices for backend APIs on Vercel.
https://t.co/JQ2erVwuBW

我们已在 @vercel 平台推出了对 Fastify 的支持。

至此，Vercel 后端 API 的选项已包含 Express.js、Hono、NestJS、Nitro、xmcp、FastAPI、Flask、Bun 以及 Fastify。
https://t.co/JQ2erVwuBW

### 943

作者: @Guillermo-Rauch
时间: 2025-11-06
链接: https://x.com/rauchg/status/1986486643755524144
互动: Likes: 43; Retweets: 4; Replies: 5; Quotes: 2; Views: 12,243; Bookmarks: 9; isReply: 1

@ibuildthecloud @OpenRouterAI @vercel This is exactly why https://t.co/GrdQeV8mHj exists. Normalized protocol and spec across all providers. BYO provider, BYO gateway. @samuel_colvin just shipped support for our Data Stream protocol:

https://t.co/51DJrzjLRM

@ibuildthecloud @OpenRouterAI @vercel 这正是我们创建 https://t.co/GrdQeV8mHj 的原因。它旨在为所有服务提供商提供一个统一的协议和规范。你可以使用自己的提供商（BYO provider），接入自己的网关（BYO gateway）。@samuel_colvin 刚刚为我们的数据流协议添加了支持：

https://t.co/51DJrzjLRM

### 944

作者: @Guillermo-Rauch
时间: 2025-11-06
链接: https://x.com/rauchg/status/1986561942585262467
互动: Likes: 14; Retweets: 0; Replies: 3; Quotes: 0; Views: 2,673; Bookmarks: 0; isReply: 1

@davidtsolheim @vercel @cursor_ai Let me know of any feedback or sharp edges, would love to continue making @vercel/@nextjs/ etc amazing with Cursor! 🫶

@davidtsolheim @vercel @cursor_ai 欢迎大家提供任何反馈或指出问题，我非常期待能继续通过 Cursor，让 @vercel/@nextjs/ 等项目变得更加出色！🫶

### 945

作者: @Guillermo-Rauch
时间: 2025-11-06
链接: https://x.com/rauchg/status/1986566265214013550
互动: Likes: 15; Retweets: 0; Replies: 1; Quotes: 0; Views: 7,348; Bookmarks: 0; isReply: 1

@birk Well played

@birk 干得漂亮

### 946

作者: @Guillermo-Rauch
时间: 2025-11-06
链接: https://x.com/rauchg/status/1986566562686615675
互动: Likes: 12; Retweets: 0; Replies: 2; Quotes: 0; Views: 6,720; Bookmarks: 0; isReply: 1

@birk also plz check iMessage

@birk 也请查一下 iMessage

### 947

作者: @Guillermo-Rauch
时间: 2025-11-07
链接: https://x.com/rauchg/status/1986612885498569186
互动: Likes: 203; Retweets: 8; Replies: 17; Quotes: 1; Views: 46,722; Bookmarks: 53; isReply: 0

Vercel’s AI products like @v0, Agent, and AI Gateway are built on Vercel.

🥵 Before: global accelerators (AGA), load balancers (NLB), TLS ingress (Nginx), Kubernetes (EKS / Karpenter), EC2, Terraform… 

🌊 After: Fluid and 𝚐𝚒𝚝 𝚙𝚞𝚜𝚑

How to build your own Gateway, globally distributed, processing trillions of tokens:

Vercel 的 AI 产品，如 @v0、AI 智能体（Agent）和 AI 网关（AI Gateway），都基于 Vercel 构建。

🥵 过去需要：全局加速器（AGA）、负载均衡器（NLB）、TLS 入口（Nginx）、Kubernetes（EKS / Karpenter）、EC2、Terraform…

🌊 现在只需：Fluid 和 𝚐𝚒𝚝 𝚙𝚞𝚜𝚑

如何构建您自己的、能处理数万亿 Token 的全球分布式网关：

### 948

作者: @Guillermo-Rauch
时间: 2025-11-07
链接: https://x.com/rauchg/status/1986617728783011969
互动: Likes: 12; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,327; Bookmarks: 0; isReply: 1

@seyong @benchmark You had me at the doge

@seyong @benchmark 你一提到狗狗币，我就心动了。

### 949

作者: @Guillermo-Rauch
时间: 2025-11-07
链接: https://x.com/rauchg/status/1986814763473793233
互动: Likes: 336; Retweets: 7; Replies: 21; Quotes: 1; Views: 38,456; Bookmarks: 120; isReply: 0

Get your own VPS (Virtual Private Sandbox) in one command: 𝚗𝚙𝚡 𝚜𝚊𝚗𝚍𝚋𝚘𝚡.

The fastest way to spin up a sandbox in the cloud and test your agent’s environment.

只需一条命令，即可获得你自己的虚拟私有沙盒（Virtual Private Sandbox，VPS)：𝚗𝚙𝚡 𝚜𝚊𝚗𝚍𝚋𝚘𝚡。

这是在云端快速启动沙盒、测试你的 AI 智能体运行环境的最快途径。

### 950

作者: @Guillermo-Rauch
时间: 2025-11-07
链接: https://x.com/rauchg/status/1986838694314324002
互动: Likes: 18; Retweets: 0; Replies: 1; Quotes: 0; Views: 4,472; Bookmarks: 1; isReply: 1

@thepanta82 The SDK is @𝚟𝚎𝚛𝚌𝚎𝚕/𝚜𝚊𝚗𝚍𝚋𝚘𝚡 – i really like the convenience of the short CLI name 😁

@thepanta82 这个 SDK 是 @𝚟𝚎𝚛𝚌𝚎𝚕/𝚜𝚊𝚗𝚍𝚋𝚘𝚡 – 我超喜欢它命令行工具名字这么短，用起来真方便 😁

### 951

作者: @Guillermo-Rauch
时间: 2025-11-07
链接: https://x.com/rauchg/status/1986838805152997658
互动: Likes: 3; Retweets: 0; Replies: 2; Quotes: 0; Views: 3,600; Bookmarks: 0; isReply: 1

@yzx396 Our free tier is incredibly generous! Anything you're missing?

@yzx396 我们的免费套餐超级大方！您还有什么需要的功能吗？

### 952

作者: @Guillermo-Rauch
时间: 2025-11-07
链接: https://x.com/rauchg/status/1986858121156043192
互动: Likes: 14; Retweets: 0; Replies: 0; Quotes: 0; Views: 2,042; Bookmarks: 0; isReply: 1

@schniz @opencode You cooked

@schniz @opencode 干得漂亮！

### 953

作者: @Guillermo-Rauch
时间: 2025-11-07
链接: https://x.com/rauchg/status/1986866706187464924
互动: Likes: 231; Retweets: 11; Replies: 8; Quotes: 1; Views: 37,802; Bookmarks: 133; isReply: 0

The price/performance range of image models is wild. This is a really cool @v0 to benchmark them.

The fastest model, served by @prodialabs, takes ~400ms. The slowest, ~11s 😳

https://t.co/QDlwKjGufM https://t.co/AsoB7v1bdo

图像模型的性价比范围差异巨大。用 @v0 这个工具来对它们进行基准测试，真的很酷。

最快的模型由 @prodialabs 提供，生成耗时大约 400 毫秒。而最慢的模型则需要大约 11 秒 😳

https://t.co/QDlwKjGufM https://t.co/AsoB7v1bdo

### 954

作者: @Guillermo-Rauch
时间: 2025-11-07
链接: https://x.com/rauchg/status/1986870965998088222
互动: Likes: 3; Retweets: 0; Replies: 1; Quotes: 0; Views: 536; Bookmarks: 0; isReply: 1

@manuelsoria_ @v0 @prodialabs @fal amazing! Share that @v0

@manuelsoria_ @v0 @prodialabs @fal 太厉害了！快分享这个 @v0

### 955

作者: @Guillermo-Rauch
时间: 2025-11-07
链接: https://x.com/rauchg/status/1986884443861368964
互动: Likes: 144; Retweets: 7; Replies: 16; Quotes: 1; Views: 25,346; Bookmarks: 30; isReply: 0

Press ⎵, type in a phrase, and a blazing fast AI model kicks in to help you search: https://t.co/7pvISXPEtI.

This is super helpful to discover TLDs relevant to your business (there are over 1,000 gTLDs)

只需按下空格键，输入一个短语，一个飞速的 AI 模型便会介入，帮你进行搜索：https://t.co/7pvISXPEtI。

这能帮你轻松找到与业务相关的顶级域名（TLDs)（目前有超过 1,000 个通用顶级域名（gTLDs）可供选择）。

### 956

作者: @Guillermo-Rauch
时间: 2025-11-07
链接: https://x.com/rauchg/status/1986895002841325964
互动: Likes: 17; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,672; Bookmarks: 1; isReply: 1

@victorcardenas @albTian Very clean

@victorcardenas @albTian 非常简洁 / 清晰 / 漂亮

### 957

作者: @Guillermo-Rauch
时间: 2025-11-07
链接: https://x.com/rauchg/status/1986926575414288540
互动: Likes: 55; Retweets: 1; Replies: 1; Quotes: 0; Views: 3,064; Bookmarks: 1; isReply: 1

@jayair OpenCode is extremely nice to demo. Nice job

@jayair OpenCode 用来做演示简直太棒了。做得好！

### 958

作者: @Guillermo-Rauch
时间: 2025-11-08
链接: https://x.com/rauchg/status/1986963921107071468
互动: Likes: 5; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,914; Bookmarks: 0; isReply: 1

@magglevalentine The design details are *chefs kiss*

@magglevalentine 这设计细节，简直是绝了！* 完美 *

### 959

作者: @Guillermo-Rauch
时间: 2025-11-08
链接: https://x.com/rauchg/status/1986970411167531266
互动: Likes: 7; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,243; Bookmarks: 0; isReply: 1

@hiddnest @AsideAI Nice job and very cool product

@hiddnest @AsideAI 做得很棒，产品非常酷炫。

### 960

作者: @Guillermo-Rauch
时间: 2025-11-08
链接: https://x.com/rauchg/status/1987218212287832105
互动: Likes: 893; Retweets: 81; Replies: 66; Quotes: 17; Views: 45,488; Bookmarks: 114; isReply: 0

There’s a contagion effect to good habits. When you watch your friends or relatives exercise, you want to exercise.

Same is true for shipping, giving back, eating well… Surround yourself with people who raise your bar.

好习惯具有传染性。当你看到朋友或家人坚持锻炼，你也会想动起来。

对于高效产出、乐于助人、健康饮食…… 这些习惯也是如此。多和那些能激励你变得更好的人在一起。

### 961

作者: @Guillermo-Rauch
时间: 2025-11-08
链接: https://x.com/rauchg/status/1987281424345616726
互动: Likes: 6; Retweets: 0; Replies: 0; Quotes: 0; Views: 705; Bookmarks: 0; isReply: 1

@tylerclark @vercel @ClarkyAI @v0 Will follow up there!

@tylerclark @vercel @ClarkyAI @v0 我会在那边继续跟进！

### 962

作者: @Guillermo-Rauch
时间: 2025-11-09
链接: https://x.com/rauchg/status/1987332183250640986
互动: Likes: 13; Retweets: 0; Replies: 2; Quotes: 0; Views: 2,542; Bookmarks: 0; isReply: 1

@EstebanSuarez It’s really good

@EstebanSuarez 确实很棒！

### 963

作者: @Guillermo-Rauch
时间: 2025-11-09
链接: https://x.com/rauchg/status/1987647776981918006
互动: Likes: 37; Retweets: 0; Replies: 1; Quotes: 0; Views: 4,231; Bookmarks: 1; isReply: 1

@joelbqz @threejs @pmndrs @v0 This would go very hard on a landing page

@joelbqz @threejs @pmndrs @v0 这要是放在着陆页上，效果绝对炸裂。

### 964

作者: @Guillermo-Rauch
时间: 2025-11-09
链接: https://x.com/rauchg/status/1987652395573391730
互动: Likes: 628; Retweets: 45; Replies: 133; Quotes: 22; Views: 144,380; Bookmarks: 265; isReply: 0

English is the insurmountable advantage of the American empire. It’s the most beautiful, sophisticated, flexible language in the world.

Like a good software system, it features progressive disclosure of complexity. It’s extremely easy to get started with, yet it takes decades to master.

There’s a word, “phrasal verb”, or idiom for anything you want to express. It’s extensible and fluid: new words are invented all the time and easily assimilated. New science, new products, new movies, new memes… odds are they first arrive in English.

Countries and individuals can simply get ahead with the one weird trick of pervasive English fluency. I love visiting places like 🇸🇪 or 🇳🇱 where everyone speaks English or makes the effort to.

英语是美国无可匹敌的优势。它是世界上最优美、最精妙、最灵活的语言。

就像一个优秀的软件系统，它具备「渐进呈现复杂性」的特点。它极其易于入门，却需要数十年才能精通。

无论你想表达什么，几乎都有一个对应的「短语动词」（phrasal verb）或习语。它极具扩展性和流动性：新词汇不断被创造并轻松融入。新的科学发现、新的产品、新的电影、新的网络迷因…… 它们往往首先诞生于英语世界。

对于国家和个人而言，只需掌握一个简单而强大的秘诀 —— 普及英语流利度 —— 便能脱颖而出。我喜爱访问像瑞典（🇸🇪）或荷兰（🇳🇱）这样的地方，那里人人都能说英语，或努力尝试去说。

### 965

作者: @Guillermo-Rauch
时间: 2025-11-10
链接: https://x.com/rauchg/status/1987716355156857087
互动: Likes: 8; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,537; Bookmarks: 0; isReply: 1

@samuel_colvin @pydantic Welcome!

@samuel_colvin @pydantic 欢迎！

### 966

作者: @Guillermo-Rauch
时间: 2025-11-10
链接: https://x.com/rauchg/status/1987871631264686096
互动: Likes: 1; Retweets: 0; Replies: 0; Quotes: 0; Views: 100; Bookmarks: 0; isReply: 1

@theo_devs @vercel Taking a look

@theo_devs @vercel 我来看看。

### 967

作者: @Guillermo-Rauch
时间: 2025-11-10
链接: https://x.com/rauchg/status/1987918031776030861
互动: Likes: 0; Retweets: 0; Replies: 0; Quotes: 0; Views: 41; Bookmarks: 0; isReply: 1

@carloswm85 Yeah that’s a hard part for sure

@carloswm85 是啊，这确实挺难的。

### 968

作者: @Guillermo-Rauch
时间: 2025-11-10
链接: https://x.com/rauchg/status/1987934826482331907
互动: Likes: 1,236; Retweets: 52; Replies: 45; Quotes: 19; Views: 277,777; Bookmarks: 145; isReply: 0

Vercel loves TanStack. 

We provided initial funding for its development. Huge respect for @tannerlinsley’s work, who is behind so many great React projects.

Excited to support TanStack on Vercel, via Nitro. Beautiful example of the open web ecosystem coming together. https://t.co/YvPiGiDDRp

Vercel 非常推崇 TanStack。

我们为其发展提供了初始资金。我们非常敬佩 @tannerlinsley 的工作，他是众多优秀 React 项目背后的核心贡献者。

我们很高兴能通过 Nitro 在 Vercel 平台上支持 TanStack。这堪称开放网络生态协同合作的绝佳典范。https://t.co/YvPiGiDDRp

### 969

作者: @Guillermo-Rauch
时间: 2025-11-10
链接: https://x.com/rauchg/status/1987935675883434376
互动: Likes: 64; Retweets: 2; Replies: 3; Quotes: 0; Views: 9,515; Bookmarks: 2; isReply: 1

@raviojhax @tannerlinsley @_pi0_ @nitrojsdev @tan_stack @sveltejs They’re cooking. One of our large enterprise customers who bet on Svelte is seeing an incredible payback. Looking forward to sharing the story soon

@raviojhax @tannerlinsley @_pi0_ @nitrojsdev @tan_stack @sveltejs 他们正在酝酿大招。我们的一家大型企业客户，当初押注 Svelte，如今获得了超乎想象的回报。期待不久后和大家分享这个案例。

### 970

作者: @Guillermo-Rauch
时间: 2025-11-10
链接: https://x.com/rauchg/status/1988008789895971204
互动: Likes: 211; Retweets: 11; Replies: 15; Quotes: 2; Views: 53,048; Bookmarks: 94; isReply: 0

Nature is healing:

•  Neon 𝚙𝚐 (TCP): 3.00𝚖𝚜 avg 🏆 
•  Neon HTTP: 4.50𝚖𝚜 avg
•  Neon WebSocket: 3.90𝚖𝚜 avg

🌊 Fluid solves the connection pooling issues of serverless. And works *best* with battle-tested clients like 𝚙𝚐.

It’s the ideal backend runtime. No lock-in, no special caching or HTTP drivers, excellent in-cloud latency and security.

生态正在恢复活力：

·Neon 𝚙𝚐（TCP）客户端：平均延迟 3.00𝚖𝚜 🏆
·Neon HTTP：平均延迟 4.50𝚖𝚜
·Neon WebSocket：平均延迟 3.90𝚖𝚜

🌊 Fluid 解决了无服务器（Serverless）架构中的连接池难题。并且与 𝚙𝚐 这类久经考验的客户端配合 * 效果最佳 *。

它是理想的后端运行时。无供应商锁定，无需特殊的缓存或 HTTP 驱动程序，提供卓越的云端延迟和安全性。

### 971

作者: @Guillermo-Rauch
时间: 2025-11-10
链接: https://x.com/rauchg/status/1988015971660165537
互动: Likes: 248; Retweets: 10; Replies: 25; Quotes: 6; Views: 76,047; Bookmarks: 77; isReply: 0

In 2025, you no longer have to write your application for a specific cloud vendor or runtime.

You should be able to grab e.g. your @nodejs/@bunjavascript codebase, Postgres db, and run it anywhere.

Your “lock-in” can actually be easily quantified: 𝚐𝚛𝚎𝚙 for the vendor name, deps, and specific runtime APIs in your codebase. Look at the length of your 𝚝𝚘𝚖𝚕 config. Watch for 𝚟𝚒𝚝𝚎-𝚙𝚕𝚞𝚐𝚒𝚗-𝚟𝚎𝚗𝚍𝚘𝚛 to paper over incompatibilities with the standard runtime.

Our commitment is rooted both in portability and ease of use. We believe configuring your runtime or app *for* Vercel is not a good experience. And it’s altogether a net negative for the world.

到 2025 年，你将不再需要针对某个特定的云服务商或运行时环境来开发应用。

你应该能够直接使用你的 @nodejs/@bunjavascript 代码库和 Postgres 数据库，并在任何地方运行你的应用。

所谓的「供应商锁定」程度，其实可以轻松量化：在代码库里用 `grep` 命令搜索一下供应商名称、依赖项以及特定的运行时 API 调用。检查你的 `toml` 配置文件有多长。留意那些通过 `vite-plugin-vendor` 等插件来掩盖与标准运行时环境不兼容问题的做法。

我们的承诺源于对可移植性和易用性的双重追求。我们认为，仅仅为了适配 Vercel 而去配置你的运行时或应用，体验并不好。而且，这对整个生态而言，总体上是弊大于利的。

### 972

作者: @Guillermo-Rauch
时间: 2025-11-10
链接: https://x.com/rauchg/status/1988027297631543455
互动: Likes: 5; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,146; Bookmarks: 0; isReply: 1

@lemolsoft @nodejs @bunjavascript 😄 just spitballing

@lemolsoft @nodejs @bunjavascript 😄 随便聊聊想法 / 抛砖引玉

### 973

作者: @Guillermo-Rauch
时间: 2025-11-10
链接: https://x.com/rauchg/status/1988031421131485529
互动: Likes: 1; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,336; Bookmarks: 0; isReply: 1

@sekhadrion @nodejs @bunjavascript Because it's the truth 🫶

@sekhadrion @nodejs @bunjavascript 因为事实就是如此呀 🫶

### 974

作者: @Guillermo-Rauch
时间: 2025-11-11
链接: https://x.com/rauchg/status/1988037862152171606
互动: Likes: 503; Retweets: 11; Replies: 33; Quotes: 2; Views: 95,058; Bookmarks: 126; isReply: 0

When Google App Engine came out (2008), its runtime was a strange "subset" of Python. 

You couldn't bind to C libraries, open sockets, run background threads… To fetch data you had to:

𝚏𝚛𝚘𝚖 𝚐𝚘𝚘𝚐𝚕𝚎.𝚊𝚙𝚙𝚎𝚗𝚐𝚒𝚗𝚎.𝚊𝚙𝚒 𝚒𝚖𝚙𝚘𝚛𝚝 𝚞𝚛𝚕𝚏𝚎𝚝𝚌𝚑
𝚛𝚎𝚜𝚞𝚕𝚝 = 𝚞𝚛𝚕𝚏𝚎𝚝𝚌𝚑.𝚏𝚎𝚝𝚌𝚑("𝚑𝚝𝚝𝚙://…")

When AWS EC2 came out (2006), you could do ✨ anything ✨. Over time GCP realized that the restrictions did not make sense, and that people wanted to have full control and versioning over their runtimes. They didn't want "Google's Python", they wanted Python.

AWS in the meantime accrued an insurmountable lead.

We're now, strangely, seeing the same play out with JavaScript runtimes today. I fully expect the "VendorJS" days to be numbered. Save this tweet.

早在 2008 年 Google App Engine 刚推出时，它的运行时环境就是一个颇为古怪的 Python「子集」。

开发者无法绑定 C 语言库、不能打开网络套接字，也不能运行后台线程…… 就连获取数据，都必须使用特定的 API：

```python
from google.appengine.api import urlfetch
result = urlfetch.fetch（"http://…")
```而 2006 年面世的 AWS EC2 就截然不同了，你几乎可以 ✨ 为所欲为 ✨。后来，Google Cloud Platform（GCP）也逐渐意识到这些限制并不合理，开发者真正需要的是对运行时环境的完全控制权和自主的版本选择。他们想要的不是"Google 定制版 Python」，而是原汁原味的 Python。

然而在此期间，AWS 已经建立了难以撼动的领先地位。

有趣的是，如今我们似乎在 JavaScript 运行时领域看到了同样的历史重演。我敢断言，各大云厂商推出的定制化「VendorJS」运行时（注：指受供应商限制的 JavaScript 环境）的好日子不会太长了。这条推文，咱们立此存照。

### 975

作者: @Guillermo-Rauch
时间: 2025-11-11
链接: https://x.com/rauchg/status/1988043054897656174
互动: Likes: 16; Retweets: 0; Replies: 1; Quotes: 0; Views: 8,262; Bookmarks: 1; isReply: 1

@neilsuperduper Interop is not good enough. You need the exact runtime at a given version to get both the DX and portability, with minimal or no restrictions. That’s the bigger lesson of GAE’s pseudo-Python

@neilsuperduper 兼容性还不够理想。你需要一个特定版本的精确运行时环境，才能同时获得良好的开发者体验（Developer Experience，DX）和可移植性，并将限制降至最低甚至完全消除。这正是 Google App Engine（GAE）其非标准 Python 环境所揭示的更深刻教训。

### 976

作者: @Guillermo-Rauch
时间: 2025-11-11
链接: https://x.com/rauchg/status/1988044598393118898
互动: Likes: 2; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,475; Bookmarks: 0; isReply: 1

@alfa_maven @nodejs @bunjavascript Fewer vendors-specific APIs, runtime semantics and proprietary statefulness solutions → less vendor specific “know-how”. 

And faster velocity for the team, likely to benefit more from global corpus of knowledge and LLMs

@alfa_maven @nodejs @bunjavascript 更少的供应商专用 API、运行时语义和专有状态解决方案，意味着更少的供应商锁定型「专有技术」。

这能提升团队的开发速度，并使其更有可能从全球知识库和大语言模型中获益。

### 977

作者: @Guillermo-Rauch
时间: 2025-11-11
链接: https://x.com/rauchg/status/1988046594017841523
互动: Likes: 580; Retweets: 28; Replies: 35; Quotes: 5; Views: 92,390; Bookmarks: 126; isReply: 0

This is so good
@stripe 🤝 @v0

You can just monetize things

太棒了！
@stripe 🤝 @v0

这样一来，产品就能直接变现了。

### 978

作者: @Guillermo-Rauch
时间: 2025-11-11
链接: https://x.com/rauchg/status/1988056381908475920
互动: Likes: 2,531; Retweets: 56; Replies: 194; Quotes: 15; Views: 310,312; Bookmarks: 152; isReply: 0

I’m at the ER in San Francisco due to my wife’s sudden, acute appendicitis.

Throughout the night and day you can hear the screams, dry-heaving, tussling, and cussing of drug-addicts in withdrawal.

On the other hard, she also just received world-class, expedient medical care by lovely, dedicated medical professionals. What a roller coaster.

We, as one American team, need to figure out how to end this opiate crisis. We're better than this. We can't have our neighbors and friends suffering on the streets, with drug dealers roaming around undeterred, and endless misery perpetuated under the veil of empathy.

因为妻子突发急性阑尾炎，我陪她在旧金山的急诊室。

一天一夜，耳边充斥着吸毒者戒断时的尖叫、干呕、撕扯与咒骂。

但另一方面，她也刚刚得到了亲切而敬业的医护人员提供的高效、世界一流的医疗救治。这心情真是像坐过山车一样起伏。

我们作为一个国家，必须想办法终结这场阿片危机。我们不该止步于此。我们不能眼睁睁看着邻里朋友在街头受苦，毒贩肆无忌惮地流窜，而无尽的苦难却在「共情」的幌子下不断蔓延。

### 979

作者: @Guillermo-Rauch
时间: 2025-11-11
链接: https://x.com/rauchg/status/1988056661345656954
互动: Likes: 114; Retweets: 0; Replies: 2; Quotes: 0; Views: 22,525; Bookmarks: 0; isReply: 1

@lewiscarhart Thanks. Surgery was a success and I'll be seeing her soon 🤞

@lewiscarhart 多谢。手术很成功，希望很快就能见到她 🤞

### 980

作者: @Guillermo-Rauch
时间: 2025-11-11
链接: https://x.com/rauchg/status/1988079437813084387
互动: Likes: 4; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,778; Bookmarks: 0; isReply: 1

@jeff_weinstein @vercel @stripe Facts

@jeff_weinstein @vercel @stripe 这是事实。

### 981

作者: @Guillermo-Rauch
时间: 2025-11-11
链接: https://x.com/rauchg/status/1988092506966516086
互动: Likes: 0; Retweets: 0; Replies: 2; Quotes: 0; Views: 134; Bookmarks: 0; isReply: 1

@hyunbinseo97 @iqbalmwasyid Point is: why do that instead of… using Node. Shipping Node. Growing Node.

@hyunbinseo97 @iqbalmwasyid 关键在于：为什么要走那条路，而不是…… 直接使用 Node、持续发布 Node 版本、并壮大 Node 生态呢？

### 982

作者: @Guillermo-Rauch
时间: 2025-11-11
链接: https://x.com/rauchg/status/1988335157838049751
互动: Likes: 14; Retweets: 0; Replies: 2; Quotes: 0; Views: 2,411; Bookmarks: 2; isReply: 1

@Sikandar_Bhide @Ibelick Keep up the great work

@Sikandar_Bhide @Ibelick 继续加油！

### 983

作者: @Guillermo-Rauch
时间: 2025-11-11
链接: https://x.com/rauchg/status/1988374207689093334
互动: Likes: 14; Retweets: 0; Replies: 0; Quotes: 0; Views: 2,786; Bookmarks: 0; isReply: 1

@vercel_dev Cool

@vercel_dev 酷

### 984

作者: @Guillermo-Rauch
时间: 2025-11-12
链接: https://x.com/rauchg/status/1988672124320698781
互动: Likes: 47; Retweets: 1; Replies: 4; Quotes: 0; Views: 3,423; Bookmarks: 4; isReply: 1

@businessbarista @tenex_labs @vercel 🫶 so excited to partner. Positioning yourself as *the* AI Cloud transformation firm is insanely smart. We get so much demand for this kind of expertise…

We'll look back in 10 years and see this as the most obvious business opportunity of the century.

@businessbarista @tenex_labs @vercel 🫶 非常高兴能与各位携手合作。将自身定位为 * 顶尖的 * AI 云转型公司，这一策略实在是高明至极。我们确实看到了市场对此类专业知识的巨大需求……

十年之后回望，我们一定会将此刻视为本世纪最显而易见的巨大商机。

### 985

作者: @Guillermo-Rauch
时间: 2025-11-12
链接: https://x.com/rauchg/status/1988681369015447694
互动: Likes: 702; Retweets: 14; Replies: 122; Quotes: 10; Views: 87,902; Bookmarks: 85; isReply: 0

Browser makers: this is what peak new tab experience looks like. I love AI and imma let you finish, but I don't want to see the weather, the news, AOL slop.

I press ⌘+T because I already know what I'm gonna do next, so your suggestions are actually noise.

ps: believe it or not, to get this in Chrome you have to install an extension 🤨 I believe only Safari makes this extremely easy to set up (front and center of "General" settings)

浏览器厂商们：来看看什么叫「新标签页体验的天花板」。我虽然喜欢 AI，也先让你们把话说完，但我真的不想在新标签页里看到天气、新闻，或者 AOL 那种垃圾内容。

我按 ⌘+T 是因为我早就想好接下来要干嘛了，所以你们的那些建议纯属干扰。

顺便说一句：信不信由你，想在 Chrome 里得到一个这么干净的新标签页，居然还得装个扩展程序 🤨。在我看来，只有 Safari 把这个选项做得极其简单明了（就在「通用」设置里非常显眼的位置）。

### 986

作者: @Guillermo-Rauch
时间: 2025-11-12
链接: https://x.com/rauchg/status/1988684991417741672
互动: Likes: 28; Retweets: 0; Replies: 6; Quotes: 0; Views: 5,841; Bookmarks: 0; isReply: 1

@branmcconnell too much visual noise, at least for pro users

@branmcconnell 视觉干扰太多了，至少对专业用户而言是这样。

### 987

作者: @Guillermo-Rauch
时间: 2025-11-12
链接: https://x.com/rauchg/status/1988695492927394038
互动: Likes: 14; Retweets: 0; Replies: 0; Quotes: 0; Views: 4,556; Bookmarks: 0; isReply: 1

@awesomekling 😂🫶 so excited!

@awesomekling 😂🫶 太激动了！

### 988

作者: @Guillermo-Rauch
时间: 2025-11-12
链接: https://x.com/rauchg/status/1988703409307054495
互动: Likes: 2; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,021; Bookmarks: 0; isReply: 1

@branmcconnell @kilianciuffolo ok at least for some OCD pro users 😂😂

@branmcconnell @kilianciuffolo 行吧，至少对某些有「强迫症」的专业用户来说是这样 😂😂

### 989

作者: @Guillermo-Rauch
时间: 2025-11-12
链接: https://x.com/rauchg/status/1988746862241997200
互动: Likes: 160; Retweets: 5; Replies: 15; Quotes: 0; Views: 31,884; Bookmarks: 60; isReply: 0

AI products are constantly attacked and abused.

@vercel BotID helps you fight abuse without degrading the UX nor hurting your top-of-funnel. 

3 point plan:
① 𝚗𝚙𝚖 𝚒 𝚋𝚘𝚝𝚒𝚍
② Run 𝚒𝚗𝚒𝚝𝙱𝚘𝚝𝙸𝚍() client-side
③ Use 𝚌𝚑𝚎𝚌𝚔𝙱𝚘𝚝𝙸𝚍().𝚒𝚜𝙱𝚘𝚝 server-side

AI 产品时常面临攻击与滥用。

@vercel BotID 助您有效防止滥用，既无需牺牲用户体验（UX），也能保护关键的获客环节。

只需三步：
① 运行 𝚗𝚙𝚖 𝚒 𝚋𝚘𝚝𝚒𝚍
② 在客户端执行 𝚒𝚗𝚒𝚝𝙱𝚘𝚝𝙸𝚍()
③ 在服务端通过 𝚌𝚑𝚎𝚌𝚔𝙱𝚘𝚝𝙸𝚍().𝚒𝚜𝙱𝚘𝚝 进行校验

### 990

作者: @Guillermo-Rauch
时间: 2025-11-12
链接: https://x.com/rauchg/status/1988749582109749642
互动: Likes: 13; Retweets: 0; Replies: 0; Quotes: 0; Views: 3,138; Bookmarks: 0; isReply: 1

@paraga Congrats!

@paraga 恭喜啊！

### 991

作者: @Guillermo-Rauch
时间: 2025-11-13
链接: https://x.com/rauchg/status/1988788145815761032
互动: Likes: 7; Retweets: 0; Replies: 2; Quotes: 0; Views: 1,592; Bookmarks: 0; isReply: 1

@shamilkayal 🔥 so cool!!

@shamilkayal 🔥 太酷了吧！！

### 992

作者: @Guillermo-Rauch
时间: 2025-11-13
链接: https://x.com/rauchg/status/1988814808767234245
互动: Likes: 6; Retweets: 0; Replies: 0; Quotes: 0; Views: 2,426; Bookmarks: 0; isReply: 1

@AdithyaTec Agreed

@AdithyaTec 同意。

### 993

作者: @Guillermo-Rauch
时间: 2025-11-13
链接: https://x.com/rauchg/status/1988987671252029672
互动: Likes: 190; Retweets: 0; Replies: 14; Quotes: 5; Views: 58,808; Bookmarks: 40; isReply: 0

Vercel’s automatic anomaly detection on point. This is a glimpse of the future of the cloud. 

Anomaly caught → AI investigation → pull request / action / analysis. https://t.co/tnhg5dwOsY

Vercel 的自动异常检测精准无误。这让我们得以窥见未来云计算的样貌。

异常被捕获 → AI 介入调查 → 生成合并请求（Pull Request）/ 触发行动 / 提供分析。https://t.co/tnhg5dwOsY

### 994

作者: @Guillermo-Rauch
时间: 2025-11-13
链接: https://x.com/rauchg/status/1989011407015407861
互动: Likes: 54; Retweets: 1; Replies: 4; Quotes: 0; Views: 5,750; Bookmarks: 17; isReply: 1

@CodeWShreyans No. Horizontal observability platforms will always have a place, and Sentry is a leader there. 

But I always found it extremely weird that clouds are almost *designed* to break out of the box and offer no solutions. Just error pages 

Wrote about it here:
https://t.co/HdeNFakmAd

@CodeWShreyans 并非如此。横向（水平）可观测性平台始终有其不可替代的价值，而 Sentry 无疑是这个领域的佼佼者。

但我一直觉得特别离谱的是，云服务的设计似乎天生就带着一种「开箱即崩」的倾向，而且往往不提供现成的解决方案，只给你一个冷冰冰的错误页面。

关于这个问题，我在这篇文章里详细讨论过：
https://t.co/HdeNFakmAd

### 995

作者: @Guillermo-Rauch
时间: 2025-11-13
链接: https://x.com/rauchg/status/1989013311925690647
互动: Likes: 2; Retweets: 0; Replies: 0; Quotes: 0; Views: 216; Bookmarks: 0; isReply: 1

@CodeWShreyans No framework integration needed. Although the fact that we integrate helps a lot with detecting *routes* vs *paths*

e.g.: you want an alert on /𝚋𝚕𝚘𝚐/[𝚙𝚘𝚜𝚝].

It's opt-in by enabling Alerts.

@CodeWShreyans 并不强制要求框架集成。但我们的集成功能，能极大地帮助区分 * 路由 *（routes）和 * 路径 *（paths）。

举个例子：你可能想针对 `/𝚋𝚕𝚘𝚐/[𝚙𝚘𝚜𝚝]` 这个路径设置警报。

这是一个可选功能，你需要手动开启警报（Alerts）才能使用。

### 996

作者: @Guillermo-Rauch
时间: 2025-11-14
链接: https://x.com/rauchg/status/1989154869916364890
互动: Likes: 1,854; Retweets: 18; Replies: 107; Quotes: 6; Views: 824,610; Bookmarks: 72; isReply: 0

Some company news. 

We’re relocating our headquarters from San Francisco to…

San Francisco. The best place to build.

We’ll be shipping from our new, much bigger, office on Monday 😁 https://t.co/vmgh6NKJtP

公司新闻速递。

我们宣布将总部迁出旧金山，新址是……

依然是旧金山。这里始终是筑梦与创造的最佳之地。

本周一，我们将从崭新且更为宽敞的办公室正式启航 😁 https://t.co/vmgh6NKJtP

### 997

作者: @Guillermo-Rauch
时间: 2025-11-14
链接: https://x.com/rauchg/status/1989310619926032474
互动: Likes: 104; Retweets: 0; Replies: 5; Quotes: 0; Views: 25,748; Bookmarks: 0; isReply: 1

@ajrgd They could have called it turbo pack

他们完全可以叫它「超级加速包」的。

### 998

作者: @Guillermo-Rauch
时间: 2025-11-14
链接: https://x.com/rauchg/status/1989334429010162030
互动: Likes: 17; Retweets: 0; Replies: 1; Quotes: 0; Views: 4,119; Bookmarks: 0; isReply: 1

@pelaseyed @v0 DMing

@pelaseyed @v0 私聊。

### 999

作者: @Guillermo-Rauch
时间: 2025-11-14
链接: https://x.com/rauchg/status/1989425561995972618
互动: Likes: 414; Retweets: 20; Replies: 27; Quotes: 4; Views: 104,881; Bookmarks: 248; isReply: 0

Timeline of agents at Vercel:

① Support agent 
Processing 70%+ tickets autonomously

② v0
Now at 6.4 app generations per second

③ Code Review
52% of the time it spots PR defects humans & other tools missed 

④ Lead agent 
Triages all inbound contact sales form submissions

⑤ Data analyst agent 
You can @​d0 on our Slack and  query our warehouse in natural language 

We’ve learned a lot building these & others, and continue to open source our learnings and agent architectures:

Vercel 的 AI 智能体发展历程：

① 客服智能体自动处理超过 70% 的用户支持工单。

② v0 生成智能体目前每秒可生成 6.4 个应用。

③ 代码审查智能体在 52% 的案例中，它能发现人类评审员及其他工具所遗漏的拉取请求（PR）缺陷。

④ 销售线索智能体初步筛选所有收到的销售咨询表单提交。

⑤ 数据分析智能体您可以在我们的 Slack 中 @​d0，直接用自然语言查询数据仓库。

在构建这些以及其他智能体的过程中，我们积累了丰富的经验，并将持续开源我们的实践心得与智能体架构：

### 1000

作者: @Guillermo-Rauch
时间: 2025-11-14
链接: https://x.com/rauchg/status/1989465835967320573
互动: Likes: 84; Retweets: 1; Replies: 5; Quotes: 0; Views: 27,198; Bookmarks: 13; isReply: 0

Every major internet website is a museum of hyperlink relics.

Scaling the CDN infrastructure to support this in a multi-tenant fashion was fun work. Plus great DX!

每个大型互联网网站，都像是一座收藏着无数超链接遗迹的博物馆。

为了支撑这样的景象，以多租户模式来扩展内容分发网络（CDN）基础设施，这项工作充满了乐趣。此外，还有极佳的开发者体验（Developer Experience，DX)！

### 1001

作者: @Guillermo-Rauch
时间: 2025-11-15
链接: https://x.com/rauchg/status/1989488113564238234
互动: Likes: 5; Retweets: 0; Replies: 0; Quotes: 0; Views: 849; Bookmarks: 0; isReply: 1

@ConnerBean We analyze the resulting merged code and we deduce whether our observation or diff got reflected in it.

This is more comprehensive than just capturing the 👍 or “apply fix” button

我们会对合并后的代码进行分析，从而判断我们的观察结果或代码差异是否已被采纳。

这种方法比单纯记录「点赞」（👍）或点击「应用修复」按钮能提供更全面的信息。

### 1002

作者: @Guillermo-Rauch
时间: 2025-11-15
链接: https://x.com/rauchg/status/1989489878896369799
互动: Likes: 16; Retweets: 0; Replies: 1; Quotes: 0; Views: 3,764; Bookmarks: 0; isReply: 1

@ProfKuangXu @vercel Thanks for having me! Amazing group

@ProfKuangXu @vercel 感谢邀请！很棒的团队。

### 1003

作者: @Guillermo-Rauch
时间: 2025-11-15
链接: https://x.com/rauchg/status/1989494179169538498
互动: Likes: 36; Retweets: 0; Replies: 5; Quotes: 0; Views: 5,458; Bookmarks: 4; isReply: 1

@LM_Braswell Blue Barn

@LM_Braswell Blue Barn

### 1004

作者: @Guillermo-Rauch
时间: 2025-11-15
链接: https://x.com/rauchg/status/1989540802390098277
互动: Likes: 4; Retweets: 0; Replies: 1; Quotes: 0; Views: 832; Bookmarks: 0; isReply: 1

We tried off the shelf solutions. We needed to build our own knowledge core to power a lot of products. 

It’s not a good experience to get divergent AIs if you’re eg: talking to support or checking out our docs.

This will vary by company but the cost to build your own agents is going to continue to come down, not least of which due to efforts like https://t.co/a4QDSsa4mL

我们尝试过一些现成的解决方案，但最终还是需要构建我们自己的知识库，来为众多产品提供支持。

想象一下，如果你在联系客服或查阅产品文档时，得到的 AI 回答前后矛盾、说法不一，这种体验肯定不好。

对于不同公司，情况可能不同，但构建你自己的 AI 智能体（AI Agent）的成本将会持续下降。这背后有很多推动力，例如开源项目（如 https://t.co/a4QDSsa4mL）的努力就功不可没。

### 1005

作者: @Guillermo-Rauch
时间: 2025-11-15
链接: https://x.com/rauchg/status/1989787128201691446
互动: Likes: 129; Retweets: 3; Replies: 78; Quotes: 10; Views: 41,579; Bookmarks: 22; isReply: 0

What’s your preferred agentic engineering interface?

你更倾向于使用哪种智能体工程（Agentic Engineering）接口？

### 1006

作者: @Guillermo-Rauch
时间: 2025-11-15
链接: https://x.com/rauchg/status/1989787563415277589
互动: Likes: 7; Retweets: 0; Replies: 3; Quotes: 0; Views: 1,648; Bookmarks: 0; isReply: 1

@reillyjodonnell Falls under “IDE” I think but could have been nice to fit web ide vs local ide

@reillyjodonnell 我觉得这应该归到「集成开发环境（IDE）」这类。不过，如果能区分一下在线 IDE（Web IDE）和本地 IDE（Local IDE）可能会更好。

### 1007

作者: @Guillermo-Rauch
时间: 2025-11-15
链接: https://x.com/rauchg/status/1989792739836531194
互动: Likes: 37; Retweets: 0; Replies: 3; Quotes: 0; Views: 6,123; Bookmarks: 3; isReply: 1

@devongovett Interesting. Potential drawback: Easy to miss, especially when the action is decoupled from the button (eg: pressing Enter on a form). Not mobile friendly

@devongovett 这个观点挺有意思。不过也有潜在的不足：这种设计容易被人忽略，尤其是在操作与按钮本身分离的情况下（比如在表单里直接按回车键提交）。而且，它对移动设备也不太友好。

### 1008

作者: @Guillermo-Rauch
时间: 2025-11-16
链接: https://x.com/rauchg/status/1989874346865869149
互动: Likes: 5; Retweets: 0; Replies: 1; Quotes: 0; Views: 899; Bookmarks: 0; isReply: 1

@_abilshr Coming

@_abilshr 在呢

### 1009

作者: @Guillermo-Rauch
时间: 2025-11-16
链接: https://x.com/rauchg/status/1990119926313754973
互动: Likes: 15; Retweets: 0; Replies: 0; Quotes: 0; Views: 3,573; Bookmarks: 0; isReply: 1

@lukeshiels_ Love it

@lukeshiels_ 太棒了！

### 1010

作者: @Guillermo-Rauch
时间: 2025-11-17
链接: https://x.com/rauchg/status/1990436938034344259
互动: Likes: 1,680; Retweets: 51; Replies: 106; Quotes: 16; Views: 218,555; Bookmarks: 950; isReply: 0

Green flags in a React codebase 

✅ Next.js
✅ Tailwind
✅ @shadcn 
✅ 𝚋𝚞𝚗.𝚕𝚘𝚌𝚔𝚋 / 𝚙𝚗𝚙𝚖-𝚕𝚘𝚌𝚔.𝚢𝚊𝚖𝚕
✅ @turborepo 
✅ @drizzleorm

React 项目中的积极信号（推荐技术栈）

✅ Next.js
✅ Tailwind CSS
✅ @shadcn/ui
✅ 使用 Bun 或 pnpm 作为包管理器（𝚋𝚞𝚗.𝚕𝚘𝚌𝚔𝚋 / 𝚙𝚗𝚙𝚖-𝚕𝚘𝚌𝚔.𝚢𝚊𝚖𝚕)
✅ Turborepo
✅ Drizzle ORM

### 1011

作者: @Guillermo-Rauch
时间: 2025-11-17
链接: https://x.com/rauchg/status/1990437200698241082
互动: Likes: 5; Retweets: 0; Replies: 2; Quotes: 0; Views: 5,433; Bookmarks: 0; isReply: 1

@abhijitwt @shadcn @turborepo @DrizzleORM For large enough codebases

当代码库规模变得足够庞大时

### 1012

作者: @Guillermo-Rauch
时间: 2025-11-17
链接: https://x.com/rauchg/status/1990437320932417654
互动: Likes: 10; Retweets: 0; Replies: 0; Quotes: 0; Views: 3,160; Bookmarks: 0; isReply: 1

@anotherlazydev @shadcn @turborepo @DrizzleORM Prisma is great too

@anotherlazydev @shadcn @turborepo @DrizzleORM Prisma 同样是个不错的选择。

### 1013

作者: @Guillermo-Rauch
时间: 2025-11-17
链接: https://x.com/rauchg/status/1990439061983723591
互动: Likes: 20; Retweets: 0; Replies: 0; Quotes: 0; Views: 5,734; Bookmarks: 0; isReply: 1

@chribjel @shadcn @turborepo @DrizzleORM True forgot they migrated from the binary format

@chribjel @shadcn @turborepo @DrizzleORM 确实，忘了他们已经从二进制格式迁移过来了。

### 1014

作者: @Guillermo-Rauch
时间: 2025-11-17
链接: https://x.com/rauchg/status/1990443471388500184
互动: Likes: 23; Retweets: 2; Replies: 2; Quotes: 0; Views: 3,456; Bookmarks: 0; isReply: 1

@michael_chomsky We will fight back

@michael_chomsky 我们会反击的。

### 1015

作者: @Guillermo-Rauch
时间: 2025-11-17
链接: https://x.com/rauchg/status/1990474715908174077
互动: Likes: 23; Retweets: 0; Replies: 1; Quotes: 0; Views: 3,117; Bookmarks: 0; isReply: 1

@SimonM139034 @shadcn @turborepo @DrizzleORM ok bot

@SimonM139034 @shadcn @turborepo @DrizzleORM 好的，收到。

### 1016

作者: @Guillermo-Rauch
时间: 2025-11-17
链接: https://x.com/rauchg/status/1990477023069024650
互动: Likes: 12; Retweets: 0; Replies: 0; Quotes: 0; Views: 6,291; Bookmarks: 2; isReply: 1

@branmcconnell @shadcn @turborepo @DrizzleORM Green flags: @haydenbleasel

靠谱的技术人选 / 项目推荐：@branmcconnell @shadcn @turborepo @DrizzleORM 以及 @haydenbleasel。

### 1017

作者: @Guillermo-Rauch
时间: 2025-11-17
链接: https://x.com/rauchg/status/1990478071275925723
互动: Likes: 11; Retweets: 0; Replies: 3; Quotes: 0; Views: 3,193; Bookmarks: 1; isReply: 1

@ky__zo @tan_stack @supabase @vercel @nextjs @aisdk I need this

@ky__zo @tan_stack @supabase @vercel @nextjs @aisdk 这个我需要。

### 1018

作者: @Guillermo-Rauch
时间: 2025-11-17
链接: https://x.com/rauchg/status/1990494171388653966
互动: Likes: 12; Retweets: 0; Replies: 0; Quotes: 0; Views: 2,875; Bookmarks: 1; isReply: 1

@joefioti Congrats, very happy to support. Frameworks ftw!

@joefioti 恭喜，非常乐意支持！框架太棒了！

### 1019

作者: @Guillermo-Rauch
时间: 2025-11-17
链接: https://x.com/rauchg/status/1990501570228990100
互动: Likes: 56; Retweets: 0; Replies: 1; Quotes: 0; Views: 5,301; Bookmarks: 1; isReply: 1

@DMarc_2 @shadcn @turborepo @DrizzleORM Both good options. Svelte would be an unusual thing to find in a React codebase 😂

@DMarc_2 @shadcn @turborepo @DrizzleORM 两个都是挺好的选择。不过要在 React 的代码库里看到 Svelte，那可就稀奇了 😂

### 1020

作者: @Guillermo-Rauch
时间: 2025-11-17
链接: https://x.com/rauchg/status/1990506139524686227
互动: Likes: 2,416; Retweets: 49; Replies: 77; Quotes: 19; Views: 349,497; Bookmarks: 315; isReply: 0

Next.js downloads

𝟸𝟶𝟷𝟼 𝟹𝟹,𝟾𝟹𝟷
𝟸𝟶𝟷𝟽 𝟿𝟽𝟻,𝟶𝟺𝟾
𝟸𝟶𝟷𝟾 𝟺,𝟹𝟸𝟿,𝟺𝟶𝟿
𝟸𝟶𝟷𝟿 𝟷𝟷,𝟾𝟷𝟽,𝟷𝟶𝟸
𝟸𝟶𝟸𝟶 𝟹𝟹,𝟹𝟻𝟶,𝟶𝟾𝟻
𝟸𝟶𝟸𝟷 𝟾𝟶,𝟾𝟻𝟾,𝟹𝟺𝟸
𝟸𝟶𝟸𝟸 𝟷𝟺𝟽,𝟷𝟺𝟺,𝟻𝟼𝟸
𝟸𝟶𝟸𝟹 𝟸𝟸𝟾,𝟻𝟹𝟶,𝟿𝟨𝟾
𝟸𝟶𝟸𝟺 𝟹𝟺𝟶,𝟷𝟹𝟾,𝟾𝟾𝟷
𝟸𝟶𝟸𝟻 𝟻𝟸𝟶,𝟿𝟧𝟽,𝟶𝟶𝟻+

Next.js 年下载量

2016 33,831
2017 975,048
2018 4,329,409
2019 11,817,102
2020 33,350,085
2021 80,858,342
2022 147,144,562
2023 228,530,968
2024 340,138,881
2025 520,957,005+

### 1021

作者: @Guillermo-Rauch
时间: 2025-11-17
链接: https://x.com/rauchg/status/1990510890844877244
互动: Likes: 0; Retweets: 0; Replies: 0; Quotes: 0; Views: 96; Bookmarks: 0; isReply: 1

@brandonhays03 so true

@brandonhays03 太真实了

### 1022

作者: @Guillermo-Rauch
时间: 2025-11-17
链接: https://x.com/rauchg/status/1990511055081255120
互动: Likes: 25; Retweets: 0; Replies: 2; Quotes: 0; Views: 10,551; Bookmarks: 0; isReply: 1

@puppeteer_0 Aiming for 1B+

@puppeteer_0 目标超过 10 亿

### 1023

作者: @Guillermo-Rauch
时间: 2025-11-17
链接: https://x.com/rauchg/status/1990515210382397680
互动: Likes: 281; Retweets: 9; Replies: 5; Quotes: 5; Views: 85,830; Bookmarks: 26; isReply: 1

AI SDK

𝟸𝟶𝟸𝟹 𝟷,𝟺𝟶𝟽,𝟶𝟸𝟻
𝟸𝟶𝟸𝟺 𝟷𝟻,𝟿𝟽𝟻,𝟶𝟸𝟿
𝟸𝟶𝟸𝟻 𝟾𝟾,𝟼𝟺𝟶,𝟺𝟹𝟼+

It took Next.js 6 years of exceptionally fast growth to get to (less than) @aisdk's 2025 levels :o

AI SDK

2023 年 1,407,025
2024 年 15,975,029
2025 年 88,640,436+

Next.js 经历了长达 6 年的异常快速增长，其成就（竟然）还不及 @aisdk 在 2025 年的水平 :O

### 1024

作者: @Guillermo-Rauch
时间: 2025-11-18
链接: https://x.com/rauchg/status/1990618037339484438
互动: Likes: 25; Retweets: 1; Replies: 1; Quotes: 0; Views: 2,753; Bookmarks: 0; isReply: 1

@tomjohndesign @vercel Welcome! So excited to ship together

@tomjohndesign @vercel 欢迎！非常期待能一起发布产品！

### 1025

作者: @Guillermo-Rauch
时间: 2025-11-18
链接: https://x.com/rauchg/status/1990659069179560369
互动: Likes: 18; Retweets: 0; Replies: 2; Quotes: 0; Views: 3,745; Bookmarks: 0; isReply: 1

@delba_oliveira aesthetic is on-point

@delba_oliveira 的审美绝了。

### 1026

作者: @Guillermo-Rauch
时间: 2025-11-18
链接: https://x.com/rauchg/status/1990659974616461814
互动: Likes: 542; Retweets: 6; Replies: 31; Quotes: 3; Views: 47,610; Bookmarks: 50; isReply: 0

Workflow patterns: email unsubscribe.

"𝚞𝚜𝚎 𝚠𝚘𝚛𝚔𝚏𝚕𝚘𝚠"
𝚊𝚠𝚊𝚒𝚝 𝚜𝚕𝚎𝚎𝚙("𝟷𝟶 𝚍𝚊𝚢𝚜")
𝚊𝚠𝚊𝚒𝚝 𝚞𝚗𝚜𝚞𝚋𝚜𝚌𝚛𝚒𝚋𝚎() https://t.co/05D6sTGYgt

工作流模式：邮件取消订阅。

"工作流示例："
等待 sleep（'10 天 ')
等待 unsubscribe（）https://t.co/05D6sTGYgt

### 1027

作者: @Guillermo-Rauch
时间: 2025-11-18
链接: https://x.com/rauchg/status/1990674749467603069
互动: Likes: 15; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,536; Bookmarks: 0; isReply: 1

@blocksnmore @BankofAmerica Fair

@blocksnmore @BankofAmerica 有道理。

### 1028

作者: @Guillermo-Rauch
时间: 2025-11-18
链接: https://x.com/rauchg/status/1990792288071823723
互动: Likes: 4,114; Retweets: 192; Replies: 168; Quotes: 65; Views: 288,232; Bookmarks: 134; isReply: 0

That must have been a nasty 𝚞𝚜𝚎𝙴𝚏𝚏𝚎𝚌𝚝

那一定是个相当棘手的副作用（Side Effect）。

### 1029

作者: @Guillermo-Rauch
时间: 2025-11-18
链接: https://x.com/rauchg/status/1990813760550752415
互动: Likes: 67; Retweets: 0; Replies: 3; Quotes: 0; Views: 6,075; Bookmarks: 2; isReply: 1

@v0 woah

@v0 哇哦

### 1030

作者: @Guillermo-Rauch
时间: 2025-11-18
链接: https://x.com/rauchg/status/1990819773530464693
互动: Likes: 342; Retweets: 1; Replies: 12; Quotes: 2; Views: 54,274; Bookmarks: 23; isReply: 0

Elysia mentioned

Elysia 指出

### 1031

作者: @Guillermo-Rauch
时间: 2025-11-18
链接: https://x.com/rauchg/status/1990875106168754665
互动: Likes: 170; Retweets: 4; Replies: 7; Quotes: 1; Views: 46,783; Bookmarks: 29; isReply: 0

Luma processes millions of event signups every month with @nextjs & @vercel. https://t.co/PtvF1J3DTp links are the URL for IRL.

By upgrading to Next 16, build and deploy times went from 𝟷𝟶𝚖 → 𝟸𝚖 (𝟻𝚡 faster). On Pages Router!

The work the @nextjs team puts into backwards-compatibility and supporting large production customers continues to pay off.

Luma 每月通过 @nextjs 和 @vercel 处理数百万的活动报名。https://t.co/PtvF1J3DTp 这个链接指向其线下活动（IRL）的页面。

升级至 Next.js 16 后，构建和部署时间从 10 分钟缩短至 2 分钟，速度提升了 5 倍。而且这是在 Pages Router 上实现的！

@nextjs 团队在确保向后兼容和支持大型生产客户方面付出的努力，正在持续带来丰厚的回报。

### 1032

作者: @Guillermo-Rauch
时间: 2025-11-18
链接: https://x.com/rauchg/status/1990908927911903492
互动: Likes: 112; Retweets: 7; Replies: 5; Quotes: 0; Views: 21,446; Bookmarks: 32; isReply: 0

How does Vercel use @v0? @wsokra used it to build a sophisticated, high-performance bundle analyzer for the Turbopack module graph.

Optimize bundle size for your apps simply by running 𝚗𝚎𝚡𝚝 𝚎𝚡𝚙𝚎𝚛𝚒𝚖𝚎𝚗𝚝𝚊𝚕-𝚊𝚗𝚊𝚕𝚢𝚣𝚎 in 𝚗𝚎𝚡𝚝@𝚌𝚊𝚗𝚊𝚛𝚢.

Vercel 是如何使用 @v0 的？@wsokra 利用它构建了一个功能复杂且高性能的打包分析工具，用于分析 Turbopack 的模块关系图。

要优化您应用程序的打包体积，只需在 𝚗𝚎𝚡𝚝@𝚌𝚊𝚗𝚊𝚛𝚢 版本中运行 𝚗𝚎𝚡𝚝 𝚎𝚡𝚙𝚎𝚛𝚒𝚖𝚎𝚗𝚝𝚊𝚕-𝚊𝚗𝚊𝚕𝚢𝚣𝚎 命令即可。

### 1033

作者: @Guillermo-Rauch
时间: 2025-11-19
链接: https://x.com/rauchg/status/1990971738965094581
互动: Likes: 1; Retweets: 0; Replies: 1; Quotes: 0; Views: 741; Bookmarks: 0; isReply: 1

@thekevinqi No, annuals

@thekevinqi 不，是一年生植物。

### 1034

作者: @Guillermo-Rauch
时间: 2025-11-19
链接: https://x.com/rauchg/status/1991157734163763529
互动: Likes: 24; Retweets: 0; Replies: 0; Quotes: 0; Views: 3,748; Bookmarks: 0; isReply: 1

@MikeyShulman Congrats. Incredible product

@MikeyShulman 恭喜，产品太棒了！

### 1035

作者: @Guillermo-Rauch
时间: 2025-11-19
链接: https://x.com/rauchg/status/1991164190791229503
互动: Likes: 11; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,762; Bookmarks: 0; isReply: 1

@jamannnnnn @kdy1dev amazing

@jamannnnnn @kdy1dev 太棒了！

### 1036

作者: @Guillermo-Rauch
时间: 2025-11-19
链接: https://x.com/rauchg/status/1991165452576534958
互动: Likes: 234; Retweets: 9; Replies: 19; Quotes: 3; Views: 49,032; Bookmarks: 55; isReply: 0

We're rolling out a new support agent at @vercel. Not only does it solve the vast majority of our tickets, but  people love it 💟.

💬"The AI support agent was the first truly useful agent I’ve experienced"

💬"This AI powered support agent Vercel has implemented is incredibly impressive"

We've been noticing people asking the agent how it was built 😄. We'll be sharing how we built it, but importantly, why we built vs bought.

h/t @vishalyathish @matchai

我们正在 @vercel 推出一款新的 AI 支持助手。它不仅帮我们解决了绝大部分的客户支持工单，而且深受大家喜爱 💟。

💬「这是我用过第一个真正派上用场的 AI 支持助手！」
💬「Vercel 上线的这个 AI 驱动支持助手实在太棒了，令人印象深刻。」

我们注意到，好多朋友都在好奇这个助手是怎么做出来的 😄。接下来，我们不仅会分享它的构建方法，更重要的是，会解释我们为什么选择自己打造，而不是直接购买现成的方案。

特别感谢 @vishalyathish @matchai

### 1037

作者: @Guillermo-Rauch
时间: 2025-11-19
链接: https://x.com/rauchg/status/1991166560422248526
互动: Likes: 6; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,742; Bookmarks: 0; isReply: 1

@pawantxt @vercel My sense given context was that they meant as a consumer, on a website. Given accuracy, speed, etc.

结合上下文来看，我认为他们指的是用户（以消费者身份）在网站上的使用场景。这需要综合考虑准确性、速度等多方面因素。

### 1038

作者: @Guillermo-Rauch
时间: 2025-11-19
链接: https://x.com/rauchg/status/1991176189776630013
互动: Likes: 199; Retweets: 0; Replies: 22; Quotes: 1; Views: 19,685; Bookmarks: 26; isReply: 0

Really enjoying the new https://t.co/VFFF7HYl1Y 'Ask AI' https://t.co/bemeh8r7WQ

太喜欢这个新的「Ask AI」功能了！https://t.co/VFFF7HYl1Y https://t.co/bemeh8r7WQ

### 1039

作者: @Guillermo-Rauch
时间: 2025-11-19
链接: https://x.com/rauchg/status/1991176466780798984
互动: Likes: 7; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,251; Bookmarks: 0; isReply: 1

@MostafaM257 DM me link plz

@MostafaM257 链接私我一下。

### 1040

作者: @Guillermo-Rauch
时间: 2025-11-19
链接: https://x.com/rauchg/status/1991179135952273573
互动: Likes: 113; Retweets: 0; Replies: 2; Quotes: 0; Views: 8,191; Bookmarks: 1; isReply: 1

@shadcn It's a mindset

@shadcn 它代表的是一种思维方式。

### 1041

作者: @Guillermo-Rauch
时间: 2025-11-19
链接: https://x.com/rauchg/status/1991250679101297060
互动: Likes: 8; Retweets: 0; Replies: 0; Quotes: 0; Views: 2,408; Bookmarks: 0; isReply: 1

@raul_dronca Cool

@raul_dronca 酷！

### 1042

作者: @Guillermo-Rauch
时间: 2025-11-20
链接: https://x.com/rauchg/status/1991348262478180663
互动: Likes: 12; Retweets: 0; Replies: 0; Quotes: 0; Views: 2,114; Bookmarks: 0; isReply: 1

@askalphaxiv @MenloVentures @haystackvc @Shakti_VC @conviction @upfrontvc @ericschmidt @SebastianThrun @sarahookr Huge. Congrats

太棒了！恭喜！

### 1043

作者: @Guillermo-Rauch
时间: 2025-11-20
链接: https://x.com/rauchg/status/1991513316867592704
互动: Likes: 2,603; Retweets: 130; Replies: 125; Quotes: 28; Views: 305,246; Bookmarks: 674; isReply: 0

The first test you must pass as an entrepreneur is to speak clearly.

When you introduce yourself and your company, be concise, don’t ramble, don’t rush, err on being blunt.

创业者要过的第一关，就是表达清晰。

介绍自己和自己的公司时，务必简洁、切中要害，不要东拉西扯，也不要语速过快，哪怕听起来直接些也没关系。

### 1044

作者: @Guillermo-Rauch
时间: 2025-11-20
链接: https://x.com/rauchg/status/1991517946213273904
互动: Likes: 1,195; Retweets: 39; Replies: 12; Quotes: 3; Views: 78,993; Bookmarks: 351; isReply: 0

Such a great addition to React. Felt like the story wasn’t complete without this

这真是对 React 一个极棒的补充！感觉有了它，整个体验才算是完整了。

### 1045

作者: @Guillermo-Rauch
时间: 2025-11-20
链接: https://x.com/rauchg/status/1991527399461429431
互动: Likes: 287; Retweets: 0; Replies: 1; Quotes: 0; Views: 27,089; Bookmarks: 6; isReply: 1

@sundarpichai Congratulations. Nano Banana is one of your greatest hits

@sundarpichai 恭喜！Nano Banana 堪称是你的代表作之一。

### 1046

作者: @Guillermo-Rauch
时间: 2025-11-20
链接: https://x.com/rauchg/status/1991543118697755032
互动: Likes: 636; Retweets: 30; Replies: 23; Quotes: 6; Views: 172,002; Bookmarks: 624; isReply: 0

Try out https://t.co/nOd7TSS2L2. Some highlights:

◆ Fully built in @v0, it's the easiest and quickest way to test out this incredible model I've found.

◆ Powered by the @vercel AI Gateway. Notably, we implemented 'Sign in with Vercel' which means the end-user pays for tokens.

◆ Persistence by @supabase. Generations stick around after you log in.

I think this template can be the foundation of a lot of really cool AI products. Just clone it and start prompting to make it your own

欢迎尝试 https://t.co/nOd7TSS2L2。以下是一些亮点：

◆ 完全基于 @v0 构建，这是我发现的测试这个强大模型的最简单、最快捷的方式。

◆ 后端由 @vercel AI Gateway 驱动。值得一提的是，我们实现了「使用 Vercel 登录」功能，这意味着使用成本（即 token 费用）将由最终用户自行承担。

◆ 数据持久化存储由 @supabase 提供。登录后，您生成的对话和内容都会得到保存。

我认为，这个模板完全可以作为许多出色 AI 产品的开发基础。你只需要克隆这个项目，然后开始输入你自己的提示词，就能让它为你所用。

### 1047

作者: @Guillermo-Rauch
时间: 2025-11-20
链接: https://x.com/rauchg/status/1991562205599617530
互动: Likes: 52; Retweets: 0; Replies: 2; Quotes: 0; Views: 4,588; Bookmarks: 0; isReply: 1

@marc_louvion You do this really well in social media though. It's not just for speaking in person.

@marc_louvion 不过你在社交媒体上也做得非常出色。这可不光是在线下交流时才用得上。

### 1048

作者: @Guillermo-Rauch
时间: 2025-11-20
链接: https://x.com/rauchg/status/1991613040991850868
互动: Likes: 29; Retweets: 0; Replies: 0; Quotes: 0; Views: 3,488; Bookmarks: 1; isReply: 1

@tomjohndesign You need a zen garden

@tomjohndesign 你需要一个枯山水（禅意花园）。

### 1049

作者: @Guillermo-Rauch
时间: 2025-11-20
链接: https://x.com/rauchg/status/1991633217171198319
互动: Likes: 386; Retweets: 12; Replies: 29; Quotes: 6; Views: 37,477; Bookmarks: 52; isReply: 0

We're working on a book https://t.co/2iGSWC3b1W

我们正在撰写一本书 https://t.co/2iGSWC3b1W

### 1050

作者: @Guillermo-Rauch
时间: 2025-11-21
链接: https://x.com/rauchg/status/1991877122072478155
互动: Likes: 230; Retweets: 5; Replies: 8; Quotes: 2; Views: 22,980; Bookmarks: 23; isReply: 0

One of the coolest things about watching the @v0 team cook is how much they contribute back to @aisdk and the @vercel ai cloud infra.

I’ve never seen devtools and frameworks become successful absent a highly demanding product.

Same reason @reactjs is where it is today. Forged alongside peak-scale Facebook dot com.

围观 @v0 团队施展技艺，最酷的一点莫过于他们向 @aisdk 和 @vercel AI 云基础设施回馈了如此之多。

我从未见过哪款开发工具或框架，能在缺乏一个要求极其严苛的产品锤炼的情况下获得成功。

@reactjs 能有今天的地位，也是出于同样的原因。它正是在 Facebook.com 承受巅峰流量考验的熔炉中锻造而成的。

### 1051

作者: @Guillermo-Rauch
时间: 2025-11-21
链接: https://x.com/rauchg/status/1991878124787949789
互动: Likes: 18; Retweets: 0; Replies: 1; Quotes: 0; Views: 3,017; Bookmarks: 0; isReply: 1

@iamdavidhill Nice

@iamdavidhill 不错

### 1052

作者: @Guillermo-Rauch
时间: 2025-11-21
链接: https://x.com/rauchg/status/1991880121339535868
互动: Likes: 690; Retweets: 19; Replies: 15; Quotes: 4; Views: 157,374; Bookmarks: 410; isReply: 0

Easy to underestimate how big of a differentiator Observability is to infrastructure products.

The difference between non-viable vs a daily driver for developers.

The @planetscale dash is an excellent @vercel dynamic app. Like GitHub rebuilt for 2025.
https://t.co/im0ZEWwZ3A

人们很容易低估可观测性（Observability）对于基础设施产品来说是一个多么巨大的差异化优势。

这决定了开发者眼中的产品，是毫无实用价值，还是能成为每日必备的主力工具。

@planetscale 的数据面板就是一个绝佳的 @vercel 动态应用范例。简直像是为 2025 年重新打造的 GitHub。
https://t.co/im0ZEWwZ3A

### 1053

作者: @Guillermo-Rauch
时间: 2025-11-21
链接: https://x.com/rauchg/status/1991884580341879028
互动: Likes: 221; Retweets: 6; Replies: 21; Quotes: 1; Views: 138,811; Bookmarks: 49; isReply: 0

Self-driving infrastructure is the perfect distillation of the @vercel product vision

自动驾驶基础设施，完美地浓缩了 @vercel 的产品愿景。

### 1054

作者: @Guillermo-Rauch
时间: 2025-11-21
链接: https://x.com/rauchg/status/1991928573779951649
互动: Likes: 4; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,153; Bookmarks: 0; isReply: 1

@roguesherlock @PlanetScale @vercel They're not on 16 / app router yet. That said, i think a lot of people get the 'quick click' and then take forever to render content. They're doing quite well on the latter, at scale, in production.

@roguesherlock @PlanetScale @vercel 他们还没有升级到 Next.js 16 或使用 App Router。不过话说回来，我觉得很多用户会遇到「点击响应很快」，但内容渲染却要等很久的情况。而在后一点上，也就是在大规模生产环境中实现高效的内容渲染，他们其实做得相当不错。

### 1055

作者: @Guillermo-Rauch
时间: 2025-11-21
链接: https://x.com/rauchg/status/1991963471571980701
互动: Likes: 2; Retweets: 0; Replies: 2; Quotes: 0; Views: 1,675; Bookmarks: 0; isReply: 1

@pawantxt @kidsuper @dfeinition &amp; @foda collab

@pawantxt、@kidsuper、@dfeinition 和 @foda 联名合作

### 1056

作者: @Guillermo-Rauch
时间: 2025-11-22
链接: https://x.com/rauchg/status/1992054021927141463
互动: Likes: 6; Retweets: 0; Replies: 0; Quotes: 0; Views: 2,163; Bookmarks: 0; isReply: 1

@LukeW Very cool

@LukeW 太酷了！

### 1057

作者: @Guillermo-Rauch
时间: 2025-11-22
链接: https://x.com/rauchg/status/1992083852010176980
互动: Likes: 4,257; Retweets: 281; Replies: 239; Quotes: 77; Views: 668,435; Bookmarks: 1,059; isReply: 0

The reason “vibe coding” continues to grow and be successful is that the alternative to vibe coding is not “elite engineering”.

It’s: the project wasn’t born, the idea didn’t get communicated, the app didn’t ship.

Elite engineering is very scarce and will continue to be in extremely high demand. (We’re hiring elite engineers!) The gap between what top engineers and agents can do still exists. Not just that.. when those people use AI, they also gain superpowers.

「氛围式编程」（vibe coding）能够持续发展并取得成功，原因在于它的对立面并非「精英式工程」。

现实是：项目根本不会启动，想法无法有效传达，应用永远无法交付。

精英式工程人才极为稀缺，并且需求将持续高涨。（我们正在招募精英工程师！）顶尖工程师与 AI 智能体（AI Agent）能力之间的差距仍然存在。不仅如此，当这些顶尖工程师使用 AI 时，他们更是如虎添翼。

### 1058

作者: @Guillermo-Rauch
时间: 2025-11-22
链接: https://x.com/rauchg/status/1992271677888319503
互动: Likes: 191; Retweets: 0; Replies: 4; Quotes: 0; Views: 25,346; Bookmarks: 6; isReply: 1

@aagarwal1012 @Cloudflare @vercel We’re looking into this. We’ll do a retro on this attack and share findings.

我们正在调查此事。我们将对此次攻击进行复盘分析，并公布我们的发现。

### 1059

作者: @Guillermo-Rauch
时间: 2025-11-22
链接: https://x.com/rauchg/status/1992322094957478289
互动: Likes: 892; Retweets: 26; Replies: 33; Quotes: 1; Views: 67,881; Bookmarks: 727; isReply: 0

I can't believe @pablostanley one-shotted this https://t.co/F60oEvzkU4

真不敢相信 @pablostanley 居然一发入魂 / 一次就搞定了！https://t.co/F60oEvzkU4

### 1060

作者: @Guillermo-Rauch
时间: 2025-11-22
链接: https://x.com/rauchg/status/1992327757465071861
互动: Likes: 9; Retweets: 0; Replies: 1; Quotes: 0; Views: 3,018; Bookmarks: 1; isReply: 1

@Amankaushik481 @pablostanley One shotted in @pablostanley⁠gpt

@Amankaushik481 @pablostanley 用 @pablostanley⁠gpt 一次就搞定了。

### 1061

作者: @Guillermo-Rauch
时间: 2025-11-23
链接: https://x.com/rauchg/status/1992464677088174429
互动: Likes: 322; Retweets: 11; Replies: 28; Quotes: 1; Views: 24,374; Bookmarks: 5; isReply: 0

Max Goatstappen 🏎️

车神马克斯·维斯塔潘（Max「GOAT」stappen）🏎️

### 1062

作者: @Guillermo-Rauch
时间: 2025-11-23
链接: https://x.com/rauchg/status/1992480046217637911
互动: Likes: 18; Retweets: 0; Replies: 2; Quotes: 0; Views: 2,040; Bookmarks: 0; isReply: 1

@tnvtwt @v0 Thx for the report we’ll take a look!

@tnvtwt @v0 感谢反馈，我们会去查看一下！

### 1063

作者: @Guillermo-Rauch
时间: 2025-11-23
链接: https://x.com/rauchg/status/1992480177713287329
互动: Likes: 1; Retweets: 0; Replies: 1; Quotes: 0; Views: 121; Bookmarks: 0; isReply: 1

@tnvtwt @v0 (We’ll grant you credits if applicable after investigation)

@tnvtwt @v0（感谢反馈。如果情况属实，我们会在调查后为您补发相应的积分。)

### 1064

作者: @Guillermo-Rauch
时间: 2025-11-23
链接: https://x.com/rauchg/status/1992660454804709682
互动: Likes: 367; Retweets: 12; Replies: 25; Quotes: 0; Views: 74,981; Bookmarks: 90; isReply: 0

Backend API function invocations on @vercel are growing 26% week-over-week. Primarily driven by Express, Hono &amp; Nitro.

Turns out devs want the same things for backends they already loved about Vercel. Great DX, fluid scale, preview deployments, instant rollbacks, great o11y…

@vercel 上的后端 API 函数调用量正以每周 26% 的速度增长，增长动力主要来自 Express、Hono 和 Nitro 这些框架。

这表明，开发者们同样希望后端服务能具备他们早已在 Vercel 上喜爱的那些优点：卓越的开发者体验（DX）、弹性伸缩能力、预览环境部署、即时回滚，以及出色的可观测性（Observability）。

### 1065

作者: @Guillermo-Rauch
时间: 2025-11-23
链接: https://x.com/rauchg/status/1992661530954125654
互动: Likes: 2; Retweets: 0; Replies: 1; Quotes: 0; Views: 881; Bookmarks: 0; isReply: 1

@reillyjodonnell @vercel Funny enough I just called it that on company fireside chat last Friday 😂

@reillyjodonnell @vercel 说来有趣，我上周五在公司内部的「炉边谈话」（fireside chat）活动上就这么叫它了 😂

### 1066

作者: @Guillermo-Rauch
时间: 2025-11-23
链接: https://x.com/rauchg/status/1992661769119289756
互动: Likes: 8; Retweets: 0; Replies: 0; Quotes: 0; Views: 995; Bookmarks: 2; isReply: 1

@chriscosentino_ @vercel Yes. API Routes / Route Handlers / Server Actions are a great way to go full stack with Next!

@chriscosentino_ @vercel 没错。API Routes、Route Handlers 和 Server Actions 这些功能，正是用 Next.js 进行全栈开发的利器！

### 1067

作者: @Guillermo-Rauch
时间: 2025-11-24
链接: https://x.com/rauchg/status/1992771214629392852
互动: Likes: 89; Retweets: 1; Replies: 3; Quotes: 1; Views: 20,087; Bookmarks: 2; isReply: 1

@mlg27_ Holy cook. Can’t wait to use this

@mlg27_ 哇，太牛了。等不及想试试了！

### 1068

作者: @Guillermo-Rauch
时间: 2025-11-24
链接: https://x.com/rauchg/status/1992826354887508310
互动: Likes: 6; Retweets: 0; Replies: 1; Quotes: 0; Views: 3,552; Bookmarks: 0; isReply: 1

@orcdev Great to hear!

@orcdev 太好了！

### 1069

作者: @Guillermo-Rauch
时间: 2025-11-24
链接: https://x.com/rauchg/status/1993000941994586477
互动: Likes: 593; Retweets: 49; Replies: 30; Quotes: 8; Views: 77,650; Bookmarks: 124; isReply: 0

LALIGA is trending again, so it's worth giving an update. We previously wrote about how this soccer league in Spain was granted broad internet censorship powers[1].

1️⃣ Vercel's customers have been unaffected
We've taken drastic measures to ensure the uptime of our customers. While we rejected LALIGA's broad approach, our goal at Vercel is to protect and maximize our customers' and developers' freedoms within the limits of the law.

We gave them a dedicated email inbox and an incident response automation. We have instructed our on-call SRE to expedite the review of these reports, because they can result in the loss of availability of entire sections of other, law-abiding customers.

This is what their email reports look like:

2️⃣ LALIGA's reports have been accurate
For every report we've received, we were able to verify that the URLs were hosting illegal streams of their copyrighted material.

I have condemned LALIGA's unprecedented and indiscriminate blocks[2], and have warned of the potential for this power to be misused.

So far, their reports have so far been valid. We expediently acted on them, in order to minimize the collateral damage.

3️⃣ Blocking hostnames vs blocking networks
If you look at their email report above, you'll notice they single out an IP address. The crux of the issue is that in modern CDN networks, that IP address can represent hundreds or thousands of legitimate customers.

The appropriate response would be to block *only the infringing hostname* by using the SNI fragment of the TLS handshake (e.g.: imagine blocking "𝚏𝚛𝚎𝚎𝚕𝚊𝚕𝚒𝚐𝚊𝚜𝚝𝚛𝚎𝚊𝚖.𝚝𝚟").

Since some CDNs don't offer this "granular blocking" possibility (given they encrypt SNI via a TLS protocol extension called "Encrypted Client Hello"), and ostensibly due to them not acting on the copyright reports, they're seeing significant collateral damage[3]

With over 150,000 paying teams and thousands of Enterprise accounts hosting critical services in areas like health care, emergency response, banking, government, and more, we're always working to protect our uptime, security, and availability.

[1] https://t.co/ufFVNUyfOE
[2] https://t.co/6MRSA8TedI
[3] https://t.co/JcSvRlx8Cf

西甲联赛（LALIGA）再次登上热搜，因此值得更新一下情况。我们之前写过，这家西班牙足球联赛如何获得了广泛的互联网审查权力 [1]。

1️⃣ Vercel 的客户未受影响我们已采取严厉措施，以确保我们客户的在线服务稳定运行。虽然我们拒绝了西甲联赛宽泛的屏蔽要求，但 Vercel 的目标是在法律允许的范围内，尽最大努力保护和维护我们的客户与开发者的自由。

我们为他们提供了一个专用的电子邮件收件箱和一套事件响应自动化流程。我们已经指示待命的站点可靠性工程师（SRE）加快审查这些报告，因为这些报告可能导致其他守法客户的整个服务部分无法访问。

他们的电子邮件报告如下所示：

2️⃣ 西甲联赛的报告一直准确对于我们收到的每一份报告，我们都已核实相关 URL 确实在托管其受版权保护内容的非法直播流。

我曾谴责西甲联赛史无前例且不加区分的屏蔽行为 [2]，并警告过这种权力存在被滥用的可能。

到目前为止，他们的报告都是有效的。我们已迅速对这些报告采取了行动，以最大限度地减少连带损害。

3️⃣ 屏蔽主机名与屏蔽网络如果你查看上面他们的电子邮件报告，你会发现他们指定了一个 IP 地址。问题的关键在于，在现代 CDN（内容分发网络）中，一个 IP 地址可能代表着数百甚至数千个合法客户。

正确的应对措施应该是 * 仅屏蔽侵权的主机名 *，这可以通过利用 TLS（安全传输层协议）握手过程中的 SNI（服务器名称指示）信息来实现（例如：想象一下只屏蔽「𝚏𝚛𝚎𝚎𝚕𝚊𝚕𝚒𝚐𝚊𝚜𝚝𝚛𝚎𝚊𝚖.𝚝𝚟」这个域名）。

由于一些 CDN 不提供这种「细粒度屏蔽」功能（因为它们通过一项名为「加密客户端问候」的 TLS 协议扩展来加密 SNI），并且表面上因为它们未对版权报告采取行动，这些 CDN 正遭受严重的连带损害 [3]。

我们为超过 15 万个付费团队和数千个企业账户提供服务，这些客户在医疗保健、应急响应、银行、政府等关键领域托管着重要服务。我们始终致力于保障我们服务的稳定运行时间、安全性和可用性。

[1] https://t.co/ufFVNUyfOE
[2] https://t.co/6MRSA8TedI
[3] https://t.co/JcSvRlx8Cf

### 1070

作者: @Guillermo-Rauch
时间: 2025-11-24
链接: https://x.com/rauchg/status/1993002564473012353
互动: Likes: 36; Retweets: 0; Replies: 1; Quotes: 0; Views: 4,793; Bookmarks: 0; isReply: 1

@m0nle0z No, it means keeping customers online

@m0nle0z 不是的，它的意思是要维持用户的在线活跃（或者说留存）。

### 1071

作者: @Guillermo-Rauch
时间: 2025-11-24
链接: https://x.com/rauchg/status/1993024947602833487
互动: Likes: 41; Retweets: 0; Replies: 2; Quotes: 0; Views: 4,960; Bookmarks: 4; isReply: 1

@m16vie This was causing significant damage for an entire country, and the courts signaled support for LALIGA, so we had to respond immediately. Inaction would have resulted in losses for our customers.

@m16vie 这给整个国家带来了巨大的损害，而且法院也表明了支持 LALIGA 的立场，因此我们不得不立即采取行动。如果坐视不管，我们的客户将蒙受损失。

### 1072

作者: @Guillermo-Rauch
时间: 2025-11-24
链接: https://x.com/rauchg/status/1993054732781490412
互动: Likes: 1,775; Retweets: 69; Replies: 91; Quotes: 22; Views: 131,524; Bookmarks: 731; isReply: 0

Opus is on a different level. It's unreasonably good at @nextjs and the best model we've tried on @v0 to date.

This is a one-shot generation. For a limited time you can try it on https://t.co/xxUbOD8oAb at no extra cost https://t.co/sVJvWSlpOv

Opus 完全处于另一个层级。它在 @nextjs 相关任务上表现超群，是我们迄今为止在 @v0 平台上测试过的最强模型。

上图是单次提示生成的结果。限时免费，您可以在 https://t.co/xxUbOD8oAb 上亲自体验。https://t.co/sVJvWSlpOv

### 1073

作者: @Guillermo-Rauch
时间: 2025-11-24
链接: https://x.com/rauchg/status/1993072481301868873
互动: Likes: 62; Retweets: 0; Replies: 15; Quotes: 0; Views: 3,602; Bookmarks: 0; isReply: 1

@vercel @dani_avila7 @YonathanDejene @izadoesdev @rohitdoesdev @arthty @franmoretti_ @stevenx1ee @hiaaryan @RaillyHugo @imskyleen @iamkunhello congrats to everyone!

@vercel @dani_avila7 @YonathanDejene @izadoesdev @rohitdoesdev @arthty @franmoretti_ @stevenx1ee @hiaaryan @RaillyHugo @imskyleen @iamkunhello 恭喜大家！

### 1074

作者: @Guillermo-Rauch
时间: 2025-11-24
链接: https://x.com/rauchg/status/1993105489069220080
互动: Likes: 156; Retweets: 3; Replies: 11; Quotes: 0; Views: 22,266; Bookmarks: 44; isReply: 0

Security products should be ① beautiful, ② fast, and ③ autonomous.

To get the best security for your apps, put Vercel in front. In realtime we analyze & fingerprint traffic, challenge & block bad bots, and surface all the data.

Custom rules, like rate limits, propagate worldwide in hundreds of milliseconds.

优秀的安全产品应具备三大特质：① 美观，② 高速，③ 自动化。

要为您的应用获取顶级安全保障，只需将 Vercel 置于前端。我们能够实时分析与识别流量指纹，验证并拦截恶意机器人，并将所有安全数据清晰呈现。

自定义规则（例如速率限制）可在数百毫秒内同步至全球网络并生效。

### 1075

作者: @Guillermo-Rauch
时间: 2025-11-24
链接: https://x.com/rauchg/status/1993106581219950988
互动: Likes: 23; Retweets: 0; Replies: 2; Quotes: 0; Views: 7,259; Bookmarks: 0; isReply: 1

We protect you out of the box because the internet can be a nasty place. But also because the industry is littered with legacy tech.

So many horror stories of products in the space:
▪️ …taking minutes to apply & propagate mitigations
▪️ …obscuring signals & data from you, the customer
▪️ …not being automated at all and putting the burden on you, or sell you professional services as a band-aid
▪️ …not being developer-friendly

It's time for a change ✌️

我们为您提供出厂即有的防护，因为互联网环境有时并不友好。但更重要的原因是，这个行业里陈旧技术堆积如山。

在这个领域，糟糕的产品体验比比皆是：
▪️ ... 部署和生效一个安全更新需要好几分钟
▪️ ... 将关键的信号和数据对您（客户）遮遮掩掩，缺乏透明度
▪️ ... 完全依赖手动操作，把负担都留给您，或者向您兜售像创可贴一样治标不治本的专业服务
▪️ ... 对开发人员极不友好是时候做出改变了 ✌️

### 1076

作者: @Guillermo-Rauch
时间: 2025-11-25
链接: https://x.com/rauchg/status/1993108012563939721
互动: Likes: 1; Retweets: 0; Replies: 0; Quotes: 0; Views: 140; Bookmarks: 0; isReply: 1

@matt_teeixeira Thank you!

@matt_teeixeira 谢谢你！

### 1077

作者: @Guillermo-Rauch
时间: 2025-11-25
链接: https://x.com/rauchg/status/1993139394719719705
互动: Likes: 49; Retweets: 1; Replies: 2; Quotes: 0; Views: 10,752; Bookmarks: 9; isReply: 1

Been getting feedback like this all day, from seasoned engineers and founders https://t.co/xxoWgolNed

今天一整天，我收到了许多来自资深工程师和创始人的类似反馈 https://t.co/xxoWgolNed

### 1078

作者: @Guillermo-Rauch
时间: 2025-11-25
链接: https://x.com/rauchg/status/1993152175019876470
互动: Likes: 289; Retweets: 8; Replies: 13; Quotes: 2; Views: 39,756; Bookmarks: 64; isReply: 0

Always bet on ⚛️

Amazing writeup from @fernandorojo of what went into building the @v0 iOS app with React Native &amp; @expo ↓

坚定选择 ⚛️（React）

以下是 @fernandorojo 分享的一篇深度好文，详细阐述了如何利用 React Native 和 @expo 构建 @v0 iOS 应用的全过程 ↓

### 1079

作者: @Guillermo-Rauch
时间: 2025-11-25
链接: https://x.com/rauchg/status/1993168972943180117
互动: Likes: 841; Retweets: 27; Replies: 116; Quotes: 18; Views: 54,880; Bookmarks: 42; isReply: 0

It’s better to re-watch The Hobbit / LOTR for the 100th time than to watch 99% of movies 😂

就算把《霍比特人》或《指环王》再看上第 100 遍，也比看市面上 99% 的新电影强啊😂

### 1080

作者: @Guillermo-Rauch
时间: 2025-11-25
链接: https://x.com/rauchg/status/1993392793675542811
互动: Likes: 15; Retweets: 0; Replies: 0; Quotes: 0; Views: 2,622; Bookmarks: 1; isReply: 1

@firecrawl_dev Cool. Amazing how succinct that is

@firecrawl_dev 酷。简洁得令人惊叹。

### 1081

作者: @Guillermo-Rauch
时间: 2025-11-25
链接: https://x.com/rauchg/status/1993416674020934055
互动: Likes: 17; Retweets: 0; Replies: 1; Quotes: 0; Views: 3,595; Bookmarks: 0; isReply: 1

@michlimlim Generate a gong

@michlimlim 生成一段锣声
（根据常见上下文，这通常指生成音频。若指生成图像，则可译为「生成一张锣的图片」。）

### 1082

作者: @Guillermo-Rauch
时间: 2025-11-25
链接: https://x.com/rauchg/status/1993419412247134530
互动: Likes: 2,408; Retweets: 142; Replies: 99; Quotes: 42; Views: 211,908; Bookmarks: 2,222; isReply: 0

We're releasing a visual agent & workflow builder

▪️ Fully open source
▪️ Built on https://t.co/HSAKEklwUl
▪️ Outputs "𝚞𝚜𝚎 𝚠𝚘𝚛𝚔𝚏𝚕𝚘𝚠" code 
▪️ Supports AI "text to workflow"
▪️ Powered by @aisdk & AI Elements
▪️ Sample integrations (@resend, @linear, @slack)

Clone & ship your own product, or embed AI workflow building capabilities into existing ones.

Demo: https://t.co/yFdRNSQW7A
Deploy: https://t.co/HTdXimRHm8

我们正式发布一款可视化 AI 智能体与工作流构建工具

▪️ 完全开源
▪️ 基于 https://t.co/HSAKEklwUl 构建
▪️ 输出 `use workflow` 代码
▪️ 支持 AI 驱动的文本生成工作流
▪️ 由 AISDK 和 AI Elements 提供技术支持
▪️ 内置示例集成（Resend，Linear，Slack)

您可以复刻代码并构建自己的产品，也可以将 AI 工作流构建能力嵌入到现有产品中。

演示：https://t.co/yFdRNSQW7A
部署：https://t.co/HTdXimRHm8

### 1083

作者: @Guillermo-Rauch
时间: 2025-11-25
链接: https://x.com/rauchg/status/1993420709616664844
互动: Likes: 17; Retweets: 0; Replies: 0; Quotes: 0; Views: 3,546; Bookmarks: 0; isReply: 1

@tonygwu @perplexity_ai Congrats! Little Aravind looking great 😄

@tonygwu @perplexity_ai 恭喜恭喜！小 Aravind 看起来真可爱 / 精神极了！😄
（注：根据上下文，「looking great」可灵活译为「真可爱」或「精神极了」，以更贴合中文对婴幼儿的常用赞美表达。）

### 1084

作者: @Guillermo-Rauch
时间: 2025-11-25
链接: https://x.com/rauchg/status/1993420911467545000
互动: Likes: 25; Retweets: 0; Replies: 1; Quotes: 0; Views: 5,886; Bookmarks: 0; isReply: 1

@EthanWoo @aisdk @resend @linear @slack 🔜 'open in v0' coming!

@EthanWoo @aisdk @resend @linear @slack 🔜 ' 在 v0 中打开 ' 功能即将上线！

### 1085

作者: @Guillermo-Rauch
时间: 2025-11-25
链接: https://x.com/rauchg/status/1993423277281394867
互动: Likes: 29; Retweets: 0; Replies: 3; Quotes: 0; Views: 5,342; Bookmarks: 3; isReply: 1

@ericciarla @aisdk @resend @linear @slack Imagine a @firecrawl_dev integration 🤯

@ericciarla @aisdk @resend @linear @slack 想象一下如果能和 @firecrawl_dev 集成会怎样 🤯

### 1086

作者: @Guillermo-Rauch
时间: 2025-11-25
链接: https://x.com/rauchg/status/1993446351879930054
互动: Likes: 144; Retweets: 5; Replies: 4; Quotes: 0; Views: 22,827; Bookmarks: 37; isReply: 0

Text-to-❄️

文本生成雪花（Text-to-❄️)

### 1087

作者: @Guillermo-Rauch
时间: 2025-11-26
链接: https://x.com/rauchg/status/1993494898218238194
互动: Likes: 34; Retweets: 0; Replies: 3; Quotes: 0; Views: 4,269; Bookmarks: 1; isReply: 1

@bekacru @vercel This is gonna be 🔥

@bekacru @vercel 这肯定会火！🔥

### 1088

作者: @Guillermo-Rauch
时间: 2025-11-26
链接: https://x.com/rauchg/status/1993497385075663086
互动: Likes: 275; Retweets: 5; Replies: 20; Quotes: 6; Views: 127,187; Bookmarks: 121; isReply: 0

.𝚏𝚊𝚜𝚝 is a banger (see: https://t.co/VAnuXw2HCR)

.𝚏𝚊𝚜𝚝 这东西太棒了（见：https://t.co/VAnuXw2HCR）

### 1089

作者: @Guillermo-Rauch
时间: 2025-11-26
链接: https://x.com/rauchg/status/1993512952042078253
互动: Likes: 612; Retweets: 17; Replies: 40; Quotes: 4; Views: 51,533; Bookmarks: 430; isReply: 0

Generated this e-com website with 2 @v0 Opus prompts + 1 @lumalabsai prompt for the video 🤘

https://t.co/gGUZKpbIE4 https://t.co/0Nu1QXpAgM

这个电商网站是用 2 个 @v0 Opus 提示词和 1 个 @lumalabsai 提示词搞定的，视频部分也是用提示词生成的，🤘

https://t.co/gGUZKpbIE4 https://t.co/0Nu1QXpAgM

### 1090

作者: @Guillermo-Rauch
时间: 2025-11-26
链接: https://x.com/rauchg/status/1993519799608263023
互动: Likes: 9; Retweets: 0; Replies: 0; Quotes: 0; Views: 2,885; Bookmarks: 1; isReply: 1

@webmaster @aisdk @resend @linear @slack 🫶 classic @ctatedev @haydenbleasel and @adriandlam_

向 @webmaster，@aisdk，@resend，@linear，@slack 🫶 以及一如既往的 @ctatedev，@haydenbleasel 和 @adriandlam_ 致意。

### 1091

作者: @Guillermo-Rauch
时间: 2025-11-26
链接: https://x.com/rauchg/status/1993714966562754989
互动: Likes: 351; Retweets: 16; Replies: 12; Quotes: 3; Views: 100,122; Bookmarks: 128; isReply: 0

This unlocks a lot. Faster onboarding for developer products. Delightful Marketplace integrations. Letting users own and pay for resources.

Try https://t.co/Jwx3vSrZaZ (which I used to generate this image). Sign in with Vercel and AI tokens will flow from your account! https://t.co/EXeNT63PZh

这带来了诸多可能性：它能加速开发者产品的上手过程，实现出色的市场平台集成，并让用户能够真正拥有并为其使用的资源付费。

试试 https://t.co/Jwx3vSrZaZ （我就是用它生成了这张图片）。使用 Vercel 账户登录，系统就会从您的账户中扣除相应的 AI Token！https://t.co/EXeNT63PZh

### 1092

作者: @Guillermo-Rauch
时间: 2025-11-26
链接: https://x.com/rauchg/status/1993776695443378336
互动: Likes: 12; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,529; Bookmarks: 0; isReply: 1

@mackenziechild It’s excellent

@mackenziechild 太棒了！

### 1093

作者: @Guillermo-Rauch
时间: 2025-11-26
链接: https://x.com/rauchg/status/1993796475495829536
互动: Likes: 0; Retweets: 0; Replies: 1; Quotes: 0; Views: 642; Bookmarks: 0; isReply: 1

@grinich @clarkbw @okbel @andrus @balazsorban44 @javierbyte @skllcrn @WorkOS @authkit @cramforce let's ship it! what do you need from our end?

@grinich @clarkbw @okbel @andrus @balazsorban44 @javierbyte @skllcrn @WorkOS @authkit @cramforce 准备上线了！我们这边需要做什么 / 提供什么支持？

### 1094

作者: @Guillermo-Rauch
时间: 2025-11-26
链接: https://x.com/rauchg/status/1993828253652717881
互动: Likes: 9; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,915; Bookmarks: 0; isReply: 1

@firecrawl_dev @vercel That was fast!

@firecrawl_dev @vercel 速度真快！

### 1095

作者: @Guillermo-Rauch
时间: 2025-11-27
链接: https://x.com/rauchg/status/1993869270779089106
互动: Likes: 261; Retweets: 14; Replies: 17; Quotes: 3; Views: 34,261; Bookmarks: 110; isReply: 0

Used 3 famous AI products today. 2/3 had full-on outages, the other one failed/hanging generations. 1 came through with what I needed but the experience was rough.

Still much better than not having AI do it (it would have taken me weeks / not having made it at all). But it's a good reminder of how early AI is, and overall how hard it is to make reliable products with cutting-edge tech.

Makes me even more excited about our investments into https://t.co/HSAKEklwUl and AI Gateway. You should architect agent products with the assumption that things will fail(over).

今天用了三款知名的 AI 产品。其中两款彻底宕机了，另一款则生成失败或卡顿。只有一款输出了我需要的结果，但整个过程也是磕磕绊绊。

尽管如此，这仍然比没有 AI 帮忙要好得多（不然可能得花我好几周时间，甚至根本做不出来）。但这很好地提醒了我们，AI 技术尚处于早期阶段，而且用尖端技术打造可靠的产品总体而言非常困难。

这让我对我们投资 https://t.co/HSAKEklwUl 和 AI Gateway 感到更加兴奋。在设计 AI 智能体（AI Agent）产品时，你应该预设组件会失败（或需要进行故障转移）。

### 1096

作者: @Guillermo-Rauch
时间: 2025-11-27
链接: https://x.com/rauchg/status/1993877092782756003
互动: Likes: 12; Retweets: 0; Replies: 0; Quotes: 0; Views: 3,811; Bookmarks: 1; isReply: 1

@sxcnxxx @v0 will take a look. that said, we're making massive upgrades to the runtime so you don't have papercuts with packages that would just work® in a normal next.js deployment, if that makes sense?

@sxcnxxx @v0 会关注一下。不过，我们正在对运行时进行大规模升级，目的是为了避免那些在标准 Next.js 部署环境下原本可以「开箱即用 ®」的软件包带来一些琐碎的问题，这样解释清楚吗？

### 1097

作者: @Guillermo-Rauch
时间: 2025-11-27
链接: https://x.com/rauchg/status/1993902143393472616
互动: Likes: 93; Retweets: 2; Replies: 7; Quotes: 1; Views: 16,100; Bookmarks: 11; isReply: 1

@Austen Amazing how good AI (Grok in this case) is at recognizing it as malicious and decoding it one-shot: https://t.co/MWmG2uSwih

@Austen 真厉害，AI（这次是 Grok）竟然能如此精准地识别出恶意内容并一次性成功解码：https://t.co/MWmG2uSwih

### 1098

作者: @Guillermo-Rauch
时间: 2025-11-27
链接: https://x.com/rauchg/status/1994079040794152988
互动: Likes: 23; Retweets: 1; Replies: 3; Quotes: 0; Views: 4,524; Bookmarks: 1; isReply: 1

@vercel_dev cool! nice job @primeintellect

@vercel_dev 太棒了！做得好啊 @primeintellect

### 1099

作者: @Guillermo-Rauch
时间: 2025-11-27
链接: https://x.com/rauchg/status/1994158738782212427
互动: Likes: 9; Retweets: 0; Replies: 1; Quotes: 0; Views: 3,936; Bookmarks: 1; isReply: 1

@cramforce That’s powerful

@cramforce 太强了

### 1100

作者: @Guillermo-Rauch
时间: 2025-11-27
链接: https://x.com/rauchg/status/1994168388869083296
互动: Likes: 330; Retweets: 5; Replies: 28; Quotes: 1; Views: 22,702; Bookmarks: 1; isReply: 0

Thankful. 🇺🇸 🦃 ▲ 🌎 👼

感恩。🇺🇸（美国） 🦃（火鸡） ▲（感恩节） 🌎（世界） 👼（天使 / 祝福）

### 1101

作者: @Guillermo-Rauch
时间: 2025-11-28
链接: https://x.com/rauchg/status/1994196351123402873
互动: Likes: 54; Retweets: 0; Replies: 3; Quotes: 0; Views: 7,419; Bookmarks: 2; isReply: 1

@RhysSullivan shadpm

@RhysSullivan shadpm
（注：输入内容为社交媒体提及及可能存在的拼写 / 简写，并非可翻译的完整英文段落，故保留原样。）

### 1102

作者: @Guillermo-Rauch
时间: 2025-11-28
链接: https://x.com/rauchg/status/1994270855052833164
互动: Likes: 109; Retweets: 2; Replies: 8; Quotes: 2; Views: 17,540; Bookmarks: 11; isReply: 0

You can see the Thanksgiving US holiday in global @vercel traffic. The gap between the dashed line (7d ago) and solid line. https://t.co/UIkc0g1gnN

从全球 Vercel 流量数据中，可以看出美国感恩节假期的影响。具体体现在图中虚线（7 天前）与实线之间的差距上。https://t.co/UIkc0g1gnN

### 1103

作者: @Guillermo-Rauch
时间: 2025-11-28
链接: https://x.com/rauchg/status/1994286421247709202
互动: Likes: 234; Retweets: 10; Replies: 46; Quotes: 5; Views: 29,857; Bookmarks: 15; isReply: 0

Thankful for 𝙽𝚊𝙽 !== 𝙽𝚊𝙽, [] == ![], “” == 0 and “” !== 0, “𝟻” - 𝟹 == 𝟸 and “𝟻” + 𝟹 == “𝟻𝟹”, 𝚝𝚢𝚙𝚎𝚘𝚏 𝚗𝚞𝚕𝚕 == “𝚘𝚋𝚓𝚎𝚌𝚝”, and 𝟶.𝟣 + 𝟶.𝟤 !== 𝟶.𝟥.

感谢 JavaScript 世界里的这些「宝藏」：`NaN !== NaN`、`[] == ![]`、`""== 0` 和 `""!== 0`、`"5」- 3 == 2`和`"5"+ 3 =="53"`、`typeof null ==「object"`，以及 `0.1 + 0.2 !== 0.3`。

### 1104

作者: @Guillermo-Rauch
时间: 2025-11-28
链接: https://x.com/rauchg/status/1994439906987556883
互动: Likes: 1; Retweets: 0; Replies: 1; Quotes: 0; Views: 234; Bookmarks: 1; isReply: 1

@israelwegierski @vercel No errors known. This is what Vercel AI says about the issue, lmk if helpful / applicable https://t.co/3TIid5P1C7

@israelwegierski @vercel 没有已知错误。这是 Vercel AI 对此问题的说明，如果这有帮助或适用的话，告诉我一声 https://t.co/3TIid5P1C7

### 1105

作者: @Guillermo-Rauch
时间: 2025-11-28
链接: https://x.com/rauchg/status/1994471955010130398
互动: Likes: 1; Retweets: 0; Replies: 1; Quotes: 0; Views: 66; Bookmarks: 0; isReply: 1

@rblalock Don Satur is insane. 9 de oro too. They go well with Yerba Mate obviously, Taraguí.

@rblalock Don Satur（唐·萨图尔，一款零食）简直绝了。9 de oro（一款饼干）也是。它们和 Taraguí 这个牌子的马黛茶（Yerba Mate）显然是绝配。

### 1106

作者: @Guillermo-Rauch
时间: 2025-11-28
链接: https://x.com/rauchg/status/1994472089374658734
互动: Likes: 1; Retweets: 0; Replies: 0; Quotes: 0; Views: 183; Bookmarks: 0; isReply: 1

@rblalock these 9 de oro specifically https://t.co/TC6PBQ8Qv6

@rblalock 具体指的是这些「9 de oro」（意为「金色 9 号」或「9 号金"）https://t.co/TC6PBQ8Qv6

### 1107

作者: @Guillermo-Rauch
时间: 2025-11-28
链接: https://x.com/rauchg/status/1994472263501189260
互动: Likes: 17; Retweets: 1; Replies: 1; Quotes: 0; Views: 17,179; Bookmarks: 1; isReply: 1

@wearebuiltwell @nextjs Problem is those headings are LLM-provided right?

@wearebuiltwell @nextjs 问题是，这些标题是 AI（大语言模型）生成的吧？

### 1108

作者: @Guillermo-Rauch
时间: 2025-11-28
链接: https://x.com/rauchg/status/1994474887831064661
互动: Likes: 17; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,473; Bookmarks: 0; isReply: 1

@wearebuiltwell @nextjs cool yeah, our CLI output could be much nicer. cc @feedthejim

@wearebuiltwell @nextjs 确实，我们的命令行界面（CLI）输出确实可以做得更漂亮。也 @feedthejim 看一下。

### 1109

作者: @Guillermo-Rauch
时间: 2025-11-28
链接: https://x.com/rauchg/status/1994478317282771114
互动: Likes: 2,017; Retweets: 89; Replies: 51; Quotes: 23; Views: 793,723; Bookmarks: 929; isReply: 0

A hackathon focused on models competing
This is gonna be fun 😄
https://t.co/D2o5lAGFBE https://t.co/UoNGDFFBEy

一场以模型竞赛为核心的黑客松（Hackathon)
肯定会很有意思 😄
https://t.co/D2o5lAGFBE https://t.co/UoNGDFFBEy

### 1110

作者: @Guillermo-Rauch
时间: 2025-11-28
链接: https://x.com/rauchg/status/1994484770181714376
互动: Likes: 312; Retweets: 8; Replies: 25; Quotes: 2; Views: 67,867; Bookmarks: 51; isReply: 0

1M+ deployments today
https://t.co/c9RzYTzbF8

目前部署量已超过 100 万
https://t.co/c9RzYTzbF8

### 1111

作者: @Guillermo-Rauch
时间: 2025-11-28
链接: https://x.com/rauchg/status/1994507656246300780
互动: Likes: 13; Retweets: 0; Replies: 0; Quotes: 0; Views: 3,818; Bookmarks: 0; isReply: 1

@jeff_weinstein thanks 🫶

@jeff_weinstein 感谢 🫶

### 1112

作者: @Guillermo-Rauch
时间: 2025-11-28
链接: https://x.com/rauchg/status/1994510438021960151
互动: Likes: 39; Retweets: 0; Replies: 0; Quotes: 0; Views: 5,691; Bookmarks: 0; isReply: 1

@tobi This is so well done and works fantastically on mobile. Kudos

@tobi 做得太棒了，在手机上的效果也特别好。给你点赞！

### 1113

作者: @Guillermo-Rauch
时间: 2025-11-28
链接: https://x.com/rauchg/status/1994512482191511631
互动: Likes: 82; Retweets: 0; Replies: 3; Quotes: 0; Views: 17,695; Bookmarks: 4; isReply: 1

@EastlondonDev Definitely a slick idea and I’m not claiming to have come up with it. It’d be awesome to link to his example if it’s in the v0 community templates directory. Thankful for him using our product 🫶

@EastlondonDev 这主意确实很酷，而且我可不是说这是我想出来的。如果他的例子在 v0 社区模板目录里，能链过去就太好了。非常感谢他使用我们的产品 🫶

### 1114

作者: @Guillermo-Rauch
时间: 2025-11-29
链接: https://x.com/rauchg/status/1994590547013742838
互动: Likes: 2; Retweets: 0; Replies: 0; Quotes: 0; Views: 923; Bookmarks: 0; isReply: 1

@rcxml Dope

@rcxml 牛啊

### 1115

作者: @Guillermo-Rauch
时间: 2025-11-29
链接: https://x.com/rauchg/status/1994802107673973140
互动: Likes: 13; Retweets: 0; Replies: 0; Quotes: 0; Views: 4,340; Bookmarks: 0; isReply: 1

@lgrammel @colinhacks @espen_codes Great goal

@lgrammel @colinhacks @espen_codes 目标很棒！

### 1116

作者: @Guillermo-Rauch
时间: 2025-11-29
链接: https://x.com/rauchg/status/1994833564136034809
互动: Likes: 13; Retweets: 0; Replies: 0; Quotes: 0; Views: 4,100; Bookmarks: 3; isReply: 1

@jh3yy Squircles hit different

@jh3yy 圆角方形的感觉就是不一样。

### 1117

作者: @Guillermo-Rauch
时间: 2025-11-29
链接: https://x.com/rauchg/status/1994834831759609869
互动: Likes: 12; Retweets: 0; Replies: 0; Quotes: 0; Views: 5,396; Bookmarks: 1; isReply: 1

@soleio Love it

@soleio 点赞！/ 赞！/ 喜欢！
（注：根据具体语境，可选择最贴切的表达。例如，在微博或推特回复中，「赞！」或「喜欢！」都是非常自然且地道的表达方式，准确传达了原文简短、积极的赞赏语气。）

### 1118

作者: @Guillermo-Rauch
时间: 2025-11-30
链接: https://x.com/rauchg/status/1994935614232539257
互动: Likes: 737; Retweets: 36; Replies: 32; Quotes: 4; Views: 63,908; Bookmarks: 586; isReply: 0

Products, platforms, people excel in different dimensions.

I've always been a fan of the little diagrams you see in videogames (e.g.: in FIFA, Messi is good at Offense, Defense, Speed…)

I built the @v0 version of it: https://t.co/ULxQmYR2CK https://t.co/kB1OxxdFF4

产品、平台和人都各有千秋，在不同维度上能力突出。

我一直是电子游戏里那种小图表的忠实粉丝（比如在《FIFA》游戏里，梅西的能力值会在进攻、防守、速度等多个维度上用雷达图展示）。

我为此制作了一个 @v0 版本：https://t.co/ULxQmYR2CK https://t.co/kB1OxxdFF4

### 1119

作者: @Guillermo-Rauch
时间: 2025-11-30
链接: https://x.com/rauchg/status/1994937110944747582
互动: Likes: 32; Retweets: 0; Replies: 1; Quotes: 0; Views: 12,168; Bookmarks: 25; isReply: 1

Published as a template
https://t.co/QXW53P0pV7

已作为模板发布
https://t.co/QXW53P0pV7

### 1120

作者: @Guillermo-Rauch
时间: 2025-11-30
链接: https://x.com/rauchg/status/1994983431609225552
互动: Likes: 12; Retweets: 1; Replies: 2; Quotes: 0; Views: 4,421; Bookmarks: 1; isReply: 1

@jasonzhou1993 @SuperDesignDev Cool

@jasonzhou1993 @SuperDesignDev 酷

### 1121

作者: @Guillermo-Rauch
时间: 2025-11-30
链接: https://x.com/rauchg/status/1995159137966317613
互动: Likes: 1; Retweets: 0; Replies: 0; Quotes: 0; Views: 67; Bookmarks: 0; isReply: 1

@RayevKaniyet @jasonzhou1993 @SuperDesignDev Wow! Clean

哇！简洁利落！

### 1122

作者: @Guillermo-Rauch
时间: 2025-12-01
链接: https://x.com/rauchg/status/1995317349465862552
互动: Likes: 571; Retweets: 7; Replies: 38; Quotes: 3; Views: 57,917; Bookmarks: 156; isReply: 0

v0, make me Robinhood on my phone, make no mistakes https://t.co/6Zv4VYLAcE

v0，给我在手机上整个 Robinhood 那样的应用，可别搞砸了。https://t.co/6Zv4VYLAcE

### 1123

作者: @Guillermo-Rauch
时间: 2025-12-01
链接: https://x.com/rauchg/status/1995319957396337090
互动: Likes: 55; Retweets: 0; Replies: 2; Quotes: 0; Views: 12,391; Bookmarks: 4; isReply: 1

@RhysSullivan cc @jaredpalmer 

Overall I think there’re three issues:

- No need to do SSO for public repos
- Login is re-enforced too frequently. Which is a pain given…
- Login handshake and redirects are too slow

@RhysSullivan cc @jaredpalmer

总的来说，我认为存在三个问题：

- 对于公共仓库（public repos）没有必要使用单点登录（SSO）。
- 登录验证过于频繁，需要反复重新登录。考虑到实际情况...，这体验很差。
- 登录握手和页面重定向的过程太慢了。

### 1124

作者: @Guillermo-Rauch
时间: 2025-12-01
链接: https://x.com/rauchg/status/1995368151954178326
互动: Likes: 1; Retweets: 0; Replies: 0; Quotes: 0; Views: 2,414; Bookmarks: 1; isReply: 1

@stressandvest so good

@stressandvest 太棒了！

### 1125

作者: @Guillermo-Rauch
时间: 2025-12-01
链接: https://x.com/rauchg/status/1995479884118761591
互动: Likes: 18; Retweets: 0; Replies: 1; Quotes: 0; Views: 6,487; Bookmarks: 0; isReply: 1

@1weiho so good!

@1weiho 太棒了！

### 1126

作者: @Guillermo-Rauch
时间: 2025-12-01
链接: https://x.com/rauchg/status/1995490177654157390
互动: Likes: 5; Retweets: 0; Replies: 1; Quotes: 0; Views: 663; Bookmarks: 0; isReply: 1

@fjpedrosa86 @fernandorojo It’s in the video 😁

视频里有答案哦 😁

### 1127

作者: @Guillermo-Rauch
时间: 2025-12-01
链接: https://x.com/rauchg/status/1995497239310197070
互动: Likes: 3; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,543; Bookmarks: 0; isReply: 1

@nutlope Cool

@nutlope 酷啊！

### 1128

作者: @Guillermo-Rauch
时间: 2025-12-01
链接: https://x.com/rauchg/status/1995503348251083129
互动: Likes: 9; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,780; Bookmarks: 1; isReply: 1

@zarazhangrui Cool been looking for sth like this

不错，我一直在找类似的东西。

### 1129

作者: @Guillermo-Rauch
时间: 2025-12-01
链接: https://x.com/rauchg/status/1995562122043163039
互动: Likes: 2; Retweets: 0; Replies: 0; Quotes: 0; Views: 52; Bookmarks: 0; isReply: 1

@astr0mnaut Yes. v0 automatically reads console logs of the embedded preview. But we’re going further

是的。v0 版本能够自动读取内嵌预览的控制台日志。不过，我们的计划远不止于此。

### 1130

作者: @Guillermo-Rauch
时间: 2025-12-01
链接: https://x.com/rauchg/status/1995567529331478912
互动: Likes: 364; Retweets: 20; Replies: 31; Quotes: 9; Views: 62,490; Bookmarks: 49; isReply: 0

Vercel now features Aurora PostgreSQL, Amazon DynamoDB, and Aurora DSQL in our marketplace.

One-click install of the world’s most reliable, scalable, and secure managed databases.
https://t.co/rguNBDTX3M

Vercel 应用市场现已推出 Aurora PostgreSQL、Amazon DynamoDB 和 Aurora DSQL。

一键即可安装全球最可靠、可扩展且安全的托管数据库。
https://t.co/rguNBDTX3M

### 1131

作者: @Guillermo-Rauch
时间: 2025-12-01
链接: https://x.com/rauchg/status/1995568454007751033
互动: Likes: 59; Retweets: 1; Replies: 2; Quotes: 1; Views: 12,076; Bookmarks: 1; isReply: 1

This is the result of a many-months-long collaboration between our teams to streamline security, automatically provision @awscloud accounts, and optimize provisioning latency.

It makes the battle-tested AWS database infrastructure truly magical.
https://t.co/cEiNXSXy66

这是我们双方团队历时数月合作的成果，旨在提升安全性、自动开通 @awscloud 账户，并大幅缩短资源开通时间。

这让久经考验的 AWS 数据库基础设施变得如魔法般强大易用。
https://t.co/cEiNXSXy66

### 1132

作者: @Guillermo-Rauch
时间: 2025-12-01
链接: https://x.com/rauchg/status/1995569218142830737
互动: Likes: 1; Retweets: 0; Replies: 1; Quotes: 0; Views: 36; Bookmarks: 0; isReply: 1

@AlexayToska @vercel Very, very soon!

@AlexayToska @vercel 马上马上！

### 1133

作者: @Guillermo-Rauch
时间: 2025-12-01
链接: https://x.com/rauchg/status/1995572794655211724
互动: Likes: 1; Retweets: 0; Replies: 0; Quotes: 0; Views: 708; Bookmarks: 0; isReply: 1

@justayushtomar I agree!

@justayushtomar 我同意！

### 1134

作者: @Guillermo-Rauch
时间: 2025-12-01
链接: https://x.com/rauchg/status/1995573773945508124
互动: Likes: 6; Retweets: 0; Replies: 0; Quotes: 0; Views: 962; Bookmarks: 0; isReply: 1

@aarondelasy Satire or AI?

@aarondelasy 这是讽刺，还是 AI 之作？

### 1135

作者: @Guillermo-Rauch
时间: 2025-12-01
链接: https://x.com/rauchg/status/1995592918468624408
互动: Likes: 13; Retweets: 0; Replies: 3; Quotes: 0; Views: 6,542; Bookmarks: 0; isReply: 1

@Dan_The_Goodman No debate at least with Dynamo right?

@Dan_The_Goodman 至少在 Dynamo 这件事上没什么可争论的，是吧？

### 1136

作者: @Guillermo-Rauch
时间: 2025-12-01
链接: https://x.com/rauchg/status/1995601962059137227
互动: Likes: 14; Retweets: 0; Replies: 1; Quotes: 0; Views: 764; Bookmarks: 0; isReply: 1

@he_i_sen_berg @RhysSullivan Interesting

@he_i_sen_berg @RhysSullivan 有意思。

### 1137

作者: @Guillermo-Rauch
时间: 2025-12-01
链接: https://x.com/rauchg/status/1995608076926550487
互动: Likes: 8; Retweets: 0; Replies: 0; Quotes: 0; Views: 644; Bookmarks: 0; isReply: 1

@arshinvests @RhysSullivan It’s good. Usually open

挺好的。通常都是开放的。

### 1138

作者: @Guillermo-Rauch
时间: 2025-12-02
链接: https://x.com/rauchg/status/1995700783472648522
互动: Likes: 62; Retweets: 0; Replies: 5; Quotes: 3; Views: 38,685; Bookmarks: 1; isReply: 1

@hungv47 @vercel Feel free to send details over DM. I DMd you

@hungv47 @vercel 详情可以随时私信我。我已经给你发私信了。

### 1139

作者: @Guillermo-Rauch
时间: 2025-12-02
链接: https://x.com/rauchg/status/1995731621723398491
互动: Likes: 2; Retweets: 0; Replies: 0; Quotes: 0; Views: 123; Bookmarks: 1; isReply: 1

@itszn13 Truly epic work

@itszn13 这工作真是太牛了！

### 1140

作者: @Guillermo-Rauch
时间: 2025-12-02
链接: https://x.com/rauchg/status/1995861912786272392
互动: Likes: 15; Retweets: 0; Replies: 0; Quotes: 0; Views: 6,068; Bookmarks: 2; isReply: 1

@emilkowalski Great writing

@emilkowalski 写得太棒了

### 1141

作者: @Guillermo-Rauch
时间: 2025-12-02
链接: https://x.com/rauchg/status/1995913814521544944
互动: Likes: 6; Retweets: 0; Replies: 1; Quotes: 0; Views: 201; Bookmarks: 0; isReply: 1

@aamirv1 @mrt3eaz @divv_dev @MohitSi44211571 @sebselassie @agonzalezrom @zeroxjackson @p_naix @swarnenduG07 @he_i_sen_berg @RhysSullivan Facts

@aamirv1 @mrt3eaz @divv_dev @MohitSi44211571 @sebselassie @agonzalezrom @zeroxjackson @p_naix @swarnenduG07 @he_i_sen_berg @RhysSullivan 说得对。

### 1142

作者: @Guillermo-Rauch
时间: 2025-12-02
链接: https://x.com/rauchg/status/1995963299557745076
互动: Likes: 198; Retweets: 14; Replies: 14; Quotes: 3; Views: 39,472; Bookmarks: 23; isReply: 0

We’re bringing Vercel’s DX and self-driving infrastructure to Python, by teaming up with @1st1, @elprans & the Gel team.

I’m so excited to work with these guys. True missionaries that have lived and breathed Python their entire professional lives. I’m confident they’ll make Vercel the best Python cloud.

We’re also sponsoring the Python Software Foundation, core maintainer @SerhiyStorchaka, and are committed to the long-term strength of the open Python ecosystem.

我们正与 @1st1，@elprans 以及 Gel 团队携手，将 Vercel 卓越的开发者体验（DX）和智能自动化基础设施引入 Python 领域。

能与这几位专家共事，我倍感振奋。他们是真正的布道者，将整个职业生涯都奉献给了 Python。我坚信，他们将助力 Vercel 成为最出色的 Python 云平台。

同时，我们也将赞助 Python 软件基金会和核心维护者 @SerhiyStorchaka，并致力于保障 Python 开源生态系统的长期繁荣与稳定。

### 1143

作者: @Guillermo-Rauch
时间: 2025-12-03
链接: https://x.com/rauchg/status/1996020538758889651
互动: Likes: 241; Retweets: 2; Replies: 0; Quotes: 0; Views: 18,476; Bookmarks: 1; isReply: 1

@bunjavascript Congrats @jarredsumner &amp; @anthropicai… excited to continue our collaboration and support for Bun on @vercel 💪

@bunjavascript 恭喜 @jarredsumner 与 @anthropicai！我们很高兴能与 @vercel 继续合作，并支持 Bun 的发展 💪

### 1144

作者: @Guillermo-Rauch
时间: 2025-12-03
链接: https://x.com/rauchg/status/1996028970958213187
互动: Likes: 152; Retweets: 7; Replies: 8; Quotes: 3; Views: 25,383; Bookmarks: 87; isReply: 0

The Vercel BFCM map rebuilt as a @v0 community template by @_abilshr 😲
https://t.co/CXaYOdRkYt

由 @_abilshr 使用 @v0 社区模板重建的 Vercel BFCM（黑五网一）地图 😲
https://t.co/CXaYOdRkYt

### 1145

作者: @Guillermo-Rauch
时间: 2025-12-03
链接: https://x.com/rauchg/status/1996034791553335552
互动: Likes: 633; Retweets: 19; Replies: 16; Quotes: 4; Views: 90,715; Bookmarks: 394; isReply: 0

Impressive agent built on @vercel workflows. AI in the service of quality

这是一个基于 @vercel 工作流构建的、令人印象深刻的 AI 智能体，致力于用 AI 技术来保障和提升质量。

### 1146

作者: @Guillermo-Rauch
时间: 2025-12-03
链接: https://x.com/rauchg/status/1996035240624828648
互动: Likes: 4; Retweets: 0; Replies: 0; Quotes: 0; Views: 2,334; Bookmarks: 1; isReply: 1

@delba_oliveira These videos are so zen 😍

@delba_oliveira 这些视频好治愈，让人心静 😍

### 1147

作者: @Guillermo-Rauch
时间: 2025-12-03
链接: https://x.com/rauchg/status/1996241834549617010
互动: Likes: 424; Retweets: 0; Replies: 5; Quotes: 0; Views: 21,088; Bookmarks: 5; isReply: 1

@bruvimtired You left out the "may i meet you" opener

@bruvimtired 你忘了用「可以认识一下吗」这个开场白。

### 1148

作者: @Guillermo-Rauch
时间: 2025-12-03
链接: https://x.com/rauchg/status/1996256269838295133
互动: Likes: 65; Retweets: 0; Replies: 2; Quotes: 2; Views: 9,851; Bookmarks: 1; isReply: 1

@deno_land 💪 awesome work Deno team, thanks for helping protect the ecosystem

@deno_land 💪 Deno 团队干得漂亮，感谢你们为保护生态所做的贡献！

### 1149

作者: @Guillermo-Rauch
时间: 2025-12-03
链接: https://x.com/rauchg/status/1996256382862192934
互动: Likes: 443; Retweets: 2; Replies: 9; Quotes: 0; Views: 83,762; Bookmarks: 4; isReply: 1

@reactjs Thank you Meta team for the expedient support and collaboration

@reactjs 感谢 Meta 团队给予的迅速响应与鼎力支持。

### 1150

作者: @Guillermo-Rauch
时间: 2025-12-03
链接: https://x.com/rauchg/status/1996256609128104354
互动: Likes: 346; Retweets: 0; Replies: 13; Quotes: 0; Views: 26,770; Bookmarks: 5; isReply: 1

@dok2001 @Cloudflare @nextjs Thank you Cloudflare team for the expedient collaboration on this

@dok2001 @Cloudflare @nextjs 感谢 Cloudflare 团队在此事上的高效协作。

### 1151

作者: @Guillermo-Rauch
时间: 2025-12-03
链接: https://x.com/rauchg/status/1996274628600455194
互动: Likes: 31; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,914; Bookmarks: 0; isReply: 1

@bruvimtired Btw cool side effect is this has opened awesome internal threads on how vercel agent could have self-diagnosed this and demistify the puzzling error. Thank you! cc @tomdale @julianbenegas8

@bruvimtired 顺便提一下，一个很棒的影响是，这引发了一些精彩的内部讨论，探讨 Vercel Agent 本该如何自行诊断此问题并澄清那个令人费解的错误。谢谢！也转给 @tomdale @julianbenegas8

### 1152

作者: @Guillermo-Rauch
时间: 2025-12-03
链接: https://x.com/rauchg/status/1996275446921756992
互动: Likes: 39; Retweets: 0; Replies: 2; Quotes: 0; Views: 3,965; Bookmarks: 0; isReply: 1

@Railway Thanks Railway team! 💪

@Railway 感谢 Railway 团队！太给力了！💪

### 1153

作者: @Guillermo-Rauch
时间: 2025-12-03
链接: https://x.com/rauchg/status/1996275756528492843
互动: Likes: 9; Retweets: 0; Replies: 1; Quotes: 0; Views: 3,604; Bookmarks: 1; isReply: 1

@RhysSullivan can I do a QA run

@RhysSullivan 我可以跑一轮测试吗？

### 1154

作者: @Guillermo-Rauch
时间: 2025-12-03
链接: https://x.com/rauchg/status/1996285215464210782
互动: Likes: 270; Retweets: 3; Replies: 13; Quotes: 0; Views: 24,517; Bookmarks: 10; isReply: 0

After my @awscloud keynote I got to hold a Blue Origin cyclonic separator 😳. 

It’s a privilege to help deliver https://t.co/pOVEy9ghDC on Vercel. What an inspiring mission! https://t.co/VAR3YZnOMt

在我做完 @awscloud 的主题演讲后，我拿到了一个蓝色起源（Blue Origin）的旋风分离器 😳。

能帮助在 Vercel 上交付 https://t.co/pOVEy9ghDC 真是莫大的荣幸。这是多么鼓舞人心的一项事业！https://t.co/VAR3YZnOMt

### 1155

作者: @Guillermo-Rauch
时间: 2025-12-03
链接: https://x.com/rauchg/status/1996295375398097033
互动: Likes: 26; Retweets: 1; Replies: 1; Quotes: 0; Views: 3,527; Bookmarks: 4; isReply: 1

@anything Congrats!! Extremely proud to be supporting @anything with Vercel’s ai cloud infrastructure 💪

@anything 恭喜恭喜！！我们无比自豪，能通过 Vercel 的 AI 云平台为 @anything 提供支持，助你一臂之力 💪

### 1156

作者: @Guillermo-Rauch
时间: 2025-12-04
链接: https://x.com/rauchg/status/1996374692454936917
互动: Likes: 194; Retweets: 7; Replies: 15; Quotes: 1; Views: 15,418; Bookmarks: 27; isReply: 0

You can now bring your own MCPs to @v0. Powerful
https://t.co/9gXJSfMs9O

你现在可以将你自己的 MCPs 引入 @v0 了。功能强大。
https://t.co/9gXJSfMs9O

### 1157

作者: @Guillermo-Rauch
时间: 2025-12-04
链接: https://x.com/rauchg/status/1996381428666523859
互动: Likes: 513; Retweets: 41; Replies: 21; Quotes: 3; Views: 45,614; Bookmarks: 171; isReply: 0

🎦 Self-driving infrastructure on @awscloud
▪ 11M customers @ 1T monthly requests
▪ Pages & Pixels → Agents & Tokens
  ▫ Fluid: Compute of AI
  ▫ AI Gateway: CDN of Tokens
  ▫ @aisdk: Next.js of Agents
▪ How @reuters is shipping agents on Vercel

🎦 基于 @awscloud 的自动化基础设施
▪ 服务 1.1 亿客户，每月处理 1 万亿次请求
▪ 从页面与像素到 AI 智能体（AI Agent）与 Token
 ▫ Fluid：AI 的计算核心
 ▫ AI Gateway：Token 的智能分发网络
 ▫ @aisdk：快速构建 AI 智能体的开发框架
▪ @reuters 如何在 Vercel 平台上快速交付 AI 智能体

### 1158

作者: @Guillermo-Rauch
时间: 2025-12-04
链接: https://x.com/rauchg/status/1996384790191448237
互动: Likes: 2; Retweets: 0; Replies: 0; Quotes: 0; Views: 881; Bookmarks: 0; isReply: 1

@alex_holovach @awscloud @aisdk @Reuters true

@alex_holovach @awscloud @aisdk @Reuters 属实。/ 是的。/ 确实如此。

### 1159

作者: @Guillermo-Rauch
时间: 2025-12-04
链接: https://x.com/rauchg/status/1996483994620461099
互动: Likes: 702; Retweets: 54; Replies: 30; Quotes: 12; Views: 89,471; Bookmarks: 186; isReply: 0

Today we partnered with Meta to disclose a critical vulnerability in React Server Components, impacting Next.js.

Huge credit to Lachlan Davidson for responsibly reporting this to Meta and to our industry partners for responding quickly to our call-to-action. 

This is how open source security is supposed to be: responsible disclosure, fast mobilization, and close collaboration.

Within 72 hours, we patched React, shipped WAF mitigations for all Vercel customers, and coordinated major cloud and security providers to protect their customers in the same way.

The united response across the ecosystem has been incredible. AWS, Microsoft, Cloudflare, Fastly, Akamai, F5, Google, Deno, Netlify, Railway, Fly, and others moved quickly with platform protections and clear guidance to their customers. 

As a reminder, if you’re running Next.js 15 or 16, please upgrade immediately to 15.5.7 or 16.0.7. Vercel customers have platform-level protections, but upgrading is still a must. 

Ref: https://t.co/Y1cVSAjViO

今天，我们与 Meta 合作，披露了 React Server Components 中的一个关键漏洞，该漏洞影响了 Next.js。

我们高度赞扬 Lachlan Davidson 负责任地向 Meta 报告了此问题，同时也感谢我们的行业合作伙伴对我们的行动呼吁做出的快速响应。

这正体现了开源安全应有的协作模式：负责任的漏洞披露、快速的应急动员以及紧密的行业合作。

在 72 小时内，我们完成了对 React 的漏洞修复，为所有 Vercel 客户部署了 WAF（Web 应用防火墙）缓解措施，并协调了主要的云服务与安全提供商，使其能够以相同的方式保护各自的客户。

整个生态系统的协同响应非常出色。AWS、Microsoft、Cloudflare、Fastly、Akamai、F5、Google、Deno、Netlify、Railway、Fly 等公司迅速行动，实施了平台级别的防护措施，并向其客户提供了清晰的指导。

提醒各位开发者，如果您正在运行 Next.js 15 或 16 版本，请立即升级至 15.5.7 或 16.0.7。Vercel 的客户虽然享有平台级别的保护，但升级应用程序版本仍然是必要的。

参考链接：https://t.co/Y1cVSAjViO

### 1160

作者: @Guillermo-Rauch
时间: 2025-12-04
链接: https://x.com/rauchg/status/1996486164799533165
互动: Likes: 451; Retweets: 13; Replies: 9; Quotes: 7; Views: 247,118; Bookmarks: 56; isReply: 1

One more note. I want to specially call out the incredible ingenuity of the researcher Lachlan Davidson, and thank him again for his responsible disclosure.

While the category of vulnerability is well-studied and familiar, the POC required deep study of React internals and an intricate cleverness that LLMs are *a far cry* from achieving.

最后还有一点需要特别说明。我要特别强调研究员 Lachlan Davidson 展现出的非凡智慧，并再次感谢他进行负责任的漏洞披露。

尽管这类安全漏洞本身已被广泛研究，但构建这个漏洞验证（POC）需要对 React 内部机制的深入钻研，以及一种精妙复杂的创造性 —— 这种能力，是目前的大语言模型（LLM）* 远远无法企及 * 的。

### 1161

作者: @Guillermo-Rauch
时间: 2025-12-04
链接: https://x.com/rauchg/status/1996486390344011835
互动: Likes: 15; Retweets: 0; Replies: 1; Quotes: 0; Views: 7,704; Bookmarks: 2; isReply: 1

@pua6al @vercel Do both files show up in the Source tab of the vercel deployment?

@pua6al @vercel 这两个文件在 Vercel 部署的 Source 标签里都能看到吗？

### 1162

作者: @Guillermo-Rauch
时间: 2025-12-04
链接: https://x.com/rauchg/status/1996629782164091220
互动: Likes: 198; Retweets: 0; Replies: 4; Quotes: 0; Views: 27,935; Bookmarks: 6; isReply: 1

@mitsuhiko @AmpCode That’s not it, not even remotely

@mitsuhiko @AmpCode 不对，完全不是这么回事。

### 1163

作者: @Guillermo-Rauch
时间: 2025-12-04
链接: https://x.com/rauchg/status/1996630743183999150
互动: Likes: 309; Retweets: 3; Replies: 24; Quotes: 4; Views: 114,458; Bookmarks: 86; isReply: 0

When the POC comes out, it’ll be a humbling moment for LLMs and how we use them. What’s circulating is extremely naive and incorrect.

Experienced engineers are sharing plausible-sounding hallucinations from frontier models.

Reminder to bump React, Next &amp; frameworks.

当概念验证（Proof of Concept，POC）结果公布时，对于大语言模型（LLMs）及其应用方式而言，无疑将是一个令人警醒的时刻。目前流传的许多说法都极其天真且错误。

一些经验丰富的工程师正在分享那些由前沿模型生成的、听起来头头是道实则谬误的「幻觉」（Hallucination）案例。

提醒大家记得更新 React、Next 及相关框架的版本。

### 1164

作者: @Guillermo-Rauch
时间: 2025-12-04
链接: https://x.com/rauchg/status/1996631847539978539
互动: Likes: 16; Retweets: 0; Replies: 1; Quotes: 0; Views: 8,398; Bookmarks: 0; isReply: 1

@nedmehic Expo has experimental RSC support. It’s a bad idea to have latent vulnerable code in your supply chain. Upgrade!

@nedmehic Expo 已提供实验性的 RSC（React Server Components）支持。让存在漏洞的代码潜伏在你的供应链中是个糟糕的做法。请尽快升级！

### 1165

作者: @Guillermo-Rauch
时间: 2025-12-04
链接: https://x.com/rauchg/status/1996641116490551771
互动: Likes: 17; Retweets: 1; Replies: 1; Quotes: 0; Views: 3,445; Bookmarks: 2; isReply: 1

@ryanvogel @nextjs Noice. More to come

@ryanvogel @nextjs 给力。后续还有更多。

### 1166

作者: @Guillermo-Rauch
时间: 2025-12-04
链接: https://x.com/rauchg/status/1996651514602180816
互动: Likes: 6; Retweets: 0; Replies: 1; Quotes: 0; Views: 3,056; Bookmarks: 0; isReply: 1

@Southclaws @timneutkens There’s definitely a package cache. cc @grappeggia to look into this

You’ll also be happy to hear we have a major improvement coming to package installs

@Southclaws @timneutkens 确实存在一个包缓存。cc @grappeggia 来跟进看一下这个问题。

另外有个好消息：我们在软件包安装方面即将有一项重大改进。

### 1167

作者: @Guillermo-Rauch
时间: 2025-12-04
链接: https://x.com/rauchg/status/1996663098007343423
互动: Likes: 2; Retweets: 0; Replies: 1; Quotes: 0; Views: 149; Bookmarks: 0; isReply: 1

@hermes_f For sure. Working on that. cc @tomdale

@hermes_f 没问题。这就处理。@tomdale

### 1168

作者: @Guillermo-Rauch
时间: 2025-12-04
链接: https://x.com/rauchg/status/1996681619722457205
互动: Likes: 36; Retweets: 1; Replies: 1; Quotes: 0; Views: 7,114; Bookmarks: 3; isReply: 1

@mfreeman451 I'm not, given how much mental power it took me to understand it. Anyone who produces it from first principles is encouraged to expediently apply to work at vercel 😉

@mfreeman451 我可做不到，毕竟为了理解它，我死了不少脑细胞。任何能从头推导出这东西的人，我们强烈建议你赶紧去 Vercel 应聘工作 😉

### 1169

作者: @Guillermo-Rauch
时间: 2025-12-04
链接: https://x.com/rauchg/status/1996701434029789366
互动: Likes: 266; Retweets: 19; Replies: 9; Quotes: 9; Views: 48,083; Bookmarks: 29; isReply: 0

We’ve got confirmation of a working #react2shell POC being shared.

We’ve verified Vercel’s Web Application Firewall is successfully blocking this known variant.

We are also seeing bad actors attempt exploitation. Upgrading React &amp; frameworks remains a top priority.

我们已确认，一个可用的 #react2shell 概念验证（POC）正在被传播。

经验证，Vercel 的 Web 应用防火墙（WAF）已成功拦截了这种已知的攻击手法。

同时，我们也监测到有恶意攻击者在尝试利用该漏洞。因此，及时升级 React 及其相关框架（如 Next.js）仍是当前的重中之重。

### 1170

作者: @Guillermo-Rauch
时间: 2025-12-04
链接: https://x.com/rauchg/status/1996701779694874717
互动: Likes: 61; Retweets: 1; Replies: 5; Quotes: 0; Views: 13,971; Bookmarks: 2; isReply: 1

If you’re on Vercel, the WAF is on automatically. No action needed other than upgrading your deps and re-deploying.

如果您正在使用 Vercel，Web 应用程序防火墙（WAF）会自动启用。您只需要升级项目依赖（dependencies）并重新部署即可，无需进行其他操作。

### 1171

作者: @Guillermo-Rauch
时间: 2025-12-05
链接: https://x.com/rauchg/status/1996743917346476528
互动: Likes: 28; Retweets: 0; Replies: 4; Quotes: 0; Views: 5,714; Bookmarks: 4; isReply: 1

As an additional datapoint, with my own knowledge of what the working POC was, it was v difficult to nudge an agent to the successful exploit.

Exercise left to the readers: with the exploit at hand and giving the React Flight source code to the agent as context, what’s the minimum set of prompts and hints that yields the POC?

It’s a really good “eval” until the exploit and its documented explanations make into the next training rounds.

此外，根据我对那个能跑通的概念验证（POC）的了解，想要引导一个 AI 智能体成功复现该漏洞利用过程是极其困难的。

留给读者一个练习：假设你手头已有漏洞利用方法（exploit），并将 React Flight 的源代码作为上下文提供给 AI 智能体，那么最少需要多少提示（和暗示）才能让它生成出那个概念验证（POC）？

在这个漏洞利用方法及其详细的原理说明被收录进下一轮训练数据之前，这确实是一个绝佳的「评测」题目。

### 1172

作者: @Guillermo-Rauch
时间: 2025-12-05
链接: https://x.com/rauchg/status/1996748557173624956
互动: Likes: 149; Retweets: 0; Replies: 3; Quotes: 4; Views: 458,060; Bookmarks: 17; isReply: 1

@infosec_au @assetnote DM’d you. You have a working repro for bypassing Cloudflare but not Vercel. Would love to correct the record or see the evidence.

@infosec_au @assetnote 已私信。你们手上有一个能绕过 Cloudflare 但绕不过 Vercel 的有效复现（repro）。我很乐意据此澄清事实，或者查看一下相关证据。

### 1173

作者: @Guillermo-Rauch
时间: 2025-12-05
链接: https://x.com/rauchg/status/1996775364475953472
互动: Likes: 0; Retweets: 0; Replies: 1; Quotes: 0; Views: 501; Bookmarks: 0; isReply: 1

@mattheweegan Our WAF and CDN are our own unique products

@mattheweegan 我们的 WAF（Web 应用防火墙）和 CDN（内容分发网络）均为我们自研的独特产品。

### 1174

作者: @Guillermo-Rauch
时间: 2025-12-05
链接: https://x.com/rauchg/status/1996831724400242851
互动: Likes: 6; Retweets: 0; Replies: 0; Quotes: 0; Views: 2,034; Bookmarks: 0; isReply: 1

@Atinux Facts

@Atinux Facts

### 1175

作者: @Guillermo-Rauch
时间: 2025-12-05
链接: https://x.com/rauchg/status/1996835232524484717
互动: Likes: 5; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,070; Bookmarks: 0; isReply: 1

@_himanshugogoi @vercel 🫶 more to come!

@_himanshugogoi @vercel 🫶 还有更多惊喜等着呢！

### 1176

作者: @Guillermo-Rauch
时间: 2025-12-05
链接: https://x.com/rauchg/status/1996989385221284127
互动: Likes: 3; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,335; Bookmarks: 0; isReply: 1

@HiSohan It does?

@HiSohan 真的吗？

### 1177

作者: @Guillermo-Rauch
时间: 2025-12-05
链接: https://x.com/rauchg/status/1996990943669444918
互动: Likes: 2; Retweets: 0; Replies: 1; Quotes: 0; Views: 352; Bookmarks: 0; isReply: 1

@HiSohan 🤔 send them to me. Would like to debug or see if there’s another upgrade vector at play

@HiSohan 🤔 发给我看看。想调试一下，或者看看是不是还有别的升级途径（upgrade vector）在起作用。

### 1178

作者: @Guillermo-Rauch
时间: 2025-12-05
链接: https://x.com/rauchg/status/1996999574104473880
互动: Likes: 54; Retweets: 0; Replies: 2; Quotes: 0; Views: 23,046; Bookmarks: 0; isReply: 1

@dus0l @infosec_au @assetnote I’m happy to work with everyone and we  have a bounty program in place. But want make sure customers &amp; community don’t get wrong facts

@dus0l @infosec_au @assetnote 我很乐意与各位合作，并且我们已经设立了漏洞悬赏计划。但同时也希望确保我们的客户和社区不会被不实信息所误导。

### 1179

作者: @Guillermo-Rauch
时间: 2025-12-05
链接: https://x.com/rauchg/status/1997002425526255702
互动: Likes: 45; Retweets: 0; Replies: 4; Quotes: 3; Views: 24,894; Bookmarks: 2; isReply: 1

@NewsGoatX @infosec_au @assetnote There’s no body, no date, no request id. Would love to verify and attribute if real. responsible.disclosure@vercel.com

@NewsGoatX @infosec_au @assetnote 这条信息没有正文、没有日期、也没有请求 ID。如果情况属实，我们很乐意进行验证并确认其来源。请联系：responsible.disclosure@vercel.com

### 1180

作者: @Guillermo-Rauch
时间: 2025-12-05
链接: https://x.com/rauchg/status/1997008706223923435
互动: Likes: 45; Retweets: 0; Replies: 3; Quotes: 0; Views: 4,700; Bookmarks: 1; isReply: 1

@hungv47 @vercel 🫶 shoutout to our magnificent support team! They confirmed it was definitely an outlier situation and will not reoccur

@hungv47 @vercel 🫶 特别感谢我们出色的支持团队！他们已确认这确实是一个特例，并且今后不会再发生。

### 1181

作者: @Guillermo-Rauch
时间: 2025-12-05
链接: https://x.com/rauchg/status/1997011680388436449
互动: Likes: 716; Retweets: 32; Replies: 50; Quotes: 8; Views: 182,312; Bookmarks: 403; isReply: 0

All software will be generated. Platforms will enable this. 

A lot of value will shift from single-usecase SaaS → AI platforms.

We’re making it as easy to deploy a multi-tenant, multi-domain platform to @vercel, as it is to deploy a single app.

未来的所有软件都将由 AI 生成。而各类平台将是实现这一愿景的关键。

巨大的市场价值将从功能单一的 SaaS（软件即服务）产品，向 AI 平台转移。

我们的目标是大幅降低部署门槛：现在，向 @vercel 部署一个支持多租户、多域名的平台，已经变得和部署一个单一应用同样简单。

### 1182

作者: @Guillermo-Rauch
时间: 2025-12-05
链接: https://x.com/rauchg/status/1997013709558878635
互动: Likes: 140; Retweets: 5; Replies: 7; Quotes: 1; Views: 25,412; Bookmarks: 104; isReply: 1

We’re also introducing the “@shadcn for platforms”. 

Reusable and modifiable UI (e.g.: for setting up custom domains and displaying DNS config). Plus an ergonomic SDK to add projects or domains with one API call.

Platform Elements:
https://t.co/6xNcpVHoMW

我们同时推出「面向平台的 @shadcn」功能。

它提供了可复用且可灵活修改的用户界面组件（例如：用于配置自定义域名和展示 DNS 信息）。此外，还包含一个开发者友好（Ergonomic）的 SDK，仅需一次 API 调用即可轻松添加项目或域名。

平台组件详情：
https://t.co/6xNcpVHoMW

### 1183

作者: @Guillermo-Rauch
时间: 2025-12-05
链接: https://x.com/rauchg/status/1997023697698541629
互动: Likes: 19; Retweets: 0; Replies: 2; Quotes: 0; Views: 4,709; Bookmarks: 0; isReply: 1

@colinhacks Why isn’t it configurable via tsconfig.json path aliases? Why just #?

@colinhacks 为什么不能通过 tsconfig.json 里的路径别名来配置，而只支持 `#` 呢？

### 1184

作者: @Guillermo-Rauch
时间: 2025-12-05
链接: https://x.com/rauchg/status/1997086665987281035
互动: Likes: 8; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,593; Bookmarks: 0; isReply: 1

@ChrisUeland @infosec_au @SLCyberSec @hash_kitten @assetnote @vercel We have responsible disclosure channels and we didn’t hear from him. This is not a good way to collaborate on a serious issue that’s affecting so many.

@ChrisUeland @infosec_au @SLCyberSec @hash_kitten @assetnote @vercel 我们设有负责任的漏洞披露渠道，但并未收到他的任何联系。对于一个影响如此广泛的严重问题，这并非一个建设性的合作方式。

### 1185

作者: @Guillermo-Rauch
时间: 2025-12-05
链接: https://x.com/rauchg/status/1997092815952613456
互动: Likes: 7; Retweets: 0; Replies: 1; Quotes: 0; Views: 1,562; Bookmarks: 0; isReply: 1

@ChrisUeland @infosec_au @SLCyberSec @hash_kitten @assetnote @vercel Appreciate that. I didn't mean it to come across that way. I've been consistent that customers should not rely on WAF, but if there was a leak, it's best for us to know it and not to tweet about it.

@ChrisUeland @infosec_au @SLCyberSec @hash_kitten @assetnote @vercel 谢谢。我本意并非如此。我始终强调客户不应依赖 Web 应用防火墙（WAF），但如果发生了泄露，最好让我们知晓，而不是直接发推讨论。

### 1186

作者: @Guillermo-Rauch
时间: 2025-12-06
链接: https://x.com/rauchg/status/1997240238070993093
互动: Likes: 1; Retweets: 0; Replies: 1; Quotes: 0; Views: 595; Bookmarks: 0; isReply: 1

@properly1298731 @damengchen @Lorkydey We have Skew Protection on Vercel for those cases. That one smells like a chrome extension? Seeing console log would clarify

@properly1298731 @damengchen @Lorkydey 对于这类情况，我们在 Vercel 上提供了 Skew Protection（偏移保护）功能。这个问题感觉像是 Chrome 扩展引起的？查看一下控制台日志应该就能弄明白。

### 1187

作者: @Guillermo-Rauch
时间: 2025-12-06
链接: https://x.com/rauchg/status/1997245990865113404
互动: Likes: 3; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,712; Bookmarks: 0; isReply: 1

@AmanVirk1 Nice!

@AmanVirk1 很棒！

### 1188

作者: @Guillermo-Rauch
时间: 2025-12-06
链接: https://x.com/rauchg/status/1997264273270092043
互动: Likes: 20; Retweets: 0; Replies: 3; Quotes: 0; Views: 3,628; Bookmarks: 0; isReply: 1

@parzerp @vercel We’ll take a look. Thanks for the feedback

@parzerp @vercel 我们会尽快查看。感谢您的反馈。

### 1189

作者: @Guillermo-Rauch
时间: 2025-12-06
链接: https://x.com/rauchg/status/1997322707143188797
互动: Likes: 19; Retweets: 1; Replies: 0; Quotes: 0; Views: 3,585; Bookmarks: 0; isReply: 1

@lgrammel I love it for CLIs!

@lgrammel 我特别喜欢用它来写命令行工具！

### 1190

作者: @Guillermo-Rauch
时间: 2025-12-06
链接: https://x.com/rauchg/status/1997366429604065681
互动: Likes: 5; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,796; Bookmarks: 0; isReply: 1

@joelbqz Love it

@joelbqz 太赞了！

### 1191

作者: @Guillermo-Rauch
时间: 2025-12-06
链接: https://x.com/rauchg/status/1997372502817837393
互动: Likes: 6; Retweets: 0; Replies: 2; Quotes: 0; Views: 770; Bookmarks: 3; isReply: 1

@JohnPhamous @wwwjim @terragonlabs @julesagent Imagine a phone OS that’s just TUI

想象一下，一个完全基于文本用户界面（Text User Interface，TUI）的手机操作系统。

### 1192

作者: @Guillermo-Rauch
时间: 2025-12-06
链接: https://x.com/rauchg/status/1997400741430821122
互动: Likes: 6; Retweets: 0; Replies: 0; Quotes: 0; Views: 3,043; Bookmarks: 0; isReply: 1

@EstebanSuarez @v0 @bfl_ml @vercel It’s incredible at manipulating text

@EstebanSuarez @v0 @bfl_ml @vercel 它在文本处理 / 生成方面简直太强了。

### 1193

作者: @Guillermo-Rauch
时间: 2025-12-06
链接: https://x.com/rauchg/status/1997402643883237788
互动: Likes: 15; Retweets: 0; Replies: 1; Quotes: 0; Views: 12,791; Bookmarks: 1; isReply: 1

@zachrip_ It’s inconsequential. It doesn’t have to be used because at that point _formData.get() is called, which is hijacked by the constructor reference by the attacker. What’s important is that it gets appended, and could break the injection, unless you terminate it with //

@zachrip_ 这并不重要。它（指某个特定的值或操作）本身不一定需要被用到，因为此时会调用 `_formData.get（)` 方法，而该方法已被攻击者利用构造函数引用所劫持。关键之处在于，攻击载荷（payload）会被附加进去，这反而可能破坏注入攻击本身，除非你用 `//`（注释符）来终止它。

### 1194

作者: @Guillermo-Rauch
时间: 2025-12-06
链接: https://x.com/rauchg/status/1997415940863013163
互动: Likes: 25; Retweets: 0; Replies: 0; Quotes: 0; Views: 32,885; Bookmarks: 5; isReply: 1

@hd_nvim Because of the recursive then() which arguably is a form of runtime duck typing (duck resolving?)

@hd_nvim 因为存在递归的 then（）调用，这可以说是一种运行时鸭子类型（duck typing）（或者叫运行时鸭子解析？）的体现。

### 1195

作者: @Guillermo-Rauch
时间: 2025-12-06
链接: https://x.com/rauchg/status/1997416066444578993
互动: Likes: 73; Retweets: 1; Replies: 1; Quotes: 0; Views: 26,132; Bookmarks: 0; isReply: 1

@GrahamFleming The original was “meowmeow” 😆

@GrahamFleming 原话是「喵喵」啦 😆

### 1196

作者: @Guillermo-Rauch
时间: 2025-12-06
链接: https://x.com/rauchg/status/1997431664989876619
互动: Likes: 1; Retweets: 0; Replies: 1; Quotes: 0; Views: 253; Bookmarks: 0; isReply: 1

@_sy1vi3 @nickparrin One way to bypass the build check would be to vendor the dep. Or have a post install script that installs an older version inside the build container 😁 

Try  `"𝚙𝚘𝚜𝚝𝚒𝚗𝚜𝚝𝚊𝚕𝚕": "𝚙𝚗𝚙𝚖 𝚒 𝚗𝚎𝚡𝚝@{old version}"`. (Obviously be careful with the deployment!)

@_sy1vi3 @nickparrin 有个办法可以绕过构建检查，那就是把依赖项内联（vendor）到项目里。或者，在构建容器里设一个 `postinstall` 脚本来装个旧版本也行 😁

可以试试：`"postinstall"："pnpm i next@{old version}"`。（当然啦，部署的时候可得留神！）

### 1197

作者: @Guillermo-Rauch
时间: 2025-12-06
链接: https://x.com/rauchg/status/1997432423395553369
互动: Likes: 109; Retweets: 0; Replies: 4; Quotes: 0; Views: 14,135; Bookmarks: 11; isReply: 1

@yimingdothan We’re working hard to make updates seamless. Sorry about the nuisance

@yimingdothan 我们正在努力实现无缝更新。对此带来的麻烦，我们深表歉意。

### 1198

作者: @Guillermo-Rauch
时间: 2025-12-06
链接: https://x.com/rauchg/status/1997435666850808192
互动: Likes: 12; Retweets: 0; Replies: 1; Quotes: 0; Views: 4,634; Bookmarks: 1; isReply: 1

@calloc134 Pretty sure @ is the syntax that indicates the chunk needs to be then()d (and thus then()d again due to then: $1:then). Otherwise it’d be like a normal JSON (de)serialization of an inert object with the fields status etc

@calloc134 我相当确定，`@` 这个语法表示该代码块需要经过 `then（)` 处理（并且，由于 `then：$1:then` 这条规则，它实际上会被 `then（)` 处理两次）。否则，整个过程就会像是对一个包含 `status` 这类字段的普通静态对象进行常规的 JSON 序列化或反序列化一样简单。

### 1199

作者: @Guillermo-Rauch
时间: 2025-12-06
链接: https://x.com/rauchg/status/1997438686821077226
互动: Likes: 55; Retweets: 0; Replies: 2; Quotes: 0; Views: 8,206; Bookmarks: 5; isReply: 1

@valyala A lot of the complexity in software exists to work around hardware faults and limitations. 

Especially the dynamo example you’re referring to, the whole point of the DNS subsystem that failed was to manage load, capacity, hardware failures etc

@valyala 软件之所以如此复杂，很大程度上是为了应对硬件故障和各种局限性。

尤其是你提到的那个关于 Dynamo（亚马逊分布式存储系统）的例子，其中出问题的 DNS 子系统，其核心设计目标就是为了管理负载、分配容量、处理硬件故障等等。

### 1200

作者: @Guillermo-Rauch
时间: 2025-12-06
链接: https://x.com/rauchg/status/1997445935660404954
互动: Likes: 13; Retweets: 0; Replies: 1; Quotes: 0; Views: 824; Bookmarks: 0; isReply: 1

@deriegle @yimingdothan Yeah the auto patching system will get better and better. We’ll emerge stronger from this. Thank you for the feedback

@deriegle @yimingdothan 是的，自动修补系统会变得越来越好。我们会因此变得更强大。感谢反馈。

### 1201

作者: @Guillermo-Rauch
时间: 2025-12-07
链接: https://x.com/rauchg/status/1997460253479428566
互动: Likes: 1; Retweets: 0; Replies: 0; Quotes: 0; Views: 221; Bookmarks: 0; isReply: 1

@zer0nerd @parzerp @vercel Looking into this

@zer0nerd @parzerp @vercel 正在查看这个问题。

### 1202

作者: @Guillermo-Rauch
时间: 2025-12-07
链接: https://x.com/rauchg/status/1997608527595213080
互动: Likes: 90; Retweets: 0; Replies: 3; Quotes: 0; Views: 17,871; Bookmarks: 16; isReply: 1

@limouren I don’t think you’re understanding the exploit 😕 it has nothing to do with the existence of resolved_model, but the overriding of then and the JS runtime calling it recursively, hijacking the Chunk. And that’s only the first stage.

@limouren 我觉得你可能没理解这个漏洞利用的原理 😕 它和 resolved_model 是否存在没有关系，关键在于覆盖了 Promise 的 `then` 方法，并利用 JavaScript 运行时递归调用这个被覆盖的方法，从而劫持了 Chunk 对象。这还只是第一阶段。

### 1203

作者: @Guillermo-Rauch
时间: 2025-12-07
链接: https://x.com/rauchg/status/1997611770362658832
互动: Likes: 5; Retweets: 0; Replies: 0; Quotes: 0; Views: 2,110; Bookmarks: 0; isReply: 1

@zeldapoem I loved it

@zeldapoem 太棒了！

### 1204

作者: @Guillermo-Rauch
时间: 2025-12-07
链接: https://x.com/rauchg/status/1997620265556353314
互动: Likes: 3; Retweets: 1; Replies: 2; Quotes: 0; Views: 924; Bookmarks: 0; isReply: 1

@limouren Understood. Wanted to clarify bc it’s a really tricky exploit, even if React made a painful omission of safety checks for what properties to accept references for

@limouren 明白了。之所以想澄清一下，是因为这个漏洞利用（exploit）手法非常棘手，即便 React 在应该对哪些属性接受引用（ref）这一问题上，犯了一个严重的疏忽，遗漏了安全检查。

### 1205

作者: @Guillermo-Rauch
时间: 2025-12-07
链接: https://x.com/rauchg/status/1997659323846025418
互动: Likes: 6; Retweets: 0; Replies: 2; Quotes: 0; Views: 13,761; Bookmarks: 0; isReply: 1

@simonfarshid Ot should be in theory possible! @tomlienard 

Obviously ecosystem compat is another question

@simonfarshid 它（It）理论上应该是可行的！@tomlienard

当然了，生态系统的兼容性（ecosystem compatibility）就是另一回事了。

### 1206

作者: @Guillermo-Rauch
时间: 2025-12-07
链接: https://x.com/rauchg/status/1997683445162733975
互动: Likes: 7; Retweets: 0; Replies: 2; Quotes: 0; Views: 2,092; Bookmarks: 0; isReply: 1

@joulsounet Lots of lessons learned from this. Firewall has gotten stronger and will be industry-leading. Flight protocol will be thoroughly reviewed and is being audited by the world’s best. Patching velocity and automations for customers will improve. Sorry about this.

@joulsounet 从这次事件中我们吸取了很多教训。防火墙已经得到加强，将达到行业领先水平。运行协议（Flight protocol）将接受全面审查，目前正由全球顶尖的审计团队进行核查。面向客户的补丁发布速度和自动化流程也将得到提升。对于此次事件，我们深表歉意。

### 1207

作者: @Guillermo-Rauch
时间: 2025-12-07
链接: https://x.com/rauchg/status/1997690207618130297
互动: Likes: 2; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,206; Bookmarks: 0; isReply: 1

@document_body The feature doesn’t rely on it. Read the post again please. It happens as a byproduct of the hijacking of the call to _formData.get() with the Function reference created via :constructor

该功能并不依赖于此。请重新阅读帖子。这种现象是在通过 `:constructor` 创建的 Function 引用劫持对 `_formData.get（)` 的调用过程中，附带产生的结果。

### 1208

作者: @Guillermo-Rauch
时间: 2025-12-08
链接: https://x.com/rauchg/status/1997875831872610556
互动: Likes: 2; Retweets: 1; Replies: 0; Quotes: 0; Views: 767; Bookmarks: 0; isReply: 1

@samesh_l Yes, excellent summary

对，总结得非常到位。

### 1209

作者: @Guillermo-Rauch
时间: 2025-12-08
链接: https://x.com/rauchg/status/1997913112968909136
互动: Likes: 5; Retweets: 0; Replies: 0; Quotes: 0; Views: 1,491; Bookmarks: 0; isReply: 1

@WoraWork Incredible

@WoraWork 太牛了！

### 1210

作者: @Guillermo-Rauch
时间: 2025-12-08
链接: https://x.com/rauchg/status/1997923969371115660
互动: Likes: 570; Retweets: 35; Replies: 38; Quotes: 7; Views: 46,542; Bookmarks: 81; isReply: 0

Vercel Firewall has blocked:
▪️ ~6MM exploit attempts (all-time)
▪️ 2.3MM in the last 24h
▪️ 18K unique attacking IPs
▪️ 500+ exploit scanners

Kudos to our CDN & Security teams working day & night to protect the internet from React2Shell attacks.

Our WAF continues to get stronger, in collaboration with security researchers worldwide. It protects against non-trivial bypasses, making it a remarkably capable first line of defense (and not just for these vulns, but existing & future rules.)

That said: please patch your applications!

Vercel 防火墙已成功拦截：
▪️ 总计约 600 万次漏洞利用尝试
▪️ 过去 24 小时内达 230 万次
▪️ 18,000 个独立攻击 IP
▪️ 500 多个漏洞扫描器在此，我们要衷心感谢 CDN 与安全团队的日夜奋战，保护互联网免受 React2Shell 这类攻击。

我们的 Web 应用防火墙（WAF）在全球安全研究人员的通力协作下正日益强大。它能够有效防御复杂的绕过攻击，已然成为一道能力出众的第一防线（其防护范围不仅限于此次提及的漏洞，还涵盖了现有及未来的安全规则）。

但最重要的是：请务必及时修补您的应用程序！

### 1211

作者: @Guillermo-Rauch
时间: 2025-12-08
链接: https://x.com/rauchg/status/1998042503107538980
互动: Likes: 0; Retweets: 0; Replies: 0; Quotes: 0; Views: 48; Bookmarks: 0; isReply: 1

@marcdev501 When in doubt, upgrade

拿不准，就升级。
