# Optional Reading: "I Trained an AI" — Three Different Concepts

A few years ago, it was common to hear "I trained a ChatGPT on my documents." The claim is heard less often now, and users have become more aware of the difference of training, fine-tuning, and prompting. However, some underlying confusions are still around. Here, we would like to provide a brief clarification about these concepts.
 
## Training, Fine-tuning, and Prompting

**Training** means building a model from scratch. Actually, we've already done this in module 1. However, the models we've trained are very small. For the large AI models, this is a whole different scale.Enormous amounts of text are fed into the system, and everything the model "knows" comes from this process. Think of raising a person from birth. Training a competitive large model costs on the order of tens or hundreds of millions of dollars, and almost nobody outside a handful of companies does it. If someone says they trained an AI, the polite and useful follow-up is: from scratch, or starting from an existing one? But it is still hopeful that in the future, with the development of new designs and computers, powerful models become less gigantic and individuals can actually build and train them. 

**Fine-tuning** means taking an already-built model and teaching it something additional or reshaping its habits, using a much smaller amount of material. Think of sending an adult to a professional school: the person already speaks the language and knows the world; the school adds a specialty. The result is a changed model: usually, the parameters in "layers" (remember this concept from Module 2?) near the output end are changed. And consequently, the model will behave differently even when given the same input as before. Individuals do a lot of fine-tuning, too, and many share their fine-tuned models online, like the programmers shared their code. Hugging Face, a popular public website where people share models the way others share open-source software, hosts thousands of fine-tuned variants of popular models, made by labs, companies, and hobbyists.

**Prompting** means shaping what the model does **without** changing the model at all. Everything happens at conversation time: the instructions given, the examples shown, the documents attached, the back-and-forth of the conversation itself. Think of briefing a consultant at the start of a meeting: the consultant is unchanged; only the briefing differs. This is what nearly every "customized AI" that ordinary users set up actually is, and the customization can be edited or deleted at any moment.

The customization features in consumer products belong to prompting, whatever their branding suggests. Each is, at bottom, stored instructions and stored reference material, handed to the model anew every time. As of mid-2026, we already have these tools (unexhaustive):

**Custom GPTs** (OpenAI ChatGPT): a saved persona with instructions, optional reference files, and optional connections to outside services.
**Gems** (Google Gemini): a saved persona with instructions.
**NotebookLM** (Google): a notebook of user-supplied documents that the system reads before answering questions about them.
**Projects** (Anthropic Claude, and a similarly named feature in ChatGPT): a workspace with standing instructions and attached files shared across many conversations.
**Artifacts** (Anthropic Claude): documents and small applications produced within a conversation; a workspace convenience, not a change to the model.

## Take-home message

Training, fine-tuning, and prompting are three different ways of guiding a model to do some task. The first two change the model; the third does not. 

## References

Brown, Tom B., et al. "Language Models Are Few-Shot Learners." *Advances in Neural Information Processing Systems*, vol. 33, 2020, pp. 1877–901.
— Established that a built model can be steered by instructions and examples alone, the foundation of prompting.

Lewis, Patrick, et al. "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." *Advances in Neural Information Processing Systems*, vol. 33, 2020, pp. 9459–74.
— The paper behind supplying documents at question time rather than building them in.

Ouyang, Long, et al. "Training Language Models to Follow Instructions with Human Feedback." *Advances in Neural Information Processing Systems*, vol. 35, 2022, pp. 27730–44.
— An example of fine-tuning reshaping a model's behavior without starting over.

"Creating a GPT." *OpenAI Help Center*, help.openai.com/en/articles/8554397-creating-a-gpt. Accessed July 2026.

"Gemini Gems Overview." *Google Gemini Help*, support.google.com/gemini. Accessed July 2026.

"NotebookLM Help." *Google Support*, support.google.com/notebooklm. Accessed July 2026.

"What Are Projects?" *Anthropic Help Center*, support.claude.com. Accessed July 2026.

"Models." *Hugging Face*, huggingface.co/models. Accessed July 2026.
— Browsing the fine-tuned variants of any popular model makes the scale of individual fine-tuning concrete.

## Appendix: A Short Glossary that you might meet when using AIs 

**Token.** The unit a model reads and writes; roughly a short word or word fragment. Model pricing, limits, and "length" are all measured in tokens.

**Context window.** The maximum amount of text (in tokens) a model can consider at once: the conversation so far, the instructions, and any supplied documents. Everything prompting supplies lives inside this window. What falls outside it, the model cannot see.

**Hallucination.** Confident, fluent output that is wrong or fabricated. It follows from how generation works: the model continues text plausibly rather than looking facts up, so fluency and truth are not correlated. 

**Parametric knowledge.** What training and fine-tuning left inside the model. It is not memory in the everyday sense: nothing is stored as records that can be looked up, cited, or deleted. It is closer to absorbed habit — patterns distilled from the material the model was built on. This is why a model can "know" something without being able to say where it came from, and why hallucination is a built-in tendency rather than an occasional bug.

**Retrieved knowledge.** One family of responses to hallucination: instead of relying on parametric knowledge, fetch the needed material from outside sources at question time. The materials are current, citable, and swappable. Retrieval reduces hallucination but does not eliminate it. The idea appears under many names, a non-exhaustive family: **RAG** (retrieval-augmented generation, the original academic term for fetching documents before answering), **grounding** or **web search** (fetching from the live web, often with citations), **source-based tools** (systems like NotebookLM that answer only from the documents given), and **tool calling** (handing a sub-task the model would guess at, such as arithmetic, to a reliable outside tool such as a calculator). The names change; the move is the same: don't ask the model to remember what it can be handed.
