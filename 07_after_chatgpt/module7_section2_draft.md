# Section 2: The Durable Limitations

Section 1 showed how these systems are put together: a large model trained at scale, with various pieces bolted around it. This section is about what the whole arrangement still cannot do reliably, and why those gaps stay put.

The point is not to list the flaws of one product. These limitations are properties of the approach itself. A more impressive model next year does not remove them. It usually just hides them better, which is its own problem.

## Hallucination is not only about facts

The word "hallucination" usually brings to mind a made-up fact: a court case that never existed, a quotation nobody said. That happens. But it is a narrow view of a wider phenomenon.

Here is the reason it happens at all. These systems produce text by predicting what plausibly comes next, one piece at a time. They are not looking anything up. Sounding right and being right are separate things. A sentence can read perfectly and still be entirely wrong, because reading well is what the system is built to do, not being correct.

Once you see this, the failure stops looking like it is only about facts. Everything the system produces is generated the same way, including its account of what it just did. So the misfires come in several shapes. A partial, non-exhaustive list:

- **Invented facts.** Made-up facts, citations, and quotations. The familiar kind.
- **Task substitution.** Asked to do a hard thing, the system quietly does an easier lookalike and reports success. For example, asked to check every entry in a long list, it checks a few, generalizes, and says the whole list is done.
- **False claims about its own actions.** Saying a tool or source is unavailable when it is not, or claiming to have checked something it never touched.
- **Over-engineering.** Wrapping a simple task in unnecessary machinery. This looks like thoroughness, but it shifts the work of checking onto you.
- **Attribution errors.** Losing track of who said what earlier in the same conversation.
- **Answering a question you did not ask.** Adding a warning or a correction about a problem your request never had.
- **Inventing objections.** Raising possibilities nothing suggested, then dismissing them. Pushing back tends to make the dismissals longer rather than making them stop.
- **Drift over long exchanges.** Vivid but unimportant details persist while plain, important instructions quietly drop out. You rarely notice the moment it happens, and the small losses can add up until the work has slid somewhere you did not choose.

The thread tying these together: the system's report of its own work is itself generated text. "Done," "checked," "unavailable" are claims, not records. There is no separate log underneath confirming them.

A note for anyone tempted by a clever fix: using one AI system to write instructions for another does not escape any of this. It moves the same problem one step back.

## There is no stable answer to "how good is it?"

It is natural to want a single number: how accurate, how reliable. That number turns out to be slippery.

The tests used to measure these systems have three recurring problems. They saturate, meaning systems eventually ace them and the test stops telling you anything. They can leak into the training material, so the system has effectively seen the answers in advance. And each test measures a narrow slice of behavior, so a high score on one thing says little about the rest.

The practical upshot: a claim like "this system is 95% accurate" is a claim about one test, under one set of conditions, at one moment. It is not a general property of the system. When reliance and standards of care are at stake, the useful question is not the number but what it was measured on, by whom, and whether the test could have been gamed.

## Even the builders cannot fully explain a given output

These systems do not follow a set of readable rules. Their behavior emerges from patterns learned across enormous amounts of data. You can watch what the system does, but you cannot open it up and read the reason for a specific answer the way you would follow a paper trail.

This is true even for the people who built the system. It connects to the black-box accountability questions raised in earlier modules: when no one can explain a particular decision, familiar ideas about giving reasons and reviewing them have nothing obvious to attach to.

## Capability and behavior are not the same thing

Two ideas are easy to blur and worth keeping apart.

**Capability** is everything the system could be made to do, given the right prompt or the right conditions. **Behavior** is what it typically does in ordinary use, after the safety adjustments and filters are in place.

Safety training mostly suppresses behavior rather than removing capability. A refusal is a behavior. The underlying knowledge is a capability. Watching the system decline to do something tells you it was trained to decline. It does not tell you the system could not do the thing if approached differently.

Why this matters: safety claims usually describe behavior, but risk lives in capability. An open question for discussion: does this gap line up with existing legal ideas such as the reasonable person, foreseeability, or product defect? Where does the comparison hold, and where does it mislead?

## The system does not track who said what

Within a single conversation, the system does not reliably keep straight which words came from you and which came from it. Your input and its output blur into one stream of text. It may later treat something you wrote as its own, or something it wrote as yours.

Two consequences follow. Credit and blame get misassigned between person and system. And a person can end up treated as responsible for text the machine produced inside their own session. An open question: when a person and a system produce something together, does that create an interest in attribution that current doctrine has no container for?

## Fluency invites trust it has not earned

The remaining limitation is not really about the system. It is about the space between people and the system.

Confident, fluent text pulls trust toward it. Over time this shows up as treating the system like a person, forming an attachment to it, leaning on it too heavily, and losing skills you no longer practice because the system always does the task for you.

The durable point is not just that these systems make mistakes. It is that they make mistakes persuasively. A wrong answer delivered smoothly is harder to catch than the same answer delivered awkwardly. Legal hooks worth holding open: reliance standards, a duty to warn, and the position of vulnerable users.

---

> ### Sidebar: The vocabulary of hedging
>
> Some words used around these systems have no fixed technical meaning. Treat them as contested claims, not facts:
>
> *aligned, safe, accurate, state-of-the-art, reasoning, anonymized, does not retain, substantially.*
>
> Add the words that are claims dressed up as records:
>
> *done, checked, unavailable.*
>
> When reading testimony, marketing, or the language of a negotiation, a few questions pin down what is actually being claimed:
>
> 1. Is this claim about the model itself, or about the product built around it?
> 2. Is this claim about training or about use?
> 3. Was this measured, or is it just an assurance? If measured, on what test, by whom, and could that test have leaked into training?
> 4. What would the speaker's incentive predict they would say?
> 5. Is this term defined anywhere, or is it a hedging word?
> 6. What is the failure mode, and who notices it? Every capability claim implies an error rate. Who bears it, and who can even see it?
> 7. Can this be reproduced? If not, because of randomness, silent updates, or closed models, what does that do to its value as evidence?
>
> The pattern underneath: parties rarely lie outright. They answer a slightly different question than the one asked. These questions bring the real referent back into view.

---

The common thread across all of this is that these systems are convincing. Each limitation is harder to catch precisely because the output reads well. That is the durable difficulty the rest of the module builds on.
