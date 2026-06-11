# PrincipiaBlastFoam Workflow 问题报告

说明：本报告只记录评测中暴露的问题，没有修改原始 workflow 代码。

## 终态分布

- success: 7
- execution_failed: 4
- workflow_state_mismatch: 1

## 高频问题

- failed check: workflow exit_code zero: 5
- failed check: workflow failure absent: 5
- observed OpenFOAM warning: openfoam_warning: 5
- observed OpenFOAM nonblocking warning: mesh_default_patch: 4
- failed check: OpenFOAM blocking diagnostics absent: 4
- failed check: execution completed: 4
- failed check: review report present: 4
- failed check: solver log clean End: 4
- missing review_report.md: 4
- observed OpenFOAM blocking diagnostic: openfoam_fatal: 4
- observed workflow issue: run_status not completed: 4
- observed workflow issue: validation_status failed after execution gate: 4
- observed OpenFOAM warning: charge_mass_discretization: 4
- observed OpenFOAM nonblocking warning: probe_location_adjusted: 3
- observed OpenFOAM blocking diagnostic: parallel_internal_patch_missing: 3
- observed workflow issue: agent attempted to read a non-existent path: 3
- observed OpenFOAM blocking diagnostic: postprocessing_missing_pressure_field: 2
- observed post-processing issue: calculateImpulse could not resolve pressure output: 2
- observed OpenFOAM nonblocking warning: mesh_boundary_update: 2
- observed OpenFOAM nonblocking warning: fieldMinMax references missing dynamicP object: 1

## 按样例列出的错误片段

### surface_burst_scaled_probe_smoke

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/raw_e2e_runs/run_20260606_051308/cases/surface_burst_scaled_probe_smoke`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/raw_e2e_runs/run_20260606_051308/benchmark_report.json`

```text
log.blastFoam: --> FOAM Warning :     functionObjects::fieldMinMax fieldMinMax cannot find required object dynamicP
Selected 0 cells for refinement out of 712.
Selected 50 split edges out of a possible 73.
```

```text
surface_burst_scaled_probe_smoke.log: content='\n--> FOAM Warning :     functionObjects::fieldMinMax fieldMinMax cannot find required object dynamicP\nSelected 24 cells for refinement out of 2362.\nRefined from 2362 to 2434 cells.\n--> FOAM Warning :     functionObjects::fieldMinMax fieldMinMax cannot find required object dynamicP\n--> FOAM Warning :     functionObjects::fieldMinMax fieldMinMax cannot find required object dynamicP\nSelected 5 split edges out of a possible 499.\nUnrefined from 2434 to 2419 cells.\n--> FOAM Warning :     functionObjects::fieldMinMax fieldMinMax cannot find required object dynamicP\n--> FOAM Warning :     functionObjects::fieldMinMax fieldMinMax cannot find required object dynamicP\nCourant Number Mean/Max = 0.00577510241277, 0.484165730232\ndeltaT = 7.27793909612e-06\nTime = 0.000898109\n\nCalculating Fluxes\nRK2SSP: step 1\nSolving compressibleSystem:\n\nRK2SSP: step 2\nSolving compressibleSy
```

### building_facade_pressure_probe_smoke

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/raw_e2e_runs/run_20260606_051308/cases/building_facade_pressure_probe_smoke`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/raw_e2e_runs/run_20260606_051308/benchmark_report.json`

```text
log.blastFoam: [3] 
[3] --> FOAM FATAL ERROR: 
[3] No mass was found in the region specified for activation of detonation point (0 0 0.5)
[3]
```

```text
log.calculateImpulse: Build  : 9-89839ae3b8cd
Exec   : calculateImpulse pressureProbes -p p
Date   : Jun 06 2026
Time   : 05:28:07
```

```text
log.setRefinedFields: [2] 
[2] --> FOAM FATAL ERROR: 
[2] When balancing is enabled, an internal patch should be added to the mesh. 
	To add the necessary patch to the mesh and the fields, use the command
```

### reconass_400kg_external_facade_smoke

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/raw_e2e_runs/run_20260606_051308/cases/reconass_400kg_external_facade_smoke`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/raw_e2e_runs/run_20260606_051308/benchmark_report.json`

```text
log.blastFoam: [1] 
[1] --> FOAM FATAL ERROR: 
[1] When balancing is enabled, an internal patch should be added to the mesh. 
	To add the necessary patch to the mesh and the fields, use the command
```

```text
log.addEmptyPatch: --------------------------------------------------------------------------
mpirun noticed that process rank 1 with PID 0 on node liuliang6Rm80Xos9qrQ exited on signal 11 (Segmentation fault).
--------------------------------------------------------------------------
```

```text
log.calculateImpulse: Build  : 9-89839ae3b8cd
Exec   : calculateImpulse pressureProbes -p p
Date   : Jun 06 2026
Time   : 05:44:06
```

### bls_two_box_interference_pressure_history

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/raw_e2e_runs/run_20260606_051308/cases/bls_two_box_interference_pressure_history`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/raw_e2e_runs/run_20260606_051308/benchmark_report.json`

```text
log.calculateImpulse: Build  : 9-89839ae3b8cd
Exec   : calculateImpulse pressureProbes -p p
Date   : Jun 06 2026
Time   : 06:06:38
```

```text
bls_two_box_interference_pressure_history.log: content='#!/bin/sh\ncd ${0%/*} || exit 1    # run from this directory\n\n# Source tutorial run functions\n. $WM_PROJECT_DIR/bin/tools/RunFunctions\n\n# -- Create paraview file\nparaFoam -builtin -touch\n\n# -- Pre-process the stl\nrunApplication surfaceFeatures\n\n# -- Create the mesh for the fluid\nrunApplication blockMesh\n\n# -- Decompose the mesh\nrunApplication decomposePar -copyZero\n\n# -- Cut out the stl\nrunParallel snappyHexMesh -overwrite\n\n# -- Add internal patch\nrunParallel addEmptyPatch internalPatch internal -overwrite\n\n# -- Set the initial conditions for the fluid\nrunParallel setRefinedFields\n\n#- Run the calc\nrunParallel $(getApplication)\n\n#- Sample all times with twice the time resolution\nrunParallel -s ground blastToVTK ground -dt 2.5e-5 \\\n     -interpolationScheme cubicClamp\nrunParallel -s walls blastToVTK walls -dt 2.5e-5 \\\n     -interpolationScheme li
```

### vented_confined_gas_explosion_window_smoke

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/raw_e2e_runs/run_20260606_051308/cases/vented_confined_gas_explosion_window_smoke`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/raw_e2e_runs/run_20260606_051308/benchmark_report.json`

```text
vented_confined_gas_explosion_window_smoke.log: content='Error: File /data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/raw_e2e_runs/run_20260606_051308/cases/vented_confined_gas_explosion_window_smoke/constant/transportProperties does not exist. Resolved path: /data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/raw_e2e_runs/run_20260606_051308/cases/vented_confined_gas_explosion_window_smoke/constant/transportProperties.' name='read_file' tool_call_id='call_01_iOiqINbp3eJ5gbUPXJE20198'
```

### hemicylinder_obstacle_reflection_probe_smoke

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/raw_e2e_runs/run_20260606_051308/cases/hemicylinder_obstacle_reflection_probe_smoke`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/raw_e2e_runs/run_20260606_051308/benchmark_report.json`

```text
hemicylinder_obstacle_reflection_probe_smoke.log: content='[2] \nFOAM parallel run exiting\n[2] \n[3] \n[3] \n[3] --> FOAM FATAL ERROR: \n[3] cannot find file "/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/raw_e2e_runs/run_20260606_051308/cases/hemicylinder_obstacle_reflection_probe_smoke/processor3/0/U"\n[3] \n[3]     From function virtual Foam::autoPtr<Foam::ISstream> Foam::fileOperations::uncollatedFileOperation::readStream(Foam::regIOobject&, const Foam::fileName&, const Foam::word&, bool) const\n[3]     in file global/fileOperations/uncollatedFileOperation/uncollatedFileOperation.C at line 539.\n[3] \nFOAM parallel run exiting\n[3] \n[liuliang6Rm80Xos9qrQ:918138] PMIX ERROR: UNREACHABLE in file server/pmix_server.c at line 1741\n[1] #0  Foam::error::printStack(Foam::Ostream&) at ??:?\n[1] #1  Foam::sigSegv::sigHandler(int
```

### three_level_building_room_pressure_smoke

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/raw_e2e_runs/run_20260606_051308/cases/three_level_building_room_pressure_smoke`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/raw_e2e_runs/run_20260606_051308/benchmark_report.json`

```text
log.calculateImpulse: Build  : 9-89839ae3b8cd
Exec   : calculateImpulse pressureProbes
Date   : Jun 06 2026
Time   : 06:31:10
```

```text
three_level_building_room_pressure_smoke.log: content='#!/bin/sh\ncd ${0%/*} || exit 1    # run from this directory\n\n# Source tutorial run functions\n. $WM_PROJECT_DIR/bin/tools/RunFunctions\n\n# -- Create paraview file\nparaFoam -builtin -touch\n\n# -- Pre-process the stl\nrunApplication surfaceFeatures\n\n# -- Create the mesh for the fluid\nrunApplication blockMesh\n\n# -- Decompose the mesh\nrunApplication decomposePar -copyZero\n\n# -- Cut out the stl\nrunParallel snappyHexMesh -overwrite\n\n# -- Add internal patch\nrunParallel addEmptyPatch internalPatch internal -overwrite\n\n# -- Set the initial conditions for the fluid\nrunParallel setRefinedFields\n\n#- Run the calc\nrunParallel $(getApplication)\n\n#- Sample all times with twice the time resolution\nrunParallel -s ground blastToVTK ground -dt 2.5e-5 \\\n     -interpolationScheme cubicClamp\nrunParallel -s walls blastToVTK walls -dt 2.5e-5 \\\n     -interpolationScheme li
```

### gable_roof_building_envelope_pressure_smoke

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/raw_e2e_runs/run_20260606_051308/cases/gable_roof_building_envelope_pressure_smoke`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/raw_e2e_runs/run_20260606_051308/benchmark_report.json`

```text
log.blastToVTK.walls: [0] 
[0] --> FOAM FATAL ERROR: 
[0] Patch named walls not found.
Available patch names:
```

```text
log.calculateImpulse: Build  : 9-89839ae3b8cd
Exec   : calculateImpulse pressureProbes -p p
Date   : Jun 06 2026
Time   : 06:42:25
```

```text
gable_roof_building_envelope_pressure_smoke.log: content='#!/bin/sh\ncd ${0%/*} || exit 1    # run from this directory\n\n# Source tutorial run functions\n. $WM_PROJECT_DIR/bin/tools/RunFunctions\n\n# -- Create paraview file\nparaFoam -builtin -touch\n\n# -- Pre-process the stl\nrunApplication surfaceFeatures\n\n# -- Create the mesh for the fluid\nrunApplication blockMesh\n\n# -- Decompose the mesh\nrunApplication decomposePar -copyZero\n\n# -- Cut out the stl\nrunParallel snappyHexMesh -overwrite\n\n# -- Add internal patch\nrunParallel addEmptyPatch internalPatch internal -overwrite\n\n# -- Set the initial conditions for the fluid\nrunParallel setRefinedFields\n\n#- Run the calc\nrunParallel $(getApplication)\n\n#- Sample all times with twice the time resolution\nrunParallel -s ground blastToVTK ground -dt 2.5e-5 \\\n     -interpolationScheme cubicClamp\nrunParallel -s walls blastToVTK walls -dt 2.5e-5 \\\n     -interpolationScheme li
```

### vertical_wall_shielding_probe_line_smoke

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/raw_e2e_runs/run_20260606_051308/cases/vertical_wall_shielding_probe_line_smoke`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/raw_e2e_runs/run_20260606_051308/benchmark_report.json`

```text
log.blastFoam: [1] 
[1] --> FOAM FATAL ERROR: 
[1] No mass was found in the domain
[1]
```

```text
log.setRefinedFields: [1] 
[1] --> FOAM FATAL ERROR: 
[1] When balancing is enabled, an internal patch should be added to the mesh. 
	To add the necessary patch to the mesh and the fields, use the command
```

```text
vertical_wall_shielding_probe_line_smoke.log: content='Good. Now I have all the evidence needed. Let me compile the comprehensive Physics Report.\n\n---\n\n## Physics Report: Current Case State Analysis\n\n### 1. Case Identity & Provenance\n\n- **Selected tutorial**: `blastFoam/building3D` (L-shaped building with C4 detonation)\n- **Case path**: `.../vertical_wall_shielding_probe_line_smoke`\n- **Current state**: Files copied from tutorial but **no modifications applied yet** — the case is in its pristine tutorial state. Only the `0/` directory exists (no mesh, no solver output).\n\n### 2. Geometry & Mesh Assessment\n\n| Item | Current Value | Requirement | Status |\n|------|--------------|-------------|--------|\n| **blockMesh domain** | 10×10×5 m box, 20×20×10 cells (0.5 m base cell) | No domain expansion | ✅ OK |\n| **Wall geometry** | `L_Wall.stl` — L-shaped building, scale 0.001 | Vertical rigid wall for shielding | ⚠️ MISMATCH
```

## 需要人工确认的代码层风险

- metrics 现在优先按 `user_request` 精确匹配；若未来 `metrics_report` 缺失，应改为以 `task_id/run_id/case_id` 绑定。
- 历史结果中曾出现 `orchestrator_empty_output_absent=False`，后续仍应保留 structured routing 回归测试。
- 若 `execution_status_completed=True` 且 solver 有 clean End 但 workflow 进程退出码仍为 1，应优先检查终态状态机和 reviewer 结果合并。