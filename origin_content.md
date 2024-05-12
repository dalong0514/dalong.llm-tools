#### Investing in AI Infrastructure

Dwarkesh: I want to go back in time to 2022, when you started acquiring these H100s. Your stock price was getting hammered, people were questioning the CapEx spending and the Metaverse investment. Presumably, you were spending that CapEx to get these H100s. Back then, how did you know to get the H100s and that you'd need the GPUs?

Mark: I think it was because we were working on Reels. We got into a situation where we always want to have enough capacity to build something that we can't quite see on the horizon yet.

With Reels, we needed more GPUs to train the models. It was a big evolution for our services. Instead of just ranking content from people who you follow, we made a big push to start recommending unconnected content - basically content from people or pages that you're not following.

So the corpus of content candidates that we could potentially show you expanded from on the order of thousands to on the order of hundreds of millions. Completely different infrastructure. And we were constrained on the infrastructure that we had to catch up to what TikTok was doing as quickly as we wanted to.

So I looked at that and was like, hey, we have to make sure we're never in this situation again. Let's order enough GPUs to do what we need for Reels and feed ranking. But let's also double that, because our normal principle is there's going to be something on the horizon that we can't see.

Dwarkesh: Did you know it would be AI?

Mark: Well, we thought it was going to be something that had to do with training large models. At the time, I thought it was probably going to be more something related to content. But it's almost just pattern matching in running the company - there's always another thing.

I'm not even sure I had that specific insight at the time. I was so deep in just trying to get the recommendations working for Reels and other content. That's such a big unlock for Instagram and Facebook - to be able to show people interesting content from those they're not even following. But that ended up being a very good decision in retrospect.

And it came from being behind. Most of the times where we make some decision that ends up seeming good is because we messed something up before and just didn't want to repeat the mistake.

#### Why Mark Didn't Sell Facebook Early On

Dwarkesh: This is a total detour, but I actually want to ask about this while we're on this. You didn't sell for $1 billion, but presumably there's some amount you would have sold for, right? Did you write down in your head what you thought the actual valuation of Facebook was at the time, and that they weren't actually getting the valuation right?

Mark: Yeah, I don't know. I mean, look, I think some of these things are just personal. I don't know that at the time I was sophisticated enough to do that analysis. But I had all these people around me making arguments for how a billion dollars was so far in the future - here's the revenue we need to make, here's how big we need to be, it's clearly so many years away. It was very far ahead of where we were at the time.

I didn't really have the financial sophistication to engage with that kind of debate. I just sort of deep down believed in what we were doing. And I did some analysis - okay, what would I go do if I wasn't doing this? Well, I really like building things. I like helping people communicate. I like understanding what's going on with people and the dynamics between people. So I think if I sold this company, I'd just go build another company like this. And I kind of like the one I have!

So I don't know. I think a lot of the biggest bets that people make are often just based on conviction and values. It's actually usually very hard to do the analyses, trying to connect the dots forward.

#### AI Becoming Central to Meta

Dwarkesh: You've had Facebook AI Research for a long time. At what point did making AGI, or however you consider that mission, become a key priority of what Meta is doing?

Mark: It's been a big deal for a while. We started FAIR about 10 years ago. The idea was that along the way to general intelligence or full AI, there can be all these different innovations that are going to improve everything that we do.

We didn't conceive it as a product, it was more a research group. And over the last 10 years, it has created a lot of different things that have improved all of our products and advanced the field. It's allowed other people in the field to create things that have improved our products too. So that's been great.

But there's obviously been a big change in the last few years when ChatGPT comes out, the diffusion models around image creation come out. This is some pretty wild stuff that is pretty clearly going to affect how people interact with every app.

So at that point, we started a second group, the GenAI group, with the goal of bringing that stuff into our products. Building leading foundation models that would power all these different products.

Initially, when we started doing that, the theory was a lot of the stuff we're doing is pretty social - helping people interact with creators, helping people interact with businesses so they can sell things or do customer support, or basic assistant functionality for apps, smart glasses, VR, all these different things.

So initially, it wasn't completely clear that you were going to need full AGI to support those use cases. But then through working on them, I think it's actually become clear that you do. It's in all these subtle ways.

For example, for Llama 2, when we were working on it, we didn't prioritize coding. The reason why is we thought people aren't going to ask Meta AI a lot of coding questions in WhatsApp.

But a somewhat surprising result over the last 18 months is that coding is important for a lot of domains, not just coding. Even if people aren't asking coding questions to the models, training the models on coding helps them be more rigorous, answer questions better, and help reason across a lot of different domains.

So for Llama 3, we really focused on training it with a lot of coding, because that's going to make it better on all these things, even if people aren't primarily asking coding questions.

Reasoning is another example. You might want to chat with a creator, or you're a business trying to interact with a customer. That interaction is not just the person sending a message and you replying. It's a multi-step interaction where you're trying to think through how to accomplish the person's goals.

A lot of times when a customer comes, they don't necessarily know exactly what they're looking for or how to ask their questions. So it's not really the job of the AI to just respond to the question. You need to think about it more holistically. It really becomes a reasoning problem.

So if someone else solves reasoning or makes good advances on it, and we're sitting here with a basic chatbot, then our product is lame compared to what other people are building.

So at the end of the day, we realized we've got to solve general intelligence. We upped the ante and the investment to make sure we could do that. The version of Llama that's going to solve all these use cases for users - is that the version that will be powerful enough to replace a programmer you might have in this building?

I just think all this stuff is going to be progressive over time. There's a lot baked into that question. I'm not sure we're replacing people as much as giving people tools to do more. Is the programmer in this building 10X more productive after? I would lean towards yes.

But I don't believe there's a single threshold of intelligence for humanity. People have different skills. At some point, AI is probably going to surpass people at most of those things, depending on how powerful the models are. But I think it's progressive.

And I don't think AGI is one thing. You're basically adding different capabilities. Multimodality is a key one we're focused on now, initially with photos, images and text, but eventually with videos. And then because we're so focused on the metaverse, 3D type stuff is important.

One modality that I'm pretty focused on that I haven't seen as many other people in the industry focus on is emotional understanding. So much of the human brain is dedicated to understanding people, understanding your expressions and emotions. I think that's its own whole modality. You could say maybe it's just video or image, but it's clearly a very specialized version of those two.

So there's all these different capabilities that I think you want to train the models to focus on, as well as getting a lot better at reasoning, getting a lot better at memory, which I think is its own whole thing.

I don't think we're going to be primarily shoving context into a query context window in the future to ask more complicated questions. I think there will be different stores of memory or custom models that are maybe more personalized to people.

But I think these are all just different capabilities. And then obviously making them big and small, we care about both. If you're running something like Meta AI, then we have the ability for it to be pretty server-based. But we also want it running on smart glasses where there's not a lot of space. So you want to have something that's very efficient for that.

Future Use Cases & Scaling Challenges

Dwarkesh: What is the use case where you're doing tens or even hundreds of billions of dollars worth of inference, using intelligence at an industrial scale? Is it simulations? The AIs in the metaverse? What will we be using the data centers for?

Mark: My bet is that this is going to change all of the products. I think there's going to be a Meta AI general assistant product. That will shift from something that feels more like a chatbot, where you just ask a question that formulates an answer, to things where you're increasingly giving it more complicated tasks that it goes away and does. So that's going to take a lot of inference, a lot of compute.

Then I think a big part of what we're going to do is interacting with other agents for other people, whether it's businesses or creators. I guess a big part of my theory on this is that there's not just going to be one singular AI that you interact with. I think every business is going to want an AI that represents their interests. They're not going to want to primarily interact with you through an AI that is going to sell their competitors' products.

So I think creators is going to be a big one. There are about 200 million creators on our platforms. They all have the pattern where they want to engage their community, but they're limited by hours in the day. And their community generally wants to engage them, but they're also limited by hours in the day.

So if you could create something where an AI could basically allow that creator to own the AI, train it in the way they want, and engage their community, I think that's going to be super powerful too. I think there's going to be a ton of engagement across all these things.

But these are just the consumer use cases. I think when you think about stuff like the Chan Zuckerberg Initiative that my wife and I run, we're doing a bunch of stuff on science. There's obviously a lot of AI work that I think is going to advance science, healthcare, and all these things too.

So I think it ended up affecting basically every area of the products and the economy.

Dwarkesh: The thing you mentioned about an AI that can just go out and do something multi-step for you, is that a bigger model? Is that you'll make Llama 4 where there will be a version that's still 70B, but you'll just train it on the right data and that will be super powerful? What does the progression look like? Is it scaling? Same size but different data sets like you were talking about?

Mark: I don't know that we know the answer to that. I think one pattern that seems to emerge is that you have the base Llama model, and then you build some other application specific code around it. Some of it is fine-tuning for the use case, but some of it is logic for how Meta AI should integrate with tools like Google or Bing to bring in real-time knowledge. That's not part of the base Llama model, that's like part of the application.

So for Llama 2, we had some of that and it was a little more hand-engineered. Part of our goal for Llama 3 was to bring more of that into the model itself. But for Llama 3, as we start getting into more of these agent-like behaviors, I think some of that is going to be more hand engineered. Then I think our goal for Llama 4 will be to bring more of that into the model.

So I think at each step along the way, you kind of have a sense of what's going to be possible on the horizon. You start messing with it and hacking around it. And then I think that helps you hone your intuition for what you want to try to train into the next version of the model itself. Which makes it more general, because anything you're hand coding is inherently brittle and non-general.

Dwarkesh: What is the community fine-tune of Llama 3 you're most excited by? Maybe not the one that will be most useful to you, but just one you will enjoy playing with the most? Like fine-tune it on antiquity and you'll just be talking to Virgil or something. What are you excited about?

Mark: I don't know. I mean, I think the nature of the stuff is that you get surprised. So I think any specific thing that I thought would be valuable, we'd probably be building.

But I think you'll get distilled versions, smaller versions. One thing is eight billion - I don't think that's quite small enough for a bunch of use cases. Over time, I'd love to get a billion parameter model, or a two billion parameter model, or even a 500 million parameter model and see what you can do with that.