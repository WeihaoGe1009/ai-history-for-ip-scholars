# Optional Reading: Making the Invisible Visible: Understanding Attribution and Data Influence in Generative AI
*A technical and ethical exploration of how training data shapes AI behavior — and what it means for creators, scholars, and society.*

## Overview

In the interactive demo earlier, we simulate training influence in demo 3. This gives us an intuitive sense of what it might mean for training data to shape a model’s behavior. But in real-world systems — especially in large language models — is it possible to rigorously trace back what data influenced a particular output?

Surprisingly, yes — at least in part. A growing body of research has begun to develop methods that estimate how much a particular training example contributes to a model’s behavior. These approaches don’t solve the problem entirely, but they offer the first steps toward visibility — and accountability.

This matters because modern generative models learn from vast datasets made up of human work — books, articles, code, art, conversations — yet the influence of any individual contribution remains largely invisible. Who deserves credit? Can responsibility be traced? What happens when outputs closely reflect training data? In this section, we explore both the algorithms that attempt to answer these questions, and the broader implications they raise for attribution, memorization, and ethical responsibility.

## What does "Influence" Really mean?

Before we talk about algorithms or measurements, we need to ask a basic question: **What does it mean to say a model was “influenced” by something?**

In the machine learning community, influence usually means this:

> If we slightly changed or removed a piece of training data, would the model’s output change in response?

This definition gives us a way to trace the most “important” training examples for a given prediction — and, in principle, a way to identify which sources shaped the model.

But the picture becomes more troubling when we consider how this plays out in large-scale models trained on massive corpora.

Imagine two situations:

* In one case, a model repeats content that closely resembles a specific article. The influence is clear and strong — and measurable.

* In the other case, the model synthesizes phrasing, tone, and framing drawn from tens of thousands of contributors. Each one’s influence is small and diffuse — but the result still reflects their labor.

Under current influence definitions, only the first example is likely to register. The second — which may reflect most real outputs — remains invisible.

This is where "small-world effects" begin to matter.

In any large corpus, a few “hub” documents — often the most viral, institutional, or widely cited — occupy central positions. Their language patterns are shared widely and reappear more often. Most individual creators, by contrast, sit on the edges of the network. Their style, even if original, is absorbed and diluted.

So when a model borrows from everyone, it’s the most echoed phrases that stand out — while the vast number of small, unique contributions fade into the background.

> **The more people a model borrows from, the fewer it visibly credits.**

> This creates a paradox: as models scale and absorb more human labor, their measurable “influences” narrow.

This isn’t just a math problem — it’s a justice problem.

It raises hard questions about whose contributions are seen, whose are erased, and how creative labor is acknowledged in systems that work at scale.

The tools we introduce next were designed within this narrower technical framing of influence. They can be powerful and useful in many settings — including research, transparency efforts, and institutional audits.

But we want to be honest with you from the beginning:

* **These tools are not neutral.**.

* They reflect a specific, limited definition of influence — one that is easier to measure than to justify.

* And they do not, by themselves, answer the harder questions about recognition, responsibility, or fairness.

This is where we begin — not where we end.

We hope this document helps you read the technical material with both clarity and critical distance.

## How Current Machine-Learning Community Measures "Influence"    
### Algorithms 
#### 1. Leave-One-Out Retraining 
**What it does** 

Removes one training example, retrains the model, and checks if the output changes. If it does, the removed data had real influence.

**Why it matters**

It offers a direct measure of **causal impact** - showing what would happen if a data point had never been used. **It defines the Gold Standard of Influence measurement under the current definition of Influence**.

**Strengths**
* Clear and intuitive.
* Makes no assumptions about model internals or training method.
* Supports strong claims about responsibility and data relevance.

**Limitations** 
* Requires retraining the model once for **each training example** , which is impractical for large models.

**However,** well-resourced labs or government agencies can:
* Use **partial checkpoints** and training logs to simulate smaller retraining runs.
* Focus on **final layers**, fine-tuning phases, or known sensitive subsets.
* Deploy **shadow models** trained with and without disputed data, for case-specific auditing.

**Feasibility Outlook**
* Feasible in **targeted investigations** with access to logs and layered retraining.
* Useful in **legal discovery**, internal audits, or contested domains (e.g., medicine, copyright, misinformation).

**Reference**

Hammoudeh, Zayd, and Daniel Lowd. "Training data influence analysis and estimation: A survey." Machine Learning 113.5 (2024): 2351-2403.[arXiv link](https://arxiv.org/abs/2212.04612) 

#### 2. Influence Functions
**What it does**

Estimates how much a model’s prediction on a test input would change if a particular training example were slightly more influential during training.

**Why it matters**

It can help trace which examples most affected the model’s behavior — and flag potentially **harmful, mislabeled, or overly dominant data.**

**Strengths**
* Useful for ranking influential training examples for any single output.
* Helps uncover both valuable and problematic data.
* Applicable to classification, regression, and even some generative tasks.

**Limitations**
* Requires access to something called the **inverse Hessian**, a mathematical structure summarizing the model’s sensitivity.
* This is hard to compute for very large models, but **can be approximated** or extracted in planned audits or during training.
* Accuracy depends on how the model was trained and what checkpoints are available.

**Feasibility Outlook**:
* Feasible for **mid-sized or audit-compliant models**, especially in partnership with research institutions.
* May be supported by legal provisions to require **Hessian snapshots or model sensitivity exports** during training. 

**Reference**

Koh, Pang Wei, and Percy Liang. "Understanding black-box predictions via influence functions." International conference on machine learning. PMLR, 2017. [arXiv link](https://arxiv.org/abs/1703.04730)  

#### 3. Data Shapley

**What it does**

Estimates how much each training example **contributes to the model’s overall performance**, based on all possible combinations of data.

**Why it matters**

Provides a **fairness-based attribution** — identifying which data points helped the model learn, and which made it worse.

**Strengths**
* Offers clear reasoning for **credit, licensing, or removal** decisions.
* Can show **positive and negative influence** across entire datasets.
* Inspired by well-established ideas from cooperative game theory.

**Limitations**
* Computing exact values is infeasible — it requires evaluating all combinations of data.
* Approximations exist, but still require many training runs or simplifications.

**However**, institutions can:
* Use **sampling-based approximations** on targeted data (e.g., government-published sets, known author groups).
* Apply the method to **filtered domains** (e.g., education, law, health).
* Use **Shapley-style scores** to inform decisions about **data ownership, deletion requests, or provenance tracing.**

**Feasibility Outlook**:
* Feasible for scoped attribution, and powerful when paired with **transparent data sources.**
* Valuable for **public model evaluation**, and for supporting authorship or removal claims.

**Reference**

Ghorbani, Amirata, and James Zou. "Data shapley: Equitable valuation of data for machine learning." International conference on machine learning. PMLR, 2019. [arXiv link](https://arxiv.org/abs/1904.02868)

#### 4. TracIn (Training Influence via Gradient Traces)

**What it does**

Tracks how much each training example’s **gradient** moved the model’s parameters in the direction of a given prediction — over time.

**Why it matters** 

It estimates which training points **shaped the model’s internal behavior** most strongly — without retraining.

**Strengths**
* Efficient and scalable if planned during training.
* Works well with deep neural networks, including LLM components.
* Can trace influence at multiple points in training (early, late, unstable regions).

**Limitations**
* Requires **gradient logging and model checkpoints** during training — cannot be added retroactively.
* Captures local alignment, not long-range dependencies.

**However**, agencies and research labs that co-develop models (or fund them) can:
* Require **gradient capture as part of training contracts.**
* Analyze **per-step influence** for specific cases (e.g., safety-critical outputs, misinforming generations).
* Pair TracIn with metadata or domain labels to support **transparency mandates** or **attribution frameworks.**

**Feasibility Outlook**
* One of the most **scalable and realistic** influence-tracing tools today.
* Suitable for **government-backed audits**, public-private evaluations, or model documentation policies.

**Reference**

Pruthi, Garima, et al. "Estimating training data influence by tracing gradient descent." Advances in Neural Information Processing Systems 33 (2020): 19920-19930. [arXiv link](https://arxiv.org/abs/2002.08484) .

### Emerging Use in Auditing Contexts (Research and Regulation)

Attribution algorithms are not yet routinely cited in court. What has actually reached formal settings splits into two layers, and the split is itself informative: output-level tracing (checking whether a model reproduces specific text) is mature enough to appear in litigation, while training-influence tracing (estimating which training examples shaped a behavior) remains in research tools, governance frameworks, and policy proposals. This list is not exhaustive.

#### 1. Copyright litigation: output matching, not influence tracing (2023–present)

Authors, programmers, and news organizations have sued OpenAI, Meta, and others over the use of copyrighted works in training. No court has ordered a defendant to run influence tracing. The tracing tooling that has surfaced in litigation operates at the output level: a 2026 deposition in the news publishers' case revealed that OpenAI had built internal tools (reported as "Project Giraffe"), including a Bloom filter that flagged and logged when ChatGPT outputs likely reproduced copyrighted journalism. Whether output matching of this kind, rather than training-influence estimation, becomes the standard of proof in these cases is an open question.

#### 2. Attribution methods in legal and policy discussion

Influence estimation appears in venues where legal scholars and technologists meet, if not yet in briefs. A 2026 Authors Alliance workshop on DMCA §1202 and attribution standards discussed influence functions, data Shapley values, and TracIn as techniques that can estimate training-data contributions. A parallel research thread proposes Shapley-style attribution as the basis for royalty and compensation schemes, motivated explicitly by the ongoing copyright disputes (Deng and Ma; Wang et al.). Whether courts or legislatures would accept an approximation as a basis for payment is, again, an open question.

#### 3. Governance frameworks: NIST, OECD, EU

The NIST AI Risk Management Framework [(2023)](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf) states that "maintaining the provenance of training data and supporting attribution of the AI system's decisions to subsets of training data can assist with both transparency and accountability." This is the clearest framework-level endorsement of influence-style attribution to date, though the framework is voluntary and names no specific technique. The OECD AI Principles include [transparency and explainability](https://oecd.ai/en/dashboards/ai-principles/P7) among their core values. The [EU AI Act](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-53) goes further in a different direction: providers of general-purpose models must publish a sufficiently detailed summary of training content, a provenance mandate rather than an influence mandate.

#### 4. Industrial and open-science practice

Anthropic researchers applied influence functions to large language models to study which training sequences shape model outputs (Grosse et al., 2023), the most prominent published industrial use of the technique at scale. On the open-science side, the BigScience collaboration that produced BLOOM (2022) built data governance structures prioritizing the agency of data rights-holders, released model and data cards, and later published the ROOTS Search Tool, which lets outside researchers inspect the 1.6 TB training corpus directly. BLOOM's transparency works through documentation and searchable data access, not through influence algorithms, which illustrates that provenance and influence estimation are separable commitments.

#### References
Grosse, Roger, et al. "Studying Large Language Model Generalization with Influence Functions." arXiv, 2023, arxiv.org/abs/2308.03296.

Deng, Junwei, and Jiaqi Ma. "Computational Copyright: Towards a Royalty Model for Music Generative AI." arXiv, 2023, arxiv.org/abs/2312.06646.

"Notes from a Recent Authors Alliance Workshop: DMCA §1202 and Attribution Standards for AI." Authors Alliance, 19 Feb. 2026, www.authorsalliance.org/2026/02/19/notes-from-a-recent-authors-alliance-workshop-dmca-%C2%A71202-and-attribution-standards-for-ai/.

National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1, Jan. 2023, nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf.

Organisation for Economic Co-operation and Development. "Principle 1.3: Transparency and Explainability." Recommendation of the Council on Artificial Intelligence, OECD/LEGAL/0449, 22 May 2019, amended 3 May 2024, legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449.

European Parliament and Council of the European Union. "Article 53: Obligations for Providers of General-Purpose AI Models." Regulation (EU) 2024/1689 of 13 June 2024 Laying Down Harmonised Rules on Artificial Intelligence (Artificial Intelligence Act), Official Journal of the European Union, L series, 12 July 2024, eur-lex.europa.eu/eli/reg/2024/1689/oj.
 
Piktus, Aleksandra, et al. "The ROOTS Search Tool: Data Transparency for LLMs." arXiv, 2023, arxiv.org/abs/2302.14035.

BigScience Workshop. "BLOOM: A 176B-Parameter Open-Access Multilingual Language Model." arXiv, 2022, arxiv.org/abs/2211.05100.

## Justice Gap in Influence-Based Attention

### The Gap

Influence-based attribution methods — such as Leave-One-Out retraining, Influence Functions, and Data Shapley — aim to quantify which training examples most affected a model’s behavior. But these algorithms privilege examples that leave a **strong and localized trace** on the model. The result is a bias toward **central, echoed, or institutionally repeated content**, and a gap in recognizing the quiet, distributed contributions that shaped the model more diffusely.

> In large models trained on millions of examples, it is often the most amplified voices that get measured — while the subtle originality of smaller creators is washed out.

This creates a justice gap: the very **scale** hat enables a model to absorb collective creativity is the same scale that **erases individual influence**, especially from the margins.

### Why This Happens (Technically)
Influence algorithms work by asking counterfactual questions like: *What would the model output be if this training sample were removed?* These approaches are computationally expensive, so they rely on simplifying assumptions — for example, measuring gradient similarity (in Influence Functions), marginal value contributions (in Shapley methods), or direct performance differences after retraining.

In each case, they detect **sharp changes** in model behavior. That means:

* High **redundant or echoed** examples stand out more (they reinforce model weights repeatedly).

* **Unique but subtle** examples are less likely to register, because their removal causes only small shifts — even if they contributed to a rich, diverse training space.

Thus, the tracing process mimics small-world network dynamics: **a few hubs dominate attention**, while the majority of nodes (voices, authors, styles) are difficult to trace.

### Ethical Implications
This dynamic risks entrenching the very inequalities that content creators and independent contributors fear:

* Creators with **institutional support or mass exposure** are more likely to be identified and credited.

* Meanwhile, those with smaller followings — whose phrasing, tone, or insights may still shape the system — remain unacknowledged.

Influence is **technically invisible** unless it’s measurable.

And what’s measurable is shaped by the underlying structure of attention and centrality.

### Possible Paths Forward
Understanding this limitation opens the door to constructive improvement — both technically and socially:

* **Redefining Influence Beyond Model Output**
    Legal or ethical frameworks may need to **decouple credit from output matching**. Influence can be acknowledged based on inclusion, stylistic absorption, or participation in a known source corpus, even if no single sentence dominates the outcome.

* **Open Audit Tools for Institutions**
    With adequate collaboration between regulatory bodies, research universities, and supercomputing centers, it’s possible to develop shared infrastructures for tracing influence in models. These don’t need to be commercial tools — they can be **open-source, public-interest systems**, built to support transparency, policy evaluation, and legal due diligence. ROOTS Search Tool and BLOOM is a success case of such collaboration 

* **Platform Precedents and Policy Crossovers**
    These questions are not new. Scholars of platform governance (Tarleton Gillespie), algorithmic bias (Safiya Noble), and datafication (José van Dijck) have argued in different ways that the technical and commercial arrangements of centralized platforms shape whose content becomes visible and valued, while presenting those arrangements as neutral. A concrete precedent: in January 2018, YouTube restricted ad revenue to channels with at least 1,000 subscribers and 4,000 watch hours in the prior twelve months, replacing a much lower lifetime-views threshold. YouTube framed the change as protection against spammers and bad actors — a threshold designed for manageability — but it also removed the smallest creators from the earning pool entirely. (The threshold has since changed; the 2018 numbers are a time-stamped example of a durable pattern.)

    Creator organizing followed. The YouTubers Union, founded in 2018, and its later FairTube campaign with the German trade union IG Metall demanded that platforms publish the criteria affecting monetization and discovery and explain individual decisions. Their complaint was not only about earnings but about legitimacy: which contributions count, judged by criteria no one outside the platform can inspect. If language models are built on similarly skewed visibility, the same asymmetry is reproduced — this time inside the training data itself.
 
* **In addition to Model Influence Evaluation**
    In parallel, other technologies may help creators assert and protect rights. **Fingerprinting, watermarking, and semantic detection tools** can help identify when a model output closely mimics a known work. **Provenance and dataset documentation standards** aim to make training data more transparent and auditable. Meanwhile, **blockchain timestamping, protective licensing,** and **content authenticity metadata** offer new ways to assert originality and preferred usage. While none of these tools solve the problem of quantifying model influence, they form a **complementary ecosystem** of safeguards — especially valuable when combined with policy or institutional support.

The goal of these efforts is not to freeze innovation, but to **recognize invisible labor**, restore proportional credit, and support fairer systems of cultural and intellectual attribution. This path is challenging, but not impossible. The tools exist. What’s needed is **collaboration, shared language, and a commitment to making the invisible visible** - especially from those engaged in interpreting intellectual property law, shaping future legal standards, or contributing original works to the cultural and creative commons. 

#### References — Possible Paths Forward

Coalition for Content Provenance and Authenticity. "C2PA Technical Specification." C2PA, c2pa.org/specifications/.

Deng, Junwei, and Jiaqi Ma. "Computational Copyright: Towards a Royalty Model for Music Generative AI." arXiv, 2023, arxiv.org/abs/2312.06646.

Dathathri, Sumanth, et al. "Scalable Watermarking for Identifying Large Language Model Outputs." Nature, vol. 634, 2024, pp. 818–23.

Gebru, Timnit, et al. "Datasheets for Datasets." Communications of the ACM, vol. 64, no. 12, 2021, pp. 86–92.

Gillespie, Tarleton. Custodians of the Internet: Platforms, Content Moderation, and the Hidden Decisions That Shape Social Media. Yale UP, 2018.

Mohan, Neal, and Robert Kyncl. "Additional Changes to the YouTube Partner Program (YPP) to Better Protect Creators." YouTube Official Blog, 16 Jan. 2018, blog.youtube/news-and-events/additional-changes-to-youtube-partner/.

Noble, Safiya Umoja. Algorithms of Oppression: How Search Engines Reinforce Racism. New York UP, 2018.

"Notes from a Recent Authors Alliance Workshop: DMCA §1202 and Attribution Standards for AI." Authors Alliance, 19 Feb. 2026, www.authorsalliance.org/2026/02/19/notes-from-a-recent-authors-alliance-workshop-dmca-%C2%A71202-and-attribution-standards-for-ai/.

Piktus, Aleksandra, et al. "The ROOTS Search Tool: Data Transparency for LLMs." arXiv, 2023, arxiv.org/abs/2302.14035.

Shan, Shawn, et al. "Glaze: Protecting Artists from Style Mimicry by Text-to-Image Models." Proceedings of the 32nd USENIX Security Symposium, 2023, pp. 2187–204.

van Dijck, José. "Datafication, Dataism and Dataveillance: Big Data between Scientific Paradigm and Ideology." Surveillance & Society, vol. 12, no. 2, 2014, pp. 197–208.

Whittaker, Zack. "YouTubers Want to Unionize, and They've Got the Support of IG Metall." CNBC, 6 Aug. 2019, www.cnbc.com/2019/08/06/youtubers-want-to-unionize-and-theyve-got-the-support-of-ig-metall.html.  
