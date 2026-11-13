# Graph skill source discovery

Inspected 2026-11-13 as public-source inspiration, not instructions to execute.

- Source: [ruvnet/ruflo kg-traverse](https://github.com/ruvnet/ruflo/blob/002d8c1ac031871fc14220e964f4dbb35b60428f/plugins/ruflo-knowledge-graph/skills/kg-traverse/SKILL.md).
- Repository commit observed through GitHub API: `002d8c1ac031871fc14220e964f4dbb35b60428f`; file blob: `40b2eda07d5b2c0ba3e55f226323265ea0a54fd9`.
- GitHub license metadata reported MIT at inspection. Recheck the license at the intended revision before any future copying or distribution of source content.
- Relevant idea: make traversal depth, relationship filtering and unavailable-edge evidence visible to the user.
- Generalization decision: retain explicit traversal boundaries, reproducible witnesses and truthful stopping evidence. Keep implementation-specific tools, numerical defaults and release-dependent behavior out of portable instructions.
- GRF-006 was independently authored from the queue and catalog comparison before this pinned inspection. It is not a copied or ported implementation of this source. No external code was executed or copied. Its general breadth-first fixture and review evidence remain the basis for acceptance.
- Potential later work: relevance-ranked path retrieval is distinct from bounded reachability and must undergo a fresh overlap and evidence review before authoring; this discovery does not establish a completed retrieval skill.
