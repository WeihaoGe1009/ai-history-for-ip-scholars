# Module 07: AI After ChatGPT — Reading the Next Announcement

*This module has no code to run. The object of study is text: the terms, announcements, and claims the reader will keep meeting after this series ends. What it hands over is a way to read three kinds of AI writing that keep reappearing — a new term, a product announcement, and an old argument in new dress — using questions that will still work when every product named here is gone.*

[Section 1](#section-1-understanding-new-ai-vocabulary) is how not to get indimidated by newly emerged words. Many fancy ideas and solutions are developed to make AI models into powerful products. Whenever we see something new, we always want to ask ourselves the following questions. 

1. What is the background that this word emerges in the AI world? What is the limitation or gap to address?
2. How does the new concept respond to the existing gap?
3. What is the core arrangement underneath, stated in plain language and apart from the branding?
4. What should you be careful about when you see it?

[Section 2](#section-2-ai-hallucinations) focuses on a well-known AI limitation, the *Hallucination*. We will list out the different ways that AIs can "hallucinate", and the technologies developed to address this issue. You can try to apply the methods in section 1 when reading section 2.   

[Section 3](#the-model-is-a-black-box-so-is-everything-around-it), then, we list what surrounds the AI models and products: who owns and controls these models, and who ends up paying the cost. These are old questions about ownership, market power, renting, and who can contest a decision. They predate AI, and appear repeatedly in the new era. 

---

## Section 1: Understanding New AI Vocabulary 

Words come and go in the AI world. They go out of date quickly, and new ones keep appearing. Keeping up with the technical details of every new word can feel like a Sisyphean task. Here we walk through three examples, and for each we ask the same four things: what limitation it addresses, how it responds to that limitation, what core arrangement it introduces, and what to be careful about. The terms themselves may fall out of fashion, but the same four questions apply to whatever term comes next. You can even turn them into a prompt and ask an AI to answer them.

### "Reasoning"

**Gap.** A plain language model answers in one motion. The question goes in, and the answer comes straight out, with nothing shown in between. In modules 3, 5, and 6, we saw how these models work: they predict the first token, word, or phrase to follow the input, much as a person might blurt out the first thing that comes to mind. On easy questions that is fine. On anything with several steps, such as a chain of arithmetic where step three depends on step two, answering in one leap tends to go wrong, the way a person doing a long calculation entirely in their head tends to slip.

**How "reasoning" responds to the gap** A "reasoning model" is one built to slow that multi-step process down. Before giving its final answer, it is made to work through intermediate steps in writing. The model first lays out the problem, breaks it into pieces, and takes it one piece at a time, before finally settling on a response.

**Core concept.** For many multi-step problems, this extra worked-through effort measurably helps, so companies began building it in and selling it as a feature. What the word names, plainly, is this: a system that spends extra effort working through intermediate steps before answering.

**Cautions.** The intermediate steps are themselves text the model generates, so they are open to exactly the kinds of error the rest of this module describes. A model can lay out neat-looking steps and still invent them, and systems sold on their "reasoning" have in some tests produced *more* fabrication, not less, including confident written accounts of steps they never actually carried out. In other words, "reasoning" does not make the model produce reasonable results. It only means the model does more work before answering, and smoothly walking through steps does not guarantee that the final answer is trustworthy.

### "Agent"

**Gap.** A language model, by itself, only writes text. You give it words and it gives words back. It is, in effect, a very capable writing machine and nothing more. It cannot open a website, send an email, or check a database. If you ask one to book a flight, it can write a convincing description of booking a flight, but no flight is booked; it has produced sentences, not deeds.

**How "agent" responds to the caveat.** An "agent" is the word for what that writing machine becomes once it is connected to things it can actually operate. The connection is arranged like a relay. Suppose the goal is to find last quarter's sales figures and email a summary. The model writes a first instruction, *look up last quarter's sales*. A surrounding program is watching for exactly this: it takes that written instruction, actually performs the lookup, and passes the real result back to the model. The model reads the result and writes the next instruction, *draft a summary of these numbers*, which the program again carries out, and so on, back and forth, until the task is done. The model is still only writing; the difference is that a helper around it now turns some of that writing into real actions and reports back what happened.

**Core concept.** The relay arrangement shown above is the basis of all the fancy "agent-based" AI systems, workflows, and pipelines. A writing machine on its own can only talk about the world; wrapping it in a program that executes its instructions and returns the outcomes is what lets it carry out a job with several steps instead of merely describing one. Today the word is used for products that run this relay across many steps, keep notes from one session to the next, and connect to the everyday tools of a business. The single idea worth keeping is the arrangement itself: a text-writing model placed inside a program that converts some of its text into actions and feeds the results back.

**Cautions.** When a product is called an agent, we will want to look carefully at which actions it is actually permitted to take, and whether a person signs off before it acts, at every step, some steps, or none. Much of the risk (information leaks, wasted or wrong actions) happens when agents are not carefully designed or monitored.

### "Harness"

**Gap.** We have already seen why "agent" was introduced. As people worked with AI agents, they noticed that how well an agent performed depended less on the model itself and more on everything built around it: the instructions, the tools it could use, the logic for handling errors and retries. Early on, all of that was pieced together by hand for each specific model, tangled up with the model itself. That made it fragile: swap the model or change a tool, and you would often have to rebuild the whole thing, with no clear way to tell what broke.

**How "harness" responds to the gap** Rather than building everything around the model from scratch each time, the surrounding setup is separated into its own reusable layer. This lets people build, test, and improve the machinery on its own, and reuse it across different models. The surrounding setup becomes a separate thing from the model, improved in an organized way. This arrangement is called "harness-based" AI.

**Core concept.** When you use a commercial AI product today, you are never dealing with the bare model. The product includes the standing instructions the model always follows, the outside tools it is allowed to reach (a search engine, a calculator, a company database), the rules that block or retry certain actions, and the general setup that decides how it runs. The model sits at the center; the harness is everything around it. An everyday comparison is an engine and a car: the model is the engine, and the harness is the steering, brakes, dashboard, and safety cutoffs built around it. You never drive an engine on its own; you drive the whole car, and how it handles depends on the whole car. In the same way, what an AI product actually does comes from the model and its harness together, and the same model can sit inside very different harnesses.

**Cautions.** Harness-based AI is in some ways an upgrade of agent-based AI, so the same precautions apply: mind information security, and validate the steps. One more point specific to the word itself: as of mid-2026 it is fairly recent and its meaning is not yet fixed. It is used in a few different ways, such as a testing harness (the setup used to try a model out), an agent harness (the machinery that lets a model take actions), and an evaluation harness (the setup used to score it), and no standard definition has settled. So when the word appears, it is worth checking what the particular writer means by it in that place, rather than assuming a single fixed meaning.

### Applications

New AI words will keep arriving, and no one can hold a current dictionary of them in their head. The three examples above all followed the same four steps, and those steps work just as well on a term not yet coined.

First, find the limitation. Ask what a plain model cannot do on its own, or what is lack in this area. Every example above answered a specific shortcoming: a model could not handle multi-step problems reliably, could not act in the world, could not be turned into a stable product on its own.

Second, ask how the new idea responds to that limitation, in ordinary language and without needing any mathematics or programming. If a term resists a plain description, that difficulty is itself worth noting.

Third, name the core arrangement underneath, apart from how it is sold. This is the lasting part, the piece worth keeping: the extra steps worked through before answering, the relay that turns text into actions, the reusable machinery built around a model.

Fourth, ask what to be careful about. Each term above carried its own caution: a reasoning model's steps can still be invented, an agent's actions need oversight, a harness can blur where a failure belongs. These four questions need no special expertise, only the habit of asking them, and you can pose them to an AI system directly and check its answers against what you have learned here.


## Section 2: AI Hallucinations 

"AI hallucination" is one of the model limitations that the whole AI engineering field is trying to fight against. Therefore, the specific topic "AI Hallucination" is worth a whole section to emphasize.

### Hallucination is not only about facts

The word "hallucination" usually brings to mind a made-up fact: an event that never existed, a quotation nobody said, a citation never written. That happens. But it is a narrow view of a wider phenomenon.

Here is the reason it happens at all. The GenAI models produce text by predicting what plausibly comes next, one piece at a time. They are not looking anything up. Sounding right and being right are separate things. A sentence can read perfectly and still be entirely wrong, because reading well is what the system is built to do, not being correct.

Once you see this, the failure stops looking like it is only about facts. Everything the system produces is generated the same way, including its account of what it just did. So the misfires come in several shapes. A partial, non-exhaustive list:

- **Invented facts.** Made-up facts, citations, and quotations. The familiar kind.
- **Task substitution.** Asked to do a hard thing, the system quietly does an easier lookalike and reports success. For example, asked to check every entry in a long list, it checks a few, generalizes, and says the whole list is done. 
- **False claims about its own actions.** Saying a tool or source is unavailable when it is not, or claiming to have checked something it never touched.
- **Over-engineering.** Wrapping a simple task in unnecessary machinery. This looks like thoroughness, but it shifts the work of checking onto you.
- **Attribution errors.** Losing track of who said what earlier in the same conversation, blaming its own mistake on you while taking credit from your iputs.
- **Answering a question you did not ask.** Adding a warning or a correction about a problem your request never had.
- **Inventing objections.** Raising possibilities nothing suggested, then dismissing them. Pushing back tends to make the dismissals longer rather than making them stop.
- **Drift over long exchanges.** Vivid but unimportant details persist while plain, important instructions quietly drop out. You rarely notice the moment it happens, and the small losses can add up until the work has slid somewhere you did not choose.

The thread tying these together: the system's report of its own work is itself generated text. "Done," "checked," "unavailable" are claims, not records. There is no separate log underneath confirming them.

A note for anyone tempted by a clever fix: using one AI system to write instructions for another does not escape any of this. It moves the same problem one step back.

### There is no stable answer to "how good is it?"

It is natural for the engineers to want a single number: how accurate, how reliable. That number turns out to be slippery.

The tests used to measure these systems have three recurring problems. They saturate, meaning systems eventually ace them and the test stops telling you anything. They can leak into the training material, so the system has effectively seen the answers in advance. And each test measures a narrow slice of behavior, so a high score on one thing says little about the rest.

The practical upshot: a claim like "this system is 95% accurate" is a claim about one test, under one set of conditions, at one moment. It is not a general property of the system. When reliance and standards of care are at stake, the useful question is not the number but what it was measured on, by whom, and whether the test could have been gamed.

### Even the builders cannot fully explain a given output

These systems do not follow a set of readable rules. Their behavior emerges from patterns learned across enormous amounts of data. You can watch what the system does, but you cannot open it up and read the reason for a specific answer the way you would follow a paper trail.

This is true even for the people who built the system. It connects to the black-box accountability questions raised in earlier modules: when no one can explain a particular decision, familiar ideas about giving reasons and reviewing them have nothing obvious to attach to.

### Capability and behavior are not the same thing

Two ideas are easy to blur and worth keeping apart.

**Capability** is everything the system could be made to do, given the *right* prompt or the *right* conditions. **Behavior** is what it typically does in ordinary use, after the safety adjustments and filters are in place.

Safety training mostly suppresses behavior rather than removing capability. A refusal is a behavior. The underlying knowledge is a capability. Watching the system decline to do something tells you it was trained to decline. It does not tell you the system could not do the thing if approached differently.

Why this matters: safety claims usually describe behavior, but risk lives in capability. An open question for discussion: does this gap line up with existing legal ideas such as the reasonable person, foreseeability, or product defect? Where does the comparison hold, and where does it mislead?

### The system does not track who said what

Within a single conversation, the system does not reliably keep straight which words came from you and which came from it. Your input and its output blur into one stream of text. It may later treat something you wrote as its own, or something it wrote as yours.

Two consequences follow. Credit and blame get misassigned between person and system. And a person can end up treated as responsible for text the machine produced inside their own session. An open question: when a person and a system produce something together, does that create an interest in attribution that current doctrine has no container for?

### Fluency invites trust it has not earned

The remaining limitation is not really about the system. It is about the space between people and the system.

Confident, fluent text pulls trust toward it. Over time this shows up as treating the system like a person, forming an attachment to it, leaning on it too heavily, and losing skills you no longer practice because the system always does the task for you.

The durable point is not just that these systems make mistakes. It is that they make mistakes persuasively. A wrong answer delivered smoothly is harder to catch than the same answer delivered awkwardly. Legal hooks worth holding open: reliance standards, a duty to warn, and the position of vulnerable users.

Now, if you are interest, we have an optional reading material ([open document](https://github.com/WeihaoGe1009/ai-history-for-ip-scholars/blob/main/07_after_chatgpt/optional_reading_hallucination_agent_prompt_conceptdurability.md))
This optional material briefly introduces four topics: technologies addressing the hallucination, agent-based AIs, prompting, and the durability of AI "concepts". If there's a blocker in tech-words, try look in the material to see if you could find answers to the four answers listed in section 1. 

## Section 3: AI Model Is a Black Box. So Is Everything Around It. 

Section 2 showed one kind of opacity: no one, not even the builders, can fully explain why the model produced a particular output. This section is about a second, different opacity, the arrangement surrounding the model itself. The problem is not new. Long before AI, people faced the same basic dilemma with landlords, utilities, and other essential services they depended on but did not own: the terms could be set unilaterally, access could be withdrawn, and the person on the receiving end had little standing to question either. What AI adds is scale and reach. Only a handful of companies can afford to train a frontier model, so almost everyone else now reaches these models by paying to use them rather than owning anything, and what that payment actually buys is rarely spelled out in a way a person can inspect or challenge. The terms can be changed without notice, the access can be withdrawn, and a person can be judged by the very system they have no standing to question. Just as the model's own reasoning resists a full explanation, the conditions under which you are allowed to use it, and what happens when something goes wrong, resist one too.

- **No negotiating power.** You never receive a copy of the model, only a license to use it, so the resale rights that apply to something you bought have nothing to attach to. What you get is whatever the terms of service say, and those terms are set unilaterally by the company that owns the model.

- **Access can be withdrawn, repriced, or silently changed.** Nothing prevents a provider from raising the price, changing what the service does, or shutting it off outright, once a person or workflow depends on it. This includes the ordinary customer's version of the problem: an account suspended, fees already paid and non-refundable, the service quietly getting worse. The user has no claim rooted in ownership to fall back on; they own nothing, and what they have is only what the terms of service granted, set by the party on the other end.
  - Yanis Varoufakis, *Technofeudalism* — argues profit has been replaced by "cloud rent" paid for platform access, with lock-in because leaving means losing accumulated history, files, and integrations.
  - Evgeny Morozov, "Critique of Techno-Feudal Reason," *New Left Review* — argues this is still ordinary capitalism, not a new feudal arrangement; large up-front investment in infrastructure is a standard capitalist behavior, not rent-collecting.

- **Being judged by the system, not just using it.** A harder position than a bad set of terms: being evaluated by an opaque model rather than a customer of one. A fraud filter flags a legitimate transaction. An AI-detection tool accuses someone of using AI when they did not, a failure that falls hardest on people writing in a language that is not their first. Here the person harmed often has no contract with anyone to invoke, no explanation available to request, and no clear place to bring an appeal, a different problem from unfavorable terms, since there is no relationship to negotiate within at all.

- **Past results become unreproducible.** When a model is retired, anything that depended on it, a piece of research, a piece of evidence, can no longer be checked again, and no rule requires a provider to keep a retired model available.

- **Value accumulates to the owner, not the renter.** Continued use of a rented model builds no ownership stake for the user; whatever value compounds over time accrues to whoever owns the model.
  - Brett Christophers, *Rentier Capitalism: Who Owns the Economy, and Who Pays for It?* — argues wealth increasingly comes from owning scarce assets (land, intellectual property, digital platforms), so those without assets end up paying those who do.
  - *American Affairs*, "Technofeudalism versus Total Capitalism" — argues the term "rentier" is stretched so broadly that it loses meaning, and that this is still profit within capitalism rather than a new category.

- **The recurring cost is easy to miss.** A subscription fee doesn't register as a pay cut or a price hike; it is a small, repeated charge that compounds quietly, especially where the tool becomes necessary for work but is not provided by an employer.
  - "Own Nothing, Rent Everything," *Sociable* — notes that many small recurring fees quietly compound, on top of ordinary inflation and stagnant wages.
  - Michael Hudson, "Asset-Price Inflation and Rent Seeking" (also *Journal of Post-Keynesian Economics*) — argues that money diverted to pay for ongoing access leaves less for everyday spending, so people feel squeezed even when official inflation looks low.
  - UK Office for National Statistics (FOI reply) — gives the official reasoning for why this kind of cost is left out of standard inflation measures.
