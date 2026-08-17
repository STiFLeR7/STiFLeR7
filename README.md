<div align="center">

<sub>VOL. 01 — IN CIRCULATION &nbsp;·&nbsp; WINTER 2026 &nbsp;·&nbsp; ISSN 2749–0041</sub>

# H I L L &nbsp;&nbsp; P A T E L

<sub>A JOURNAL OF AI SYSTEMS ARCHITECTURE</sub><br />
<sub>**APPENDIX A** — SOURCE &amp; WORKING NOTES</sub>

<br />

<sub>AI Systems Engineer, **CloudRedux** &nbsp;·&nbsp; Pune, Maharashtra &nbsp;·&nbsp; `STiFLeR7`</sub>

<br />

<sub>[hillpatel.tech](https://hillpatel.tech) &nbsp;·&nbsp; [Résumé](https://hillpatel.tech) &nbsp;·&nbsp; [Begin a correspondence](mailto:stifler@hillpatel.tech)</sub>

</div>

---

<br />

> ### A model is a component, not a system.
>
> The model will keep getting better on its own. The parts that decide whether you can
> trust it — memory, recovery, governance — are the parts we still build by hand.
>
> <sub>— *Vol. 01, §01 Thesis Field Notes*</sub>

<br />

This appendix records the source. Three systems, one concern each: **persistence**,
**recovery**, **orchestration**. Everything below is either shipped, licensed, and
installable — or explicitly marked as held.

<br />

## §01 &nbsp; The Register

<br />

**№ 01** &nbsp;·&nbsp; **[memex](https://github.com/STiFLeR7/memex)** — *Persistence*
<sub>Python · MIT · ★12</sub>

Persistent memory for AI coding agents over the Model Context Protocol: a bitemporal
knowledge graph of your codebase, served to Claude Code, Cursor, Gemini CLI and any MCP
client. Tree-sitter + Gemini Flash → Neo4j via Graphiti. Twelve MCP tools, hierarchical
clusters, two-regime confidence decay.

`10k+` interactions before recall degrades &nbsp;·&nbsp; `0 drift` reconciled writes, no
silent contradiction &nbsp;·&nbsp; `pip install memex-mcp`

<br />

**№ 02** &nbsp;·&nbsp; **[Cairn](https://github.com/STiFLeR7/Cairn)** — *Recovery*
<sub>Python · Apache-2.0 · ★2</sub>

Recoverable long-horizon agents: a framework-agnostic reference harness plus a
recovery-faithful live benchmark. The thesis — *checkpoints are compactions* — argues
recovery is re-grounding, not replay.

`100%` resumable at last committed step &nbsp;·&nbsp; `<1s` median time to re-attach and
continue &nbsp;·&nbsp; **v1.0 held** pending a powered live-LLM study

<br />

**№ 03** &nbsp;·&nbsp; **[nexus](https://github.com/STiFLeR7/nexus)** — *Orchestration*
<sub>Python · MIT · ★2</sub>

A governed execution platform for autonomous agents: runtime orchestration, human
approval workflows, sandboxed execution, recovery, and operational intelligence over the
whole run.

`4 layers` agents · routing · policy · audit &nbsp;·&nbsp; `1:1` same input, same
execution plan

<br />

<sub>FIG. 01 — *How it fits.*</sub>

```
   request ──▶ nexus ──────────────────────────────▶ result
                 │  routing · policy · audit          ▲
                 │                                    │
                 ├──▶ memex   persistence  ───────────┤
                 │    bitemporal graph, Neo4j         │
                 │                                    │
                 └──▶ Cairn   recovery     ───────────┘
                      re-grounding, not replay
```

<br />

## §02 &nbsp; Field Notes

<sub>Smaller instruments, earlier volumes. Ordered by relevance, not stars.</sub>

<br />

| | | |
| :--- | :--- | ---: |
| **[imgshape](https://github.com/STiFLeR7/imgshape)** | Dataset intelligence for computer vision — deterministic fingerprints, explainable decisions, reproducible artifacts. `pip install imgshape` | <sub>MIT · ★4</sub> |
| **[Edge-LLM](https://github.com/STiFLeR7/Edge-LLM)** | Qwen2.5-3B under GPTQ: **5.75 GB → 1.93 GB**, faster inference, tuned for edge deployment. | <sub>Python · ★3</sub> |
| **[agentic-rag](https://github.com/STiFLeR7/agentic-rag)** | Agentic RAG engineered to run reliably on one 6 GB laptop GPU. Graph-based, controllable, explicit failure handling. | <sub>Phi-3 · Gemini</sub> |
| **[claude-plugins](https://github.com/STiFLeR7/claude-plugins)** | Claude Code marketplace — ships `memex-mcp` and [`prompt-forge`](https://github.com/STiFLeR7/prompt-forge), a prompt refinement engine. | <sub>MIT · ★3</sub> |
| **[DevPulseAIv3](https://github.com/STiFLeR7/DevPulseAIv3)** | Multi-agent LLM pipeline turning developer signals into real-time chat, REST API and scheduled digests. | <sub>FastAPI</sub> |
| **[personal-agent-os](https://github.com/STiFLeR7/personal-agent-os)** | Local-first agent that plans, executes and verifies. Designed to listen, remember, assist. | <sub>Python</sub> |

<sub>Also in circulation: [antigravity](https://github.com/STiFLeR7/antigravity) · [vision-to-action](https://github.com/STiFLeR7/vision-to-action) · [gradia](https://github.com/STiFLeR7/gradia) · [MedMNIST-EdgeAI](https://github.com/STiFLeR7/MedMNIST-EdgeAI) — [the full index →](https://github.com/STiFLeR7?tab=repositories)</sub>

<br />

## Interlude — on shipping

<br />

Constraint first. If it cannot run on 6 GB of consumer VRAM, it is not finished — cloud
GPUs are an optimisation, not a prerequisite.

Benchmarks before claims. Cairn is pinned at 0.x on purpose; the version number is a
statement about evidence, not about effort.

Published means installable. PyPI, a license, and documentation, or it stays a field note.

Failure modes go in writing — quantisation deltas, recall decay curves, recovery
latency. The number that embarrasses you is the one worth publishing.

<br />

## §03 &nbsp; Instruments

<br />

**Agent infrastructure** &nbsp; Model Context Protocol · bitemporal memory · knowledge
graphs · durable execution · re-grounding recovery · policy &amp; audit layers

**Retrieval** &nbsp; RAG · Agentic RAG · LangGraph · vector search · Neo4j · Graphiti ·
Tree-sitter

**Optimisation** &nbsp; GPTQ &amp; 1–8 bit quantisation · distillation · pruning · ONNX
Runtime · TensorRT · CUDA

**Learning** &nbsp; PyTorch · TensorFlow · Transformers · CNNs · multimodal · OpenCV

**Delivery** &nbsp; Python · TypeScript · FastAPI · Docker · GitHub Actions · Redis ·
GCP · AWS

<br />

## §04 &nbsp; Record

<br />

**Published** &nbsp; *Transforming Urban Solutions for Smart Cities through Crowdsourced
Feedback* — March 2025

**Certified** &nbsp; MCP Mastery, *Fractal Analytics* · RAG and Agentic AI, *Coursera* ·
Neural Networks with PyTorch, *Coursera*

<br />

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=STiFLeR7&show_icons=true&hide_border=true&bg_color=00000000&title_color=57606a&text_color=57606a&icon_color=57606a&hide_title=true&count_private=true" width="440" alt="GitHub statistics for STiFLeR7" />

<sub>FIG. 02 — *Telemetry.* 59 repositories, mostly Python. Since January 2024.</sub>

</div>

<br />

## §05 &nbsp; Colophon &amp; Correspondence

<br />

```yaml
editor:   Hill Patel — STiFLeR7
station:  CloudRedux · Pune, Maharashtra, India
volume:   01 — Persistent Systems
subject:  the architecture around the model
set in:   Python, mostly
```

[**hillpatel.tech**](https://hillpatel.tech) &nbsp;·&nbsp;
[LinkedIn](https://www.linkedin.com/in/hill-patel-stifler7/) &nbsp;·&nbsp;
[X](https://x.com/hillpatel07) &nbsp;·&nbsp;
[Medium](https://medium.com/@stiflerxd) &nbsp;·&nbsp;
[Hugging Face](https://huggingface.co/STiFLeR7) &nbsp;·&nbsp;
[stifler@hillpatel.tech](mailto:stifler@hillpatel.tech)

<br />

---

<div align="center">
<sub>© 2026 Hill Patel &nbsp;/&nbsp; Vol. 01 — Persistent Systems &nbsp;/&nbsp; Architect · Editorial · Engineer</sub>
</div>
