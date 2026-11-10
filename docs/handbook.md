# Drone Video Privacy Studio handbook

By Jason Stys.

Review two manually authored keyframes using conservative privacy envelopes with private revision and export checks.

Review two manually authored keyframes using conservative privacy envelopes with private revision and export checks.

Makes redaction planning reproducible and keeps manual assumptions visible rather than claiming automatic recognition or tracking.

## Read the documentation

| Edition | Audience and contents |
| --- | --- |
| [project-guide.docx](reports/project-guide.docx) | User and developer guide: purpose, current usage, design, boundaries and source references. |

The editable Markdown remains the maintenance source. The Word files are readable editions. See [publication identities and review](reports/publications.json) and the [documentation refresh record](reports/documentation-refresh-2026-11-09.md).

## Current usage and help

[README quick start](../README.md) is the entry point. Use the project-specific guides below before changing inputs, operating modes or deployment assumptions.

### Usage and operations

- [OPERATIONS](OPERATIONS.md)
- [USER GUIDE](USER_GUIDE.md)

### Design and contracts

- [API](API.md)
- [ARCHITECTURE](ARCHITECTURE.md)
- [RESEARCH](RESEARCH.md)
- [SECURITY MODEL](SECURITY_MODEL.md)

### Security and validation

- [TESTING](TESTING.md)
- [VALIDATION](VALIDATION.md)

## Historical results and reproduction

The reviewed source is [`e61722c7780f3114a873ce8187b48104affeca7d`](https://github.com/JasonStys/drone-video-privacy-studio/tree/e61722c7780f3114a873ce8187b48104affeca7d). The observed functional workflow baseline is `e61722c7780f3114a873ce8187b48104affeca7d`; those observations are recorded at `2026-11-10T05:25:40.628667+00:00`. They do not certify an unrun later revision.

- [Detailed recorded validation](reports/PRACTICAL_WORKFLOWS_20261109.md)
- [Current Actions](https://github.com/JasonStys/drone-video-privacy-studio/actions) records later integration checks separately.
- Preserve dated measurements and follow the existing testing guide to reproduce them; a test-source inventory alone does not establish execution.

## Practical boundaries

- Two manually authored rectangle keyframes and linear assumptions, not automatic detection, recognition or identity tracking.
- Nonlinear movement or contextual identifiers require every-frame human review; envelopes can over-mask and do not certify anonymity.
- Workspace protection trusts the local OS owner; no real sensitive footage or operational surveillance validation is claimed.
- Source-first project with current package/service validation; no public native desktop application release is supplied.

## Maintaining these editions

Update the editable usage/design/test documents first. Rebuild and visually review every Word page and workbook tab before replacing an edition; verify the exact binary digests and evidence source in publications.json. Keep account data, logs with secrets, installed-app state and private test stores out of documentation. Source and release assets retain their existing security and licensing boundaries.
