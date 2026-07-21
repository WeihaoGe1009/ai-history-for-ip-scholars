# Supplementary Reading: Six Places Where the Technology Meets the Law

*Optional reading for Module 06. Assumes the core module concepts: inputs, outputs, training data, and classification. No programming knowledge is required.*

*A note on method: this reading deliberately names no cases, statutes, or agencies. Litigation and regulation in this area change faster than a durable reading can track, and evaluating them is your expertise, not this notebook's. What this reading offers instead is the technical side of each question, stated precisely enough that you can find and assess the current legal state yourself. Each theme ends with a short research vocabulary: the terms of art that will retrieve the live disputes whenever you read this.*

---

## Theme 1: Authorship and the Creativity Threshold

**The mechanism.** A generative model produces output by sampling from patterns learned during training. The human contribution to any given output can range from almost nothing (a five-word prompt, first result accepted) to sustained direction (hundreds of prompt revisions, selection among outputs, manual editing, recombination). Technically, these are points on one continuous spectrum. The deliberate end of it involves enough effort and skill that a named practice has grown around it, prompt engineering: specifying intent explicitly in the prompt, testing the output against that intent, and revising until they match. Even so, there is no natural break in the process where "the machine's part" ends and "the person's part" begins; the division is a judgment imposed from outside, not a fact read off the system.

**The tension.** Copyright traditions generally assume works are made by people, and for most of their history that assumption cost nothing to hold, because human choice and original output arrived together. Generative systems separate them. A rule that asks "was there a human author?" now needs a theory of *which* human activities count: prompting, selecting, arranging, editing, or some threshold combination. Whether the answer should be found by examining the finished work, the production process, or both is exactly the kind of question this series poses without answering.

**Research vocabulary.** *Human authorship requirement* (the doctrinal hook in most jurisdictions); *AI-assisted versus AI-generated* (the distinction registration authorities have tried to draw); *sufficient human control* or *human contribution* (phrases used for the emerging threshold); *prompt* and *sampling* (the technical terms for the input and the generation step, defined in this module); *prompt engineering* (the discipline of explicit specification and iterative testing).

> **Discussion Questions**
> 1. Photography once posed a similar problem: the machine captures, the human frames and selects. Does the analogy hold for prompting, and where exactly does it break?
> 2. If authorship turns on process rather than the finished work, what evidence would a tribunal need, and who possesses it?
> 3. Find the most recent authorship decision or registration guidance in your jurisdiction. Which activities on the spectrum above did it treat as sufficient?

---

## Theme 2: Training Data as a Legal Object

**The mechanism.** Training does not store copies of works the way a library does. Each work in the training set contributes small adjustments to the model's parameters, and the finished model is a single set of numbers shaped by everything it saw. Two technical facts matter for any legal analysis. First, the works are genuinely copied at ingestion time, into datasets and into memory, before training begins. Second, after training, individual works are usually not retrievable from the model, yet under some conditions a model can reproduce passages of training text nearly verbatim, a behavior called memorization. Both facts are true at once, and arguments in this area often turn on which one a party emphasizes.

**The tension.** A copyrighted work used in training is functioning as an input to a statistical process rather than as something read, viewed, or performed. Whether that use requires permission, compensation, disclosure, or nothing at all is unsettled, and different jurisdictions are answering with different levers: consent regimes (asking first), opt-out regimes (allowing refusal in advance), transparency regimes (requiring disclosure of what was used), and after-the-fact remedies (litigating harm). These four levers are independent; a jurisdiction can pull any combination. Which combination fits which interests is a design question for legislators, not a technical one.

**Research vocabulary.** *Training corpus* and *data provenance* (what was used and where it came from); *memorization* and *regurgitation* (the reproduction behavior); *text-and-data-mining exception* and *opt-out* (the European-origin lever); *fair use* and *transformative use* (the American-origin lever); *scraping* (bulk collection from the open web).

> **Discussion Questions**
> 1. Opt-in places the burden on developers to ask; opt-out places it on rights holders to refuse. Given that a training corpus may contain millions of works by millions of owners, what does each choice cost, and who pays?
> 2. Memorization is an occasional behavior, not the mechanism of training. Should the legal analysis of training turn on the typical case or the failure case?
> 3. Survey the current litigation and legislation on training data in two jurisdictions of your choice. Which of the four levers is each actually pulling?

---

## Theme 3: The "Black Box" Problem and Accountability

**The mechanism.** A trained model's behavior is determined by parameters, often millions of them, adjusted automatically during training. Nobody wrote the decision rule down; it emerged from data. The model can report *what* it predicts and, with additional tooling, *which inputs most influenced* a prediction, but it cannot produce the kind of reason a human decision-maker gives, because no such reason exists inside it. This is not secrecy in the ordinary sense. Even with full access to every parameter, the explanation legal processes usually want may not be reconstructible. Opacity here comes in two distinct forms that are easy to conflate: contractual opacity (the vendor will not show you) and intrinsic opacity (there is nothing legible to show).

**The tension.** Adversarial legal process assumes decisions can be contested, and contesting a decision usually requires knowing its basis. When a learned system contributes to a consequential decision, that assumption fails in a new way. Regulatory responses so far fall into two broad families: absorbing opaque systems into existing liability doctrine (treating them as one more complex product) or regulating opacity itself before deployment (documentation, oversight, and explainability mandates for designated uses). A second-order issue, developed elsewhere in this series, is that a system trained on historical decision records reproduces the patterns in those records while presenting its outputs as neutral computation.

**Research vocabulary.** *Interpretability* and *explainability* (the technical research fields); *feature attribution* (the "which inputs mattered" tooling); *high-risk system* (the classification label used in tier-based regulation); *automated decision-making* (the phrase most statutes and regulations use); *trade secret* (the contractual-opacity dimension).

> **Discussion Questions**
> 1. What would a legally sufficient explanation of a model's output contain, and sufficient for whom: the affected person, their counsel, a reviewing court, or a regulator?
> 2. Which existing doctrine in your field has already absorbed a technology whose inner workings the parties could not inspect? Does its template transfer?
> 3. Distinguish contractual from intrinsic opacity in a current dispute of your choosing. Which one was actually at issue, and would disclosure have cured it?

---

## Theme 4: Distillation and the Second Model

**The mechanism.** Distillation trains a small model to approximate the behavior of a large one. The large model (the teacher) answers a curated set of queries; the small model (the student) is trained on those answers instead of, or alongside, original data. Several technical facts bound the legal arguments. The student generally underperforms the teacher across the board, though it can match it within a narrow domain. Producing a good student is skilled work in its own right: choosing what to ask the teacher, curating and filtering the answers, and designing the training regimen all matter, so distillation is not simply copying outputs. The teacher itself only performs well when served with substantial compute, so the student is often the only form in which the capability is practically usable on modest hardware. And distillation is cheap relative to training from scratch, which consumes large amounts of electricity and cooling water. Finally, any party with ordinary query access to a model can attempt distillation; there is no known technical means of preventing it that does not also degrade normal use.

**The tension.** Does distilling take something the teacher's developer owns? The question is harder than it sounds, because it is unclear what the legal object would be. Model parameters are numbers produced by an automated process, not obviously an authored work; the teacher's outputs raise the authorship questions of Theme 1; and the strongest available instruments are often contractual, since most providers prohibit training on their outputs in terms of service. Arguments then run in both directions, and this reading arranges rather than resolves them. In distillation's favor: the student is a genuinely lesser artifact; making a good one requires human effort and technique; it avoids re-spending the energy and water of full retraining; and it converts general capability into portable, economical, specialized tools that the teacher's developer may never have built. Against it: the distiller rides on the training investment of others while bearing none of its cost or risk, which, generalized, weakens anyone's incentive to train large models at all; a specialized student can substitute for the teacher precisely in the market segment where the teacher earned its value, so "not as good overall" does not mean "not competing"; distillation carries the teacher's biases and errors into the student while severing the provenance trail, so transparency obligations attached to the original training data quietly lapse one model downstream; safety behaviors trained into the teacher do not automatically survive into the student, so distillation can strip safeguards along with cost; and where the teacher's own corpus was used without permission, the student extends that use a further step without any new consent from the original rights holders. Which of these considerations sound in property, contract, unfair competition, or none of the above is exactly the question for the reader.

**Research vocabulary.** *Knowledge distillation* and *teacher/student model* (the technique); *model extraction* (the adversarial-framing cousin); *synthetic training data* (what the teacher's outputs become); *output restrictions* or *training-on-outputs clauses* (the contractual lever); *misappropriation* and *free-riding* (the unfair-competition framing).

> **Discussion Questions**
> 1. If parameters are not an authored work and outputs lack a human author, what legal object, if any, does distillation take? Test each candidate doctrine you know against the mechanism described above.
> 2. Your field likely has a doctrine governing second comers who build on a first mover's investment. Does its logic transfer to distillation, and what does the energy-and-water argument do to the balance?
> 3. Find the training-on-outputs provision in the terms of service of two current model providers. What conduct do they actually prohibit, and against whom would the prohibition be enforceable?

---

## Theme 5: Synthetic Media and Epistemic Integrity

**The mechanism.** Generative models can now produce audio, image, and video that ordinary inspection cannot distinguish from recordings of real events, at negligible cost and without specialist skill. Detection is an arms race, not a solved problem: detectors are themselves classifiers, trained on known generators, and degrade against new generators or lightly edited output. Provenance labeling (marking content at creation) is technically feasible but fragile, because labels can be stripped by re-encoding, screenshotting, or passing content through another tool.

**The tension.** Authentication regimes were designed around a background economic fact: convincing forgery of photographs, audio, and video was expensive and rare, so genuineness could enjoy a practical presumption. That cost assumption has collapsed, and it loads two problems onto the rules at once. The first is the fake exhibit offered as genuine. The second is subtler: once fabrication is cheap, any authentic recording can be met with the claim that it is synthetic. Commentators call this the liar's dividend, and it taxes true evidence rather than promoting false evidence. Note that the two problems pull rules in opposite directions; raising the bar for admitting recordings helps against the first and worsens the second.

**Research vocabulary.** *Deepfake* and *synthetic media* (the content class); *authentication* (the evidentiary hurdle); *liar's dividend* (the denial problem); *content provenance* and *watermarking* (the labeling approaches, and their stripping problem); *detection classifier* (why detection is an arms race, in this module's terms).

> **Discussion Questions**
> 1. Should the burden of proving an exhibit genuine rise when the opposing party plausibly alleges synthesis? What would "plausibly" mean, given that detection tools are themselves fallible classifiers?
> 2. Can evidence rules address the liar's dividend at all, or is it a problem for institutions outside the courtroom?
> 3. Trace one path a synthetic political video takes from generator to voter. Mark every point where a provenance label could be stripped, and every point where a legal obligation could attach.

---

## Theme 6: Regulatory Divergence

**The mechanism side of this theme is institutional rather than computational.** AI systems are trained in one place, hosted in a second, and used everywhere, while the models themselves are portable files that cross borders as easily as any data. The technology is jurisdictionally indifferent by construction. Regulation, meanwhile, encodes each jurisdiction's prior habits: a tradition of comprehensive ex ante regulation produces a comprehensive ex ante statute; a sectoral tradition meets AI sector by sector; an administrative-governance tradition regulates through registration and platform obligations.

**The tension.** Divergence is therefore structural, not accidental, and it can be read along a small set of durable axes rather than as a list of statutes to memorize. Four axes do most of the work: *scope* (one horizontal law versus many sectoral rules), *timing* (obligations before deployment versus liability after harm), *location of discretion* (legislature, regulator, or court), and *stability* (how easily the regime reverses with political turnover). Any current regime, and any future one, can be placed on these axes. For multinational actors the consequence is concrete: a single model may face inconsistent obligations about disclosure, labeling, and permissible use across the jurisdictions it touches, with no treaty framework resolving conflicts. Whether this area eventually harmonizes, as aviation safety did, or stays fragmented, as data privacy largely has, is open.

**Research vocabulary.** *Risk-based / tiered regulation* (the horizontal ex ante pattern); *sectoral regulation* (the domain-by-domain pattern); *ex ante versus ex post* (the timing axis); *extraterritorial effect* (why one jurisdiction's rules reach others); *soft law* and *harmonization* (the non-binding coordination instruments).

> **Discussion Questions**
> 1. Ex ante regimes pay enforcement costs before harms occur; ex post regimes pay them after. Which allocation fits a technology whose failure modes are still being discovered?
> 2. Place the current AI regimes of three jurisdictions on the four axes above. Where do they genuinely differ, and where is the difference only vocabulary?
> 3. What does regulatory instability do to compliance incentives, compared with a stable but stricter regime?

---

## How to Use This Reading

Each theme above gives you the technical mechanism and the structural tension; the current legal state is yours to supply. A workable method: take one theme, search the research vocabulary in your preferred legal database, restrict to the past eighteen months, and ask of whatever you find a single question, namely which assumption identified above the dispute is actually testing. In our experience the mechanisms and tensions change on decade timescales; the dockets change monthly. This reading is built to survive on the slower clock.
