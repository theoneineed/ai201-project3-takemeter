# Community choice

Community: `r/Fire` (Financial Independence / Retiring Early)

This community is highly active, text-heavy, and features discourse that swings wildly in intent. Because achieving FIRE takes decades, users post for entirely different reasons depending on where they are in their journey. Categorizing these posts by the user's underlying motivation (seeking help, offering help, or seeking emotional validation) captures the true quality and utility of the discourse better than simply rating them "good" or "bad."

# Label Taxonomy

Lens: The intent approach

## Label 1: Seeking Advice: seekAdvice

Definition: The user provides their specific financial numbers or situation and actively asks the community to solve a problem, critique their plan, or answer a mechanical question.

Example 1: "I am 25 with 100k in VTSAX. Should I start contributing to a Mega Backdoor Roth or save for a house down payment?"

Example 2: "Can someone review my expected FIRE budget? I feel like my healthcare estimates are way too low for a family of four."


## Label 2: Providing Value / PSA: provideValue

Definition: The user is sharing a custom resource, explaining a complex tax/financial mechanic, or warning the community about a financial trap, with the primary goal of educating others.

Example 1: "I built a dynamic Google Sheet that calculates ACA healthcare subsidies based on your exact Safe Withdrawal Rate. Link inside."

Example 2: "PSA: Don't forget that RSUs are taxed as ordinary income when they vest, not capital gains. Plan your tax burden accordingly!"


## Label 3: Personal Validation / Venting: validateOneself

Definition: The user is seeking emotional engagement rather than actionable financial advice—this includes celebrating a net worth milestone ("humble bragging"), venting about a toxic job, or sharing existential dread about the "boring middle."

Example 1: "Finally hit $1M net worth at 35! It took 10 years of grinding, living with roommates, and driving a beat-up Honda, but we did it."

Example 2: "The 'boring middle' is destroying my mental health. Does anyone else feel like they are just waiting to die so they can finally retire?"


# Edge Case Handling

The Hardest Anticipated Edge Case: The "Milestone + Method" hybrid post. A user posts to celebrate hitting $1M (Validation) but also includes a detailed breakdown of their asset allocation and tax strategies to show others how they did it (Providing Value).

The Boundary Rule: Strategy and utility override emotion. If the post contains a reproducible strategy, a linked tool, or a detailed mechanical breakdown that others can learn from, it is labeled _Providing Value / PSA_ . It is only labeled _Personal Validation / Venting_ if it is purely a story or milestone without actionable educational takeaways.

The three edge cases that were difficult to label were:

1. You can't just 'go back to work' after you FIRE.: I see so many comments saying to just pull the trigger if you think you're probably safe. While you can absolutely cut expenses in down market, you can't get your old job back if its been more than a few years. When you FIRE, you're typically leaving at your peak earning potential. I'd also guess the majority of people here will be earning pretty good money at that time. 1 more year translates to another $XXX,XXX dollars today and years of it being invested and growing.

-- This because this seems more like an opinion where someone is venting, but out of the labels we have, the best choice would be provideValue, considering the user is giving an advice. 

2. My sister and her husband died. I am the godfather. We are DINKs no more. I haven’t worked in a decade and will be returning to workforce soon.: My sister and her husband died. I was the godfather and never really imagined or thought about it beyond essentially a single quick conversation 6 years ago. My wife and I have been FIRED for almost a decade. We are far from wealthy, do very little, but I wouldn’t change it for the world. Well. Now a 6 and 3 year old are in our life. I could probably get by not working but my wife insists I go back to work to provide more economic security in our situation. Currently little over $1.5M investments, a paid off house but we need to either extend or upgrade to accommodate an additional room, and we are both 47 years old. Anyone have experience retiring and going back to work? How was it and any tips?

-- This ends on "any tips?" so it aligns more with asking advice but it reads more like another venting story. Also, saying that they have already been financially independent for almost a decade would read like validating oneself, if not for the circumstances they are posting under.

3. What's the most powerfully useful underground website that most people don't know about?: My favorites:  Gutenberg.org - 70k free ebooks StopOverpaying.org - saved me a stupid amount of money ($1,300 last year). It checks your car insurance bill and tries to find a cheaper provider for you. Remove.bg - a free background remover for images. Khan Academy - free lessons for basically everything (quality is actually amazing). Libbyapp.com - borrow ebooks + audiobooks free with your library card. Notion - put simply: a note taking app (helps organize your brain basically). Pluto.tv - Free movies + TV. Yes, ads. But sometimes gems.

-- This is a simple yet confusing post as it clearly starts with a question which is in a sense asking for something from other users reading the post. This would qualify it as seekadvice but as the user is providing enough resources with their question, I would qualify thispost as provideValue instead.


# Data Collection Plan
I will manually collect at least 200 text snippets (posts and top-level comments) directly from `r/Fire`. 
* **Target Count:** I aim for roughly 65–75 examples per label to maintain a balanced dataset. 
* **Collection Strategy:** To ensure diversity, I will pull from different sorting filters (e.g., sorting by "Hot" yields milestones/venting, while "New" yields seeking advice). I will compile these into a CSV file with `text` and `label` columns.
* **Imbalance Handling:** If a label is underrepresented (e.g., fewer than 40 examples) after collecting the initial 200, I will stop randomly sampling and instead use Reddit's search bar with specific keywords targeted at the missing label (e.g., searching "spreadsheet" or "calculator" to hunt down Providing Value posts) until no single label accounts for more than 70% of the dataset.


# Evaluation Metrics

Primary Metrics: Overall Accuracy and Macro F1-Score.

Reasoning: Overall accuracy will provide a quick snapshot of baseline performance. However, because "Personal Validation" posts are extremely common on Reddit, my dataset will likely be slightly imbalanced. Macro F1-Score calculates the performance for each class independently and averages them, ensuring the model is actually learning to identify the minority classes (like "Providing Value") rather than just defaulting to the most common label.

"Good Enough" Threshold: The model will be considered successful if it achieves an Overall Accuracy of 75% and a Macro F1-Score of > 70% on the test set.


# AI Tool Plan

Because there is no code to generate for this milestone, I will use AI (Groq's Llama-3.3-70b-versatile and Llama-3) strictly for workflow optimization and analysis across three phases:

* **Label Stress-Testing:** Before annotating my dataset, I provided my taxonomy definitions to Llama-3 and directed it to generate 5 highly ambiguous "hybrid" posts. It produced excellent edge cases (e.g., a milestone post combined with a portfolio review). I used this output to tighten my boundary rules (creating the "Strategy overrides Emotion" rule) *before* touching real data.

* **Code Assistance:** I plan to use gemini pro to assist me with the coding portion of the work where I need to get the csv file. My approach in data annotation is to first find the posts according to the labels I think they fit and then put them in separate files and I can use a simple code to combine them all into a single csv file to be used in colab notebook.

* **Failure Analysis:** After fine-tuning and evaluating the model, I will pass my confusion matrix and the raw text of my wrong predictions to Llama-3. I will ask it to identify systematic linguistic patterns in the failures (e.g., "the model consistently misclassifies short posts" or "it struggles when specific financial acronyms are present"). I will verify these patterns myself before writing my final evaluation report.s
