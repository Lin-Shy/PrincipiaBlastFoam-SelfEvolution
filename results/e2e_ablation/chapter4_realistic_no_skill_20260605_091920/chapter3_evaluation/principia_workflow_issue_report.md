# PrincipiaBlastFoam Workflow 问题报告

说明：本报告只记录评测中暴露的问题，没有修改原始 workflow 代码。

## 终态分布

- success: 7
- execution_failed: 3
- workflow_state_mismatch: 1
- artifact_incomplete: 1

## 高频问题

- observed OpenFOAM warning: openfoam_warning: 7
- observed OpenFOAM warning: charge_mass_discretization: 6
- failed check: workflow exit_code zero: 5
- failed check: workflow failure absent: 5
- observed OpenFOAM nonblocking warning: mesh_default_patch: 4
- failed check: OpenFOAM blocking diagnostics absent: 4
- failed check: execution completed: 4
- failed check: review report present: 4
- failed check: solver log clean End: 4
- missing review_report.md: 4
- observed OpenFOAM blocking diagnostic: openfoam_fatal: 4
- observed workflow issue: run_status not completed: 4
- observed workflow issue: validation_status failed after execution gate: 4
- observed OpenFOAM nonblocking warning: probe_location_adjusted: 3
- observed OpenFOAM nonblocking warning: mesh_boundary_update: 2
- observed workflow issue: agent attempted to read a non-existent path: 2
- observed OpenFOAM nonblocking warning: fieldMinMax references missing dynamicP object: 1
- observed OpenFOAM blocking diagnostic: postprocessing_missing_pressure_field: 1
- observed post-processing issue: calculateImpulse could not resolve pressure output: 1
- observed OpenFOAM warning: blast_function_library_unavailable: 1

## 按样例列出的错误片段

### surface_burst_scaled_probe_smoke

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_no_skill_20260605_091920/chapter3_evaluation/raw_e2e_runs/run_20260605_091920/cases/surface_burst_scaled_probe_smoke`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_no_skill_20260605_091920/chapter3_evaluation/raw_e2e_runs/run_20260605_091920/benchmark_report.json`

```text
log.blastFoam: --> FOAM Warning :     functionObjects::fieldMinMax fieldMinMax cannot find required object dynamicP
Selected 0 cells for refinement out of 712.
Selected 50 split edges out of a possible 73.
```

```text
surface_burst_scaled_probe_smoke.log: content='\n--> FOAM Warning :     functionObjects::fieldMinMax fieldMinMax cannot find required object dynamicP\nSelected 18 cells for refinement out of 2413.\nRefined from 2413 to 2467 cells.\n--> FOAM Warning :     functionObjects::fieldMinMax fieldMinMax cannot find required object dynamicP\n--> FOAM Warning :     functionObjects::fieldMinMax fieldMinMax cannot find required object dynamicP\nSelected 7 split edges out of a possible 506.\nUnrefined from 2467 to 2446 cells.\n--> FOAM Warning :     functionObjects::fieldMinMax fieldMinMax cannot find required object dynamicP\n--> FOAM Warning :     functionObjects::fieldMinMax fieldMinMax cannot find required object dynamicP\nCourant Number Mean/Max = 0.00594346765051, 0.496738671229\ndeltaT = 7.47012851058e-06\nTime = 0.000901195\n\nCalculating Fluxes\nRK2SSP: step 1\nSolving compressibleSystem:\n\nRK2SSP: step 2\nSolving compressibleSy
```

### building_facade_pressure_probe_smoke

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_no_skill_20260605_091920/chapter3_evaluation/raw_e2e_runs/run_20260605_091920/cases/building_facade_pressure_probe_smoke`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_no_skill_20260605_091920/chapter3_evaluation/raw_e2e_runs/run_20260605_091920/benchmark_report.json`

```text
log.blastFoam: [0] 
[0] --> FOAM FATAL ERROR: 
[0] No mass was found in the region specified for activation of detonation point (0 0 0.5)
[0]
```

```text
log.calculateImpulse: Build  : 9-89839ae3b8cd
Exec   : calculateImpulse pressureProbes -p p
Date   : Jun 05 2026
Time   : 09:33:09
```

```text
building_facade_pressure_probe_smoke.log: content='#!/bin/sh\ncd ${0%/*} || exit 1    # run from this directory\n\n# Source tutorial run functions\n. $WM_PROJECT_DIR/bin/tools/RunFunctions\n\n# -- Create paraview file\nparaFoam -builtin -touch\n\n# -- Pre-process the stl\nrunApplication surfaceFeatures\n\n# -- Create the mesh for the fluid\nrunApplication blockMesh\n\n# -- Decompose the mesh\nrunApplication decomposePar -copyZero\n\n# -- Cut out the stl\nrunParallel snappyHexMesh -overwrite\n\n# -- Add internal patch\nrunParallel addEmptyPatch internalPatch internal -overwrite\n\n# -- Set the initial conditions for the fluid\nrunParallel setRefinedFields\n\n#- Run the calc\nrunParallel $(getApplication)\n\n#- Sample all times with twice the time resolution\nrunParallel -s ground blastToVTK ground -dt 2.5e-5 \\\n     -interpolationScheme cubicClamp\nrunParallel -s walls blastToVTK walls -dt 2.5e-5 \\\n     -interpolationScheme li
```

### erdc_internal_airblast_vent_pipe_probe

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_no_skill_20260605_091920/chapter3_evaluation/raw_e2e_runs/run_20260605_091920/cases/erdc_internal_airblast_vent_pipe_probe`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_no_skill_20260605_091920/chapter3_evaluation/raw_e2e_runs/run_20260605_091920/benchmark_report.json`

```text
erdc_internal_airblast_vent_pipe_probe.log: content='/*---------------------------------------------------------------------------*\\\n  =========                 |\n  \\\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox\n   \\\\    /   O peration     | Website:  https://openfoam.org\n    \\\\  /    A nd           | Version:  9\n     \\\\/     M anipulation  |\n\\*---------------------------------------------------------------------------*/\nBuild  : 9-89839ae3b8cd\nExec   : blastFoam\nDate   : Jun 05 2026\nTime   : 09:37:05\nHost   : "liuliang6Rm80Xos9qrQ"\nPID    : 725998\nI/O    : uncollated\nCase   : /data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_no_skill_20260605_091920/chapter3_evaluation/raw_e2e_runs/run_20260605_091920/cases/erdc_internal_airblast_vent_pipe_probe\nnProcs : 1\nsigFpe : Enabling floating point exception trapping (FOAM_SIGFPE).\nfileModificati
```

### reconass_400kg_external_facade_smoke

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_no_skill_20260605_091920/chapter3_evaluation/raw_e2e_runs/run_20260605_091920/cases/reconass_400kg_external_facade_smoke`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_no_skill_20260605_091920/chapter3_evaluation/raw_e2e_runs/run_20260605_091920/benchmark_report.json`

```text
log.blastFoam: [1] 
[1] --> FOAM FATAL ERROR: 
[1] surfaceFieldValue facadeSurfaceFieldValue: faceZone(facadeFaceZone):
    Region has no faces
```

```text
log.calculateImpulse: Build  : 9-89839ae3b8cd
Exec   : calculateImpulse pressureProbes
Date   : Jun 05 2026
Time   : 09:47:18
```

```text
reconass_400kg_external_facade_smoke.log: content='#!/bin/sh\ncd ${0%/*} || exit 1    # run from this directory\n\n# Source tutorial run functions\n. $WM_PROJECT_DIR/bin/tools/RunFunctions\n\n# -- Create paraview file\nparaFoam -builtin -touch\n\n# -- Pre-process the stl\nrunApplication surfaceFeatures\n\n# -- Create the mesh for the fluid\nrunApplication blockMesh\n\n# -- Decompose the mesh\nrunApplication decomposePar -copyZero\n\n# -- Cut out the stl\nrunParallel snappyHexMesh -overwrite\n\n# -- Add internal patch\nrunParallel addEmptyPatch internalPatch internal -overwrite\n\n# -- Set the initial conditions for the fluid\nrunParallel setRefinedFields\n\n#- Run the calc\nrunParallel $(getApplication)\n\n#- Sample all times with twice the time resolution\nrunParallel -s ground blastToVTK ground -dt 2.5e-5 \\\n     -interpolationScheme cubicClamp\nrunParallel -s walls blastToVTK walls -dt 2.5e-5 \\\n     -interpolationScheme li
```

### bls_two_box_interference_pressure_history

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_no_skill_20260605_091920/chapter3_evaluation/raw_e2e_runs/run_20260605_091920/cases/bls_two_box_interference_pressure_history`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_no_skill_20260605_091920/chapter3_evaluation/raw_e2e_runs/run_20260605_091920/benchmark_report.json`

```text
log.calculateImpulse: Build  : 9-89839ae3b8cd
Exec   : calculateImpulse pressureProbes
Date   : Jun 05 2026
Time   : 10:12:00
```

```text
bls_two_box_interference_pressure_history.log: content='#!/bin/sh\ncd ${0%/*} || exit 1    # run from this directory\n\n# Source tutorial run functions\n. $WM_PROJECT_DIR/bin/tools/RunFunctions\n\n# -- Create paraview file\nparaFoam -builtin -touch\n\n# -- Pre-process the stl\nrunApplication surfaceFeatures\n\n# -- Create the mesh for the fluid\nrunApplication blockMesh\n\n# -- Decompose the mesh\nrunApplication decomposePar -copyZero\n\n# -- Cut out the stl\nrunParallel snappyHexMesh -overwrite\n\n# -- Add internal patch\nrunParallel addEmptyPatch internalPatch internal -overwrite\n\n# -- Set the initial conditions for the fluid\nrunParallel setRefinedFields\n\n#- Run the calc\nrunParallel $(getApplication)\n\n#- Sample all times with twice the time resolution\nrunParallel -s ground blastToVTK ground -dt 2.5e-5 \\\n     -interpolationScheme cubicClamp\nrunParallel -s walls blastToVTK walls -dt 2.5e-5 \\\n     -interpolationScheme li
```

### hemicylinder_obstacle_reflection_probe_smoke

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_no_skill_20260605_091920/chapter3_evaluation/raw_e2e_runs/run_20260605_091920/cases/hemicylinder_obstacle_reflection_probe_smoke`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_no_skill_20260605_091920/chapter3_evaluation/raw_e2e_runs/run_20260605_091920/benchmark_report.json`

```text
hemicylinder_obstacle_reflection_probe_smoke.log: content='Good — no runtime output, the case has not been run yet. Now I have all the information needed. Let me compile the physics report.\n\n---\n\n# Physics Report: hemicylinder_obstacle_reflection_probe_smoke\n\n## 1. Case Identification\n\n| Item | Value |\n|------|-------|\n| **Tutorial base** | `blastFoam/movingCone` (per `README.md`) |\n| **Solver** | `blastFoam` (single-phase, per `constant/phaseProperties`: `type basic`) |\n| **Mesh type** | 2D wedge (axisymmetric), `movingAdaptiveFvMesh` |\n| **Case status** | **Not yet run** — no time directories, no `postProcessing/` |\n\n## 2. Current Geometry & Mesh (`system/blockMeshDict`)\n\n- **Domain**: 2D wedge (1 cell thick in θ), `convertToMeters 0.001` → mm scale.\n- **X-range**: -10 to 2 (i.e., -0.01 m to 0.002 m in physical units).\n- **Y (radial)**: 0 to ~4.98 (≈ 0.005 m).\n- **Obstacle**: A **moving cone** defined by the `movin
```

### three_level_building_room_pressure_smoke

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_no_skill_20260605_091920/chapter3_evaluation/raw_e2e_runs/run_20260605_091920/cases/three_level_building_room_pressure_smoke`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_no_skill_20260605_091920/chapter3_evaluation/raw_e2e_runs/run_20260605_091920/benchmark_report.json`

```text
log.calculateImpulse: Build  : 9-89839ae3b8cd
Exec   : calculateImpulse pressureProbes
Date   : Jun 05 2026
Time   : 10:37:00
```

```text
three_level_building_room_pressure_smoke.log: content='#!/bin/sh\ncd ${0%/*} || exit 1    # run from this directory\n\n# Source tutorial run functions\n. $WM_PROJECT_DIR/bin/tools/RunFunctions\n\n# -- Create paraview file\nparaFoam -builtin -touch\n\n# -- Pre-process the stl\nrunApplication surfaceFeatures\n\n# -- Create the mesh for the fluid\nrunApplication blockMesh\n\n# -- Decompose the mesh\nrunApplication decomposePar -copyZero\n\n# -- Cut out the stl\nrunParallel snappyHexMesh -overwrite\n\n# -- Add internal patch\nrunParallel addEmptyPatch internalPatch internal -overwrite\n\n# -- Set the initial conditions for the fluid\nrunParallel setRefinedFields\n\n#- Run the calc\nrunParallel $(getApplication)\n\n#- Sample all times with twice the time resolution\nrunParallel -s ground blastToVTK ground -dt 2.5e-5 \\\n     -interpolationScheme cubicClamp\nrunParallel -s walls blastToVTK walls -dt 2.5e-5 \\\n     -interpolationScheme li
```

### gable_roof_building_envelope_pressure_smoke

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_no_skill_20260605_091920/chapter3_evaluation/raw_e2e_runs/run_20260605_091920/cases/gable_roof_building_envelope_pressure_smoke`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_no_skill_20260605_091920/chapter3_evaluation/raw_e2e_runs/run_20260605_091920/benchmark_report.json`

```text
log.calculateImpulse: Build  : 9-89839ae3b8cd
Exec   : calculateImpulse pressureProbes
Date   : Jun 05 2026
Time   : 10:45:25
```

```text
gable_roof_building_envelope_pressure_smoke.log: content='#!/bin/sh\ncd ${0%/*} || exit 1    # run from this directory\n\n# Source tutorial run functions\n. $WM_PROJECT_DIR/bin/tools/RunFunctions\n\n# -- Create paraview file\nparaFoam -builtin -touch\n\n# -- Pre-process the stl\nrunApplication surfaceFeatures\n\n# -- Create the mesh for the fluid\nrunApplication blockMesh\n\n# -- Decompose the mesh\nrunApplication decomposePar -copyZero\n\n# -- Cut out the stl\nrunParallel snappyHexMesh -overwrite\n\n# -- Add internal patch\nrunParallel addEmptyPatch internalPatch internal -overwrite\n\n# -- Set the initial conditions for the fluid\nrunParallel setRefinedFields\n\n#- Run the calc\nrunParallel $(getApplication)\n\n#- Sample all times with twice the time resolution\nrunParallel -s ground blastToVTK ground -dt 2.5e-5 \\\n     -interpolationScheme cubicClamp\nrunParallel -s walls blastToVTK walls -dt 2.5e-5 \\\n     -interpolationScheme li
```

### vertical_wall_shielding_probe_line_smoke

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_no_skill_20260605_091920/chapter3_evaluation/raw_e2e_runs/run_20260605_091920/cases/vertical_wall_shielding_probe_line_smoke`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_no_skill_20260605_091920/chapter3_evaluation/raw_e2e_runs/run_20260605_091920/benchmark_report.json`

```text
vertical_wall_shielding_probe_line_smoke.log: --- Workflow Run Test Failed ---
❌ report is a placeholder continuation response; physics_report is shorter than the minimum content contract
❌ validation_status is failed
```

## 需要人工确认的代码层风险

- metrics 现在优先按 `user_request` 精确匹配；若未来 `metrics_report` 缺失，应改为以 `task_id/run_id/case_id` 绑定。
- 历史结果中曾出现 `orchestrator_empty_output_absent=False`，后续仍应保留 structured routing 回归测试。
- 若 `execution_status_completed=True` 且 solver 有 clean End 但 workflow 进程退出码仍为 1，应优先检查终态状态机和 reviewer 结果合并。