# Hermes Dependency

This project does not modify Hermes source code.

Hermes is used as an external runtime base for executing skill-injected prompts.
The added functionality lives in `PrincipiaBlastFoam-SelfEvolution`: skill extraction,
skill abstraction, skill retrieval, prompt construction, output redaction, and
run metadata capture.

## Invocation Boundary

Default invocation:

```bash
/data/bin/hermes -z "<skill-injected prompt>"
```

The wrapper script stores only the reproducibility evidence needed by the
thesis experiment:

- injected prompt;
- redacted Hermes output;
- selected skill ids and retrieval scores;
- command, working directory, exit code, and elapsed time.

The following Hermes runtime state is intentionally not archived as project
source:

- `/data/hermes-home/.hermes/.env`
- `/data/hermes-home/.hermes/state.db`
- `/data/hermes-home/.hermes/sessions/`
- account, cache, gateway, and authentication state.

If Hermes itself is ever changed, archive that change as a patch or commit
reference rather than copying the runtime home directory.
