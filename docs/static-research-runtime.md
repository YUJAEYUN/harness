# Code-first static research runtime

This runtime turns external API, disclosure, IR, and report data into a validated
static **Evidence Pack** before an AI analyst is invoked. It intentionally does
not operate a permanent market database.

## Responsibility boundary

| Deterministic code | AI agents |
|---|---|
| Download and preserve sources | Decompose ambiguous research questions |
| Normalize dates, units, and identifiers | Interpret economic meaning |
| Calculate and validate metrics | Build and challenge hypotheses |
| Hash raw inputs and reject invalid runs | Explain conclusions and uncertainty |
| Generate evidence packs and snapshot diffs | Request narrowly scoped follow-up evidence |

An agent must not browse first when the requested observation already exists in
the Evidence Pack. An agent must not recalculate a metric that the deterministic
pipeline can produce.

## Run modes and default budgets

| Mode | Typical use | Suggested AI budget |
|---|---|---:|
| `lookup` | One observed value | 0 agents |
| `explain` | Explain known facts | 1 agent, 1 round |
| `analyze` | Compare evidence and form a hypothesis | Up to 3 agents, 1 round |
| `deep_research` | Scenarios, red team, risk review | Explicitly approved full wave |

The request file stores the hard `agent_budget`; the Evidence Pack forwards that
budget to the orchestrator.

## Build a snapshot

From the repository root:

```bash
python -m research_snapshot build \
  --request examples/research_snapshot/request.json \
  --run-dir /tmp/sample-hyperscaler-capex
```

The run directory contains:

```text
request.json
run_manifest.json
raw/
normalized/observations.jsonl
evidence/evidence_pack.json
validation/validation_report.json
```

Raw files are copied into the snapshot and hashed. Normalized observations carry
the provider, publisher, source family, evidence grade, observation date, and
source row. A failed validation marks the Evidence Pack as blocked.

## Compare snapshots

```bash
python -m research_snapshot diff \
  --before runs/previous \
  --after runs/current \
  --output runs/current/change_set.json
```

The comparison reports additions, removals, and value changes using entity,
metric, observation date, and source family as the stable key. This enables
incremental research without a server database.

## Adding a real source

Implement the source as a declarative request entry when it returns CSV or JSON.
Keep authentication material outside request files. For PDF, HTML, or APIs with
custom pagination, add a small deterministic adapter that writes CSV or JSON,
then feed that output into this runtime. Preserve the original document beside
the extracted records and record both hashes in the adapter manifest.

Never average values merely because providers disagree. Keep separate
observations when dates, populations, accounting definitions, or source families
differ, and ask an agent to explain the difference only after code has preserved
it.

## Agent-authored dynamic collectors

An agent may write a short collector at runtime and ask the snapshot runtime to
execute it. This is the escape hatch for authenticated APIs, pagination, HTML,
PDF extraction, or browser automation. Dynamic execution is deliberately opt-in:
the top-level request must contain `"allow_dynamic_collectors": true`.

The collector must write a CSV or JSON record set to **stdout**. Diagnostics go
to stderr. The runtime invokes the command as an argument array without a shell,
captures stdout as the immutable raw input, saves stderr beside it, hashes the
declared collector code, and then runs the normal parser, normalization, and
validation pipeline. It also exposes `RESEARCH_RAW_DIR`; collectors should save
the original API response, HTML, PDF, screenshot, or browser download there.
Every file written there is hashed into the collector manifest.

```json
{
  "allow_dynamic_collectors": true,
  "sources": [{
    "id": "meta-capex",
    "type": "generated_json",
    "provider": "Meta investor relations",
    "publisher": "Meta",
    "source_family": "meta-official-ir",
    "evidence_grade": "A",
    "collector": {
      "command": ["python", "collectors/meta_capex.py"],
      "cwd": ".",
      "timeout_seconds": 120,
      "env": ["META_API_TOKEN"],
      "code_paths": ["collectors/meta_capex.py"]
    },
    "field_map": {
      "entity": "company",
      "metric": "metric",
      "value": "value",
      "unit": "unit",
      "observed_at": "observed_at"
    }
  }]
}
```

The same contract supports three acquisition styles:

1. **API collector:** generated Python calls an official API, follows pagination,
   and prints normalized candidate records as JSON.
2. **Browser collector:** generated Playwright/Selenium code opens a public page,
   downloads or extracts the document, and prints records as JSON. Browser
   dependencies must already exist in the runtime environment.
3. **Generated parser:** generated code reads a previously downloaded PDF/HTML,
   extracts tables, and prints CSV or JSON.

The agent is responsible for authoring the collector and registering the source;
the deterministic runtime remains responsible for execution limits, raw capture,
hashing, normalization, and fail-closed validation. API keys must be passed by
environment-variable name through `collector.env`, never embedded in the request
or generated script.

This feature executes code and can access the network and files available to the
process. Only enable it for trusted agents and run it inside the platform's normal
sandbox/container. The opt-in is a safety boundary, not a security sandbox.
