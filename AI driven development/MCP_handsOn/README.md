# Model Context Protocol (MCP) Hands-on Lab 🌐

A workspace containing concrete implementations, token cost analyses, and browser automation test benches using the **Model Context Protocol (MCP)** and custom skills.

---

## 📁 Project Structure

```
MCP_handsOn/
├── claude-code-skills-lab-main/  # Sub-lab containing 13+ custom production-grade skills
│   ├── .claude/skills/           # Specific skills (xlsx, pptx, playwright, pdf, etc.)
│   └── README.md                 # Lab documentation
├── mcp-token-overhead-analysis.md # Detailed token cost audit of Playwright & Context7 servers
├── playwright-tasks.js           # Playwright automation script (Chromium)
└── README.md                     # Lab overview (this file)
```

---

## 🛠️ Lab Components

### 1. Claude Code Skills Lab (`claude-code-skills-lab-main`)
A comprehensive collection of 13 production-grade skills extending Claude Code's capabilities:
- **Automation**: `browsing-with-playwright`, `theme-factory`
- **Builders**: `docx`, `pdf`, `pptx`, `xlsx`, `internal-comms`, `fetch-library-docs`
- **Guides**: `doc-coauthoring`, `interview`, `skill-creator-pro`
- **Validators**: `skill-validator`

For more details on these skills, check the [Skills Lab README](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/AI%20driven%20development/MCP_handsOn/claude-code-skills-lab-main/README.md).

### 2. Token Overhead Analysis (`mcp-token-overhead-analysis.md`)
An analytical audit documenting the exact startup token cost of running MCP servers:
- **Playwright MCP Server**: ~2,860 tokens overhead (~130 tokens per tool across 22 tools).
- **Context7 MCP Server**: ~680 tokens overhead (across 5 tools).
- **Impact Analysis**: Calculated startup cost (~3,690 tokens) consuming 1.85% of a standard 200,000 context window (e.g. Claude 3.5 Sonnet).
- **Optimizations**: Recommends selective connection and disconnecting high-overhead servers when not executing task-specific automation.

For full breakdown, see the [Token Overhead Analysis](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/AI%20driven%20development/MCP_handsOn/mcp-token-overhead-analysis.md).

### 3. Playwright Automation Testbed (`playwright-tasks.js`)
A Node.js scripting file verifying local browser automation capabilities. It performs the following sequence:
- Launches a headless Chromium browser instance.
- **Task 1**: Navigates to `github.com`, waits for page load, and captures a full-page screenshot saved as `github-screenshot.png`.
- **Task 2**: Navigates to Hacker News (`news.ycombinator.com`) and extracts the page title.
- **Task 3**: Navigates to `example.com` and validates if the page contains the word "documentation".

---

## 🚀 Running Playwright Script

Ensure you have Node.js installed, then navigate to this directory and run:

```bash
# Navigate to the directory
cd MCP_handsOn

# Install Playwright dependencies
npm install playwright

# Run the automation script
node playwright-tasks.js
```
