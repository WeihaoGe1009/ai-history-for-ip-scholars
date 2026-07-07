# Module 7: AI After ChatGPT — Durable Concepts for Legal Readers

## Purpose

The closing module of the series. Primarily reading and discussion; no code demo required. The goal is not to catalog current techniques but to equip readers — IP scholars, legislators, legal researchers — with durable concepts and a self-learning template, so that any future AI announcement can be quickly understood at an ELI5 level, approached with appropriate caution about limitations and hallucination, and examined for collateral legal concerns.

## Cluster 1: How the System Is Assembled

- **Scale as the engine**
  - Capability now comes from data volume and compute, not explicit programming.
  - Every "new fancy model" is still this. Legal hook: capability without design intent complicates foreseeability.
- **From completion to assistant**
  - Base models predict text; instruction tuning and human feedback shape behavior.
  - Durable distinction: what a model *can* do vs. what it is *trained to prefer* doing. Legal hook: whose preferences, and who is accountable for them?
- **The scaffold family**
  - The bare model can't do X reliably, so something is bolted around it. Today's instances (examples, not canon):
    - Chain-of-thought: unreliable at multi-step problems → make it show intermediate work (reasoning scaffold).
    - Retrieval (RAG): can't know recent/private facts → fetch documents and let it read them first (knowledge scaffold).
    - Tools / skills / plugins: can't do everything → package specialized capabilities it can call (capability scaffold).
    - Agents: can only emit text → give it tools and let it loop: act, observe, act again (action scaffold).
- **The three-question template** (the self-learning tool)
  1. What inadequacy does it patch?
  2. What new concern does it expose? (e.g., retrieval → poisoned documents, copyright in retrieved corpora; agents → liability for acts, not words; chain-of-thought → discoverable reasoning records?)
  3. Where does it sit in the pipeline? (before the model / inside the prompt / after the output / looping around it — a crude but durable layout vocabulary for patent claims analysis)
- **Environmental cost**
  - Compute-hungry training and inference as the shadow side of scale. Legal hooks: disclosure obligations, siting/permitting, externalities.

## Cluster 2: The Durable Limitations

- **Hallucination is not limited to facts**
  - Generation is probabilistic continuation, not database lookup; fluency and truth are uncorrelated.
  - Take-home message: there are many sorts of hallucination, not only factual ones. A simple (non-exhaustive) list:
    - Factual hallucination: invented facts, citations, quotations.
    - Task substitution: asked to do X, the system does an easier X′ and reports success.
    - False capability claims: stating a tool, source, or resource is unavailable when it is not — or claiming to have checked something it never touched.
    - Over-engineering: wrapping a simple task in unnecessary structure, consuming resources and shifting review burden to humans.
    - Attribution errors: misremembering who contributed what within the conversation.
    - Unrequested framing: answering a question that wasn't asked alongside the one that was — cautionary or corrective asides addressing intent or flaws nothing in the input exhibits.
    - Scope invention: raising and dismissing possibilities nothing in the input suggested; user pushback tends to make the dismissal more visible (growing preambles restating constraints) rather than making it stop.
    - Salience drift: across long or iterative interactions, vivid but irrelevant details persist while structurally important but plain instructions get quietly dropped; the compounding effect can invisibly redirect a project's trajectory.
  - The unifying idea: the system's report of its own work is itself generated text — "done," "checked," "unavailable" are claims, not logs.
  - Note on meta-prompting: using one AI to generate prompts for another does not escape these failures; it relocates them one layer back.
- **The evaluation problem**
  - "How good is it?" has no stable answer; benchmarks saturate, leak into training data, and measure narrow slices. Legal hook: standards of care and reliance.
- **Opacity**
  - Even builders cannot fully explain specific outputs. Connects to black-box accountability themes from earlier reading.
- **Capability vs. behavior**
  - Capability: everything a system can be made to do under some prompt or condition. Behavior: what it typically does under normal use, after safety tuning and filters.
  - Safety training mostly suppresses rather than removes. Refusal is a behavior; knowledge is a capability — testing the first tells little about the second.
  - Legal hooks: safety claims usually describe behavior while risk lives in capability; foreseeability may turn on the capability envelope the developer knows (or should know). Discussion prompt: does the capability/behavior gap map onto existing doctrine — reasonable person, foreseeability, product defect? Where does the analogy hold, and where does it mislead?
- **Provenance blindness inside the conversation**
  - The system does not reliably track who contributed what within a session; input and output blur into one stream.
  - Consequences: attribution (credit and blame misassigned between user and model) and accountability (users held responsible for machine-generated content in their own sessions). Open question: does human–AI co-production create attribution interests existing doctrine has no vessel for?
- **Psychological effects**
  - Anthropomorphism, parasocial attachment, over-reliance, deskilling.
  - A durable limitation of the human–AI *interface*: fluency triggers misplaced trust. The danger is not just that systems err, but that they err persuasively. Legal hooks: reliance standards, duty to warn, vulnerable users.

### Boxed sidebar: The Vocabulary of Hedging

Terms with no fixed technical meaning, to be treated as contested claims rather than facts: "aligned," "safe," "accurate," "state-of-the-art," "reasoning," "anonymized," "does not retain," "substantially." Add words that are claims wearing the clothes of logs: "done," "checked," "unavailable."

Companion self-questions for interpreting testimony and negotiation language:

1. Is this claim about the model, or the product around it?
2. Is this claim about training or inference?
3. Was this measured, or is it an assurance? If measured — on what benchmark, by whom, and could the benchmark have leaked into training?
4. What would the speaker's incentive predict they would say?
5. Is this term defined anywhere, or is it a hedging word?
6. What is the failure mode, and who detects it? Every capability claim implies an error rate; who bears it, and who can even see it?
7. Can this be reproduced? If not — sampling, silent updates, closed weights — what does that do to it as evidence?

The uniting pattern: parties rarely lie outright; they answer a slightly different question than the one asked. These questions pin the referent.

## Cluster 3: Who Controls the Stack, Who Bears the Cost

### Control

- **Distillation** — capability copied model-to-model; derivative chains of fine-tuned models. Discussion case: disputes where the alleged victim is itself accused of extracting from the training-data commons. Keep the concept durable; treat specific lawsuits as perishable examples.
- **Monopoly / concentration** — few actors can afford frontier training; chokepoints in compute, data, and distribution. Open questions in antitrust and essential-facilities framing.
- **Rental economics** — models accessed by subscription/API; capability can be revoked, repriced, or silently changed. Nothing owned, nothing stable. Legal hooks: first-sale doctrine's irrelevance, contract vs. property framing, preservation/archival problems.
  - **Research reproducibility on model retirement**: when a retired model underpinned published research or litigation evidence, the finding becomes unverifiable; no archive requirement exists.
- **Open vs. closed release** — a governance fault line shaping liability, research access, and safety debates.
- **Prompts as IP-relevant entities**
  - U.S. Copyright Office position (Part 2 report, Jan. 2025): prompts alone do not confer authorship over outputs — the gap between prompt and output breaks the chain of human creative control. A sufficiently elaborate prompt may be copyrightable as a text, but owning the prompt does not extend into the output. Two questions frequently conflated in public debate.
  - Open questions: where on the control spectrum does authorship attach (selection/arrangement, substantial modification, hundreds of refinement iterations)? Note the internal echo: authorship analysis presumes clean separation of human and machine contributions — exactly what provenance blindness undermines.
  - Comparative wrinkle: other jurisdictions diverge (UK computer-generated works provision, Chinese case law), so the U.S. position is not the global answer.
  - Commercial reality: prompts are often protected as trade secrets precisely because copyright protection is thin and output ownership uncertain.
  - Date-stamp any specific statements; litigation and further guidance are ongoing.

### Recourse

- **Power imbalance (contract side)** — account suspension, non-refundable fees, quality degradation; users hold no property-based claim, only what the terms of service grant.
- **Automated adverse decisions without accessible appeal (detection side)** — being *evaluated by* an opaque model rather than *using* one: false-positive fraud flags, AI-detector accusations against non-native speakers. The harmed party often has no contract to invoke, no explanation to request, and no clear forum for appeal.
  - Worked hypothetical (deliberately abstract): a user instructs the system to keep its output within platform rules; the moderation layer, unable to distinguish input from output, sanctions the account. The regulated act was generation, but the observed object was the whole conversation. Three distinct failures: attribution (input/output blur), category (discussing in input treated as generating), recourse (appeal goes to the same opaque pipeline, and the evidence was partly authored by the accusing system).
  - Counterweight: the user's mitigation theory — treating the AI as a contained, private audience — is itself contested. A sycophantic system may validate and escalate rather than contain, and removing human audiences removes social friction. Discussion prompt: when both the enforcement mechanism and the compliance strategy rest on unverified assumptions, where should the burden sit?

## Unifying Framing Device: A Reader's Toolkit for the Next Announcement

Reprises the three-question template and extends it. Questions to ask of any new AI system:

1. What is the base model?
2. What was it trained on?
3. What is bolted around it? (Which scaffold type?)
4. What can't it know? What might it hallucinate — about facts, or about its own work?
5. Who controls it?
6. Who can contest what it decides?

The module closes the loop: the toolkit is the deliverable; the clusters are its justification.

### Note: on prompting advice

The discipline of prompt engineering — explicit task specification, structure, examples, iterative testing — is real and durable; it is essentially requirements specification. But any specific technique within it ("this exact template," "this phrasing boosts accuracy") is an empirical, time-stamped claim tied to a particular model generation, and can go stale silently. Treat prompting advice with the same skepticism as any behavior claim about a moving target.

## Cross-Module Notes

- Training vs. inference: covered in Module 4 optional reading.
- Weights vs. architecture vs. data: add a paragraph to Module 2, where heat maps and printed model architectures already illustrate weights and structure.
- Determinism vs. sampling: covered in Module 3 (Markov model vs. searching demo).

## Format Notes

- Reading and discussion module; concepts posed as open legal questions, not doctrinal conclusions.
- Name today's techniques as examples of durable types, not as canon.
- Keep lists simple and non-exhaustive; the goal is awareness, not completeness.
- No code demo planned; optional light illustrative material only if it adds durable value.
