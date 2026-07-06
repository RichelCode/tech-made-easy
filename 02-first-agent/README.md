# 🤖 Your First AI Agent (in Pure Python)

Hi, I'm Richel. This is a tiny AI agent you can run on your own laptop with nothing but plain Python. No API key, no signup, no cost.

It's part of my "Tech Made Easy" series, where I explain AI to beginners as someone still learning it too.

## What it does

You give the agent a goal, like "What is 12 * 8, and what is the weather in Accra?" and it works through it step by step. It thinks about what to do, picks a tool, uses it, looks at the result, and loops until the goal is done.

That think, act, look, repeat loop is the heart of every AI agent. Once you see it here, you understand the real thing.

## What you need

- Python 3.9 or newer. That's it. No packages to install.

## How to run it

Open a terminal in this folder and run:

```bash
python3 agent.py
```

You'll see the agent's whole thought process printed out, step by step, ending in a final answer.

## An honest note

In a real agent, a language model makes the decisions. Here, to keep it free and simple, those decisions are made with plain rules inside `decide_action()`. That's the one spot where a real model would slot in later. Everything else, the tools and the loop, works exactly like the grown-up version.

## The files

- `agent.py` is the whole agent: two tools, a simple brain, and the loop.

## 📖 Read the full walkthrough on Medium: [link coming soon]

---

Richel makes tech easy 💕
