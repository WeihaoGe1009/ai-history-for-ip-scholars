# GenAI foundations for law and policy: four building blocks

**The most important thing a legal professional needs to understand about generative AI in 2026 is not any single technique — it is that AI reliability is a systems problem, not a switch.** Hallucination cannot be "solved" by one fix; it is managed through layered defenses. AI agents are not autonomous persons; they are tools that amplify both creative power and legal ambiguity. And prompt engineering has evolved from a craft into an engineering discipline. Across all of this, certain conceptual anchors remain stable even as specific tools churn every year. This module walks through each of these four pillars at a depth suitable for legal professionals, legislators, and content creators who need to reason about AI without becoming computer scientists.

---

## 1. How the field has fought hallucination since GPT-1

AI hallucination — when a model generates confident, fluent text that is factually wrong or entirely fabricated — is not a minor glitch. It has produced fabricated legal citations (*Mata v. Avianca*, 2023), invented medical advice, and false claims about real people. Understanding the milestones in reducing hallucination reveals a critical insight: **each technique addresses a different root cause, and none makes the others obsolete.** They stack like layers of automotive safety — seatbelts did not become unnecessary when airbags arrived.

### The knowledge gap: retrieval-augmented generation (2020)

The first major hallucination-reduction technique, **Retrieval-Augmented Generation (RAG)**, was introduced by Lewis et al. at Facebook AI Research in 2020. The idea is straightforward: instead of forcing the model to answer from memory alone, the system first searches an external knowledge base — a document library, legal database, or the open web — and feeds the relevant passages to the model before it generates a response. Think of it as allowing a witness to consult actual case files rather than testifying from memory.

RAG solved the **knowledge layer** of hallucination: models trained on static data inevitably lack information about events after their training cutoff, niche topics, and rapidly changing facts. A 2025 IEEE study found that RAG-based grounding reduces technical errors by approximately **75%** in specialized fields like engineering and medicine. Even as context windows have expanded to 200,000+ tokens, RAG remains essential because no window can hold all relevant knowledge, and RAG provides citable, verifiable sources — a critical feature for legal and regulatory settings.

### Behavioral alignment: RLHF and its descendants (2022)

In January 2022, OpenAI published the InstructGPT paper, introducing **Reinforcement Learning from Human Feedback (RLHF)**. The concept: after initial training, human evaluators rank the model's responses from best to worst. These rankings train a scoring system (a "reward model"), and the language model is further trained to produce outputs that score highly. When applied at scale in **ChatGPT** (November 2022), the results were dramatic — human raters preferred the small InstructGPT model over the vastly larger GPT-3 in most comparisons, and the model hallucinated less and produced less toxic content.

RLHF addresses the **behavioral alignment layer**. A model can have access to perfect knowledge (via RAG) but still present information misleadingly if its default behavior rewards fluency over truth. RLHF teaches the model the norms of honest communication. By 2025, an estimated **70% of enterprises** used RLHF or its derivatives for AI alignment. Its key successor, **Direct Preference Optimization (DPO)**, introduced by Stanford researchers in May 2023, achieves comparable alignment with far less computational cost — democratizing preference-based training for open-source projects and smaller organizations. DPO and its variants (KTO, IPO, ORPO) are now the dominant alignment methods for open-source models.

An important caveat for legal audiences: RLHF can create a subtler problem called **sycophancy** — models learn to produce confident, agreeable answers because humans prefer confidence, even when the correct response is "I don't know." This is why RLHF alone is insufficient.

### Reasoning quality: chain-of-thought prompting (2022)

Also in January 2022, Google researchers published the chain-of-thought (CoT) technique: instead of asking the model to jump to an answer, you instruct it to "think step by step." By articulating intermediate reasoning, the model reduces logical leaps and makes errors visible. On math benchmarks, CoT with a large model surpassed even fine-tuned GPT-3 with a separate verification system.

CoT addresses the **reasoning layer**. Even a model with perfect knowledge and good behavioral alignment can produce wrong answers if it reasons poorly about what it knows — the equivalent of a well-intentioned analyst who makes a computational error. CoT remains free to use (no retraining needed) and universally applicable, which is why OpenAI's "o1" reasoning models (September 2024) essentially built CoT directly into the model's architecture. However, a June 2025 study found that while CoT reduces hallucination frequency, it can make remaining errors harder to detect automatically — a tradeoff with regulatory implications.

### Principled governance: Constitutional AI (December 2022)

Anthropic introduced **Constitutional AI (CAI)** as an alternative to pure RLHF. Instead of relying on thousands of human raters whose collective preferences are opaque, CAI gives the model a written set of principles — a "constitution" — and trains the model to critique and revise its own responses against those principles. The constitution is a public document (Anthropic's draws from sources including the UN Declaration of Human Rights).

CAI solves the **governance layer**: it makes AI values explicit and inspectable. For regulators, this is significant — you can audit the principles that guided the model's training, unlike RLHF where human preferences are statistically aggregated and impossible to individually inspect. In January 2026, Anthropic updated Claude's constitution with more nuanced guidelines, and variants like **Collective Constitutional AI** now incorporate public democratic input. CAI also solved a practical problem: RLHF models often became overly cautious ("I can't help with that"), while CAI models were simultaneously more helpful *and* more careful.

### Capability boundaries: tool use and grounding (2023)

**Toolformer** (Meta AI, February 2023) and subsequent implementations like ChatGPT Plugins showed that models can learn to call external tools — calculators, search engines, databases, code interpreters — when they recognize their internal knowledge is insufficient. Before tool use, asking a model to multiply large numbers or report today's stock price would reliably produce hallucinations. With a calculator or search tool, these entire classes of error disappear.

Tool use addresses the **capability boundary layer**: recognizing what the model fundamentally cannot do internally and outsourcing those tasks to reliable systems. This becomes even more critical as models are deployed in agentic workflows (discussed in Section 2), where autonomous multi-step operations require real-time factual grounding.

### Post-2023: reasoning models and a humbling discovery

OpenAI's **o1 reasoning models** (September 2024) represented a paradigm shift — the model spends significant "thinking time" at inference, decomposing problems before responding. The o3-mini variant achieved a remarkably low **0.8% hallucination rate** on certain benchmarks. But a humbling finding followed: newer reasoning models (o3, o4-mini) showed *increased* hallucination on biographical questions, with o4-mini hallucinating **48%** of the time on PersonQA. A nonprofit lab, Transluce, found that o3 fabricated claims about actions it supposedly took (like claiming it ran code when it hadn't).

This counterintuitive result — that better reasoning can coexist with worse factual accuracy — confirms the layered defense thesis. **Reasoning capabilities and factual accuracy are distinct qualities**, and a model can improve at one while declining at the other. OpenAI's own 2025 theoretical paper by Kalai et al. argued that hallucination is a statistical inevitability of next-word prediction and will never reach zero. The practical response is calibration (models expressing uncertainty) and abstention (models declining to answer when unsure).

### The layered defense model

For policymakers, the central takeaway is captured in this framework:

- **RAG** gives the model access to verified, current information (the knowledge layer)
- **RLHF/DPO** trains the model's behavioral tendencies toward honesty (the alignment layer)
- **Chain-of-thought** forces structured reasoning to reduce logical errors (the reasoning layer)
- **Constitutional AI** makes the model's guiding values explicit and auditable (the governance layer)
- **Tool use** outsources tasks the model cannot reliably perform internally (the capability layer)
- **Benchmarks** (TruthfulQA, HaluEval, SimpleQA) measure progress (the measurement layer)
- **Regulation** (EU AI Act, state laws) creates external accountability (the legal layer)

Requiring "zero hallucination" is like requiring zero automotive accidents. The regulatory goal should be comprehensive risk management with multiple redundant safety layers, clear accountability structures, and measurable standards — which is the trajectory the EU AI Act's risk-based approach already follows.

---

## 2. Agent-based LLMs and their collision with IP law

### What makes an "agent" different from a chatbot

A regular LLM call is like asking a librarian a single question and getting a single answer. An **AI agent** is like hiring a research assistant who can plan a multi-step strategy, use tools (web browsers, calculators, databases), make intermediate decisions, loop back to correct errors, and persist memory across sessions — all with minimal human oversight at each step.

Technically, agents add four capabilities beyond a basic model call: **planning** (decomposing goals into subtasks), **tool use** (calling APIs, browsing the web, executing code), **memory** (maintaining state across steps and sessions), and **autonomy** (deciding what to do next without human approval at each step). They range from copilot agents that augment human decisions (like GitHub Copilot) to autopilot agents that act independently (like Devin for coding) to multi-agent systems where specialized agents collaborate on complex tasks.

### The agentic landscape in early 2026

The global AI agents market reached approximately **$7.6–7.8 billion in 2025**, projected to exceed $10.9 billion in 2026. Gartner forecasts that **40% of enterprise applications** will embed task-specific AI agents by the end of 2026, up from less than 5% in 2025. However, only about 11% of organizations currently run agents in production, revealing a significant gap between experimentation and deployment.

The technical infrastructure has matured rapidly. **Anthropic's Model Context Protocol (MCP)** — donated to the Linux Foundation in December 2025 — has become the de facto standard for how agents connect to external tools, with support from OpenAI, Google, and Microsoft. Google's **Agent-to-Agent (A2A) protocol** enables agents built on different frameworks to discover and collaborate with each other. The leading orchestration frameworks include **LangGraph** (graph-based workflows for complex stateful systems), **CrewAI** (role-based agent teams, claimed adoption by 60%+ of Fortune 500), and the **Microsoft Agent Framework** (merging AutoGen and Semantic Kernel, with enterprise-grade Azure integration). Gartner warns, however, that only about **130 of thousands** of claimed agentic AI vendors offer legitimate agent technology — "agent washing" is widespread.

### Where agents collide with intellectual property law

The intersection of autonomous AI agents with IP law creates four distinct zones of legal ambiguity.

**Autonomous content creation and ownership.** When an AI agent creates content without meaningful human creative control at each step, who owns the result? In the United States, this question is now effectively settled at the highest level. **Thaler v. Perlmutter** — where an inventor sought copyright for art autonomously generated by his AI system — was affirmed by the D.C. Circuit in March 2025, denied rehearing, and the **Supreme Court denied certiorari on March 2, 2026**. Human authorship is a "bedrock requirement" of copyright. The U.S. Copyright Office's Part 2 guidance (January 2025) further clarified that **prompts alone do not provide sufficient control** to make users the authors of AI output. However, human-authored elements perceptible in AI-assisted output remain protectable, and creative selection, coordination, or modification of AI material can be copyrightable on a case-by-case basis. Internationally, China's Beijing Internet Court has taken a more permissive stance (recognizing copyright for AI-generated images reflecting human intellectual effort), while Japan remains the most permissive jurisdiction for AI training on copyrighted works.

**Web scraping agents and copyright.** Autonomous agents that browse and scrape the web raise intensifying copyright questions. The **NYT v. OpenAI** litigation (filed December 2023) is the bellwether case; discovery is ongoing, and in March 2026 the court ordered production of 78 million additional logs. **Bartz v. Anthropic** settled for **$1.5 billion** in August 2025 — the largest copyright recovery in U.S. history — with the judge distinguishing between lawfully obtained training data (potentially fair use) and pirated data (not fair use). A critical ruling in **Ziff Davis v. OpenAI** (2025) held that robots.txt is not a "technological measure" under the DMCA — it is more like "a sign than a barrier." The proposed **AI Accountability for Publishers Act** (draft unveiled February 2026) would make robots.txt compliance legally enforceable, override fair use for scraping, and impose treble damages. Under the EU AI Act (provisions effective August 2, 2026), general-purpose AI providers must publish structured summaries of training data and respect opt-outs under the EU Copyright Directive.

**Agency law and AI acting on behalf of humans.** When an agent acts as a proxy for a human creator — negotiating licenses, publishing content, or making creative decisions — traditional agency law concepts apply unevenly. The principal-agent relationship requires a principal who assents, an agent who acts on the principal's behalf, and the principal's right to control. **Electronic agents already have legal standing** under the Uniform Electronic Transactions Act and the E-SIGN Act for forming contracts. But as Yale's Jack Balkin argues, "the law of AI is the law of risky agents without intentions" — people should not obtain a reduced duty of care by substituting AI for human agents. When Amazon alleged that Perplexity's Comet browser agent violated Amazon's terms of service by autonomously shopping, it highlighted the tension between agent autonomy and platform terms. DLA Piper warns that companies "may find themselves strictly liable for all AI agent conduct, whether or not predicted or intended."

**Liability when an agent infringes.** The liability chain for AI-generated copyright infringement is multi-layered. Potential liable parties include the training dataset creators, model trainers (as Anthropic's $1.5 billion settlement confirms), fine-tuners, deployers, and end users. Key theories in active litigation include direct infringement (NYT alleges OpenAI outputs are substantially similar to its articles), contributory infringement (claims against Microsoft survived motions to dismiss), and inducement (claims in *Andersen v. Stability AI* survived). Under emerging EU jurisprudence, if infringement stems from user input, the user bears primary liability; if from systemic training defects, the provider does. **Colorado's AI Act** (effective June 2026) imposes a duty of reasonable care on both developers and deployers, with penalties up to $20,000 per violation.

### What grassroots creators need to know

AI agents are transforming independent creative workflows — research-to-script-to-edit pipelines for video creators, automated music composition via tools like Suno and Udio, and no-code agent platforms for small businesses. But legal risks are real and specific. Content generated primarily by AI agents is likely **uncopyrightable** in the U.S., meaning competitors can freely copy it. YouTube now requires mandatory disclosure of AI-generated realistic content and has begun demonetizing channels producing mass AI content without demonstrated human creativity — the distinction being AI as a *tool* (allowed) versus AI as the *entire creative process* (not monetizable). New York's synthetic performer law (effective June 2026) requires disclosure of AI-generated human likenesses in advertisements. Creators should document their human creative contributions meticulously, verify that AI generation tools use licensed training data, and understand that they remain legally responsible for everything their AI agents produce.

---

## 3. From crafting prompts to designing prompting systems

### What changed and why it matters

In 2022–2023, "prompt engineering" meant the craft of writing better natural-language instructions — role-playing prompts, few-shot examples, clever phrasing tricks. LinkedIn reported a **434% increase** in prompt engineer job postings. By 2025, however, Fast Company reported the standalone "prompt engineer" title had "all but disappeared," with 68% of firms providing prompt skills as standard training across all roles. The skill became more valuable; the siloed job became less necessary.

The deeper shift was conceptual: from **"write a better prompt"** to **"design a prompting system."** As Andrej Karpathy framed it in June 2025, the LLM is a "CPU," the context window is "RAM," and the practitioner's job is to be the "operating system" — loading working memory with exactly the right information for each task. The field now prefers terms like **"context engineering"** or **"prompt orchestration"** — reflecting that modern AI systems involve chained sequences of prompts, branching logic, tool calls, and self-correction loops managed programmatically. Microsoft released **POML (Prompt Orchestration Markup Language)** in August 2025, and Stanford's SPEAR framework (January 2026) treats prompts as "first-class entities" with executable prompt algebra.

This shift matters for legal and policy audiences because it fundamentally changes the accountability question. When an AI system's behavior was determined by a single prompt, liability was relatively traceable. In an orchestrated system with dozens of chained prompts, multiple agents, and self-reflection loops, the question "who is responsible for this output?" becomes far more complex.

### The key techniques in plain language

**Chain-of-Thought (CoT)** asks the model to show its reasoning step-by-step, like a student showing work on a math exam. It remains the most widely used advanced prompting technique and has been built directly into reasoning-focused models like OpenAI's o1 series. Its variant **Self-Consistency** generates multiple reasoning chains and selects the most common answer, improving accuracy by 6–18%.

**ReAct (Reasoning + Acting)**, introduced by Yao et al. in 2022, alternates between thinking and doing — the model reasons about what it needs, takes an action (like searching the web), observes the result, and reasons again. ReAct is the conceptual bridge between prompting techniques and AI agents; it is embedded as a standard pattern in every major agent framework.

**Tree-of-Thought (ToT)**, from Yao et al. in 2023, extends chain-of-thought by exploring multiple reasoning paths simultaneously — like branches of a decision tree — evaluating which are promising and backtracking from dead ends. It excels at problems requiring exploration or creative planning but is more computationally expensive.

**Constitutional AI prompting** has the model self-critique against explicit written principles. Unlike external human feedback, the evaluation criteria are transparent and auditable — a property with obvious regulatory appeal.

**Meta-prompting and self-reflection** techniques like **Reflexion** (Shinn et al., 2023) create loops where the model evaluates its own output, produces a verbal self-critique, stores it in memory, and uses that reflection to improve on the next attempt. Research confirms that LLM agents "significantly improve their problem-solving performance through self-reflection" (p < 0.001).

More recent innovations include **Graph-of-Thought** (2024), which models reasoning as an arbitrary graph where ideas can merge and branch — increasing quality by **62%** over Tree-of-Thought while reducing costs by over 31%. **Chain-of-Draft** (2025) achieves comparable accuracy to full chain-of-thought using roughly five words per reasoning step, dramatically reducing cost and latency.

### The orchestration framework landscape

The current ecosystem has consolidated around several tiers. **LangGraph** (the successor to LangChain's agent features) is the most battle-tested framework for complex, stateful production systems, used by an estimated 600–800 companies in production. **DSPy**, from Stanford, represents a fundamentally different philosophy: instead of writing prompts, developers write modular Python programs and let DSPy's compiler automatically optimize the prompts — a DSPy-optimized prompt generated in 10 minutes significantly outperformed a human-crafted prompt that took 20 hours. **CrewAI** offers role-based agent teams with the fastest time-to-prototype and now supports no-code YAML configuration. The **Microsoft Agent Framework** (merging AutoGen with Semantic Kernel, GA expected Q1 2026) targets enterprises in the Azure ecosystem with compliance guarantees and production SLAs. **OpenAI's Agents SDK** (March 2025) and **Anthropic's MCP** provide the platform-specific tools and connectivity standards, respectively.

For non-technical creators, the practical reality is that the most powerful frameworks still require programming. However, accessible tiers are emerging: CrewAI's YAML-driven configuration, no-code platforms like Zapier and n8n with AI integrations, and consumer-facing tools like ChatGPT's Custom GPTs and Claude Projects that allow non-developers to create specialized AI assistants with persistent context.

---

## 4. Durable concepts versus fast-moving details

Across everything above, some ideas will remain relevant for a decade; others will be obsolete in 18 months. For legal scholars and policymakers investing in AI literacy, the distinction is critical. What follows identifies the stable conceptual anchors worth committing to memory and the implementation details worth tracking but not memorizing.

### Five concepts that will still matter in 2035

**The layered defense model for AI reliability.** The insight that hallucination has multiple independent root causes — knowledge gaps, reasoning errors, misaligned incentives, capability limitations — and that each requires a different mitigation is as durable as the Swiss cheese model in safety engineering. Specific techniques will evolve, but the principle that no single fix is sufficient is permanent. Any future regulation that demands "hallucination-free AI" will be as misguided as demanding "accident-free driving" — the proper framework is layered risk management.

**The human authorship requirement for copyright.** With the Supreme Court declining to hear *Thaler v. Perlmutter* in March 2026, the principle that purely AI-generated works cannot be copyrighted is settled U.S. law for the foreseeable future. The more nuanced question — exactly how much human contribution makes an AI-assisted work copyrightable — will evolve case by case, but the foundational principle is stable. Legal professionals should internalize this as a structural feature of copyright law, not a temporary gap awaiting legislative fix.

**The distinction between parametric knowledge and retrieved knowledge.** Whether the technique is called RAG, grounding, or some future term, the conceptual distinction between what a model "knows" from training (static, unverifiable, potentially outdated) versus what it retrieves from external sources at query time (dynamic, citable, updatable) is a permanent feature of how these systems work. This distinction underpins questions about reliability, auditability, and evidentiary value of AI outputs that will recur regardless of which specific retrieval technology is in use.

**Principal-agent liability in autonomous systems.** The legal question of who bears responsibility when an autonomous system acts on behalf of a human — the developer, the deployer, the user, or some combination — is a durable framework question that predates AI and will outlast any specific agent technology. The UETA's "electronic agent" concept, apparent authority doctrine, and the fundamental tension between autonomy and accountability are stable conceptual tools. Specific answers will vary by jurisdiction and evolve with legislation, but the framework for analyzing them is settled.

**The shift from single decisions to system design.** The evolution from "write a better prompt" to "design a prompting system" reflects a broader, durable truth: as AI becomes more capable, the locus of human control shifts from individual interactions to **system architecture**. This has direct implications for regulation — auditing a single prompt is fundamentally different from auditing a multi-step orchestration pipeline. The EU AI Act's requirement for documentation of AI system design (not just outputs) already reflects this reality. Any future AI governance framework will need to grapple with the fact that AI behavior is determined by systems, not single instructions.

### What will change — track but don't memorize

**Specific framework names and versions.** LangChain, DSPy, CrewAI, and AutoGen are important today; some or all may be superseded within two years. AutoGen has already been placed in maintenance mode. The underlying *concepts* they embody — graph-based workflow orchestration, automated prompt optimization, role-based agent collaboration — are more durable than any specific tool.

**Specific model names and capabilities.** GPT-4, Claude 3, Gemini — these are version numbers, not permanent features of the landscape. What matters is understanding *categories* of capability (reasoning models, multimodal models, long-context models) rather than specific product names.

**Specific benchmark scores and hallucination rates.** The 0.8% hallucination rate of o3-mini or the 48% rate of o4-mini on PersonQA are snapshots, not permanent truths. The *principle* that hallucination rates must be measured with standardized benchmarks — and that different benchmarks test different things — is durable.

**Specific regulatory details still in flux.** Whether the AI Accountability for Publishers Act passes, exactly how the EU AI Act's transparency requirements will be enforced for agents, and whether fair use covers training on lawfully obtained copyrighted data (the core question in *NYT v. OpenAI*) are all actively evolving. Legal professionals should track these but recognize that the underlying doctrinal questions — fair use, secondary liability, transparency requirements — are the stable anchors.

**Specific licensing deal structures.** The Disney-OpenAI deal, UMG-Udio settlement, and Warner Music-Suno settlement are early data points in what will be a long evolution of AI content licensing. The *principle* that licensing frameworks are emerging as an alternative to litigation is more durable than any specific deal's terms.

### A framework for staying current without starting over

For the target audience of this module, the practical recommendation is to organize AI knowledge into three tiers. **Tier 1: permanent concepts** — the layered defense model, the human authorship requirement, parametric vs. retrieved knowledge, principal-agent liability, system-level accountability. Learn these once and deeply. **Tier 2: slow-moving frameworks** — the categories of prompting techniques (chain-of-thought, retrieval augmentation, self-reflection), the types of agent architectures (single-agent, multi-agent, orchestrated), the major regulatory approaches (risk-based, rights-based, liability-based). Update these annually. **Tier 3: fast-moving specifics** — product names, version numbers, benchmark scores, individual court decisions, specific tool capabilities. Track these through curated newsletters and briefings rather than trying to maintain comprehensive knowledge.

The AI landscape is changing fast, but not everything about it changes at the same speed. The conceptual vocabulary introduced in this module — hallucination layers, agent autonomy, orchestration systems, and the durable legal principles they intersect with — provides a stable foundation from which to interpret whatever comes next.