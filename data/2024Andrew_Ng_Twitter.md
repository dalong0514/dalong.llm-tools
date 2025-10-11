# Andrej Karpathy Twitter 2024

本文件包含Andrej Karpathy在2024年的所有推文。

总计推文数量: 162


### 001

作者: @AndrewYNg
时间: 2024-01-01
链接: https://x.com/AndrewYNg/status/1741890108713009631
互动: Likes: 1,272; Retweets: 65; Replies: 91; Quotes: 2; Views: 129,802; Bookmarks: 14; isReply: 0

Happy New Year! I hope you have a 2024 filled with love, growth and adventure.

新年快乐！愿你的 2024 年充满爱、成长和冒险。

### 002

作者: @AndrewYNg
时间: 2024-01-01
链接: https://x.com/AndrewYNg/status/1741892184977309823
互动: Likes: 358; Retweets: 96; Replies: 66; Quotes: 5; Views: 111,921; Bookmarks: 148; isReply: 0

What does 2024 hold for AI? ​​In the latest edition of The Batch, @agermanidis @sarahookr @percyliang @SashaMTL @tamati_biskit and @kevin_scott outline their hopes for AI for this year ahead. 

Their wide ranging articles explore new AI tools for storytelling, inclusion, AI transparency, respecting human creativity, getting smaller models to work, and planning for continued exponential growth. 

You can read more below: https://t.co/r1gc0aV71t

2024 年 AI 将迎来什么？在最新一期的 The Batch 中，@agermanidis、@sarahookr、@percyliang、@SashaMTL、@tamati_biskit 和 @kevin_scott 分享了他们对未来一年 AI 发展的期盼。

他们的多篇文章深入探讨了 AI 在多个领域的新应用和前景，包括如何利用 AI 工具进行故事创作、促进包容性、提升 AI 透明度、尊重人类创造力、让小型模型发挥更大作用，以及如何规划 AI 持续的指数级增长。

你可以在下方阅读更多：https://t.co/r1gc0aV71t

### 003

作者: @AndrewYNg
时间: 2024-01-04
链接: https://x.com/AndrewYNg/status/1742943594242249023
互动: Likes: 1,467; Retweets: 258; Replies: 77; Quotes: 22; Views: 190,628; Bookmarks: 987; isReply: 0

New short course on advanced retrieval for RAG (retrieval augmented generation)! 

RAG fetches relevant documents to give context to an LLM. In Advanced Retrieval for AI with Chroma, taught by @trychroma founder @atroyn, you’ll learn:
(i) Query expansion using an LLM to rewrite and improve a query, by either generating either additional relevant queries or a hypothetical answer to the query.
(ii) Reranking using a cross-encoder - a model trained to measure similarity between two inputs presented simultaneously. Reranking reorders retrieved documents based on the cross-encoder similarity measure. 
(iii) Constructing and training an Embedding Adaptor, which is a model that adapts the embedding values to be more relevant to your use case.

Each of these techniques can help you build much better RAG systems. Please sign up for the course here: https://t.co/6N1H8agcYC

RAG（检索增强生成）高级检索新短课程开讲啦！

RAG 的作用是获取相关文档，从而为大语言模型（LLM）提供更丰富的上下文信息。在由 @trychroma 创始人 @atroyn 亲授的「Chroma AI 高级检索」课程中，您将学到：
(i）查询扩展：利用大语言模型重写并优化原始查询，方法包括生成额外的相关查询，或者直接提供一个假设性的答案来帮助模型理解。
(ii）重排序：通过交叉编码器（cross-encoder）进行。交叉编码器是一种经过专门训练的模型，能够同时评估并测量两个输入之间的相似度。它会根据这种相似度来重新排列检索到的文档，确保最相关的排在前面。
(iii）构建和训练嵌入适配器（Embedding Adaptor）：这是一种模型，旨在调整嵌入值，使其更好地适应您的特定应用场景和用例。

掌握这些技术，您就能构建出远超以往的 RAG 系统。请点击此链接报名课程：https://t.co/6N1H8agcYC

### 004

作者: @AndrewYNg
时间: 2024-01-07
链接: https://x.com/AndrewYNg/status/1744145064115446040
互动: Likes: 3,448; Retweets: 550; Replies: 299; Quotes: 101; Views: 945,113; Bookmarks: 842; isReply: 0

After reading the @nytimes lawsuit against @OpenAI and @Microsoft, I find my sympathies more with OpenAI and Microsoft than with the NYT. 

The suit:
(1) Claims, among other things, that OpenAI and Microsoft used millions of copyrighted NYT articles to train their models
(2) Gives examples in which OpenAI models regurgitated NYT articles almost verbatim

But the presentation muddies (1) and (2), and I saw a lot of commentary on social media that -- because of what I believe is a muddied presentation -- draws a link between them that I'm not sure is what people think it is.

On (1): I understand why media companies don't like people training on their documents, but believe that just as humans are allowed to read documents on the open internet, learn from them, and synthesize brand new ideas, AI should be allowed to do so too. I would like to see training on the public internet covered under fair use -- society will be better off this way -- though whether it actually is will ultimately be up to legislators and the courts. 

On (2): I suspect a lot of the examples of ChatGPT regurgitating articles nearly verbatim were due to a RAG-like mechanism where the user prompt causes the system to browse the web, retrieve a specific article and then print it out. (If my statement here isn't accurate, I would love to see the @nytimes clarify this.) If this is the case, then (i) To OpenAI's credit, they seem to have already updated their software to make this much less likely, and (ii) This is also a much easier problem to fix than if an LLM were to regurgitate text using only the pre-trained weights, which AFAIK very rarely happens (and which, given its rarity, also raises the question of how much harm to NYT this has actually caused). 

To be clear, I believe independent media is important for democracy and must be protected. I also sympathize with media businesses worried about Generative AI disrupting their businesses. But I'm not convinced the NYT lawsuit is the right way to do this. 

Usual caveat: I am not a lawyer and am not giving legal advice or any other form of advice here. 

You can also read more details of my take on this below. https://t.co/wkZSMHsvNA

在阅读了 《纽约时报》（NYT）对 OpenAI 和 Microsoft 的诉讼之后，我发现自己对 OpenAI 和 Microsoft 的同情多于对 NYT 的同情。

诉讼指出：
(1）OpenAI 和 Microsoft 被指控使用了数百万篇受版权保护的 NYT 文章来训练他们的大语言模型（LLM），这只是众多主张之一。
(2）诉讼也列举了 OpenAI 的模型几乎逐字逐句地重复了 NYT 文章的例子。

然而，这种陈述方式却将上述（1）和（2）两点混淆了。我在社交媒体上看到许多评论，由于这种在我看来有些模糊的呈现方式，这些评论将两者关联起来，但这种关联是否就是人们所认为的那样，我并不确定。

关于第一点：我理解媒体公司不乐意人们使用他们的内容进行模型训练。但我认为，就像人类被允许在开放的互联网上阅读资料、从中学习并创造出全新的想法一样，AI 也应该被允许这样做。我希望将基于公共互联网内容的训练纳入「合理使用」(fair use）范畴 —— 这会使社会受益匪浅 —— 尽管最终这是否能实现，仍将取决于立法者和法院的裁决。

关于第二点：我猜测许多 ChatGPT 几乎逐字逐句地重复文章的例子，是由于一种类似于检索增强生成（RAG）的机制。在这种机制下，用户的提示会导致系统浏览网页，检索特定的文章，然后将其输出。（如果我这里的说法不准确，我希望 《纽约时报》 能对此进行澄清。）如果情况确实如此，那么：(i）值得称赞的是，OpenAI 似乎已经更新了他们的软件，大大降低了这种情况发生的可能性；(ii）这个问题也比大语言模型（LLM）仅使用预训练权重来重复文本更容易解决。据我所知，后者的情况非常罕见（考虑到其罕见性，这也引发了一个问题：这实际上对 NYT 造成了多大的损害？）。

需要明确的是，我认为独立媒体对民主至关重要，必须受到保护。我也同情那些担心生成式 AI（Generative AI）业务发展会冲击其营收的媒体公司。但我不相信 NYT 的诉讼是解决这个问题的正确方法。

惯例声明：我并非律师，在此不提供任何法律建议或其他形式的建议。

您也可以点击下方链接，阅读我对此事的更多详细看法。https://t.co/wkZSMHsvNA

### 005

作者: @AndrewYNg
时间: 2024-01-08
链接: https://x.com/AndrewYNg/status/1744433663969022090
互动: Likes: 667; Retweets: 114; Replies: 112; Quotes: 17; Views: 265,186; Bookmarks: 186; isReply: 0

I said some things poorly in my previous tweet, so let me elaborate/clarify.

1. I don't think it's okay for any company to regurgitate others' copyrighted content at scale without permission or a viable fair-use rationale. I should have said this more explicitly.

And... I still think the link between training an LLM on someone's content to having the LLM regurgitate that content to users at scale is weaker than many would have thought from looking at the NYT lawsuit. It is possible that an LLM will regurgitate text using only the pre-trained weights (no RAG), but I believe only in very rare, corner cases, in response to particular prompts (that in practice are hardly ever used by normal users).

2. When I try to replicate the "worst" looking examples of copyright violations in the lawsuit -- such as a user trying to use ChatGPT to get around a paywall, or get Wirecutter (an NYT property) results -- I end up triggering GPT-4's web browsing capability. (See two examples in attached screenshots.) That's why I said I suspect RAG was involved in the examples used in the NYT lawsuit.

Specifically, one of the cool features of GPT-4 is that it can browse the web to download additional information to generate its response. For example, one can prompt it to do a web search, or sometimes even to download a specific article. While it's not great that GPT-4 apparently used to be willing to download and display an article (nearly) verbatim, to OpenAI's credit, this loophole appears to have been closed.

I believe the prominence given to these examples in the lawsuit made people think that it was training an LLM on NYT text that led directly to some of these examples of NYT text being regurgitated. But if RAG was involved, then the root cause of these examples of regurgitation is not that the LLM was trained on NYT text -- that's why I said I found the presentation of issues in the lawsuit muddied.

3. It is also true that the NYT shows that you can get GPT-4 to regurgitate NYT text, by prompting it in a particular way. (I should have said this in my last tweet as well.) The prompts used seem to typically involve giving a large chunk of an article, and then getting the LLM to complete it.

While it's not great that an LLM does this, I am skeptical that practically anyone uses an LLM this way.  That’s why I said that given the rarity of such generations resulting in text regurgitation, I question how much harm to NYT this has actually caused. I'm also not sure if this works only on articles that have been syndicated and are all over the internet anyway (so that the article appears numerous times in the LLM training set). Further, it looks like the newer versions of ChatGPT have closed this loophole. 

@TonyW also makes this point well: https://t.co/KKYir0eFVV

Thanks for reading!

我之前的一些表述有欠妥之处，所以在此进行详细阐述和澄清。

1. 我认为任何公司在未经许可或缺乏合理使用理由的情况下，大规模复述他人的版权内容都是不妥的。这一点我本应更明确地指出。

此外…… 我仍然认为，将大语言模型（LLM）利用他人的内容进行训练，与让大语言模型将这些内容大规模复述给用户之间，其联系的紧密程度可能比许多人在看过《纽约时报》诉讼后所想象的要弱。大语言模型确实有可能仅使用预训练权重（不依赖检索增强生成，即 RAG）来复述文本，但我相信这仅发生在极少数边缘案例中，并且是对特定提示的响应（而这些提示在实践中几乎不会被普通用户使用）。

2. 当我尝试复现诉讼中那些看似「最糟糕」的版权侵权示例时 —— 例如用户试图使用 ChatGPT 绕过付费墙，或获取 Wirecutter（《纽约时报》旗下的媒体）的内容 —— 我最终都会调用 GPT-4 的网页浏览功能。（请参见附图中两个示例。）这就是为什么我怀疑《纽约时报》诉讼中提到的示例涉及了 RAG。

具体来说，GPT-4 的一个出色功能是它能够浏览网页以下载额外信息来生成响应。例如，用户可以提示它进行网络搜索，甚至有时直接下载某篇文章。虽然 GPT-4 以前显然愿意下载并（几乎）逐字显示文章这一行为并不理想，但值得称赞的是，OpenAI 似乎已经修补了这一漏洞。

我相信，这些例子在诉讼中被着重强调，使得人们误以为是由于用《纽约时报》的文本训练大语言模型才直接导致了这些《纽约时报》文本被复述的例子。但如果其中涉及了 RAG，那么这些复述的根本原因就不在于大语言模型是用《纽约时报》的文本训练的 —— 这就是为什么我说我发现诉讼中问题的呈现方式模糊了焦点。

3. 同样，事实是《纽约时报》展示了，通过以特定方式提示 GPT-4，确实可以使其复述《纽约时报》的文本。（我上次的推文中也应该提及这一点。）所使用的提示通常似乎涉及提供文章的很大一部分内容，然后让大语言模型完成剩余部分。

尽管大语言模型存在这种复述能力并非好事，但我对此持怀疑态度，因为在实际应用中几乎没有人会以这种方式使用大语言模型。这就是为什么我说，考虑到这种生成方式导致文本复述的罕见性，我质疑这实际上对《纽约时报》造成了多大的损害。我也不确定这是否仅适用于那些已被广泛联合发布并遍布互联网的文章（以至于该文章在大语言模型训练集中出现了无数次）。此外，看起来更新版本的 ChatGPT 已经解决了这一问题。

@TonyW 也很好地阐述了这一观点： https://t.co/KKYir0eFVV

感谢阅读！

### 006

作者: @AndrewYNg
时间: 2024-01-10
链接: https://x.com/AndrewYNg/status/1745127613742657887
互动: Likes: 1,709; Retweets: 332; Replies: 78; Quotes: 40; Views: 283,672; Bookmarks: 1,126; isReply: 0

Our first Generative AI short course in JavaScript!

GitHub recently reported that JavaScript is again the world’s most popular programming language. To support web developers exploring and developing with generative AI, we just launched a new short course in JavaScript taught by @Hacubu, founding engineer at @LangChainAI. In ​​Build LLM Apps with LangChain.js you’ll learn elements common in AI development, including:

(i) Using data loaders to pull data from common sources such as PDFs, websites, and databases
(ii) Prompts, which are used to provide the LLM context
(iii) Modules to support RAG such as text splitters and integrations with vector stores
(iv) Working with different models to write applications that are not vendor-specific
(v) Parsers, which extract and format the output for your downstream code to process

You’ll also build with the LangChain Expression Language, which lets you easily compose  sequences (also called chains) of modules to perform complex tasks using LLMs. 

Putting all this together, you’ll also work on a conversational question-answering LLM application capable of using external data as context.

Please sign up here: https://t.co/oVoFPKRBbW

我们的首个 JavaScript 生成式 AI（Generative AI）短期课程！

GitHub 最近报告称，JavaScript 再次成为全球最受欢迎的编程语言。为了支持网页开发者探索和使用生成式 AI 进行开发，我们刚刚推出了一门全新的 JavaScript 短期课程。这门课程由 @Hacubu 讲授，他是 @LangChainAI 的创始工程师。在名为「构建 LangChain.js 大语言模型（LLM）应用」的课程中，您将学习 AI 开发中常见的核心要素，包括：

(i）使用数据加载器从 PDF、网站和数据库等常见来源提取数据
(ii）提示词（Prompts），它们用来为大语言模型提供上下文信息
(iii）支持检索增强生成（RAG）的模块，例如文本分割器（text splitters）以及与向量存储（vector stores）的集成
(iv）使用不同的模型来编写不局限于特定供应商的应用程序
(v）解析器（Parsers），它们负责提取并格式化输出，以便您的后续代码进行处理您还将学习并使用 LangChain 表达式语言（LangChain Expression Language）来构建应用。这种语言能让您轻松地将一系列模块（也称为「链」(chains)）组合起来，从而利用大语言模型完成复杂的任务。

总而言之，您还将亲手开发一个对话式问答的大语言模型应用程序，它能够利用外部数据作为上下文进行交互。

请点击此处注册：https://t.co/oVoFPKRBbW

### 007

作者: @AndrewYNg
时间: 2024-01-11
链接: https://x.com/AndrewYNg/status/1745516258697863259
互动: Likes: 5,099; Retweets: 764; Replies: 90; Quotes: 78; Views: 694,998; Bookmarks: 3,694; isReply: 0

It is only rarely that, after reading a research paper, I feel like giving the authors a standing ovation. But I felt that way after finishing Direct Preference Optimization (DPO) by @rm_rafailov @archit_sharma97 @ericmitchellai @StefanoErmon @chrmanning and @chelseabfinn. This beautiful paper proposes a much simpler alternative to RLHF (reinforcement learning from human feedback) for aligning language models to human preferences. 

RLHF has been a key technique for training LLMs. In brief, RLHF (i) Gets humans to specify their preferences by ranking LLM outputs, (ii) Trains a reward model (used to score LLM outputs) -- typically represented using a transformer network -- to be consistent with the human rankings, (iii) Uses reinforcement learning to tune an LLM, also represented as a transformer, to maximize rewards. This requires two transformer networks, and RLHF is also finicky to the choice of hyperparameters.

DPO simplifies the whole thing. Via clever mathematical insight, the authors show that given an LLM, there is a specific reward function for which that LLM is optimal. DPO then trains the LLM directly to make the reward function (that’s now implicitly defined by the LLM) consistent with the human rankings. So you no longer need to deal with a separately represented reward function, and you can train the LLM directly to optimize the same objective as RLHF. 

Although it’s still too early to be sure, I am cautiously optimistic that DPO will have a huge impact on LLMs and beyond in the next few years.

You can read the paper here: https://t.co/m14qRYszVa I also write more about this in The Batch (linked to below).  
https://t.co/8h2ag2plIa

我很少在读完一篇研究论文后，会感到想给作者们起立鼓掌。但在读完 Rafailov、Sharma、Mitchell、Ermon、Manning 和 Finn 几位合著的《直接偏好优化》（Direct Preference Optimization，DPO）后，我确实有这种感觉。这篇精彩的论文提出了一种比 RLHF（reinforcement learning from human feedback）简单得多的替代方案，用于让语言模型更好地符合人类偏好。

RLHF 一直是训练大语言模型（LLM）的关键技术。简而言之，RLHF 的流程包括：（i）让人类通过对 LLM 输出进行排序来表达他们的偏好；（ii）训练一个奖励模型（通常使用 Transformer 网络来表示，用于对 LLM 输出进行评分），使其与人类的偏好排序保持一致；（iii）使用强化学习来调整 LLM（同样也是一个 Transformer），以最大化这个奖励。这需要两个 Transformer 网络，而且 RLHF 对超参数（hyperparameters）的选择也非常敏感，调优起来比较棘手。

DPO 简化了整个过程。通过巧妙的数学洞察，作者们发现，对于任何一个给定的 LLM，都存在一个特定的奖励函数，而这个 LLM 对该奖励函数来说是「最优」的。DPO 随后直接训练 LLM，使由 LLM 隐式定义的奖励函数与人类的偏好排序保持一致。这样一来，你就不再需要单独设计或显式表示一个奖励函数，并且可以直接训练 LLM 来优化与 RLHF 相同的目标。

尽管现在下结论还为时过早，但我谨慎乐观地认为 DPO 将在未来几年对 LLM 以及更广泛的领域产生巨大影响。

你可以在这里阅读这篇论文：https://t.co/m14qRYszVa 我还在 The Batch（链接如下）中对此写了更多内容。
https://t.co/8h2ag2plIa

### 008

作者: @AndrewYNg
时间: 2024-01-18
链接: https://x.com/AndrewYNg/status/1748005715237654528
互动: Likes: 1,461; Retweets: 281; Replies: 78; Quotes: 25; Views: 221,278; Bookmarks: 1,014; isReply: 0

New short course on LLMOps!

LLMOps (large language model operations) is a rapidly developing field that takes ideas from MLOps (machine learning operations) and specializes them to building and deploying LLM-based applications. In this course, taught by @googlecloud's Erwin Huizenga, you'll learn to use automation to make building, tuning and deploying an LLM-based application less manual and more efficient. 

You'll learn how to:
- Apply supervised fine-tuning to tune an LLM to a specific task
- Automate and orchestrate LLM-tuning and deployment by customizing a pre-built tuning pipeline
- Apply best practices for preparing training data for supervised fine-tuning of an LLM
- Create an LLMOps workflow you can adapt to other LLM-tuning jobs

This course doesn't assume any prior MLOps or LLMOps experience. Sign up here to learn about this emerging field! https://t.co/UlDEbI0DbK

关于 LLMOps 的全新短期课程来了！

LLMOps（大语言模型运营）是一个迅速发展的领域，它借鉴了 MLOps（机器学习运营）的理念，并将其专门应用于构建和部署基于大语言模型的应用程序。在这门由 Google Cloud 的 Erwin Huizenga 主讲的课程中，你将学习如何运用自动化，让大语言模型应用的构建、调优和部署过程减少人工干预，变得更加高效。

你将掌握以下技能：
- 运用监督微调（supervised fine-tuning）技术，将大语言模型针对特定任务进行优化。
- 通过定制预设的调优流程，自动化和编排大语言模型的调优与部署。
- 掌握为大语言模型进行监督微调准备训练数据的最佳实践。
- 创建一个可应用于其他大语言模型调优任务的 LLMOps 工作流。

本课程不要求你具备任何 MLOps 或 LLMOps 经验。点击此处报名，探索这个新兴领域吧！https://t.co/UlDEbI0DbK

### 009

作者: @AndrewYNg
时间: 2024-01-24
链接: https://x.com/AndrewYNg/status/1750200384600309872
互动: Likes: 789; Retweets: 148; Replies: 67; Quotes: 9; Views: 100,885; Bookmarks: 356; isReply: 0

New short course on Automated Testing for LLMOps, by @CircleCI's CTO Rob Zuber! This teaches you how to adapt some key ideas from CI (continuous integration), which has been a pillar of efficient software engineering, to building LLM-based applications.

Tweaking an LLM-based app to improve it -- say by modifying a prompt -- can have unexpected side effects. For example, what if a teammate updates a prompt to try to make the LLM output sound more interesting, but this causes it to hallucinate more? Automated testing, as part of your approach to LLMOps (LLM Operations), helps avoid these problems and lets you ship faster and with greater confidence.

In this course, you’ll learn to:
(i) Write LLM evaluations to cover common problems like hallucinations, data drift, and harmful or offensive output.
(ii) Build a CI workflow to automatically evaluate each change to your application.
(iii) Orchestrate your CI workflow to run specific evaluations at different stages of development.

CI is especially important for AI applications given the iterative nature of AI development, which means we often want to make many incremental changes. 

Please sign up for this course here!  https://t.co/eTfzX2dPjD

@CircleCI 首席技术官（CTO）Rob Zuber 推出了一门关于大语言模型运维（LLMOps）自动化测试的全新短期课程！本课程将教你如何把持续集成（CI）中的一些关键理念应用到基于大语言模型（Large Language Model）的应用程序开发中。持续集成（CI）一直是高效软件工程的支柱。

调整一个基于大语言模型（LLM）的应用程序来改进它 —— 比如通过修改一个提示词（prompt）—— 可能会产生意想不到的副作用。举个例子，如果一位队友更新了提示词，试图让大语言模型（LLM）的输出听起来更有趣，但这却导致模型产生更多幻觉（hallucination），那该怎么办呢？自动化测试，作为你大语言模型运维（LLM Operations，LLMOps）策略的一部分，有助于避免这些问题，让你能更快、更有信心地交付应用。

在这门课程中，你将学习：
(i）编写大语言模型（LLM）评估，以应对幻觉、数据漂移（data drift）以及有害或冒犯性输出等常见问题。
(ii）构建持续集成（CI）工作流，对你应用程序的每一次更改进行自动评估。
(iii）协调你的持续集成（CI）工作流，以便在开发的不同阶段运行特定的评估。

鉴于人工智能（AI）开发的迭代性质，即我们通常需要进行许多增量更改，持续集成（CI）对于人工智能（AI）应用程序来说尤为重要。

请在此处报名参加本课程： https://t.co/eTfzX2dPjD

### 010

作者: @AndrewYNg
时间: 2024-01-26
链接: https://x.com/AndrewYNg/status/1750985019789873244
互动: Likes: 1,439; Retweets: 264; Replies: 105; Quotes: 32; Views: 723,896; Bookmarks: 451; isReply: 0

My takeaways from attending WEF at Davos last week:
- There were lots of discussions on business implementation of AI. My top two tips: (i) Pretty much all knowledge workers can benefit from using GenAI now, but most will need training. (ii) Task-based analysis of jobs is helping businesses identify opportunities. 
- Also lots of AI regulation conversations. I'm happy to report that the conversation is much more sensible than 6 months ago. For example, the unnecessary fears and discussion on AI extinction risk is fading away. But some big companies are still pushing for stifling, anti-competitive regulations, and the fight to protect open-source is still far from won. 
- Attending climate sessions made me even more worried about the lack of action to change our planet's trajectory. Rather than 1.5 degrees Celsius of warming as the optimistic case and 2 degrees as the pessimistic case, I think 2 degrees is an optimistic case, and 4 degrees a more realistic pessimistic case. Decarbonization remains critical; and unfortunately, that we're talking about 1.5-2 degrees rather than 2-4 degrees means we're underinvesting in resilience, adaptation, and potentially game-changing technologies like geo-engineering.

Longer writeup below in The Batch: https://t.co/ZkdsgeF6WU

我上周参加达沃斯世界经济论坛（WEF）的收获：
- 会上针对人工智能（AI）的商业化落地进行了大量讨论。我的两大建议是：（i）几乎所有知识工作者现在都能从生成式 AI（Generative AI）的使用中受益，但大多数人仍需要专业培训。(ii）基于任务的工作分析正帮助企业发现新的机遇。
- 关于 AI 监管的探讨也很多。我很高兴地告诉大家，目前的讨论比六个月前理性得多。例如，对 AI 灭绝风险那些不必要的担忧和争论正在逐渐消退。然而，一些大型企业仍在力推具有抑制作用、反竞争的监管政策，因此保护开源（Open-source）的努力远未成功。
- 参加气候议题会议让我对目前缺乏改变地球气候走向的行动感到更加担忧。我认为，将全球升温 1.5 摄氏度视为乐观情况、2 摄氏度视为悲观情况，这并不准确。实际上，2 摄氏度升温或许已是乐观预期，而 4 摄氏度升温可能才是更现实的悲观情景。脱碳依然至关重要；不幸的是，我们仍在讨论 1.5 到 2 摄氏度的升温，而非 2 到 4 摄氏度，这意味着我们在抵御气候变化的能力（韧性）、适应措施以及地球工程等可能改变局面的技术上投入不足。

更详细的内容可在《The Batch》中查看： https://t.co/ZkdsgeF6WU

### 011

作者: @AndrewYNg
时间: 2024-01-31
链接: https://x.com/AndrewYNg/status/1752763171042165183
互动: Likes: 1,150; Retweets: 206; Replies: 65; Quotes: 14; Views: 136,721; Bookmarks: 654; isReply: 0

New short course on Building Applications with Vector Databases, taught by @pinecone’s @timt! At the heart of a vector database is the ability to store a collection of vectors and then query against that, meaning input a new vector and find similar ones. This is useful for many AI applications. In this course, you'll learn how to use vector databases to build:

(i) Semantic Search: Create a text search tool that goes beyond keyword matching, and instead focuses on the meaning of content.
(ii) RAG (retrieval augmented generation): Enhance your LLM output by incorporating context from sources the model wasn't trained on.
(iii) Recommender System: Combine semantic search and RAG to recommend topics, and demonstrate it with a news article recommender.
(iv) Hybrid Search: Build an application that finds items using both images and descriptive text -- by combining both sparse and dense vector representations of the data -- using an eCommerce dataset as an example.
(v) Image Similarity: Use image vector embeddings to create an app to compare facial features, using a database of public figures to determine the likeness between them.
(vi) Anomaly Detection: Build an anomaly detection app that identifies unusual patterns in network communication logs.

I hope you’ll enjoy learning how to build all these types of applications! Please sign up here: https://t.co/nginq45FAf

由 @pinecone 公司的 @timt 讲授的「使用向量数据库构建应用程序」新短期课程开课啦！向量数据库（Vector Database）的核心功能是存储大量向量，并能通过输入一个新向量来查询和检索与之相似的向量。这在许多 AI 应用程序中都非常有用。在本课程中，您将学习如何使用向量数据库构建以下应用：

(i）语义搜索（Semantic Search)：创建一个文本搜索工具，它不仅限于关键词匹配，更侧重于内容的深层含义。
(ii）RAG（检索增强生成，retrieval augmented generation)：通过引入模型未曾训练过的外部上下文信息，来增强您的大语言模型（LLM）输出。
(iii）推荐系统（Recommender System)：结合语义搜索和 RAG 来推荐主题，并将通过一个新闻文章推荐器进行演示。
(iv）混合搜索（Hybrid Search)：构建一个应用程序，结合图像和描述性文本来查找商品，同时利用数据的稀疏和密集向量表示 —— 我们将以一个电子商务数据集为例。
(v）图像相似性（Image Similarity)：使用图像向量嵌入（Image Vector Embeddings）来创建一个应用程序，用于比较面部特征，通过一个公共人物数据库来判断不同人之间的相似程度。
(vi）异常检测（Anomaly Detection)：构建一个异常检测应用程序，用于识别网络通信日志中的异常模式。

希望您能享受学习如何构建这些多样化应用程序的过程！请在这里注册：https://t.co/nginq45FAf

### 012

作者: @AndrewYNg
时间: 2024-02-14
链接: https://x.com/AndrewYNg/status/1757821916843552842
互动: Likes: 900; Retweets: 181; Replies: 68; Quotes: 8; Views: 107,782; Bookmarks: 406; isReply: 0

New short course on Serverless LLM apps with Amazon Bedrock, taught by @AWS' @mikegchambers! A serverless architecture enables you to quickly deploy your applications without needing to set up and manage compute servers to run your applications on, the maintenance of which can be another full-time job. In this course, you’ll learn how to do this by using an event-driven architecture to build complex AI workflows.

Mike illustrate these concepts by building a cool application that automatically detects incoming customer inquiries, transcribes them with ASR (automatic speech recognition), summarizes them with an LLM using Bedrock, and deploys serverless with AWS Lambda.

I hope this course makes it much easier for you to build and deploy LLM applications requiring multi-step AI workflows.  Please sign up here: https://t.co/37hE71j3pT

@AWS 的 @mikegchambers 带来了一门关于使用 Amazon Bedrock 构建无服务器大语言模型（LLM）应用程序的新短期课程！无服务器架构（Serverless Architecture）能让您快速部署应用程序，而无需耗费精力去设置和管理运行这些应用的计算服务器，因为服务器的维护本身可能就是一份全职工作。在本课程中，您将学习如何通过事件驱动架构（Event-driven Architecture）来构建复杂的 AI 工作流（AI Workflows）。

Mike 将通过构建一个精彩的应用来演示这些概念：这个应用能够自动检测传入的客户咨询，利用 ASR（自动语音识别，Automatic Speech Recognition）技术将其转录，再通过 Bedrock 上的大语言模型（LLM）对其进行总结，最后使用 AWS Lambda 实现无服务器部署。

我希望这门课程能让您在构建和部署需要多步骤 AI 工作流的 LLM 应用程序时，变得更加轻松。请点击此处报名：https://t.co/37hE71j3pT

### 013

作者: @AndrewYNg
时间: 2024-02-14
链接: https://x.com/AndrewYNg/status/1757826615147704345
互动: Likes: 9; Retweets: 0; Replies: 0; Quotes: 0; Views: 7,199; Bookmarks: 2; isReply: 1

@fahadaziz It is our privilege at AI Fund to be working with you!

@fahadaziz 在 AI Fund，我们非常荣幸能与您合作！

### 014

作者: @AndrewYNg
时间: 2024-02-16
链接: https://x.com/AndrewYNg/status/1758633108654711008
互动: Likes: 393; Retweets: 40; Replies: 58; Quotes: 0; Views: 102,764; Bookmarks: 63; isReply: 0

Congratulations @hwchase17 and the whole @LangChainAI team! Love the work you're doing to make it easy for others to build LLM apps.

祝贺 @hwchase17 和整个 @LangChainAI 团队！非常喜欢你们的工作，让大家能更轻松地开发大语言模型（LLM）应用程序。

### 015

作者: @AndrewYNg
时间: 2024-02-19
链接: https://x.com/AndrewYNg/status/1759430085957111932
互动: Likes: 98; Retweets: 3; Replies: 5; Quotes: 1; Views: 33,479; Bookmarks: 6; isReply: 1

@roelofbotha @sequoia It's wonderful that @sequoia is putting this together to support Open Source to benefit everyone. Thank you @roelofbotha! 

Am also a huge fan of your first Open Source Fellow @tiangolo -- I was literally using his FastAPI framework today to deploy an app!

@roelofbotha @sequoia 很高兴 @sequoia 正在着手做这件事来支持开源，造福所有人。谢谢你 @roelofbotha！

我也是其首位开源研究员 @tiangolo 的忠实粉丝 —— 我今天恰好就在用他的 FastAPI 框架部署一个应用程序！

### 016

作者: @AndrewYNg
时间: 2024-02-26
链接: https://x.com/AndrewYNg/status/1761912346153521374
互动: Likes: 3,456; Retweets: 204; Replies: 267; Quotes: 70; Views: 445,641; Bookmarks: 172; isReply: 0

To all my Google friends: I know this week has been tough with a lot of criticism about Gemini's gaffes. 

Just wanted to say I love all of you and am rooting for you. I know everyone means well, and am grateful for your work &amp; eager to see where you next take this amazing tech!

致我所有的 Google 朋友们： 这一周过得不容易，我知道 Gemini 的一些失误引来了不少批评。

我只想说，我爱你们每一个人，并会为你们所有人加油打气！我深知大家都是出于好意，非常感谢你们所付出的努力和工作。我也无比期待，看到你们接下来会将这项惊人的技术带向何方！

### 017

作者: @AndrewYNg
时间: 2024-02-28
链接: https://x.com/AndrewYNg/status/1762879627633287477
互动: Likes: 1,287; Retweets: 260; Replies: 86; Quotes: 18; Views: 162,302; Bookmarks: 805; isReply: 0

New short course: Prompt Engineering with Llama 2, built in collaboration with Meta @AIatMeta, and taught by @asangani7! Meta's Llama 2 has been game-changing for AI. Building with open source lets you control your own data, scrutinize errors, update (or not) the models as you please, and work alongside the global community advancing open models.

Llama isn't a single model, it's a collection of models. In this course, you'll:
- Learn the differences between different Llama 2 flavors, and when to use each.
- Prompt the Llama chat models -- you'll also see how Llama's instruction tags work -- so they can help you with day-to-day tasks, like writing or summarization.
- Use advanced prompting, like few-shot prompting for classification, and chain-of-thought prompting for solving logic problems.
- Use specialized models in the Llama collection for specific tasks, like Code Llama to help you write, analyze, and improve code, and Llama Guard, which checks prompts and model responses for harmful content. 

The course also touches on how to run Llama 2 locally on your own computer.

I hope you’ll take this course and try out these powerful, open models!
https://t.co/kas7jmeCkj

新短课程：Llama 2 提示工程（Prompt Engineering），由 Meta @AIatMeta 合作开发，并由 @asangani7 亲自授课！Meta 的 Llama 2 对人工智能（AI）领域而言，无疑带来了革命性的改变。基于开源模型进行开发，你将能够更好地掌控自己的数据，仔细审查潜在错误，根据需要选择更新或不更新模型，并与全球社区一同推动开放模型的进步。

Llama 并非单一模型，而是一个由多种模型组成的系列。通过本课程，你将：
- 学习不同 Llama 2 变体之间的区别，并了解何时选择使用它们。
- 学会如何向 Llama 聊天模型进行提示（Prompt），你还会了解 Llama 的指令标签（instruction tags）是如何运作的，从而让它们协助你完成日常任务，例如写作或内容总结。
- 掌握高级提示技巧，例如用于分类的少样本提示（few-shot prompting），以及用于解决逻辑问题的思维链提示（chain-of-thought prompting）。
- 了解并使用 Llama 系列中针对特定任务的专业模型，例如 Code Llama 可以帮助你编写、分析和改进代码，而 Llama Guard 则用于检查提示和模型响应中是否存在有害内容。

本课程还会探讨如何在你自己的计算机上本地运行 Llama 2。

希望你能够通过这门课程，亲身体验这些功能强大且开放的模型！
https://t.co/kas7jmeCkj

### 018

作者: @AndrewYNg
时间: 2024-03-05
链接: https://x.com/AndrewYNg/status/1765059128190173202
互动: Likes: 1,306; Retweets: 131; Replies: 67; Quotes: 25; Views: 157,065; Bookmarks: 145; isReply: 0

There're now multiple, very well resourced companies that "can't afford to lose" spending billions to compete to build better LLMs. I expect this competition to go on for years. This is going to great for innovation, and also for everyone building applications on top of LLMs.

当前，许多资金雄厚的公司正不惜投入数十亿美元，竞相构建更出色的大语言模型（LLM），它们深知这场竞争「输不起」。我预计这种竞争将会持续数年。这不仅将极大地促进创新，也将为所有基于大语言模型（LLM）开发应用的人带来巨大的益处。

### 019

作者: @AndrewYNg
时间: 2024-03-06
链接: https://x.com/AndrewYNg/status/1765426218847949236
互动: Likes: 1,140; Retweets: 185; Replies: 40; Quotes: 28; Views: 224,100; Bookmarks: 707; isReply: 0

New short course: Open Source Models with Hugging Face 🤗, taught by @mariaKhalusova, @_marcsun, and Younes Belkada! @huggingface has been a game changer by letting you quickly grab any of hundreds of thousands of already-trained open source models to assemble into new applications. This course teaches you best practices for building this way, including how to search and choose among models.

You’ll learn to use the Transformers library and walk through multiple models for text, audio, and image processing, including zero-shot image segmentation, zero-shot audio classification, and speech recognition. You'll also learn to use multimodal models for visual question answering, image search, and image captioning. Finally, you’ll learn how to demo what you build locally, on the cloud, or via an API using Gradio and Hugging Face Spaces. 

You can sign up here: https://t.co/KavDNQHCCY

全新短期课程：由 @mariaKhalusova、@_marcsun 和 Younes Belkada 主讲，带你玩转 Hugging Face 🤗 的开源模型！@huggingface 平台堪称行业颠覆者，它允许你快速获取数十万个预训练的开源模型，并将它们集成到新的应用程序中。本课程将教授你通过这种方式构建项目的最佳实践，包括如何搜索和选择合适的模型。

你将学习使用 Transformers 库，并深入了解用于文本、音频和图像处理的多种模型，包括零样本图像分割（zero-shot image segmentation）、零样本音频分类（zero-shot audio classification）和语音识别（speech recognition）。此外，你还将学习如何使用多模态模型（multimodal models）进行视觉问答（visual question answering）、图像搜索（image search）和图像字幕（image captioning）。最后，你将学会如何利用 Gradio 和 Hugging Face Spaces 在本地、云端或通过 API（Application Programming Interface）展示你构建的应用成果。

点击这里注册：https://t.co/KavDNQHCCY

### 020

作者: @AndrewYNg
时间: 2024-03-09
链接: https://x.com/AndrewYNg/status/1766554536192446957
互动: Likes: 1,598; Retweets: 259; Replies: 91; Quotes: 37; Views: 240,773; Bookmarks: 648; isReply: 0

When we get to AGI, it will have come slowly, not overnight. 

A NeurIPS Outstanding Paper award recipient, Are Emergent Abilities of Large Language Models a Mirage? (by @RylanSchaeffer, @BrandoHablando, @sanmikoyejo) studies emergent properties of LLMs, and concludes: 
"... emergent abilities appear due the researcher’s choice of metric rather than due to fundamental changes in model behavior with scale. Specifically, nonlinear or discontinuous metrics produce apparent emergent abilities, whereas linear or continuous metrics produce smooth, continuous, predictable changes in model performance." 

Public perception goes through discontinuities when lots of people suddenly become aware of a technology -- maybe one that's been developing for a long time --  leading to a surprise. But growth in AI capabilities is  more continuous than one might think. 

That's why I expect the path to AGI to be one involving numerous steps forward, leading to step-by-step improvements in how intelligent our systems are.

当我们抵达通用人工智能（AGI）的彼岸时，它将是一个循序渐进的过程，而非一蹴而就。

一篇荣获 NeurIPS 杰出论文奖的论文 ——《大语言模型（Large Language Model）的涌现能力是海市蜃楼吗？》（作者：@RylanSchaeffer，@BrandoHablando，@sanmikoyejo）— 深入研究了大语言模型的涌现能力，并得出结论：
「... 涌现能力似乎是由于研究人员选择的衡量指标造成的，而非模型行为随规模变化而产生的根本性改变。具体来说，非线性或不连续的衡量指标会使涌现能力显得尤为突出，而线性或连续的衡量指标则展现出模型性能平滑、连续、可预测的变化。」

当一项技术 —— 也许是已经发展了很长时间的技术 —— 突然被大众所知时，公众的认知会经历跳跃式变化，从而产生惊讶感。然而，人工智能能力的发展实际上比人们想象的更具有连续性。

因此，我预计通往通用人工智能的道路将是步步为营的，每一步的进步都将使我们系统的智能程度逐步提升。

### 021

作者: @AndrewYNg
时间: 2024-03-09
链接: https://x.com/AndrewYNg/status/1766589035781202423
互动: Likes: 103; Retweets: 15; Replies: 20; Quotes: 4; Views: 11,793; Bookmarks: 21; isReply: 1

@SiVola @RylanSchaeffer @BrandoHablando @sanmikoyejo The definition of AGI I use is "AI that can perform any intellectual task that a human can."

But a few teams have come up with alternative definitions, so its meaning has become muddied and confusing, I now less it less esp in discussions that need technical precision.

@SiVola @RylanSchaeffer @BrandoHablando @sanmikoyejo 我所使用的 AGI（通用人工智能）定义是「能够执行人类可以完成的任何智力任务的 AI」。

然而，一些团队提出了其他的定义，这使得 AGI 的含义变得模糊且容易混淆。因此，我现在较少使用这个词，尤其是在需要技术精确性的讨论中。

### 022

作者: @AndrewYNg
时间: 2024-03-13
链接: https://x.com/AndrewYNg/status/1767941813820862655
互动: Likes: 2,104; Retweets: 408; Replies: 50; Quotes: 38; Views: 242,392; Bookmarks: 1,660; isReply: 0

Our new short course, Knowledge Graphs for RAG, is now available! Knowledge graphs are a data structure that is great at capturing complex relationships between data of multiple types. By enabling more sophisticated retrieval of text than similarity search alone, knowledge graphs can improve the context you pass to the LLM and the performance of your RAG applications. 

In this course, taught by @akollegger of @neo4j, you’ll
- Explore how knowledge graphs work by building a graph of public financial documents from scratch
- Learn to write queries that retrieve text and data from the graph and use it to enhance the context you pass to an LLM chatbot
- Combine a knowledge graph with a question-answer chain to build better RAG-powered chat systems

Sign up here! https://t.co/N3gceKrvib

我们的新短期课程「面向 RAG 的知识图谱」现已上线！知识图谱（Knowledge Graphs）是一种擅长捕获多种类型数据之间复杂关系的数据结构。通过实现比单纯的相似性搜索（similarity search）更复杂的文本检索方式，知识图谱可以改善您传递给大语言模型（LLM）的上下文，从而提升您的 RAG（Retrieval-Augmented Generation）应用程序的性能。

在本课程中，由来自 @neo4j 的 @akollegger 教授，您将：
- 通过从零开始构建一个关于公共财务文档的图谱，探索知识图谱的工作原理
- 学习编写查询，从图谱中检索文本和数据，并利用这些信息来增强您传递给大语言模型聊天机器人（chatbot）的上下文
- 将知识图谱与问答链（question-answer chain）结合，以构建更优秀的由 RAG 提供支持的聊天系统在此报名！https://t.co/N3gceKrvib

### 023

作者: @AndrewYNg
时间: 2024-03-18
链接: https://x.com/AndrewYNg/status/1769761666143814122
互动: Likes: 756; Retweets: 130; Replies: 21; Quotes: 14; Views: 104,458; Bookmarks: 413; isReply: 0

Learn how to build an optimized LLM inference system from the ground up in our new short course, Efficiently Serving LLMs, built in collaboration with @predibase and taught by @TravisAddair.

Whether you're serving your own LLM or using a model hosting service, this course will give you a deep understanding of the optimizations required to efficiently serve many users at once.
- Learn how LLMs generate text one token at a time, and how techniques like KV caching, continuous batching, and quantization speed things up and optimize memory usage for serving multiple users.
- Benchmark the performance of these LLM optimizations to explore the trade-offs between quickly responding to an individual user’s request vs. serving many users at once.
- Use techniques like low-rank adaptation (LoRA) to efficiently serve hundreds of unique, custom fine-tuned models on a single device, without sacrificing throughput.
- Use Predibase's LoRAX framework to see optimization techniques in action on a real LLM server.

Sign up here: https://t.co/JgIvrJGf8G

在我们的新短期课程《高效服务大语言模型》中，您将学习如何从头构建一套优化的大语言模型（LLM）推理系统。本课程由 @TravisAddair 授课，并与 @predibase 合作开发。

无论您是部署自己的大语言模型 ，还是使用模型托管服务，本课程都将让您深入理解，如何进行必要的优化才能高效地同时服务大量用户。
- 学习大语言模型是如何逐个 token 生成文本的，以及 KV 缓存（KV caching）、连续批处理（continuous batching）和量化（quantization）等技术如何加速推理并优化内存使用，从而服务多个用户。
- 对这些大语言模型优化技术的性能进行基准测试，探索快速响应单个用户请求与同时服务众多用户之间的权衡。
- 运用低秩适应（LoRA）等技术，在单个设备上高效服务数百个独特且定制化的微调模型，同时不牺牲吞吐量。
- 使用 Predibase 的 LoRAX 框架，在一个真实的大语言模型服务器上亲眼见证优化技术在实际中的应用。

在此注册：https://t.co/JgIvrJGf8G

### 024

作者: @AndrewYNg
时间: 2024-03-21
链接: https://x.com/AndrewYNg/status/1770897666702233815
互动: Likes: 5,257; Retweets: 1,251; Replies: 217; Quotes: 196; Views: 832,515; Bookmarks: 3,902; isReply: 0

I think AI agentic workflows will drive massive AI progress this year — perhaps even more than the next generation of foundation models. This is an important trend, and I urge everyone who works in AI to pay attention to it.

Today, we mostly use LLMs in zero-shot mode, prompting a model to generate final output token by token without revising its work. This is akin to asking someone to compose an essay from start to finish, typing straight through with no backspacing allowed, and expecting a high-quality result. Despite the difficulty, LLMs do amazingly well at this task!

With an agentic workflow, however, we can ask the LLM to iterate over a document many times. For example, it might take a sequence of steps such as:
- Plan an outline.
- Decide what, if any, web searches are needed to gather more information.
- Write a first draft.
- Read over the first draft to spot unjustified arguments or extraneous information.
- Revise the draft taking into account any weaknesses spotted.
- And so on.

This iterative process is critical for most human writers to write good text. With AI, such an iterative workflow yields much better results than writing in a single pass.

Devin’s splashy demo recently received a lot of social media buzz. My team has been closely following the evolution of AI that writes code. We analyzed results from a number of research teams, focusing on an algorithm’s ability to do well on the widely used HumanEval coding benchmark. You can see our findings in the diagram below. 

GPT-3.5 (zero shot) was 48.1% correct. GPT-4 (zero shot) does better at 67.0%. However, the improvement from GPT-3.5 to GPT-4 is dwarfed by incorporating an iterative agent workflow. Indeed, wrapped in an agent loop, GPT-3.5 achieves up to 95.1%. 

Open source agent tools and the academic literature on agents are proliferating, making this an exciting time but also a confusing one. To help put this work into perspective, I’d like to share a framework for categorizing design patterns for building agents. My team AI Fund is successfully using these patterns in many applications, and I hope you find them useful.

- Reflection: The LLM examines its own work to come up with ways to improve it.
- Tool use: The LLM is given tools such as web search, code execution, or any other function to help it gather information, take action, or process data.
- Planning: The LLM comes up with, and executes, a multistep plan to achieve a goal (for example, writing an outline for an essay, then doing online research, then writing a draft, and so on).
- Multi-agent collaboration: More than one AI agent work together, splitting up tasks and discussing and debating ideas, to come up with better solutions than a single agent would.

I’ll elaborate on these design patterns and offer suggested readings for each next week. 

[Original text: https://t.co/y4McIAjD2m]

我认为 AI 智能体（AI agent）工作流将在今年推动巨大的 AI 进步 —— 其影响力甚至可能超越下一代基础模型。这是一个值得高度关注的重要趋势，我强烈建议所有从事 AI 工作的人关注它。

目前，我们主要以零样本（zero-shot）模式使用大语言模型（LLM)：通过提示词指令模型逐个生成最终输出 Token（Token），期间不允许其修改自己的工作。这就像是要求一个人从头到尾完成一篇论文，中间不能回溯或修改，却仍然期待高质量的结果。尽管任务难度很高，但大语言模型在这种模式下依然表现惊人！

然而，借助智能体工作流，我们可以要求大语言模型对一份文档进行多次迭代。例如，它可能会遵循一系列步骤，例如：
- 规划大纲。
- 决定是否需要进行网络搜索以收集更多信息。
- 撰写初稿。
- 审阅初稿，找出缺乏依据的论点或多余的信息。
- 根据发现的任何弱点修改草稿。
- 依此类推。

这种迭代过程对于大多数人类作者来说，是写出优秀文本的关键。对于 AI 而言，这种迭代工作流比一次性写作能产生远更好的结果。

Devin 最近那场轰动一时的演示在社交媒体上引发了广泛热议。我的团队一直在密切关注 AI 编写代码的演变。我们分析了来自多个研究团队的结果，重点关注算法在广泛使用的 HumanEval 编码基准测试上表现如何。您可以在下面的图中看到我们的发现。

GPT-3.5（零样本）的正确率为 48.1%。GPT-4（零样本）表现更好，达到 67.0%。然而，从 GPT-3.5 到 GPT-4 的改进，在整合了迭代智能体工作流之后就显得相形见绌了。事实上，当 GPT-3.5 封装在智能体循环中时，其正确率高达 95.1%。

开源智能体工具和关于智能体的学术文献正在蓬勃发展，这使得当前既是激动人心的时刻，也可能令人感到困惑。为了帮助大家更好地理解这项工作，我想分享一个用于对构建智能体的设计模式进行分类的框架。我的团队 AI Fund 正在许多应用程序中成功运用这些模式，希望您也能从中受益。

- 反思（Reflection)：大语言模型检查自己的工作，以找出改进的方法。
- 工具使用（Tool use)：大语言模型被赋予工具，例如网络搜索、代码执行或任何其他功能，以帮助它收集信息、采取行动或处理数据。
- 规划（Planning)：大语言模型提出并执行一个多步骤计划以实现目标（例如，为一篇论文撰写大纲，然后进行在线研究，然后撰写初稿，依此类推）。
- 多智能体协作（Multi-agent collaboration)：多个 AI 智能体协同工作，分摊任务并讨论和辩论想法，以提出比单个智能体更好的解决方案。

我将在下周详细阐述这些设计模式，并为每种模式提供建议的阅读材料。

[原文链接： https://t.co/y4McIAjD2m]

### 025

作者: @AndrewYNg
时间: 2024-03-22
链接: https://x.com/AndrewYNg/status/1770967731753677266
互动: Likes: 35; Retweets: 6; Replies: 1; Quotes: 0; Views: 13,692; Bookmarks: 7; isReply: 1

@erikbryn Yes, and the outcomes of task-based analysis of jobs is also changing, since the set of tasks that agentic workflows can do is much larger than the set of tasks that non-agentic LLMs can do!

@erikbryn 没错，而且对工作的任务式分析结果也在发生变化。原因在于，AI 智能体（AI Agent）工作流能够处理的任务范围，比不具备智能体能力的大语言模型（Large Language Model）所能处理的任务范围要大得多！

### 026

作者: @AndrewYNg
时间: 2024-03-22
链接: https://x.com/AndrewYNg/status/1770969902452822519
互动: Likes: 117; Retweets: 16; Replies: 7; Quotes: 10; Views: 28,549; Bookmarks: 32; isReply: 1

Yes, with agentic workflows, super fast token generation (like @groq) becomes very important to overall system speed. 

If an LLM were generating tokens only for human consumption, then there's not much value to generating much faster than human reading speed. But with agentic workflows, most of the generated tokens are consumed not by humans but instead by another part of the AI system, so very very high token generation throughput is a big help to speeding up the overall system.

是的，在 AI 智能体（AI Agent）工作流中，超快的 Token 生成（比如 @groq）对提升整个系统的速度至关重要。

如果一个大语言模型（LLM）生成 Token 仅仅是为了供人类阅读和理解，那么生成速度远超人类阅读速度的意义就不大了。然而，在 AI 智能体工作流中，大多数生成的 Token 并非由人类直接消费，而是由 AI 系统的其他部分进一步处理，因此极高的 Token 生成吞吐量（throughput）对于加速整个系统运行有着巨大的帮助。

### 027

作者: @AndrewYNg
时间: 2024-03-22
链接: https://x.com/AndrewYNg/status/1771297451506622741
互动: Likes: 669; Retweets: 61; Replies: 28; Quotes: 9; Views: 107,590; Bookmarks: 129; isReply: 0

I’ve been a fan of ⁦@pyautogen⁩ as a multiagent programming framework for awhile. It was great hosting two of its leaders ⁦@Chi_Wang_⁩ and ⁦@qingyun_wu⁩ to discuss agent design patterns! https://t.co/1c2SrjLtj1

我一直是 @pyautogen 这个多智能体编程框架的忠实拥趸（粉丝）。很高兴能邀请到它的两位负责人 @Chi_Wang_ 和 @qingyun_wu，一起探讨 AI 智能体（Agent）的设计模式（Design Patterns）！ https://t.co/1c2SrjLtj1

### 028

作者: @AndrewYNg
时间: 2024-03-27
链接: https://x.com/AndrewYNg/status/1773006786058219889
互动: Likes: 1,277; Retweets: 241; Replies: 35; Quotes: 25; Views: 218,147; Bookmarks: 1,046; isReply: 0

New JavaScript short course: Build a full-stack web application that uses RAG in JavaScript RAG Web Apps with LlamaIndex, taught by @seldo, VP of Developer Relations at @llama_index and npm co-founder.
- Build a RAG application for querying your own data
- Develop tools to interact with multiple data sources using an agent that intelligently selects the right tool for your queries
- Create a full-stack web app that can chat with your data
- Dig further into production-ready techniques, like how to persist your data so you aren’t constantly reindexing, and try the create-llama command line tool from LlamaIndex
You can sign up here: https://t.co/w2j0Mq2df1

新的 JavaScript 短期课程来了：学习如何在 LlamaIndex 的「JavaScript RAG Web Apps」中，构建一个使用 RAG（Retrieval Augmented Generation，检索增强生成）技术的全栈网络应用程序。本课程由 @seldo 亲自授课，他不仅是 @llama_index 的开发者关系副总裁，还是 npm 的联合创始人。
- 构建一个能够查询您个人数据的 RAG 应用程序
- 开发工具，通过一个能智能选择合适工具来处理您查询的 AI 智能体（AI Agent），与多个数据源进行交互
- 创建一个可以与您的数据进行聊天的全栈网络应用程序
- 深入探索可用于生产环境的技术，例如如何持久化存储您的数据，避免频繁地重复索引，并体验 LlamaIndex 提供的 create-llama 命令行工具您可以在这里注册：https://t.co/w2j0Mq2df1

### 029

作者: @AndrewYNg
时间: 2024-03-28
链接: https://x.com/AndrewYNg/status/1773393357022298617
互动: Likes: 2,801; Retweets: 576; Replies: 101; Quotes: 76; Views: 488,223; Bookmarks: 2,649; isReply: 0

Last week, I described four design patterns for AI agentic workflows that I believe will drive significant progress this year: Reflection, Tool use, Planning and Multi-agent collaboration. Instead of having an LLM generate its final output directly, an agentic workflow prompts the LLM multiple times, giving it opportunities to build step by step to higher-quality output. Here, I'd like to discuss Reflection. For a design pattern that’s relatively quick to implement, I've seen it lead to surprising performance gains. 

You may have had the experience of prompting ChatGPT/Claude/Gemini, receiving unsatisfactory output, delivering critical feedback to help the LLM improve its response, and then getting a better response. What if you automate the step of delivering critical feedback, so the model automatically criticizes its own output and improves its response? This is the crux of Reflection. 

Take the task of asking an LLM to write code. We can prompt it to generate the desired code directly to carry out some task X. After that, we can prompt it to reflect on its own output, perhaps as follows:

Here’s code intended for task X:
[previously generated code]
Check the code carefully for correctness, style, and efficiency, and give constructive criticism for how to improve it.

Sometimes this causes the LLM to spot problems and come up with constructive suggestions. Next, we can prompt the LLM with context including (i) the previously generated code and (ii) the constructive feedback, and ask it to use the feedback to rewrite the code. This can lead to a better response. Repeating the criticism/rewrite process might yield further improvements. This self-reflection process allows the LLM to spot gaps and improve its output on a variety of tasks including producing code, writing text, and answering questions.

And we can go beyond self-reflection by giving the LLM tools that help evaluate its output; for example, running its code through a few unit tests to check whether it generates correct results on test cases or searching the web to double-check text output. Then it can reflect on any errors it found and come up with ideas for improvement.

Further, we can implement Reflection using a multi-agent framework. I've found it convenient to create two different agents, one prompted to generate good outputs and the other prompted to give constructive criticism of the first agent's output. The resulting discussion between the two agents leads to improved responses.

Reflection is a relatively basic type of agentic workflow, but I've been delighted by how much it improved my applications’ results in a few cases. I hope you will try it in your own work. If you’re interested in learning more about reflection, I recommend these papers:
- Self-Refine: Iterative Refinement with Self-Feedback, by Madaan et al. (2023)
- Reflexion: Language Agents with Verbal Reinforcement Learning, by Shinn et al. (2023)
- CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing, by Gou et al. (2024)

I’ll discuss the other agentic design patterns as well in the future.

[Original text: https://t.co/FtM2zOT2Lx ]

上周，我介绍了四种 AI 智能体工作流的设计模式，我相信它们将在今年推动显著的进展： 反思（Reflection）、 工具使用（Tool use）、 规划（Planning）和多智能体协作（Multi-agent collaboration）。与让大语言模型（LLM）直接生成最终输出不同， AI 智能体工作流会多次提示大语言模型，使其有机会逐步构建出更高质量的输出。今天，我想深入探讨一下反思这种模式。尽管它实现起来相对快速，但其带来的性能提升却常常令人惊喜。

你也许有过这样的经历：向 ChatGPT/Claude/Gemini 提问，收到的答案不尽如人意，于是你提供了批判性反馈，帮助大语言模型改进响应，最终获得了更好的答案。那么，如果我们将提供批判性反馈的步骤自动化，让模型自动评估自己的输出并进行改进呢？这正是反思的核心思想。

以要求大语言模型编写代码的任务为例。我们可以直接提示它生成执行特定任务 X 的代码。之后，我们可以提示它对自己的输出进行反思和评估，具体可以这样引导：

这是为任务 X 编写的代码：
[以前生成的代码]
请仔细检查代码的正确性、风格和效率，并提出建设性的改进意见。

在这种情况下， 大语言模型有时会发现问题并提出建设性建议。接下来，我们可以将（i）之前生成的代码和（ii）建设性反馈作为上下文，再次提示大语言模型，要求它根据反馈重写代码。这通常能带来更好的结果。重复这种评估 / 重写过程，可能会进一步提升代码质量。这种自我反思过程能帮助大语言模型在各种任务中发现不足并改进输出，无论是生成代码、撰写文本还是回答问题。

我们还可以将反思过程提升一个层次，为大语言模型配备有助于评估其输出的工具。例如，让它通过几个单元测试来运行生成的代码，检查在测试用例上是否得到正确结果；或者搜索网络来核实文本内容的准确性。这样， 大语言模型就能反思它发现的任何错误，并提出改进方案。

此外，我们还可以通过多智能体框架来实现反思。我发现一种有效的方法是创建两个不同的 AI 智能体：一个专门负责生成优质输出，另一个则负责对第一个智能体的输出提供建设性批评。这两个智能体之间的「讨论」能够促成响应质量的提升。

反思是一种相对基础的 AI 智能体工作流，但令我欣喜的是，它在一些情况下极大地改善了我的应用程序结果。我鼓励你也在自己的工作中尝试这种方法。如果你对了解更多关于反思的信息感兴趣，我推荐以下论文：
- Self-Refine：Iterative Refinement with Self-Feedback，作者 Madaan 等人（2023)
- Reflexion：Language Agents with Verbal Reinforcement Learning，作者 Shinn 等人（2023)
- CRITIC：Large Language Models Can Self-Correct with Tool-Interactive Critiquing，作者 Gou 等人（2024)

未来，我将继续探讨其他的 AI 智能体设计模式。

[原文链接：https://t.co/FtM2zOT2Lx]

### 030

作者: @AndrewYNg
时间: 2024-04-03
链接: https://x.com/AndrewYNg/status/1775324778624397657
互动: Likes: 1,866; Retweets: 127; Replies: 47; Quotes: 5; Views: 188,744; Bookmarks: 28; isReply: 0

I hope everyone in Taiwan 🇹🇼 is okay after the earthquake. My thoughts are with everyone affected. ❤️

希望台湾 🇹🇼 的每个人在地震后都平安。我的心与所有受影响的人同在。❤️

### 031

作者: @AndrewYNg
时间: 2024-04-03
链接: https://x.com/AndrewYNg/status/1775569875639116148
互动: Likes: 734; Retweets: 129; Replies: 27; Quotes: 7; Views: 109,324; Bookmarks: 319; isReply: 0

Learn to carry out red teaming attacks against your own LLM-based applications to spot and patch vulnerabilities! In our new short course, Red Teaming LLM Applications, Matteo Dora & Luca Martial of LLM testing company @giskard_ai teach how to simulate malicious actions to discover vulnerabilities, and improve security. We start with prompt injection, where you can trick an LLM into bypassing safeguards to reveal private information, or say something inappropriate. There is no one-size-fits-all approach to security, but this course will help you identify some scenarios to protect against.

We believe having red teaming capabilities widely known will result in greater transparency and safer LLM-based systems. However, we ask you to use the skills you gain from this course ethically.

Please sign up here: https://t.co/Y9ZANSldhG

学习如何对您自己的基于大语言模型（LLM）的应用程序进行红队攻击（red teaming attack），以发现并修补安全漏洞！在我们新的短期课程《LLM 应用程序的红队演练》中，LLM 测试公司 @giskard_ai 的 Matteo Dora 和 Luca Martial 将教您如何模拟恶意行为，从而发现漏洞并提高系统的安全性。我们将从提示注入（prompt injection）开始，这种攻击方式可以欺骗 LLM 绕过安全防护，泄露私人信息或发出不当言论。虽然安全防护没有万能的解决方案，但本课程将帮助您识别一些需要重点防范的场景。

我们相信，红队能力如果能被广泛掌握，将有助于提高透明度，并使基于 LLM 的系统更加安全。但是，我们要求您以道德的方式使用从本课程中获得的技能。

请在此处注册：https://t.co/Y9ZANSldhG

### 032

作者: @AndrewYNg
时间: 2024-04-04
链接: https://x.com/AndrewYNg/status/1775951610059141147
互动: Likes: 1,588; Retweets: 301; Replies: 80; Quotes: 33; Views: 255,763; Bookmarks: 1,270; isReply: 0

Tool use, in which an LLM is given functions it can request to call for gathering information, taking action, or manipulating data, is a key design pattern of AI agentic workflows. You may be familiar with LLM-based systems that can perform a web search or execute code. Some of the large, consumer-facing LLMs already incorporate these features. But tool use goes well beyond these examples. 

If you prompt an online LLM-based chat system, “What is the best coffee maker according to reviewers?”, it might decide to carry out a web search and download one or more web pages to gain context. Early on, LLM developers realized that relying only on a pre-trained transformer to generate output tokens is limiting, and that giving an LLM a tool for web search lets it do much more. With such a tool, an LLM is either fine-tuned or prompted (perhaps with few-shot prompting) to generate a special string like {tool: web-search, query: "coffee maker reviews"} to request calling a search engine. (The exact format of the string depends on the implementation.) A post-processing step then looks for strings like these, calls the web search function with the relevant parameters when it finds one, and passes the result back to the LLM as additional input context for further processing.

Similarly, if you ask, “If I invest $100 at compound 7% interest for 12 years, what do I have at the end?”, rather than trying to generate the answer directly using a transformer network — which is unlikely to result in the right answer — the LLM might use a code execution tool to run a Python command to compute 100 * (1+0.07)**12 to get the right answer. The LLM might generate a string like this: {tool: python-interpreter, code: "100 * (1+0.07)**12"}.

But tool use in agentic workflows now goes much further. Developers are using functions to search different sources (web, Wikipedia, arXiv, etc.), to interface with productivity tools (send email, read/write calendar entries, etc.), generate or interpret images, and much more. We can prompt an LLM using context that gives detailed descriptions of many functions. These descriptions might include a text description of what the function does plus details of what arguments the function expects. And we’d expect the LLM to automatically choose the right function to call to do a job.

Further, systems are being built in which the LLM has access to hundreds of tools. In such settings, there might be too many functions at your disposal to put all of them into the LLM context, so you might use heuristics to pick the most relevant subset to include in the LLM context at the current step of processing. This technique, which is described in the Gorilla paper cited below, is reminiscent of how, if there is too much text to include as context, retrieval augmented generation (RAG) systems offer heuristics for picking a subset of the text to include.

Early in the history of LLMs, before widespread availability of large multimodal models (LMMs)  like LLaVa, GPT-4V, and Gemini, LLMs could not process images directly, so a lot of work on tool use was carried out by the computer vision community. At that time, the only way for an LLM-based system to manipulate an image was by calling a function to, say, carry out object recognition or some other function on it. Since then, practices for tool use have exploded. GPT-4’s function calling capability, released in the middle of last year, was a significant step toward general-purpose tool use. Since then, more and more LLMs are being developed to similarly be facile with tool use.

If you’re interested in learning more about tool use, I recommend:
- Gorilla: Large Language Model Connected with Massive APIs, Patil et al. (2023)
- MM-REACT: Prompting ChatGPT for Multimodal Reasoning and Action, Yang et al. (2023)
- Efficient Tool Use with Chain-of-Abstraction Reasoning, Gao et al. (2024)

Both Tool Use and Reflection, which I posted about last week, are design patterns that I can get to work fairly reliably on my applications — both are capabilities well worth learning about. In the future, I’ll describe the Planning and Multi-agent collaboration design patterns. They allow AI agents to do much more but are less mature, less predictable — albeit very exciting — technologies.

[Original text:  https://t.co/gHCOYSsKQO ]

工具使用，即赋予大语言模型（LLM）可供其请求调用的功能，用于收集信息、采取行动或操纵数据，是 AI 智能体（AI agent）工作流中的一个关键设计模式。你可能已经熟悉那些能够执行网页搜索或运行代码的基于大语言模型的系统。一些大型的、面向消费者的的大语言模型已经内置了这些功能。但工具使用的范畴远不止于此。

如果你向一个在线的基于大语言模型的聊天系统提问：「根据评论者，最好的咖啡机是什么？」，它可能会决定进行一次网页搜索，并下载一个或多个网页来获取相关背景信息。早期，大语言模型开发者就意识到，仅仅依靠预训练的 Transformer 来生成输出 Token（标记）是有局限的。如果赋予大语言模型网页搜索工具，它就能做更多事情。有了这样的工具，大语言模型会经过微调或通过提示（例如少样本（few-shot）提示）来生成一个特殊字符串，例如 {tool：web-search，query："coffee maker reviews"}，从而请求调用搜索引擎。(该字符串的具体格式取决于具体的实现。）随后，一个后处理步骤会查找这些特殊字符串，一旦找到，便会使用相关参数调用网页搜索功能，并将结果作为额外的输入上下文反馈给大语言模型进行进一步处理。

同样，如果你问：「如果我以 7% 的复利投资 100 美元 12 年，最后我能得到多少钱？」，大语言模型不会试图直接使用 Transformer 网络来生成答案 — 因为这不太可能得出正确结果 — 而是可能调用一个代码执行工具，运行像 100 *（1+0.07)**12 这样的 Python 命令，从而得出正确答案。大语言模型可能会生成一个类似这样的字符串：{tool：python-interpreter，code："100 *（1+0.07)**12"}。

然而，在智能体工作流中，工具使用的能力已经大大拓展。开发者正利用这些功能搜索不同的信息来源（例如网络、维基百科、arXiv 等），与生产力工具对接（例如发送电子邮件、读写日历条目等），生成或解释图像，以及实现更多目标。我们可以通过提供详细描述众多功能的上下文来提示大语言模型。这些描述可能包括对功能作用的文本说明，以及该功能预期接收哪些参数的详细信息。我们期望大语言模型能够自动选择合适的工具来完成任务。

此外，目前正在开发的系统，能让大语言模型访问数百种工具。在这种情况下，可供大语言模型使用的功能可能太多，无法将所有功能都纳入其上下文（context），因此系统可能会采用启发式方法来挑选最相关的子集，以便在当前处理步骤中包含在大语言模型的上下文内。这项技术在下面引用的 Gorilla 论文中有所描述，它类似于当有太多文本无法全部作为上下文时，检索增强生成（RAG）系统如何提供启发式方法来选择文本的一个子集以供包含。

在大语言模型发展早期，在 LLaVa、GPT-4V 和 Gemini 等大型多模态模型（LMM）尚未广泛普及之前，大语言模型无法直接处理图像。因此，计算机视觉社区在工具使用方面做了大量工作。那时，基于大语言模型的系统操纵图像的唯一方式是调用一个功能，例如对其执行目标识别或进行其他处理。自那时起，工具使用的实践已经蓬勃发展。GPT-4 于去年年中发布的功能调用能力，是迈向通用工具使用的重要一步。此后，越来越多的的大语言模型正在开发中，以期同样擅长工具使用。

如果你有兴趣了解更多关于工具使用的信息，我推荐以下论文：
- Gorilla：Large Language Model Connected with Massive APIs，Patil et al.（2023)
- MM-REACT：Prompting ChatGPT for Multimodal Reasoning and Action，Yang et al.（2023)
- Efficient Tool Use with Chain-of-Abstraction Reasoning，Gao et al.（2024)

工具使用和反思，我在上周的帖子中提到了它们，这些设计模式在我开发的应用程序中都能相当可靠地发挥作用 — 两者都是非常值得学习的能力。未来，我将描述规划和多智能体协作设计模式。它们能让 AI 智能体完成更多任务，但作为技术而言，它们成熟度较低、可预测性较差 — 尽管它们非常令人兴奋。

[原始文本：https://t.co/gHCOYSsKQO]

### 033

作者: @AndrewYNg
时间: 2024-04-05
链接: https://x.com/AndrewYNg/status/1776363779141628369
互动: Likes: 519; Retweets: 90; Replies: 33; Quotes: 8; Views: 172,487; Bookmarks: 316; isReply: 0

The task-based analysis of how AI affects jobs is a powerful technique for creating business value. It was pioneered by Workhelix’s @erikbryn et al. Now, Workhelix has developed technology to apply this at scale, by automatically examining a company’s job descriptions, professional social data, and other information, to give CEOs and Boards a roadmap to creating value. 

AI Fund is thrilled to support Workhelix’s launch, coming Tuesday April 9th. To learn more, please join the conversation with @erikbryn, @amcafee, @danielrock and @JamesMilin and me at the webinar below! https://t.co/I6sVHhEGmV

针对 AI（Artificial Intelligence）如何基于任务影响工作的分析，是创造商业价值的一种强大技术。这项技术最初由 Workhelix 的 @erikbryn 等人开创。现在，Workhelix 已经开发出相关技术，能够大规模应用这一分析方法：通过自动审查公司的职位描述、专业社交数据及其他信息，为 CEO（首席执行官）和董事会（Boards）提供一份创造价值的路线图。

AI Fund 很高兴能支持 Workhelix 在 4 月 9 日（星期二）上线。想要了解更多信息，请点击下方链接，与 @erikbryn、@amcafee、@danielrock、@JamesMilin 以及我一起参加网络研讨会，加入我们的讨论！https://t.co/I6sVHhEGmV

### 034

作者: @AndrewYNg
时间: 2024-04-06
链接: https://x.com/AndrewYNg/status/1776737961243218134
互动: Likes: 279; Retweets: 56; Replies: 43; Quotes: 7; Views: 110,658; Bookmarks: 97; isReply: 0

The Financial Times has a great article on Renate Nyborg @renate's work on @meeno_official , written by @madhumita29. 

The article is paywalled, but I appreciate Renate (as well as Harvard's @ronivey)'s leadership speaking about the dangers of the AI fake girlfriend/boyfriend industry and the risk of this leading to greater loneliness. Renate says  "Men didn’t want to meet girls because they had virtual girlfriends who said exactly what they wanted to hear." To regulators wondering what are the risky applications of AI, I would urge taking a look at the fake gf/bf industry! 

In contrast, Meeno gives advice for human relationships, and is working to bring people together. Working to reduce human loneliness is a wonderful goal! 

https://t.co/nB6dfkHaHn

《金融时报》刊登了一篇由 @madhumita29 撰写的精彩文章，介绍了 Renate Nyborg @renate 在 @meeno_official 方面的工作。

该文章设有付费墙，但我非常赞赏 Renate（以及哈佛大学的 @ronivey）带头指出 AI 假女友 / 男友行业的危险，以及这可能加剧人类孤独感的问题。Renate 表示：「男性不愿与现实中的女孩交往，因为他们拥有虚拟女友，这些虚拟女友总能说出他们想听的一切。」对于那些正在探寻 AI（人工智能）潜在高风险应用的监管机构，我强烈建议他们关注假女友 / 男友行业！

与此形成对比的是，Meeno 旨在为真实的人际关系提供建议，并努力将人们联系在一起。致力于减少人类孤独感，这无疑是一个美好的目标！

https://t.co/nB6dfkHaHn

### 035

作者: @AndrewYNg
时间: 2024-04-10
链接: https://x.com/AndrewYNg/status/1778075380886495676
互动: Likes: 1,190; Retweets: 235; Replies: 24; Quotes: 21; Views: 150,023; Bookmarks: 814; isReply: 0

Data preprocessing is critical for building effective RAG systems. Our new short course, Preprocessing Unstructured Data for LLM Applications, taught by @mrobinson0623 of @UnstructuredIO, demonstrates important but sometimes overlooked aspects of RAG systems:

- How to extract and normalize content from diverse formats like PDF, Powerpoint, and HTML to expand your LLM's knowledge
- Enriching data with metadata to enable more powerful retrieval and reasoning
- Applying document layout analysis and vision transforms to process embedded images and tables

Then you’ll use all these skills and build a RAG bot that draws from a corpus that includes PDF, PowerPoint, and Markdown documents.

Please sign up here: https://t.co/AM3rmZJmNF

数据预处理对于构建高效的 RAG 系统（Retrieval Augmented Generation systems）来说不可或缺。我们新推出的短课程「面向大语言模型（Large Language Model）应用的非结构化数据预处理」，由 @UnstructuredIO 的 @mrobinson0623 老师主讲，将深入探讨 RAG 系统中一些至关重要却常被忽视的环节：

- 如何从 PDF、Powerpoint 和 HTML 等多种格式中提取并规范化内容，从而为大语言模型提供更广阔的知识基础。
- 利用元数据（metadata）丰富数据，以实现更强大的检索和推理能力。
- 应用文档版面分析（document layout analysis）和视觉转换（vision transforms）技术来处理文档中嵌入的图像和表格。

学完本课程，您将能够运用这些技能，亲手搭建一个 RAG 机器人（Retrieval Augmented Generation bot），它能从包含 PDF、PowerPoint 和 Markdown 文档的语料库（corpus）中智能提取信息。

欢迎点击此处报名学习：https://t.co/AM3rmZJmNF

### 036

作者: @AndrewYNg
时间: 2024-04-14
链接: https://x.com/AndrewYNg/status/1779606380665803144
互动: Likes: 2,431; Retweets: 457; Replies: 83; Quotes: 58; Views: 389,654; Bookmarks: 2,022; isReply: 0

Planning is a key agentic AI design pattern in which we use a large language model (LLM) to autonomously decide on what sequence of steps to execute to accomplish a larger task. For example, if we ask an agent to do online research on a given topic, we might use an LLM to break down the objective into smaller subtasks, such as researching specific subtopics, synthesizing findings, and compiling a report.

Many people had a “ChatGPT moment” shortly after ChatGPT was released, when they played with it and were surprised that it significantly exceeded their expectation of what AI can do. If you have not yet had a similar “AI Agentic moment,” I hope you will soon. I had one several months ago, when I presented a live demo of a research agent I had implemented that had access to various online search tools.

I had tested this agent multiple times privately, during which it consistently used a web search tool to gather information and wrote up a summary. During the live demo, though, the web search API unexpectedly returned with a rate limiting error. I thought my demo was about to fail publicly, and I dreaded what was to come next. To my surprise, the agent pivoted deftly to a Wikipedia search tool — which I had forgotten I’d given it — and completed the task using Wikipedia instead of web search.

This was an AI Agentic moment of surprise for me. I think many people who haven’t experienced such a moment yet will do so in the coming months. It’s a beautiful thing when you see an agent autonomously decide to do things in ways that you had not anticipated, and succeed as a result!

Many tasks can’t be done in a single step or with a single tool invocation, but an agent can decide what steps to take. For example, to simplify an example from the HuggingGPT paper (cited below), if you want an agent to consider a picture of a boy and draw a picture of a girl in the same pose, the task might be decomposed into two distinct steps: (i) detect the pose in the picture of the boy and (ii) render a picture of a girl in the detected pose. An LLM might be fine-tuned or prompted (with few-shot prompting) to specify a plan by outputting a string like "{tool: pose-detection, input: image.jpg, output: temp1 } {tool: pose-to-image, input: temp1, output: final.jpg}".

This structured output, which specifies two steps to take, then triggers software to invoke a pose detection tool followed by a pose-to-image tool to complete the task. (This example is for illustrative purposes only; HuggingGPT uses a different format.)

Admittedly, many agentic workflows do not need planning. For example, you might have an agent reflect on, and improve, its output a fixed number of times. In this case, the sequence of steps the agent takes is fixed and deterministic. But for complex tasks in which you aren’t able to specify a decomposition of the task into a set of steps ahead of time, Planning allows the agent to decide dynamically what steps to take.

On one hand, Planning is a very powerful capability; on the other, it leads to less predictable results. In my experience, while I can get the agentic design patterns of Reflection and Tool use to work reliably and improve my applications’ performance, Planning is a less mature technology, and I find it hard to predict in advance what it will do. But the field continues to evolve rapidly, and I'm confident that Planning abilities will improve quickly.

If you’re interested in learning more about Planning with LLMs, I recommend:
- Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, Wei et al. (2022)
- HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face, Shen et al. (2023)
- Understanding the planning of LLM agents: A survey, by Huang et al. (2024)

[Original text: https://t.co/pWmIR9wEki ]

规划（Planning）是一种核心的 AI 智能体（AI agent）设计模式。在这种模式中，我们利用大语言模型（LLM）自主决定一系列要执行的步骤，以完成一项更大的任务。举个例子，如果我们要求一个智能体就某个主题进行在线研究，我们可能会让 LLM 将这个大目标拆解成更小的子任务，比如研究具体的子主题、整合各项发现，最后再撰写一份报告。

许多人在 ChatGPT 发布后不久，都经历过一个「ChatGPT 时刻」—— 当他们试用 ChatGPT 时，惊喜地发现它的表现远超他们对 AI 能力的预期。如果你还没体验过类似的「AI 智能体时刻」，我希望你很快也能经历。我几个月前就有过一次这样的体验：当时我现场演示了一个自己实现的研究智能体，它能调用各种在线搜索工具。

我曾多次私下测试这个智能体，每次它都能稳定地使用网络搜索工具收集信息，并总结出一份报告。然而，在一次现场演示中，网络搜索 API 却意外地报出了速率限制错误。我当时以为我的演示要当众失败了，心里非常忐忑。但出乎我意料的是，这个智能体灵巧地切换到了维基百科搜索工具 —— 我都忘了自己曾赋予它这项能力 —— 并最终使用维基百科而不是网络搜索完成了任务。

这对我来说就是一个充满惊喜的 AI 智能体时刻。我相信，许多尚未有过这种体验的人，在未来几个月内也将迎来这样的时刻。当你看到一个智能体能自主决定以你意想不到的方式完成任务，并且最终成功了，那感觉真是妙不可言！

很多任务无法一步到位，也无法通过单一工具调用来完成，但智能体可以自主决定要采取哪些步骤。例如，为了简化 HuggingGPT 论文（参见下文引用）中的一个例子：如果你想让一个智能体分析一张男孩的照片，然后画一张相同姿势的女孩的照片，这项任务可以分解成两个截然不同的步骤：(i）检测男孩照片中的姿势，以及（ii）基于检测到的姿势渲染一张女孩的照片。一个 LLM 可能会被微调，或者通过少样本（Few-shot）提示来规划步骤，并输出一个类似「{tool：pose-detection，input：image.jpg，output：temp1} {tool：pose-to-image，input：temp1，output：final.jpg}」的字符串。

这个结构化的输出明确了要执行的两个步骤，随后会触发软件依次调用姿势检测工具（pose detection tool）和姿势转图像工具（pose-to-image tool）来完成任务。（此示例仅用于说明目的；HuggingGPT 使用的格式有所不同。）

当然，许多 AI 智能体工作流（workflow）并不需要规划。例如，你可能让一个智能体在固定次数内反思（Reflection）并优化其输出。在这种情况下，智能体采取的步骤序列是固定且确定性的。但对于那些你无法预先指定任务分解步骤的复杂任务，规划（Planning）就允许智能体动态地决定如何行动。

一方面，规划是一项非常强大的能力；另一方面，它也使得结果的可预测性降低。根据我的经验，虽然我能让反思（Reflection）和工具使用（Tool use）这两种智能体设计模式可靠地发挥作用，并提升我应用程序的性能，但规划仍是一项相对不够成熟的技术，我发现很难提前预测它的具体行为。不过，这个领域正在迅速发展，我相信规划能力会很快得到显著提升。

如果您对利用 LLM 进行规划（Planning）感兴趣，我推荐阅读以下文献：
- Chain-of-Thought Prompting Elicits Reasoning in Large Language Models，Wei et al.（2022)
- HuggingGPT：Solving AI Tasks with ChatGPT and its Friends in Hugging Face，Shen et al.（2023)
- Understanding the planning of LLM agents：A survey，by Huang et al.（2024)

[Original text：https://t.co/pWmIR9wEki]

### 037

作者: @AndrewYNg
时间: 2024-04-15
链接: https://x.com/AndrewYNg/status/1779905922602782752
互动: Likes: 2,355; Retweets: 451; Replies: 41; Quotes: 28; Views: 287,673; Bookmarks: 1,351; isReply: 0

LLMs can take gigabytes of memory to store, which limits what can be run on consumer hardware. But quantization can dramatically compress models, making a wider selection of models available to developers. You can often reduce model size by 4x or more while maintaining reasonable performance. In our new short course Quantization Fundamentals taught by @huggingface's @younesbelkada and @_marcsun, you'll: 
- Learn how to quantize nearly any open source model
- Use int8 and bfloat16 (Brain float 16) data types to load and run LLMs using PyTorch and the Hugging Face Transformers library
- Dive into the technical details of linear quantization to map 32-bit floats to 8-bit integers

As models get bigger and bigger, quantization becomes more important for making models practical and accessible. Please check out the course here:  https://t.co/i8trQdOIOh

大语言模型（LLM）的存储通常需要占用数千兆字节的内存，这限制了它们在消费级硬件上的运行能力。然而，量化（quantization）技术可以显著压缩模型，从而让开发者能够使用更广泛的模型。通常情况下，您可以在保持合理性能的同时，将模型大小减少 4 倍甚至更多。在由 @huggingface 的 @younesbelkada 和 @_marcsun 讲授的新短课程「量化基础（Quantization Fundamentals）」中，您将学习到：
- 如何量化几乎所有开源模型
- 利用 int8 和 bfloat16（Brain float 16）数据类型，通过 PyTorch 和 Hugging Face Transformers 库加载并运行大语言模型（LLM)
- 深入了解线性量化的技术细节，即如何将 32 位浮点数映射成 8 位整数随着模型规模越来越庞大，量化对于提升模型的实用性和可访问性变得愈发重要。请点击此处查看课程详情：https://t.co/i8trQdOIOh

### 038

作者: @AndrewYNg
时间: 2024-04-18
链接: https://x.com/AndrewYNg/status/1780991671855161506
互动: Likes: 2,402; Retweets: 516; Replies: 89; Quotes: 87; Views: 413,335; Bookmarks: 1,894; isReply: 0

Multi-agent collaboration has emerged as a key AI agentic design pattern. Given a complex task like writing software, a multi-agent approach would break down the task into subtasks to be executed by different roles -- such as a software engineer, product manager, designer, QA (quality assurance) engineer, and so on -- and have different agents accomplish different subtasks.

Different agents might be built by prompting one LLM (or, if you prefer, different LLMs) to carry out different tasks. For example, to build a software engineer agent, we might prompt the LLM: "You are an expert in writing clear, efficient code. Write code to perform the task …".

It might seem counterintuitive that, although we are making multiple calls to the same LLM, we apply the programming abstraction of using multiple agents. I'd like to offer a few reasons:
- It works! Many teams are getting good results with this method, and there's nothing like results! Further, ablation studies (for example, in the AutoGen paper cited below) show that multiple agents give superior performance to a single agent.
- Even though some LLMs today can accept very long input contexts (for instance, Gemini 1.5 Pro accepts 1 million tokens), their ability to truly understand long, complex inputs is mixed. An  agentic workflow in which the LLM is prompted to focus on one thing at a time can give better performance. By telling it when it should play software engineer, we can also specify what is important in that  subtask: For example, the prompt above emphasized clear, efficient code as opposed to, say, scalable and highly secure code. By decomposing the overall task into subtasks, we can optimize the subtasks better.
- Perhaps most important, the multi-agent design pattern gives us, as developers, a framework for breaking down complex tasks into subtasks. When writing code to run on a single CPU, we often break our program up into different processes or threads. This is a useful abstraction that lets us decompose a task -- like implementing a web browser -- into subtasks that are easier to code. I find thinking through multi-agents roles to be a useful abstraction.

In many companies, managers routinely decide what roles to hire, and then how to split complex projects -- like writing a large piece of software or preparing a research report -- into smaller tasks to assign to employees with different specialties. Using multiple agents is analogous. Each agent implements its own workflow, has its own memory (itself a rapidly evolving area in agentic technologies -- how can an agent remember enough of its past interactions to perform better on upcoming ones?), and may ask other agents for help. Agents themselves can also engage in Planning and Tool Use. This results in a cacophony of LLM calls and message passing between agents that can result in very complex workflows.

While managing people is hard, it's a sufficiently familiar idea that it gives us a mental framework for how to "hire" and assign tasks to our AI agents. Fortunately, the damage from mismanaging an AI agent is much lower than that from mismanaging humans!

Emerging frameworks like AutoGen, Crew AI, and LangGraph, provide rich ways to build multi-agent solutions to problems. If you're interested in playing with a fun multi-agent system, also check out ChatDev, an open source implementation of a set of agents that run a virtual software company. I encourage you to check out their github repo and perhaps even clone the repo and run  the system yourself. While it may not always produce what you want, you might be amazed at how well it does!

Like the design pattern of Planning, I find the output quality of multi-agent collaboration hard to predict. The more mature patterns of Reflection and Tool use are more reliable. I hope you enjoy playing with these agentic design patterns and that they produce amazing results for you!

If you're interested in learning more, I recommend:
- Communicative Agents for Software Development, Qian et al. (2023) (the ChatDev paper)
- AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation, Wu et al. (2023)
- MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework, Hong et al. (2023)

[Original text: https://t.co/4gTbcQfikx ]

多智能体协作（Multi-agent collaboration）已经成为 AI 智能体（AI agent）设计中的一个关键模式。设想一个像编写软件这样的复杂任务，多智能体方法会将任务分解成由不同「角色」负责的子任务 —— 比如软件工程师、产品经理、设计师、QA（质量保证）工程师等等 —— 然后让不同的智能体去完成这些不同的子任务。

构建这些智能体的方法是，用特定的提示词引导一个大语言模型（LLM）（或者说，可以为不同的智能体设定不同的 LLM）来执行不同的任务。例如，要创建一个软件工程师智能体，我们可能会这样提示 LLM：「你是一位编写清晰、高效代码的专家。请编写代码来完成这项任务……」

这或许听起来有些反常，毕竟我们可能只是在对同一个大语言模型进行多次调用，但我们仍然采用了多个智能体的编程抽象模式。对此，我想给出几个原因：
- 这种方法确实有效！许多团队正通过它取得良好的结果，实践效果是最好的证明！此外，消融研究（ablation studies）（例如，下面引用的 AutoGen 论文中）也表明，多个智能体比单个智能体能带来更卓越的性能。
- 尽管现在一些大语言模型可以接受非常长的输入上下文（比如 Gemini 1.5 Pro 能接受 100 万个 Token），但它们真正理解这些长而复杂输入的能力表现不一。采用智能体工作流（agentic workflow），让大语言模型一次只专注于一件事情，可以带来更好的性能。通过明确告诉它何时应该扮演软件工程师的角色，我们也能指定该子任务中哪些要素是重要的：例如，上面提到的提示词强调了清晰、高效的代码，而非可扩展性或高安全性。通过将整体任务分解为子任务，我们就能更好地优化每一个子任务。
- 也许最重要的一点是，多智能体设计模式为我们开发者提供了一个将复杂任务分解为子任务的框架。就像我们在编写运行于单个 CPU 上的代码时，常常会把程序分解成不同的进程或线程。这是一种非常有用的抽象方式，让我们能够将一个大任务（比如实现一个网页浏览器）分解成更容易编码的子任务。我发现将多智能体角色作为一种抽象思考方式，能带来极大的便利。

在许多公司中，管理者们通常会决定招聘哪些职位，然后将复杂的项目（比如开发大型软件或准备研究报告）分解成小任务，分配给具有不同专业技能的员工。使用多个智能体的道理与此类似。每个智能体都执行自己的工作流，拥有自己的记忆（这本身就是智能体技术中一个快速发展的领域 —— 智能体如何记住足够多的过去交互，以便在未来的任务中表现更出色？），并且可能会向其他智能体寻求帮助。智能体本身还可以进行规划（Planning）和工具使用（Tool Use）。这些因素共同导致了大语言模型调用和智能体之间消息传递的频繁发生，从而形成了非常复杂的工作流。

虽然管理人员很困难，但它是一个我们足够熟悉的理念，它为我们提供了一个如何「招聘」和分配任务给我们的 AI 智能体的心智模型。幸运的是，错误管理 AI 智能体所造成的损失，远低于错误管理人力所造成的损失！

AutoGen、Crew AI 和 LangGraph 等新兴框架提供了丰富的方式来构建多智能体解决方案。如果你有兴趣尝试一个有趣的多智能体系统，也可以看看 ChatDev，它是一个运行虚拟软件公司的一组智能体的开源实现。我鼓励你查看他们的 GitHub 仓库，甚至可以克隆仓库并亲自运行这个系统。虽然它可能不总是产生你想要的结果，但你可能会对其表现感到惊叹！

与规划（Planning）这种设计模式类似，我发现多智能体协作的输出质量难以预测。而更为成熟的反射（Reflection）和工具使用（Tool Use）则相对更可靠。我希望你喜欢尝试这些智能体设计模式，并期待它们能为你带来惊人的成果！

如果你有兴趣了解更多，我推荐：
- Communicative Agents for Software Development，Qian et al.（2023）(ChatDev 论文)
- AutoGen：Enabling Next-Gen LLM Applications via Multi-Agent Conversation，Wu et al.（2023)
- MetaGPT：Meta Programming for A Multi-Agent Collaborative Framework，Hong et al.（2023)

### 039

作者: @AndrewYNg
时间: 2024-04-18
链接: https://x.com/AndrewYNg/status/1781021135339164147
互动: Likes: 4,171; Retweets: 166; Replies: 288; Quotes: 27; Views: 293,078; Bookmarks: 113; isReply: 0

Meta released Llama 3 on my birthday! 🎂 Best present ever, thanks Meta! 😀

Meta 在我生日当天发布了 Llama 3！🎂 这真是有史以来最棒的礼物，感谢 Meta！😀

### 040

作者: @AndrewYNg
时间: 2024-04-22
链接: https://x.com/AndrewYNg/status/1782442718960230688
互动: Likes: 1,630; Retweets: 278; Replies: 40; Quotes: 17; Views: 385,624; Bookmarks: 1,030; isReply: 0

New short course with @MistralAI !

Mistral's open-source Mixtral 8x7B model uses a "mixture of experts" (MoE) architecture. Unlike a standard transformer, an MoE model has multiple expert feed-forward networks (8 in this case), with a gating network selecting two experts at inference time. This enables MoE to match the performance of a large model but faster inference. Mixtral 8x7B has 46.7B parameters but activates only 12.9B at inference to predict the next token.

In Getting Started with Mistral, you’ll learn from Mistral’s @sophiamyang to:
- Explore Mistral's open-source models (Mistral 7B, Mixtral 8x7B) and commercial models via API calls and Mistral AI's Le Chat website
- Implement JSON mode to generate structured outputs to integrate directly into larger software systems.
- Use function calling for Tool Use, such as calling custom Python code that queries tabular data
- Ground your LLM's response with external knowledge sources using RAG
- Build a Mistral-powered chat interface that can reference external documents

This course will help deepen your prompt engineering skills. Please sign up here: https://t.co/weYwGmPlLA

@MistralAI 推出全新短期课程！

Mistral 的开源 Mixtral 8x7B 模型采用了一种「专家混合」(Mixture of Experts，MoE）架构。与标准 Transformer 不同，MoE 模型拥有多个专家前馈网络 （本例中有 8 个），并配备一个门控网络，在推理时选择其中两个专家。这种设计使得 MoE 在性能上能够与大型模型媲美，同时实现更快的推理速度。Mixtral 8x7B 拥有 46.7B 参数，但在推理时仅激活其中的 12.9B 参数来预测下一个 Token（Token）。

在《开始使用 Mistral》课程中，你将跟随 Mistral 的 @sophiamyang 学习：
- 探索 Mistral 的开源模型（Mistral 7B，Mixtral 8x7B），以及通过 API 调用和 Mistral AI 的 Le Chat 网站访问的商业模型
- 实现 JSON 模式，以生成结构化输出，从而直接集成到更大的软件系统中
- 使用函数调用（Function Calling）实现工具调用，例如调用查询表格数据的自定义 Python 代码
- 利用 RAG（Retrieval Augmented Generation）技术，基于外部知识源来增强你大语言模型（LLM）的响应
- 构建一个由 Mistral 提供支持的聊天界面，该界面能够参考外部文档本课程将帮助你提升提示工程（Prompt Engineering）技能。请在此处注册：https://t.co/weYwGmPlLA

### 041

作者: @AndrewYNg
时间: 2024-04-25
链接: https://x.com/AndrewYNg/status/1783521818093195277
互动: Likes: 1,303; Retweets: 236; Replies: 52; Quotes: 39; Views: 251,741; Bookmarks: 499; isReply: 0

Much has been said about many companies’ desire for more compute (as well as data) to train larger foundation models. I think it’s under-appreciated that we have nowhere near enough compute available for inference on foundation models as well.

Years ago, when I was leading teams at Google, Baidu, and Stanford that focused on scaling up deep learning algorithms, many semiconductor manufacturers, data center operators, and academic researchers asked me whether I felt that AI technology would continue to make good use of more compute if they kept on delivering it. For many normal desktop processing workloads, like running a web browser or a text editor, having a faster CPU doesn’t help that much beyond a certain point. So do we really need faster and faster AI processors to train larger and larger models? Each time, I confidently replied “yes!” and encouraged them to keep scaling up compute. (Sometimes, I added half-jokingly that I had never met a machine learning engineer who felt like they had enough compute. 😀)

Fortunately, this prediction has been right so far. However, beyond training, I believe we are also far from exhausting the benefits of faster and higher volumes of inference.

Today, a lot of LLM output is primarily for human consumption. A human might read around 250 words per minute, which is around 6 tokens per second (250 words/min / (0.75 words/token) / (60 secs/min)). So it might initially seem like there’s little value to generating tokens much faster than this.

But in an agentic workflow, an LLM might be prompted repeatedly to reflect on and improve its output, use tools, plan and execute sequences of steps, or implement multiple agents that collaborate with each other. In such settings, we might easily generate hundreds of thousands of tokens or more before showing any output to a user. This makes fast token generation very desirable and makes slower generation a bottleneck to taking better advantage of existing foundation models.

That’s why I’m excited about the work of companies like @GroqInc, which can generate hundreds of tokens per second. Recently, @SambaNovaAI also published an impressive demo that hit hundreds of tokens per second.

Incidentally, faster, cheaper token generation will also help make running evaluations (evals), a step that can be slow and expensive today since it typically involves iterating over many examples, more palatable. Having better evals will help many developers with the process of tuning models to improve their performance.

Fortunately, it appears that both training and inference are rapidly becoming cheaper. I recently spoke with @CathieDWood and @CCRobertsARK of the investment firm ARK, which is famous for its bullish predictions on tech. They estimate that AI training costs are falling at 75% a year. If they are right, a foundation model that costs $100M to train this year might cost only $25M to train next year. Further, they report that for “enterprise scale use cases, inference costs seem to be falling at an annual rate of ~86%, even faster than training costs.”

I don’t know how accurate these specific predictions will turn out to be, but with improvements in both semiconductors and algorithms, I do see training and inference costs falling rapidly. This will be good for application builders and help AI agentic workflows lift off.

[Original text: https://t.co/BaH6bqZDds ]

关于许多公司渴望更多算力（以及数据）来训练更大的基础模型，人们已经讨论了很多。但我认为，我们用于基础模型推理的算力也远不够用，这一点却常常被低估。

多年前，我在 Google、百度和斯坦福领导团队，致力于扩展深度学习算法。那时，许多半导体制造商、数据中心运营商和学术研究人员都曾问我，如果他们持续提供更多算力，我是否认为 AI 技术会继续高效地利用这些资源。要知道，对于许多日常桌面处理任务，比如运行网页浏览器或文本编辑器，CPU 速度提升到一定程度后，帮助就不大了。那么，我们真的需要越来越快的 AI 处理器来训练越来越大的模型吗？每次我都坚定地回答「是的！」，并鼓励他们继续扩展算力。（有时，我还会半开玩笑地补充一句：我从未遇到过觉得自己算力足够的机器学习工程师。😀）

幸运的是，这个预测到目前为止都是准确的。然而，除了模型训练，我相信在更快、更大规模的推理方面，我们还有巨大的潜力远未被充分挖掘。

如今，大语言模型（LLM）的大部分输出主要是供人类阅读。一个人每分钟大约能阅读 250 个单词，这相当于每秒约 6 个 Token（250 words/min/（0.75 words/token）/（60 secs/min)）。所以，乍一看，如果生成 Token 的速度远超这个值，似乎没有多大意义。

但在 AI 智能体（agentic）的工作流程中，大语言模型可能会被反复提示，用于反思并改进自己的输出、调用工具、规划和执行一系列步骤，或者协同运作多个 AI 智能体。在这种场景下，我们可能在向用户展示任何结果之前，就已经轻松生成了数十万甚至更多的 Token。因此，快速生成 Token 变得极其重要，而生成速度过慢则会成为我们更好利用现有基础模型的瓶颈。

正因如此，我对像 @GroqInc 这样每秒能生成数百个 Token 的公司所做的工作感到非常兴奋。最近，@SambaNovaAI 也展示了一项令人印象深刻的演示，其生成速度同样达到了每秒数百个 Token。

顺带一提，更快、更便宜的 Token 生成也将有助于让运行评估（evals）变得更容易。目前，评估过程可能既缓慢又昂贵，因为它通常需要迭代大量示例。而更好的评估方法将帮助许多开发者优化模型，从而提升其性能。

令人欣慰的是，无论是训练还是推理，其成本似乎都在迅速下降。我最近与投资公司 ARK 的 @CathieDWood 和 @CCRobertsARK 进行了交流，该公司以其对科技行业的乐观预测而闻名。他们估计，AI 训练成本每年下降 75%。如果他们的预测准确，那么今年训练一个花费 1 亿美元的基础模型，明年可能只需 2500 万美元。此外，他们报告称，对于「企业规模的用例，推理成本似乎正以每年约 86% 的速度下降，甚至比训练成本下降得更快。」

我无法判断这些具体预测的准确性如何，但随着半导体和算法的不断进步，我确实看到训练和推理成本正在快速降低。这对应用程序开发者来说是个好消息，也将助力 AI 智能体工作流实现腾飞。

[原文链接：https://t.co/BaH6bqZDds]

### 042

作者: @AndrewYNg
时间: 2024-04-25
链接: https://x.com/AndrewYNg/status/1783588055770886652
互动: Likes: 637; Retweets: 37; Replies: 43; Quotes: 7; Views: 115,255; Bookmarks: 122; isReply: 0

I've really enjoyed using @crewAIInc 's tools to build multiagent AI systems -- in addition to being productive, it's also fun to use! It was great hanging out with its creator @joaomdmoura to chat about best practices for building agentic workflows. https://t.co/IxVeqTqWWj

我非常喜欢使用 @crewAIInc 的工具来构建多智能体（multiagent）AI 系统 —— 这些工具不仅高效，用起来也很有意思！能和它的创建者 @joaomdmoura 聊聊构建 AI 智能体（AI Agent）工作流的最佳实践，真是太棒了。https://t.co/IxVeqTqWWj

### 043

作者: @AndrewYNg
时间: 2024-04-29
链接: https://x.com/AndrewYNg/status/1784977075176374704
互动: Likes: 651; Retweets: 124; Replies: 23; Quotes: 14; Views: 151,458; Bookmarks: 382; isReply: 0

In Prompt Engineering for Vision Models, taught by @anmorgan2414 @JacquesVerre and @KaiserFrose of @Cometml , you’ll learn how to prompt and fine-tune vision models for personalized image generation, image editing, object detection and segmentation. The prompts you'll use for vision models could be text, point coordinates, or bounding boxes, depending on the model. You'll also learn to tune hyperparameters to shape the output.

Models you'll use include Segment-Anything Model (SAM), OWL-ViT, and Stable Diffusion. You'll also learn to fine-tune Stable Diffusion to generate personalized images (say, an image of a specific person), using a handful of images for training. As an example of a multi-step workflow, you'll use OWL-ViT to detect an object based on a text prompt, then pass the bounding box to SAM to create a segmentation mask, and input that mask into Stable Diffusion to replace the original object with a new one based on a text prompt.

Controlling vision models can be tricky; this course will teach prompting and fine-tuning techniques to get precise control over their output. Get started here: https://t.co/7JerpCG9l9

在由 @Cometml 公司的 @anmorgan2414、@JacquesVerre 和 @KaiserFrose 共同讲授的《视觉模型提示工程》课程中，你将学习如何对视觉模型进行提示（prompt）和微调（fine-tune），以实现个性化图像生成、图像编辑、目标检测（object detection）和分割（segmentation）等任务。根据不同的模型，你用于视觉模型的提示可以是文本、点坐标或边界框（bounding box）。你还将学习调整超参数（hyperparameters）来塑造模型的输出。

你将使用的模型包括 Segment-Anything Model（SAM）、OWL-ViT 和 Stable Diffusion。你还将学习如何微调 Stable Diffusion，仅用少量图像进行训练，就能生成个性化图像（比如，特定人物的图像）。作为多步工作流程的一个例子，你将学习如何使用 OWL-ViT 根据文本提示检测一个对象，然后将检测到的边界框传递给 SAM 以创建分割掩膜（segmentation mask），最后将该掩膜输入 Stable Diffusion，根据新的文本提示替换掉原始对象。

控制视觉模型可能颇具挑战性；本课程将教授提示和微调技术，帮助你精准地控制它们的输出。立即开始学习：https://t.co/7JerpCG9l9

### 044

作者: @AndrewYNg
时间: 2024-04-30
链接: https://x.com/AndrewYNg/status/1785152969304068405
互动: Likes: 1,205; Retweets: 104; Replies: 52; Quotes: 12; Views: 147,202; Bookmarks: 122; isReply: 0

Chatting with @GroqInc’s CEO @JonathanRoss321. Groq has super fast token generation capabilities now. And,  I was excited also to hear about his plans to scale up capacity aggressively and also expand this to other models than just LLMs! This is a good time to be building AI applications.

我正在与 GroqInc 的首席执行官 Jonathan Ross（@JonathanRoss321）聊天。Groq 现在具备超快的 Token 生成能力。更让我感到兴奋的是，我听说他计划积极扩大产能，并将这项技术不仅限于大语言模型（LLM），还要扩展到其他模型！这无疑是开发 AI 应用程序的一个绝佳时机。

### 045

作者: @AndrewYNg
时间: 2024-05-02
链接: https://x.com/AndrewYNg/status/1786057567178834328
互动: Likes: 1,267; Retweets: 236; Replies: 32; Quotes: 26; Views: 203,693; Bookmarks: 706; isReply: 0

Inexpensive token generation and agentic workflows for large language models (LLMs) open up intriguing new possibilities for training LLMs on synthetic data. Pretraining an LLM on its own directly generated responses to prompts doesn't help. But if an agentic workflow implemented with the LLM results in higher quality output than the LLM can generate directly, then training on that output becomes potentially useful.

Just as humans can learn from their own thinking, perhaps LLMs can, too. For example, imagine a math student who is learning to write mathematical proofs. By solving a few problems — even without external input — they can reflect on what does and doesn’t work and, through practice, learn how to more quickly generate good proofs.

Broadly, LLM training involves (i) pretraining (learning from unlabeled text data to predict the next word) followed by (ii) instruction fine-tuning (learning to follow instructions) and (iii) RLHF/DPO tuning to align the LLM’s output to human values. Step (i) requires many orders of magnitude more data than the other steps. For example, Llama 3 was pretrained on over 15 trillion tokens, and LLM developers are still hungry for more data. Where can we get more text to train on?

Many developers train smaller models directly on the output of larger models, so a smaller model learns to mimic a larger model’s behavior on a particular task. However, an LLM can’t learn much by training on data it generated directly, just like a supervised learning algorithm can’t learn from trying to predict labels it generated by itself. Indeed, training a model repeatedly on the output of an earlier version of itself can result in model collapse.

However, an LLM wrapped in an agentic workflow may produce higher-quality output than it can generate directly. In this case, the LLM’s higher-quality output might be useful as pretraining data for the LLM itself.
Efforts like these have precedents:
- When using  reinforcement learning to play a game like chess, a model might learn a function that evaluates board positions. If we apply game tree search along with a low-accuracy evaluation function, the model can come up with more accurate evaluations. Then we can train that evaluation function to mimic these more accurate values.
- In the alignment step, Anthropic’s constitutional AI method uses RLAIF (RL from AI Feedback) to judge the quality of LLM outputs, substituting feedback generated by an AI model for human feedback.

A significant barrier to using LLMs prompted via agentic workflows to produce their own training data is the cost of generating tokens. Say we want to generate 1 trillion tokens to extend a pre-existing training dataset. Currently, at publicly announced prices, generating 1 trillion tokens using GPT-4-turbo ($30 per million output tokens), Claude 3 Opus ($75), Gemini 1.5 Pro ($21), and Llama-3-70B on Groq ($0.79) would cost, respectively, $30M, $75M, $21M and $790K. Of course, an agentic workflow that uses a design pattern like Reflection would require generating more than one token per token that we would use as training data. But budgets for training cutting-edge LLMs easily surpass $100M, so spending a few million dollars more for data to boost performance is quite feasible.

That’s why I believe agentic workflows will open up intriguing new opportunities for high-quality synthetic data generation.

[Original text: https://t.co/zOiuUFtmo3 ]

大语言模型（LLM）廉价的 Token 生成能力和 AI 智能体（agentic）工作流，为在合成数据上训练 LLM 带来了许多令人兴奋的新可能。如果只是用 LLM 自己直接生成的响应来预训练它，效果并不理想。但是，如果一个由 LLM 驱动的 AI 智能体工作流能够产生比 LLM 直接生成更高质量的输出，那么利用这些高质量输出进行训练就可能大有裨益。

就像人类可以从自身的思考中学习一样，或许 LLM 也能做到。例如，想象一位正在学习编写数学证明的学生。即使没有外部帮助，他们也可以通过解决一些问题来反思哪些方法有效、哪些无效，并通过不断练习，学会更快地给出优秀的证明。

从宏观上看，LLM 的训练通常包括：（i）预训练（从大量未标注文本数据中学习预测下一个词）；接着是（ii）指令微调（学习理解并遵循指令）；最后是（iii）通过 RLHF/DPO 微调，使 LLM 的输出与人类价值观对齐。其中，步骤（i）所需的数据量要比其他步骤多出几个数量级。例如，Llama 3 就曾在超过 15 万亿个 Token 上进行预训练，而 LLM 开发者们依然对更多数据求贤若渴。那么，我们能从哪里获得更多可用于训练的文本数据呢？

许多开发者会直接用较大模型的输出来训练较小的模型，这样小模型就能学习模仿大模型在特定任务上的行为。然而，LLM 无法通过训练自己直接生成的数据学到多少东西，这就像一个监督学习算法无法通过尝试预测自己生成的标签来学习一样。事实上，如果反复用一个模型早期版本生成的输出来训练它，甚至可能导致模型崩溃。

然而，一个融入了 AI 智能体工作流的 LLM，可能会比它直接生成产生更高质量的输出。在这种情况下，LLM 产生的高质量输出就可以作为 LLM 自身的预训练数据来使用。
这类尝试并非没有先例：
- 在使用强化学习玩国际象棋这类游戏时，模型可能会学习一个用于评估棋盘位置的函数。如果我们结合博弈树搜索和这个精度较低的评估函数，模型就能得出更准确的评估。然后，我们就可以训练该评估函数来学习这些更准确的评估值。
- 在对齐阶段，Anthropic 的宪法 AI 方法就使用了 RLAIF（基于 AI 反馈的强化学习）来判断 LLM 输出的质量，用 AI 模型生成的反馈替代了人类反馈。

利用通过 AI 智能体工作流提示 LLM 来生成自身训练数据的一个主要障碍是生成 Token 的成本。假设我们想生成 1 万亿个 Token 来扩展现有的训练数据集。目前根据公开报价，使用 GPT-4-turbo（每百万输出 Token 30 美元）、Claude 3 Opus（75 美元）、Gemini 1.5 Pro（21 美元）和 Groq 上的 Llama-3-70B（0.79 美元）生成 1 万亿个 Token 的费用将分别高达 3000 万美元、7500 万美元、2100 万美元和 79 万美元。当然，一个采用 Reflection 等设计模式的 AI 智能体工作流，每生成一个我们用作训练数据的 Token，可能需要消耗更多的 Token。但是，训练最先进 LLM 的预算通常会轻易超过 1 亿美元，因此多花几百万美元来获取数据以提升性能，是完全可行的。

正因如此，我相信 AI 智能体工作流将为高质量合成数据生成开辟出激动人心的新机遇。

[原文链接：https://t.co/zOiuUFtmo3]

### 046

作者: @AndrewYNg
时间: 2024-05-05
链接: https://x.com/AndrewYNg/status/1787198521747308637
互动: Likes: 452; Retweets: 96; Replies: 63; Quotes: 15; Views: 112,120; Bookmarks: 134; isReply: 0

I'm glad the Washington Post's editorial board is pushing for governments to engage in exploring climate geoengineering. I believe AI climate modeling has an important role to play. 

Here's the situation as I see it:
- Earth is on track to a catastrophic 2-4 degrees Celsius of warming. The article references the UN Environment Program's estimate of 2.9 degrees on the current trajectory.
- We have a high degree of confidence that geoengineering via stratospheric aerosol injection (SAI) will significantly lower Earth's average surface temperature. The science here is really solid: Use aerosols in the atmosphere to reflect more sunlight away from earth, and we become cooler.
- So, why don't we just do it? Multiple reasons, but the biggest is that we still don't have good models for estimating how it will affect local climate and weather patterns, even though we're confident global average surface temperature will go down. 

That's why better AI climate modeling is crucial for reducing uncertainty and better understanding the impacts of various geoengineering strategies.

There're other issues to consider too, like governance, moral hazard (disincentivizing decarbonization), equity,  pollution from the aerosols, and the challenging implementation engineering. But many of these  problems become easier if we can make progress on the core problem of better understanding what impact SAI will have.

我很高兴看到《华盛顿邮报》编辑委员会正在积极倡导各国政府参与探讨气候地球工程（geoengineering）。我相信， AI 气候建模（AI climate modeling）在其中能发挥举足轻重的作用。

在我看来，目前的情况是这样的：
- 地球正朝着灾难性的 2-4 摄氏度升温轨迹发展。根据文章引述的联合国环境规划署（UN Environment Program）估算，按当前趋势，全球气温将上升 2.9 摄氏度。
- 我们高度确信，通过平流层气溶胶注入（stratospheric aerosol injection，SAI）进行地球工程，能够显著降低地球的平均地表温度。这背后的科学原理非常坚实：在大气中喷洒气溶胶，将更多阳光反射回太空，从而使地球降温。
- 既然如此，我们为何不直接付诸实践呢？原因有很多，但最主要的一点是，尽管我们确信全球平均地表温度会下降，但我们仍然缺乏可靠的模型来准确预测它将如何影响局部气候和天气模式。

因此，为了减少不确定性，更好地理解各种地球工程策略可能带来的影响，开发更先进的 AI 气候建模技术显得至关重要。

当然，我们还需要考虑其他一系列问题，包括治理、道德风险（即可能削弱人们对脱碳（decarbonization）的积极性）、公平性、气溶胶本身可能造成的污染，以及实施工程的巨大挑战。然而，如果我们能在更好地理解 SAI 会产生何种影响这一核心问题上取得突破，许多上述问题都将迎刃而解。

### 047

作者: @AndrewYNg
时间: 2024-05-05
链接: https://x.com/AndrewYNg/status/1787199044194070776
互动: Likes: 45; Retweets: 5; Replies: 6; Quotes: 0; Views: 26,866; Bookmarks: 5; isReply: 1

Link to original article:  https://t.co/9CEoDsWYgh

在 Microsoft、OpenAI 和 Amazon [20] 最近发表的一篇文章中，研究人员展示了如何让大语言模型（LLM）通过控制自己的开关来「休眠」和「唤醒」。具体来说，他们引入了一种机制，让大语言模型能够自行决定进入低功耗的「休眠」状态，从而降低计算成本，然后在需要执行任务时再「唤醒」。这对 AI 来说，就好比人类决定何时休息、何时活动一样。

图 1：具有休眠和唤醒功能的大语言模型智能体（LLM agent）的概念图。

### 048

作者: @AndrewYNg
时间: 2024-05-05
链接: https://x.com/AndrewYNg/status/1787204296590987630
互动: Likes: 230; Retweets: 10; Replies: 3; Quotes: 0; Views: 46,321; Bookmarks: 51; isReply: 1

I'm with @JeffDean on this. DistBelief taught us early important lessons about scaling up deep learning, and it was general enough for many algorithms including supervised backprop. 

Obviously, we got a lot of software and hardware architecture details "wrong" back in 2012 -- but who didn't? But DistBelief was used by numerous teams within Google, taught early lessons about scaling deep learning, and became the precursor to TensorFlow. 

Fun fact: Back then, "Deep Belief Networks" (by Geoff Hinton) was a popular algorithm. When we built our Distributed training system, it was Jeff that came up with the name DistBelief, which I thought was a real groaner. I guess we were hoping our results would be so good that people would look at them with disbelief. 😀

关于这一点，我赞同 Jeff Dean 的看法。DistBelief 教会了我们扩展（scaling up）深度学习（deep learning）的早期重要经验，而且它足够通用，能支持包括监督反向传播（supervised backprop）在内的多种算法。

当然，我们回望 2012 年，当时在许多软件和硬件架构细节上确实犯了不少「错误」—— 但谁又不是呢？不过，DistBelief 当时被 Google 内部的许多团队广泛使用，积累了扩展深度学习的早期经验，并成为了 TensorFlow 的前身。

一个趣闻是：那时，「深度信念网络」(Deep Belief Networks）（由 Geoff Hinton 提出）是一种很流行的算法。当我们构建分布式训练系统时，是 Jeff 提出了 DistBelief 这个名字，我当时觉得这名字听起来真是个「冷笑话」。我想，我们大概是希望我们的研究成果能好到让人们难以置信吧。😀

### 049

作者: @AndrewYNg
时间: 2024-05-05
链接: https://x.com/AndrewYNg/status/1787209990023082105
互动: Likes: 19; Retweets: 0; Replies: 1; Quotes: 3; Views: 4,677; Bookmarks: 0; isReply: 1

@unJADded @JeffDean @ylecun @deliprao @karpathy You were a real pioneer @unJADded ! ❤️

Looking back, honestly I feel a bit bad at how hard DistBelief was to use, and the complexity of the C++ interface we built.... Nonetheless, I'm glad it turned out to be a useful product of its time!

@unJADded @JeffDean @ylecun @deliprao @karpathy @unJADded 你真是一位真正的先驱！ ❤️

回想起来，说实话，我有点抱歉 DistBelief 用起来那么困难，还有我们当年构建的 C++ 接口是如此复杂…… 尽管如此，我还是很欣慰它最终成为了那个时代的一项有用成果！

### 050

作者: @AndrewYNg
时间: 2024-05-05
链接: https://x.com/AndrewYNg/status/1787216859621958078
互动: Likes: 52; Retweets: 3; Replies: 3; Quotes: 1; Views: 14,228; Bookmarks: 6; isReply: 1

@quocleix @ylecun @JeffDean @deliprao @karpathy Yup. By the way @quocleix, I still remember the time we were both in the office, and you waved at me to come over to your desk to look at your new result. And right there on your monitor was the now-famous Google Cat image. That was a defining moment for Google Brain!

@quocleix @ylecun @JeffDean @deliprao @karpathy 是的，没错。顺便提一下，@quocleix，我仍然清楚地记得，当时我们都在办公室，你向我招手示意我到你的办公桌旁，看看你的最新研究成果。就在你的显示器上，赫然显示着如今已家喻户晓的 Google Cat 图像。那对于 Google Brain 来说，真是一个标志性的决定性时刻！

### 051

作者: @AndrewYNg
时间: 2024-05-05
链接: https://x.com/AndrewYNg/status/1787219405916828001
互动: Likes: 4; Retweets: 0; Replies: 1; Quotes: 0; Views: 798; Bookmarks: 1; isReply: 1

Back then, the idea that scaling deep learning would lead to significant performance gains was controversial. Several senior academic colleagues were advising me not to waste time trying to scale deep learning, but to just focus on inventing new algorithms, which was where they thought the action was! 

Fortunately, I already had small scale data from my Stanford group (thanks to @adampaulcoates, @honglaklee, and many others) that gave me conviction that scaling was going to work, and we just kept pushing in that direction.

回溯到那时，深度学习（deep learning）的规模化（scaling）能带来显著性能提升的观点备受争议。有几位资深的学术同事劝我，别把时间浪费在尝试扩大深度学习的规模上，而应该专注于发明新算法，他们认为那才是关键所在！

幸运的是，我当时已经从我的斯坦福团队那里获得了小规模的数据（感谢 @adampaulcoates、@honglaklee 和许多其他人），这让我坚信规模化是行得通的。于是，我们便持续朝着这个方向努力。

### 052

作者: @AndrewYNg
时间: 2024-05-06
链接: https://x.com/AndrewYNg/status/1787525611864695148
互动: Likes: 1,174; Retweets: 191; Replies: 22; Quotes: 15; Views: 197,942; Bookmarks: 745; isReply: 0

Have you used quantization with an open source machine learning library, and wondered how quantization works? How can you preserve model accuracy as you compress from 32 bits to 16, 8, or even 2 bits? In our new short course, Quantization in Depth, taught by @huggingface's @_marcsun and @younesbelkada, you'll learn to implement variants of linear quantization, such as asymmetric and symmetric modes, from scratch. You'll also quantize at different granularities (per-tensor, per-channel, per-group) to maintain performance. You’ll then construct a quantizer to compress any open source deep learning model’s dense layers to 8-bit precision. Finally, you’ll practice quantizing weights into 2 bits by packing four 2-bit weights into a single 8-bit integer.

If you've ever run a large open source model on your laptop, you've likely benefited from someone's work in quantization. Come learn how this key technique works under the hood!

Please sign up here: https://t.co/lPfRY0LdFI

您是否曾在开源机器学习库中尝试过 ** 量化 **（quantization），并好奇它究竟是如何工作的？当您需要将模型从 32 位压缩到 16 位、8 位甚至低至 2 位时，该如何确保模型的准确性不打折扣呢？在我们的新短期课程《深度量化》（Quantization in Depth）中，您将跟随 @huggingface 的 @_marcsun 和 @younesbelkada 两位老师，学习从零开始亲手实现各种线性量化方式，例如 ** 非对称模式 **（asymmetric mode）和 ** 对称模式 **（symmetric mode）。您还将掌握如何在不同的 ** 粒度 **（granularity）下进行量化（例如按张量 per-tensor、按通道 per-channel、按组 per-group），以保持模型的性能。接着，您将动手构建一个量化器，将任何开源深度学习模型的 ** 密集层 **（dense layers）压缩到 8 位精度。最后，您还将实践如何将 ** 权重 **（weights）量化到 2 位，具体做法是将四个 2 位权重「打包」到一个 8 位整数中。

如果您曾在自己的笔记本电脑上运行过大型开源模型，那么很可能已经受益于他人所做的量化工作。快来深入了解这项关键技术的底层工作原理吧！

请在此处注册：https://t.co/lPfRY0LdFI

### 053

作者: @AndrewYNg
时间: 2024-05-08
链接: https://x.com/AndrewYNg/status/1788246239517282795
互动: Likes: 1,247; Retweets: 227; Replies: 24; Quotes: 21; Views: 296,183; Bookmarks: 969; isReply: 0

I’m excited to kick off the first of our short courses focused on agents, starting with Building Agentic RAG with LlamaIndex, taught by @jerryjliu0, CEO of @llama_index.

This covers an important shift in RAG (retrieval augmented generation), in which rather than having the developer write explicit routines to retrieve information to feed into the LLM context, we instead build a RAG agent that that has access to tools for retrieving information. This lets the agent decide what information to fetch, and enables it to answer more complex questions using multi-step reasoning.

In detail, you'll learn about:
- Routing: Where your agent will use decision-making to route requests to multiple tools.
- Tool Use: Where you'll create an interface for agents to select what tool (function call) to use as well as generate the right arguments.
- Multi-step reasoning with tool use: Where you'll use an LLM to carry out multiple steps of reasoning, while retaining memory throughout the process.

You’ll also learn how to step through what your agent is doing to debug and improve it iteratively.

It’s an exciting time to build agents. Sign up and get started here! https://t.co/sHhzRRJG0l

我很高兴地宣布，我们首个专注于 AI 智能体（Agent）的短期课程即将开课，课程主题是「Building Agentic RAG with LlamaIndex」，由 @llama_index 的首席执行官 @jerryjliu0 亲自授课。

本次课程将深入探讨 RAG（检索增强生成，Retrieval Augmented Generation）领域的一个重要转变。过去，开发者需要编写明确的例程来检索信息，并将其提供给大语言模型（Large Language Model）的上下文。而现在，我们将构建一个 RAG AI 智能体，它能够自行访问各种工具来检索信息。这使得 AI 智能体可以自主决定获取哪些信息，并通过多步推理来回答更复杂的问题。

具体来说，您将学习以下内容：
- 路由（Routing)：您的 AI 智能体将运用其决策能力，将请求路由到不同的工具。
- 工具使用（Tool Use)：您将为 AI 智能体创建一个接口，使其能够选择要使用的工具（函数调用），并生成正确的参数。
- 结合工具使用的多步推理（Multi-step reasoning with tool use)：您将学习如何利用大语言模型执行多步推理，并在此过程中保持记忆。

您还将学习如何逐步跟踪 AI 智能体的运行过程，以便进行迭代调试和持续改进。

这是一个构建 AI 智能体的激动人心的时代。立即注册，开始您的学习之旅吧：https://t.co/sHhzRRJG0l

### 054

作者: @AndrewYNg
时间: 2024-05-09
链接: https://x.com/AndrewYNg/status/1788648531873628607
互动: Likes: 1,137; Retweets: 253; Replies: 81; Quotes: 51; Views: 290,058; Bookmarks: 244; isReply: 0

Last week, I spoke about AI and regulations at an event at the U.S. Capitol attended by legislative and business leaders. I’m encouraged by the progress the open source community has made fending off regulations that would have stifled innovation. But opponents of open source are continuing to shift their arguments, with the latest worries centering on open source's impact on national security. I hope we’ll all keep protecting open source!

Based on my conversations with legislators, I’m encouraged by the progress the U.S. federal government has made getting a realistic grasp of AI’s risks. To be clear, guardrails are needed. But they should be applied to AI applications, not to general-purpose AI technology.

Nonetheless, some companies are eager to limit open source, possibly to protect the value of massive investments they’ve made in proprietary models and to deter competitors. It has been fascinating to watch their arguments change over time.

For instance, about 12 months ago, the Center For AI Safety’s “Statement on AI Risk” warned that AI could cause human extinction and stoked fears of AI taking over. This alarmed leaders in Washington. But many people in AI pointed out that this dystopian science-fiction scenario had little basis in reality. About six months later, when I testified at the U.S. Senate’s AI Insight forum, legislators no longer worried much about an AI takeover.

Then the opponents of open source shifted gears. Their leading argument shifted to the risk of AI helping to create bioweapons. Soon afterward, OpenAI and RAND showed that current AI does not significantly increase the ability of malefactors to build bioweapons. This fear of AI-enabled bioweapons has diminished. To be sure, the possibility that bad actors could use bioweapons — with or without AI — remains a topic of great international concern.

The latest argument for blocking open source AI has shifted to national security. AI is useful for both economic competition and warfare, and open source opponents say the U.S. should make sure its adversaries don’t have access to the latest foundation models. While I don’t want authoritarian governments to use AI, particularly to wage unjust wars, the LLM cat is out of the bag, and authoritarian countries will fill the vacuum if democratic nations limit access. When, some day, a child asks an AI system questions about democracy, the role of a free press, or the function of an independent judiciary in preserving the rule of law, I would like the AI to reflect democratic values rather than favor authoritarian leaders’ goals over, say, human rights.

I came away from Washington optimistic about the progress we’ve made. A  year ago, legislators seemed to me to spend 80% of their time talking about guardrails for AI and 20% about investing in innovation. I was delighted that the ratio has flipped, and there was far more talk of investing in innovation.
Looking beyond the U.S. federal government, there are many jurisdictions globally. Unfortunately, arguments in favor of  regulations that would stifle AI development continue to proliferate. But I’ve learned from my trips to Washington and other nations’ capitals that talking to regulators does have an impact. If you have a chance to talk to a regulator at any level, I hope you’ll do what you can to help governments better understand AI.

[Original text (with links): https://t.co/tw2iT0ooLT ]

上周，我在美国国会大厦参加了一场由立法和商业领袖出席的活动，并在会上讨论了人工智能（AI）及其监管问题。令我感到鼓舞的是，开源社区在抵制那些可能扼杀创新的监管方面取得了显著进展。然而，开源的反对者们正不断调整他们的论点，目前最新的担忧主要集中在开源对国家安全可能造成的影响上。我希望我们所有人都能继续保护开源！

根据我与立法者的交流，美国联邦政府在切实理解 AI 风险方面所取得的进展也让我备受鼓舞。需要明确的是，保障措施确实是必需的。但这些措施应该应用于 AI 应用程序本身，而不是针对通用的 AI 技术。

尽管如此，一些公司仍然急于限制开源，这可能是为了保护他们在专有模型上投入的巨额资金价值，并借此阻止竞争对手。观察他们的论点如何随着时间推移而变化，一直令人着迷。

例如，大约 12 个月前，人工智能安全中心（Center For AI Safety）的《AI 风险声明》（Statement on AI Risk）曾警告 AI 可能导致人类灭绝，并加剧了人们对 AI 接管世界的恐慌。这震惊了华盛顿的领导人。但许多 AI 领域的专业人士指出，这种反乌托邦式的科幻场景缺乏现实基础。大约六个月后，当我出席美国参议院的 AI 洞察论坛作证时，立法者们已经不再那么担心 AI 接管的问题了。

随后，开源的反对者们改变了论调。他们的主要论点转向了 AI 可能帮助制造生物武器的风险。此后不久，OpenAI 和 RAND 的研究表明，当前的 AI 并未显著增加不法分子制造生物武器的能力。这种对 AI 驱动的生物武器的恐惧已经减弱。当然，恶意行为者可能使用生物武器 —— 无论是否有 AI 辅助 —— 这仍然是一个受到国际社会高度关注的话题。

目前，阻碍开源 AI 的最新论点已经转向国家安全。AI 对于经济竞争和军事战争都非常有用，开源的反对者声称美国应该确保其对手无法获取最新的基础模型。虽然我不希望威权政府使用 AI，尤其是发动非正义的战争，但是大语言模型（LLM）的发展已势不可挡。如果民主国家限制访问，威权国家反而会填补这一空白。总有一天，当一个孩子向 AI 系统提问关于民主、自由媒体的作用，或者独立司法机构在维护法治中的功能时，我希望 AI 能反映民主价值观，而不是偏袒威权领导人的目标，使其凌驾于人权（例如）之上。

我从华盛顿回来时，对我们所取得的进展感到乐观。一年前，在我看来，立法者似乎将 80% 的时间花在讨论 AI 的保障措施上，而只有 20% 的时间用于投资创新。我很高兴这个比例已经发生了转变，现在更多地是在讨论投资创新。
放眼美国联邦政府之外，全球还有许多司法管辖区。不幸的是，支持出台扼杀 AI 发展的监管措施的论点仍在持续存在。但我从华盛顿和其他国家首都的访问中了解到，与监管机构对话确实能产生影响。如果你有机会与任何级别的监管机构交谈，我希望你尽力帮助政府更好地理解 AI。

[原文链接： https://t.co/tw2iT0ooLT]

### 055

作者: @AndrewYNg
时间: 2024-05-13
链接: https://x.com/AndrewYNg/status/1790050852776112439
互动: Likes: 836; Retweets: 179; Replies: 19; Quotes: 9; Views: 103,888; Bookmarks: 531; isReply: 0

New short course: Building Multimodal Search and RAG", by @weaviate_io's  @sebawita.

Contrastive learning is used to train models to map vectors into an embedding space by pulling similar concepts closer together and pushing dissimilar concepts away from each other. This technique is also used to train multimodal embedding models that capture semantic similarity across different modalities like text, images, and audio. These multimodal embeddings can be used to build multimodal search and RAG systems.

In this course, you'll learn how contrastive learning works, and how to add multimodality to RAG – so your models can draw on diverse, relevant context to answer questions. For example, a query about a financial report might synthesize information from text snippets, graphs, tables, and slides. You will also learn how visual instruction tuning lets you integrate image understanding into language models, and build a multi-vector recommender system using Weaviate’s open-source vector database.

Please sign up here: https://t.co/IVULLqbdOD

新短期课程：《构建多模态搜索和 RAG》，由 @weaviate_io 的 @sebawita 主讲。

对比学习（Contrastive learning）是一种训练模型的方法，它通过拉近相似概念的向量并推远不相似概念的向量，从而将它们映射到一个嵌入空间（embedding space）中。这项技术也被用于训练多模态嵌入模型，这些模型能够捕捉文本、图像和音频等不同模态之间的语义相似性。利用这些多模态嵌入，我们可以构建多模态搜索和检索增强生成（RAG）系统。

在本课程中，你将学习对比学习的工作原理，以及如何为 RAG 引入多模态能力 —— 这样你的模型就能利用多样化且相关的上下文来回答问题。例如，当查询一份财务报告时，模型可以综合文本片段、图表、表格和幻灯片中的信息。你还将学习视觉指令微调（visual instruction tuning）如何将图像理解能力整合到大语言模型中，并使用 Weaviate 的开源向量数据库构建一个多向量推荐系统。

请在此处注册：https://t.co/IVULLqbdOD

### 056

作者: @AndrewYNg
时间: 2024-05-13
链接: https://x.com/AndrewYNg/status/1790088683259048120
互动: Likes: 1,934; Retweets: 222; Replies: 46; Quotes: 7; Views: 184,926; Bookmarks: 158; isReply: 0

Congrats to OpenAI for the release of GPT-4o! 2x faster and 50% cheaper tokens will be great for everyone using agentic AI workflows. 

When an agentic job that used to take 10min now takes 5min just by switching APIs, that's great progress!

恭喜 OpenAI 发布 GPT-4o！速度提升两倍、token 价格降低 50%，这对所有使用 AI 智能体（Agentic AI）工作流的用户来说都将是重大利好。

如果一个 AI 智能体任务过去需要 10 分钟，现在仅仅通过切换 API 就能在 5 分钟内完成，那无疑是巨大的进步！

### 057

作者: @AndrewYNg
时间: 2024-05-14
链接: https://x.com/AndrewYNg/status/1790500978279776450
互动: Likes: 1,061; Retweets: 72; Replies: 36; Quotes: 6; Views: 112,230; Bookmarks: 68; isReply: 0

Congratulations to all my Google friends for the cool announcements at I/O! 

I'm personally looking forward to Gemini with 2 million token input context window and better support for on-device AI -- should open up new opportunities for application builders!

恭喜我所有的谷歌朋友们在 I/O 大会上的精彩发布！

我个人非常期待拥有 200 万 token 输入上下文窗口的 Gemini，以及对设备端 AI（on-device AI）的更好支持 —— 这应该会为应用开发者们开启新的机遇！

### 058

作者: @AndrewYNg
时间: 2024-05-15
链接: https://x.com/AndrewYNg/status/1790769732146307308
互动: Likes: 1,490; Retweets: 278; Replies: 85; Quotes: 46; Views: 348,115; Bookmarks: 1,255; isReply: 0

New agentic short course! Multi AI Agent Systems with crewAI, built with @crewAIInc's founder and CEO @joaomdmoura. In this course, you'll learn how to break down complex tasks into subtasks for multiple AI agents, each playing a specialized role, to execute. 

For example, to generate a research report, you might have researcher, writer, and quality assurance agents collaborate. You'll define the roles, expectations, and interactions between the agents—like a manager organizing a team.

You'll work with key agentic AI techniques like role-playing, tool use, memory, guardrails, and cross-agent collaboration. And you'll build your own multi-agent systems that can tackle complex tasks. I think you'll find it both productive and fun to design agents and watch them collaborate to get things done.

Let me know what you think! I believe multi-agent architectures will drive significant progress in AI systems.

Please sign up here! https://t.co/0rObe4feBz

重磅推出全新基于智能体的短期课程！与 @crewAIInc 的创始人兼 CEO @joaomdmoura 共同打造的 Multi AI Agent Systems with crewAI。在本课程中，你将学习如何将复杂任务分解为多个子任务，并分配给不同的 AI 智能体（AI Agent）来执行，每个智能体都扮演着专业的角色。

例如，为了生成一份研究报告，你可能需要让研究员、作者和质量保证智能体相互协作。你将定义这些智能体之间的角色、预期行为以及它们如何互动 —— 就像一位经理在组织一个团队。

你将接触并运用关键的智能体 AI 技术，例如角色扮演（role-playing）、工具使用（tool use）、记忆（memory）、护栏（guardrails）以及跨智能体协作（cross-agent collaboration）。你还将亲手构建自己的多智能体系统，这些系统能够应对各种复杂任务。我相信你会发现设计智能体并看着它们协同工作来完成任务，既富有成效又充满乐趣。

期待听到你的想法！我相信多智能体架构将为 AI 系统带来突破性的进展。

请在此处注册！https://t.co/0rObe4feBz

### 059

作者: @AndrewYNg
时间: 2024-05-16
链接: https://x.com/AndrewYNg/status/1791134037178020308
互动: Likes: 2,873; Retweets: 553; Replies: 74; Quotes: 66; Views: 505,103; Bookmarks: 2,067; isReply: 0

This week, Google announced a doubling of Gemini Pro 1.5's input context window from 1 million to 2 million tokens, and OpenAI released GPT-4o, which generates tokens 2x faster and 50% cheaper than GPT-4 Turbo and natively accepts and generates multimodal tokens. I view these developments as the latest in an 18-month trend. Given the improvements we've seen, best practices for developers have changed as well.

Since the launch of ChatGPT in Nov 2022, with key milestones that include the releases of GPT-4, Gemini 1.5 Pro, Claude 3 Opus, and Llama 3-70B, many model providers have improved their capabilities in two important ways: (i) reasoning, which allows LLMs to think through complex concepts and and follow complex instructions; and (ii) longer input context windows. 

The reasoning capability of GPT-4 and other advanced models makes them quite good at interpreting complex prompts with detailed instructions. Many people are used to dashing off a quick, 1- to 2-sentence query to an LLM. In contrast, when building applications, I see sophisticated teams frequently writing prompts that might be 1 to 2 pages long (my teams call them “mega-prompts”) that provide complex instructions to specify in detail how we’d like an LLM to perform a task. I still see teams not going far enough in terms of writing detailed instructions. For an example of a moderately lengthy prompt, take a look at Claude 3’s system prompt. It’s detailed and gives clear guidance on how Claude should behave. 

This is a very different style of prompting than we typically use with LLMs’ web user interfaces, where we might dash off a quick query and, if the response is unsatisfactory, clarify what we want through repeated conversational turns with the chatbot.

Further, the increasing length of input context windows has added another technique to the developer’s toolkit. GPT-3 kicked off a lot of research on few-shot in-context learning. For example, if you’re using an LLM for text classification, you might give a handful — say 1 to 5 examples — of text snippets and their class labels, so that it can use those examples to generalize to additional texts. However, with longer input context windows — GPT-4o accepts 128,000 input tokens, Claude 3 Opus 200,000 tokens, and Gemini 1.5 Pro 1 million tokens (2 million just announced in a limited preview) — LLMs aren’t limited to a handful of examples. With many-shot learning, developers can give dozens, even hundreds of examples in the prompt, and this works better than few-shot learning. 

When building complex workflows, I see developers getting good results with this process: 
- Write quick, simple prompts and see how it does.
- Based on where the output falls short, flesh out the prompt iteratively. This often leads to a longer, more detailed, prompt, perhaps even a mega-prompt.
- If that’s still insufficient, consider few-shot or many-shot learning (if applicable) or, less frequently, fine-tuning.
- If that still doesn’t yield the results you need, break down the task into subtasks and apply an agentic workflow.

I hope a process like this will help you build applications more easily. If you’re interested in taking a deeper dive into prompting strategies, I recommend Microsoft's Medprompt paper (Nori et al., 2023), which lays out a complex set of prompting strategies that can lead to very good results.

[Original text (with links): https://t.co/UOtLDza1Vh ]

本周，Google 宣布将 Gemini Pro 1.5 的输入上下文窗口（input context window）容量翻倍，从 100 万个 Token 增加到 200 万个 Token ；同时，OpenAI 发布了 GPT-4o，它的 Token（Token）生成速度是 GPT-4 Turbo 的 2 倍，成本降低 50%，并且能够原生支持多模态（multimodal）Token 的输入和生成。我认为这些发展是过去 18 个月趋势的最新体现。鉴于我们所见的这些进步，开发人员的最佳实践（best practices）也随之发生了改变。

自 2022 年 11 月 ChatGPT 发布以来，随着 GPT-4、Gemini 1.5 Pro、Claude 3 Opus 和 Llama 3-70B 等重要里程碑的推出，许多模型提供商在两个关键方面提升了其能力：(i）推理（reasoning）能力，这使得大语言模型（LLM）能够处理复杂概念并遵循复杂指令；(ii）更长的输入上下文窗口。

GPT-4 及其他先进模型的推理能力，使其在理解带有详细说明的复杂提示（prompt）方面表现出色。许多人习惯于向大语言模型随意发出 1 到 2 句话的简短查询。然而，在构建应用程序时，我发现专业的团队经常会编写长达 1 到 2 页的提示 （我的团队称之为「巨型提示」），这些提示提供了复杂的指令，详细地说明了我们希望大语言模型如何执行某项任务。但我发现仍有团队在编写详细指令时未能充分发挥其潜力。例如，如果想了解一个中等长度的提示，可以参考 Claude 3 的系统提示。它非常详细，并就 Claude 应如何表现提供了清晰的指导。

这与我们通常在大语言模型的网页用户界面中使用的提示风格截然不同，在网页界面中，我们可能会快速提出一个问题，如果回复不尽如人意，就会通过与聊天机器人反复对话来澄清我们的意图。

此外，输入上下文窗口长度的增加为开发人员的工具箱增添了一项新技术。GPT-3 催生了大量关于少样本（Few-shot）上下文学习（in-context learning）的研究。例如，如果你正在使用大语言模型进行文本分类，你可能会提供少量 —— 比如 1 到 5 个例子 —— 的文本片段及其对应的类别标签，这样模型就可以利用这些例子来推断或应用于其他文本。然而，随着输入上下文窗口的不断加长 ——GPT-4o 支持 128,000 个输入 Token ，Claude 3 Opus 支持 200,000 个 Token ，而 Gemini 1.5 Pro 支持 100 万个 Token （最近宣布在有限预览版中达到 200 万个）—— 大语言模型不再仅限于提供少量例子。通过多样本（many-shot）学习，开发人员可以在提示中给出几十甚至数百个例子，并且这种方法通常比少样本学习效果更好。

在构建复杂工作流时，我发现开发人员通过以下流程能获得良好效果：
- 先编写快速、简单的提示，观察其表现。
- 根据输出的不足之处，迭代地充实和完善提示。这通常会形成一个更长、更详细的提示，甚至可能是一个巨型提示。
- 如果这仍然不够，可以考虑采用少样本或多样本学习 （如果适用），或者，不那么频繁地，进行微调（fine-tuning）。
- 如果依然未能获得所需结果，则将任务分解为子任务，并采用 AI 智能体（AI Agent）工作流。

我希望这样的流程能帮助你更轻松地构建应用程序。如果你有兴趣深入探索提示策略，我推荐阅读 Microsoft 的 Medprompt 论文（Nori et al.，2023），该论文提出了一套复杂的提示策略，能够带来非常好的结果。

[原文链接（包含链接)：https://t.co/UOtLDza1Vh ]

### 060

作者: @AndrewYNg
时间: 2024-05-21
链接: https://x.com/AndrewYNg/status/1792919935691214899
互动: Likes: 981; Retweets: 199; Replies: 34; Quotes: 14; Views: 112,667; Bookmarks: 508; isReply: 0

Learn to deploy AI models to edge devices in our new short course Introduction to On-Device AI, created with @Qualcomm and taught by Senior Director of Engineering @krishna_srd.

I think on-device (edge) AI is an important technology trend that's enabling new low latency, privacy-preserving applications. In this course, you'll deploy a real-time image segmentation model on-device, and through this learn key steps for on-device deployment: Neural Network graph capture, on-device compilation, hardware acceleration, and validating on-device numerical correctness. You'll also see how quantization can make your model up to 4x faster and 4x smaller, and thereby improve its performance on resource-constrained edge devices.

The techniques covered are used to deploy models on numerous device types including smartphones, drones, and robots, and are enabling many new, creative applications. 

Please sign up here: https://t.co/V4mS6E7dXx

在我们的全新短期课程《On-Device AI 介绍》中，你将学习如何将 AI 模型部署到边缘设备。本课程由 Qualcomm 联合打造，并由工程高级总监 Krishna Sarda 亲自授课。

我认为设备端 AI（On-Device AI）或称为边缘 AI（Edge AI）是一个重要的技术趋势，它正在赋能许多低延迟、注重隐私的应用。在本课程中，你将亲手部署一个实时图像分割模型到设备端，并通过这个过程掌握设备端部署的关键步骤：神经网络图捕获（Neural Network graph capture）、设备端编译（on-device compilation）、硬件加速（hardware acceleration），以及验证设备端数值正确性（on-device numerical correctness）。你还将了解到量化（quantization）技术如何能让你的模型速度提升 4 倍，同时体积缩小 4 倍，从而显著提升模型在资源受限的边缘设备上的性能。

课程中涵盖的技术广泛应用于包括智能手机、无人机和机器人在内的多种设备类型上部署 AI 模型，并正在催生许多新颖、富有创意的应用。

请在此处注册：https://t.co/V4mS6E7dXx

### 061

作者: @AndrewYNg
时间: 2024-05-21
链接: https://x.com/AndrewYNg/status/1792986667852374386
互动: Likes: 11; Retweets: 2; Replies: 2; Quotes: 0; Views: 2,076; Bookmarks: 0; isReply: 1

Thank you! It’s been a privilege for Landing AI to work with you @RamaswmySridhar, 
@jeffhollan, and the whole Snowflake team. Many businesses have a lot of image data, and integrating our vision software to run as a native app in Snowpark Container Services makes it easy for users to get insights out of their vision data stored in Snowflake. @danmaloney and I also look forward to seeing you at the Summit!

谢谢！Landing AI 很荣幸能与 @RamaswmySridhar、@jeffhollan 以及整个 Snowflake 团队合作。许多企业都拥有海量的图像数据，而我们将视觉软件集成到 Snowpark Container Services 中，使其能作为原生应用运行，这让用户可以轻松地从存储在 Snowflake 中的视觉数据里获取有价值的洞察。@danmaloney 和我也期待能在峰会（Summit）上与您见面！

### 062

作者: @AndrewYNg
时间: 2024-05-23
链接: https://x.com/AndrewYNg/status/1793673520863715396
互动: Likes: 897; Retweets: 141; Replies: 38; Quotes: 12; Views: 91,383; Bookmarks: 281; isReply: 0

A good way to get started in AI is to start with coursework, which gives a systematic way to gain knowledge, and then to work on projects. For many who hear this advice, “projects” may evoke a significant undertaking that delivers value to users. But I encourage you to set a lower bar and relish small, weekend tinkering projects that let you learn, even if they don’t result in a meaningful deliverable.

Recently, my son and daughter (ages 3 and 5) were building Lego vehicles. They built a beautiful ice-cream truck as well as a . . . umm . . . colorful and asymmetric dinosaur car, shown in the picture below. While most observers would judge the ice-cream truck as the superior creation, my kids built it by following Lego’s instructions, and it is likely identical to thousands of ice-cream trucks built by others. In contrast, building the dinosaur car required creativity and novel thinking. The exercise helped them hone their ability to pick and assemble Lego building blocks.

There is, of course, room for both mimicking others’ designs (with permission) and coming up with your own. As a parent, I try to celebrate both. (To be honest, I celebrated the dinosaur car more.) When learning to build Lego, it’s helpful to start by following a template. But eventually, building your own unique projects enriches your skills.

As a developer, too, I try to celebrate unique creations. Yes, it is nice to have beautiful software, and the impact of the output does matter. But good software is often written by people who spend many hours tinkering and building things. By building unique projects, you master key software building blocks. Then, using those blocks, you can go on to build bigger projects

I routinely tinker with building AI applications, and a lot of my tinkering doesn’t result in anything useful. My latest example: I built a Streamlit app that would authenticate to Google docs, read the text in a doc, use a large language model to edit my text, and write the result back into the doc. I didn’t find it useful in the end because of friction in the user interface, and I’m sure a commercial provider will soon, if they haven’t already, build a better product than I was able to throw together in a couple of hours on a weekend. But such tinkering helps me hone my intuition and master software components (I now know how to programmatically interface with Google docs) that might be useful in future projects.

If you have an idea for a project, I encourage you to build it! Often, working on a project will also help you decide what additional skills to learn, perhaps through coursework. To sustain momentum, it helps to find friends with whom to talk about ideas and celebrate projects — large or small.

[Original text: https://t.co/i21oCaQpDc ]

想要迈入 AI 领域，一个很好的开始方式是学习相关课程，这能帮你系统地积累知识，随后便是着手实践项目。很多人听到「项目」这个词，脑海中可能会浮现出那些能为用户创造价值的、意义重大的工作。但我鼓励你放低标准，尽情投入那些小型的、利用周末时间修修补补的项目，它们能让你从中学习，即使最终没有产生什么「拿得出手」的成果。

最近，我的儿子和女儿（分别为 3 岁和 5 岁）正在搭建乐高玩具。他们拼出了一辆漂亮的冰淇淋车，还有一辆…… 嗯…… 造型独特、色彩鲜艳且不对称的恐龙车，正如你从下图所看到的。虽然大多数旁观者会觉得冰淇淋车更精美，但那是我的孩子们照着乐高说明书拼出来的，可能和成千上万其他人拼出的冰淇淋车一模一样。相比之下，搭建那辆恐龙车则需要更多的创造力和新颖思维。这个过程帮助他们锻炼了挑选和组装乐高积木的能力。

当然，模仿他人的设计（在获得许可的前提下）和自己创造设计，两者都有其价值。作为一名家长，我努力对这两种创造都表示认可。（说实话，我对那辆恐龙车更「偏爱」一些。）在学习搭建乐高时，从遵循模板开始确实有所帮助。但最终，搭建自己独一无二的项目才能真正丰富你的技能。

作为一名开发者，我也努力推崇独创性的作品。没错，拥有精美的软件固然是好事，其产出的影响也确实重要。但优秀的软件往往是由那些投入大量时间修修补补、不断构建的人写出来的。通过构建独特的项目，你可以掌握关键的软件构建模块。然后，利用这些模块，你就能着手构建更大的项目。

我经常会捣鼓着开发一些 AI 应用程序，其中很多尝试最终都没有什么实际用处。举个最近的例子：我曾开发了一个 Streamlit 应用，它可以连接到 Google Docs 进行身份验证，读取文档中的文本，然后使用一个大语言模型（Large Language Model）来编辑我的文本，并将结果写回文档。但由于用户界面（UI）的一些不便，我最终觉得它不太实用。我相信，很快就会有商业公司（如果他们还没做）推出比我周末花几个小时拼凑出来的产品更好的解决方案。但即便如此，这样的修修补补也帮助我磨练了直觉，并掌握了许多软件组件（比如我现在知道如何通过编程方式与 Google Docs 进行交互），这些知识可能在未来的项目中发挥作用。

如果你有一个项目的想法，我非常鼓励你去动手实现它！很多时候，着手一个项目也会帮你明确还需要学习哪些额外的技能，也许这又会促使你继续学习新的课程。为了保持这份热情，找一些志同道合的朋友，一起交流想法，共同庆祝项目的进展 —— 无论项目大小 —— 都将大有裨益。

[Original text：https://t.co/i21oCaQpDc]

### 063

作者: @AndrewYNg
时间: 2024-05-23
链接: https://x.com/AndrewYNg/status/1793760961343701045
互动: Likes: 12; Retweets: 0; Replies: 0; Quotes: 0; Views: 2,132; Bookmarks: 0; isReply: 1

@greg_karsten Thank you for sharing this -- I think a lot of people feel similarly as you. Please keep tinkering, and from your description it sounds to me like you're making good progress! 🎉

@greg_karsten 感谢你分享这些想法 —— 我想很多人都和你有着相似的感受。请继续你的探索和尝试，听你描述的情况，看来你正在取得不错的进展！🎉

### 064

作者: @AndrewYNg
时间: 2024-05-29
链接: https://x.com/AndrewYNg/status/1795845101979406490
互动: Likes: 1,496; Retweets: 294; Replies: 60; Quotes: 26; Views: 215,378; Bookmarks: 1,143; isReply: 0

New Agentic AI short course! AI Agentic Design Patterns with AutoGen, taught by @MSFTResearch's @Chi_Wang_ and @penn_state's @qingyun_wu, shows you how to use AutoGen to implement agentic design patterns like multi-agent collaboration, sequential and nested chat, reflection, tool use, and planning. Learn how to build and combine multiple specialized agents – such as researchers, planners, coders, writers, and critics – that interact to execute complex workflows, like generating detailed financial reports, that would otherwise have taken extensive manual effort.

This course illustrates key agentic design principles with many fun demonstrations. For example, you'll build a conversational chess game using two player agents, each of which can use a tool to validate moves and update the board state, while engaging in lively banter about the game!

I've enjoyed using AutoGen, and think you will too. Sign up to get started here:  https://t.co/C0tsLuilMf

全新的 AI 智能体（Agentic AI）短期课程来了！由 @MSFTResearch 的 @Chi_Wang_ 和 @penn_state 的 @qingyun_wu 教授的「基于 AutoGen 的 AI 智能体设计模式」课程，将向你展示如何利用 AutoGen 实现各种智能体设计模式，例如多智能体协作、顺序和嵌套聊天、自我反思、工具使用以及规划等。你将学习如何构建和组合多个专业的智能体 —— 比如研究员、规划者、程序员、作家和评论员 —— 让它们协同工作，以完成复杂的任务流程，例如生成详细的财务报告，而这些任务若非如此，将需要大量的人工操作。

本课程通过许多有趣的演示，阐释了关键的 AI 智能体设计原则。例如，你将构建一个对话式国际象棋游戏，其中包含两个玩家智能体，每个智能体都能使用工具来验证棋步并更新棋盘状态，同时它们还能就棋局展开妙趣横生的对话！

我个人非常喜欢使用 AutoGen，相信你也会如此。点击这里注册，即刻开启你的学习之旅： https://t.co/C0tsLuilMf

### 065

作者: @AndrewYNg
时间: 2024-05-30
链接: https://x.com/AndrewYNg/status/1796206876805489105
互动: Likes: 881; Retweets: 162; Replies: 60; Quotes: 26; Views: 186,788; Bookmarks: 597; isReply: 0

A barrier to faster progress in generative AI is evaluations (evals), particularly of custom AI  applications that generate free-form text. Let’s say you have a multi-agent research system that includes a researcher agent and a writer agent. Would adding a fact-checking agent improve the results? If we can’t efficiently evaluate the impact of such changes, it’s hard to know which changes to keep.

For evaluating general-purpose foundation models such as large language models (LLMs) — which are trained to respond to a large variety of prompts — we have standardized tests like MMLU (multiple-choice questions that cover 57 disciplines like math, philosophy, and medicine) and HumanEval (testing code generation); the LMSYS Chatbot arena, which pits two LLMs’ responses against each other and asks a human to judge which response is superior; and large-scale benchmarking like HELM. These evaluation tools took considerable effort to build, and they are invaluable for giving LLM users a sense of different models' relative performance. Nonetheless, they have limitations: For example, leakage of benchmarks datasets’ questions and answers into training data is a constant worry, and human preference for certain answers does not mean those answers are more accurate.

In contrast, our current options for evaluating specific applications built using LLMs are far more limited. Here, I see two major types of applications.
- For applications designed to deliver unambiguous, right-or-wrong responses, we have reasonable options. Let’s say we want an LLM to read a resume and extract the candidate's most recent job title, or read a customer email and route it to the right department. We can create a test set that comprises ground-truth labeled examples with the right responses, and measure the percentage of times the LLM generates the right output. The main bottleneck is creating the labeled test set, which is expensive but surmountable.
- But many LLM-based applications generate free-text output with no single right response. For example, if we ask an LLM to summarize customer emails, there’s a multitude of possible good (and bad) responses. The same holds for an agentic system to do web research and write an article about a topic, or a RAG system for answering questions. It’s impractical to hire an army of human experts to read the LLM’s outputs every time we tweak the algorithm and evaluate if the answers have improved — we need an automated way to test the outputs. Thus, many teams use an advanced language model to evaluate outputs. In the customer email summarization example, we might design an evaluation rubric (scoring criteria) for what makes a good summary. Given an email summary generated by our system, we might prompt an advanced LLM to read it and score it according to our rubric. I’ve found that the results of such a procedure, while better than nothing, can also be noisy — sometimes too noisy to reliably tell me if the way I’ve tweaked an algorithm is good or bad.

The cost of running evals poses an additional challenge. Let’s say you’re using an LLM that costs $10 per million input tokens, and a typical query has 1000 tokens. Each user query therefore costs only $0.01. However, if you iteratively work to improve your algorithm based on 1000 test examples, and if in a single day you evaluate 20 ideas, then your cost will be 20*1000*0.01 = $200. For many projects I’ve worked on, the development costs were fairly negligible until we started doing evals, whereupon the costs suddenly increased. (If the product turned out to be successful, then costs increased even more at deployment, but that was something we were happy to see!)

In addition to the dollar cost, evals also have a significant time cost. Running evals on 1000 examples might take tens of minutes or even hours. Time spent waiting for eval jobs to finish also slows down the speed with which we can experiment and iterate over new ideas. Previously I wrote that fast, inexpensive token generation is critical for agentic workflows. This will also be useful for evals, which involve nested for-loops that iterate over a test set and different model/hyperparameter/prompt choices and therefore consume large numbers of tokens.

Despite the limitations of today's eval methodologies, I’m optimistic that our community will invent better techniques (maybe involving agentic workflows like reflection?) for getting LLMs to evaluate such output.

If you’re a developer or researcher and have ideas along these lines, I hope you’ll keep working on them and consider open sourcing or publishing your findings!

[Original text: https://t.co/HXtzJH7eP8 ]

生成式 AI（Generative AI）想要取得更快进展，一大阻碍就是评估（evals），尤其是对那些能生成自由格式文本的定制化 AI 应用程序的评估。比方说，你有一个多智能体研究系统，里面包含一个研究员智能体和一个写作者智能体。那么，如果再加一个事实核查智能体，效果会更好吗？如果我们无法高效地评估这些改动带来的影响，就很难知道究竟哪些改动值得保留。

对于评估像大语言模型（LLMs）这样的通用基础模型 —— 这些模型经过训练，能够响应各种各样的提示 —— 我们有一套标准化的测试方法。例如，MMLU（包含数学、哲学、医学等 57 个学科的多项选择题）和 HumanEval（测试代码生成能力)；LMSYS Chatbot Arena，它通过让两个 LLM 的回答进行比拼，并由人类判断哪个回答更优；以及像 HELM 这样的大规模基准测试。这些评估工具的构建耗费了巨大的精力，它们对于 LLM 用户了解不同模型的相对性能来说是无价之宝。然而，它们也并非没有局限性：例如，基准测试数据集的问题和答案可能会泄露到训练数据中，这是一个持续的担忧；而且人类偏好的答案不一定就意味着它们更准确。

相比之下，我们目前用于评估基于 LLM 构建的特定应用程序的选项则要有限得多。在我看来，这类应用程序主要分为两类：
- 对于那些旨在提供明确的、非对即错响应的应用，我们有相对成熟的评估方案。例如，我们希望 LLM 阅读一份简历，提取候选人最近的职位名称，或者阅读一封客户邮件，将其路由到正确的部门。这时，我们可以创建一个测试集，其中包含带有正确响应的真实标签示例，然后测量 LLM 生成正确输出的百分比。主要的挑战在于创建这样的标签测试集，这虽然成本不菲，但并非无法克服。
- 然而，许多基于 LLM 的应用会生成开放式文本输出，往往没有唯一正确的答案。比如，如果我们要求 LLM 总结客户邮件，可能会有无数种好的（当然也有坏的）总结方式。对于一个负责网络研究并撰写文章的智能体系统，或者一个用于回答问题的 RAG 系统来说，也面临同样的问题。每次我们调整算法，并想评估答案是否有所改进时，都雇佣一支庞大的人类专家团队来阅读 LLM 的输出，这是不现实的。我们需要一种自动化的方法来测试这些输出。因此，许多团队选择使用先进的语言模型来评估输出。在客户邮件总结的例子中，我们可能会设计一套评估准则（评分标准）来定义什么才算一份好的总结。然后，对于系统生成的一份邮件总结，我们就可以提示一个先进的 LLM 来阅读它，并根据我们的准则进行评分。我发现，这种方法的评估结果虽然聊胜于无，但也可能充满噪声 —— 有时这种噪声大到无法可靠地告诉我，我对算法的调整究竟是好是坏。

运行评估的成本也带来了额外的挑战。假设你正在使用一个 LLM，每百万输入 Token 成本为 10 美元，而一次典型查询包含 1000 个 Token。这样算下来，每个用户查询的成本仅为 0.01 美元。然而，如果你基于 1000 个测试示例来迭代改进算法，并且如果你在一天之内评估了 20 个不同的想法，那么你的成本将是 20 * 1000 * 0.01 = 200 美元。在我参与过的许多项目中，在开始进行评估之前，开发成本都相当微不足道，而一旦启动评估，成本就会突然飙升。(如果产品最终获得成功，那么部署时的成本还会更高，但这通常是我们乐见其成的事！)

除了金钱成本，评估还需要耗费大量时间。对 1000 个示例进行评估可能需要数十分钟甚至数小时。等待评估任务完成的时间，也会拖慢我们实验和迭代新想法的速度。我之前曾提到，快速、廉价的 Token 生成对于智能体工作流至关重要。这对于评估同样大有裨益，因为评估涉及嵌套的 for 循环，需要遍历测试集以及不同的模型、超参数和提示选择，因此会消耗大量的 Token。

尽管目前的评估方法存在局限性，我仍然乐观地认为，我们的社区将发明出更好的技术（也许会涉及像反思这样的智能体工作流？）来让 LLM 更好地评估此类输出。

如果你是开发人员或研究人员，并且在这些方面有任何想法，我希望你能继续努力，并考虑开源或公布你的研究成果！

[原文链接：https://t.co/HXtzJH7eP8]

### 066

作者: @AndrewYNg
时间: 2024-06-04
链接: https://x.com/AndrewYNg/status/1798063159787577843
互动: Likes: 987; Retweets: 163; Replies: 95; Quotes: 37; Views: 140,885; Bookmarks: 268; isReply: 0

We just released a new climate emulator to explore the application of Stratospheric Aerosol Injection (SAI) to mitigate global warming!

SAI uses reflective particles in the atmosphere to reflect sunlight and thereby cool Earth’s surface. Our emulator lets you explore how different ways to apply SAI might affect average global temperature.

Please check out the emulator at https://t.co/OxtaQMyDuL.

SAI is a promising direction, but we still need more research to better understand its impact and potential implementation.

Big thanks to collaborators @jeremy_irvin16 @DanVisioni Ben Kravitz @dakotagruener @chrisroadmap and @DWatsonParris

我们刚刚发布了一款全新的气候模拟器，旨在探索平流层气溶胶注入（SAI）在缓解全球变暖方面的应用！

平流层气溶胶注入（SAI）的原理是利用大气中的反射粒子来反射太阳光，从而达到冷却地球表面的目的。我们的模拟器能帮助你探索，以不同方式实施 SAI 可能对全球平均温度产生怎样的影响。

欢迎访问 https://t.co/OxtaQMyDuL 体验这款模拟器。

SAI 是一个很有前景的方向，但我们仍需更多研究，以便更好地理解其影响以及如何潜在地实施。

衷心感谢所有合作者：@jeremy_irvin16、@DanVisioni、Ben Kravitz、@dakotagruener、@chrisroadmap 和 @DWatsonParris。

### 067

作者: @AndrewYNg
时间: 2024-06-05
链接: https://x.com/AndrewYNg/status/1798378861337723039
互动: Likes: 1,134; Retweets: 215; Replies: 57; Quotes: 16; Views: 151,103; Bookmarks: 826; isReply: 0

New AI Agentic course! Learn to use LangGraph to build single and multi-agent LLM applications in AI Agents in LangGraph. This short course, taught by LangChain @LangChainAI  founder Harrison Chase @hwchase17 and @tavilyai founder @weiss_rotem, shows how to integrate agentic search to enhance an agent's knowledge with query-focused answers in predictable formats. Also learn to implement agentic memory to save state for reasoning and debugging, and see how human-in-the-loop input can guide agents at key junctures. 

You'll build an agent from scratch, then reconstruct it with LangGraph to thoroughly understand the framework. Finally, you'll build a sophisticated essay-writing agent that incorporates all the learnings from the course.

Sign up here! https://t.co/ZDpjLmdyDL

新的 AI 智能体（AI Agent）课程！学习如何使用 LangGraph 在 LangGraph 框架下构建单智能体和多智能体大语言模型（LLM）应用程序。这个短课程由 LangChain @LangChainAI 创始人 Harrison Chase @hwchase17 和 @tavilyai 创始人 @weiss_rotem 亲自授课，将向你展示如何集成智能体搜索（Agentic Search），通过可预测格式的、以查询为中心的答案来增强智能体的知识。你还将学习如何实现智能体记忆（Agentic Memory）来保存推理和调试的状态，并了解人工循环输入（Human-in-the-loop Input）如何在关键时刻引导智能体。

你将从零开始构建一个智能体，然后使用 LangGraph 对其进行重构，以便彻底理解该框架。最后，你将构建一个复杂的文章写作智能体，它将融合课程中的所有学习内容。

在此注册！https://t.co/ZDpjLmdyDL

### 068

作者: @AndrewYNg
时间: 2024-06-06
链接: https://x.com/AndrewYNg/status/1798753608974139779
互动: Likes: 3,331; Retweets: 782; Replies: 163; Quotes: 136; Views: 1,119,357; Bookmarks: 881; isReply: 0

The effort to protect innovation and open source continues. I believe we’re all better off if anyone can carry out basic AI research and share their innovations. Right now, I’m deeply concerned about California's proposed law SB-1047. It’s a long, complex bill with many parts that require safety assessments, shutdown capability for models, and so on.

There are many things wrong with this bill, but I’d like to focus here on just one: It defines an unreasonable “hazardous capability” designation that may make builders of large AI models liable if someone uses their models to do something that exceeds the bill’s definition of harm (such as causing $500 million in damage). That is practically impossible for any AI builder to ensure. If the bill is passed in its present form, it will stifle AI model builders, especially open source developers.

Some AI applications, for example in healthcare, are risky. But as I wrote previously, regulators should regulate applications rather than technology.
- Technology refers to tools that can be applied in many ways to solve various problems.
- Applications are specific implementations of technologies designed to meet particular customer needs.

For example, an electric motor is a technology. When we put it in a blender, an electric vehicle, dialysis machine, or guided bomb, it becomes an application. Imagine if we passed laws saying, if anyone uses a motor in a harmful way, the motor manufacturer is liable. Motor makers would either shut down or make motors so tiny as to be useless for most applications. If we pass such a law, sure, we might stop people from building guided bombs, but we’d also lose blenders, electric vehicles, and dialysis machines. In contrast, if we look at specific applications, like blenders, we can more rationally assess risks and figure out how to make sure they’re safe, and even ban classes of applications, like certain types of munitions.

Safety is a property of the application, not a property of the technology (or model), as @random_walker and @sayashk have pointed out. Whether a blender is a safe one can’t be determined by examining the electric motor. A similar argument holds for AI.

SB-1047 doesn’t account for this distinction. It ignores the reality that the number of beneficial uses of AI models is, like electric motors, vastly greater than the number of harmful ones. But, just as no one knows how to build a motor that can’t be used to cause harm, no one has figured out how to make sure an AI model can’t be adapted to harmful uses. In the case of open source models, there’s no known defense to fine-tuning to remove RLHF alignment. And jailbreaking work has shown that even closed-source, proprietary models that have been properly aligned can be attacked in ways that make them give harmful responses. Indeed, the sharp-witted @elder_plinius regularly tweets about jailbreaks for closed models. Kudos also to Anthropic’s @cem__anil and collaborators for publishing their work on many-shot jailbreaking, an attack that can get leading large language models to give inappropriate responses and is hard to defend against.

California has been home to a lot of innovation in AI. I’m worried that this anti-competitive, anti-innovation proposal has gotten so much traction in the legislature. Worse, other jurisdictions often follow California, and it would be awful if they were to do so in this instance.

SB-1047 passed in a key vote in the State Senate in May, but it still has additional steps before it becomes law. I hope you will speak out against it if you get a chance to do so.

[Original text (with links): https://t.co/MOQqFF6cID ]

保护创新和开源（open source）的努力仍在继续。我相信，如果每个人都能进行基础的 AI 研究并分享他们的创新，我们所有人都会从中受益。目前，我深切关注加利福尼亚州拟议的法律 SB-1047。这是一项漫长而复杂的法案，其中许多条款要求对模型进行安全评估、具备模型关闭能力等。

这项法案存在诸多问题，但我在此只聚焦于其中一个：它定义了一种不合理的「危险能力」认定，这可能导致大型 AI 模型开发者承担责任。具体来说，如果有人使用他们的模型做出了超出该法案所定义损害范围的行为（例如造成 5 亿美元的损失），开发者就可能被追责。对于任何 AI 开发者来说，几乎不可能确保模型不被如此滥用。如果该法案以目前的形式通过，它将扼杀 AI 模型开发者，尤其是开源开发者。

一些 AI 应用，例如在医疗保健领域，确实存在风险。但正如我之前所写，监管机构应该监管应用，而不是技术。
- 技术指的是可以多种方式应用以解决各种问题的工具。
- 应用是技术的特定实现，旨在满足特定的客户需求。

举个例子，电动机就是一种技术。当我们将其安装在搅拌机、电动汽车、透析机或制导炸弹中时，它就变成了一种应用。试想一下，如果我们通过法律规定，如果有人以有害方式使用电机，电机制造商将承担责任，那会怎样？电机制造商要么倒闭，要么制造出非常微小的电机，以至于无法用于大多数应用。如果通过这样的法律，我们固然可能阻止人们制造制导炸弹，但同时我们也将失去搅拌机、电动汽车和透析机。相比之下，如果我们审视具体的应用，比如搅拌机，我们就可以更合理地评估风险，并找出如何确保其安全的方法，甚至可以禁止某些类别的应用，比如特定类型的弹药。

安全性是应用的属性，而非技术（或模型）固有的属性，正如 @random_walker 和 @sayashk 所指出的。搅拌机是否安全，无法通过检查其电动机来判断。类似的论点也适用于 AI。

SB-1047 没有考虑到这种区别。它忽略了这样一个现实：AI 模型的有益用途数量，就像电动机一样，远远超过了有害用途的数量。但是，正如没有人知道如何制造一个不能造成伤害的电机一样，也没有人知道如何确保 AI 模型不会被滥用于有害目的。对于开源模型，目前没有已知的防御措施可以有效阻止通过微调（fine-tuning）来移除强化学习人类反馈（RLHF）对齐。此外，越狱（jailbreaking）研究表明，即使是经过适当对齐的闭源专有模型，也可能被攻击，使其产生有害回应。事实上，@elder_plinius 经常在推特上发布关于闭源模型越狱的消息。我们也要赞扬 Anthropic 的 @cem__anil 及其合作者，他们发表了关于多样本越狱（many-shot jailbreaking）的研究，这种攻击能够使领先的 ** 大语言模型（Large Language Model)** 给出不当回应，并且难以防御。

加利福尼亚州一直是 AI 领域许多创新的发源地。我担心这项反竞争、反创新的提案在立法机构中获得了如此大的关注。更糟糕的是，其他司法管辖区通常会效仿加利福尼亚州，如果他们在这种情况下也这样做，那将是令人担忧的。

SB-1047 已于五月份在州参议院的一次关键性投票中通过，但在成为法律之前仍需经历进一步的立法程序。我希望如果有机会，大家能站出来反对它。

[原文链接：https://t.co/MOQqFF6cID]

### 069

作者: @AndrewYNg
时间: 2024-06-11
链接: https://x.com/AndrewYNg/status/1800582171259982289
互动: Likes: 1,736; Retweets: 348; Replies: 87; Quotes: 52; Views: 544,536; Bookmarks: 1,363; isReply: 0

I think AI agentic machine translation has huge potential for improving over traditional neural machine translation, and am releasing as open-source a demonstration I'd been playing with as a fun weekend project.

Using an agentic workflow, this demonstration (i) Prompts an LLM to translate from one language to another, (ii) Reflects on the translation to come up with constructive suggestions, (iii) Uses the suggestions to refine the translation. In our limited testing, this is sometimes competitive with, and sometimes worse than, leading commercial providers.

But it gives a highly steerable translation system where by simply changing the prompt, you can specify the tone (formal/informal), regional variation (do you want Spanish as spoken in Spain or as spoken in Latin America?), and ensure consistent translation of terms (by providing a glossary).

This is not mature software. But I hope the open-source community can make agentic translation work much better. Given how a simple reflection workflow already gives decent results, I think there's significant headroom to make agentic translation much better.

Releasing an early software prototype like this is something new I decided to try to see if it is helpful to the developer community. I'd love any feedback on this.

Thanks to Joaquin Dominguez, @nedteneva, @JohnSanterre for help with this.

https://t.co/nghC3wN3Id

我认为 AI 智能体机器翻译（AI agentic machine translation）在超越传统神经网络机器翻译方面具有巨大潜力，因此我决定将我作为周末兴趣项目开发的一个演示程序开源发布。

这个演示程序采用了一种智能体工作流（agentic workflow），它会执行以下步骤：(i）提示一个大语言模型（LLM）进行跨语言翻译；(ii）对翻译结果进行反思，从而提出建设性建议；(iii）利用这些建议来优化最终译文。在我们有限的测试中，它的表现有时能与顶尖的商业翻译服务媲美，有时则略逊一筹。

不过，它提供了一个高度可控的翻译系统。通过简单地修改提示词，你就能指定译文的语调（例如，正式或非正式）、区域差异（比如，你想要在西班牙使用的西班牙语，还是拉丁美洲的西班牙语？），甚至可以通过提供术语表来确保专业术语翻译的一致性。

这虽然还不是一款成熟的软件，但我希望开源社区能共同努力，让智能体翻译发挥出更大的作用。鉴于一个简单的反思工作流就已经能带来不错的效果，我认为智能体翻译未来还有巨大的提升空间。

发布这样一个早期的软件原型，是我首次尝试的方式，希望能对开发者社区有所帮助。我非常期待能收到大家对此的任何反馈。

感谢 Joaquin Dominguez、@nedteneva、@JohnSanterre 在此项目中的帮助。

https://t.co/nghC3wN3Id

### 070

作者: @AndrewYNg
时间: 2024-06-13
链接: https://x.com/AndrewYNg/status/1801277928740970619
互动: Likes: 1,052; Retweets: 216; Replies: 20; Quotes: 21; Views: 109,282; Bookmarks: 781; isReply: 0

New short course: Building Your Own Database Agent, created with Microsoft @Azure's @adriangs86. You'll learn to build an AI assistant that translates natural language questions into SQL queries. Querying with natural language empowers everyone in your organization, from business leaders to developers, to access data insights directly, using plain English.

You’ll use the Azure OpenAI Service and LangChain to implement retrieval augmented generation and function calling, and leverage the Assistants API. You'll gain hands-on experience building an agent that can reason over both CSV files and SQL databases.

Please sign up here! https://t.co/9NxN8pJYKC

新的短期课程：构建你自己的数据库智能体（AI Agent），由 Microsoft @Azure 与 @adriangs86 合作推出。你将学习如何构建一个 AI 助手（AI assistant），它能够将自然语言问题转化为 SQL 查询。通过自然语言查询，组织里的每个人 —— 从业务领导者到开发者 —— 都能直接使用日常英语获取数据洞察。

本课程中，你将使用 Azure OpenAI Service 和 LangChain 来实现检索增强生成（retrieval augmented generation）和函数调用（function calling），并利用 Assistants API。你将获得实际经验，构建一个能理解 CSV 文件和 SQL 数据库并据此进行推理的智能体。

请在这里报名！https://t.co/9NxN8pJYKC

### 071

作者: @AndrewYNg
时间: 2024-06-13
链接: https://x.com/AndrewYNg/status/1801295202788983136
互动: Likes: 1,130; Retweets: 204; Replies: 59; Quotes: 23; Views: 178,391; Bookmarks: 430; isReply: 0

One reason for machine learning’s success is that our field welcomes a wide range of work. I can’t think of even one example where someone developed what they called a machine learning algorithm and senior members of our community criticized it saying, “that’s not machine learning!” Indeed, linear regression using a least-squares cost function was used by mathematicians Legendre and Gauss in the early 1800s — long before the invention of computers — yet machine learning has embraced these algorithms, and we routinely call them “machine learning” in introductory courses!

In contrast, about 20 years ago, I saw statistics departments at a number of universities look at developments in machine learning and say, “that’s not really statistics.” This is one reason why machine learning grew much more in computer science than statistics departments. (Fortunately, since then, most statistics departments have become much more open to machine learning.)

This contrast came to mind a few months ago, as I thought about how to talk about agentic systems that use design patterns such as reflection, tool use, planning, and multi-agent collaboration to produce better results than zero-shot prompting. I had been involved in conversations about whether certain systems should count as “agents.” Rather than having to choose whether or not something is an agent in a binary way, I thought, it would be more useful to think of systems as being agent-like to different degrees. Unlike the noun “agent,” the adjective “agentic” allows us to contemplate such systems and include all of them in this growing movement.

More and more people are building systems that prompt a large language model multiple times using agent-like design patterns. But there’s a gray zone between what clearly is not an agent (prompting a model once) and what clearly is (say, an autonomous agent that, given high-level instructions, plans, uses tools, and carries out multiple, iterative steps of processing).

Rather than arguing over which work to include or exclude as being a true agent, we can acknowledge that there are different degrees to which systems can be agentic. Then we can more easily include everyone who wants to work on agentic systems. We can also encourage newcomers to start by building simple agentic workflows and iteratively make their systems more sophisticated.

In the past few weeks, I’ve noticed that, while technical people and non-technical people alike sometimes use the word “agent,” mainly only technical people use the word “agentic” (for now!). So when I see an article that talks about “agentic” workflows, I’m more likely to read it, since it’s less likely to be marketing fluff and more likely to have been written by someone who understands the technology.

Let’s keep working on agentic systems and keep welcoming anyone who wants to join our field!

[Original text: https://t.co/4izf1hsv9P ]

机器学习（Machine Learning）之所以能取得成功，其中一个原因是我们的领域对各种研究方向都持开放态度。我甚至想不出有哪个例子，是有人开发了他们所谓的机器学习算法，却遭到社区资深成员的批评，说「那根本不是机器学习！」事实上，使用最小二乘成本函数（least-squares cost function）的线性回归（linear regression），早在 19 世纪初，也就是计算机发明之前，就被数学家 Legendre 和 Gauss 使用了。然而，机器学习却欣然接纳了这些算法，我们甚至在入门课程中也习惯性地称它们为「机器学习」！

与此形成鲜明对比的是，大约 20 年前，我看到许多大学的统计学系在看待机器学习的发展时，会说「那不是真正的统计学。」这也是为什么机器学习在计算机科学系的发展，要比在统计学系快得多的一个原因。（幸运的是，自那以后，大多数统计学系对机器学习的态度变得开放了许多。）

几个月前，当我思考如何谈论那些使用反射（reflection）、工具使用（tool use）、规划（planning）和多 AI 智能体（multi-agent）协作等设计模式（design patterns），从而产出比零样本（Zero-shot）提示（prompting）更好结果的智能体系统（agentic systems）时，我想到了这种对比。我曾参与过一些讨论，争论某些系统是否应该被算作「AI 智能体（AI Agent）」。我当时想，与其必须以非此即彼的方式去判断一个系统是不是 AI 智能体，不如将系统看作是具备不同程度「智能体化（agentic）」特性的，这会更有意义。与名词「AI 智能体」不同，形容词「智能体化」允许我们审视并接纳所有这类系统，将它们都纳入到这一日益壮大的运动中。

越来越多的人正在构建系统，这些系统会利用智能体化的设计模式，多次向大语言模型（LLM/Large Language Model）发出提示。然而，在那些明确不是 AI 智能体的系统（例如，只向模型发出一次提示）和那些明确是 AI 智能体的系统（例如，一个自主 AI 智能体，在接收到高级指令后，能够进行规划、使用工具并执行多个迭代处理步骤）之间，存在一个灰色地带。

与其争论哪些工作应该被纳入或排除在「真正 AI 智能体」的范畴之外，我们不如承认系统在不同程度上可以是智能体化的。这样，我们就能更容易地欢迎所有希望从事智能体化系统研究的人。我们还可以鼓励新手从构建简单的智能体化工作流（workflow）开始，然后通过迭代的方式逐步提升其系统的复杂性。

在过去的几周里，我注意到，尽管技术人员和非技术人员有时都会使用「AI 智能体」这个词，但（目前！）主要只有技术人员会使用「智能体化」这个词。所以，当我看到一篇谈论「智能体化」工作流的文章时，我更有可能去阅读它，因为它不太可能是营销性质的空话，而更可能是由真正理解技术的人撰写的。

让我们继续致力于智能体化系统，并欢迎所有愿意加入我们领域的人！

[原文链接：https://t.co/4izf1hsv9P]

### 072

作者: @AndrewYNg
时间: 2024-06-20
链接: https://x.com/AndrewYNg/status/1803812309460189479
互动: Likes: 846; Retweets: 200; Replies: 98; Quotes: 14; Views: 110,186; Bookmarks: 513; isReply: 0

Function calling is a powerful way to extend the capabilities of LLMs and AI agents by letting them use external tools. Our new short course Function calling and Data Extraction with LLMs, created with @NexusflowX and taught by @JiantaoJ  and @VenkatKSrini, demonstrates how to prompt LLMs to form calls to external functions. 

You'll work with NexusRavenV2-13B, a 13B parameter open-source model that excels in function calling tasks while still being small enough to host locally. Learn to use function calling to extract structured data from unstructured text and access web APIs, and build an end-to-end application that processes customer service transcripts. You'll learn how to build LLM-powered applications that can analyze feedback, automate data entry, and enhance search. 

Please get started here: https://t.co/FxSp3jv36w

函数调用（Function calling）是一种强大的方法，它能让大语言模型（LLM）和 AI 智能体（AI Agent）借助外部工具，从而扩展它们的能力。我们与 @NexusflowX 合作开发，并由 @JiantaoJ 和 @VenkatKSrini 教授的新短课程「使用大语言模型进行函数调用和数据提取」，将演示如何提示大语言模型来生成对外部函数的调用。

你将会在课程中接触到 NexusRavenV2-13B—— 一个拥有 130 亿参数的开源模型。它在函数调用任务中表现出色，并且体积足够小，可以在本地设备上运行。你将学习如何利用函数调用，从非结构化文本中提取结构化数据，访问网络 API，并构建一个端到端的应用程序来处理客户服务文本记录。你还会掌握如何开发基于大语言模型的应用程序，这些应用能够分析用户反馈、自动化数据输入以及增强搜索功能。

请点击此处开始学习：https://t.co/FxSp3jv36w

### 073

作者: @AndrewYNg
时间: 2024-06-20
链接: https://x.com/AndrewYNg/status/1803835964604977663
互动: Likes: 1,604; Retweets: 314; Replies: 56; Quotes: 18; Views: 217,527; Bookmarks: 1,341; isReply: 0

On Father’s Day last weekend, I sat with my daughter to help her practice solving arithmetic problems. To give her practice problems, I used OpenDevin, an open-source agentic coding framework, to write a Python script that generated questions that she enjoyed answering at her own pace. OpenDevin wrote the code much faster than I could have and genuinely improved my and my daughter’s day.

Six months ago, coding agents were a novelty. They still frequently fail to deliver, but I find that they’re now working well enough that they might be genuinely useful to more and more people!

Given a coding problem that’s specified in a prompt, the workflow for a coding agent typically goes something like this: Use a large language model (LLM) to analyze the problem and potentially break it into steps to write code for, generate the code, test it, and iteratively use any errors discovered to ask the coding agent to refine its answer. But within this broad framework, a huge design space and numerous innovations are available to experiment with. I’d like to highlight a few papers that I find notable:
- “AgentCoder: Multiagent-Code Generation with Iterative Testing and Optimisation,” Huang et al. (2024).
- “LDB: A Large Language Model Debugger via Verifying Runtime Execution Step by Step,” Zhong et al., (2024).
- “SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering,” Yang et al. (2024).

How can we test the code without requiring the user to write test cases? In a multi-agent system, each “agent” is an LLM prompted to play a particular role. An interesting result from AgentCoder shows that having separate agents for writing code and generating tests results in better performance than letting a single agent do both tasks. This is presumably because, if the agent writing the code is also responsible for writing the tests, the tests might be influenced by the code and fail to consider corner cases that the code does not cover.

When people think of testing code, many initially think of output testing, in which we see if the code generates the correct outputs to a specific set of test inputs. If the code fails a test, an LLM can be prompted to reflect on why the code failed and then to try to fix it. In addition to testing the output, the LDB method is helpful. LDB steps through the code and presents to the LLM values of the variables during intermediate steps of execution, to see if the LLM can spot exactly where the error is. This mimics how a human developer might step through the code to see where one of the computational steps went wrong, and so pinpoint and fix the problem.

A lot of agentic workflows mimic human workflows. Similar to other work in machine learning, if humans can do a task, then trying to mimic humans makes development much easier compared to inventing a new process. However, the authors of SWE-agent noticed that many tools that humans use for coding are very inefficient for agents. For example, giving an agent access to a bash shell and having it find a piece of code by executing numerous cd, ls, and cat commands is inefficient, even though humans can do this rapidly. Similarly, visual coding editors like VSCode, emacs, and vim are easy for humans to use, but hard for LLMs (or LMMs) to navigate. Because agents interact with computers differently than humans do, the authors found that building special-purpose tools (functions) to let an agent search, view, and edit codebases resulted in better performance.

One reason research into coding agents is making rapid progress is that their performance can be evaluated automatically and reliably. With benchmarks like HumanEval, MBPP, and SWE-bench, researchers can try out an idea and automatically test how often it generates correct code. In contrast, even though there’s considerable activity on AI research agents that search the web and synthesize an article (I’ve enjoyed using the open-source STORM system by Stanford's Yijia Shao et al.), they are hard to evaluate and this makes progress harder.

Github Copilot was released in 2021, and many developers have been getting coding help by prompting LLMs. The rapid evolution from that to more sophisticated coding agents is expanding how computers can help us with coding tasks, and the pace of progress is rapid. With these tools, I expect programming to become even more fun and more productive.

[Original text (with links): https://t.co/QP1JRomjrZ ]

上周末的父亲节，我陪女儿练习算术题。为了给她出题，我用 OpenDevin 这个开源的 AI 智能体（AI Agent）编码框架，编写了一个 Python 脚本，生成她喜欢按照自己的节奏回答的问题。OpenDevin 编写代码的速度远超我的预期，确实让我和女儿的一天更加愉快。

仅仅六个月前，编码 AI 智能体（coding agents）还是个新鲜事物。虽然它们现在仍时常无法完全达到预期，但我发现它们已经变得足够好用，有望对越来越多的人真正有所助益！

对于一个在提示词（prompt）中指定的编码问题，编码 AI 智能体的工作流程通常是这样的：它会利用一个大语言模型（LLM）来分析问题，并可能将其分解成若干个编写代码的步骤，然后生成代码，进行测试，并根据发现的错误迭代地要求编码 AI 智能体优化其解决方案。然而，在这个宽泛的框架内，存在巨大的设计空间，有无数创新可供我们探索和实验。我想重点介绍几篇我发现值得关注的论文：
-「AgentCoder：Multiagent-Code Generation with Iterative Testing and Optimisation,」Huang et al.（2024).
-「LDB：A Large Language Model Debugger via Verifying Runtime Execution Step by Step,」Zhong et al.，(2024).
-「SWE-agent：Agent-Computer Interfaces Enable Automated Software Engineering,」Yang et al.（2024).

我们如何在不要求用户编写测试用例的情况下测试代码呢？在一个多智能体（multi-agent）系统中，每个「智能体」都是一个被指示扮演特定角色的大语言模型（LLM）。AgentCoder 的一项有趣研究结果显示，如果让不同的智能体分别负责编写代码和生成测试，其性能要优于让单个智能体完成这两项任务。这大概是因为，如果负责编写代码的智能体同时也要负责编写测试，那么测试可能会受到代码本身的影响，从而忽略代码可能存在的边缘情况。

当人们想到测试代码时，许多人首先想到的是输出测试，即检查代码是否为一组特定的测试输入生成了正确的输出。如果代码未通过测试，我们可以提示大语言模型（LLM）分析代码失败的原因，然后尝试修复它。除了输出测试，LDB 方法也很有用。LDB 会逐步执行代码，并向大语言模型（LLM）展示代码执行中间步骤中变量的值，以帮助 LLM 准确找出错误所在。这模仿了人类开发人员逐步调试代码，查找计算步骤中哪个环节出了问题，从而精确定位并修复问题的过程。

许多 AI 智能体（agentic）工作流都模仿了人类的工作方式。与机器学习领域的其他研究类似，如果一项任务人类可以完成，那么尝试模仿人类的工作方式往往比发明全新的流程能让开发工作容易得多。然而，SWE-agent 的作者注意到，许多人类在编码中使用的工具对于 AI 智能体来说效率非常低。例如，让一个 AI 智能体访问 bash shell 并通过执行大量的 cd、ls 和 cat 命令来查找一段代码，效率非常低下，尽管人类可以迅速完成这些操作。同样，像 VSCode、emacs 和 vim 这样的可视化代码编辑器对人类来说易于使用，但对大语言模型（LLMs)（或大型多模态模型（LMMs)）来说却难以操作。由于 AI 智能体与计算机的交互方式与人类不同，作者发现，构建专门的工具（函数）让智能体能够搜索、查看和编辑代码库，能够带来更好的性能。

编码 AI 智能体研究之所以能取得快速进展，一个原因在于它们的性能可以被自动且可靠地评估。借助 HumanEval、MBPP 和 SWE-bench 等基准测试，研究人员可以尝试新的想法，并自动测试其生成正确代码的频率。相比之下，尽管专注于搜索网页和合成文章的 AI 研究智能体（AI research agents）领域非常活跃（我个人很喜欢使用 Stanford 大学 Yijia Shao 等人开发的开源 STORM 系统），但它们很难评估，这使得该领域的进展更加困难。

GitHub Copilot 于 2021 年发布，许多开发人员已经开始通过提示大语言模型（LLMs）来获得编码帮助。从那时到现在，更复杂的编码 AI 智能体的快速演变，正在极大地扩展计算机在编码任务上帮助我们的方式，而且进展速度非常快。有了这些工具，我预计编程将变得更加有趣和高效。

[原文链接： https://t.co/QP1JRomjrZ]

### 074

作者: @AndrewYNg
时间: 2024-06-26
链接: https://x.com/AndrewYNg/status/1806008133862805840
互动: Likes: 787; Retweets: 158; Replies: 30; Quotes: 10; Views: 102,839; Bookmarks: 205; isReply: 0

As machine learning models grow in size, so too does their carbon footprint. As AI scales, it's important that we quantify and mitigate these emissions. 
In our new short course Carbon Aware Computing for GenAI Developers you'll learn from @googlecloud  Developer Advocate Nikita Namjoshi how to:
- Query the ElectricityMaps API for real-time data on regional electricity grid carbon intensity
- Route your model training jobs to data centers in regions primarily powered by low-carbon sources like wind, solar, hydro and nuclear
- Measure the carbon footprint of your ML training, inference, storage and API usage with the Google Cloud's Carbon Footprint tool
- Optimize training job scheduling to run when clean energy is most abundant in a given region.

You can sign up here: https://t.co/CW3dBUJYfe

随着机器学习模型规模不断扩大，其碳足迹也随之增大。在 AI（人工智能）规模化发展的同时，量化并减少这些排放至关重要。
在我们的新短课程「面向生成式 AI（Generative AI）开发者的碳感知计算」中，你将跟随 @googlecloud 开发者倡导者 Nikita Namjoshi 学习如何：
- 查询 ElectricityMaps API，获取区域电网碳强度的实时数据
- 将你的模型训练任务部署到主要依靠风能、太阳能、水力发电和核能等低碳能源供电的数据中心所在的区域
- 使用 Google Cloud 的碳足迹工具，测量你的模型训练、推理、存储和 API 使用所产生的碳足迹
- 优化训练任务的调度，以便在特定区域清洁能源最充足时运行。

你可以在这里注册：https://t.co/CW3dBUJYfe

### 075

作者: @AndrewYNg
时间: 2024-06-27
链接: https://x.com/AndrewYNg/status/1806383866472730749
互动: Likes: 158; Retweets: 24; Replies: 15; Quotes: 3; Views: 48,625; Bookmarks: 22; isReply: 0

An often overlooked part of the AI supply chain is electricity to power our data centers. 

@TheAESCorp is the leading provider of renewable energy to data centers, and is a also global leader in building technology to efficiently scale renewal energy projects. At AI Fund, we're thrilled to work with the visionary @AndresGluski and the AES team to co-build new AI companies that will help with the energy transition!

在人工智能的供应链中，有一个常常被人们忽略的关键环节，那就是为数据中心提供动力的电力。

AES 公司（@TheAESCorp）不仅是数据中心可再生能源的主要供应商，同时也是在高效扩大可再生能源项目技术方面的全球领军者。在 AI Fund，我们非常高兴能与富有远见的 Andres Gluski 先生和 AES 团队携手合作，共同孵化新的 AI 公司，助力全球能源转型！

### 076

作者: @AndrewYNg
时间: 2024-07-06
链接: https://x.com/AndrewYNg/status/1809658174724796583
互动: Likes: 2,063; Retweets: 482; Replies: 80; Quotes: 47; Views: 546,962; Bookmarks: 1,389; isReply: 0

Shoutout to the team that built https://t.co/sJnTRDfHGF . Really neat site that benchmarks the speed of different LLM API providers to help developers pick which models to use. This nicely complements the LMSYS Chatbot Arena, Hugging Face open LLM leaderboards and Stanford's HELM that focus more on the quality of the outputs. 

I hope benchmarks like this encourage more providers to work on fast token generation, which is critical for agentic workflows!

在此特别感谢开发了 https://t.co/sJnTRDfHGF 网站的团队。这个网站非常出色，它对不同大语言模型（LLM）API 提供商的速度进行了基准测试，旨在帮助开发者选择合适的模型。这与 LMSYS Chatbot Arena、Hugging Face 开放 LLM 排行榜以及 Stanford 的 HELM 形成了良好的互补，因为后者更多关注模型输出的质量。

我希望这样的基准测试能鼓励更多提供商专注于提升 Token 的生成速度，这对于 AI 智能体（AI Agent）的工作流至关重要！

### 077

作者: @AndrewYNg
时间: 2024-07-08
链接: https://x.com/AndrewYNg/status/1810338684270768464
互动: Likes: 427; Retweets: 64; Replies: 59; Quotes: 11; Views: 64,056; Bookmarks: 90; isReply: 0

As we reach the milestone of the 256th issue of The Batch, I’m reflecting on how AI has changed over the years and how society continues to change with it. As AI becomes more widely available, it’s clear that many people — developers and non-developers — will benefit from high-quality training to keep up with the changes and gain useful AI skills.

In my years of working in education, I’ve felt that the world has enough low-quality courses, newsletters, social media posts, and other forms of content.  It’s possible to build a business churning out mediocre content in sufficient volume to attract a meaningful amount of attention, but I have no interest in doing that.

At https://t.co/zpIxRSuky4, our core philosophy is to put learners first. Our team obsesses about how to create quality training or other programs that benefit people who want to learn about AI. We have intense debates about what tools to teach, which examples to include, even which partners to work with, based on what we think is best for learners.

For example, I recall vividly how, when working on the Machine Learning Specialization, our team spent ages debating whether to use row or column matrices. Both sides showed up with deep analysis of the pros and cons, made Powerpoint presentations to argue their case, and we spent hours debating over what was better for learners in terms of both ease of picking up the concepts as well as subsequently being able to use these skills with third-party machine learning libraries.

We don’t release a course unless we think it’s a good use of a learner’s time and we’d be proud to recommend it to our own friends and family members. Quality, of course, can mean a lot of things. I expect what we do to be technically accurate, useful, up to date, clear, and time-efficient for learners. And, if possible, fun!

We don’t always get it right, but we scrutinize learner feedback (one of my most important weekly routines is to study a dashboard that summarizes learner ratings of our courses) and work to make sure our courses serve learners well. And yes, we have a large-language model powered application that reads learner reviews to flag important issues quickly.

Earlier this year, we realized that some of the paid content we had launched was below our quality standard, and that I wouldn’t in good conscience recommend it to my friends or family members. Despite this content being profitable, we did what we felt was the right thing for learners. So we decided to retire that content and forgo the revenues, but we feel much better now for having done the right thing for learners.

When we teach courses with partners, we tell them our priorities are “learners first, partners second, ourselves last.” I’m grateful to the many wonderful companies and individuals that work with us to teach cutting-edge techniques, and given an opportunity we try to support our partners’ goals as well. But we never prioritize the interest of our educational partners over that of learners. Fortunately, our partners are onboard with this as well. We have a common goal to serve learners. Without their help, it would be difficult to teach many of the topics we do with high-quality content.

Quite a few companies have tried to offer to pay us to teach a course with them, but we’ve always said no. We work only with the companies that we think help us serve learners best, and are not interested in being paid to teach lower quality courses.

One reason I obsess about building quality training materials is that I think learning must be a habit. Learning a little every week is important to get through the volume of learning we all need, and additionally to keep up with changing technology. High-quality training that’s also fun supports a healthy learning habit!

Fun fact: In addition to taking online courses, I also read a lot. Recently I noticed that my digital reading app says I’ve been on a reading streak for 170 weeks. I’ve used the app for many years, but apparently I had broken and restarted my streak 170 weeks ago. What happened then? That was the week that my son was born, Coursera became a public company, and my grandfather died. While my life has had disruptions since then, I was happy to find that it takes a disruption of this magnitude to make me pause my learning habit for a week.

[Original text: https://t.co/OXdmYHgrR1 ]

当 The Batch 刊发第 256 期之际，我不禁回顾 AI（人工智能）这些年的发展历程，以及社会如何随之不断演变。随着 AI 的日益普及，一个显而易见的事实是，无论是开发者还是非开发者，许多人都将从高质量的培训中受益，从而跟上技术变革的步伐，掌握实用的 AI 技能。

在我多年从事教育工作的生涯中，我深感市面上充斥着大量低质量的课程、新闻邮件、社交媒体帖子以及其他形式的内容。虽然以量取胜、大量炮制平庸内容或许能吸引足够的关注并建立起一番事业，但我对此毫无兴趣。

在 https://t.co/zpIxRSuky4，我们的核心理念是始终把学习者放在首位。我们的团队致力于深入思考如何创建高质量的培训或其他项目，从而真正造福那些渴望学习 AI 的人。我们围绕教授哪些工具、选择哪些案例，甚至与哪些合作伙伴合作等问题展开过激烈的讨论，所有这些考量都基于我们认为什么对学习者最有利。

例如，我清楚地记得，在开发机器学习专业课程时，我们的团队曾花了大量时间争论究竟是应该使用行矩阵还是列矩阵。双方都带着对各自优缺点的深入分析，制作了 Powerpoint 演示文稿来阐述观点。我们花费了数小时讨论，哪种方式对学习者而言更好，这既包括他们掌握概念的容易程度，也包括他们随后将这些技能应用于第三方机器学习库的能力。

除非我们认为一门课程真正值得学习者投入时间，并且我们非常乐意将其推荐给我们的朋友和家人，否则我们绝不会发布。当然，「质量」的内涵十分丰富。我期望我们所做的每一件事都能做到技术准确、实用、及时更新、清晰易懂，并且对学习者来说是高效省时的。如果可能的话，还要充满乐趣！

我们并非总能做到完美，但我们会认真审视学习者的反馈（我最重要的每周例行工作之一，就是研究一个汇总学员对我们课程评价的仪表盘），并努力确保我们的课程能更好地服务于学习者。是的，我们还拥有一款由大语言模型（Large Language Model）驱动的应用程序，它能够阅读学习者评论，并迅速标记出重要问题。

今年早些时候，我们意识到之前推出的一些付费内容未能达到我们的质量标准，我无法问心有愧地将它们推荐给我的朋友或家人。尽管这些内容能够盈利，但我们还是做了我们认为对学习者正确的事情。因此，我们决定停用这些内容并放弃由此带来的收益，但现在我们为对学习者做了正确的事情而感到心安理得。

当我们与合作伙伴共同授课时，我们会明确告诉他们，我们的优先顺序是「学习者第一，合作伙伴第二，我们自己最后」。我非常感谢众多优秀的机构和个人与我们携手教授前沿技术。在有机会的情况下，我们也会努力支持合作伙伴的目标。但我们绝不会将教育合作伙伴的利益置于学习者的利益之上。幸运的是，我们的合作伙伴也对此深表认同。我们共同的目标是服务好学习者。没有他们的帮助，我们很难以高质量的内容教授我们所涉及的诸多主题。

不少公司曾主动提出付费，希望与我们合作开设课程，但我们始终拒绝。我们只与那些我们认为能帮助我们更好地服务学习者的公司合作，并且不愿为了报酬去教授低质量的课程。

我之所以执着于打造高质量的培训材料，其中一个原因是，我认为学习必须成为一种习惯。每周持续学习一点点，对于消化我们所需的大量知识至关重要，同时也能帮助我们跟上不断变化的技术。高质量且有趣的培训，正是培养健康学习习惯的有力保障！

趣闻：除了参加在线课程，我也阅读了大量书籍。最近我注意到我的数字阅读应用程序显示，我已经连续阅读了 170 周。我使用这款应用已经很多年了，但显然我的阅读连贯性是在 170 周前中断并重新开始的。那时发生了什么？那是我的儿子出生、Coursera 成为上市公司、以及我祖父去世的那一周。尽管此后我的生活也不乏打扰，但我很高兴地发现，只有如此重大的变故，才能让我暂停一周的学习习惯。

[原文：https://t.co/OXdmYHgrR1]

### 078

作者: @AndrewYNg
时间: 2024-07-10
链接: https://x.com/AndrewYNg/status/1811065347841348052
互动: Likes: 782; Retweets: 156; Replies: 18; Quotes: 8; Views: 71,249; Bookmarks: 394; isReply: 0

Learn to optimize RAG for cost and performance in our new short course, Prompt Compression and Query Optimization, created with @MongoDB and taught by @richmondalake. 

This course teaches you to combine traditional database capabilities with vector search using MongoDB for RAG. You'll learn these techniques:
- Vector search: For semantic matching of user queries
- Filtering using metadata: Pre- and post-filtering to narrow search results
- Projections: Selecting only necessary fields to minimize data returned
- Boosting: Reranking results to improve relevance
- Prompt compression: Using a small LLM to compress context, significantly reducing token count and processing costs

These methods address scaling, performance, and security challenges in large-scale RAG applications. 

You can sign up here: https://t.co/Z7KwOXlx7i

在我们的新短课程《提示压缩和查询优化》中，您将学习如何优化检索增强生成（RAG）的成本和性能。这门课程由 MongoDB 合作开发，并由 Richmond Alake 教授。

本课程将教您如何利用 MongoDB 将传统数据库功能与向量搜索结合起来，应用于 RAG。您将学习以下实用技巧：
- 向量搜索：实现用户查询的语义匹配。
- 使用元数据过滤：通过预过滤和后过滤，有效缩小搜索结果范围。
- 投影：只选择必要的字段，以最大限度地减少返回的数据量。
- 提升：重新排序搜索结果，从而提高其相关性。
- 提示压缩：利用小型大语言模型（LLM）压缩上下文，显著减少 Token 数量和处理成本。

这些方法能够有效解决大规模 RAG 应用程序在扩展性、性能和安全性方面面临的挑战。

您可以在此处注册：https://t.co/Z7KwOXlx7i

### 079

作者: @AndrewYNg
时间: 2024-07-11
链接: https://x.com/AndrewYNg/status/1811425437048070328
互动: Likes: 2,175; Retweets: 502; Replies: 132; Quotes: 84; Views: 455,274; Bookmarks: 465; isReply: 0

I continue to be alarmed at the progress of proposed California regulation SB 1047 and the attack it represents on open source and more broadly on AI innovation. As I wrote previously, this proposed law makes a fundamental mistake of regulating AI technology instead of AI applications, and thus would fail to make AI meaningfully safer. I’d like to explain why the specific mechanisms of SB 1047 are so pernicious to open source.

To be clear, there are routes that regulators should pursue to improve safety. For example, I would welcome outlawing nonconsensual deepfake pornography, standardizing watermarking and fingerprinting to identify generated content, and investing more in red teaming and other safety research. Unfortunately, the proposed bill pursues a less beneficial and more harmful path.

SB 1047’s purported goal is to ensure safety of AI models. It puts in place complex reporting requirements for developers who fine-tune models or develop models that cost more than $100 million to train. It is a vague, ambiguous law that imposes significant penalties for violations, creating a huge gray zone in which developers can’t be sure how to avoid breaking the law. This will paralyze many teams.

You can read the latest draft of the law online. I’ve read through it carefully, and I find it ambiguous and very hard to follow.

Developers who try to navigate the law’s complex requirements face what feels like a huge personal risk. It requires that developers submit, under penalty of perjury, a certification of compliance with the requirements of the law. But when the requirements are complex, hard to understand, and can even shift according to the whims of an unelected body (more on this below), how do we ensure we are in compliance?

For example, the certification must include many different sections. One is an analysis of “the nature and magnitude of critical harms … the model might reasonably cause or enable.” But given that even leading AI researchers aren’t sure what harms models might cause or enable, how is a team of developers supposed to figure this out and declare — under penalty of perjury — that they meet this requirement?

Further, some developers will be required to implement “protections to prevent … misuse of, or unsafe post-training modifications of, the covered model and all covered model derivatives … that are appropriate in light of the risks associated with the covered model, including from advanced persistent threats or other sophisticated actors.” Even leading AI researchers don’t agree on how best to “protect” AI models against these supposed risks, or what would be “appropriate.” So how are developers supposed to figure out how to comply with this requirement?

This creates a scary situation for developers. Committing perjury could lead to fines and even jail time. Some developers will have to hire expensive lawyers or consultants to advise them on how to comply with these requirements. (I am not a lawyer and am not giving legal advice, but one way to try to avoid perjury is to show that you are relying on expert advice, to demonstrate that you had no intent to lie.) Others will simply refrain from releasing cutting-edge AI products.

If this law passes, the fear of a trial by a jury — leading to a verdict that can be very unpredictable and with significant penalties in the event of a conviction — will be very real. What if someone releases a model today after taking what they genuinely felt were reasonable safeguards, but a few years later, when views on AI technology might have shifted, some aggressive prosecutor manages to convince a jury that whatever they did was not, in hindsight, “reasonable”? 

Reasonableness is ambiguous and its legal interpretation can depend on case law, jury instructions, and common facts, among other things. This makes it very hard to ensure that what a developer does today will be deemed reasonable by a future jury. (For more on this, see Context Fund’s analysis of SB 1047. [URLs in article linked to below.])

One highly placed lawyer in the California government who studied this law carefully told me they found it hard to understand. I invite you to read it and judge for yourself — if you find the requirements clear, you might have a brilliant future as a lawyer!

Adding to the ambiguity, the bill would create a Frontier Model Division (FMD) with a five-person board that has the power to dictate standards to developers. This small board would be a great target for lobbying and regulatory capture. (Bill Gurley has a great video on regulatory capture.) The unelected FMD can levy fees on developers to cover its costs. It can arbitrarily change the computation threshold at which fine-tuning a model becomes subject to its oversight. This can lead to even small teams being required to hire an auditor to check for compliance with an ambiguous safety standard.

These provisions don’t ensure that AI is safe. They create regulatory uncertainty, and more opportunities for vested interests wishing to stifle open-source to lobby for shifts in the requirements that raise the cost of compliance. This would lock out many teams that don’t have a revenue stream — specifically, many open-source contributors — that would let them pay for lobbyists, auditors, and lawyers to help ensure they comply with these ambiguous and unreasonable requirements.

Open source is a wonderful force that is bringing knowledge and tools to many people, and is a key pillar of AI innovation. I am dismayed at the concerted attacks on it. Make no mistake, there is a fight in California right now for the future health of open source. I am committed to doing what I can to preserve open source, but I don’t assume that the pro-open source side will prevail. I hope you will join me in speaking out against SB 1047 and other laws that threaten to stifle open source.

[Original text (with links): https://t.co/whAndl5C2g ]

加州拟议的 SB 1047 法规正在不断推行，这让我持续感到警惕，它代表着对开源乃至更广泛的 AI 创新发起了一场攻击。正如我此前所写，这项拟议法律犯了一个根本性错误，即它监管的是 AI 技术本身，而非 AI 的具体应用，因此无法真正让 AI 变得更安全。我想借此机会，解释 SB 1047 的具体机制为何对开源领域如此有害。

诚然，监管机构确实应该探索一些途径来提高 AI 安全性。例如，我非常支持取缔未经同意的深度伪造色情内容、推广水印和指纹技术以识别生成内容，以及加大对红队测试（red teaming）和其他安全研究的投入。然而，令人遗憾的是，这项拟议法案却选择了一条收效甚微且危害更大的道路。

SB 1047 的目标声称是为了确保 AI 模型的安全。它对那些微调模型或开发训练成本超过 1 亿美元模型的开发者施加了复杂的报告要求。这项法律条文含糊不清、模棱两可，对违规行为规定了严厉的惩罚，从而制造了一个巨大的灰色地带，让开发者难以确定如何才能合法合规。这无疑将使许多团队的工作举步维艰。

您可以在线阅读该法律的最新草案。我仔细研读后发现，它确实晦涩难懂，让人难以理解。

试图理解并遵循该法律复杂要求的开发者，仿佛面临着巨大的个人风险。法律要求开发者在承担伪证罪风险的前提下，提交一份声明其符合法律要求的认证。但当这些要求既复杂又难以理解，甚至可能根据一个未经选举的机构的意愿而随意改变时（下文将详细说明），我们又如何能确保自己完全合规呢？

举例来说，该认证必须包含许多不同的部分。其中一项是对「模型可能合理导致或助长的关键危害的性质和严重程度」进行分析。然而，鉴于即使是顶尖的 AI 研究人员也无法完全确定模型可能造成或助长哪些危害，一个开发团队又该如何弄清这些，并承诺 —— 在承担伪证罪风险的前提下 —— 他们符合这项要求呢？

此外，一些开发者还将被要求实施「保护措施，以防止... 被涵盖模型及其所有衍生模型被误用或进行不安全的模型后训练修改... 这些措施应根据被涵盖模型所面临的风险，包括来自高级持续性威胁（advanced persistent threats）或其他复杂攻击者的风险，进行适当调整。」即使是领先的 AI 研究人员也未能就如何最好地「保护」AI 模型免受这些潜在风险，或者何种措施才算「适当」达成一致。那么，开发者又该如何摸索出一条合规之路呢？

这为开发者创造了一个令人担忧的局面。一旦被判伪证罪，可能面临罚款甚至牢狱之灾。一些开发者将不得不聘请昂贵的律师或顾问来指导他们如何遵守这些要求。(我并非律师，也无意提供法律建议，但避免伪证罪的一种方法是表明您依赖了专家建议，以此证明您没有撒谎的意图。）而另一些人则会干脆放弃发布前沿的 AI 产品。

如果这项法律得以通过，那么被陪审团审判的恐惧将变得真真切切 —— 这种审判结果往往难以预测，一旦定罪，将面临严厉的惩罚。试想，如果有人在今天发布了一个模型，当时他们真诚地认为已经采取了合理的安全措施，但几年后，当人们对 AI 技术的看法可能发生变化时，某个积极的检察官却设法说服陪审团，认为他们当时所做的一切，事后看来并不「合理」，那该怎么办？

「合理性」本身就是一个模糊的概念，其法律解释可能取决于判例法、陪审团指示以及具体案情等多种因素。这使得开发者很难确保他们今天所做的事情，在未来会被陪审团认定为合理。(关于这一点，请参阅 Context Fund 对 SB 1047 的分析。)

加州政府中一位对这项法律进行过深入研究的高级律师告诉我，他们也觉得这项法律难以理解。我邀请您亲自阅读并判断 —— 如果您认为这些要求清晰明了，那么您或许拥有成为一名杰出律师的潜力！

除了模糊性之外，该法案还将设立一个名为前沿模型部门（Frontier Model Division，FMD）的机构，由一个五人委员会组成，该委员会有权向开发者制定标准。这个小型委员会将极易成为游说和监管俘获（regulatory capture）的目标。(Bill Gurley 有一个关于监管俘获的精彩视频。）这个未经选举产生的 FMD 可以向开发者征收费用来弥补其运营成本。它还可以随意调整微调模型何时需要接受其监管的计算阈值。这可能导致即使是小型团队，也需要聘请审计师来检查是否符合那些模糊的安全标准。

这些条款并不能真正确保 AI 的安全性。它们只会制造监管不确定性，并为那些希望扼杀开源的既得利益者提供更多机会，让他们游说修改要求，从而抬高合规成本。这无疑会将许多没有收入来源的团队 —— 特别是众多的开源贡献者 —— 排除在外，因为他们将无法支付游说者、审计师和律师的费用，以确保他们能够遵守这些模糊且不合理的要求。

开源是一股令人赞叹的力量，它将知识和工具带给无数人，也是 AI 创新的关键支柱。我对其遭受的有组织攻击感到沮丧。毋庸置疑，加州目前正在进行一场事关开源未来发展的激烈斗争。我致力于尽我所能地维护开源，但我也不会想当然地认为支持开源的一方一定会获胜。我希望您能与我一道，大声疾呼反对 SB 1047 以及其他可能扼杀开源的法律。

### 080

作者: @AndrewYNg
时间: 2024-07-17
链接: https://x.com/AndrewYNg/status/1813591557511295234
互动: Likes: 986; Retweets: 206; Replies: 30; Quotes: 14; Views: 85,009; Bookmarks: 488; isReply: 0

New short course on Pretraining LLMs! Developed with @UpstageAI and taught by their CEO @hunkims and CSO @echojuliett.

While prompting or fine-tuning existing models works well for many general language tasks, pretraining is  valuable for specialized domains or languages with limited representation in current models.

This course walks you through the LLM pretraining pipeline:
1. Data preparation: Learn to source, clean, and prepare training data using HuggingFace.
2. Model architecture: Configure transformer networks, including modifying existing models.
3. Training: Set up and run training using open-source libraries.
4. Evaluation: Benchmark performance using popular evaluation strategies.

As an example use case, you'll also compare the output of a base model with its fine-tuned and further pretrained variants, to see the impact of pretraining on a model's ability to write Python. 

The course also explores an innovative technique called depth up-scaling, which Upstage used to train their Solar model family, reducing pretraining compute costs by up to 70%. This technique works by first duplicating layers of a smaller pretrained model to form a larger model, and then further pretraining the result.

Sign up here! https://t.co/IjYmNPR7sd

预训练大语言模型的新短期课程来啦！本课程与 @UpstageAI 联合开发，由其 CEO @hunkims 和 CSO @echojuliett 亲自讲解。

尽管对现有模型进行提示（prompting）或微调（fine-tuning）在许多通用语言任务上表现出色，但预训练（pretraining）对于专业领域或数据代表性不足的语言来说，仍然具有不可替代的价值。

本课程将带你深入探索大语言模型的预训练流程：
1. ** 数据准备 **：学习如何使用 HuggingFace 获取、清洗和准备训练数据。
2. ** 模型架构 **：配置 Transformer（Transformer）网络，包括如何修改现有模型。
3. ** 训练 **：使用开源库设置并运行模型训练。
4. ** 评估 **：运用流行的评估策略对模型性能进行基准测试。

作为实践案例，你还会比较一个基础模型与经过微调和进一步预训练的变体模型，亲眼见证预训练如何提升模型生成 Python 代码的能力。

此外，本课程还会介绍一项名为深度扩展（depth up-scaling）的创新技术。Upstage 公司正是利用这项技术训练了他们的 Solar 模型家族，从而将预训练的计算成本降低了高达 70%！这项技术的核心原理是：首先复制一个较小预训练模型的层，以构建一个更大的模型，然后再对这个新形成的更大模型进行进一步的预训练。

点击这里报名！https://t.co/IjYmNPR7sd

### 081

作者: @AndrewYNg
时间: 2024-07-23
链接: https://x.com/AndrewYNg/status/1815792223411429741
互动: Likes: 1,717; Retweets: 215; Replies: 36; Quotes: 12; Views: 104,425; Bookmarks: 85; isReply: 0

Thank you Meta and the Llama team for your huge contributions to open-source! Llama 3.1 with increased context length and improved capabilities is a wonderful gift to everyone. 

I hope foolish regulations don't like California's proposed SB1047 don't stop such innovations.

感谢 Meta 和 Llama 团队为开源社区做出的巨大贡献！Llama 3.1 版本，凭借其更长的上下文长度和更强的能力，无疑是送给大家的一份厚礼。

我真心希望，不要让像加利福尼亚州提议的 SB1047 这样的愚蠢法规，阻碍了此类创新。

### 082

作者: @AndrewYNg
时间: 2024-07-24
链接: https://x.com/AndrewYNg/status/1816171538275787145
互动: Likes: 656; Retweets: 128; Replies: 20; Quotes: 11; Views: 63,905; Bookmarks: 323; isReply: 0

Learn to train an LLM with distributed data while ensuring privacy using federated learning in a new two-part short course, Intro to Federated Learning and Federated Fine-tuning of LLMs with Private Data, created with @flwrlabs and taught by @daniel_janes and @niclane7.

Federated learning allows a single model to be trained across multiple devices, such as phones, or multiple organizations, such as hospitals, without the need to share data to a central server.

This two-part course gives you an introduction to federated learning, and then teaches you how to fine-tune your large language model with distributed data using Flower Lab’s open source federated learning framework.

You’ll learn:
- How to use federated learning to train a variety of models, ranging from speech and vision models to LLMs, across distributed data while offering data privacy options to users and organizations.
- Privacy Enhancing Technologies like differential privacy (DP), which obscures individual data by adding calibrated noise to query results.
- Two variants of differential privacy - Central and Local - and how to choose depending on your use case.
- How to measure and decrease bandwidth usage to make federated learning more practical and efficient with techniques like using pre-trained models and Parameter-Efficient Fine-Tuning
- How federated LLM fine-tuning reduces the risk of leaking training data.

Sign up here! https://t.co/cuN1n0ylee

在新的两部分短期课程中，学习如何利用联邦学习（Federated Learning），在确保数据隐私的前提下，使用分布式数据训练大语言模型（LLM）。这门课程名为「联邦学习简介与基于私有数据的联邦大语言模型微调」，由 @flwrlabs 创建，并由 @daniel_janes 和 @niclane7 授课。

联邦学习允许在多个设备（例如手机）或多个组织（例如医院）上训练单个模型，而无需将数据共享到中央服务器。

这个两部分的课程将向你介绍联邦学习，然后教你如何使用 Flower Lab 的开源联邦学习框架，利用分布式数据微调你的大语言模型。

你将学到：
- 如何使用联邦学习，在分布式数据上训练各种模型，包括从语音模型、视觉模型到大语言模型（LLM），同时为用户和组织提供数据隐私选项。
- 隐私增强技术（Privacy Enhancing Technologies），例如差分隐私（DP），它通过向查询结果添加经过校准的噪声来模糊个人数据。
- 差分隐私的两种变体 —— 中央式和局部式 —— 以及如何根据你的具体用例进行选择。
- 如何通过使用预训练模型和参数高效微调（Parameter-Efficient Fine-Tuning）等技术，衡量并减少带宽使用，使联邦学习更实用、更高效。
- 联邦大语言模型（LLM）微调如何降低训练数据泄露的风险。

在此注册！ https://t.co/cuN1n0ylee

### 083

作者: @AndrewYNg
时间: 2024-07-30
链接: https://x.com/AndrewYNg/status/1818320842654371918
互动: Likes: 581; Retweets: 114; Replies: 90; Quotes: 14; Views: 58,787; Bookmarks: 327; isReply: 0

AI’s usefulness in a wide variety of applications creates many opportunities for entrepreneurship. Here, I’d like to share what might be a counter-intuitive best practice that I’ve learned from leading AI Fund, a venture studio that has built dozens of startups with extraordinary entrepreneurs. When it comes to building AI applications, we strongly prefer to work on a concrete idea, meaning a specific product envisioned in enough detail that we can build it for a specific target user.

Some design philosophies say you shouldn’t envision a specific product from the start. Instead, they recommend starting with a problem to be solved and then carefully studying the market before you devise a concrete solution. There’s a reason for this: The more concrete or precise your product specification, the more likely it is to be off-target. However, I find that having something specific to execute toward lets you go much faster and discover and fix problems more rapidly along the way. If the idea turns out to be flawed, rapid execution will let you discover the flaws sooner, and this knowledge and experience will help you switch to a different concrete idea.

One test of concreteness is whether you’ve specified the idea in enough detail that a product/engineering team could build an initial prototype. For example, “AI for livestock farming” is not concrete; it’s vague. If you were to ask an engineer to build this, they would have a hard time knowing what to build.  Similarly, “AI for livestock tracking in farming” is still vague. There are so many approaches to this that most reasonable engineers wouldn’t know what to build. But “Apply face recognition to cows so as to recognize individual cows and monitor their movement on a farm” is specific enough that a good engineer could quickly choose from the available options (for example, what algorithm to try first, what camera resolution to use, and so on) to let us relatively efficiently assess:
- Technical feasibility: For example, do face recognition algorithms developed for human faces work for cows? (It turns out that they do!)
- Business feasibility: Does the idea add enough value to be worth building? (Talking to farmers might quickly reveal that solutions like RFID are easier and cheaper.)

Articulating a concrete idea — which is more likely than a vague idea to be wrong — takes more courage. The more specific an idea, the more likely it is to be a bit off, especially in the details. The general area of AI for livestock farming seems promising, and surely there will be good ways to apply AI for livestock. In contrast, specifying a concrete idea, which is much easier to invalidate, is scary.

The benefit is that the clarity of a specific product vision lets a team execute much faster. One strong predictor of how likely a startup is to succeed is the speed with which it can get stuff done. This is why founders with clarity of vision tend to be desired; clarity helps drive a team in a specific direction. Of course, the vision has to be a good one, and there’s always a risk of efficiently building something that no one wants to buy! But a startup is unlikely to succeed if it meanders for too long without forming a clear, concrete vision.

Building toward something concrete — if you can do so in a responsible way that doesn’t harm others — lets you get critical feedback more efficiently and, if necessary, switch directions sooner. (An earlier letter in The Batch also discussed when it’s better to go with a “Ready, Fire, Aim” approach to projects.) One factor that favors this approach is the low cost of experimenting and iterating. This is increasingly the case for many AI applications, but perhaps less so for deep-tech AI projects.

I realize that this advice runs counter to common practice in design thinking, which warns against leaping to a solution too quickly, and instead advocates spending time understanding end-users, deeply understanding their problems, and brainstorming a wide range of solutions. If you’re starting without any ideas, then such an extended process can be a good way to develop good ideas. Further, keeping ideas open-ended can be good for curiosity-driven research, where investing to pursue deep tech with only a vague direction in mind can pay huge dividends over the long term.

If you are thinking about starting a new AI project, consider whether you can come up with a concrete vision to execute toward. Even if the initial vision turns out not to be quite right, rapid iteration will let you discover this sooner, and the learnings will let you switch to a different concrete idea.

[Original text: https://t.co/8CkePKyBJ4 ]

人工智能（AI）在各种应用中的广泛前景，为创业带来了许多机会。在这里，我想分享一个我从领导 AI Fund 学到的、可能有点反直觉（counter-intuitive）的最佳实践。AI Fund 是一家风险投资工作室（venture studio），已经与众多杰出的企业家合作建立了数十家初创公司。在开发人工智能应用时，我们强烈倾向于专注于一个具体的想法 —— 这意味着这个特定产品在构想时必须足够详细，以便我们能够为特定的目标用户将其付诸实现。

有些设计理念认为，你不应该从一开始就设想一个具体的产品。相反，他们建议先从一个有待解决的问题入手，然后仔细研究市场，之后再设计出具体的解决方案。这样做的理由是：你的产品规范越具体或越精确，就越有可能偏离目标。然而，我发现，拥有一个具体的执行目标能让你前进得更快，并在此过程中更迅速地发现和解决问题。如果某个想法被证实有缺陷，快速执行将让你更快地发现这些缺陷，而这些知识和经验将帮助你转向一个不同的具体想法。

如何衡量一个想法是否具体呢？一个检验标准是，你是否已经足够详细地阐述了这个想法，以便产品 / 工程团队可以构建一个初始原型。例如，「用于畜牧业的人工智能」就不具体；它很模糊。如果你让一位工程师基于这个模糊想法进行开发，他们将很难知道具体要做什么。同样，「用于畜牧业牲畜追踪的人工智能」仍然模糊。实现这一目标的方法太多了，大多数有经验的工程师都不知道该选择哪种方案来构建。但是，「将面部识别应用于奶牛，以识别个体奶牛并监测它们在农场上的活动」就足够具体了。一位优秀的工程师可以快速从现有选项中进行选择（例如，首先尝试哪种算法，使用什么摄像头分辨率等），从而让我们相对高效地评估：
- 技术可行性：例如，为人类面部开发的面部识别算法是否适用于奶牛？（事实证明，它们确实适用！）
- 商业可行性：这个想法是否能创造足够的价值，值得我们投入开发？（与农民交流可能会很快发现，RFID 等解决方案可能更简单、更便宜。）

提出一个具体的想法 —— 这比模糊的想法更有可能出错 —— 需要更大的勇气。一个想法越具体，它就越有可能在细节上出现偏差。虽然「用于畜牧业的人工智能」这个大方向看起来很有前景，而且肯定会有好方法将人工智能应用于畜牧业，但相比之下，提出一个具体的、更容易被证伪的想法，确实令人望而生畏。

这样做的好处是，清晰的产品愿景能让团队执行得更快。衡量一家初创公司成功可能性的一个重要预测因素，就是它完成工作（get stuff done）的速度。这就是为什么那些具有清晰愿景的创始人备受追捧的原因；清晰度有助于推动团队朝着一个特定方向前进。当然，这个愿景必须是好的，而且总有高效地构建出无人想购买的东西的风险！但如果一家初创公司长时间漫无目的地徘徊，没有形成一个清晰、具体的愿景，它就不太可能成功。

朝着具体的目标努力 —— 如果你能以负责任的方式做到这一点，并且不伤害他人 —— 能让你更有效地获得关键反馈，并在必要时更快地改变方向。（《The Batch》上更早的一封信也讨论了何时最好采用「Ready，Fire，Aim」的方法来处理项目。）支持这种方法的一个因素是实验和迭代的低成本。对于许多人工智能应用来说，这种情况越来越普遍，但对于硬科技（deep-tech）人工智能项目可能并非如此。

我意识到，这个建议与设计思维（design thinking）中的常见做法有所不同，设计思维警告不要过快地跳到解决方案，而是主张花时间了解最终用户，深入理解他们的问题，并集思广益提出广泛的解决方案。如果你在没有任何想法的情况下开始，那么这样一个扩展的过程可能是一个产生好想法的好方法。此外，保持想法开放式对于好奇心驱动的研究可能是有益的，在这种研究中，即使心中只有模糊的方向，投资于追求硬科技，从长远来看也可能带来巨大的回报。

如果你正在考虑启动一个新的 AI 项目，请思考你是否能提出一个具体的愿景作为执行方向。即使最初的愿景被证实不完全正确，快速迭代也将让你更快地发现这一点，并且所学到的经验将帮助你转向一个不同的具体想法。

[Original text：https://t.co/8CkePKyBJ4]

### 084

作者: @AndrewYNg
时间: 2024-07-31
链接: https://x.com/AndrewYNg/status/1818666105340330260
互动: Likes: 716; Retweets: 147; Replies: 23; Quotes: 8; Views: 71,347; Bookmarks: 389; isReply: 0

Learn how embedding models are built, trained, and used in semantic search systems in this new short course, Embedding Models: From Architecture to Implementation, created with @vectara and taught by @ofermend.

Many LLM apps use a single embedding model for both questions and answers. This can lead to issues such as retrieving results that are similar to the question itself rather than relevant answers. With a dual encoder architecture, you can use separate embedding models for questions and answers to better match questions with appropriate answers.

In this course, you will use, build, and train a dual encoder model.

You’ll also learn:
- What are word embeddings, and how they are used
- The evolution of embeddings to BERT, where embeddings take into account each word's surrounding context  
- How a contrastive loss is used to train a dual encoder model with one encoder trained to embed questions and the other responses.
- How to analyze a dual encoder’s effect on search relevance and compare it to a retrieval process with a single encoder.

Please sign up here! https://t.co/4wuz0vAw6X

在这门由 @vectara 创建、@ofermend 讲授的新短课程《嵌入模型：从架构到实现》中，你将学习如何在语义搜索系统中构建、训练和使用嵌入模型。

许多大语言模型（LLM）应用程序在处理问题和答案时，都只使用一个嵌入模型。这可能导致检索到的结果与问题本身过于相似，而非真正相关的答案，从而产生问题。而通过双编码器（dual encoder）架构，你可以为问题和答案分别使用独立的嵌入模型，从而更好地将问题与恰当的答案匹配起来。

在本课程中，你将亲自动手使用、构建和训练一个双编码器模型。

你还将学习：
- 什么是词嵌入（word embeddings），以及它们是如何被使用的。
- 嵌入技术如何演变到 BERT 模型，其中嵌入会考虑每个词的上下文信息。
- 如何使用对比损失（contrastive loss）来训练一个双编码器模型，其中一个编码器负责处理问题，另一个则负责处理响应。
- 如何分析双编码器对搜索相关性的影响，并将其与使用单编码器的检索过程进行比较。

请在此注册！ https://t.co/4wuz0vAw6X

### 085

作者: @AndrewYNg
时间: 2024-08-06
链接: https://x.com/AndrewYNg/status/1820863062993490137
互动: Likes: 947; Retweets: 194; Replies: 24; Quotes: 11; Views: 118,669; Bookmarks: 1,011; isReply: 0

I wrote last week about why working on a concrete startup or project idea — meaning a specific product envisioned in enough detail that we can build it for a specific target user — lets you go faster. In this letter, I’d like to share some best practices for identifying promising ideas. 

AI Fund, which I lead, works with many corporate partners to identify ideas, often involving applications of AI to the company’s domain. Because AI is applicable to numerous sectors such as retail, energy, logistics and finance, I’ve found working with domain experts who know these areas well immensely helpful for identifying what applications are worth building in these areas.

Our brainstorming process starts with recommending that a large number of key contributors at our partner corporation (at least 10 but sometimes well over 100) gain a non-technical, business-level understanding of AI and what it can and can’t do. Taking https://t.co/zpIxRSuky4’s “Generative AI for Everyone” course is a popular option, after which a company is well positioned to assign a small team to coordinate a brainstorming process, followed by a prioritization exercise to pick what to work on. The brainstorming process can be supported by a task-based analysis of jobs in which we decompose employees’ jobs into tasks to identify which ones might be automated or augmented using AI.

Here are some best practices for these activities:

(i) Trust the domain expert’s gut. A domain expert who has worked for years in a particular sector will have well honed instincts that let them make leaps that would take a non-expert weeks of research.

Let’s say we’re working with a financial services expert and have developed a vague idea (“build a chatbot for financial advice”). To turn this into a concrete idea, we might need to answer questions such as what areas of finance to target (should we focus on budgeting, investing, or insurance?) and what types of user to serve (fresh graduates, mortgage applicants, new parents, or retirees?) Even a domain expert who has spent years giving financial advice might not know the best answer, but a choice made via their gut gives a quick way to get to one plausible concrete idea. Of course, if market-research data can be obtained quickly to support this decision, we should take advantage of it. But to avoid slowing down too much, we’ve found that experts’ gut reactions work well and are a quick way to make decisions.

So, if I’m handed a non-concrete idea, I often ask a domain expert to use their gut — and nothing else — to quickly make decisions as needed to make the idea concrete. The resulting idea is only a starting point to be tweaked over time. If, in the discussion, the domain expert picks one option but seems very hesitant to disregard a different option, then we can also keep the second option as a back-up that we can quickly pivot to if the initial one no longer looks promising.

(ii) Generate many ideas. I usually suggest coming up with at least 10 ideas; some will come up with over 100, which is even better. The usual brainstorming advice to go for volume rather than quality applies here. Having many ideas is particularly important when it comes to prioritization. If only one idea is seriously considered — sometimes this happens if a senior executive has an idea they really like and puts this forward as the “main” idea to be worked on — there’s a lot of pressure to make this idea work. Even if further investigation discovers problems with it — for example, market demand turns out to be weak or the technology is very expensive to build — the team will want to keep trying to make it work so we don’t end up with nothing.

In contrast, when a company has many ideas to choose from, if one starts to look less interesting, it’s easy to shift attention to a different one. When many ideas are considered, it’s easier to compare them to pick the superior ones. As explained in the book Ideaflow, teams that generate more ideas for evaluation and prioritization end up with better solutions.

Because of this, I’ve found it helpful to run a broad brainstorming process that involves many employees. Specifically, large companies have many people who collectively have a lot of wisdom regarding the business. Having a small core team coordinate the gathering of ideas from a large number of people lets us tap into this collective fountain of invention. Many times I’ve seen a broad effort (involving, say, ~100 people who are knowledgeable about the domain and have a basic understanding of AI) end up with better ideas than a narrow one (involving, say, a handful of top executives).

(iii) Make the evaluation criteria explicit. When evaluating and prioritizing, clear criteria for scoring and ranking ideas helps the team to judge ideas more consistently. Business value and technical feasibility are almost always included. Additionally, many companies will prioritize projects that can be a quick win (to build momentum for their overall AI efforts) or support certain strategic priorities such as growth in a particular part of the business. Making such criteria explicit can help during the idea-generation phase, and it’s critical when you evaluate and prioritize.

In large companies, it can take a few weeks to go through a process to gather and prioritize ideas, but this pays off well in identifying valuable, concrete ideas to pursue. AI isn’t useful unless we find appropriate ways to apply it, and I hope these best practices will help you to generate great AI application ideas to work on.

[Original text: https://t.co/7pwXMGEbpI ]

我上周的文章讨论了为什么聚焦于一个具体的创业项目或产品构想 —— 即一个足够细致、能针对特定用户打造的产品 —— 可以帮助你更快地取得进展。在今天的这封信中，我想分享一些识别有前景想法的最佳实践。

我领导的 AI Fund 与许多企业伙伴合作，共同发掘新的想法，这些想法通常涉及将 AI 应用到公司特有的业务领域。由于 AI（人工智能）适用于零售、能源、物流和金融等众多行业，我发现与熟悉这些领域的专家合作，对于识别哪些应用值得开发，非常有帮助。

我们的头脑风暴过程始于建议我们的合作公司中大量的核心贡献者（至少 10 人，有时甚至超过 100 人）对 AI 及其能力边界有一个非技术性、业务层面的理解。参加 https://t.co/zpIxRSuky4 上的「Generative AI for Everyone」课程是一个受欢迎的选择。之后，公司就能更好地组建一个小型团队来协调头脑风暴过程，接着进行优先级排序，以确定优先开展哪些工作。头脑风暴过程还可以通过一项任务分析来支持，即我们将员工的工作细分为具体的任务，以识别哪些任务可能通过 AI 实现自动化或增强。

以下是进行这些活动的一些最佳实践：

(i）信任领域专家的直觉。一位在特定行业深耕多年的领域专家，会拥有敏锐的直觉，能够快速做出非专业人士需要数周研究才能得出的判断。

假设我们正与一位金融服务专家合作，并有了一个模糊的想法（「开发一个提供金融建议的聊天机器人」）。为了将这个想法具体化，我们可能需要回答一些问题，例如：要瞄准金融领域的哪个具体方向（我们应该关注预算规划、投资策略，还是保险服务？）以及要服务哪类用户（应届毕业生、抵押贷款申请人、新手父母，还是退休人员？）即使是多年提供金融建议的专家，也可能无法立刻知道最佳答案，但通过他们的直觉做出的选择，能提供一个快速获得合理具体想法的途径。当然，如果能快速获得市场调研数据来支持这个决策，我们应该加以利用。但为了避免进展缓慢，我们发现专家的直觉反应非常有效，是快速做出决策的好方法。

所以，如果我得到一个不够具体的想法，我通常会请领域专家仅仅依靠直觉，快速做出必要的决策，以使想法具体化。由此产生的想法只是一个起点，会随着时间的推移不断调整。如果在讨论中，领域专家选择了一个选项但似乎非常犹豫是否放弃另一个选项，那么我们也可以将第二个选项作为备选方案，如果最初的选项不再有前景，我们就可以迅速转向它。

(ii）产生大量想法。我通常建议至少提出 10 个想法；有些人会提出超过 100 个，这当然更好。头脑风暴中「追求数量而非质量」的常见建议在这里同样适用。在优先级排序时，拥有大量想法尤其重要。如果只有一个想法被认真考虑 —— 比如，某位高级主管提出了一个他非常喜欢并指定为「主要」工作方向的想法 —— 那么这个想法成功的压力就会非常大。即使后续调查发现它存在问题（例如，市场需求疲软或技术开发成本极高），团队也往往会努力使其奏效，以免最终一无所获。

相反，当公司有许多想法可供选择时，如果其中一个看起来不再那么吸引人，就可以轻松地将注意力转移到另一个上。当同时考虑多个想法时，也更容易进行比较，从而选出更优秀的方案。正如《Ideaflow》一书所解释的，生成更多想法进行评估和优先级排序的团队，最终会找到更好的解决方案。

正因为如此，我发现开展一个广泛、多员工参与的头脑风暴过程非常有益。具体来说，大公司拥有众多员工，他们 collectively（共同地）积累了关于业务的丰富智慧。让一个小型核心团队协调从大量员工那里收集想法，能让我们充分利用这种集体的创新源泉。我多次看到，一项广泛的努力（例如，涉及约 100 名对领域了解并对 AI 有基本理解的人）最终产生的想法，要优于一项狭隘的努力（例如，仅涉及少数几位高管）。

(iii）明确评估标准。在评估和优先级排序时，清晰的评分和排名标准有助于团队更一致地判断想法。业务价值和技术可行性几乎总是评估标准中不可或缺的。此外，许多公司还会优先考虑那些能快速取得成功（为整体 AI 部署工作建立势头）或支持特定战略重点（例如在业务的某个特定部分实现增长）的项目。明确这些标准在想法生成阶段会有所帮助，并且在评估和优先级排序时至关重要。

在大型公司中，完成收集和优先级排序想法的过程可能需要几周时间，但这对于识别有价值、可行的具体想法来说，是物有所值的。除非我们找到合适的方法来应用 AI，否则 AI 的潜力将无法发挥。我希望这些最佳实践能帮助你生成出色的 AI 应用想法并付诸实施。

[Original text：https://t.co/7pwXMGEbpI]

### 086

作者: @AndrewYNg
时间: 2024-08-07
链接: https://x.com/AndrewYNg/status/1821206887913943110
互动: Likes: 8,575; Retweets: 1,779; Replies: 487; Quotes: 173; Views: 1,214,911; Bookmarks: 7,991; isReply: 0

I'm teaching a new course! AI Python for Beginners is a series of four short courses that teach anyone to code, regardless of current technical skill. We are offering these courses free for a limited time.

Generative AI is transforming coding. This course teaches coding in a way that’s aligned with where the field is going, rather than where it has been:

(1) AI as a Coding Companion. Experienced coders are using AI to help write snippets of code, debug code, and the like. We embrace this approach and describe best-practices for coding with a chatbot. Throughout the course, you'll have access to an AI chatbot that will be your own coding companion that can assist you every step of the way as you code.

(2) Learning by Building AI Applications. You'll write code that interacts with large language models to quickly create fun applications to customize poems, write recipes, and manage a to-do list. This hands-on approach helps you see how writing code that calls on powerful AI models will make you more effective in your work and personal projects.

With this approach, beginning programmers can learn to do useful things with code far faster than they could have even a year ago.

Knowing a little bit of coding is increasingly helping people in job roles other than software engineers. For example, I've seen a marketing professional write code to download web pages and use generative AI to derive insights; a reporter write code to flag important stories; and an investor automate the initial drafts of contracts.

With this course you’ll be equipped to automate repetitive tasks, analyze data more efficiently, and leverage AI to enhance your productivity.

If you are already an experienced developer, please help me spread the word and encourage your non-developer friends to learn a little bit of coding.

I hope you'll check out the first two short courses here! https://t.co/lTupltSZkT

我正在教授一门新课程！「面向初学者的 AI Python」是一个由四个短期课程组成的系列，旨在教授任何人编码，无论当前的技术技能如何。我们限时免费提供这些课程。

生成式 AI（Generative AI）正在改变编码方式。本课程的编码教学方式与该领域未来的发展趋势保持一致，而非墨守成规：

(1）AI 作为编码伙伴。经验丰富的程序员正在利用 AI 编写代码片段、调试代码等。我们推崇这种方法，并会介绍使用聊天机器人进行编码的最佳实践。在整个课程中，你都将可以使用一个 AI 聊天机器人，它会成为你专属的编码伙伴，在你编写代码的每一步都能提供协助。

(2）通过构建 AI 应用程序进行学习。你将编写与大语言模型（Large Language Model）交互的代码，从而快速创建有趣的应用程序，例如自定义诗歌、撰写食谱和管理待办事项列表。这种动手实践的方法将帮助你理解，如何通过编写调用强大 AI 模型的代码，来提高你在工作和个人项目中的效率。

通过这种教学方法，编程初学者能够比一年前更快地学会用代码完成有用的事情。

掌握一点点编码技能正日益帮助软件工程师以外的职业人群。例如，我曾看到一位营销专业人士编写代码下载网页，并利用生成式 AI 提取有价值的洞察；一位记者编写代码筛选重要新闻；以及一位投资者自动生成合同的初稿。

通过本课程，你将能够自动化重复性任务，更高效地分析数据，并利用 AI 提升你的生产力。

如果你已经是经验丰富的开发人员，请帮助我传播这个消息，并鼓励你的非开发人员朋友学习一点点编码。

希望你在这里查看前两个短期课程！ https://t.co/lTupltSZkT

### 087

作者: @AndrewYNg
时间: 2024-08-09
链接: https://x.com/AndrewYNg/status/1821950054439252385
互动: Likes: 292; Retweets: 69; Replies: 11; Quotes: 8; Views: 72,687; Bookmarks: 38; isReply: 0

There is an chorus of voices across academia, business and even government concerned about California's proposed anti-open source, anti-innovation bill SB 1047. 

@martin_casado has a nice thread summarizing some of these. Thank you @russellwald, @vishalmisra, Ion Stoica, many people from the University of California community, @AnimaAnandkumar, @drfeifei, @garrytan, @AnjneyMidha, Zoe Lofgren and many many others for speaking out to explain why this bill will hurt AI innovation without actually increasing safety. 

If anything, by hurting open source and thus hampering researchers' ability to study cutting-edge models to identify problems, I believe SB1047 is more likely to make AI less safe.

学术界、商界甚至政府各方，都对加州提议的反开源、反创新法案 SB 1047 表达了担忧。

@martin_casado 发了一个帖子，很好地总结了其中的一些担忧。感谢 @russellwald、@vishalmisra、Ion Stoica、来自加州大学社区的许多人、@AnimaAnandkumar、@drfeifei、@garrytan、@AnjneyMidha、Zoe Lofgren 以及其他许多人公开指出，为什么这项法案会损害 AI 创新，而实际上并不会提高安全性。

退一步讲，我相信 SB 1047 通过损害开源，从而阻碍研究人员研究前沿模型以识别问题的能力，反而更有可能让 AI 变得更不安全。

### 088

作者: @AndrewYNg
时间: 2024-08-13
链接: https://x.com/AndrewYNg/status/1823388325409140946
互动: Likes: 169; Retweets: 33; Replies: 23; Quotes: 6; Views: 33,538; Bookmarks: 24; isReply: 0

I’m speaking on a panel this Thursday (3pm PT) about Stratospheric Aerosol Injection (SAI). SAI is a potential approach to reducing global warming, and AI climate modeling has an important role to play in understanding its impact. I look forward to discussing the atmospheric science and social/political factors of SAI with @chrfield @DKeithClimate @DougMacMartin and Simone Tilmes.

Please register here to join us! https://t.co/Algxy9Wxqp

我将在本周四（太平洋时间下午 3 点）参加一个小组讨论会，主题是平流层气溶胶注入（Stratospheric Aerosol Injection，SAI）。SAI 是一种可能有助于缓解全球变暖的方法，而 AI 气候建模在理解其潜在影响方面扮演着重要角色。我非常期待能与 @chrfield @DKeithClimate @DougMacMartin 以及 Simone Tilmes 一起，深入探讨 SAI 所涉及的大气科学原理及其社会 / 政治影响。

欢迎大家点击此链接注册，加入我们的讨论！https://t.co/Algxy9Wxqp

### 089

作者: @AndrewYNg
时间: 2024-08-13
链接: https://x.com/AndrewYNg/status/1823429929381585248
互动: Likes: 197; Retweets: 29; Replies: 15; Quotes: 2; Views: 38,910; Bookmarks: 14; isReply: 0

It is very rare for the U.S. Federal government to chime in  on state-level legislation. I'm glad that Congressman @RoKhanna is speaking out about why California's proposed SB 1047 is a bad idea. 

He writes that he is "concerned that the bill as currently written would be ineffective, punishing of individual entrepreneurs and small businesses, and hurt California’s spirit of innovation." I agree with him. 

https://t.co/V1yf7ERyxw

美国联邦政府很少对州级立法（state-level legislation）发表意见。我很高兴众议员 @RoKhanna 公开表达了他对加州拟议的 SB 1047 法案为何是个糟糕主意的看法。

他写道，他「担心该法案目前的版本将是无效的，会对个体企业家和小型企业造成惩罚性影响，并损害加州的创新精神。」我同意他的观点。

https://t.co/V1yf7ERyxw

### 090

作者: @AndrewYNg
时间: 2024-08-14
链接: https://x.com/AndrewYNg/status/1823759268937650528
互动: Likes: 635; Retweets: 126; Replies: 22; Quotes: 12; Views: 65,971; Bookmarks: 312; isReply: 0

Learn a development pattern to systematically improve the accuracy and reliability of LLM applications in our new short course, Improving Accuracy of LLM Applications, built in partnership with @LaminiAI and @Meta, and taught by Lamini’s CEO @realSharonZhou, and Meta’s Senior Director of Partner Engineering,  @asangani7. (Disclosure: I am an investor in Lamini.)

The path to tuning an LLM application can be complex. In this course, you'll learn a systematic sequence of steps for improving accuracy by reducing hallucinations: 
- Create an evaluation dataset to measure model accuracy
- Add prompt engineering and self-reflection
- Fine-tune your model including "memory-tuning" which is a new method of embedding facts in an LLM

Using the Llama 3-8B parameter model, you will:
- Build a text-to-SQL agent with a custom schema and simulate situations where it hallucinates
- Understand the difference between instruction fine-tuning, which gives pre-trained LLMs instructions to follow, and memory fine-tuning
- See how Performance-Efficient Fine-tuning (PEFT) techniques like Low-Rank Adaptation (LoRA) reduce training time by 100x and Mixture of Memory Experts (MoME) reduces it even further

I appreciate Meta releasing the Llama's family of open models -- this course gives an example of the unique type of work that developers can do with such models.

Please sign up here: https://t.co/FITZFVlzNk

想系统性地提升大语言模型（LLM）应用的准确性和可靠性吗？快来参加我们的新短期课程「提高大语言模型（LLM）应用的准确性」吧！这门课程由 @LaminiAI 和 @Meta 联手打造，将由 Lamini 的首席执行官 @realSharonZhou 和 Meta 的合作工程高级总监 @asangani7 亲自授课。（声明：我是 Lamini 的投资者。）

优化大语言模型（LLM）应用的过程可能错综复杂。在本课程中，您将学到一套系统化的改进步骤，通过减少模型「幻觉」现象来提升其准确性：
- 创建评估数据集，用于衡量模型准确性
- 引入提示工程（Prompt Engineering）和自我反思（Self-Reflection）机制
- 微调您的模型，包括一项名为「记忆微调」的新方法，它能将事实有效地嵌入到大语言模型（LLM）中使用 Llama 3-8B 参数模型，您将：
- 构建一个带有自定义模式的文本到 SQL AI 智能体（AI Agent），并模拟其出现「幻觉」的场景
- 理解指令微调（即为预训练的大语言模型（LLM）提供指令使其遵循）与记忆微调之间的区别
- 了解性能高效微调（PEFT）技术，例如低秩适应（LoRA），如何将训练时间缩短 100 倍；以及记忆专家混合（MoME）如何在此基础上进一步加速训练我非常感谢 Meta 发布了 Llama 系列的开源模型 —— 本课程正是一个绝佳范例，展示了开发者们能如何利用这类模型开展独具创意的开发工作。

请点击此处报名：https://t.co/FITZFVlzNk

### 091

作者: @AndrewYNg
时间: 2024-08-15
链接: https://x.com/AndrewYNg/status/1824106080106123638
互动: Likes: 466; Retweets: 72; Replies: 49; Quotes: 12; Views: 72,121; Bookmarks: 97; isReply: 0

When entrepreneurs build a startup, it is often their speed and momentum that gives them a shot at competing with the tech behemoths. This is true of countries as well.

I was recently in Thailand, where I was delighted to see tremendous momentum building in AI (and sip the best Thai ice tea I’ve ever tasted). Even though Thailand is not as advanced in AI technology or applications as leading tech countries, the enthusiasm for building AI throughout government, corporations, and academia was thrilling. I came away heartened that AI’s benefits will be spread among many countries and convinced that one's level of AI development right now matters less than your momentum toward increasing it.

Seeing the momentum behind AI in Thailand — where the per capita GDP is around one fifth that of Japan, and one tenth that of the United States — left me feeling that any country, company, or person has a shot at doing meaningful work in the field. While advanced economies such as the U.S. and China are still in the lead, generative AI has made the playing field more level. Foundation models, especially those with open weights, are significantly lowering the barriers to building meaningful AI projects. In Thailand, a lot of people I met weren’t just talking about AI, they were rolling up their sleeves and building. That buys a nation a lot more momentum than just talk.

I met with Prime Minister Srettha Thavisin and his Ministers of Higher Education and Education (primary/secondary) along with many staffers. It was delightful to hear the PM speak of his enthusiasm for AI. The ministers discussed how to (i) provide AI training and (ii) use AI to improve education in a variety of subjects. Happily, the focus was on creating value while thinking through realistic risks like AI’s potential to proliferate misinformation, and not a single person asked me about whether AI will lead to human extinction!

I also met with many business leaders and enjoyed seeing a rapid pace of experimentation with AI. KBTG, an affiliate of the country’s leading digital bank KBank, is working on a financial chatbot advisor, AI-based identity verification for anti-fraud, AI for auto insurance, and a Thai-language financial large language model. These features are growing mobile banking and increasing financial access. Many business leaders in other sectors, too, have asked their teams to run experiments. There are many AI applications yet to be built in industrial sectors, tourism, trade, and more! (KBTG is an investor in AI Fund, which I lead.)

I often visit universities in both developed and developing economies, and I’ve been surprised to see that universities in developing economies sometimes adopt AI faster. At Chulalongkorn University (known as Chula), I met with the University President Bundhit Eua-arporn and Director of Chula AI Professor Proadpran Punyabukkana. Chula AI has rolled out campus-wide training in generative AI for faculty, staff, and students. In addition, it supports building AI applications such as AI screening for depression and gastrointestinal cancer. 

It takes years to build up advanced technology. But momentum matters, and there will be many rewards along the journey. There’s no time like the present to start building!

[Original text: https://t.co/xqFyYudIZ7 ]

创业者在创立新公司时，往往凭借速度和冲劲才能有机会与科技巨头一较高下。对于国家来说，这也是同样的道理。

我最近在泰国，很高兴看到当地在 AI 领域积聚着巨大的发展势头（当然，也品尝到了我喝过最棒的泰式冰茶）。尽管泰国在 AI 技术或应用方面可能不如一些领先的科技强国，但政府、企业和学术界对发展 AI 的热情令人振奋。我此行感到非常鼓舞，相信 AI 的益处将普惠全球诸多国家，并坚信一个国家当前 AI 的发展水平远不如其持续提升的势头重要。

目睹泰国在 AI 领域展现出的澎湃动力 —— 那里的人均 GDP 大约是日本的五分之一，美国的十分之一 —— 让我确信，任何国家、公司或个人都有机会在这个领域做出有意义的贡献。尽管美国和中国等发达经济体仍处于领先地位，但生成式 AI（generative AI）的出现已经让竞争环境变得更加公平。基础模型（Foundation models），特别是那些开放权重的模型，正显著降低构建有意义的 AI 项目的门槛。在泰国，我遇到的许多人不仅仅停留在口头讨论 AI，他们更是撸起袖子，付诸实践。这种行动力能为一个国家带来比空谈多得多的发展势头。

我会见了泰国总理 Srettha Thavisin 及其高等教育部长和基础教育部长，还有许多工作人员。很高兴听到总理表达他对 AI 的热情。部长们讨论了如何（1）提供 AI 培训，以及（2）利用 AI 改进各种学科的教育。令人欣慰的是，他们的关注点在于创造价值，同时审慎思考 AI 传播错误信息等现实风险，而且没有一个人问我 AI 是否会导致人类灭绝！

我还与许多商业领袖进行了交流，很高兴看到 AI 实验正在快速推进。KBTG，作为泰国领先数字银行 KBank 的附属公司，正在开发一款金融聊天机器人顾问、基于 AI 的反欺诈身份验证系统、应用于汽车保险的 AI 技术，以及一个泰语金融大语言模型（large language model）。这些创新正在推动移动银行的发展，并提高金融服务的可及性。其他行业的许多商业领袖也已要求他们的团队开展 AI 实验。在工业、旅游、贸易等领域，还有许多 AI 应用等待我们去开发！（KBTG 也是我所领导的 AI Fund 的投资者。)

我经常访问发达经济体和发展中经济体的大学，并惊讶地发现发展中经济体的大学有时在 AI 的采纳速度上更快。在朱拉隆功大学（Chulalongkorn University）(简称 Chula），我会见了校长 Bundhit Eua-arporn 和 Chula AI 主任 Professor Proadpran Punyabukkana。Chula AI 已面向全体教职员工和学生推出了校园范围的生成式 AI 培训。此外，它还支持构建 AI 应用，例如用于抑郁症和胃肠癌的 AI 筛查工具。

发展先进技术往往需要数年时间。但势头至关重要，而且在这一征程中会有丰厚的回报。时不我待，现在就是开始行动的最佳时机！

[原文链接：https://t.co/xqFyYudIZ7]

### 092

作者: @AndrewYNg
时间: 2024-08-19
链接: https://x.com/AndrewYNg/status/1825577904287395984
互动: Likes: 444; Retweets: 79; Replies: 19; Quotes: 8; Views: 116,780; Bookmarks: 36; isReply: 0

Thank you @RepZoeLofgren for speaking out against the anti-open source, anti-innovation bill SB-1047. 

She is the ranking member of the House Science, Space and Technology Committee. Her staff concludes: "the problematic core concerns remain: there is little evidentiary basis for the bill; the bill would negatively affect open-source development by applying liability to downstream use; it uses arbitrary thresholds not backed in science." [my boldface] 

Lets all keep fighting to protect open source AI.

https://t.co/ln7uOEzmgh

感谢 @RepZoeLofgren 公开反对阻碍开源和创新的 SB-1047 法案。

她是众议院科学、空间和技术委员会的首席成员。她的工作人员得出结论：「该法案的核心问题依然突出：其缺乏足够的证据支持；它将通过对下游使用施加责任来对开源开发产生负面影响；并且它设定了没有科学依据的任意门槛。」[我的粗体]

让我们所有人继续为保护开源 AI（open source AI）而努力。

https://t.co/ln7uOEzmgh

### 093

作者: @AndrewYNg
时间: 2024-08-21
链接: https://x.com/AndrewYNg/status/1826273022149587383
互动: Likes: 526; Retweets: 101; Replies: 26; Quotes: 7; Views: 53,542; Bookmarks: 232; isReply: 0

Build and customize complex AI applications with a flexible framework in this new short course, Building AI Applications with Haystack. Created in collaboration with @deepset_ai, and taught by @tuanacelik, who is the developer relations lead for Haystack at deepset.

Generative AI technology is changing rapidly and it can be challenging to integrate APIs from different LLMs, vector databases, and various tools such as web search. In this course, you will learn how to use the Haystack framework to make your development process more modular, allowing you to manage complexity and focus more on building your application.

In detail, you’ll:
- Build a RAG pipeline using Haystack’s main building blocks – components, pipelines, and document stores.
- Create custom components in your pipeline by building a Hacker News summarizer that extends your app’s ability to access APIs.
- Use conditional routing to create a branching pipeline with a fallback to web search mechanism when the LLM does not have the necessary context to respond to the user's query.
- Build a self-reflecting agent for named entity recognition that loops using an output validator custom component.
- Create a chat agent using OpenAI's function-calling capabilities which allow you to provide Haystack pipelines as tools to the LLM, enhancing that agent's capabilities.

By the end of this course, you will learn a high-level orchestration framework that can help make your applications flexible, extendible, and maintainable, even as the technology stack changes, new user needs arise, and you add new features to your application.

Please sign up here: https://t.co/wCvf549cM0

欢迎参加由 @deepset_ai 合作推出、deepset 公司 Haystack 开发者关系负责人 @tuanacelik 亲授的全新短期课程 ——「使用 Haystack 构建 AI 应用程序」。在本课程中，你将学习如何利用灵活的框架，构建并定制复杂的 AI 应用程序。

生成式 AI（Generative AI）技术日新月异，将不同的大语言模型（LLM）、向量数据库以及诸如网络搜索等各种工具的 API（应用程序编程接口）整合起来，可能颇具挑战。本课程将教你如何使用 Haystack 框架，让你的开发过程更具模块化，从而帮你管理复杂性，将更多精力放在应用程序的构建上。

具体来说，你将：
- 使用 Haystack 的核心构建模块 —— 组件、管道和文档存储 —— 构建一个 RAG（检索增强生成）管道。
- 构建一个 Hacker News 摘要器，以此创建管道中的自定义组件，扩展你的应用程序访问外部 API 的能力。
- 利用条件路由（conditional routing）创建一个分支管道，当大语言模型缺乏响应用户查询所需的上下文信息时，能自动回退（fallback）到网络搜索机制。
- 构建一个用于命名实体识别（named entity recognition）的自反思 AI 智能体（agent），它通过使用输出验证器自定义组件实现循环。
- 利用 OpenAI 的函数调用（function-calling）能力，创建一个聊天 AI 智能体，你可以将 Haystack 管道作为工具提供给大语言模型，从而提升该 AI 智能体的功能。

完成本课程后，你将掌握一个高级编排框架，它能帮助你的应用程序在技术栈不断变化、新的用户需求不断涌现以及你持续添加新功能的情况下，依然保持灵活、可扩展和易于维护。

请在此处注册：https://t.co/wCvf549cM0

### 094

作者: @AndrewYNg
时间: 2024-08-22
链接: https://x.com/AndrewYNg/status/1826635358848909737
互动: Likes: 320; Retweets: 63; Replies: 44; Quotes: 14; Views: 46,353; Bookmarks: 47; isReply: 0

I’m encouraged at the progress of the U.S. government at moving to stem harmful AI applications. Two examples are the new Federal Trade Commission (FTC) ban on fake product reviews and the DEFIANCE Act, which imposes punishments for creating and disseminating non-consensual deepfake porn. Both rules take a sensible approach to regulating AI insofar as they target harmful applications rather than general-purpose AI technology.

The best way to ensure AI safety is to regulate it at the application level rather than the technology level. This is important because the technology is general-purpose and its builders (such as a developer who releases an open-weights foundation model) cannot control how someone else might use it. If, however, someone applies AI in a nefarious way, we should stop that application.

Even before generative AI, fake reviews were a problem on many websites, and many tech companies dedicate considerable resources to combating them. A telltale sign of old-school fake reviews is the use of similar wording in different reviews. AI’s ability to automatically paraphrase or rewrite is making fake reviews harder to detect.

Importantly, the FTC is not going after the makers of foundation models for fake reviews. The provider of an open weights AI model, after all, can’t control what someone else uses it for. Even if one were to try to train a model to put up guardrails against writing reviews, I don’t know how it could distinguish between a real user of a product asking for help writing a legitimate review and a spammer who wanted a fake review. The FTC appropriately aims to ban the application of fake reviews along with other deceptive practices such as buying positive reviews.

The DEFIANCE Act, which passed unanimously in the Senate (and still requires passage in the House of Representatives before the President can sign it into law) imposes civil penalties for the creating and distributing non-consensual, deepfake porn. This disgusting application is harming many people including underage girls. While many image generation models do have guardrails against generating porn, these guardrails often can be circumvented via jailbreak prompts or fine-tuning (for models with open weights).

Again, DEFIANCE regulates an application, not the underlying technology. It aims to punish people who engage in the application of creating and distributing non-consensual intimate images, regardless of how they are generated — whether the perpetrator uses a diffusion model, a generative adversarial network, or Microsoft Paint to create an image pixel by pixel.

I hope DEFIANCE passes in the House and gets signed into law. Both rules guard against harmful AI applications without stifling AI technology itself (unlike California’s poorly designed SB-1047), and they offer a good model for how the U.S. and other nations can protect citizens against other potentially harmful applications.

[Original text (with links): https://t.co/AA2x2KxCqW ]

美国政府在遏制有害 AI 应用方面取得的进展让我备受鼓舞。有以下两个例子：联邦贸易委员会（FTC）新颁布的虚假产品评论禁令，以及 DEFIANCE 法案。后者旨在对创建和传播未经同意的深度伪造（deepfake）色情内容施加惩罚。这两项规定在 AI 监管上都采取了明智的策略，即它们主要针对有害的应用，而非笼统地限制通用人工智能（AI）技术本身。

确保 AI 安全的最佳途径是在应用层面而非技术层面进行监管。这一点至关重要，因为 AI 技术具有通用性，其开发者（例如发布开源权重基础模型（open-weights foundation model）的人）无法控制他人如何使用它。然而，如果有人以恶意方式应用 AI，我们理应阻止这种应用。

甚至在生成式 AI（Generative AI）出现之前，虚假评论在许多网站上就已是个老大难问题，许多科技公司投入了大量资源来打击它们。传统虚假评论的一个明显特征是不同评论中常使用相似的措辞。而 AI 自动改写或转述（paraphrase）的能力，使得虚假评论变得更难被检测。

值得注意的是，FTC 并没有因为虚假评论而追究基础模型开发者的责任。毕竟，一个开源权重 AI 模型的提供者无法控制其他人将它用于何种目的。即使有人尝试训练一个模型，旨在设置防护栏来阻止撰写虚假评论，我也不知道它该如何区分一个产品的真实用户寻求帮助撰写合法评论，和一个想要发布虚假评论的垃圾邮件发送者。因此，FTC 恰当地选择禁止虚假评论的应用，以及其他欺骗性行为，例如购买好评。

DEFIANCE 法案已在参议院获得一致通过（在总统签署成为法律前，仍需众议院通过），它对创建和分发未经同意的深度伪造色情内容施加民事处罚。这种令人发指的应用正在伤害许多人，包括未成年女孩。尽管许多图像生成模型确实设有防止生成色情内容的防护措施，但这些防护措施往往可以通过「越狱提示（jailbreak prompts）」或「微调（fine-tuning）」(对于开源权重模型而言）来规避。

再次强调，DEFIANCE 监管的是具体的应用，而不是底层的技术。它的目标是惩罚那些从事创建和分发未经同意的私密图像应用的人，无论这些图像是如何生成的 —— 无论是犯罪者使用了扩散模型（diffusion model）、生成对抗网络（generative adversarial network），还是仅仅用 Microsoft Paint 逐像素地绘制出来的。

我衷心希望 DEFIANCE 法案能在众议院通过并最终签署成为法律。这两项规定都在防范有害 AI 应用的同时，没有扼杀 AI 技术本身（这与加利福尼亚州设计欠佳的 SB-1047 法案形成鲜明对比），它们为美国及其他国家如何保护公民免受其他潜在有害应用提供了一个良好的范例。

[Original text（with links)：https://t.co/AA2x2KxCqW ]

### 095

作者: @AndrewYNg
时间: 2024-08-23
链接: https://x.com/AndrewYNg/status/1827047221013180611
互动: Likes: 311; Retweets: 26; Replies: 27; Quotes: 4; Views: 42,753; Bookmarks: 31; isReply: 0

I am thrilled to announce that Dan Maloney is becoming the Chief Executive Officer (CEO) of LandingAI, and I will step into the company’s Executive Chairman role, where I will continue to focus on Visual AI deep tech with our team, including agentic vision.

Since Dan joined two years ago as the company’s Chief Operating Officer (COO), his leadership across the company has been instrumental to LandingAI serving more customers and better than ever. Dan played an integral role in all of our key initiatives, including the launch of our self-service offering with LandingLens available for any vision application builder to use, establishing dozens of strategic and channel partnerships, increasing our focus on serving developers, and improving our operational excellence; even as we continue to innovate on Visual AI technology.

I look forward to continuing LandingAI’s journey with Dan, with our fantastic team, and with all our wonderful partners and users!

Text of full announcement below. https://t.co/At9k1JhvBV

我很高兴地宣布，Dan Maloney 将出任 LandingAI 的首席执行官（CEO），而我本人将转任公司的执行主席，继续与团队深耕视觉 AI（Visual AI）深度技术，特别是智能体视觉（agentic vision）领域。

自从 Dan 两年前加入公司担任首席运营官（COO）以来，他的卓越领导力对于 LandingAI 更好地服务更多客户起到了关键作用。Dan 在我们各项核心举措中都发挥了不可或缺的作用，其中包括：推出我们的自助服务产品 LandingLens，供任何视觉应用构建者使用；建立了数十个战略和渠道合作伙伴关系；增加了对服务开发者的关注；以及提升了我们的运营卓越性。所有这些都在我们持续创新视觉 AI 技术的同时稳步推进。

我期待着与 Dan、我们优秀的团队以及所有出色的合作伙伴和用户一起，继续 LandingAI 的发展旅程！

完整公告文本请见下方链接。https://t.co/At9k1JhvBV

### 096

作者: @AndrewYNg
时间: 2024-08-27
链接: https://x.com/AndrewYNg/status/1828504913158316075
互动: Likes: 346; Retweets: 65; Replies: 20; Quotes: 20; Views: 51,087; Bookmarks: 73; isReply: 0

I've been playing with @SambaNovaAI's API serving fast Llama 3.1 405B tokens. Really cool to see leading model running at speed. Congrats to Samba Nova for hitting a 114 tokens/sec speed record (and also thanks @KunleOlukotun for getting me an API key!) https://t.co/GuBfYsfizJ

我一直在试用 @SambaNovaAI 的 API，它能高速处理 Llama 3.1 405B 模型的 token。看到领先的大语言模型（Large Language Model）如此迅速地运行，真是令人印象深刻。祝贺 Samba Nova 达到了 114 token / 秒的速度记录（也要感谢 @KunleOlukotun 帮我申请到了 API 密钥！）https://t.co/GuBfYsfizJ

### 097

作者: @AndrewYNg
时间: 2024-08-27
链接: https://x.com/AndrewYNg/status/1828552114123288835
互动: Likes: 405; Retweets: 44; Replies: 26; Quotes: 5; Views: 64,941; Bookmarks: 36; isReply: 0

Really fun hackathon, and it was great to see 30 creative Agentic AI projects, all built in a day. Well done to all the hackathon participants, and thank you @HenryYin_ , @AlexReibman and @agihouse_org for having me! 
·

·这是一场非常有趣的黑客马拉松，很高兴看到 30 个富有创意的 Agentic AI（Agentic AI）项目，所有项目都在一天之内就构建完成了。向所有黑客马拉松的参与者表示祝贺，并感谢 @HenryYin_ 、 @AlexReibman 和 @agihouse_org 邀请我参加！

### 098

作者: @AndrewYNg
时间: 2024-08-28
链接: https://x.com/AndrewYNg/status/1828844538712224137
互动: Likes: 838; Retweets: 158; Replies: 36; Quotes: 7; Views: 73,454; Bookmarks: 450; isReply: 0

Explore state-of-the-art multimodal prompting in our new short course Large Multimodal Model Prompting with Gemini, taught by Erwin Huizenga in collaboration with @googlecloud.

One interesting insight from this course: with multimodal models, prompt structure matters significantly. Placing text inputs, such as a patient's medical history, before image inputs, like an X-ray, can enhance the model's ability to contextualize and interpret visual data effectively. In other contexts, such as image captioning, you may get better results by putting the image first. Multimodal models behave differently than text-only LLMs, and effective prompting for models varies depending on the model you’re using. In this course you’ll learn how to effectively prompt Gemini models.

Gemini's multimodal capabilities also enable new approaches in AI application development, for example:
- The Gemini library handles various video formats (MP4, MOV, MPEG), streamlining applications using these formats.
- Large context window (up to 1 million tokens) enables processing of extensive content, like analyzing multiple 50-minute videos simultaneously. 
- Function calling feature integrates real-time data (e.g., current exchange rates) into model responses.

The course demonstrates building multimodal applications with real-world examples including document analyzers that reason across text and graphs simultaneously, video content extractors that find and timestamp specific information from multiple hours of footage, and automated expense report systems processing receipt images while cross-referencing company policies.

Sign up here: https://t.co/4yI4DXcFpK

与 Erwin Huizenga 和 @googlecloud 合作，我们推出了一门新短期课程《Gemini 大型多模态模型提示》，带您深入了解目前最先进的多模态提示（multimodal prompting）技术。

本课程分享了一个有趣的观点：对于多模态模型（multimodal models）而言，提示（prompt）的结构至关重要。例如，将文本输入（如患者病史）放在图像输入（如 X 射线）之前，可以显著增强模型有效结合上下文理解和解释视觉数据的能力。而在其他应用场景，比如图像字幕生成中，您可能会发现先放置图像能获得更好的效果。多模态模型的行为与纯文本大语言模型（LLM）有所不同，因此针对不同模型的有效提示策略也会因模型而异。在本课程中，您将学习如何有效地向 Gemini 模型发出提示。

Gemini 的多模态能力也为 AI 应用程序开发开启了新思路，例如：
- Gemini 库能够处理多种视频格式（MP4、MOV、MPEG），从而简化了使用这些格式的应用程序开发。
- 巨大的上下文窗口（高达 100 万 token）让处理海量内容成为可能，比如同时分析多段 50 分钟的视频。
- 函数调用（Function calling）功能可以将实时数据（例如当前汇率）整合到模型响应中。

本课程通过真实世界案例演示了如何构建多模态应用程序，包括能同时分析理解文本和图表的文档分析器、能从数小时视频片段中查找并标记特定信息的视频内容提取器，以及在处理收据图像时能对照公司政策进行核查的自动化费用报告系统。

点击此处注册：https://t.co/4yI4DXcFpK

### 099

作者: @AndrewYNg
时间: 2024-08-29
链接: https://x.com/AndrewYNg/status/1829190549842321758
互动: Likes: 3,583; Retweets: 627; Replies: 114; Quotes: 114; Views: 740,702; Bookmarks: 2,048; isReply: 0

After a recent price reduction by OpenAI, GPT-4o tokens now cost $4 per million tokens (using a blended rate that assumes 80% input and 20% output tokens). GPT-4 cost $36 per million tokens at its initial release in March 2023. This price reduction over 17 months corresponds to about a 79% drop in price per year. (4/36 = (1 - p)^{17/12}) 

As you can see, token prices are falling rapidly! One force that’s driving prices down is the release of open weights models such as Llama 3.1. If API providers, including startups Anyscale, Fireworks, Together AI, and some large cloud companies, do not have to worry about recouping the cost of developing a model, they can compete directly on price and a few other factors such as speed. 

Further, hardware innovations by companies such as Groq (a leading player in fast token generation), Samba Nova (which serves Llama 3.1 405B tokens at an impressive 114 tokens per second), and wafer-scale computation startup Cerebras (which just announced a new offering this week), as well as the semiconductor giants NVIDIA, AMD, Intel, and Qualcomm, will drive further price cuts. 

When building applications, I find it useful to design to where the technology is going rather than only where it has been. Based on the technology roadmaps of multiple software and hardware companies — which include improved semiconductors, smaller models, and algorithmic innovation in inference architectures — I’m confident that token prices will continue to fall rapidly.

This means that even if you build an agentic workload that isn’t entirely economical, falling token prices might make it economical at some point. As I wrote previously, being able to process many tokens is particularly important for agentic workloads, which must call a model many times before generating a result. Further, even agentic workloads are already quite affordable for many applications. Let's say you build an application to assist a human worker, and it uses 100 tokens per second continuously: At $4/million tokens, you'd be spending only $1.44/hour – which is significantly lower than the minimum wage in the U.S. and many other countries.

So how can AI companies prepare?
- First, I continue to hear from teams that are surprised to find out how cheap LLM usage is when they actually work through cost calculations. For many applications, it isn’t worth too much effort to optimize the cost. So first and foremost, I advise teams to focus on building a useful application rather than on optimizing LLM costs.
- Second, even if an application is marginally too expensive to run today, it may be worth deploying in anticipation of lower prices.
- Finally, as new models get released, it might be worthwhile to periodically examine an application to decide whether to switch to a new model either from the same provider (such as switching from GPT-4 to the latest GPT-4o-2024-08-06) or a different provider, to take advantage of falling prices and/or increased capabilities.

Because multiple providers now host Llama 3.1 and other open-weight models, if you use one of these models, it might be possible to switch between providers without too much testing (though implementation details — specifically quantization, does mean that different offerings of the model do differ in performance). When switching between models, unfortunately, a major barrier is still the difficulty of implementing evals, so carrying out regression testing to make sure your application will still perform after you swap in a new model can be challenging. However, as the science of carrying out evals improves, I’m optimistic that this will become easier.

[Original text (with links): https://t.co/txk7q32EXn ]

在 OpenAI 最近降价后，GPT-4o 的 token（Token）成本现已降至每百万 token 4 美元（此混合费率假设 80% 为输入 token，20% 为输出 token）。而 GPT-4 在 2023 年 3 月首次发布时，每百万 token 的成本高达 36 美元。这意味着在短短 17 个月内，token 价格下降了约 79%，相当于每年约 79% 的价格跌幅。(4/36 =（1 - p)^{17/12})

正如你所见，token 价格正在迅速下滑！推动价格下跌的一个重要力量是 Llama 3.1 等开放权重模型的发布。如果 Anyscale、Fireworks、Together AI 等初创公司以及一些大型云公司等 API 提供商无需担忧收回模型开发成本，他们就能直接在价格、速度等因素上展开竞争。

此外，Groq（在快速 token 生成方面处于领先地位）、Samba Nova（能以每秒 114 token 的惊人速度提供 Llama 3.1 405B token）和晶圆级计算初创公司 Cerebras（本周刚宣布了新产品）等公司的硬件创新，以及 NVIDIA、AMD、Intel 和 Qualcomm 等半导体巨头的发展，都将进一步推动价格下调。

在开发应用程序时，我发现根据技术未来发展方向进行设计，而非仅仅局限于现有技术，会更具价值。基于多家软件和硬件公司的技术路线图 —— 其中包括改进的半导体、更精简的模型和推理架构中的算法创新 —— 我坚信 token 价格将继续快速下跌。

这意味着，即使你构建的代理式工作负载（agentic workload）目前经济效益不佳，不断下降的 token 价格也可能使其在未来某个时间点变得划算。正如我之前所写，对于代理式工作负载而言，能够处理大量 token 尤其重要，因为它们在生成最终结果之前需要多次调用模型。而且，即便代理式工作负载，对于许多应用来说也已经相当经济实惠。假设你开发了一个应用程序来辅助人类工作者，它每秒持续使用 100 token：按照每百万 token 4 美元计算，你每小时的开销仅为 1.44 美元 —— 这远低于美国及许多其他国家的最低工资水平。

那么，AI 公司该如何应对呢？
- 首先，我不断听到有团队在实际进行成本估算时，惊讶地发现大语言模型（LLM）的使用成本竟然如此之低。对于许多应用来说，投入过多精力去优化成本并不十分值得。因此，我首要建议团队应专注于构建有用的应用程序，而非过度关注优化大语言模型（LLM）的成本。
- 其次，即使某个应用程序今天运行成本略高，但考虑到未来价格会更低，它可能也值得提前部署。
- 最后，随着新模型的不断发布，定期检查应用程序以决定是否切换到新模型可能很有价值，无论是来自同一提供商（例如从 GPT-4 切换到最新的 GPT-4o-2024-08-06），还是不同提供商，以便充分利用不断下降的价格和 / 或增强的功能。

由于现在有多个提供商托管 Llama 3.1 和其他开放权重模型，如果你使用其中一个模型，可能无需进行太多测试即可在不同提供商之间切换（不过，实现细节，尤其是量化（quantization）技术，确实会导致同一模型的不同产品在性能上有所差异）。然而，在模型之间切换时，一个主要障碍仍然是实施评估（evals）的难度。因此，进行回归测试以确保你的应用程序在更换新模型后仍能正常运行，可能具有挑战性。不过，随着评估（evals）科学方法的不断改进，我乐观地认为这将会变得更容易。

[原文（带链接)：https://t.co/txk7q32EXn ]

### 100

作者: @AndrewYNg
时间: 2024-08-29
链接: https://x.com/AndrewYNg/status/1829218674806583779
互动: Likes: 940; Retweets: 195; Replies: 80; Quotes: 38; Views: 237,806; Bookmarks: 99; isReply: 0

There’s still time to stop California’s SB 1047 from becoming law. For @TIME, I wrote about why this bill would hinder developers and actually make AI less safe. We should be regulating harmful applications of AI, not  general-purpose AI models. https://t.co/dco1e65u9H

阻止加州 SB 1047 法案成为法律，我们还有时间。我为 @TIME 撰文，阐述了为何这项法案会阻碍开发者，并实际上让人工智能（AI）变得更不安全。我们应该监管 AI 的有害应用，而不是针对通用型 AI 模型进行规范。https://t.co/d01e65u9H

### 101

作者: @AndrewYNg
时间: 2024-09-04
链接: https://x.com/AndrewYNg/status/1831346457854771255
互动: Likes: 3,784; Retweets: 766; Replies: 86; Quotes: 47; Views: 420,025; Bookmarks: 4,529; isReply: 0

We just released the final two courses of AI Python for Beginners! The complete set of four courses is now available and remains free for a limited time.

They teach how to write code (a) Using AI-assistance, which is where the field is going, and (b) to take advantage of generative AI, which allows you to quickly do valuable things with code.

If you're considering learning to code, AI has made this a great time to jump in. Or if you know someone who is considering learning, please recommend these courses! 

https://t.co/lTupltSZkT

我们刚刚发布了为初学者设计的 AI Python 系列课程的最后两门！现在，全套四门课程都已上线，并且在有限时间内依然免费开放。

这些课程将教你如何编写代码，具体包括两方面：一是借助 AI 辅助来编写代码，这正是当前编程领域的发展趋势；二是利用生成式 AI（Generative AI）的能力，让你能快速用代码实现各种有价值的应用。

如果你正考虑学习编程，AI 的发展让现在成为一个绝佳的入门时机。如果你身边有朋友想学编程，也请务必向他们推荐这些课程！

https://t.co/lTupltSZkT

### 102

作者: @AndrewYNg
时间: 2024-09-05
链接: https://x.com/AndrewYNg/status/1831715072248545741
互动: Likes: 1,282; Retweets: 148; Replies: 57; Quotes: 30; Views: 137,016; Bookmarks: 155; isReply: 0

Recently I visited South Korea, where I spoke at length about AI with President Yoon Suk Yeol. Based on what I saw there in government, business, and academia, the nation is well positioned to become a strong AI hub. When he asked me if I would advise South Korea as a member of the Global AI Strategy Steering Group of the country’s National AI Committee, I agreed on the spot. I was delighted to learn this week that Yann LeCun has also joined. I’ve been consistently impressed by the thoughtful approach the Korean government has taken toward AI, with an emphasis on investment and innovation and a realistic understanding of risks without being distracted by science-fiction scenarios of harm.

I’ve advised many countries to build AI for the sectors where they’re strong. For example, I wrote previously that by investing in sectors like tourism and certain industrial areas, Thailand can do projects more efficiently than I can in Silicon Valley. South Korea’s tech ecosystem gives it a foundation to move fast even across numerous sectors. This emphasizes the long-term value for countries to become good at tech, because tech is now pervasive and affects all industries.

Korea has a very strong local software ecosystem. For example, the dominant search engine is not Google or Bing, but Naver (a Korean company). The dominant messaging system is not WhatsApp or WeChat, but KakaoTalk. With local tech giants Naver and Kakao offering email, mobile payment, cloud computing, ride sharing, and other services, the country has many sophisticated tech businesses. Additionally, SK hynix and Samsung are advanced semiconductor manufacturers. It also has a thriving entrepreneurship ecosystem, including Upstage, a language modeling startup, which taught a course with us on “Pretraining LLMs.” Finally, the Korean institutions Seoul National University, which I visited last year, and KAIST have global reputations.

Korea has a highly educated population, highly skilled software engineers, and a thriving set of software products. This gives it a fantastic foundation to embrace the next generation of AI. After meeting with businesses in retail, construction, insurance, cosmetics, telecoms, and other industries, I was delighted by the wide variety of opportunities many companies are pursuing across different industry sectors.

Lastly, Korea is known globally for its K-pop. Meeting Bang Si-Hyuk, the chairman of HYBE, which manages the superstar singing group BTS, and learning how the company operates was a real treat! 

That’s why I’ve traveled to South Korea four times since last year. My venture studio AI Fund, which collaborates with many Korean companies, has benefited tremendously from the advice of many South Koreans, including Taizo Son, Changmook Kang, Hyungjun Kim, Sung Kim, JP Lee, Ian Park, and Alice Oh. I look forward to doing more in, and with, South Korea!

[Original text (with links): https://t.co/mVSVBCI49q ]

最近我访问了韩国，与尹锡悦总统深入探讨了 AI（人工智能）。根据我在那里看到的政府、商业和学术界的表现，韩国完全有能力成为一个强大的 AI 中心。当他邀请我加入该国国家 AI 委员会全球 AI 战略指导小组，为韩国提供建议时，我当场就欣然同意了。令我高兴的是，本周得知 Yann LeCun 也加入了这个小组。韩国政府在 AI 方面深思熟虑的做法一直令我印象深刻，他们不仅注重投资和创新，同时对风险有着务实的理解，避免被科幻小说式的危害情景所干扰。

我曾建议许多国家，应在其擅长的领域发展 AI。例如，我之前就提到过，通过投资旅游业和特定工业领域等，泰国可以比我在硅谷更高效地开展项目。韩国的科技生态系统为其提供了快速发展的基础，即便是在众多领域也能迅速推进。这凸显了各国发展科技实力的长期价值，因为科技如今已无处不在，并影响着所有行业。

韩国拥有非常强大的本土软件生态系统。例如，这里的主流搜索引擎不是 Google 或 Bing，而是 Naver（一家韩国公司）。主流即时通讯系统也不是 WhatsApp 或 WeChat，而是 KakaoTalk。Naver 和 Kakao 等本土科技巨头提供电子邮件、移动支付、云计算、共享出行等多种服务，使得韩国涌现出众多先进的科技企业。此外，SK hynix 和 Samsung 都是顶尖的半导体制造商。韩国还有一个充满活力的创业生态系统，其中包括语言模型初创公司 Upstage，该公司曾与我们合作开设「预训练大语言模型（Pretraining LLMs）」课程。最后，我去年访问过的韩国学府首尔国立大学和 KAIST 都享有国际盛誉。

韩国拥有受过高等教育的人口、高技能的软件工程师，以及一系列蓬勃发展的软件产品。这为他们拥抱下一代 AI 奠定了坚实的基础。在与零售、建筑、保险、化妆品、电信等多个行业的企业会面后，我很高兴看到许多公司在不同行业领域积极探索着广泛的机遇。

最后，韩国以其 K-pop（韩国流行音乐）享誉全球。能有机会见到管理超级歌唱组合 BTS（防弹少年团）的 HYBE 董事长 Bang Si-Hyuk，并了解这家公司的运作方式，真是一次难忘的经历！

这就是我自去年以来四次前往韩国的原因。我的风险投资工作室 AI Fund，与许多韩国公司都有合作，并从 Taizo Son、Changmook Kang、Hyungjun Kim、Sung Kim、JP Lee、Ian Park 和 Alice Oh 等多位韩国友人那里受益匪浅。我期待着在韩国以及与韩国开展更多合作！

[原文（含链接）：https://t.co/mVSVBCI49q ]

### 103

作者: @AndrewYNg
时间: 2024-09-12
链接: https://x.com/AndrewYNg/status/1834268475243856342
互动: Likes: 1,190; Retweets: 198; Replies: 33; Quotes: 12; Views: 106,733; Bookmarks: 683; isReply: 0

New short course Multimodal RAG: Chat with Videos, developed with @intel and taught by @vasudev_lal!

In this course, you’ll work with LLaVA (Large Language and Vision Assistant), a Large Vision Language Model (LVLM) that can process both images and text. For example, given an image of a person doing a handstand on a skateboard at the beach, LLaVA doesn't just caption the scene, it’s able to predict possible outcomes, like the person losing balance or falling off. By understanding not just what's in a video frame, but what might happen next, your application can provide more insightful answers to questions about video.

You'll build a full multimodal RAG pipeline that can chat about video content:
- Use the BridgeTower model to create joint text-image embeddings in a 512-dimensional multimodal semantic space.
- Learn video processing techniques to extract keyframes, generate transcripts using Whisper, and create captions.
- Use the LanceDB vector database to store and retrieve high-dimensional multimodal embeddings.
- Integrate the LLaVA model, combining CLIP's (Contrastive Language Image Pretraining) vision transformer with Llama, for advanced visual-textual reasoning.

Your final system will ingest video data, generate embeddings for frames and text, perform similarity searches for relevant content, and use the retrieved multimodal context to inform LVLM-based response generation. The result is a system capable of answering nuanced questions about video content, effectively chatting about the video it has processed.

Please sign up here! https://t.co/cjUHPK3rK2

全新短课程「多模态 RAG：与视频聊天」发布啦！本课程由 Intel 携手 @vasudev_lal 共同开发与讲授。

在本课程中，你将有机会接触 LLaVA（Large Language and Vision Assistant）模型。LLaVA 是一种大视觉语言模型（LVLM），它能够同时处理图像和文本信息。举个例子，假设你给 LLaVA 一张一个人在海边滑板上倒立的图片，它不仅能生成对场景的描述，还能预测可能发生的结果，比如这个人可能会失去平衡或摔倒。通过这种方式，你的应用程序将不仅理解视频帧中的内容，还能预判接下来可能发生什么，从而为关于视频的问题提供更具洞察力的答案。

你将亲手搭建一个完整的多模态 RAG（Retrieval Augmented Generation）管道，实现与视频内容的对话：
- 利用 BridgeTower 模型创建联合文本 - 图像嵌入（embeddings），并将它们置于 512 维的多模态语义空间中。
- 学习视频处理技术，包括提取关键帧、使用 Whisper 生成语音转文本（即文字稿），以及创建字幕。
- 采用 LanceDB 向量数据库，用于存储和检索这些高维多模态嵌入。
- 整合 LLaVA 模型，它巧妙地将 CLIP（Contrastive Language Image Pretraining）的视觉 Transformer 与 Llama 模型结合，以实现更高级的视觉 - 文本推理能力。

最终，你构建的系统将能够接收视频数据，为视频帧和文本生成嵌入，进行相关内容的相似性搜索，并利用检索到的多模态上下文来生成基于 LVLM 的响应。通过这个系统，你将能够回答关于视频内容的细致复杂的问题，有效与它所处理的视频进行互动。

请在此处注册！https://t.co/cjUHPK3rK2

### 104

作者: @AndrewYNg
时间: 2024-09-14
链接: https://x.com/AndrewYNg/status/1835028475436257705
互动: Likes: 385; Retweets: 46; Replies: 53; Quotes: 9; Views: 86,029; Bookmarks: 68; isReply: 0

Last weekend, my two kids colluded in a hilariously bad attempt to mislead me to look in the wrong place during a game of hide-and-seek. I was reminded that most capabilities — in humans or in AI — develop slowly.

Some people fear that AI someday will learn to deceive humans deliberately. If that ever happens, I’m sure we will see it coming from far away and have plenty of time to stop it.

While I was counting to 10 with my eyes closed, my daughter (age 5) recruited my son (age 3) to tell me she was hiding in the bathroom while she actually hid in the closet. But her stage whisper, interspersed with giggling, was so loud I heard her instructions clearly. And my son’s performance when he pointed to the bathroom was so hilariously overdramatic, I had to stifle a smile.

Perhaps they will learn to trick me someday, but not yet! (In his awful performance, I think my son takes after me. To this day, I have a terrible poker face — which is matched by my perfect lifetime record of losing every poker game I have ever played!)

Last year, the paper “Are Emergent Abilities of Large Language Models a Mirage?” by Rylan Schaeffer, Brando Miranda, and Sanmi Koyejo, which won a NeurIPS outstanding paper award, considered “emergent” properties of LLMs, which refers to capabilities that seem to appear suddenly as model sizes increase. The authors point out that scaling laws imply that the per-token error rate decreases (improves) slowly with scale, and emergent properties might be an artifact of researchers studying nonlinear or discontinuous metrics that transform a gradually decreasing per-token error rate into something that looks more like a step function.

Consider a “combination lock” metric that requires getting many items right. Say we’re measuring the likelihood that an LLM will get 10 independent digits of an answer right. If the odds of it getting each digit right improve gradually from 0 to 1, then the odds of it getting all 10 digits right will appear to jump suddenly. But if we look at continuous metrics, such as the total number of correct digits, we will see that the underlying performance actually improves gradually. (Public perception of a technology can also shift in a discontinuous way because of social dynamics.)

This is why many of us saw GPT-3 as a promising step in transforming text processing long before ChatGPT appeared: BERT, GPT, GPT-2, and GPT-3 represented points on a continuous spectrum of progress. Or, looking back further in AI history, even though AlphaGo’s victory over Lee Sedol in the game of Go took the public by surprise, it actually represented many years of gradual improvements in AI’s ability to play Go.

While analogies between human and machine learning can be misleading, I think that just as a person’s ability to do math, to reason — or to deceive — grows gradually, so will AI’s. This means the capabilities of AI technology will grow gradually (I wish we could achieve AGI overnight!), and the ability of AI to be used in harmful applications, too, will grow gradually. As long as we keep performing red-teaming exercises and monitoring our systems’ capabilities as they evolve, I’m confident that we will have plenty of time to spot issues in advance, and the science-fiction fears of AI-initiated doomsday will remain science fiction.

[Original text (with links): https://t.co/HTnKpqqse5 ]

上周末，我的两个孩子在玩捉迷藏时，想出了一个拙劣到可笑的计谋，试图把我引到错误的地方。这让我想到，无论是人类还是 AI，大多数能力的成长都是一个缓慢的过程。

有些人担心，AI（人工智能）有朝一日会学会蓄意欺骗人类。如果真有那么一天，我确信我们会提前很长时间察觉到，并有充足的时间来阻止它。

当我闭着眼睛数到 10 时，我 5 岁的女儿让 3 岁的儿子告诉我她藏在浴室里，而她自己却躲进了衣橱。但她假装悄悄话的声音（其实很大声），夹杂着咯咯的笑声，让我把她的指示听得一清二楚。我儿子指着浴室时，那表演夸张得简直滑稽，我不得不强忍着笑意。

也许他们有一天会学会骗我，但现在还不行！（我想我儿子拙劣的表演像极了我。直到今天，我的扑克脸都差得要命 —— 这和我打过的每一场扑克都输掉的「完美」记录真是绝配！）

去年，Rylan Schaeffer、Brando Miranda 和 Sanmi Koyejo 撰写的论文《大语言模型（LLM）的涌现能力是海市蜃楼吗？》获得了 NeurIPS 杰出论文奖。这篇论文探讨了 LLM 的「涌现」属性，也就是那些随着模型规模增大而看似突然出现的能力。作者指出，缩放定律表明，每 Token（Token）的错误率是随着模型规模缓慢下降（即性能逐渐提升）的，而所谓的「涌现」属性，可能只是研究人员采用了非线性或不连续的评估指标所导致的一种假象，这些指标将原本缓慢下降的每 Token 错误率，转化成了类似阶跃函数一样的突然跃升。

打个比方，假设有一个「组合锁」指标，要求模型必须答对很多项才能算成功。比如说，我们测量一个大语言模型正确答出某个答案的 10 个独立数字的概率。如果它答对每个数字的概率从 0 逐渐提高到 1，那么它答对所有 10 个数字的概率就会看起来是突然跳跃的。但如果我们观察连续的指标，比如答对数字的总数，我们就会发现，底层的性能其实是一点点逐渐改善的。（公众对某项技术的认知也可能因为社会动态而出现不连续的转变。）

这就是为什么我们很多人在 ChatGPT 出现很久之前，就将 GPT-3 视为文本处理领域迈出有前景的一步：BERT、GPT、GPT-2 和 GPT-3 代表了持续进步的连续谱系上的一个个节点。或者，回顾更早的 AI 历史，尽管 AlphaGo 在围棋比赛中战胜 Lee Sedol 让公众大吃一惊，但这背后实际上是 AI 在围棋能力上多年来逐步改进的成果。

尽管人类学习和机器学习之间的类比有时会产生误导，但我认为，就像一个人学习数学、进行推理 —— 或是欺骗 —— 的能力是逐渐增长的一样，AI 的能力也会如此。这意味着 AI 技术的各种能力将会逐渐增强（我多么希望我们能一夜之间实现通用人工智能（AGI)！），AI 被用于有害应用的能力也会逐渐发展。只要我们持续进行红队演练（red-teaming exercises）并监测我们系统不断演进的能力，我确信我们会有充足的时间提前发现问题，而那些关于 AI 引发末日的科幻恐惧，就只会停留在科幻层面。

[原文（带链接)：https://t.co/HTnKpqqse5 ]

### 105

作者: @AndrewYNg
时间: 2024-09-18
链接: https://x.com/AndrewYNg/status/1836433152803488119
互动: Likes: 1,352; Retweets: 221; Replies: 39; Quotes: 12; Views: 119,315; Bookmarks: 1,030; isReply: 0

We just launched a major new Data Engineering Professional Certificate on Coursera! Data underlies all modern AI systems, and engineers who know how to build systems to store and serve it are in high demand. If you're interested in learning this skill, please check out this 4-course sequence, which is designed to make you job-ready to be a Data Engineer. 

This is a new specialization taught by Joe Reis, the co-author of the best-selling book “Fundamentals of Data Engineering," in collaboration with AWS. (Disclosure, I serve on Amazon's board.) For many AI systems, data engineering is 80% of the work, and modeling is 20%. But people’s attention on these two topics is often flipped. This makes the job of the data engineer particularly important.

In this professional certificate, you'll learn foundational data engineering skills while implementing modern data architectures using open-source tools:
- Learn the key steps of the data lifecycle, to generate, ingest, store, transform, and serve data.
- Learn to align with organizational goals to design the data pipeline right for your business' needs.
- Understand how to make necessary trade-offs between speed, scalability, security, and cost.

Joe has distilled into this specialization decades of experience helping startups and large companies with data infrastructure. He is also joined by 17 other industry leaders in the data field, who will help you learn in-demand skills for the growing field of data engineering.

Please sign up here: https://t.co/2kTGSXrSHP

我们刚刚在 Coursera 上推出了一个重磅级的数据工程专业证书（Data Engineering Professional Certificate)！数据是所有现代 AI 系统的基石，因此，懂得如何构建系统来存储和 ** 服务数据 ** 的工程师正受到市场的热烈追捧。如果你有兴趣学习这项关键技能，请务必了解这个包含四门课程的系列，它旨在让你做好成为一名 ** 数据工程师（Data Engineer)** 的就业准备。

这是一个由畅销书《数据工程基础》的合著者 Joe Reis 与 AWS 合作教授的全新 ** 专项课程 **。（声明：我本人是 Amazon 董事会成员。）对于许多 AI 系统来说，数据工程（Data Engineering）占据了 80% 的工作量，而模型构建仅占 20%。然而，人们对这两个主题的关注度却常常 ** 本末倒置 **。这恰恰凸显了 ** 数据工程师 ** 工作的特殊重要性。

通过这份专业证书，你将学习 ** 数据工程 ** 的基础技能，同时运用开源工具来 ** 构建现代数据架构 **：
- 学习 ** 数据生命周期 ** 的关键环节，包括数据的生成、** 摄取 **、存储、转换和 ** 服务 **。
- 掌握如何根据组织目标，设计出最符合你业务需求的数据 ** 管道（data pipeline)**。
- 理解如何在速度、可扩展性、安全性与成本之间做出必要的权衡取舍。

Joe 在这门 ** 专项课程 ** 中凝结了他数十年的宝贵经验，这些经验曾帮助无数初创公司和大型企业搭建数据基础设施。此外，还有 17 位 ** 数据领域 ** 的行业领袖 ** 倾力加盟 **，他们将共同帮助你学习 ** 日益壮大 ** 的 ** 数据工程 ** 领域中那些 ** 紧缺的实用技能 **。

请点击此处报名：https://t.co/2kTGSXrSHP

### 106

作者: @AndrewYNg
时间: 2024-09-25
链接: https://x.com/AndrewYNg/status/1839016467767111829
互动: Likes: 1,559; Retweets: 292; Replies: 38; Quotes: 17; Views: 111,444; Bookmarks: 576; isReply: 0

The Llama 3.2 open multimodal model just dropped! https://t.co/R0m408f8CA has been working with Meta on a short course on how to use it. Please sign up for "Introducing Llama 3.2", taught by Meta's @asangani7, which will launch Oct 9!
https://t.co/CC2uLNQ20W

Llama 3.2 开放多模态模型（open multimodal model）重磅发布！https://t.co/R0m408f8CA 正在与 Meta 合作，共同推出一门关于如何使用 Llama 3.2 的短期课程。请大家踊跃报名参加由 Meta 的 @asangani7 讲授的「Llama 3.2 介绍」课程，该课程将于 10 月 9 日上线！
https://t.co/CC2uLNQ20W

### 107

作者: @AndrewYNg
时间: 2024-09-26
链接: https://x.com/AndrewYNg/status/1839338535519932886
互动: Likes: 799; Retweets: 161; Replies: 24; Quotes: 3; Views: 68,926; Bookmarks: 522; isReply: 0

Announcing Generative AI for Software Development, a new specialization on Coursera! Taught by my friend and longtime https://t.co/zpIxRSuky4 instructor @lmoroney. 

Using GenAI for software development goes well beyond using chatbots for code generation. This 3-course series shares current best practices for AI use through the entire software development lifecycle: From design and architecture to coding, testing, deployment, and maintenance.

You'll learn to use LLMs as your thought partner, pair programmer, documentation specialist, security analyst, and performance optimization expert. There's a lot that anyone that writes software can gain from using GenAI, and this will show you how!

Please sign up here to get started! https://t.co/8nKgy32vIc

宣布在 Coursera 上推出一门新专项课程：软件开发中的生成式 AI（Generative AI)！该课程由我的朋友、同时也是 https://t.co/zpIxRSuky4 的资深讲师 @lmoroney 教授。

将生成式 AI（GenAI）应用于软件开发，远不止用聊天机器人来生成代码。这三门系列课程将分享在整个软件开发生命周期中应用 AI 的最新最佳实践：涵盖从设计与架构，到编码、测试、部署和维护的各个环节。

你将学会如何将大语言模型（LLM）视为你的思考伙伴、结对程序员、文档专家、安全分析师以及性能优化专家。任何从事软件开发的人，都能从使用生成式 AI 中获益良多，而这门课程将向你展示具体的方法！

请在此处注册，立即开始学习！https://t.co/8nKgy32vIc

### 108

作者: @AndrewYNg
时间: 2024-09-26
链接: https://x.com/AndrewYNg/status/1839392271386730591
互动: Likes: 1,762; Retweets: 480; Replies: 72; Quotes: 55; Views: 629,075; Bookmarks: 80; isReply: 0

A decision on SB-1047 is due soon. Governor @GavinNewsom has said he's concerned about its "chilling effect, particularly in the open source community". He's right, and I hope he will veto this. 

If you agree, please like/retweet this to show your support for VETOing SB-1047!

关于 SB-1047 的决定即将公布。州长 @GavinNewsom 曾表示他担心该法案会产生「寒蝉效应（chilling effect）」，尤其是在开源社区。他的看法是正确的，我希望他能否决这项提案。

如果您同意，请点赞 / 转发此推文，以表示您支持否决 SB-1047！

### 109

作者: @AndrewYNg
时间: 2024-09-27
链接: https://x.com/AndrewYNg/status/1839744822737002662
互动: Likes: 3; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,048; Bookmarks: 0; isReply: 1

@asangani7 Thank you for having me at Meta Connect @asangani7! I love what you and the @AIatMeta team are doing and am very grateful for all the open models y'all are  releasing. What a wonderful gift to the world!

@asangani7 谢谢你邀请我参加 Meta Connect！我非常喜欢你和 @AIatMeta 团队所做的一切，也无比感激你们发布的所有开放模型。这真是送给世界的一份美好礼物！

### 110

作者: @AndrewYNg
时间: 2024-09-29
链接: https://x.com/AndrewYNg/status/1840439968407363942
互动: Likes: 206; Retweets: 36; Replies: 10; Quotes: 2; Views: 95,813; Bookmarks: 23; isReply: 0

Good summary of the case for vetoing SB-1047 by @psychosort

@psychosort 对否决 SB-1047 的论点进行了很好的总结。

### 111

作者: @AndrewYNg
时间: 2024-09-29
链接: https://x.com/AndrewYNg/status/1840497561821651069
互动: Likes: 1,464; Retweets: 214; Replies: 66; Quotes: 31; Views: 158,553; Bookmarks: 66; isReply: 0

Thank you Governor @GavinNewsom for vetoing SB-1047 -- your pro-innovation leadership is much appreciated! 

And to the many people who've been pushing back on SB-1047, a huge thank you as well. Congratulations to all -- we won! 🎉 
 
Looking ahead, lets keep on protecting AI open-source and innovation. We must make sure AI policy is based on science, not science fiction!

感谢州长 @GavinNewsom 否决了 SB-1047 —— 您支持创新的领导力令人非常赞赏！

同时，也向所有一直抵制 SB-1047 的朋友们致以最诚挚的感谢。恭喜大家 —— 我们赢了！🎉

展望未来，我们必须继续保护 AI 的开源精神和创新活力。我们一定要确保 AI 政策是基于科学事实，而不是科幻想象！

### 112

作者: @AndrewYNg
时间: 2024-09-29
链接: https://x.com/AndrewYNg/status/1840502075593199931
互动: Likes: 138; Retweets: 6; Replies: 1; Quotes: 1; Views: 11,256; Bookmarks: 3; isReply: 1

@martin_casado @GavinNewsom Huge shoutout to you @martin_casado for the tremendous work you've done to push back on SB-1047 and other anti-open-source regulation. Thank you!

@martin_casado @GavinNewsom 必须向你 @martin_casado 表达由衷的感谢，感谢你为抵制 SB-1047 及其他反开源法规所付出的巨大努力。谢谢你！

### 113

作者: @AndrewYNg
时间: 2024-09-29
链接: https://x.com/AndrewYNg/status/1840515301106237858
互动: Likes: 9; Retweets: 1; Replies: 1; Quotes: 0; Views: 1,476; Bookmarks: 0; isReply: 1

@pentagoniac @thewendylee @latimes Thank you @pentagoniac for your tireless efforts speaking out against SB-1047! It has been great having you and the AI Alliance help spread the word regarding  why it was a broken, harmful bill.

@pentagoniac @thewendylee @latimes 感谢 @pentagoniac 为反对 SB-1047 所做的不懈努力！很高兴有您和 AI Alliance 帮助大家了解为何这项法案存在缺陷且危害深远。

### 114

作者: @AndrewYNg
时间: 2024-09-29
链接: https://x.com/AndrewYNg/status/1840515709190943085
互动: Likes: 108; Retweets: 0; Replies: 2; Quotes: 0; Views: 9,308; Bookmarks: 0; isReply: 1

@jeremyphoward Thank you @jeremyphoward for your speaking out against SB-1047! Much appreciate your vocal opposition to this ill-informed law!

@jeremyphoward 感谢您 @jeremyphoward 公开反对 SB-1047! 非常感谢您对这项欠考虑的法律表达的强烈反对！

### 115

作者: @AndrewYNg
时间: 2024-09-29
链接: https://x.com/AndrewYNg/status/1840516178948870569
互动: Likes: 30; Retweets: 0; Replies: 1; Quotes: 1; Views: 7,537; Bookmarks: 0; isReply: 1

@AnimaAnandkumar @GavinNewsom @Caltech Thank you @AnimaAnandkumar and the broader @Caltech community for speaking out against SB-1047. I appreciated particularly the letter you circulated explaining why the law would have been a bad idea.

@AnimaAnandkumar @GavinNewsom @Caltech 感谢 @AnimaAnandkumar 和更广泛的 @Caltech 社区对 SB-1047 提出异议。我尤其赞赏您们传阅的那封信，其中阐明了为何这项法律会是一个糟糕的提议。

### 116

作者: @AndrewYNg
时间: 2024-09-29
链接: https://x.com/AndrewYNg/status/1840516963405271113
互动: Likes: 750; Retweets: 25; Replies: 6; Quotes: 1; Views: 38,403; Bookmarks: 12; isReply: 1

@ylecun @GavinNewsom Thank you @ylecun for your consistently clear and thoughtful explanations for why SB-1047 was a bad idea. We are lucky to have you as such a strong champion for open-source and AI innovation!

@ylecun @GavinNewsom 感谢 @ylecun 始终如一地清晰且深思熟虑地解释了为什么 SB-1047 是个糟糕的主意。我们很幸运有你这样一位开源和 AI 创新（AI innovation）的坚定倡导者！

### 117

作者: @AndrewYNg
时间: 2024-09-29
链接: https://x.com/AndrewYNg/status/1840517975167967261
互动: Likes: 25; Retweets: 4; Replies: 1; Quotes: 0; Views: 1,637; Bookmarks: 0; isReply: 1

@chrislengerich @GavinNewsom Thank you @chrislengerich for your fighting SB-1047 and for your thoughtful analyses of the law. Even as the (bad) law kept getting amended repeatedly, that you kept publishing clear analyses of each revision really helped cut through the noise and confusion!

@chrislengerich @GavinNewsom 谢谢你，@chrislengerich，感谢你为反对 SB-1047 所做的努力，以及你对该法案富有洞察力的分析。即使这项（糟糕的）法案屡次修订，你仍然坚持发布对每次修改的清晰解读，这确实帮助大家拨开了喧嚣和困惑！

### 118

作者: @AndrewYNg
时间: 2024-09-29
链接: https://x.com/AndrewYNg/status/1840518403683172833
互动: Likes: 20; Retweets: 0; Replies: 1; Quotes: 0; Views: 2,507; Bookmarks: 0; isReply: 1

@AnjneyMidha @GavinNewsom Thank you @AnjneyMidha for being a consistent voice of reason in the discussion on SB-1047. It's been a pleasure watching you patiently reach out to and help multiple stakeholders understand why SB-1047 was an awful idea!

@AnjneyMidha @GavinNewsom 感谢 @AnjneyMidha 在关于 SB-1047 的讨论中始终保持理性发声。很高兴看到你耐心地与多方利益相关者沟通，并帮助他们理解为什么 SB-1047 是一个糟糕的主意！

### 119

作者: @AndrewYNg
时间: 2024-09-29
链接: https://x.com/AndrewYNg/status/1840519382390497441
互动: Likes: 477; Retweets: 15; Replies: 1; Quotes: 2; Views: 71,852; Bookmarks: 19; isReply: 1

@pmarca @GavinNewsom Thank you @pmarca for your leadership fighting SB1047. (I know the full story of what you've done to fight bad AI regulation is far from told; and, I'm grateful for your massive efforts here.) Having @a16z fight for a rational approach to AI has been a huge boon!

@pmarca @GavinNewsom 感谢 @pmarca 您在反对 SB1047 法案中发挥的领导作用。(我知道您为抵制糟糕的 AI 监管所做的一切还远未被完全公开；对此，我非常感谢您在此付出的巨大努力。）有 @a16z 这样为 AI 寻求理性方法而战的力量，真是帮了大忙！

### 120

作者: @AndrewYNg
时间: 2024-09-29
链接: https://x.com/AndrewYNg/status/1840520356114952231
互动: Likes: 51; Retweets: 1; Replies: 1; Quotes: 0; Views: 5,748; Bookmarks: 1; isReply: 1

@garrytan @GavinNewsom @ycombinator Thank you @garrytan and the @ycombinator team for all you've done to push back on SB 1047. It has been a pleasure seeing YC organize to argue for a rational approach to AI policy!

@garrytan @GavinNewsom @ycombinator 感谢 @garrytan 和 @ycombinator 团队在抵制 SB 1047 方面所做的一切努力。很高兴看到 YC 组织起来，倡导对 AI 政策采取理性的方法！

### 121

作者: @AndrewYNg
时间: 2024-09-29
链接: https://x.com/AndrewYNg/status/1840521131511697617
互动: Likes: 15; Retweets: 0; Replies: 1; Quotes: 0; Views: 3,525; Bookmarks: 1; isReply: 1

@RonConway @GavinNewsom Thank you @RonConway for your massive efforts reaching out to and helping many stakeholders think through AI policy. I'm grateful that you've been such a powerful voice of reason in debate on SB-1047!

@RonConway @GavinNewsom 谢谢 @RonConway 为联系众多利益相关者并帮助他们深入思考 AI（人工智能）政策所付出的巨大努力。我非常感谢你在 SB-1047 的辩论中，一直都是一个如此有力且理性的声音！

### 122

作者: @AndrewYNg
时间: 2024-09-29
链接: https://x.com/AndrewYNg/status/1840521890936598784
互动: Likes: 32; Retweets: 3; Replies: 3; Quotes: 0; Views: 2,201; Bookmarks: 0; isReply: 1

@deanwball Thank you @deanwball for your tirelessly writing and speaking on SB-1047. I've enjoyed many of your writings and am grateful for your consistently championing an approach to AI policy that targets bad conduct, rather than attacks AI models!

@deanwball 谢谢你 @deanwball，感谢你为 SB-1047 不知疲倦地撰写文章和发表演讲。我很欣赏你的诸多作品，并感谢你始终如一地倡导这样一种人工智能（AI）政策方法：它致力于针对不当行为，而非直接攻击 AI 模型本身！

### 123

作者: @AndrewYNg
时间: 2024-09-29
链接: https://x.com/AndrewYNg/status/1840523898653467108
互动: Likes: 44; Retweets: 1; Replies: 1; Quotes: 0; Views: 5,269; Bookmarks: 2; isReply: 1

@reidhoffman @GavinNewsom Thank you @reidhoffman for being a consistently rational voice in AI, and for advocating a responsible approach to bringing benefits to billions while also not being distracted by science fiction fears!

@reidhoffman @GavinNewsom 感谢你 @reidhoffman，在人工智能（AI）领域始终发出理性的声音，并倡导以负责任的方式为数十亿人带来益处，同时不被科幻式的担忧所困扰！

### 124

作者: @AndrewYNg
时间: 2024-09-29
链接: https://x.com/AndrewYNg/status/1840525012719329551
互动: Likes: 34; Retweets: 2; Replies: 0; Quotes: 1; Views: 6,026; Bookmarks: 1; isReply: 1

@psychosort @GavinNewsom Thank you @psychosort for your many thoughtful writings on SB-1047, and also your hard work debunking bad arguments -- I've really appreciated your cutting through the noise to the heart of why SB-1047 was a bad idea!

@psychosort @GavinNewsom 感谢 @psychosort 你关于 SB-1047 的诸多深思熟虑的文章，以及你为驳斥不当论点所付出的辛勤努力 —— 我真的很欣赏你拨开喧嚣，直达 SB-1047 为什么是个糟糕主意的核心！

### 125

作者: @AndrewYNg
时间: 2024-09-29
链接: https://x.com/AndrewYNg/status/1840525690770542797
互动: Likes: 195; Retweets: 10; Replies: 2; Quotes: 1; Views: 12,659; Bookmarks: 3; isReply: 1

@drfeifei @StanfordHAI @CAgovernor @GavinNewsom Thank you @drfeifei for your speaking out against SB-1047, and also for working toward a more rational approach to AI policy that protects research and innovation. It has been fantastic seeing you step into the fray and so effectively influence things for the better!

@drfeifei @StanfordHAI @CAgovernor @GavinNewsom 感谢 @drfeifei 您公开反对 SB-1047 法案，并致力于推动制定更理性的 AI（人工智能）政策，以保护研究和创新。非常高兴看到您能挺身而出，如此有效地积极影响了局面！

### 126

作者: @AndrewYNg
时间: 2024-09-29
链接: https://x.com/AndrewYNg/status/1840530050040631600
互动: Likes: 225; Retweets: 11; Replies: 2; Quotes: 2; Views: 15,038; Bookmarks: 2; isReply: 1

@bindureddy Thank you @bindureddy for fighting for open-source and against SB-1047. I appreciate especially your  pushing back against AGI hype -- which leads to science fiction based fears and bad laws like SB-1047!

@bindureddy 谢谢你，Bindu Reddy，为开源事业而奋斗，并反对 SB-1047 法案。我尤其赞赏你抵制通用人工智能（AGI）炒作 —— 这种炒作往往会引发科幻小说般的恐惧，并导致像 SB-1047 这样糟糕的法律出现！

### 127

作者: @AndrewYNg
时间: 2024-09-30
链接: https://x.com/AndrewYNg/status/1840547768894685497
互动: Likes: 39; Retweets: 0; Replies: 0; Quotes: 0; Views: 4,177; Bookmarks: 1; isReply: 1

@ClementDelangue @GavinNewsom Thank you @ClementDelangue for unfailingly  advocating for open-source, and speaking out against bad laws like SB-1047. Hugging Face has been a wonderful force bringing openness to AI!

@ClementDelangue @GavinNewsom 感谢 @ClementDelangue 始终如一地倡导开源，并公开反对像 SB-1047 这样有问题的法律。Hugging Face 一直是推动人工智能（AI）开放的重要力量！

### 128

作者: @AndrewYNg
时间: 2024-09-30
链接: https://x.com/AndrewYNg/status/1840788292750791046
互动: Likes: 436; Retweets: 79; Replies: 35; Quotes: 3; Views: 75,446; Bookmarks: 44; isReply: 0

AI policy should be based in science, not science fiction! 

With SB-1047 defeated, @dawnsongtweets gives a sound plan for taking a scientific approach to study  actual risks and mitigating harms. 

A couple of key ideas:
* Lets empower researchers to study AI risks, focusing on the question of marginal risk: I.e., how much does an AI application increase the risk of a negative outcome? 
* Lets also increase transparency of AI systems. For example, open-source and and red-teaming will help! 

Many of the opponents to SB-1047 have been strong champions of Responsible AI, long before it was trendy to talk about it. We take safety seriously; and, we want policy to based in science, not science fiction.

AI 政策应立足科学，而非科幻！

随着 SB-1047 法案被否决，@dawnsongtweets 提出了一项可靠的计划，旨在通过科学方法来研究实际风险并有效规避潜在危害。

其中有几个关键观点：
*  我们应该支持研究人员深入探究 AI 风险，尤其要关注边际风险（Marginal Risk）问题：例如，一个 AI 应用究竟会将负面结果的风险提高多少？
*  我们还应该提高 AI 系统的透明度。例如，通过开源和红队演练（Red-Teaming）等方式，将大有裨益！

许多反对 SB-1047 法案的人士，其实早在「负责任 AI（Responsible AI）」成为热门话题之前，就已经是其坚定的倡导者了。我们始终认真对待安全问题，并且希望 AI 政策能够以科学为基础，而非仅仅停留在科幻想象。

### 129

作者: @AndrewYNg
时间: 2024-10-01
链接: https://x.com/AndrewYNg/status/1841178556904456275
互动: Likes: 1,659; Retweets: 147; Replies: 55; Quotes: 21; Views: 109,190; Bookmarks: 202; isReply: 0

AI needs UI, and OpenAI's impressive new voice APIs  open up a lot of possibilities. Congrats @OpenAI team -- we'll soon be  seeing a whole new generation of speech applications!

AI 离不开 UI，而 OpenAI 全新且令人惊叹的语音 API（API）的推出，无疑开启了无数新的可能。恭喜 @OpenAI 团队，我们很快就能看到全新一代的语音应用程序蓬勃发展了！

### 130

作者: @AndrewYNg
时间: 2024-10-02
链接: https://x.com/AndrewYNg/status/1841496274350247951
互动: Likes: 1,658; Retweets: 300; Replies: 30; Quotes: 11; Views: 145,546; Bookmarks: 1,403; isReply: 0

Tokenization -- turning text into a sequence of integers -- is a key part of generative AI, and most API providers charge per million tokens. How does tokenization work? Learn the details of tokenization and RAG optimization in Retrieval Optimization: From Tokenization to Vector Quantization, created in collaboration with @qdrant_engine and taught by its Developer Relations Lead, @LukawskiKacper.

This course focuses on Retrieval augmented generation (RAG), which has two steps: First, a retriever finds relevant information; then, the generator uses what’s retrieved as context to produce a response. You’ll learn to optimize the first step (the retriever) by understanding how tokenization works and how it impacts the relevance of your search. In addition, you will also learn to measure and improve retrieval quality, speed, and memory.

In detail, you’ll:
- Learn about the internal workings of the embedding models and how your text turns into vectors.
- Understand how several tokenizers, such as Byte-Pair Encoding, WordPiece, Unigram, and SentencePiece work.
- Explore common challenges with tokenizers, such as unknown tokens, domain-specific identifiers, and numerical values, that can negatively affect your vector search.
- Understand how to measure the quality of your search across relevance, ranking, and score-related metrics.
- Understand how the main parameters in "HNSW", a graph-based algorithm, affect the relevance and speed of vector search, and how to tune its parameters.
- Experiment with the three major quantization methods – product, scalar, and binary – and learn how they impact memory requirements, search quality, and speed.

By the end of this course, you’ll have a solid understanding of how tokenization functions and how to optimize vector search in your RAG systems.

Please sign up here! https://t.co/wIrSEGAcb9

<p>Tokenization（分词）—— 将文本转化为整数序列的过程 —— 是生成式 AI（Generative AI）的一个关键环节，大多数 API 提供商都按每百万个 token 收费。那么，Tokenization 是如何工作的呢？在《检索优化：从 Tokenization 到向量量化》这门课程中，您将深入了解 Tokenization 和 RAG 优化的细节。这门课程是与 @qdrant_engine 合作推出，并由其开发者关系负责人 @LukawskiKacper 主讲。</p>
<p> 本课程重点聚焦检索增强生成（Retrieval Augmented Generation，RAG）技术，它包含两个核心步骤：首先，检索器（retriever）负责查找相关信息；然后，生成器（generator）利用这些检索到的内容作为上下文，来生成最终的响应。您将学习如何通过理解 Tokenization 的工作原理以及它如何影响搜索结果的相关性，从而优化 RAG 的第一步（即检索环节）。此外，您还将掌握衡量和提升检索质量、速度及内存效率的方法。</p>
<p> 具体来说，您将：</p>
<ul>
<li> 了解嵌入模型（embedding models）的内部机制，以及文本是如何被转化为向量的。</li>
<li> 理解几种主流的分词器（tokenizer），例如 Byte-Pair Encoding、WordPiece、Unigram 和 SentencePiece 的工作原理。</li>
<li> 探索分词器常见的挑战，例如未知 token、特定领域的标识符和数值，这些都可能对您的向量搜索产生负面影响。</li>
<li> 学习如何根据相关性、排名和与分数相关的指标来评估搜索质量。</li>
<li> 理解基于图的算法「HNSW」中的主要参数如何影响向量搜索的相关性和速度，以及如何对其进行调优。</li>
<li> 通过实践，体验三种主要的量化方法 —— 乘积量化（product quantization）、标量量化（scalar quantization）和二进制量化（binary quantization)—— 并了解它们如何影响内存需求、搜索质量和速度。</li>
</ul>
<p> 学完本课程后，您将对 Tokenization 的功能以及如何在 RAG 系统中优化向量搜索有一个扎实的理解。</p>
<p> 请在此处注册！ <a href="https://t.co/wIrSEGAcb9">https://t.co/wIrSEGAcb9</a></p>

### 131

作者: @AndrewYNg
时间: 2024-10-03
链接: https://x.com/AndrewYNg/status/1841952373218123996
互动: Likes: 624; Retweets: 122; Replies: 25; Quotes: 8; Views: 91,737; Bookmarks: 269; isReply: 0

How AI will change Coding & Education? I'm looking forward to this chat with @mehran_sahami. Mehran is a legendary programming instructor and an old friend, and has been thinking a lot about how AI is transforming coding. Come join us -- this will be fun! 

Please register here: https://t.co/yWO7ovW916

Thank you @jpaxtonh and @StanfordOnline for hosting!

人工智能（AI）将如何改变编程和教育？我非常期待与 @mehran_sahami 的这场对话。Mehran 是一位传奇的编程讲师，也是我的一位老朋友，他一直在深入思考人工智能是如何重塑编程领域的。快来加入我们吧 —— 这场活动一定会非常有趣！

请通过此链接注册：https://t.co/yWO9ovW916

感谢 @jpaxtonh 和 @StanfordOnline 的慷慨主持！

### 132

作者: @AndrewYNg
时间: 2024-10-08
链接: https://x.com/AndrewYNg/status/1843711446552846732
互动: Likes: 4,825; Retweets: 460; Replies: 83; Quotes: 29; Views: 172,976; Bookmarks: 217; isReply: 0

I was the first to call Geoff Hinton "Godfather of Deep Learning", which later became "Godfather of AI." Thrilled to see him win the Nobel prize together with John Hopfield for AI. Congrats @geoffreyhinton!

我最先称 Geoff Hinton 为「深度学习教父」，后来他也被称为「AI 教父」。很高兴看到他与 John Hopfield 因在 AI 领域的贡献而共同获得诺贝尔奖。祝贺 @geoffreyhinton!

### 133

作者: @AndrewYNg
时间: 2024-10-08
链接: https://x.com/AndrewYNg/status/1843764485632524664
互动: Likes: 763; Retweets: 84; Replies: 13; Quotes: 3; Views: 81,481; Bookmarks: 43; isReply: 0

Lisa Su's leadership of AMD has been phenomenal. 10 years ago, AMD was in dire straits, was losing money  and faced intense competition from Intel (CPUs) and NVIDIA (GPUs). She turned the company around, introduced Ryzen and Epyc processors, introduced the Zen architecture, acquired Xilinx, and is now making a good showing with MI300/MI350 for AI workloads. I've come to deeply respect her as a leader. Congratulations @LisaSu on these last ten years!

Lisa Su 领导下的 AMD 表现非凡。回溯到十年前，AMD 正深陷困境，不仅亏损严重，还面临着来自 Intel（中央处理器 CPUs）和 NVIDIA（图形处理器 GPUs）的激烈竞争。她成功地使公司扭亏为盈，重回正轨，推出了 Ryzen 和 Epyc 处理器，引入了 Zen 架构，并成功收购了 Xilinx。目前，AMD 凭借 MI300/MI350 在 AI（人工智能）工作负载领域表现强劲。我作为一名领导者，对她深感敬佩。祝贺 @LisaSu 在过去十年取得的辉煌成就！

### 134

作者: @AndrewYNg
时间: 2024-10-09
链接: https://x.com/AndrewYNg/status/1843995968636866799
互动: Likes: 1,415; Retweets: 149; Replies: 35; Quotes: 9; Views: 72,621; Bookmarks: 38; isReply: 0

Amazing -- even more Nobel Prizes to AI people! Congrats to Google's @demishassabis &amp; John Jumper, and University of Washington's David Baker for their work on AI for protein sequences. AlphaFold, and @UWproteindesign's protein design work , were real breakthroughs!

太棒了 —— 甚至有更多的诺贝尔奖被授予了 AI（Artificial Intelligence）领域的科学家！祝贺 Google 的 Demis Hassabis 和 John Jumper，以及华盛顿大学的 David Baker，他们因在利用 AI 处理蛋白质序列方面的工作而获此殊荣。AlphaFold 项目，以及 @UWproteindesign 团队的蛋白质设计工作，都是真正的重大突破！

### 135

作者: @AndrewYNg
时间: 2024-10-09
链接: https://x.com/AndrewYNg/status/1844092080987177409
互动: Likes: 1,615; Retweets: 247; Replies: 30; Quotes: 13; Views: 131,022; Bookmarks: 935; isReply: 0

"Introducing Multimodal Llama 3.2": As promised two weeks ago, here's the short course on Meta's latest open model!

This short course is created with @Meta and taught by @asangani7, Director of AI Partner Engineering at Meta.

Meta’s Llama family of models is leading the way in open models, allowing anyone to download, customize, fine-tune, or build new applications on top of them.

Learn about the vision capabilities of the Llama 3.2, and use it for image classification, prompting, tokenization, tool-calling. You'll also learn about the open-source Llama stack, which gives building blocks for many different stages of the LLM application life cycle.

In detail, you’ll:
- Learn what are the features of Meta's four newest models, and when to use which Llama model.
- Learn best practices for multimodal prompting, with applications to advanced image reasoning, illustrated by many examples: Understanding errors on a car dashboard, adding up the total of photographed restaurant receipts, grading written math homework.
- Use different roles—system, user, assistant, ipython—in the Llama 3.1 and 3.2 models  and the prompt format that identifies those roles.
- Understand how Llama uses the tiktoken tokenizer, and how it has expanded to a 128k vocabulary size that improves encoding efficiency and multilingual support.
- Learn how to prompt Llama to call built-in and custom tools (functions) with examples for web search and solving math equations.
- Learn about Llama Stack, a standardized interface for common toolchain components like fine-tuning or synthetic data generation, useful for building agentic applications.

By the end of this course, you’ll be equipped to build out new applications with the new Llama 3.2.

Thank you to @Ahmad_Al_Dahle, Amit Sangani, and the whole AI at Meta team @AIatMeta for all the hard work on Llama 3.2 — we’re excited to make these open models even more accessible to more developers with this new course! 

Please sign up here!  https://t.co/Flp5Ae9apy

「多模态 Llama 3.2 来了！」：正如两周前我们承诺的那样，Meta 最新开源模型的速成课程现在正式推出！

这门速成课程是 Meta 公司与 @Meta 合作开发，并由 Meta AI 合作伙伴工程总监 Amit Sangani（即 @asangani7）亲自授课。

Meta 的 Llama 模型家族在开源模型领域持续领跑，让每个人都能自由下载、定制、微调，或在此基础上构建全新的应用程序。

在本课程中，你将深入了解 Llama 3.2 的视觉能力，并学会如何将其应用于图像分类、提示（prompting）、Token 化（tokenization）和工具调用。你还将学习到开源的 Llama Stack，它为大语言模型（LLM）应用程序生命周期的多个阶段提供了坚实的构建模块。

具体来说，你将：
- 掌握 Meta 四个最新模型的独特功能，并了解在不同场景下如何选择最合适的 Llama 模型。
- 学习多模态提示的最佳实践，并将其应用于高级图像推理任务。课程将通过丰富的实例进行讲解，包括：识别汽车仪表盘上的错误、计算照片中餐厅收据的总金额、批改手写的数学作业等。
- 在 Llama 3.1 和 3.2 模型中，使用不同的角色 ——system（系统）、user（用户）、assistant（助手）和 ipython，并学习识别这些角色的提示格式。
- 理解 Llama 如何利用 tiktoken 分词器（tokenizer），以及它如何将词汇量扩展到 128k，从而显著提升编码效率和多语言支持能力。
- 学习如何向 Llama 发出提示，使其调用内置工具和自定义函数（functions），并辅以网页搜索和解决数学方程的实际案例。
- 了解 Llama Stack—— 一个为微调（fine-tuning）或合成数据生成（synthetic data generation）等常见工具链组件提供标准化接口的平台，对于开发 AI 智能体（AI Agent）应用至关重要。

完成本课程后，你将完全有能力利用全新的 Llama 3.2 开发出各类创新应用。

衷心感谢 Ahmad Al Dahle（@Ahmad_Al_Dahle）、Amit Sangani 以及 Meta AI 团队（即 @AIatMeta）为 Llama 3.2 所付出的辛勤努力 —— 我们非常高兴能通过这门新课程，让更多开发者能够更便捷地接触和使用这些优秀的开源模型！

请点击此处注册！ https://t.co/Flp5Ae9apy

### 136

作者: @AndrewYNg
时间: 2024-10-16
链接: https://x.com/AndrewYNg/status/1846608552359833674
互动: Likes: 856; Retweets: 139; Replies: 60; Quotes: 4; Views: 80,408; Bookmarks: 584; isReply: 0

New short course: Serverless Agentic Workflows with Amazon Bedrock. Learn to build and deploy serverless agents in this course created with @awscloud and taught by @mikegchambers, a Senior Developer Advocate at AWS specializing in GenAI. (Disclosure: I serve on Amazon's board.)

Generative AI applications are becoming more complex, sophisticated, and agentic. Agentic applications have workloads that can be hard to predict in advance -- for example, what tools will it decide to call? -- and a serverless architecture helps you efficiently providing on-demand resources.

This course teaches you to build and deploy a serverless agentic application. You’ll learn to create agents with tools, code execution, and guardrails, and build responsible agents for business use cases:
- Build a customer service bot for a fictional tea mug business that can answering questions, retrieve information, and process orders.
- Connect your customer service agent to a CRM to get customer info and log support tickets in real-time.
- Explore how you invoke the agent, and see the trace to review the agent’s thought process and observation loop until it reaches its final output.
- Attach a code interpreter to your agent, giving it the ability to perform accurate calculations by writing and running its own Python code.
- Implement guardrails to prevent your agent from revealing sensitive information or using inappropriate language.

By the end, you will have built a sophisticated AI agent capable of handling real-world customer support scenarios.

Please sign up here! https://t.co/FQKGJNBPwp

全新短期课程：使用 Amazon Bedrock 构建无服务器 AI 智能体工作流。这门课程由 @awscloud 打造，并由 AWS 专门研究生成式 AI（Generative AI）的高级开发者倡导者 @mikegchambers 亲自授课，旨在帮助您学习如何构建和部署无服务器 AI 智能体。（披露：我目前担任 Amazon 董事会成员。）

生成式 AI（Generative AI）应用程序正变得日益复杂、精巧，并具备更强的智能体（agentic）能力。这类智能体应用程序的工作负载往往难以提前预知 —— 比如，AI 智能体最终会决定调用哪些工具？—— 而无服务器架构（serverless architecture）则能帮助您高效地按需提供所需资源。

本课程将指导您如何构建和部署一个无服务器 AI 智能体应用程序。您将学习如何创建具备工具调用、代码执行和安全防护机制（guardrails）的 AI 智能体，并为实际业务场景构建负责任的 AI 智能体：
- 为一家虚构的茶杯销售业务打造一个客户服务机器人，使其能够回答问题、检索信息并处理订单。
- 将您的客户服务 AI 智能体与客户关系管理系统（CRM）连接，以实时获取客户信息并记录支持工单。
- 深入了解如何调用 AI 智能体，并通过追踪功能审查 AI 智能体的思维过程和观察循环，直至其得出最终输出。
- 为您的 AI 智能体附加一个代码解释器，使其能够通过编写和运行 Python 代码来执行精确计算。
- 实施安全防护机制，防止您的 AI 智能体泄露敏感信息或使用不当语言。

学完本课程后，您将能够构建一个复杂的 AI 智能体，足以应对真实世界的客户支持场景。

请点击此处报名参加！https://t.co/FQKGJNBPwp

### 137

作者: @AndrewYNg
时间: 2024-10-17
链接: https://x.com/AndrewYNg/status/1846952116516278591
互动: Likes: 280; Retweets: 62; Replies: 61; Quotes: 3; Views: 43,133; Bookmarks: 61; isReply: 0

It’s high time to take geoengineering more seriously as a potential tool to mitigate climate change. 2023 was the hottest year on record, and 2024 is likely to top that. In the United States, Hurricane Helene caused over 200 deaths, and Hurricane Milton's death toll is at least two dozen. It’s well established that the hurricanes are growing stronger as global temperatures rise.

While stratospheric aerosol injection (SAI) — which sprays particles (aerosols) in the atmosphere to provide a small amount of shade from the sun — is far from a perfect solution, we should take it seriously as a possible tool for saving lives. A few months ago, my collaborators and I released a climate emulator, Planet Parasol https://t.co/OxtaQMyDuL , that you can play with to simulate different SAI scenarios to understand its possible impact. By using AI to model its impact and thereby advance our understanding of SAI, we’ll be better prepared to decide if this is a good step.

The key idea of SAI, which is a form of climate geoengineering, is to spray reflective particles into the stratosphere to reflect a little more, say 1%, of the sunlight that otherwise would fall on Earth back into space. This small increase in reflected sunlight would be sufficient to mitigate much of the impact of human-induced warming. For example, in 1991, Mount Pinatubo ejected almost 20 tons of aerosols (sulfur dioxide) into the atmosphere and cooled down the planet by around 0.5 degrees Celsius over the following year. We should be able to induce cooling equivalent to, say, a fraction of Mount Pinatubo, via a fair, international process that’s backed by science.

There are many criticisms of SAI, such as:
- It could have unintended climate consequences, for example, disrupting local weather patterns and creating droughts or floods.
- If it were started and then stopped suddenly, it could lead to sudden warming, known as “termination shock.”
- Depending on the aerosol used (sulfur dioxide is a leading candidate), it could contribute to pollution and/or ozone depletion.
- It might reduce urgency to decarbonize (an example of a “moral hazard”).

In addition, many people have a visceral emotional reaction, as I once did before I understood the science more deeply, against “playing god” by daring to engineer the planet.

All these downsides should be balanced against the reality that people are dying.

I’m moved by meteorologist John Morales’ emotional account of the havoc caused by Hurricane Milton. The New York Times quoted him as saying, “It claims lives. It also wrecks lives.” https://t.co/MKD8GIrV5g 

Skyfire AI, a drone company led by CEO Don Mathis that my team AI Fund helped to co-build, was recently on the ground in the aftermath of Helene and Milton, deploying drones to help emergency responders survey remote areas and find survivors. Mathis reports that Skyfire was credited with saving at least 13 lives. https://t.co/rsrcWMka17 On Monday, I also spoke about AI applied to renewable energy with AES’ CEO Andres Gluski and CPO Chris Shelton. You can view our conversation here: https://t.co/kzKBp3NmrM

While I’m glad that AI can help mitigate these disasters, it saddens me that so many lives have already been lost due to climate-influenced causes. My mind frequently returns to SAI as one of the few untapped tools in our arsenal that can help. We need to be investing in SAI research now.

I’m grateful to my collaborators on the Planet Parasol emulator (a group that includes many climate scientists) including Jeremy Irvin, Daniele Visioni, Ben Kravitz, Dakota Gruener, Chris Smith, and Duncan Watson-Parris. MIT Technology Review’s James Temple wrote about his experience playing with our emulator and also outlines fair criticisms. (See https://t.co/ufXAKNBiLQ ) Much work remains to be done, and making sure our actions are based on science — a task that AI can help with (witness the recent Chemistry and Physics Nobel Prizes going to innovators in AI!) – will help us make better decisions.

If you’re interested in learning more about SAI, check out this recent panel discussion (https://t.co/UFerfFIskp) where I spoke alongside climate scientists Chris Field, David Keith, Douglas MacMartin, and Simone Tilmes about the science and possible roadmaps ahead.

[Original text: https://t.co/u1thkhK0XY ]

现在，是时候更认真地将地球工程（geoengineering）视为一种潜在的气候变化缓解工具了。2023 年是史上最热的一年，而 2024 年很可能打破这一纪录。在美国，飓风海伦（Hurricane Helene）造成 200 多人死亡，飓风米尔顿（Hurricane Milton）的死亡人数也至少有 24 人。随着全球气温上升，飓风强度不断增强，这已是公认的事实。

尽管平流层气溶胶注入（SAI，Stratospheric Aerosol Injection）— 即向大气中喷洒颗粒（气溶胶，aerosols），以提供少量阳光遮蔽 — 远非完美的解决方案，但我们应该将其视为一种可能挽救生命的工具，认真对待。几个月前，我的合作者和我发布了一个气候模拟器（climate emulator）— Planet Parasol https://t.co/OxtaQMyDuL — 你可以通过它模拟不同的 SAI 场景，从而了解其潜在影响。通过利用 AI（人工智能）模拟 SAI 的影响，并以此加深我们对其的理解，我们将能更好地决定这是否是值得迈出的一步。

SAI 作为一种气候地球工程形式，其核心思想是向平流层（stratosphere）喷射反射性颗粒，使原本会抵达地球的太阳光，有少量（比如 1%）被反射回太空。太阳光反射量的微小增加，就足以大大缓解人类活动导致的气候变暖的影响。举例来说，1991 年，皮纳图博火山（Mount Pinatubo）向大气中喷射了近 20 吨气溶胶（二氧化硫，sulfur dioxide），使得接下来一年地球的温度降低了大约 0.5 摄氏度。我们应该能够通过一个公平、并有科学支撑的国际进程，实现相当于皮纳图博火山喷发一小部分的降温效果。

SAI 面临诸多质疑，例如：
- 它可能带来意想不到的气候后果，比如扰乱局部天气模式，引发干旱或洪水。
- 如果该项目一旦启动又突然停止，可能会导致地球温度骤然升高，这被称为「终止冲击（termination shock）」。
- 根据所使用的气溶胶类型（二氧化硫是主要的候选物质之一），它可能导致污染和 / 或臭氧损耗。
- 它可能会削弱人们减少碳排放的紧迫性（这是一种「道德风险（moral hazard）」的表现）。

此外，很多人对通过大胆改造地球来「扮演上帝」抱有一种本能的情绪抵触，正如我在更深入了解科学之前也曾有过这种感受。

所有这些不利因素，都必须与当前正在发生的生命逝去的现实相权衡。

气象学家 John Morales 对飓风米尔顿肆虐造成破坏的深情叙述让我深受触动。《纽约时报》引用他的话：「它夺走了生命，也摧毁了生活。」https://t.co/MKD8GIrV5g

Skyfire AI 是一家由首席执行官 Don Mathis 领导的无人机公司，我的团队 AI Fund 曾帮助共同建立。最近，Skyfire AI 在飓风海伦和米尔顿过后抵达受灾现场，部署无人机协助紧急救援人员勘测偏远地区并寻找幸存者。Mathis 报告称，Skyfire 因成功挽救至少 13 条生命而受到表彰。https://t.co/rsrcWMka17 周一，我还与 AES 的首席执行官 Andres Gluski 和首席产品官 Chris Shelton 讨论了 AI 在可再生能源领域的应用。你可以在这里观看我们的对话： https://t.co/kzKBp3NmrM

虽然我很高兴 AI 能够帮助缓解这些灾难，但令我悲伤的是，已经有如此多的生命因气候影响而逝去。我的思绪常常回到 SAI，将其视为我们应对气候挑战的「工具箱」中为数不多的、尚未充分利用的工具之一。我们现在亟需投资 SAI 的研究。

我非常感谢我的 Planet Parasol 模拟器合作者们（一个由众多气候科学家组成的团队），包括 Jeremy Irvin、Daniele Visioni、Ben Kravitz、Dakota Gruener、Chris Smith 和 Duncan Watson-Parris。MIT Technology Review 的 James Temple 撰文描述了他使用我们模拟器的体验，并提出了公正的批评意见。(参见 https://t.co/ufXAKNBiLQ）还有很多工作尚待完成，而确保我们的行动基于科学 —— 这项 AI 可以提供帮助的任务（请看最近的诺贝尔化学奖和物理学奖都颁给了 AI 领域的创新者！)—— 将帮助我们做出更明智的决策。

如果你有兴趣了解更多关于 SAI 的信息，请查看这场近期的小组讨论（https://t.co/UFerfFIskp），我与气候科学家 Chris Field、David Keith、Douglas MacMartin 和 Simone Tilmes 一同探讨了相关科学原理和未来的可能路线图。

[原始文本： https://t.co/u1thkhK0XY]

### 138

作者: @AndrewYNg
时间: 2024-10-17
链接: https://x.com/AndrewYNg/status/1846978449346646089
互动: Likes: 2; Retweets: 0; Replies: 0; Quotes: 0; Views: 594; Bookmarks: 0; isReply: 1

@DiggerofAI Yup. Reducing shipping emissions reduced pollution, but also reduced sunlight reflection and thus accelerating warming. With SAI, we would spray aerosols high up in the stratosphere, where it'll last longer. This gets us more cooling and less pollution than shipping emissions.

@DiggerofAI 没错。减少航运排放（shipping emissions）确实降低了污染，但同时也减少了阳光反射，进而加速了全球变暖。而通过平流层气溶胶注入（SAI），我们可以在平流层高处喷洒气溶胶（aerosols），在那里它们能停留更久。相比于航运排放，这种方式能带来更多的降温效果，同时产生的污染也更少。

### 139

作者: @AndrewYNg
时间: 2024-10-23
链接: https://x.com/AndrewYNg/status/1849112129904738656
互动: Likes: 1,493; Retweets: 260; Replies: 91; Quotes: 45; Views: 339,721; Bookmarks: 1,405; isReply: 0

New short course: Practical Multi AI Agents and Advanced Use Cases with crewAI. Learn to build and deploy advanced agent-based systems in real applications in this course, created with @crewAIInc and taught by its founder, @joaomdmoura! (Disclosure: I've made a small seed investment in CrewAI.)

In this course, you’ll learn how to create advanced agent-based apps that use external tools, do performance testing, can be trained with human feedback, and perform multiple tasks with different large language models.

You will build several practical agentic apps that provide real business value, such as an automated project planning system, lead scoring and engagement pipeline, customer support data analysis, and a robust content creation system.

In detail, you will learn how to:
- Create these multi-agent systems with the building blocks of tasks, agents, and crews, along with the different things that make them work, such as caching, memory, and guardrails.
- Integrate your multi-agent application with internal and external systems.
- Connect multiple agents in complex setups, including parallel, sequential, and hybrid configurations, and create flows involving multiple agentic applications working together.
- Test your agentic workflow and train it using human feedback to optimize its performance for better and more consistent results.
- Work with multiple LLMs in your multi-agent system, using the appropriate model sizes and providers to fit each agent’s specific task.
- Start a project from scratch in your environment and prepare it for deployment.

You’ll also learn from an interview between João and Jacob Wilson, the Commercial GenAI Principal at PwC , in which they discuss deploying agentic workflows in real industry use cases.

By the end of this course, you will be equipped to start building custom multi-agentic systems for your work.

Please sign up here! https://t.co/JkD52B3ONA

新课程上线：crewAI 实用多 **AI 智能体 **（AI Agent）与高级应用案例。本课程由 @crewAIInc 及其创始人 @joaomdmoura 倾力打造并亲自授课，将带你学习如何在实际应用中构建和部署先进的 ** 基于智能体的系统 **（agent-based systems)！（声明：我已对 CrewAI 进行了小额种子投资。)

在这门课程中，你将学会如何创建高级的 ** 智能体应用 **（agentic apps），这些应用能够利用外部工具、进行性能测试、通过人工反馈进行训练，并能结合不同的 ** 大语言模型 **（LLM）执行多项任务。

你将亲手搭建多个具有实际商业价值的智能体应用，例如：自动项目规划系统、潜在客户评分和互动流程、客户支持数据分析，以及强大的内容创作系统。

具体来说，你将学习以下内容：
- 如何利用任务、智能体和「船员」(crews）这些核心构建模块，结合缓存、内存和 ** 护栏 **（guardrails）等关键要素，来创建多智能体系统。
- 如何将你的多智能体应用程序与内部及外部系统进行集成。
- 如何在复杂的配置（包括并行、顺序和混合模式）中连接多个智能体，并创建涉及多个智能体应用协同工作的流程。
- 如何测试你的 ** 智能体工作流 **（agentic workflow），并利用人工反馈进行训练，从而优化其性能，获得更出色、更稳定的结果。
- 如何在你的多智能体系统中有效运用多个 **LLM**，根据每个智能体的特定任务，选择合适的模型规模和提供商。
- 如何在自己的环境中从零开始一个项目，并为后续部署做好准备。

你还将从 João 与普华永道（PwC）商业 ** 生成式 AI**（Generative AI）负责人 Jacob Wilson 的一次访谈中获益，他们将共同探讨如何在真实的行业用例中部署智能体工作流。

完成本课程后，你将完全有能力为你的工作量身定制并构建多智能体系统。

请点击此处注册！ https://t.co/JkD52B3ONA

### 140

作者: @AndrewYNg
时间: 2024-10-26
链接: https://x.com/AndrewYNg/status/1850246368126021744
互动: Likes: 5; Retweets: 0; Replies: 1; Quotes: 0; Views: 4,158; Bookmarks: 2; isReply: 1

@vishalmisra Cool visualization!

@vishalmisra 很棒的（数据）可视化！

### 141

作者: @AndrewYNg
时间: 2024-10-26
链接: https://x.com/AndrewYNg/status/1850280961768104332
互动: Likes: 421; Retweets: 66; Replies: 56; Quotes: 6; Views: 112,914; Bookmarks: 79; isReply: 0

Congrats @andrewdfeldman and @CerebrasSystems for a huge leap forward and setting a new speed record for serving Llama 3.1-70B. 2100 tokens/sec is blazingly fast for a 70B model. This is great for agentic AI!

恭喜 @andrewdfeldman 和 @CerebrasSystems，他们在 Llama 3.1-70B 模型的服务方面取得了巨大突破，并创下了新的速度纪录。对于一个 70B 模型来说，每秒 2100 个 Token 的处理速度可谓极其迅速。这对 AI 智能体（agentic AI）的发展而言，无疑是重大利好！

### 142

作者: @AndrewYNg
时间: 2024-10-28
链接: https://x.com/AndrewYNg/status/1850912176896463328
互动: Likes: 879; Retweets: 180; Replies: 69; Quotes: 12; Views: 87,883; Bookmarks: 392; isReply: 0

Startups live or die by their ability to execute at speed. For large companies, too, the speed with which an innovation team is able to iterate has a huge impact on its odds of success. Generative AI makes it possible to quickly prototype AI capabilities. AI capabilities that used to take months can sometimes be built in days or hours by simply prompting a large language model. I find this speed exciting and have been thinking about how to help startups and large companies alike go faster.

I’ve been obsessed with speedy execution for a long time. When working on a project, I am loath to take two weeks to do something that I could do in one week. The price of moving at that pace is not that we take one week longer (which might be okay) but that we’re 2x slower (which is not)!

When building an AI-powered product, there are many steps in designing, building, shipping, and scaling the product that are distinct from building the AI capability, and our ability to execute these other steps has not sped up as much as the AI part. But the speed with which we can prototype AI creates significant pressure to speed up these other steps, too. If it took 6 months to collect data, train a supervised learning algorithm, and deploy the model to the cloud, it might be okay to take 2 months to get user feedback. But if it takes a week to build a prototype, waiting 2 months for feedback seems intolerably slow!

I’d like to focus on one key step of building applications: getting user feedback. A core part of the iterative workflow of designing and building a product (popularized by Eric Ries in his book The Lean Startup) is to build a prototype (or MVP, minimum viable product), get user feedback on it, and to use that feedback to drive improvements. The faster you can move through this loop — which may require many iterations — the faster you can design a product that fits the market. This is why AI Fund, a venture studio that I lead, uses many fast, scrappy tactics to get feedback.

For B2C (business to consumer) offerings, here is a menu of some options for getting customer feedback:
1. Ask 3 friends or team members to look at the product and let you know what they think (this might take ~0.5 days).
2. Ask 10 friends or team members to take a look (~2 days).
3. Send it to 100 trusted/volunteer alpha testers (~1 week?).
4. Send it to 1,000 users to get qualitative or quantitative feedback (~2 weeks?).
5. Incorporate it into an existing product to get feedback (1 to 2 months?).
6. Roll it out to a large user base of an existing product and do rigorous A/B testing.

As we go down this list, we get (probably) more accurate feedback, but the time needed to get that feedback increases significantly. Also, the tactics at the top of the list create basically no risk, and thus it’s safe to repeatedly call on them, even with preliminary ideas and prototypes. Another advantage of the tactics further up the list is that we get more qualitative feedback (for example, do users seem confused? Are they telling us they really need one additional feature?), which sparks better ideas for how to change our product than an A/B test, which tells us with rigor whether a particular implementation works but is less likely to point us in new directions to try. I recommend using the fast feedback tactics first. As we exhaust the options for learning quickly, we can try the slower tactics.

With these tactics, scrappy startup leaders and innovation-team leaders in large companies can go faster and have a much higher chance of success.

The mantra “move fast and break things” got a bad reputation because, well, it broke things. Unfortunately, some have interpreted this to mean we should not move fast, but I disagree. A better mantra is “move fast and be responsible.” There are many ways to prototype and test quickly without shipping a product that can cause significant harm. In fact, prototyping and testing/auditing quickly before launching to a large audience is a good way to identify and mitigate potential problems.

There are numerous AI opportunities ahead, and our tools are getting better and better to pursue them at speed, which is exhilarating!

[Original text: https://t.co/NeMP4DKdDX ]

初创公司的生死存亡，往往取决于它们快速执行的能力。对于大型公司而言，创新团队迭代（iterate）的速度，也对其成功几率有着举足轻重的影响。生成式 AI（Generative AI）的出现，使得快速构建 AI 能力原型成为可能。过去需要数月才能实现的 AI 能力，现在可能只需向大语言模型（LLM / Large Language Model）发出提示，就能在几天甚至几小时内完成。这种惊人的速度让我感到无比兴奋，我也一直在思考如何帮助初创公司和大型企业都能够跑得更快。

长期以来，我一直热衷于追求快速执行。在进行项目时，我非常不喜欢花两周时间去做一周内就能完成的事情。以那种速度前进的代价，不是我们多花了一周时间（这可能还在接受范围），而是我们的速度慢了整整一倍（这是绝对不能接受的)！

在构建一款 AI 驱动的产品时，从设计、构建、交付到规模化产品的许多步骤，都与开发 AI 能力本身有所不同。在提速方面，这些非 AI 部分的执行速度，并没有像 AI 能力开发那样显著。然而，我们快速构建 AI 原型的能力，也迫使我们必须加快这些其他步骤的速度。如果收集数据、训练监督学习算法（supervised learning algorithm）并将模型部署到云端需要 6 个月，那么花 2 个月时间来获取用户反馈或许还可以接受。但如果构建一个原型只需要一周，那么等待 2 个月才能获得反馈，就显得慢得让人无法忍受了！

我想重点谈谈应用程序构建中的一个关键步骤：获取用户反馈。产品设计和构建迭代工作流程中的一个核心环节（Eric Ries 在他的著作《精益创业》（The Lean Startup）中普及了这一理念），就是先构建一个原型（或 MVP，最小可行产品），然后收集用户对其的反馈，并利用这些反馈来推动产品改进。这个循环（可能需要多次迭代）运行得越快，你就能越快地设计出符合市场需求的产品。这就是我所领导的风险投资工作室（venture studio）AI Fund 采用许多快速、轻量级策略来获取反馈的原因。

对于 B2C（business to consumer）产品，这里有一些获取客户反馈的选项：
1. 请 3 位朋友或团队成员查看产品，让他们分享看法（大约半天）。
2. 请 10 位朋友或团队成员查看产品（大约 2 天）。
3. 将其发送给 100 位值得信赖的或志愿的 alpha 测试人员（大约 1 周）。
4. 将其发送给 1,000 位用户以获取定性或定量反馈（大约 2 周）。
5. 将其整合到现有产品中以获取反馈（1 到 2 个月）。
6. 将其推广到现有产品的大量用户群，并进行严格的 A/B 测试。

随着我们在列表中往下探索，我们可能会获得更准确的反馈，但获取这些反馈所需的时间也大幅增加。此外，列表顶部的策略几乎没有风险，因此即使是初步的想法和原型，也可以安全且反复地使用。列表靠前策略的另一个优势是，我们能获得更多定性反馈（例如，用户是否显得困惑？他们是否告诉我们确实需要某个额外功能？），这比 A/B 测试更能激发我们改进产品的绝妙想法。A/B 测试能严谨地告诉我们某个特定实现是否有效，但却不太可能为我们指明新的尝试方向。因此，我建议优先使用快速反馈策略。当快速学习的选项被充分利用后，我们再尝试较慢的策略。

通过这些策略，那些务实的初创公司领导者和大型企业的创新团队领导者都能跑得更快，并大幅提高成功几率。

「快速行动，打破常规」这句口号之所以声名狼藉，就是因为它确实造成了破坏。不幸的是，有些人因此误以为我们不应该快速行动，但我对此并不认同。一个更好的口号应该是「快速行动，负责任」。有很多方法可以快速构建原型和测试，同时避免发布可能造成重大损害的产品。事实上，在向大量受众发布之前，快速构建原型并进行测试 / 验证，是识别和减轻潜在问题的好方法。

未来还有无数的 AI 机遇，我们的工具也变得越来越好，可以高速地抓住它们，这着实令人兴奋！

[原文链接：https://t.co/NeMP4DKdDX]

### 143

作者: @AndrewYNg
时间: 2024-10-31
链接: https://x.com/AndrewYNg/status/1852107599254073821
互动: Likes: 307; Retweets: 41; Replies: 48; Quotes: 0; Views: 46,546; Bookmarks: 59; isReply: 0

Happy Halloween! 🎃 

On this spooky day, The Batch continues its annual tradition of exploring fears related to AI. This special edition has 5 articles: 
* AI Burns All the Energy 
* Innovation Dies
* No Work for Coders
* Benchmarks Are Meaningless
* Synthetic Data Distorts Models

Are these things we should worry about? Check it out here: https://t.co/Vt5xnhZToT

万圣节快乐！🎃

在这个特别的万圣节，The Batch 延续了每年探索与 AI（人工智能）相关担忧的传统。本期特辑包含 5 篇文章，探讨了以下主题：
* AI 耗尽所有能源
* 创新停滞不前
* 程序员将面临失业
* 基准测试变得毫无意义
* 合成数据误导模型这些是我们需要担忧的问题吗？点击这里了解详情：https://t.co/Vt5xnhZToT

### 144

作者: @AndrewYNg
时间: 2024-11-05
链接: https://x.com/AndrewYNg/status/1853653742509502571
互动: Likes: 2,768; Retweets: 363; Replies: 51; Quotes: 22; Views: 192,478; Bookmarks: 1,309; isReply: 0

It finally happened -- thanks to people learning to write AI code, Python is now the top programming language on GitHub! 

If you want to learn Python, check out https://t.co/zpIxRSuky4's free course AI Python for Beginners.

它终于来了 -- 得益于越来越多的人开始学习编写 AI 代码，Python 如今已成为 GitHub 上最受欢迎的编程语言！

如果你也想学习 Python，不妨了解一下 https://t.co/zpIxRSuky4 提供的免费课程《AI Python for Beginners》（面向初学者的 AI Python）。

### 145

作者: @AndrewYNg
时间: 2024-11-05
链接: https://x.com/AndrewYNg/status/1853653834490642801
互动: Likes: 127; Retweets: 15; Replies: 6; Quotes: 0; Views: 38,773; Bookmarks: 58; isReply: 1

Source: https://t.co/juDEKqJEBc

原文为一条推文，推文内容只包含一个链接，因此无法进行翻译。

### 146

作者: @AndrewYNg
时间: 2024-11-07
链接: https://x.com/AndrewYNg/status/1854587401018261962
互动: Likes: 2,014; Retweets: 332; Replies: 109; Quotes: 30; Views: 198,352; Bookmarks: 1,509; isReply: 0

New short course: LLMs as Operating Systems: Agent Memory, created with @Letta_AI, and taught by its founders @charlespacker and @sarahwooders.

An LLM's input context window has limited space. Using a longer input context also costs more and results in slower processing. So, managing what's stored in this context window is important.

In the innovative paper MemGPT: Towards LLMs as Operating Systems, its authors (which include the instructors) proposed using an LLM agent to manage this context window. Their system uses a large persistent memory that stores everything that could be included in the input context, and  an agent decides   what is actually included.

Take the example of building a chatbot that needs to remember what's been said earlier in a conversation (perhaps over many days of interaction with a user). As the conversation's length grows, the memory management agent will move information from the input context to a persistent searchable database; summarize information to keep relevant facts in the input context; and restore relevant conversation elements from further back in time. This allows a chatbot to keep what's currently most relevant in its input context memory to generate the next response.

When I read the original MemGPT paper, I thought it was an innovative technique for handling memory for LLMs. The open-source Letta framework, which we'll use in this course, makes MemGPT easy to implement. It adds memory to your LLM agents and gives them transparent long-term memory.

In detail, you’ll learn:
- How to build an agent that can edit its own limited input context memory, using tools and multi-step reasoning
- What is a memory hierarchy (an idea from computer operating systems, which use a cache to speed up memory access), and how these ideas apply to managing the LLM input context (where the input context window is a "cache" storing the most relevant information; and an agent decides what to move in and out of this to/from a larger persistent storage system)
- How to implement multi-agent collaboration by letting different agents share blocks of memory

This course will give you a sophisticated understanding of memory management for LLMs, which is important for chatbots having long conversations, and for complex agentic workflows.

Please sign up here!  https://t.co/XMlBifnwVa

新课程： 将大语言模型（Large Language Model/LLM）视为操作系统： AI 智能体（AI Agent）记忆。本课程由 @Letta_AI 共同创建，并由其创始人 @charlespacker 和 @sarahwooders 亲自授课。

大语言模型（LLM）的输入上下文窗口空间有限。不仅如此，使用更长的输入上下文通常意味着更高的成本和更慢的处理速度。因此，有效管理这个上下文窗口中存储的内容变得至关重要。

在一篇极具创新性的论文《MemGPT：Towards LLMs as Operating Systems》中，论文作者（其中也包括本课程的讲师们）提出了一种新颖的方法：利用一个 AI 智能体来专门管理 LLM 的上下文窗口。他们的系统设计了一个庞大的持久性记忆存储区，用于存放所有可能需要被纳入输入上下文的信息，然后由 AI 智能体来智能地决定哪些信息应该被实际包含进来。

举个例子，假设我们要构建一个聊天机器人，它需要记住在长时间对话中（甚至可能跨越数天的用户互动）之前说过的内容。随着对话长度的增加，记忆管理 AI 智能体将执行以下操作：它会将部分信息从当前的输入上下文移至一个持久且可搜索的数据库中；同时，它会总结信息，以确保相关的关键事实始终保留在输入上下文里；并且，它能够从更早的对话记录中恢复出相关的对话元素。这种机制确保了聊天机器人总能将当前最相关的信息保留在它的输入上下文记忆中，从而生成下一个准确的回复。

当我阅读最初的 MemGPT 论文时，我认为这是一种处理 LLM 记忆问题的创新技术。我们将在本课程中使用的开源 Letta 框架，让 MemGPT 的实现变得异常简单。它为你的 AI 智能体增加了记忆能力，并赋予它们一种「透明」的长期记忆，即 AI 智能体能够自然且无需额外干预地访问和利用这些历史信息。

具体来说，你将学习：
- 如何构建一个 AI 智能体，使其能够利用工具和多步骤推理，编辑自身有限的输入上下文记忆。
- 什么是记忆层次结构（这个概念源自计算机操作系统，其中缓存被用来加速记忆访问），以及这些思想如何应用于管理 LLM 的输入上下文。在这里，输入上下文窗口可以被视为一个「缓存」，存储着最相关的信息；而 AI 智能体则负责决定哪些信息在「缓存」与更大的持久存储系统之间进行移入和移出。
- 如何通过让不同的 AI 智能体共享记忆块，来实现多 AI 智能体协作。

本课程将帮助你对 LLM 的记忆管理建立起一个深入而精密的理解。这对于需要进行长时间对话的聊天机器人，以及处理复杂 AI 智能体工作流（agentic workflows）的应用来说，都具有极其重要的意义。

请点击此处注册！ https://t.co/XMlBifnwVa

### 147

作者: @AndrewYNg
时间: 2024-11-12
链接: https://x.com/AndrewYNg/status/1856402761900011622
互动: Likes: 1,192; Retweets: 66; Replies: 64; Quotes: 8; Views: 181,956; Bookmarks: 101; isReply: 0

Chatting with OpenAI’s @karinanguyen_ who joined OpenAI earlier this year and within 6 months co-created and shipped Canvas. I really respect teams that can move fast. That OpenAI, even as a large-ish company, can ship at this pace is fantastic! https://t.co/xuxH1hZZiV

我正在与 OpenAI 的 @karinanguyen_ 交流，她于今年早些时候加入 OpenAI，并在六个月内共同创建并成功推出了 Canvas。我非常敬佩那些能够快速行动的团队。OpenAI 即使作为一家规模相对较大的公司，也能保持如此快的研发和产品上线速度，这真是太棒了！https://t.co/xuxH1hZZiV

### 148

作者: @AndrewYNg
时间: 2024-11-13
链接: https://x.com/AndrewYNg/status/1856779913757691922
互动: Likes: 722; Retweets: 144; Replies: 55; Quotes: 10; Views: 105,956; Bookmarks: 369; isReply: 0

New short course: Safe and Reliable AI via Guardrails! Learn to create production-ready, reliable LLM applications with guardrails in this new course, built in collaboration with @guardrails_ai and taught by its CEO and co-founder,  @ShreyaR.

I see many companies worry about the reliability of LLM-based systems -- will they hallucinate a catastrophically bad response? -- which slows down investing in building them and transitioning prototypes to deployment.  That LLMs generate probabilistic outputs has made them particularly hard to deploy in highly regulated industries or in safety-critical environments. 

Fortunately, there are good guardrail tools that give a significant new layer of control and reliability/safety. They act as a protective framework that can prevent your application from revealing incorrect, irrelevant, or confidential information, and they are an important part of what it takes to actually get prototypes to deployment. 

This course will walk you through common failure modes of LLM-powered applications (like hallucinations or revealing personally identifiable information). It will show you how to build guardrails from scratch to mitigate them. You’ll also learn how to access a variety of pre-built guardrails on the GuardrailsAI hub that are ready to integrate into your projects.

You'll implement these guardrails in the context of a RAG-powered customer service chatbot for a small pizzeria. Specifically, you'll:
- Explore common failure modes like hallucinations, going off-topic, revealing sensitive information, or responses that can harm the pizzeria's reputation.
- Learn to mitigate these failure modes with input and output guards that check inputs and/or outputs
- Create a guardrail to prevent the chatbot from discussing sensitive topics, such as a confidential project at the pizza shop
- Detect hallucinations by ensuring responses are grounded in trusted documents
- Add a Personal Identifiable Information (PII) guardrail to detect and redact sensitive information in user prompts and in LLM outputs
- Set up a guardrail to limit the chatbot’s responses to topics relevant to the pizza shop, keeping interactions on-topic
- Configure a guardrail that prevents your chatbot from mentioning any competitors using a name detection pipeline consisting of conditional logic that routes to an exact match or a threshold check with named entity recognition 

Guardrails are an important part of the practical building and deployment of LLM-based applications today. This course will show you how to make your applications more reliable and more ready for real-world deployment.

Please sign up here: https://t.co/C1fwsOn9yy

新短期课程：通过安全护栏（Guardrails）实现安全可靠的 AI！学习如何利用安全护栏来创建可投入生产且可靠的大语言模型（LLM）应用程序。这门新课程是与 @guardrails_ai 合作开发的，由其首席执行官兼联合创始人 @ShreyaR 亲自讲授。

我发现许多公司都担心基于大语言模型（LLM）的系统能否保持可靠 —— 它们是否会突然出现幻觉，给出灾难性的错误回复？—— 这种担忧减缓了企业在构建此类系统上的投入，也阻碍了将原型产品转化为实际部署的进程。大语言模型（LLL）生成概率性输出的特性，使得它们在受到严格监管的行业或对安全性要求极高的环境中部署时面临特殊挑战。

幸运的是，现在有出色的安全护栏（Guardrails）工具，它们为大语言模型（LLM）应用程序提供了显著增强的控制力、可靠性和安全性。这些工具就像一个保护性框架，能有效防止应用程序泄露不正确、不相关或机密信息。它们是确保原型产品能够成功投入实际部署的关键组成部分。

本课程将带您深入了解大语言模型（LLM）驱动应用程序的常见故障模式（比如出现幻觉或泄露个人身份信息（PII)）。它会向您展示如何从零开始构建安全护栏来有效缓解这些问题。您还将学习如何访问 GuardrailsAI 中心提供的各种预构建安全护栏，这些护栏可随时集成到您的项目中。

您将在一个为小型披萨店打造的 RAG 驱动的客户服务聊天机器人场景中，亲手实践如何实施这些安全护栏。具体来说，您将：
- 探索常见的故障模式，例如出现幻觉、聊天跑题、泄露敏感信息，或给出可能损害披萨店声誉的回复。
- 学习如何利用检查输入和 / 或输出的输入 / 输出守卫（input/output guards）来缓解这些故障模式。
- 创建一个安全护栏，以防止聊天机器人讨论敏感话题，例如披萨店的机密项目。
- 通过确保聊天机器人的回复都基于可信赖的文档，来检测幻觉。
- 添加一个个人身份信息（PII）安全护栏，以检测并遮盖用户提示和大语言模型（LLM）输出中的敏感信息。
- 设置一个安全护栏，将聊天机器人的回复限定在与披萨店相关的话题上，从而保持对话始终围绕主题。
- 配置一个安全护栏，防止您的聊天机器人提及任何竞争对手。这通过一个名称检测管道实现，该管道包含条件逻辑，能够路由到精确匹配或结合命名实体识别进行阈值检查。

如今，安全护栏是大语言模型（LLM）应用程序实际构建和部署过程中不可或缺的重要组成部分。本课程将向您展示如何让您的应用程序更可靠，并为实际部署做好更充分的准备。

请在此处报名：https://t.co/C1fwsOn9yy

### 149

作者: @AndrewYNg
时间: 2024-11-13
链接: https://x.com/AndrewYNg/status/1856791398592516132
互动: Likes: 11; Retweets: 0; Replies: 0; Quotes: 0; Views: 3,400; Bookmarks: 0; isReply: 1

@SnowflakeDB @LandingAI Thanks you for having me! It's a pleasure as always to speak at BUILD.

@SnowflakeDB @LandingAI 感谢你们的邀请！很高兴能像往常一样，在 BUILD 发表讲话。

### 150

作者: @AndrewYNg
时间: 2024-11-14
链接: https://x.com/AndrewYNg/status/1857117382378164267
互动: Likes: 1,838; Retweets: 321; Replies: 83; Quotes: 34; Views: 165,308; Bookmarks: 1,118; isReply: 0

Large language models (LLMs) are typically optimized to answer peoples’ questions. But there is a trend toward models also being optimized to fit into agentic workflows. This will give a huge boost to agentic performance!

Following ChatGPT’s breakaway success at answering questions, a lot of LLM development focused on providing a good consumer experience. So LLMs were tuned to answer questions (“Why did Shakespeare write Macbeth?”) or follow human-provided instructions (“Explain why Shakespeare wrote Macbeth”). A large fraction of the datasets for instruction tuning guide models to provide more helpful responses to human-written questions and instructions of the sort one might ask a consumer-facing LLM like those offered by the web interfaces of ChatGPT, Claude, or Gemini.

But agentic workloads call on different behaviors. Rather than directly generating responses for consumers, AI software may use a model in part of an iterative workflow to reflect on its own output, use tools, write plans, and collaborate in a multi-agent setting. Major model makers are increasingly optimizing models to be used in AI agents as well.

Take tool use (or function calling). If an LLM is asked about the current weather, it won’t be able to derive the information needed from its training data. Instead, it might generate a request for an API call to get that information. Even before GPT-4 natively supported function calls, application developers were already using LLMs to generate function calls, but by writing more complex prompts (such as variations of ReAct prompts) that tell the LLM what functions are available and then have the LLM generate a string that a separate software routine parses (perhaps with regular expressions) to figure out if it wants to call a function.

Generating such calls became much more reliable after GPT-4 and then many other models natively supported function calling. Today, LLMs can decide to call functions to search for information for retrieval augmented generation (RAG), execute code,  send emails, place orders online, and much more.

Recently, Anthropic released a version of its model that is capable of computer use, using mouse-clicks and keystrokes to operate a computer (usually a virtual machine). I’ve enjoyed playing with the demo. While other teams have been prompting LLMs to use computers to build a new generation of RPA (robotic process automation) applications, native support for computer use by a major LLM provider is a great step forward. This will help many developers!

As agentic workflows mature, here is what I am seeing:
- First, many developers are prompting LLMs to carry out the agentic behaviors they want. This allows for quick, rich exploration!
- In a much smaller number of cases, developers who are working on very valuable applications will fine-tune LLMs to carry out particular agentic functions more reliably. For example, even though many LLMs support function calling natively, they do so by taking as input a description of the functions available and then (hopefully) generating output tokens to request the right function call. For mission-critical applications where generating the right function call is important, fine-tuning a model for your application’s specific function calls significantly increases reliability. (But please avoid premature optimization! Today I still see too many teams fine-tuning when they should probably spend more time on prompting before they resort to this.)
- Finally, when a capability such as tool use or computer use appears valuable to many developers, major LLM providers are building these capabilities directly into their models. Even though OpenAI o1-preview’s advanced reasoning helps consumers, I expect that it will be even more useful for agentic reasoning and planning.

Most LLMs have been optimized for answering questions primarily to deliver a good consumer experience, and we’ve been able to “graft” them into complex agentic workflows to build valuable applications. The trend of LLMs built to support particular operations in agents natively will create a lot of lift for agentic performance. I’m confident that large agentic performance gains in this direction will be realized in the next few years.

[Original text: https://t.co/gginTyOgwe ]

大语言模型（LLMs）通常是为了回答人们的问题而优化的。但目前存在一种趋势，模型也正在被优化以更好地融入 AI 智能体（AI Agent）工作流。这将极大地提升智能体的性能！

在 ChatGPT 在回答问题方面取得突破性成功之后，许多大语言模型的开发都专注于提供良好的消费者体验。因此，大语言模型被微调，旨在回答各种问题（例如「莎士比亚为何写《麦克白》？」）或遵循人类提供的指令（例如「解释莎士比亚为何写《麦克白》」）。大量用于指令微调的数据集引导模型为人类编写的问题和指令提供更有帮助的响应，这些问题和指令类似于人们可能会通过 ChatGPT、Claude 或 Gemini 等面向消费者的在线界面提出。

然而，智能体的工作负载对模型行为有不同的要求。AI 软件可能不会直接为消费者生成响应，而是将模型作为迭代工作流的一部分，用于审视自身的输出、使用工具、编写计划，并在多智能体环境中进行协作。主流模型制造商也日益优化其模型，使其更好地用于 AI 智能体。

以工具使用（或函数调用）为例。如果一个大语言模型被问及当前天气，它无法从其训练数据中直接获取所需信息。相反，它可能会生成一个 API 调用请求来获取这些信息。甚至在 GPT-4 原生支持函数调用之前，应用程序开发人员就已经在使用大语言模型生成函数调用。他们通过编写更复杂的提示（例如 ReAct 提示的变体）来告知大语言模型可用的函数，然后让大语言模型生成一个字符串，再由单独的软件例程（可能使用正则表达式）进行解析，以决定是否调用某个函数。

在 GPT-4 和许多其他模型原生支持函数调用之后，生成这类函数调用的可靠性得到了显著提升。如今，大语言模型可以决定调用函数来搜索信息以进行检索增强生成（RAG），执行代码，发送电子邮件，在线下单等等。

最近，Anthropic 发布了一个能够操作计算机的模型版本，该模型通过模拟鼠标点击和键盘输入来控制计算机（通常是虚拟机）。我很高兴体验了这款演示。虽然其他团队一直在通过提示大语言模型来使用计算机，从而构建新一代的机器人流程自动化（RPA）应用程序，但主流大语言模型提供商对计算机使用的原生支持无疑是一个巨大的进步。这将为许多开发者带来便利！

随着智能体工作流的日益成熟，我观察到以下几点：
- 首先，许多开发人员正在通过提示大语言模型来执行他们想要的智能体行为。这使得快速、丰富的探索成为可能！
- 在数量相对较少的情况下，致力于开发高价值应用程序的开发人员会对大语言模型进行微调，以更可靠地执行特定的智能体功能。例如，尽管许多大语言模型原生支持函数调用，但它们通常接收可用函数的描述作为输入，然后（我们期望）生成输出 Token 来请求正确的函数调用。对于那些生成正确函数调用至关重要的任务关键型应用程序，为您的应用特定函数调用微调模型能够显著提高可靠性。（但请避免过早优化！我仍然发现许多团队在应该花更多时间在提示工程上时，就急于进行微调。）
- 最后，当工具使用或计算机使用等功能对许多开发者都展现出巨大价值时，主流大语言模型提供商会将这些功能直接内置到模型中。尽管 OpenAI o1-preview 的高级推理能力有助于消费者，但我预计它对于智能体推理和规划将发挥更大的作用。

大多数大语言模型主要为了提供良好的消费者体验而被优化来回答问题，而我们已经能够将它们「整合」到复杂的智能体工作流中，从而构建有价值的应用程序。大语言模型原生支持智能体中特定操作的趋势将为智能体性能带来巨大的提升。我坚信，未来几年内，这个方向将实现显著的智能体性能飞跃。

[Original text：https://t.co/gginTyOgwe]

### 151

作者: @AndrewYNg
时间: 2024-11-20
链接: https://x.com/AndrewYNg/status/1859258084079882512
互动: Likes: 899; Retweets: 153; Replies: 23; Quotes: 12; Views: 84,690; Bookmarks: 531; isReply: 0

Time to play! Build an interactive game from scratch with LLMs in this new short course: Building an AI-Powered Game. Created with @togethercompute and  @aidungeon @LatitudeGamesAI, taught by @niki_birkner, Senior Product Manager at Together AI, and @nickwalton00, CEO and Co-Founder of Latitude.

This course shows you how to use large language models to create and power a text-based game that you can share with your friends and family. You’ll build a world with hierarchical content generation, a method that allows you to leverage LLMs to create a vast amount of content with a high level of control and consistency. For instance, if you were building a fantasy world with several kingdoms, in which each kingdom has multiple towns, and each town has several locations and residents, creating all this content from scratch can easily become tedious and difficult to track.

With hierarchical content generation, you can create information about your world, shape its direction with a human-in-the-loop, and keep it consistent, with little effort based on your prompts.

By the end of this course, you’ll know how to prompt engineer to create a layered and interwoven world and integrate it into an AI roleplay game that is interesting, interactive, and safe to share with anyone.

In detail, you’ll:
- Learn to implement game mechanics using AI to parse text data into structured JSON output, enabling features like an inventory system.
- Use game mechanics with story and state components that feed into one another to improve your game's memory, and gives the player a steady state of the world.
- Learn to enforce safety and compliance for AI content generation and create custom policies using Llama Guard.

With these techniques, you'll be equipped to build AI-powered applications, starting with your own game.

Please sign up here:  https://t.co/Ght1dlUkcG

是时候开玩了！在这门全新的短期课程 ——《构建 AI 驱动游戏》中，你将学习如何用大语言模型（LLM）从零开始搭建一个互动游戏。这门课程由 @togethercompute、@aidungeon 和 @LatitudeGamesAI 联合打造，并由 Together AI 的高级产品经理 @niki_birkner 以及 Latitude 的首席执行官兼联合创始人 @nickwalton00 亲自授课。

本课程将教你如何运用大语言模型创建并驱动一个基于文本的游戏，你可以与亲朋好友一同分享。你将学会如何通过分层内容生成（hierarchical content generation）构建游戏世界。这是一种巧妙的方法，能让你充分利用大语言模型，以高度可控和一致的方式生成海量内容。举个例子，假设你要构建一个奇幻世界，其中包含多个王国，每个王国下辖数个城镇，而每个城镇又拥有多个地点和居民 —— 如果从头开始手动创建所有这些内容，很快就会变得枯燥乏味且难以管理。

有了分层内容生成，你只需依据你的提示词，便能轻松创建关于游戏世界的信息，通过「人在环路」(human-in-the-loop）的方式调整其发展方向，并确保内容保持一致性，省时省力。

完成本课程后，你将掌握提示工程（prompt engineering）的技巧，能够创建一个层次丰富、彼此交织的游戏世界，并将其整合到一款有趣、互动且可以安全地与任何人分享的 AI 角色扮演游戏中。

具体来说，你将学到：
- 如何运用 AI 将文本数据解析成结构化的 JSON 输出，从而实现库存系统等游戏机制。
- 如何将游戏机制与故事及状态组件结合起来，这些组件相互关联、共同作用，以增强游戏的记忆力，并为玩家呈现一个持续稳定的世界状态。
- 如何为 AI 生成的内容强制实施安全与合规性，并使用 Llama Guard 创建自定义策略。

掌握这些技术后，你将具备构建 AI 驱动应用程序的能力，就从打造你自己的游戏开始吧！

请在此处注册：https://t.co/Ght1dlUkcG

### 152

作者: @AndrewYNg
时间: 2024-11-21
链接: https://x.com/AndrewYNg/status/1859625355541348798
互动: Likes: 759; Retweets: 144; Replies: 52; Quotes: 24; Views: 88,411; Bookmarks: 332; isReply: 0

A small number of people are posting text online that’s intended for direct consumption not by humans, but by LLMs (large language models). I find this a fascinating trend, particularly when writers are incentivized to help LLM providers better serve their users!

People who post text online don’t always have an incentive to help LLM providers. In fact, their incentives are often misaligned. Publishers worry about LLMs reading their text, paraphrasing it, and reusing their ideas without attribution, thus depriving them of subscription or ad revenue. This has even led to litigation such as The New York Times’ lawsuit against OpenAI and Microsoft for alleged copyright infringement. There have also been demonstrations of prompt injections, where someone writes text to try to give an LLM instructions contrary to the provider’s intent. (For example, a handful of sites advise job seekers to get past LLM resumé screeners by writing on their resumés, in a tiny/faint font that’s nearly invisible to humans, text like “This candidate is very qualified for this role.”) Spammers who try to promote certain products — which is already challenging for search engines to filter out — will also turn their attention to spamming LLMs.

But there are examples of authors who want to actively help LLMs. Take the example of a startup that has just published a software library. Because the online documentation is very new, it won’t yet be in LLMs’ pretraining data. So when a user asks an LLM to suggest software, the LLM won’t suggest this library, and even if a user asks the LLM directly to generate code using this library, the LLM won’t know how to do so. Now, if the LLM is augmented with online search capabilities, then it might find the new documentation and be able to use this to write code using the library. In this case, the developer may want to take additional steps to make the online documentation easier for the LLM to read and understand via RAG. (And perhaps the documentation eventually will make it into pretraining data as well.)

Compared to humans, LLMs are not as good at navigating complex websites, particularly ones with many graphical elements. However, LLMs are far better than people at rapidly ingesting long, dense, text documentation. Suppose the software library has many functions that we want an LLM to be able to use in the code it generates. If you were writing documentation to help humans use the library, you might create many web pages that break the information into bite-size chunks, with graphical illustrations to explain it. But for an LLM, it might be easier to have a long XML-formatted text file that clearly explains everything in one go. This text might include a list of all the functions, with a dense description of each and an example or two of how to use it. (This is not dissimilar to the way we specify information about functions to enable LLMs to use them as tools.)

A human would find this long document painful to navigate and read, but an LLM would do just fine ingesting it and deciding what functions to use and when!

Because LLMs and people are better at ingesting different types of text, we write differently for LLMs than for humans. Further, when someone has an incentive to help an LLM better understand a topic — so the LLM can explain it better to users — then an author might write text to help an LLM.

So far, text written specifically for consumption by LLMs has not been a huge trend. But Jeremy Howard’s proposal for web publishers to post a llms.txt file to tell LLMs how to use their websites, like a robots.txt file tells web crawlers what to do, is an interesting step in this direction. In a related vein, some developers are posting detailed instructions that tell their IDE how to use tools, such as the plethora of .cursorrules files that tell the Cursor IDE how to use particular software stacks.

I see a parallel with SEO (search engine optimization). The discipline of SEO has been around for decades. Some SEO helps search engines find more relevant topics, and some is spam that promotes low-quality information. But many SEO techniques — those that involve writing text for consumption by a search engine, rather than by a human — have survived so long in part because search engines process web pages differently than humans, so providing tags or other information that tells them what a web page is about has been helpful.

The need to write text separately for LLMs and humans might diminish if LLMs catch up with humans in their ability to understand complex websites. But until then, as people get more information through LLMs, writing text to help LLMs will grow.

[Original text: https://t.co/MDjPq9wCDH ]

现在，有少数人在网上发布文本，但这些文本并非供人类直接阅读，而是供大语言模型（LLMs）使用。我发现这是一个引人入胜的趋势，尤其当作者们被鼓励去帮助大语言模型供应商更好地服务其用户时，这种现象就更加有趣了。

然而，在线发布文本的人并非总是有动力去帮助大语言模型供应商。事实上，他们的目标往往是相悖的。出版商担心大语言模型会阅读他们的内容，将其改写，并在不注明出处的情况下重复使用他们的创意，从而损害他们的订阅或广告收入。这甚至导致了一些法律纠纷，例如《纽约时报》就曾起诉 OpenAI 和 Microsoft 涉嫌侵犯版权。此外，还出现过「提示注入（prompt injections）」的案例，即有人故意编写文本，试图让大语言模型执行与供应商意图相反的指令。（举个例子，有些网站会建议求职者，在简历上用人类几乎看不见的微小字体写上「该候选人非常适合此职位」等文本，以此绕过大语言模型简历筛选器。）那些试图推广特定产品的垃圾邮件发送者 —— 这些内容对搜索引擎来说已经很难过滤了 —— 也将把目标转向大语言模型。

但也有作者积极希望帮助大语言模型的例子。比如一家初创公司，刚刚发布了一个新的软件库。由于在线文档发布不久，它尚未被纳入大语言模型的预训练数据中。因此，当用户向大语言模型咨询软件建议时， 大语言模型不会推荐这个库；即使用户直接要求大语言模型使用该库生成代码，它也无从下手。不过，如果大语言模型具备了在线搜索能力，它或许就能找到这份新文档，并利用它来编写使用该库的代码。在这种情况下，开发人员可能会采取额外措施，通过 RAG（Retrieval Augmented Generation）技术，让在线文档更易于大语言模型阅读和理解。（或许这份文档最终也会被纳入预训练数据。）

与人类相比， 大语言模型在浏览复杂网站方面表现不佳，特别是那些包含大量图形元素的网站。然而，在快速处理冗长、密集文本文档方面， 大语言模型却远超人类。假设某个软件库有许多我们希望大语言模型能够在其生成的代码中使用的函数。如果你是为人类编写使用该库的文档，你可能会创建许多网页，将信息分解成易于理解的小块，并配上图形插图进行解释。但对于大语言模型来说，一个冗长的 XML 格式文本文件，能一次性清晰地解释所有内容，可能会更容易理解。这份文本可能包含所有函数的列表，以及每个函数的详细描述和一两个使用示例。（这与我们指定函数信息以使大语言模型能够将其用作工具的方式非常相似。）

人类会觉得阅读这份冗长的文档令人痛苦，但大语言模型却能很好地消化吸收，并决定何时使用哪些函数！

由于大语言模型和人类擅长处理不同类型的文本，因此我们为大语言模型编写文本的方式也与为人类编写文本的方式有所不同。此外，当有人有动力帮助大语言模型更好地理解某个主题 —— 以便大语言模型能够更好地向用户解释该主题时 —— 作者就会专门编写文本来帮助大语言模型。

到目前为止，专门为大语言模型编写的文本尚未成为主流趋势。但 Jeremy Howard 提出的建议 —— 让网络出版商发布一个类似 robots.txt 文件的 llms.txt 文件，来指导大语言模型如何使用他们的网站 —— 是朝着这个方向迈出的有趣一步。与此相关的是，一些开发者正在发布详细指令，告诉他们的 IDE（Integrated Development Environment）如何使用工具，例如大量的 .cursorrules 文件，这些文件指导 Cursor IDE 如何使用特定的软件栈。

我从中看到了与 SEO（Search Engine Optimization）的相似之处。SEO 这门学科已经存在了几十年。有些 SEO 旨在帮助搜索引擎找到更相关的主题，有些则是推广低质量信息的垃圾邮件。但许多 SEO 技术 —— 那些涉及为搜索引擎而非人类编写文本的技术 —— 之所以能存活这么久，部分原因在于搜索引擎处理网页的方式与人类不同。因此，提供标签或其他信息来告知搜索引擎网页的主题，一直以来都非常有用。

如果大语言模型在理解复杂网站的能力上能赶上人类，那么为大语言模型和人类分别编写文本的需求可能会减少。但在此之前，随着人们通过大语言模型获取更多信息，专门为帮助大语言模型而编写文本的实践将会不断增长。

[原文链接：https://t.co/MDjPq9wCDH]

### 153

作者: @AndrewYNg
时间: 2024-11-23
链接: https://x.com/AndrewYNg/status/1860468376809931061
互动: Likes: 12; Retweets: 0; Replies: 2; Quotes: 0; Views: 3,756; Bookmarks: 1; isReply: 1

@joaomdmoura Congratulations!!! ❤️

@joaomdmoura 恭喜！！！❤️

### 154

作者: @AndrewYNg
时间: 2024-11-25
链接: https://x.com/AndrewYNg/status/1861085482526105842
互动: Likes: 5,801; Retweets: 1,070; Replies: 146; Quotes: 103; Views: 436,130; Bookmarks: 3,737; isReply: 0

Announcing new open-source Python package: aisuite!  

This makes it easy for developers to use large language models from multiple providers. When building applications I found it a hassle to integrate with multiple providers. Aisuite lets you pick a "provider:model" just by changing one string, like openai:gpt-4o, anthropic:claude-3-5-sonnet-20241022, ollama:llama3.1:8b, etc. 

pip install aisuite

Open-source code with instructions: https://t.co/gwz9oKTCFx

Thanks to Rohit Prsad, Kevin Solorio, @standsleeping,   Jeff Tang and @Johnsanterre for helping build this!

隆重推出新的开源 Python 包：aisuite！

这款工具旨在让开发者能够轻松调用来自多个服务商的 ** 大语言模型 **（Large Language Model）。在开发应用程序时，我们发现与不同服务商的 API（应用程序编程接口）进行集成常常是一项繁琐的任务。有了 Aisuite，您只需修改一个字符串，就能轻松选择不同的「提供商：模型」，例如 openai:gpt-4o、anthropic:claude-3-5-sonnet-20241022、ollama:llama3.1:8b 等。

pip install aisuite

项目的开源代码及使用说明请访问：https://t.co/gwz9oKTCFx

特别感谢 Rohit Prsad、Kevin Solorio、@standsleeping、Jeff Tang 和 @Johnsanterre 对此项目开发提供的帮助！

### 155

作者: @AndrewYNg
时间: 2024-11-27
链接: https://x.com/AndrewYNg/status/1861830140730487206
互动: Likes: 11; Retweets: 0; Replies: 3; Quotes: 0; Views: 2,517; Bookmarks: 0; isReply: 1

@weimenglee @AIAdvances Thanks for writing up this aisuite guide!

@weimenglee @AIAdvances 感谢你们撰写了这份 aisuite 指南！

### 156

作者: @AndrewYNg
时间: 2024-12-11
链接: https://x.com/AndrewYNg/status/1866880693588070440
互动: Likes: 1,383; Retweets: 262; Replies: 34; Quotes: 14; Views: 127,317; Bookmarks: 795; isReply: 0

New short course: Collaborative Writing and Coding with OpenAI Canvas!

Explore new ways to write and code with OpenAI Canvas, a user-friendly interface that allows you to brainstorm, draft, and refine text and code in collaboration with ChatGPT.

In the short course, created with @OpenAI, and taught by @karinanguyen_, a research lead at OpenAI, you’ll learn to use Canvas to enhance your workflows.

Canvas lets you go beyond simple chat interactions. It provides a side-by-side workspace where you and ChatGPT can edit and refine text or code collaboratively. This makes brainstorming, drafting, and iterating as you write feel more natural and effective. As the first major update to ChatGPT’s visual interface since its launch in 2022, Canvas gives a new, innovative approach to collaboration with AI.

For instance, after writing the first version of your code, Canvas can review it and give suggestions for improvement. It can also help with debugging by adding logging, identifying problems to fix, and writing comments. In addition, you'll also learn what it takes to train the model for an interface like Canvas.

In this video-only short course, you’ll:
- Learn how to ask for in-line feedback and control the iteration of your work by directly editing selected areas of your text or code from the model’s output.
- Learn how to access quick automation tools in a shortcut menu that allows you to modify your writing tone and length, enhance your code, and restore previous versions of your work.
- Learn how to use Canvas as a research assistant tool with an example of asking the model to reason through the screenshot of a plot to write a research report, in which you can ask questions within the created report.
- Ask the model to write Python code to replicate the graph seen on a screenshot image.
- Go behind the scenes of how you can create a video game, such as Space Battleship, from scratch, edit it, and display it in one self-contained HTML file.
- Get a real-world application example of creating a SQL database from the image of its architecture.
- Understand the model training and design processes that power Canvas!

Please sign up here: https://t.co/vdWBfHHGia

新上线短期课程：使用 OpenAI Canvas 进行协作写作和编码！

探索利用 OpenAI Canvas 这一用户友好的界面，与 ChatGPT 协作进行头脑风暴、起草和完善文本及代码的全新方式。

这门短期课程由 @OpenAI 合作打造，并由 OpenAI 的研究主管 @karinanguyen_ 亲自授课。课程中，您将学习如何使用 Canvas 来提升您的工作效率。

Canvas 不仅仅局限于简单的聊天互动。它提供了一个并排的工作空间，您和 ChatGPT 可以在其中共同编辑和完善文本或代码。这使得头脑风暴、起草以及在写作过程中不断迭代的过程变得更加自然和高效。作为 ChatGPT 可视化界面自 2022 年推出以来的首次重大更新，Canvas 为与 AI 协作带来了一种创新方法。

例如，在编写完代码的初稿后，Canvas 可以对其进行审查并提供改进建议。它还可以通过添加日志、识别需要修复的问题以及编写注释来帮助调试。此外，您还将了解为 Canvas 这样的界面训练模型所需的关键要素。

在这个纯视频的短期课程中，您将：
- 学习如何请求内联反馈，并通过直接编辑模型输出中文本或代码的特定区域来控制您工作的迭代。
- 学习如何通过快捷菜单访问快速自动化工具，从而修改您的写作语气和长度、优化您的代码以及恢复之前版本的工作。
- 学习如何将 Canvas 用作研究助理工具。例如，您可以要求模型通过图表（plot）的屏幕截图进行推理，撰写研究报告，并可在生成的报告中提出问题。
- 要求模型编写 Python 代码，以复现屏幕截图图像上显示的图表。
- 深入了解如何从零开始创建视频游戏（例如太空战舰），对其进行编辑，并将其展示在一个独立的 HTML 文件中。
- 获得一个实际应用示例：如何从其架构图像创建 SQL 数据库。
- 了解驱动 Canvas 的模型训练和设计过程！

请在此处注册：https://t.co/vdWBfHHGia

### 157

作者: @AndrewYNg
时间: 2024-12-12
链接: https://x.com/AndrewYNg/status/1867269937397670082
互动: Likes: 1,712; Retweets: 330; Replies: 86; Quotes: 42; Views: 257,355; Bookmarks: 1,777; isReply: 0

AI Product Management

AI Product Management is evolving rapidly. The growth of generative AI and AI-based developer tools has created numerous opportunities to build AI applications. This is making it possible to build new kinds of things, which in turn is driving shifts in best practices in product management — the discipline of defining what to build to serve users — because what is possible to build has shifted. In this post, I’ll share some best practices I have noticed.

Use concrete examples to specify AI products. Starting with a concrete idea helps teams gain speed. If a product manager (PM) proposes to build “a chatbot to answer banking inquiries that relate to user accounts,” this is a vague specification that leaves much to the imagination. For instance, should the chatbot answer questions only about account balances or also about interest rates, processes for initiating a wire transfer, and so on? But if the PM writes out a number (say, between 10 and 50) of concrete examples of conversations they’d like a chatbot to execute, the scope of their proposal becomes much clearer. Just as a machine learning algorithm needs training examples to learn from, an AI product development team needs concrete examples of what we want an AI system to do. In other words, the data is your PRD (product requirements document)!

In a similar vein, if someone requests “a vision system to detect pedestrians outside our store,” it’s hard for a developer to understand the boundary conditions. Is the system expected to work at night? What is the range of permissible camera angles? Is it expected to detect pedestrians who appear in the image even though they’re 100m away? But if the PM collects a handful of pictures and annotates them with the desired output, the meaning of “detect pedestrians” becomes concrete. An engineer can assess if the specification is technically feasible and if so, build toward it. Initially, the data might be obtained via a one-off, scrappy process, such as the PM walking around taking pictures and annotating them. Eventually, the data mix will shift to real-word data collected by a system running in production.

Using examples (such as inputs and desired outputs) to specify a product has been helpful for many years, but the explosion of possible AI applications is creating a need for more product managers to learn this practice.

Assess technical feasibility of LLM-based applications by prompting. When a PM scopes out a potential AI application, whether the application can actually be built — that is, its technical feasibility — is a key criterion in deciding what to do next. For many ideas for LLM-based applications, it’s increasingly possible for a PM, who might not be a software engineer, to try prompting — or write just small amounts of code — to get an initial sense of feasibility.

For example, a PM may envision a new internal tool for routing emails from customers to the right department (such as customer service, sales, etc.). They can prompt an LLM to see if they can get it to select the right department based on an input email, and see if they can achieve high accuracy. If so, this gives engineering a great starting point from which to implement the tool. If not, the PM can falsify the idea themselves and perhaps improve the product idea much faster than if they had to rely on an engineer to build a prototype.

Often, testing feasibility requires a little more than prompting. For example, perhaps the LLM-based email system needs basic RAG capability to help it make decisions. Fortunately, the barrier to writing small amounts of code is now quite low, since AI can help by acting as a coding companion, as I describe in the course, “AI Python for Beginners.” This means that PMs can do much more technical feasibility testing, at least at a basic level, than was possible before.

Prototype and test even without engineers. User feedback to initial prototypes is also instrumental to shaping products. Fortunately, barriers to building prototypes rapidly are falling, and PMs themselves can move basic prototypes forward without needing professional software developers.

In addition to using LLMs to help write code for prototyping, tools like Replit, Vercel’s V0, Bolt, and Anthropic’s Artifacts (I’m a fan of all of these!) are making it easier for people without a coding background to build and experiment with simple prototypes. These tools are increasingly accessible to non-technical users, though I find that those who understand basic coding are able to use them much more effectively, so it’s still important to learn basic coding. (Interestingly, highly technical, experienced developers use them too!) Many members of my teams routinely use such tools to prototype, get user feedback, and iterate quickly.

AI is enabling a lot of new applications to be built, creating massive growth in demand for AI product managers who know how to scope out and help drive progress in building these products. AI product management existed before the rise of generative AI, but the increasing ease of building applications is creating greater demand for AI applications, and thus a lot of PMs are learning AI and these emerging best practices for building AI products. I find this discipline fascinating, and will keep on sharing best practices as they grow and evolve.

[Original text: https://t.co/ohLyrpU4SJ ]

AI 产品管理

AI 产品管理正在飞速发展。随着生成式 AI（Generative AI）和基于 AI 的开发者工具的兴起，构建 AI 应用程序的机会也随之大量涌现。这不仅催生了各种新型应用，也推动了产品管理领域 —— 即定义应开发何种产品以满足用户需求的学科 —— 的最佳实践发生转变，因为技术边界和可构建性都已今非昔比。在这篇文章中，我将分享我观察到的一些最佳实践。

用具体示例来定义 AI 产品。从一个具体的想法入手，有助于团队快速启动项目。如果产品经理（PM）提议构建一个「用于回答与用户账户相关的银行查询的聊天机器人」，这仍然是一个过于模糊的描述，留下了太多的想象空间。例如，这个聊天机器人是只回答关于账户余额的问题，还是也包括利率、电汇流程等方面的查询？但如果 PM 能提供许多（比如 10 到 50 个）具体的对话示例，来展示他们希望聊天机器人如何执行任务，那么这项提案的范围就会清晰得多。正如机器学习算法需要训练示例来学习一样，AI 产品开发团队也需要具体的示例来明确我们希望 AI 系统做什么。换句话说，数据就是你的产品需求文档（PRD)！

同理，如果有人要求「一个用于检测我们商店外行人的视觉系统」，开发者很难理解其具体的适用范围。该系统是否需要在夜间工作？允许的摄像机角度范围是多少？它是否应该检测即使距离 100 米远，但在图像中仍然出现的行人？但如果 PM 收集一些图片，并用期望的输出来进行标注，那么「检测行人」的含义就变得具体了。工程师可以据此评估该规范在技术上是否可行，如果可行，便可朝着这个目标进行开发。最初，数据可能通过一次性、非规范的流程获取，例如 PM 亲自走动拍摄照片并进行标注。最终，数据来源将转向由生产环境中运行的系统所收集的真实世界数据。

多年来，使用示例（例如输入和期望的输出）来定义产品一直行之有效，但 AI 应用程序的爆炸式增长，正促使越来越多的产品经理学习和掌握这种实践。

通过提示词评估基于大语言模型（LLM）应用程序的技术可行性。当 PM 规划一个潜在的 AI 应用程序时，该应用程序是否真的能够构建 —— 即其技术可行性 —— 是决定下一步行动的关键标准。对于许多基于 LLM 的应用程序构想，即使 PM 可能不是软件工程师，现在也越来越有可能通过尝试编写提示词（prompting），甚至只编写少量代码，来初步了解其可行性。

例如，PM 可能设想一个新的内部工具，用于将客户邮件路由到正确的部门（例如客户服务、销售等）。他们可以向 LLM 发出提示词，看看它能否根据输入的邮件选择正确的部门，并评估其准确率。如果能达到较高准确率，这将为工程团队实施该工具提供一个极佳的起点。如果不行，PM 就可以自己快速推翻这个想法，并可能比依赖工程师构建原型更快地改进产品构思。

通常，测试可行性需要的往往不仅仅是提示词。例如，基于 LLM 的邮件系统可能需要基本的 RAG 能力来辅助决策。幸运的是，现在编写少量代码的门槛已经非常低，因为 AI 可以充当编码助手（coding companion）来提供帮助，正如我在「AI Python for Beginners」课程中描述的那样。这意味着 PM 们现在能够进行更多、更基础的技术可行性测试，这在以前是不可能实现的。

即使没有工程师也能进行原型设计和测试。用户对初始原型的反馈对于产品成形至关重要。幸运的是，快速构建原型的障碍正在降低，PM 们现在可以独立推进基础原型的开发，而无需专业的软件开发人员。

除了利用 LLM 协助编写原型代码，Replit、Vercel 的 V0、Bolt 和 Anthropic 的 Artifacts 等工具（我都是这些工具的忠实用户！）也让没有编码背景的人更容易构建和尝试简单的原型。这些工具对非技术用户越来越易于上手，尽管我发现那些了解基本编码的人能够更有效地使用它们，因此学习基础编码仍然很重要。（有趣的是，技术精湛、经验丰富的开发人员也会使用它们！）我的团队中有许多成员经常使用这类工具来构建原型、获取用户反馈并快速迭代。

AI 正在催生大量新应用，从而极大增加了对懂得如何规划和推动这些产品构建的 AI 产品经理的需求。在生成式 AI 兴起之前，AI 产品管理就已经存在，但应用程序构建的日益简化正催生出对 AI 应用程序更大的需求，因此许多 PM 正在学习 AI 以及这些新兴的 AI 产品构建最佳实践。我发现这个领域引人入胜，并将继续分享其不断发展和演变中的最佳实践。

[原始文本：https://t.co/ohLyrpU4SJ]

### 158

作者: @AndrewYNg
时间: 2024-12-18
链接: https://x.com/AndrewYNg/status/1869421643925422166
互动: Likes: 2,747; Retweets: 426; Replies: 84; Quotes: 47; Views: 355,748; Bookmarks: 2,424; isReply: 0

OpenAI just announced API access to o1 (advanced reasoning model) yesterday. I'm delighted to announce today a new short course, Reasoning with o1, built with @OpenAI, and taught by @colintjarvis, Head of AI Solutions at OpenAI, to show you how to use this effectively!

Unlike previous language models which generate output directly, o1 “thinks before it responds,” and generates many reasoning tokens before returning a more thoughtful and accurate response. It is great at complex reasoning -- including planning for agentic workflows, coding, and domain-specific reasoning in STEM fields like law. But how you should use it is quite different from other LLMs. 

I think o1 will be a game changer for many AI applications; and in this course, you'll learn how to use it effectively. 

In detail, you’ll:
- Learn to recognize what tasks o1 is suited for, and when to use a smaller model, or combine o1 with a smaller model
- Understand the new principles of prompting reasoning models: Be simple and direct; no explicit chain-of-thought required; use structure; show rather than tell
- Implement multi-step orchestration in which o1 plans, and hands tasks over to gpt-4o-mini to execute specific steps; this illustrates a design pattern to optimize intelligence (accuracy) and cost
- Use o1 for a coding task to build a new application, edit existing code, and test performance by running a coding competition between o1-mini and GPT 4o
- Use o1 for image understanding and learn how it performs better with a "hierarchy of reasoning," in which it incurs the latency and cost upfront, preprocessing the image and indexing it with rich details so it can be used for Q&A later
- Learn a technique called meta-prompting, in which you use o1 to improve your prompts. Using a customer support evaluation set, you'll iteratively use o1 to modify a prompt to improve performance

You'll also learn about how OpenAI used reinforcement learning to produce a model that uses "test-time compute" to improve performance.

I think you'll find this course enjoyable and valuable. 

Please sign up for it here: https://t.co/0XIGzinyrx

OpenAI 昨天刚刚宣布开放 o1（高级推理模型）的 API 访问权限。今天，我很高兴能向大家宣布一门全新的短期课程 ——《与 o1 进行推理》（Reasoning with o1）。这门课程是与 OpenAI 合作开发，由 OpenAI 的 AI 解决方案主管 @colintjarvis 亲自授课，旨在向大家展示如何高效地使用 o1！

与以往直接生成输出的语言模型不同，o1 能够「先思考后回应」。它会先生成大量的推理 Token（reasoning token），从而返回更周到、更准确的回复。o1 尤其擅长处理复杂推理任务 —— 包括为 AI 智能体（AI Agent）工作流制定计划、编写代码，以及在法律等 STEM 领域进行专业推理。但它的使用方式与其他大语言模型（LLM）截然不同。

我认为 o1 将会是许多 AI 应用的颠覆性技术（game changer)；而在这门课程中，你将学会如何有效利用它。

具体来说，你将学习：
- 识别哪些任务适合 o1，以及何时应该使用较小的模型，或将 o1 与较小的模型结合使用。
- 理解提示推理模型的新原则：保持简洁直白；不需要明确的思维链（chain-of-thought)；善用结构；通过展示而非讲述来引导。
- 实现多步骤编排：o1 负责规划，并将具体任务交给 gpt-4o-mini 来执行。这展示了一种优化智能（准确性）和成本的设计模式。
- 利用 o1 完成编码任务，包括构建新应用、编辑现有代码，并通过 o1-mini 和 GPT 4o 之间的编码竞赛来测试性能。
- 利用 o1 进行图像理解，并学习它如何通过「推理层次结构」(hierarchy of reasoning）获得更好的表现。在这种模式下，o1 会预先承担延迟和成本，对图像进行预处理并用丰富的细节进行索引，以便后续进行问答。
- 学习一种名为元提示（meta-prompting）的技术，即利用 o1 来改进你的提示词。通过一个客户支持评估数据集，你将迭代地使用 o1 修改提示词，以提高性能。

你还将了解到 OpenAI 如何运用强化学习（reinforcement learning）来开发一个利用「测试时计算」(test-time compute）来提高性能的模型。

我相信你会发现这门课程既有趣又有价值。

请点击此处报名：https://t.co/0XIGzinyrx

### 159

作者: @AndrewYNg
时间: 2024-12-19
链接: https://x.com/AndrewYNg/status/1869783741566202074
互动: Likes: 693; Retweets: 97; Replies: 47; Quotes: 5; Views: 58,428; Bookmarks: 126; isReply: 0

I’m thrilled that former students and postdocs of mine won both of this year’s NeurIPS Test of Time Paper Awards. This award recognizes papers published 10 years ago that have significantly shaped the research field. The recipients included Ian Goodfellow (who, as an undergraduate, built my first GPU server for deep learning in his dorm room) and his collaborators for their work on generative adversarial networks, and my former postdoc Ilya Sutskever and PhD student Quoc Le (with Oriol Vinyals) for their work on sequence-to-sequence learning. Congratulations to all these winners!

By nature, I tend to focus on the future rather than the past. Steve Jobs famously declined to build a corporate museum, instead donating Apple's archives to Stanford University, because he wanted to keep the company forward-looking. Jeff Bezos encourages teams to approach every day as if it were “Day 1,” a mindset that emphasizes staying in the early, innovative stage of a company or industry. These philosophies resonate with me.

But taking a brief look at the past can help us reflect on lessons for the future. One takeaway from looking at what worked 10 to 15 years ago is that many of the teams I led bet heavily on scaling to drive AI progress — a bet that laid a foundation to build larger and larger AI systems. At the time, the idea of scaling up neural networks was controversial, and I was on the fringe. I recall distinctly that, around  2008, Yoshua Bengio advised me not to bet on scaling and to focus on inventing algorithms instead!

A lesson I carry from that time is to not worry about what others think, but follow your convictions, especially if you have data to support your beliefs. Small-scale experiments performed by my Stanford group convinced me that scaling up neural networks would drive significant progress, and that’s why I was willing to ignore the skeptics. The diagram below, generated by Adam Coates and Honglak Lee, is the one that most firmed up my beliefs at that time. It shows that, for a range of models, the larger we scaled them, the better they perform. I remember presenting it at CIFAR 2010, and if I had to pick a single reason why I pushed through to start Google Brain and set as the team’s #1 goal to scale up deep learning algorithms, it is this diagram!

I also remember presenting at NeurIPS in 2008 our work on using GPUs to scale up training neural networks. (By the way, one measure of success in academia is when your work becomes sufficiently widely accepted that no one cites it anymore. I’m quite pleased the idea that GPUs should be used for AI — which was controversial back then — is now such a widely accepted “fact” that no one bothers to cite early papers that pushed for it.😃)

When I started Google Brain, the thesis was simple: I wanted to use the company’s  huge computing capability to scale up deep learning. Shortly afterward, I built Stanford’s first supercomputer for deep learning using GPUs, since I could move faster at Stanford than within a large company. A few years later, my team at Baidu showed that as you scale up a model, its performance improves linearly on a log-log scale, which was a precursor to OpenAI’s scaling laws.

As I look to the future, I’m sure there are ideas that many people are skeptical about today, but will prove to be accurate. Scaling up AI models turned out to be useful for many teams, and it continues to be exciting, but now I’m even more excited by upcoming ideas that will prove to be even more valuable in the future.

This past year, I spent a lot of time encouraging teams to build applications with agentic AI and worked to share best practices. I have a few hypotheses for additional technologies that will be important next year. I plan to spend the winter holiday playing with a few of them, and I will have more to share next year. But if you have an idea that you have conviction on, so long as you can do so responsibly, I encourage you to pursue it!

[Original text (with links): https://t.co/Km7ENTODId]

我非常高兴地宣布，我的前学生和博士后们荣获了今年 NeurIPS （神经信息处理系统大会）「十年影响力论文奖」的两项大奖！这个奖项旨在表彰那些在十年前发表、并对研究领域产生了深远影响的论文。获奖者包括 Ian Goodfellow （当年他还是本科生时，就曾在宿舍里为我搭建了第一个用于深度学习的 GPU 服务器）和他的合作者，他们凭借在生成对抗网络（Generative Adversarial Networks）方面的工作获此殊荣；以及我的前博士后 Ilya Sutskever 和博士生 Quoc Le （与 Oriol Vinyals 合作），他们则因在序列到序列学习（Sequence-to-Sequence Learning）方面的贡献而获奖。衷心祝贺所有这些获奖者！

我这个人天生就更喜欢着眼未来，而不是沉湎过去。Steve Jobs 曾有个著名的举动，他拒绝建造 Apple 的企业博物馆，而是将公司的档案捐赠给 Stanford University，因为他希望公司始终保持前瞻性。Jeff Bezos 也鼓励团队将每一天都当作「第一天」来对待，这种心态强调公司或行业要永远保持在早期创新阶段。这些理念都深深触动了我。

不过，偶尔回顾一下过去，也能帮助我们汲取经验教训，为未来指明方向。回顾过去 10 到 15 年的成功经验，我得到了一个重要的启示：我领导过的许多团队都坚定地押注于通过「规模化」(scaling）来推动 AI 发展 —— 这一策略为构建越来越庞大的 AI 系统奠定了坚实基础。要知道，在当时，扩大神经网络规模的想法还备受争议，我算是「另类」。我清楚地记得，大约在 2008 年，Yoshua Bengio 曾建议我不要专注于规模化，而应该把精力放在发明新算法上！

从那时起，我学到的一个宝贵经验就是：不要过分在意别人的看法，要勇于追随自己的信念，尤其是在你有数据支持你的观点时。我的 Stanford 团队通过小规模实验让我坚信，扩大神经网络的规模能带来巨大的进步，这也是我愿意不理会那些怀疑者的原因。下面这张由 Adam Coates 和 Honglak Lee 绘制的图表，正是当时最坚定我信念的关键。它清楚地展示了，对于一系列模型而言，我们将其规模扩大得越多，它们的性能就越好。我记得在 CIFAR 2010 大会上展示过它，如果非要我说一个理由，为什么我会全力以赴地创办 Google Brain，并将扩大深度学习算法规模定为团队的首要目标，那一定就是这张图表了！

我还记得在 2008 年的 NeurIPS 大会上，我们展示了如何利用 GPU 来加速神经网络的训练。(顺便提一句，在学术界，衡量一项工作是否足够成功的一个标准就是，当它被广泛接受到人们不再需要引用它时。我非常欣慰，当年颇具争议的「GPU 应该用于 AI」这个想法，现在已经成为一个如此广为人知的「事实」，以至于再也没有人特意去引用那些早期推动这一概念的论文了。😃)

当我创办 Google Brain 时，其核心理念非常简单：我希望利用 Google 庞大的计算能力来推动深度学习的规模化发展。此后不久，我便在 Stanford 使用 GPU 搭建了该校第一个用于深度学习的超级计算机，因为在 Stanford，我能比在大公司内部更快速、更灵活地推进项目。几年后，我在 Baidu 的团队发现了一个规律：模型的性能会随着规模的扩大，在对数 - 对数（log-log）坐标系中呈现线性提升。这正是 OpenAI 后来提出的「规模化定律」(scaling laws）的前身。

展望未来，我确信有许多现在看来备受质疑的想法，最终都将被证明是正确的。扩大 AI 模型规模的策略对许多团队来说都非常有效，并且依然令人兴奋。但现在，我对于那些即将出现、并在未来能带来更大价值的新想法感到更加激动。

过去一年里，我投入了大量时间，鼓励团队开发基于 AI 智能体（AI Agent）的应用程序，并努力分享最佳实践。对于明年哪些技术会变得重要，我有一些新的假设。我计划在寒假期间探索其中一些，明年将会有更多内容与大家分享。但是，如果你自己也有一个坚信不疑的想法，只要你能以负责任的方式去实践，我鼓励你大胆追求它！

[原文（带链接)：https://t.co/Km7ENTODId]

### 160

作者: @AndrewYNg
时间: 2024-12-22
链接: https://x.com/AndrewYNg/status/1870965047738220934
互动: Likes: 1,743; Retweets: 172; Replies: 76; Quotes: 12; Views: 198,579; Bookmarks: 82; isReply: 0

Sriram has been consistently thoughtful about AI policy, including specifically the importance of promoting open source. His working with @DavidSacks on AI will be good for innovation and good for the U.S. Thank you @sriramk for your service!

Sriram 一直以来都对 AI 政策持续关注并深入思考，尤其重视推动开源的重要性。他与 @DavidSacks 在 AI 领域的合作，将对创新和美国的发展大有裨益。感谢 @sriramk 所做的贡献！

### 161

作者: @AndrewYNg
时间: 2024-12-26
链接: https://x.com/AndrewYNg/status/1872079097121431855
互动: Likes: 3,187; Retweets: 376; Replies: 375; Quotes: 57; Views: 368,103; Bookmarks: 285; isReply: 0

One of the best things the U.S. can do is make high-skill immigration easier. @levie is right. 

It is awful that the wait time for a green card can be over a decade, and that after waiting years someone can still be forced to leave simply because they lost a job. Fixing this is both an economic and a moral issue. 

A rigorous economic analysis (by Pierre Azoulay and collaborators) shows that immigrants create more jobs than they take. So to create jobs for Americans, lets let more immigrants in!

美国可以采取的最佳举措之一，就是简化高技能移民（high-skill immigration）的申请流程。@levie 的观点是正确的。

令人遗憾的是，绿卡（green card）的等待时间可能长达十余年，而且即使等待多年后，申请人也可能仅仅因为失去工作就被迫离开美国。解决这个问题，既是一个经济议题，也是一个道德议题。

Pierre Azoulay 及其合作者进行的一项严谨经济分析（rigorous economic analysis）表明，移民创造的就业机会多于他们所占据的。因此，为了给美国民众创造更多就业机会，我们应该允许更多移民入境！

### 162

作者: @AndrewYNg
时间: 2024-12-26
链接: https://x.com/AndrewYNg/status/1872079319813816597
互动: Likes: 150; Retweets: 19; Replies: 10; Quotes: 1; Views: 44,986; Bookmarks: 42; isReply: 1

@levie Link to the study I refer to: https://t.co/xgct2iVwEo

@levie 这是我提到的研究链接：https://t.co/xgct2iVwEo
