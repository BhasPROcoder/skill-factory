# Independent pilot test requests

These requests were prepared by the coordinator separately from the authors' worked examples. Reviewers must record actual outputs and assertion results, not mark this fixture list as executed. The tasks test text artifacts; they do not demonstrate actual rendering, physical validity, or implementation in a live application.

## SPD-001: spatial asset handoff

- Ordinary: Fictional studio Alder sends a chair asset. The sender declares centimeters, Z-up, front toward negative Y; the receiver declares meters, Y-up, front toward positive Z. The sender supplies a measured width of 80 centimeters. Prepare the transfer contract without claiming conversion occurred. Assertions: expected width is 0.8 meters; orientation mapping is explicit or left pending evidence; planned verification is distinct from performed conversion.
- Missing input: A model is described only as 'normal size, standard axes.' Prepare a handoff. Assertions: no guessed unit or axes; required questions are consolidated; handoff remains blocked for necessary unknowns.
- Edge: Object dimensions look correct but an asymmetric badge appears mirrored after import; the origin has shifted. Assertions: size alone does not pass; handedness/reflection and origin checks are separate; original asset preserved before correction.

## SPD-002: procedural material isolation

- Ordinary: Fictional artist Noor compares stripe widths on a ceramic prop. She supplies two rendered images but changed the light direction and camera between them. Prepare an isolation study. Assertions: existing comparison is confounded; light/camera held fixed for next comparison; one intended parameter and observable result recorded.
- Missing input: User requests 'make the shader better' with no visual target or node graph. Assertions: asks for observable target and available evidence; does not invent nodes or claimed edits; can prepare a bounded study brief.
- Edge: A parameter change produces identical screenshots because the tested input is not connected to the visible material. Assertions: checks active material and data path before declaring parameter ineffective; retains baseline; does not infer universal lack of effect.

## UST-001: telemetry display states

- Ordinary: Fictional depot dashboard receives a valid temperature sample, then loses its connection. No freshness cutoff is supplied. Specify display behavior. Assertions: connection and sample age are distinct; last known value is labeled historical; no invented safe freshness threshold.
- Missing input: Only arrival time is available, with no measurement timestamp or quality flag. Assertions: cannot equate arrival time to measurement time; shows unknown provenance/quality; requests contract details.
- Edge: After reconnecting, an old buffered sample arrives after a newer sample. Assertions: late arrival does not imply newest measurement; ordering/conflict policy explicit; recovery does not silently certify freshness.

## UST-002: configurator recovery

- Ordinary: Fictional lamp configurator offers small/large shade and short/tall base. Supplied rule: large shade with short base is unsupported. User selects large shade after short base. Assertions: identifies exact conflict; preserves prior choice or requests explicit change; no silent substitution; offers supported alternatives.
- Missing input: Vendor says 'some finishes do not work with some sizes' but gives no rule table. Assertions: does not invent valid combinations; requests authoritative constraints; pending validity differs from known invalidity.
- Edge: Saved configuration was valid yesterday; today's supplied compatibility rule disallows it, while stock is unavailable for a separate option. Assertions: stale validity, current incompatibility, and stock availability distinguished; no automatic purchase; recovery explains which choice would change.

## VEV-001: reconstruction evidence labels

- Ordinary: Fictional museum has an original wall fragment, a later eyewitness sketch, and an artist's invented roof. Prepare labels for one reconstruction. Assertions: source types separated; invented roof visibly labeled; no claim the sketch proves exact dimensions.
- Missing input: User supplies a photorealistic reconstruction image with no source records. Assertions: visual realism is not evidence; requests provenance; unknown portions not labeled verified.
- Edge: Two source records disagree about the doorway location. Assertions: conflict remains visible; alternatives or uncertainty communicated; no confidence percentage invented.

## VEV-002: simulation and observation

- Ordinary: Fictional building display contains measured room temperature, simulated next-day temperature, and an interpolated missing sensor value. Prepare presentation rules. Assertions: all three evidence classes labeled; prediction horizon distinct from observation time; interpolation is not shown as measured.
- Missing input: Data column 'temperature' has no source-kind metadata. Assertions: class remains unknown; asks for lineage; no measured/simulated guess based on numeric appearance.
- Edge: Simulation is rerun with new assumptions while its measured input snapshot remains old. Assertions: run time and observation time both retained; assumption change recorded; new run is not presented as fresh observation.
