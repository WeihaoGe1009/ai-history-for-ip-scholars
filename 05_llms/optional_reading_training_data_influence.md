# Optional Reading: Making the Invisible Visible: Understanding Attribution and Data Influence in Generative AI
*A technical and ethical exploration of how training data shapes AI behavior — and what it means for creators, scholars, and society.*

## Overview

In the interactive demo earlier, we simulate training influence <--filling the demo here-->. This gives us an intuitive sense of what it might mean for training data to shape a model’s behavior. But in real-world systems — especially in large language models — is it possible to rigorously trace back what data influenced a particular output?

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

### Emerging Use in Auditing Contexts (Research + Regulation) 
<--- need to manually verify the source ---> 
These algorithms are not yet *routinely cited in court*, but they are entering **formal auditing tools, research partnerships, and policy proposals** - and could be used in future litigation or regulatory proceedings.

#### 1. OpenAI Copyright Lawsuits (2023–present)
* Plaintiffs (authors, programmers) allege that GPT-like models reproduce copyrighted content.

* While no court has yet ordered OpenAI to run influence tracing, **experts have proposed using methods like Influence Functions or TracIn** to determine if the model was influenced by specific training samples.

* Influence tracing has been discussed in **amicus briefs and expert opinions**, especially from researchers at organizations like **EPIC, AI Now Institute, and Mozilla Foundation.**

#### 2. NIST and OECD Auditing Frameworks
* The **NIST AI Risk Management Framework (2023)** includes traceability as a core pillar — and influence estimation is being integrated in risk assessment tooling (especially via model documentation, training lineage, and data valuation).

* The **OECD.AI framework** includes auditability, data governance, and influence awareness under “Transparency and Explainability.”

#### 3. Meta AI’s internal audits (2022–2024)
* In several published audits of LLaMA and multilingual models, Meta researchers have cited gradient-based influence tracing and dataset analysis using leave-one-out approximations and filtering.

* One internal paper tested **gradient attribution and data influence tracking** on multilingual bias and misinformation tasks.

#### 4. BigScience Project / BLOOM model (2022)
* As part of a **publicly auditable LLM**, the BigScience collaboration tested **subset retraining, Shapley approximations**, and **gradient logging** to track data contributions and inform open governance.

* These techniques were part of a **model card** released alongside BLOOM and reflected real usage of influence and traceability tooling. 

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
    With adequate collaboration between regulatory bodies, research universities, and supercomputing centers, it’s possible to develop shared infrastructures for tracing influence in models. These don’t need to be commercial tools — they can be **open-source, public-interest systems**, built to support transparency, policy evaluation, and legal due diligence. 

* **Platform Precedents and Policy Crossovers** <--double-check citations-->  
    These questions are not new. Scholars like **Tarleton Gillespie** (on platform governance), **Safiya Noble** (on algorithmic bias), and **José van Dijck** (on datafication and visibility) have long argued that centralized platforms systematically obscure the labor and creativity of smaller actors. **The 2018 shift in YouTube’s monetization policy** — where only creators with 1,000+ subscribers and 4,000+ watch hours could earn ad revenue — offers a clear analogy: a threshold designed for manageability, but one that systematically excluded smaller voices from visibility and credit.

    As activists from the **YouTube Creators Union and others have pointed out, this doesn’t just affect earnings — it affects **which contributions are acknowledged as legitimate**. If we build our language models on similarly skewed visibility, we risk reproducing the same injustice. 

* **In addition to Model Influence Evaluation**
    In parallel, other technologies may help creators assert and protect rights. **Fingerprinting, watermarking, and semantic detection tools** can help identify when a model output closely mimics a known work. **Provenance and dataset documentation standards** aim to make training data more transparent and auditable. Meanwhile, **blockchain timestamping, protective licensing,** and **content authenticity metadata** offer new ways to assert originality and preferred usage. While none of these tools solve the problem of quantifying model influence, they form a **complementary ecosystem** of safeguards — especially valuable when combined with policy or institutional support.

The goal of these efforts is not to freeze innovation, but to **recognize invisible labor**, restore proportional credit, and support fairer systems of cultural and intellectual attribution. This path is challenging, but not impossible. The tools exist. What’s needed is **collaboration, shared language, and a commitment to making the invisible visible** - especially from those engaged in interpreting intellectual property law, shaping future legal standards, or contributing original works to the cultural and creative commons.   
