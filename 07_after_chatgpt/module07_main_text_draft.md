# Module 07: AI After ChatGPT — Reading the Next Announcement

*This module has no code to run. The object of study is text: the terms, announcements, and claims the reader will keep meeting after this series ends. What it hands over is a way to read three kinds of AI writing that keep reappearing — a new term, a product announcement, and an old argument in new dress — using questions that will still work when every product named here is gone.*

Section 1 is how not to get indimidated by newly emerged terminologies. We always want to ask ourselves the following questions. 

1. What can a plain model not do on its own here? This is the limitation, or caveat, the term addresses.
2. How does the new concept respond to that limitation?
3. What is the core arrangement underneath, stated in plain language and apart from the branding?
4. What should you be careful about when you see it?

Section 2 introduces 6 questions to think about, when looking at a product announcement or model release notice. 

1. What is the base model?
2. What was it trained on?
3. What is bolted around it?
4. What can't it know, and what might it hallucinate — about facts, or about its own work?
5. Who controls it?
6. Who can contest what it decides?

Section 3 lists some debates and arguments rooted back before AI-era, and let's see how they evolves in the context of AI. 

---

## Section 1: Understanding New AI Terms

AI terms come and go. They go out of date quickly, and new ones keep appearing. Keeping up with the technical details of every new term can feel like a Sisyphean task. Here we walk through three examples, and for each we ask the same four things: what limitation it addresses, how it responds to that limitation, what core arrangement it introduces, and what to be careful about. The terms themselves may fall out of fashion, but the same four questions apply to whatever term comes next. You can even turn them into a prompt and ask an AI to answer them.

### "Reasoning"

**Caveat.** A plain language model answers in one motion. The question goes in, and the answer comes straight out, with nothing shown in between. In modules 3, 5, and 6 we saw how these models work: they predict the first token, word, or phrase to follow the input, much as a person might blurt out the first thing that comes to mind. On easy questions that is fine. On anything with several steps, such as a chain of arithmetic where step three depends on step two, answering in one leap tends to go wrong, the way a person doing a long calculation entirely in their head tends to slip.

**How "reasoning" responds to the caveat.** A "reasoning model" is one built to slow that down. Before giving its final answer, it is made to work through intermediate steps in writing. The model first lays out the problem, breaks it into pieces, and takes it one piece at a time, before finally settling on a response.

**Core concept.** For many multi-step problems, this extra worked-through effort measurably helps, so companies began building it in and selling it as a feature. What the word names, plainly, is this: a system that spends extra effort working through intermediate steps before answering.

**Cautions.** The intermediate steps are themselves text the model generates, so they are open to exactly the kinds of error the rest of this module describes. A model can lay out neat-looking steps and still invent them, and systems sold on their "reasoning" have in some tests produced *more* fabrication, not less, including confident written accounts of steps they never actually carried out. In other words, "reasoning" does not make the model produce reasonable results. It only means the model does more work before answering, and smoothly walking through steps does not guarantee that the final answer is trustworthy.

### "Agent"

**Caveat.** A language model, by itself, only writes text. You give it words and it gives words back. It is, in effect, a very capable writing machine and nothing more. It cannot open a website, send an email, or check a database. If you ask one to book a flight, it can write a convincing description of booking a flight, but no flight is booked; it has produced sentences, not deeds.

**How "agent" responds to the caveat.** An "agent" is the word for what that writing machine becomes once it is connected to things it can actually operate. The connection is arranged like a relay. Suppose the goal is to find last quarter's sales figures and email a summary. The model writes a first instruction, *look up last quarter's sales*. A surrounding program is watching for exactly this: it takes that written instruction, actually performs the lookup, and passes the real result back to the model. The model reads the result and writes the next instruction, *draft a summary of these numbers*, which the program again carries out, and so on, back and forth, until the task is done. The model is still only writing; the difference is that a helper around it now turns some of that writing into real actions and reports back what happened.

**Core concept.** The relay arrangement shown above is the basis of all the fancy "agent-based" AI systems, workflows, and pipelines. A writing machine on its own can only talk about the world; wrapping it in a program that executes its instructions and returns the outcomes is what lets it carry out a job with several steps instead of merely describing one. Today the word is used for products that run this relay across many steps, keep notes from one session to the next, and connect to the everyday tools of a business. The single idea worth keeping is the arrangement itself: a text-writing model placed inside a program that converts some of its text into actions and feeds the results back.

**Cautions.** When a product is called an agent, we will want to look carefully at which actions it is actually permitted to take, and whether a person signs off before it acts, at every step, some steps, or none. Much of the risk (information leaks, wasted or wrong actions) happens when agents are not carefully designed or monitored.

### "Harness"

**Caveat.** We have already seen why "agent" was introduced. As people worked with AI agents, they noticed that how well an agent performed depended less on the model itself and more on everything built around it: the instructions, the tools it could use, the logic for handling errors and retries. Early on, all of that was pieced together by hand for each specific model, tangled up with the model itself. That made it fragile: swap the model or change a tool, and you would often have to rebuild the whole thing, with no clear way to tell what broke.

**How "harness" responds to the caveat.** Rather than building everything around the model from scratch each time, the surrounding setup is separated into its own reusable layer. This lets people build, test, and improve the machinery on its own, and reuse it across different models. The surrounding setup becomes a separate thing from the model, improved in an organized way. This arrangement is called "harness-based" AI.

**Core concept.** When you use a commercial AI product today, you are never dealing with the bare model. The product includes the standing instructions the model always follows, the outside tools it is allowed to reach (a search engine, a calculator, a company database), the rules that block or retry certain actions, and the general setup that decides how it runs. The model sits at the center; the harness is everything around it. An everyday comparison is an engine and a car: the model is the engine, and the harness is the steering, brakes, dashboard, and safety cutoffs built around it. You never drive an engine on its own; you drive the whole car, and how it handles depends on the whole car. In the same way, what an AI product actually does comes from the model and its harness together, and the same model can sit inside very different harnesses.

**Cautions.** Harness-based AI is in some ways an upgrade of agent-based AI, so the same precautions apply: mind information security, and validate the steps. One more point specific to the word itself: as of mid-2026 it is fairly recent and its meaning is not yet fixed. It is used in a few different ways, such as a testing harness (the setup used to try a model out), an agent harness (the machinery that lets a model take actions), and an evaluation harness (the setup used to score it), and no standard definition has settled. So when the word appears, it is worth checking what the particular writer means by it in that place, rather than assuming a single fixed meaning.

### Applying this to the next term

New AI words will keep arriving, and no one can hold a current dictionary of them in their head. The three examples above all followed the same four steps, and those steps work just as well on a term not yet coined.

First, find the limitation. Ask what a plain model cannot do on its own in this area. Every term above answered a specific shortcoming: a model could not act in the world, could not handle multi-step problems reliably, could not be turned into a stable product on its own.

Second, ask how the term responds to that limitation, in ordinary language and without needing any mathematics or programming. If a term resists a plain description, that difficulty is itself worth noting.

Third, name the core arrangement underneath, apart from how it is sold. This is the lasting part, the piece worth keeping: the relay that turns text into actions, the extra steps worked through before answering, the reusable machinery built around a model.

Fourth, ask what to be careful about. Each term above carried its own caution: a reasoning model's steps can still be invented, an agent's actions need oversight, a harness can blur where a failure belongs. These four questions need no special expertise, only the habit of asking them, and you can pose them to an AI system directly and check its answers against what you have learned here.


---

## Section 2: How to Read an Announcement

Below is a fictional launch announcement. It is a composite: nothing here is quoted from a real company, but every move in it — the framing, the comparisons, the reassurances — is drawn from how real launches are actually written. The company is Company A and the model is Model B, so that nothing dates. Read it once. Before the commentary, try the exercise: which of the six questions from the top of this module does this text answer, and which does it slide past?

> **Company A: introducing Model B, our most capable system yet.**
>
> Today we're introducing Model B, our most capable model yet. Model B delivers major gains in reasoning, coding, and agentic tasks, and is available starting today in our apps and through the API.
>
> Model B outperforms our previous flagship, Model A, and the leading models from other providers across a wide range of industry benchmarks. The improvements are largest on complex, multi-step problems: on GenBench, a widely used benchmark for multi-step reasoning, Model B scores 62%, up from 41% for Model A. It also writes higher-quality code, follows instructions more reliably, and is better at recognizing when a task calls for a tool rather than a guess. Alongside these gains, Model B is faster than Model A and roughly 40% cheaper per token.
>
> Early-access customers have used Model B across a range of settings. A financial-services team reported cutting the hours its analysts spend on document review; an engineering group said Model B completes multi-step tasks their previous tooling couldn't finish. "Model B is now the default across our team," one early-access partner said. "It handles long, multi-step work end to end, and it's noticeably better at telling us when it's unsure."
>
> Model B is also our most capable agentic model to date. It can plan and carry out multi-step tasks, call external tools, and work across the applications teams already use, keeping track of context along the way. With a 500,000-token context window, it can take in entire codebases, long document sets, and extended conversations at once.
>
> Safety remains central to how we build. We spent months evaluating Model B before release, including red-teaming with outside experts across areas such as cybersecurity, bias, and misuse, and we're publishing a detailed system card and technical report alongside this launch. As with any model, Model B still has limitations — it can make factual errors and, at times, state them confidently — and we will continue to improve it based on real-world use. We do not train our models on customer data without explicit permission.
>
> Model B is available today on Company A's web and mobile apps and through the API, as well as on major cloud platforms. It is included for Pro, Team, and Enterprise plans, with higher rate limits at higher tiers. API pricing is $5 per million input tokens and $25 per million output tokens, with a 500,000-token context window. To get started, see our documentation.


### Commentary

Read the announcement not for what it asserts but for the shape of what it asserts — where it is specific, where it is warm, and where it goes quiet.

**The opening frame.** The first lines are not about the product at all; they are about the reader's world and the cost of being left behind. This is standard, and worth naming as a technique rather than a claim: it sets a mood of inevitability before a single verifiable statement appears. Nothing here is false. Nothing here is checkable either. The reader's task is to notice the register shift when the prose moves from mood to claim, and to hold the two apart.

**"Preferred it to the leading competitor... on the tasks that matter most."** A comparison is offered, which is more than pure adjectives — but every load-bearing word is unspecified. Preferred by whom, on which tasks, judged how? "The tasks that matter most" is chosen by the company, after the fact. Recall the evaluation problem from earlier in the module: a preference result is only as meaningful as the method behind it, and the method is exactly what a launch tends to omit. Questions 1 and the evaluation problem meet here.

**"Built from the ground up... we do not distill... clean, traceable, and appropriately licensed."** This paragraph is the most interesting in the announcement, because it makes strong, specific, *affirmative* claims about training data — the very thing most launches avoid. That is to its credit, and also exactly why it deserves the most scrutiny. "Clean," "traceable," and "appropriately licensed" are strong words; the reader can ask what would count as evidence for each, whether any is offered here, and who would be in a position to check. An affirmative provenance claim is a promise that can be tested in principle — which is different from having been tested. Question 2 is answered in words; whether it is answered in fact is left to trust.

**"Most capable agentic system... across the tools your team already uses... your workflows stay yours."** Question 3 (what is bolted around it) is genuinely addressed: there is an action loop that reaches into the organization's tools. What the warm phrasing softens is everything that matters when such a system acts: which steps happen without a human confirming them, what occurs when a step goes wrong inside real systems, and who answers for the result. "Your workflows stay yours" is reassuring about ownership while saying nothing about responsibility.

**"Passed our most thorough safety review yet... built to remain under human direction."** A safety claim measured against the company's own past, with a report promised alongside. Note what kind of claim it is. A review of what a system usually does is a claim about its behavior; the harder question is what it can be made to do under pressure, which is a claim about its capability — and the two can diverge sharply. "Built to remain under human direction" states an intention, not a demonstrated limit.

**"Available today; pricing scales with use."** Two words carry the whole of questions 5 and 6, mostly by omission. The model is rented, not owned; it can be repriced, altered, or withdrawn, and nothing here promises notice, stability, or any way to preserve results that depended on this exact version. Nothing anywhere in the text addresses who could contest a decision the model makes, or an account action taken against a user. The silence is not an oversight. It is the shape of the genre.

### The shape, not the company

Lay the six questions against the announcement and a pattern appears: one question answered by comparison without method, one answered by strong words awaiting evidence, one genuinely addressed but stripped of the parts about responsibility, one met with an assurance about behavior that leaves capability untouched, and two answered mainly by silence. None of this is special to the invented Company A. It is the standard distribution of a launch announcement, and learning to see that distribution — which questions the genre reliably answers, and which it reliably leaves blank — is the durable skill this section teaches.

---

## Section 3: Old Debates in New Costumes

Most of the concerns raised across this series were not born with AI. They are older arguments in new technical dress — which is steadying in one way, because the reader's existing frameworks still apply, and unsettling in another, because those older arguments were never actually settled. Each pairing below points at a debate the reader may already know, notes what AI genuinely changes about it, and then stops. The stopping is deliberate. The question worth asking is left for the reader to form and carry, not handed over pre-packaged; a borrowed question is easy to nod at and forget, while one you phrase yourself tends to stay.

**Opacity.** Courts have long worked with things they cannot fully see into: expert testimony a jury cannot independently verify, evidence shielded as trade secret, proprietary forensic instruments. AI adds a genuinely new wrinkle — with these systems, even the people who built them often cannot fully explain a particular output, so there may be no knowledgeable witness to put on the stand at all. Sit with what an adversarial process, built around examinable witnesses, does with that.

**The evaluation problem.** Standardized testing has argued for a century about what a score really measures, about teaching to the test, about gaming. AI benchmarks replay every part of that quarrel, only faster: scores saturate, test material leaks into training data, and any single benchmark captures a narrow slice — all on a cycle of months, not generations. Consider what it would take for a quality claim resting on a benchmark to be genuinely examinable.

**Rental economics.** Fights over first-sale doctrine, software licensing, and e-book access already established that "buying" something digital is often renting a permission that can be revoked. AI adds a quieter twist: the rented thing can change what it does while keeping the same name, and when a version is retired it takes with it the ability to reproduce anything that depended on it. Weigh what that does to work — research, evidence — built on a model that no longer exists.

**Automated adverse decisions.** Credit scoring, security watch-lists, and automated benefit denials posed the recourse problem decades ago: an opaque system decides, and the person affected gets no explanation and no real forum. AI adds the attribution blur from the durable-limitations cluster — the material used against a person may itself be partly machine-generated, and the system often cannot cleanly separate what the user wrote from what it wrote. Think about where the burden should fall when both the accusation and the person's defense rest on things no one can fully verify.

**Re-identification.** The lesson that "anonymized" data can be turned back into named individuals predates modern AI — the Netflix Prize de-anonymization made it vivid years ago. What AI changes is the raw material required: identity can now be inferred from ordinary writing at scale, not only from structured records. And the very same tracing power is demanded as a remedy — creators asking whether their work sits in a training set — and feared as a threat to privacy. Notice that these are one capability, not two, and follow where that leads.

**Copying that cannot be technically prevented.** Unauthorized copying of digital text and music was never actually stopped by technical locks; the law ended up governing an act it could not physically prevent. Distillation — training one model on another's output — looks like it belongs to the same family: defenses applied at the level of the output are an active research topic with nothing settled. Ask what decades of regulating copying-that-can't-be-blocked taught, and how much of it survives when the copier is a training process rather than a person.

**Concentration.** Railroads, telephone networks, and platform gatekeepers each produced a version of the same argument about essential facilities: what is owed when a few actors control infrastructure everyone else needs? Frontier AI concentrates three such inputs at once — computing power, data, and the channels of distribution. Turn over which of those three, if any, the existing legal tools already fit, and which would need something genuinely new.

**Misplaced trust in a fluent interface.** Worries about parasocial attachment and persuasive media are generations old. What AI adds is an interface fluent in the second person: it makes its mistakes persuasively, and it makes them to *you* in particular. Consider whether the old remedies — a warning label, a duty to disclose — were ever built to compete with a product speaking in its own confident voice, directly to the individual.

---

## Closing: The Toolkit, Now Earned

Section 1 offered a way to meet a new word: set the impressive part aside, ask what the word plainly points at and why it appeared, and notice what the fashionable use suggests but has not shown. Section 2 offered a way to read a launch: run the six questions across it and pay as much attention to the silences as to the claims. Section 3 offered a way to place a concern: find the older debate it continues, mark precisely what AI changes, and let the question it raises stay open in your own words.

The full toolkit, once more:

*For a new term:*

1. What plain thing does the word point at, once the impressive part is set aside?
2. Why did it appear — what does it let a system do?
3. What does the fashionable use suggest that has not actually been shown?

*For a product announcement:*

1. What is the base model?
2. What was it trained on?
3. What is bolted around it?
4. What can't it know, and what might it hallucinate — about facts, or about its own work?
5. Who controls it?
6. Who can contest what it decides?

*For an old argument in new dress:* find the older debate it continues, mark what AI changes, and hold the question open.

Every product, benchmark, and lawsuit named in this series will expire. These questions are the part built to keep.
