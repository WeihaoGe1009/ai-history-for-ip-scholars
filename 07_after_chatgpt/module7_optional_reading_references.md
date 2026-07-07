# Module 7 Optional Reading — Reference List (Working Draft)

Compiled July 2026. MLA 9th edition. Grouped by topic; one-line annotations note relevance. Preprints marked as such; treat empirical findings from preprints as provisional. Lawsuit/controversy items are perishable examples — date-stamp when used.

## Topic 1: Consent and Repurposing (persona distillation, digital afterlife, likeness)

Congressional Research Service. *Artificial Intelligence Prompts Renewed Consideration of a Federal Right of Publicity*. LSB11052, Library of Congress, 29 Jan. 2024, www.congress.gov/crs-product/LSB11052.
— Overview of right-of-publicity gaps exposed by AI replication; surveys NO FAKES Act and No AI FRAUD Act proposals.

Harbinja, Edina, et al. "Governing Ghostbots." *Computer Law & Security Review*, vol. 48, 2023, article 105791, doi:10.1016/j.clsr.2023.105791.
— Core legal scholarship on digital reincarnation of the deceased; proposes an enforceable "do not bot me" clause in wills. Maps harms to privacy, property, personal data, and reputation.

Hollanek, Tomasz, and Katarzyna Nowaczyk-Basińska. "Griefbots, Deadbots, Postmortem Avatars: On Responsible Applications of Generative AI in the Digital Afterlife Industry." *Philosophy & Technology*, vol. 37, no. 2, 2024, article 63, doi:10.1007/s13347-024-00744-w.
— Design-scenario analysis introducing the data donor / data recipient / service interactant framework; recommends mutual consent of data donors and interactants.

Lindemann, Nora Freya. "The Ethics of 'Deathbots.'" *Science and Engineering Ethics*, vol. 28, 2022, article 60, doi:10.1007/s11948-022-00417-x.
— Early ethics treatment of chatbot simulation of the deceased; frequently cited baseline for the consent debate.

United States, Copyright Office. *Copyright and Artificial Intelligence, Part 2: Copyrightability*. Jan. 2025, www.copyright.gov/ai/.
— Official position that prompts alone do not confer authorship; relevant here for the human-contribution and control-spectrum questions that persona repurposing raises.

Holland & Knight. "Senate Committee Advances Bill to Protect Name, Image, Likeness and Voice Against Unauthorized AI Use." *Holland & Knight Insights*, June 2026, www.hklaw.com/en/insights/publications/2026/06.
— Current status of the NO FAKES Act: a proposed federal IP right in voice/likeness digital replicas with DMCA-style notice-and-takedown. Perishable; verify status before use.

"The Making of Digital Ghosts: Designing Ethical AI Afterlives." *arXiv*, 2025, arXiv:2511.20094. Preprint.
— Surveys unauthorized-resurrection incidents (e.g., the Qiao Renliang fan avatar) and design principles around consent, dignity, and residual personhood.

## Topic 2: Distillation

### Concept and lawsuits/controversy

Hinton, Geoffrey, et al. "Distilling the Knowledge in a Neural Network." *arXiv*, 2015, arXiv:1503.02531. Preprint.
— The founding paper: teacher/student framing, distillation as compression.

Xu, Xiaohan, et al. "A Survey on Knowledge Distillation of Large Language Models." *arXiv*, 2024, arXiv:2402.13116. Preprint.
— Standard survey of LLM distillation techniques; useful for the "distill design requires substantial engineering" point.

"Dispute over AI Model Distillation Tech in OpenAI-DeepSeek Case." *Law.asia*, 26 Sept. 2025, law.asia/openai-deepseek-ai-distillation/.
— Legal analysis of the dispute from contract, copyright, and anti-unfair-competition perspectives; notes anti-distillation ToS clauses at OpenAI, Anthropic, Mistral, xAI.

"The Innovation Dilemma: AI Distillation in OpenAI v. DeepSeek." *The Network* (Berkeley Law), 30 Mar. 2025, sites.law.berkeley.edu/thenetwork/2025/03/30/.
— Frames the stakes: enforcement vs. democratization; analogy to Oracle v. Google.

"Unpacking DeepSeek: Distillation, Ethics and National Security." *University of Michigan News*, 31 Jan. 2025, news.umich.edu/unpacking-deepseek-distillation-ethics-and-national-security/.
— Expert Q&A noting license-dependence of legitimacy and the evidentiary difficulty of proving distillation occurred.

### Preventability

Pan, Leyi, et al. "Can LLM Watermarks Robustly Prevent Unauthorized Knowledge Distillation?" *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, ACL, 2025, pp. 13228–51.
— Shows watermark "radioactivity" can be stripped by paraphrasing or inference-time neutralization; watermark-based prevention is fragile.

"DistillGuard: Evaluating Defenses Against LLM Knowledge Distillation." *arXiv*, 2026, arXiv:2603.07835. Preprint.
— Systematic evaluation finding output-level defenses generally insufficient to prevent distillation; effects are task-dependent.

"Towards Distillation-Resistant Large Language Models: An Information-Theoretic Perspective." *arXiv*, 2026, arXiv:2602.03396. Preprint.
— A proposed logit-perturbation defense; useful as the counterpoint (active research, not settled capability).

### Distilled vs. original performance; teacher-student gap

Cho, Jang Hyun, and Bharath Hariharan. "On the Efficacy of Knowledge Distillation." *Proceedings of the IEEE/CVF International Conference on Computer Vision*, 2019, pp. 4794–802.
— Classic result: larger/stronger teachers do not reliably produce better students; student accuracy saturates and can degrade as the capability gap widens.

Mirzadeh, Seyed Iman, et al. "Improved Knowledge Distillation via Teacher Assistant." *Proceedings of the AAAI Conference on Artificial Intelligence*, vol. 34, no. 4, 2020, pp. 5191–98.
— Documents the teacher-student gap problem and proposes intermediate models to bridge it; evidence that usable distillation requires deliberate design.

"A Survey on Knowledge Distillation: Recent Advancements." *Machine Learning with Applications*, 2024, doi:10.1016/j.mlwa.2024.100811 (ScienceDirect, S2666827024000811).
— Notes student performance is tied to teacher quality and inherits teacher limitations and biases.

### Resource vs. quality (non-distilled)

Kaplan, Jared, et al. "Scaling Laws for Neural Language Models." *arXiv*, 2020, arXiv:2001.08361. Preprint.
— Establishes the power-law relationship between compute/data/parameters and loss.

Hoffmann, Jordan, et al. "Training Compute-Optimal Large Language Models." *arXiv*, 2022, arXiv:2203.15556. Preprint.
— The Chinchilla result: quality depends on balanced compute and data budgets; under-resourced training yields measurably worse models.

Sardana, Nikhil, et al. "Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws." *arXiv*, 2024, arXiv:2401.00448. Preprint.
— Extends scaling analysis to deployment costs; useful for the rental-economics link.

"Scaling Laws Revisited: Modeling the Role of Data Quality in Language Model Pretraining." *arXiv*, 2025, arXiv:2510.03313. Preprint.
— Directly addresses the point that "quality" in scaling work is itself under-defined; data quality shifts the curves.

Note for narrative use: "response quality" in this literature usually means benchmark scores or pretraining loss — connect to the module's evaluation-problem item rather than treating it as settled measurement.

## Topic 3: Re-identification vs. Attribution

### Privacy face (re-identification as harm)

Narayanan, Arvind, and Vitaly Shmatikov. "Robust De-anonymization of Large Sparse Datasets." *Proceedings of the 2008 IEEE Symposium on Security and Privacy*, IEEE, 2008, pp. 111–25.
— The pre-AI baseline (Netflix Prize de-anonymization); shows the problem predates current models.

Staab, Robin, et al. "Beyond Memorization: Violating Privacy via Inference with Large Language Models." *Proceedings of the Twelfth International Conference on Learning Representations (ICLR)*, 2024.
— LLMs infer personal attributes (location, income, etc.) from ordinary text at scale; the key demonstration that inference, not just memorization, is the privacy threat.

"From Weak Cues to Real Identities: Evaluating Inference-Driven De-Anonymization in LLM Agents." *arXiv*, 2026, arXiv:2603.18382. Preprint.
— LLM agents reconstruct identities from scattered non-identifying cues, substantially outperforming classical matching on the Netflix setting; argues identity inference should be a first-class privacy risk.

"Robust Utility-Preserving Text Anonymization Based on Large Language Models." *arXiv*, 2024–25, arXiv:2407.11770. Preprint.
— Shows current anonymization methods cannot adequately defend against LLM re-identification without destroying the text's usefulness.

### Attribution face (re-identification as remedy)

Shokri, Reza, et al. "Membership Inference Attacks Against Machine Learning Models." *Proceedings of the 2017 IEEE Symposium on Security and Privacy*, IEEE, 2017, pp. 3–18.
— The founding membership-inference paper; the technical basis for "was my work in your training set?"

Das, Debeshee, et al. "Blind Baselines Beat Membership Inference Attacks for Foundation Models." *arXiv*, 2024, arXiv:2406.16201. Preprint.
— Shows existing MIA evaluations for foundation models are flawed; tempers optimism about MIA as an audit tool.

Zhang, Jie, et al. "Membership Inference Attacks Cannot Prove That a Model Was Trained on Your Data." *arXiv*, 2024, arXiv:2409.19798. Preprint.
— Position paper arguing MIA cannot provide reliable evidence for training-data proofs — directly relevant to what courts should accept.

"On the Evidentiary Limits of Membership Inference for Copyright Auditing." *arXiv*, 2026, arXiv:2601.12937. Preprint.
— Formalizes the adversarial audit setting (judge/prosecutor/accused); examines whether MIA survives developer obfuscation.

"Position: Membership Inference Attack Should Move On to Distributional Statistics for Distilled Generative Models." *arXiv*, 2025, arXiv:2502.02970. Preprint.
— Names "model laundering": distilling a student model to obscure unauthorized training data. The bridge between the distillation topic and the attribution topic.

### The erasure side (right to be forgotten meets learned copies)

"A Survey of Machine Unlearning in Large Language Models: Methods, Challenges and Future Directions." *arXiv*, 2025, arXiv:2503.01854. Preprint.
— Survey of unlearning methods motivated by right-to-be-forgotten mandates; documents the open question of whether knowledge is robustly forgotten or adversarially recoverable.

Staufer, Dimitri. "What Should LLMs Forget? Quantifying Personal Data in LLMs for Right-to-Be-Forgotten Requests." *arXiv*, 2025, arXiv:2507.11128. Preprint.
— Practical gap: RTBF assumes you can identify what the model stored about a person; memorization scales with web presence and model size.

## Cross-topic note

The two faces of re-identification (privacy threat / attribution remedy) and the model-laundering result together support the module's framing: capability to trace what went into a model is simultaneously demanded and feared, and distillation sits at the joint — it is both the thing creators want to detect and a mechanism for evading detection.
