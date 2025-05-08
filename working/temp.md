## PREFACE  

The field of Artificial Intelligence (AI) really came into existence with the birth of computers in and around the 1940s and 1950s. For the earlier period of its development, attention was clearly focused on getting computers to do things that, if a human did them, would be regarded as intelligent. Essentially, this involved trying to get computers to copy humans in some or all aspects of their behaviour. In the 1960s and 1970s this opened up a philosophical discussion as to just how close to a human brain a computer could be, and whether any differences that arose were really important. This period – referred to as ‘classical AI’ in this book – was, however, rather limited in its potential.  

In the 1980s and 1990s we saw a whole new approach, a sort of bottom-­up attack on the problem, effectively building artificial brains to bring about AI. This completely opened up the possibilities and created a whole new set of questions. No longer was AI restricted to merely copying human intelligence – now it could be intelligent in its own way. In some cases it could still be brought about by mimicking the way a human brain performed, but now it had the potential to be bigger, faster and better. The philosophical consequence of this was that now an artificial brain could potentially outperform a human brain.  

In more recent years the field has really taken off. Real-­world applications of AI, particularly in the finance, manufacturing and military sectors, are performing in ways with which the human brain simply cannot compete. Artificial brains are now being given their own body, with which to perceive the world in their own way and to move around in it and modify it as they see fit. They are being given the ability to learn, adapt and carry out their wishes with regard to humans. This raises all sorts of issues for the future.  

The aim of this book has been to realise a truly modern and upto-date look at the field of AI in its entirety. Classical AI is certainly looked at, but only as part of the total area. Modern AI is also considered with equal balance. In particular, some of the very latest research into embodied AI and growing biological AI is also discussed.  

The intention is to provide a readable basic guide to the field of AI today – to see where it has come from and where it may be going. The main aim is to provide an introduction for someone not at all familiar with the topic. However, it may well also be of interest to those already involved in science, technology and even computing, who perhaps need to catch up with recent developments.  

I would like to thank many people for their help in putting this book together. In particular, my colleagues and research students at the University of Reading, especially Mark Gasson, Ben Hutt, Iain Goodhew, Jim Wyatt, Huma Shah and Carole Leppard, all of whom have contributed significantly to the work described. I also wish to extend my gratitude to Andy Humphries of Taylor & Francis, who has pushed me to get the book completed despite many other conflicting calls on my time. Finally, I wish to thank my wife, Irena, for her patience, and my kids, Maddi and James, for their criticism.  

Kevin Warwick Reading, January 2011  

## INTRODUCTION  

### SYNOPSIS  

In this opening chapter a brief overview is given of what the book is about, its aims and potential readership. A glimpse is also given of how the subject area has developed over the years, including mention of the key movers, important issues and breakthroughs. Essentially, the chapter provides a gentle helping hand to guide new readers into the subject. This chapter is not a necessity for those already familiar with the subject of AI, but nevertheless it could stimulate some thoughts or provide useful nuggets of information.  

### INTRODUCTION  

The book is written as an introductory course text in Artificial Intelligence (AI), to provide material for a first course for students specialising in areas such as computer science, engineering and cybernetics. However, it can act as a background or reference text for all interested students, particularly in other branches of science and technology. It may also be useful as an introductory text for A-l­evel students and even members of the general public who wish to get an overview of the field in an easily digestible form.  

The subject area has shifted dramatically in the last few years and the text is intended to give a modern view of the subject. Classical AI techniques are certainly covered, but in a limited way – the goal is an all-­encompassing, modern text.  

The content of the book covers aspects of AI involving philosophy, technology and basic methods. Although indicators are given of AI programming with basic outlines, the book does not attend to the details of writing actual programs and does not get bogged down with intricacies concerning the differences between programming languages. The main aim is to give an overview of AI – an essential guide that doesn’t go too heavily into depth on any specific topic. Pointers are given as to further texts which can take the reader deeper into a particular area of interest.  

Although the text provides a general overview, potentially accessible by the general public, it has been written with academic rigour. Some previous texts have been directed more towards a fun book for children – this book is not of that type.  

### EARLY HISTORY OF AI  

There are strong links between the development of computers and the emergence of AI. However, the seeds of AI were sown long before the development of modern computers. Philosophers such as Descartes considered animals in terms of their machine performance, and automatons were the precursors of the humanoid robots of today. But artificial beings can be traced back even further, to stories of the Prague Golem, or even further to Greek myths such as Pygmalion’s Galatea.  

The strongest immediate roots probably date back to the work of McCulloch and Pitts, who, in 1943, described mathematical models (called perceptrons) of neurons in the brain (brain cells) based on a detailed analysis of the biological originals. They not only indicated how neurons either fire or do not fire (are ‘on’ or ‘off ’), thereby operating in a switching binary fashion, but also showed how such neurons could learn and hence change their action with respect to time.  

Perhaps one of the greatest pioneers of the field was a British scientist, Alan Turing. In the 1950s (long before the computers of today appeared), Turing wrote a seminal paper in which he attempted to answer the question ‘Can a machine think?’ To even ask the question was, at the time, revolutionary, but to also come up with an applicable test (commonly known as the Turing Test) with which to answer the question was provocative in the extreme. The test is considered in detail in Chapter 3.  

It was shortly after this that Marvin Minsky and Dean Edmonds built what could be described as the first AI computer, based on a network of the neuron models of McCulloch and Pitts. At the same time, Claude Shannon considered the possibility of a computer playing chess and the type of strategies needed in order to decide which move to make next. In 1956, at the instigation of John McCarthy, along with Minsky and Shannon, researchers came together at Dartmouth College in the USA for the first workshop celebrating the new field of AI. It was here that many of the subsequent classical foundations of the subject were first laid.  

### THE MIDDLE AGES OF AI DEVELOPMENT  

In the 1960s the most profound contribution to the field was arguably the General Problem Solver of Newell and Simon. This was a multi-­purpose program aimed at simulating, using a computer, some human problem-­solving methods. Unfortunately the technique employed was not particularly efficient, and because of the time taken and memory requirements to solve even relatively straightforward real problems, the project was abandoned.  

The other significant contribution of the 1960s was that of Lotfi Zadeh, with his introduction of the idea of ‘fuzzy’ sets and systems – meaning that computers do not have to operate in a merely binary, logical format, but can also perform in a human-l­ike, ‘fuzzy way. This technique and its spin-­offs are considered in Chapter 4.  

Other than these examples, the 1960s was perhaps a time of some foolhardy claims regarding the potential of AI to copy and even perhaps recreate the entire workings of the human brain within a very short space of time. An observation in hindsight is that trying to get a computer to operate in exactly the same way as a human brain was rather like trying to make an aeroplane fly in the same way as a bird. In the latter case one would miss out on the good characteristics of the aeroplane, and so it was that AI research at this time missed out on much of the good points on offer from computers.  

Unfortunately (and quite surprisingly), some of the limited thinking from the 1960s persists today. Some present textbooks (some even under the guise of modern AI) still concentrate merely on the classical approach of trying to get a computer to copy human intelligence, without truly considering the extent and exciting possibilities of different types of AI – in terms of machines being intelligent in their own way, not merely copying human intelligence.  

In this period, considerable effort did go into making computers understand and converse in natural, human language, rather than their more direct machine code. This was partly driven by Turing’s ideas of intelligence, but also partly by a desire for computers to more readily interface with the real world.  

One of the best English-­speaking computer programs was Joseph Weisenbaum’s ELIZA. Indeed, this was the first of what have become known as ‘Chatterbots’. Even at this relatively early stage, some of its conversations were sufficiently realistic that some users occasionally were fooled into thinking they were communicating with a human rather than a computer.  

In fact, ELIZA generally gave a canned response or simply repeated what had been said to it, merely rephrasing the response with a few basic rules of grammar. However, it was shown that such an action appeared to adequately copy, to some extent, some of the conversational activities of humans.  

### THE DARK AGES OF AI RESEARCH  

After the excitement of the 1960s, with substantial research funding and claims of what would shortly be achieved in terms of AI replicating human intelligence, the 1970s proved to be something of a let down, and in many ways was a Dark Age for AI. Some of the more optimistic claims of the 1960s raised expectations to an extremely high level, and when the promised results failed to be realised, much of the research funding for AI disappeared.  

At the same time the field of neural networks – computers copying the neural make-­up of the brain – came to a halt almost overnight due to a scathing attack from Marvin Minsky and Seymour Papert on the inability of perceptrons to generalise in order to deal with certain types of relatively simple problems – something we will look at in Chapter 4.  

It must be realised, however, that in the 1970s the capabilities of computers and therefore AI programs were quite limited in comparison with those of today. Even the best of the programs could only deal with simple versions of the problems they were aimed at solving; indeed, all the programs at that time were, in some sense, ‘toy’ programs.  

Researchers had in fact run into several fundamental limits that would not be overcome until much later. The main one of these was limited computing power. There was nowhere near enough speed or memory for really useful tasks – an example of this from the time was Ross Quillan’s natural language machine, which had to get by with a total vocabulary of 20 words!  

However, the main problem was that AI tasks, such as getting a computer to communicate in a natural language or to understand the content of a picture in anything like a human way, required a lot of information and a lot of processing power, even to operate at a very low, restricted level. General, everyday objects in an image can be difficult for computers to discern, and what humans regard as common-­sense reasoning about words and objects actually requires a lot of background information.  

If the technical difficulties faced in the 1970s were not enough, the field also became an acceptable topic of interest to philosophers. For example, John Searle came up with his Chinese room argument (which we look at in Chapter 3) to show that a computer cannot be said to ‘understand’ the symbols with which it communicates. Further, he argued, because of this the machine cannot necessarily be described as ‘thinking’ – as Turing had previously postulated – purely in terms of symbol manipulation.  

Although many practical researchers simply got on with their jobs and avoided the flak, several philosophers (such as Searle) gave the strong impression that the actual achievements of AI would always be severely limited. Minsky said, of these people: ‘They misunderstand, and should be ignored.’ As a result, a lot of infighting occurred, which took the focus away from technical developments, and towards philosophical arguments which (in hindsight) many now see to be red herrings.  

Almost standing alone at the time, John McCarthy considered that how the human brain operates and what humans do is not directly relevant for AI. He felt that what were really needed were machines that could solve problems – not necessarily computers that think in exactly the same way people do. Minsky was critical of this, claiming that understanding objects and conversing, to be done well, required a computer to think like a person. And so the arguments went on . . .  

### THE AI RENAISSANCE  

The 1980s saw something of a revival in AI. This was due to three factors.  

First, many researchers followed McCarthy’s lead and continued to develop AI systems from a practical point of view. To put it simply, they just got on with it. This period saw the development of ‘expert systems’, which were designed to deal with a very specific domain of knowledge – hence somewhat avoiding the arguments based on a lack of ‘common sense’. Although initially piloted in the 1970s, it was in the 1980s that such systems began to be used for actual, practical applications in industry.  

Second, although the philosophical discussions (and arguments) continued, particularly as regards to whether or not a machine could possibly think in the same way as a human, they seemed to do so largely independently of the practical AI work that was occurring. The two schools simply proceeded with their own thing, the AI developers realising practical industrial solutions without necessarily claiming that computers should or could behave like humans.  

Third, the parallel development of robotics started to have a considerable influence on AI. In this respect a new paradigm arose in the belief that to exhibit ‘real’ intelligence, a computer needs to have a body in order to perceive, move and survive in the world. Without such skills, the argument goes, how can a computer ever be expected to behave in the same way as a human? Without these abilities, how could a computer experience common sense? So, the advent of a cybernetic influence on AI put much more emphasis on building AI from the bottom up, the sort of approach, in fact, originally postulated by McCulloch and Pitts.  

### TO THE PRESENT  

Gradually, the emergent field of AI found its feet. Industrial applications of AI grew in number and it started to be used in expansive areas, such as financial systems and the military. In these areas it was shown to be not only a replacement for a human operative, but also, in many cases, able to perform much better. Applications of AI in these areas have now expanded enormously, to the extent that financial companies that used to earn their money from advising clients now make much bigger profits from developing AI systems to sell to and service for their clients.  

The period since the start of the 1990s has also seen various milestones reached and targets hit. For example, on 11 May 1997, Deep Blue became the first chess-­playing computer system to beat a reigning, world chess champion (Garry Kasparov) at his own game. In another vein, on 14 March 2002 Kevin Warwick (the author) was the first to successfully link the human nervous system directly with a computer to realise a new combined form of AI – but more of that in a moment. On 8 October 2005 it was announced that a Stanford University robot had won the DARPA Grand Challenge by driving autonomously for 131 miles along an unrehearsed desert trail. Meanwhile, in 2009, the Blue Brain Project team announced that they had successfully simulated parts of a rat’s cortex.  

For the most part, such successes as these were not, in any case, due to a newly invented form of technology, but rather to pushing the limits with the technology available. In fact, Deep Blue, as a computer, was over ten million times faster than the Ferranti computer system taught to play chess in 1951. The ongoing, year-­onyear, dramatic increase in computing power is both followed and predicted by what has become known as Moore’s Law.  

Moore’s Law indicates that the speed and memory capacity of computers doubles every two years. It means that the earlier problems faced by AI systems are quite rapidly being overcome by sheer computing power. Interestingly, each year sees some claim or other in a newspaper that Moore’s Law will come to an end due to a limiting factor such as size, heat, cost, etc. However, each year new technological advances mean that available computing power doubles and Moore’s Law just keeps on going.  

On top of this, the period has also seen novel approaches to AI emerge. One example is the method of ‘intelligent agents’. This is a modular approach, which could be said to be mimicking the brain in some ways – bringing together different specialist agents to tackle each problem, in the same sort of way that a brain has different regions for use in different situations. This approach also fits snugly with computer science methods in which different programs are associated with different objects or modules – the appropriate objects being brought together as required.  

An intelligent agent is much more than merely a program. It is a system in itself in that it must perceive its environment and take actions to maximise its chances of success. That said, it is true that in their simplest form, intelligent agents are merely programs that solve specific problems. However, such agents can be individual robot or machine systems, operating physically autonomously.  

As is described in Chapter 4, as well as agents, lots of other new approaches have arisen in the field of AI during this period. Some of these have been decidedly more mathematical in nature, such as probability and decision theory. Meanwhile, neural networks and concepts from evolution, such as genetic algorithms, have played a much more influential role.  

It is certainly the case that particular actions can be construed as being intelligent acts (in humans or animals) up to the point that they can be performed (often more effectively) by a computer. It is also the case that a lot of new developments in AI have found their way into more general applications. In doing so, they often lose the tag of ‘AI’. Good examples of this can be found with data mining, speech recognition and much of the decision making presently carried out in the banking sector. In each case, what was originally AI has become regarded as just another part of a computer program.  

### THE ADVENT OF WIRELESS  

One of the key technologies that became a practical reality in the 1990s was wireless technology as a form of communication for computers, following on from widespread introduction and use of the internet. From an AI perspective, this completely changed the playing field. Until that time what existed were standalone computers, the power and capabilities of which could be directly compared with standalone human brains – the normal set up. With networked computers becoming commonplace, rather than considering each computer separately, it became realistically necessary to consider the entire network as one, large intelligent brain with much distribution – called distributed intelligence.  

Thanks to wireless technology, connectivity is an enormous advantage for AI over human intelligence – in its present-­day standalone form. At first it was mainly a means whereby computers could communicate rapidly with each other. However, it has quickly become the case that large pockets of memory are dispersed around a network, specialism is spread and information flows freely and rapidly. It has changed the human outlook on security and privacy and has altered the main means by which humans communicate with each other.  

### HAL 9000  

In 1968 Arthur C. Clarke wrote 2001: A Space Odyssey, which was later turned into a film of the same name by Stanley Kubrick. The story contains a character, HAL 9000. HAL is a machine whose intelligence is either the same as or better than human intelligence. Indeed it/he exhibits human traits of meaningful emotions and philosophy. Although HAL was merely a fictional machine, it nevertheless became something of a milestone to be reached in the field of AI. In the late 1960s many believed that such a form of AI would exist by $2001-$ particularly as HAL was based on underpinning science of the time.  

Various people have asked why we didn’t have some form of HAL, or at least a close approximation, by 2001. Minsky grumbled that too much time had been spent on industrial computing rather than on a fundamental understanding of issues such as common sense. In a similar vein, others complained that AI research concentrated on simple neuron models, such as the perceptron, rather than on an attempt to get a much closer model of original human brain cells.  

Perhaps the answer as to why we didn’t have HAL by 2001 is an amalgamation of these issues, and more. We simply didn’t have the focused drive to achieve such a form of AI. No one put up the money to do it and no research team worked on the project. In many ways – such as networking, memory and speed – we had already realised something much more powerful than HAL by 2001, but emotional, moody reflections within a computer did not (and probably still do not) have a distinctive role to play, other than perhaps in feature films.  

For the guru Ray Kurzweil, the reason for the non-­appearance of HAL is merely computer power and, using Moore’s Law, his prediction is that machines with human-l­evel intelligence will appear by 2029. Of course, what is meant by ‘human-l­evel intelligence’ is a big question. My own prediction in my earlier book, March of the Machines, was not too far away from Kurzweil though – machines will have an intelligence that is too much for humans to handle by 2050.  

### TO THE FUTURE  

Much of the classical philosophy of AI (as discussed in Chapter 3) is based largely on the concept of a brain or computer as a sort of standalone entity – a disembodied brain in a jar, so to speak. In the real world, however, humans interact with the world around them through sensors and motor skills.  

What is of considerable interest now, and will be even more so in the future, is the effect of the body on the intellectual abilities of that body’s brain. Ongoing research aims at realising an AI system in a body – embodiment – so it can experience the world, whether it be the real version of the world or a virtual or even simulated world. Although the study of AI is still focused on the AI brain in question, the fact that it does have a body with which it can interact with the world is seen as important.  

As we step into the future, perhaps the most exciting area of AI research is that in which AI brains are grown from biological neural tissue – typically obtained from either a rat or a human. Particular details of the procedures involved and the methods required to launder and successfully grow living biological neural tissue are given in Chapter 5. In this case, the AI is no longer based on a computer system as we know it, but rather on a biological brain that has been grown afresh.  

This topic is certainly of interest in its own right as a new form of AI, and is potentially useful in the future for household robots. However, it also provides a significant new area of study in terms of its questioning of many of the philosophical assumptions from classical AI. Essentially, such philosophy discussed the difference between human intelligence and that of a silicon machine. In this novel research area, however, AI brains can be grown from human neurons, by building them up into something like an AI version of a human brain type, thus blurring what was a crisp divide between two distinctly different brain styles.  

### CYBORGS  

It could be said that when a biological AI brain is given a technological robot body then it is a type of cyborg – a cybernetic organism (part animal/human, part technology/machine) – with an embodied brain. This area of research is the most exciting of all – the direct link between an animal and a machine for the betterment (in terms of performance) of both. Such a cyborg as discussed is just one potential version. Indeed, neither the normal researched form of cyborg nor that usually encountered in science fiction is of this type.  

The type of cyborg more regularly encountered is in the form of a human who has, implanted in them, integral technology which is linked to a computer which thereby gives them abilities above those of the human norm – meaning a cyborg has skills that a human does not. These skills can be physical and/or mental and can pertain to intelligence. In particular, we will see that an AI brain is usually (excluding a biological AI brain) very different from a human brain, and these differences can be realised in terms of advantages (particularly for AI).  

Reasons for the creation of cyborgs generally revolve around enhancing the performance of the human brain by linking it directly with a machine brain. The combined brain can then, potentially at least, function with characteristic features from both its constituent parts – a cyborg could therefore possibly have better memory, faster math skills, better senses, multidimensional thought and improved communication skills when compared with a human brain. To date, experiments have successfully shown both sensory enhancement and a new form of communication for cyborgs. Although not specifically dealt with in this text, it is felt that the material covered in Chapters 5 and 6 will put the reader in good stead for a follow-­on study in this field.  

# CONCLUDING REMARKS  

This chapter has set the scene for the rest of the book, giving a brief overview of AI’s historical development and some of the key developments. In doing so, some of the movers and shakers in the field have been introduced.  

In the following text, after a gentle introduction (Chapter 1) to the overall concept of intelligence, Chapters 2 and 3 concentrate on the classical AI methods that were originally introduced. Chapters 4 and 5 then consider ongoing, modern and more futuristic approaches. You will find that the more novel, up-­to-date sections of Chapters 4 and 5 are probably not encountered in most other AI textbooks – even when such books are called Artificial Intelligence or AI: A Modern Approach. Chapter 6 then considers how an AI can perceive the world through its sensor system.  

Enjoy!  

KEY TERM  

embodiment  

### FURTHER READING  

1 AI: A Guide to Intelligent Systems by M. Negnevitsky, published by Addison Wesley, 1st edition, 2001. This is quite a general book which keeps mathematics to a minimum and provides a reasonably broad coverage of classical AI with little jargon. It is a good introductory guide, based on lectures given by the author. Unfortunately, it doesn’t deal with topics such as robotics, biological AI or sensing.   
2 Artificial Intelligence: A Beginner’s Guide by B. Whitby, published by OneWorld, 2008. This is quite a reasonable, level-­headed overview text. It is more concerned with ethical issues and is fairly conservative, but well posed. It doesn’t explain topics in any depth, however.   
3 Understanding Artificial Intelligence, edited by Scientific American staff, Warner Books, 2002. This is actually a collection of essays on the subject. Although mostly concerned with the philosophy of AI, it gives a feel for what different experts consider to be the main issues.