# AI Study System & Note Generator 🎓

An academic study management system designed to generate structured learning notes, quizzes, and flashcards from technical sources following pedagogical frameworks (e.g., Bloom's Taxonomy).

---

## 📁 Project Structure

```
study_system/
├── .claude/
│   └── skills/
│       ├── notes-generator/  # Skill to compile source data into structured notes
│       │   ├── examples/     # Output examples
│       │   ├── references/   # Bloom's Taxonomy documentation
│       │   └── SKILL.md      # Skill configuration
│       └── skill-maker/      # Guide skill to build custom study skills
├── notes/
│   └── llm-20260110.md       # Detailed study notes on Large Language Models
├── flashcards/               # Spaced repetition card sets
├── quizes/                   # Assessment and self-testing files
├── CLAUDE.md                 # Agent guidelines, academic tone, and safety constraints
└── README.md                 # Project overview (this file)
```

---

## 🛠️ Core Capabilities

### 1. Notes Generator Skill (`notes-generator`)
Converts complex books, research papers, or lectures into educational notes. It enforces structure across **Bloom's Taxonomy Levels**:
1. **Remember**: Key terms, essential facts, and core concepts.
2. **Understand**: Explanations, comparisons, and interpretations of principles.
3. **Apply**: Practical exercises, code snippets, or real-world scenarios.
4. **Analyze**: Deconstruction, structural breakdown, and diagrams.
5. **Evaluate**: Critique, trade-off comparisons, and validation criteria.
6. **Create**: Design challenges, architectures, and synthesis prompts.

Check out the sample note structure in **[Large Language Models Notes](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/AI%20driven%20development/study_system/notes/llm-20260110.md)**.

### 2. Skill Maker Skill (`skill-maker`)
A helper skill designed to generate new modular Claude Code skills matching workspace standards. It reads standard schemas and outputs clean markdown templates.

---

## 📜 Academic Tone & Constraints (`CLAUDE.md`)

All documents and agent responses must maintain the rigorous standards defined in `CLAUDE.md`:
- **Formal Academic Tone**: Objective, third-person perspective with scholarly vocabulary. Avoid colloquialisms or contractions.
- **Precision**: Clear definition of technical terms upon first introduction.
- **Brevity**: Short, focused responses formatted using GitHub-flavored markdown. No excessive emojis.
- **Direct Disagreement**: The agent must challenge incorrect assertions with evidence, prioritizing factual correctness over compliance.
