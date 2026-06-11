# PrincipiaBlastFoam Workflow 问题报告

说明：本报告只记录评测中暴露的问题，没有修改原始 workflow 代码。

## 终态分布

- success: 8
- execution_failed: 2
- workflow_state_mismatch: 1
- review_failed: 1

## 高频问题

- observed OpenFOAM warning: charge_mass_discretization: 7
- observed OpenFOAM warning: openfoam_warning: 5
- observed OpenFOAM nonblocking warning: mesh_default_patch: 4
- observed OpenFOAM nonblocking warning: probe_location_adjusted: 4
- observed OpenFOAM nonblocking warning: mesh_boundary_update: 3
- failed check: OpenFOAM blocking diagnostics absent: 3
- failed check: workflow exit_code zero: 3
- failed check: workflow failure absent: 3
- observed OpenFOAM blocking diagnostic: openfoam_fatal: 3
- failed check: execution completed: 2
- failed check: solver log clean End: 2
- observed workflow issue: run_status not completed: 2
- observed workflow issue: validation_status failed after execution gate: 2
- observed OpenFOAM nonblocking warning: fieldMinMax references missing dynamicP object: 1
- observed post-processing issue: calculateImpulse could not resolve pressure output: 1
- observed workflow issue: agent attempted to read a non-existent path: 1
- observed workflow issue: reviewer failed validation after solver execution: 1
- observed workflow issue: validation_status failed despite completed execution: 1
- failed check: review report present: 1
- missing review_report.md: 1

## 按样例列出的错误片段

### surface_burst_scaled_probe_smoke

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_concrete_from_chapter3_20260606_065034/chapter3_evaluation/raw_e2e_runs/run_20260606_065035/cases/surface_burst_scaled_probe_smoke`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_concrete_from_chapter3_20260606_065034/chapter3_evaluation/raw_e2e_runs/run_20260606_065035/benchmark_report.json`

```text
log.blastFoam: --> FOAM Warning :     functionObjects::fieldMinMax fieldMinMax cannot find required object dynamicP
Selected 0 cells for refinement out of 712.
Selected 50 split edges out of a possible 73.
```

```text
surface_burst_scaled_probe_smoke.log: content='Solving compressibleSystem:\n\nRK2SSP: step 2\nSolving compressibleSystem:\n\nPost-updating compressibleSystem:\n\nmax(p): 2676998.13135, min(p): 50432.5682575\nmax(T): 2456.69375717, min(T): 287.925643795\nExecutionTime = 16.27 s  ClockTime = 17 s\n\n--> FOAM Warning :     functionObjects::fieldMinMax fieldMinMax cannot find required object dynamicP\nSelected 3 cells for refinement out of 2644.\nRefined from 2644 to 2653 cells.\n--> FOAM Warning :     functionObjects::fieldMinMax fieldMinMax cannot find required object dynamicP\n--> FOAM Warning :     functionObjects::fieldMinMax fieldMinMax cannot find required object dynamicP\nSelected 5 split edges out of a possible 551.\nUnrefined from 2653 to 2638 cells.\n--> FOAM Warning :     functionObjects::fieldMinMax fieldMinMax cannot find required object dynamicP\n--> FOAM Warning :     functionObjects::fieldMinMax fieldMinMax cann
```

### building_facade_pressure_probe_smoke

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_concrete_from_chapter3_20260606_065034/chapter3_evaluation/raw_e2e_runs/run_20260606_065035/cases/building_facade_pressure_probe_smoke`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_concrete_from_chapter3_20260606_065034/chapter3_evaluation/raw_e2e_runs/run_20260606_065035/benchmark_report.json`

```text
log.calculateImpulse: Build  : 9-89839ae3b8cd
Exec   : calculateImpulse pressureProbes
Date   : Jun 06 2026
Time   : 07:05:51
```

```text
building_facade_pressure_probe_smoke.log: content='#!/bin/sh\ncd ${0%/*} || exit 1    # run from this directory\n\n# Source tutorial run functions\n. $WM_PROJECT_DIR/bin/tools/RunFunctions\n\n# -- Create paraview file\nparaFoam -builtin -touch\n\n# -- Pre-process the stl\nrunApplication surfaceFeatures\n\n# -- Create the mesh for the fluid\nrunApplication blockMesh\n\n# -- Decompose the mesh\nrunApplication decomposePar -copyZero\n\n# -- Cut out the stl\nrunParallel snappyHexMesh -overwrite\n\n# -- Add internal patch\nrunParallel addEmptyPatch internalPatch internal -overwrite\n\n# -- Set the initial conditions for the fluid\nrunParallel setRefinedFields\n\n#- Run the calc\nrunParallel $(getApplication)\n\n#- Sample all times with twice the time resolution\nrunParallel -s ground blastToVTK ground -dt 2.5e-5 \\\n     -interpolationScheme cubicClamp\nrunParallel -s walls blastToVTK walls -dt 2.5e-5 \\\n     -interpolationScheme li
```

### erdc_internal_airblast_vent_pipe_probe

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_concrete_from_chapter3_20260606_065034/chapter3_evaluation/raw_e2e_runs/run_20260606_065035/cases/erdc_internal_airblast_vent_pipe_probe`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_concrete_from_chapter3_20260606_065034/chapter3_evaluation/raw_e2e_runs/run_20260606_065035/benchmark_report.json`

```text
erdc_internal_airblast_vent_pipe_probe.log: content='    \\\\  /    A nd           | Version:  9\n     \\\\/     M anipulation  |\n\\*---------------------------------------------------------------------------*/\nBuild  : 9-89839ae3b8cd\nExec   : blastFoam\nDate   : Jun 06 2026\nTime   : 07:11:59\nHost   : "liuliang6Rm80Xos9qrQ"\nPID    : 947031\nI/O    : uncollated\nCase   : /data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_concrete_from_chapter3_20260606_065034/chapter3_evaluation/raw_e2e_runs/run_20260606_065035/cases/erdc_internal_airblast_vent_pipe_probe\nnProcs : 1\nsigFpe : Enabling floating point exception trapping (FOAM_SIGFPE).\nfileModificationChecking : Monitoring run-time modified files using timeStampMaster (fileModificationSkew 10)\nallowSystemOperations : Allowing user-supplied system call operations\n\n// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
```

### reconass_400kg_external_facade_smoke

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_concrete_from_chapter3_20260606_065034/chapter3_evaluation/raw_e2e_runs/run_20260606_065035/cases/reconass_400kg_external_facade_smoke`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_concrete_from_chapter3_20260606_065034/chapter3_evaluation/raw_e2e_runs/run_20260606_065035/benchmark_report.json`

```text
log.blastFoam: [1] 
[1] --> FOAM FATAL ERROR: 
[1] No cells will be activated using the detonation point (2.5 0 0.5)
[1]
```

```text
log.calculateImpulse: Build  : 9-89839ae3b8cd
Exec   : calculateImpulse pressureProbes
Date   : Jun 06 2026
Time   : 07:20:28
```

```text
reconass_400kg_external_facade_smoke.log: content='#!/bin/sh\ncd ${0%/*} || exit 1    # run from this directory\n\n# Source tutorial run functions\n. $WM_PROJECT_DIR/bin/tools/RunFunctions\n\n# -- Create paraview file\nparaFoam -builtin -touch\n\n# -- Pre-process the stl\nrunApplication surfaceFeatures\n\n# -- Create the mesh for the fluid\nrunApplication blockMesh\n\n# -- Decompose the mesh\nrunApplication decomposePar -copyZero\n\n# -- Cut out the stl\nrunParallel snappyHexMesh -overwrite\n\n# -- Add internal patch\nrunParallel addEmptyPatch internalPatch internal -overwrite\n\n# -- Set the initial conditions for the fluid\nrunParallel setRefinedFields\n\n#- Run the calc\nrunParallel $(getApplication)\n\n#- Sample all times with twice the time resolution\nrunParallel -s ground blastToVTK ground -dt 2.5e-5 \\\n     -interpolationScheme cubicClamp\nrunParallel -s walls blastToVTK walls -dt 2.5e-5 \\\n     -interpolationScheme li
```

### bls_two_box_interference_pressure_history

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_concrete_from_chapter3_20260606_065034/chapter3_evaluation/raw_e2e_runs/run_20260606_065035/cases/bls_two_box_interference_pressure_history`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_concrete_from_chapter3_20260606_065034/chapter3_evaluation/raw_e2e_runs/run_20260606_065035/benchmark_report.json`

```text
log.calculateImpulse: Build  : 9-89839ae3b8cd
Exec   : calculateImpulse pressureProbes
Date   : Jun 06 2026
Time   : 07:42:49
```

```text
log.blastToVTK.ground: [1] 
[1] --> FOAM FATAL ERROR: 
[1] cubicClamp is not a valid interpolation scheme for a list  of size 3
Valid Options are:
```

```text
bls_two_box_interference_pressure_history.log: content='#!/bin/sh\ncd ${0%/*} || exit 1    # run from this directory\n\n# Source tutorial run functions\n. $WM_PROJECT_DIR/bin/tools/RunFunctions\n\n# -- Create paraview file\nparaFoam -builtin -touch\n\n# -- Pre-process the stl\nrunApplication surfaceFeatures\n\n# -- Create the mesh for the fluid\nrunApplication blockMesh\n\n# -- Decompose the mesh\nrunApplication decomposePar -copyZero\n\n# -- Cut out the stl\nrunParallel snappyHexMesh -overwrite\n\n# -- Add internal patch\nrunParallel addEmptyPatch internalPatch internal -overwrite\n\n# -- Set the initial conditions for the fluid\nrunParallel setRefinedFields\n\n#- Run the calc\nrunParallel $(getApplication)\n\n#- Sample all times with twice the time resolution\nrunParallel -s ground blastToVTK ground -dt 2.5e-5 \\\n     -interpolationScheme cubicClamp\nrunParallel -s walls blastToVTK walls -dt 2.5e-5 \\\n     -interpolationScheme li
```

### hemicylinder_obstacle_reflection_probe_smoke

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_concrete_from_chapter3_20260606_065034/chapter3_evaluation/raw_e2e_runs/run_20260606_065035/cases/hemicylinder_obstacle_reflection_probe_smoke`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_concrete_from_chapter3_20260606_065034/chapter3_evaluation/raw_e2e_runs/run_20260606_065035/benchmark_report.json`

```text
log.setFields: --> FOAM FATAL ERROR: 
Cannot find file "points" in directory "polyMesh" in times "0" down to constant
```

```text
log.blastFoam: --> FOAM FATAL ERROR: 
Cannot find file "points" in directory "polyMesh" in times "0" down to constant
```

```text
log.blockMesh: --> FOAM FATAL ERROR: 
Inconsistent number of faces between block pair 0 and 1
```

### three_level_building_room_pressure_smoke

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_concrete_from_chapter3_20260606_065034/chapter3_evaluation/raw_e2e_runs/run_20260606_065035/cases/three_level_building_room_pressure_smoke`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_concrete_from_chapter3_20260606_065034/chapter3_evaluation/raw_e2e_runs/run_20260606_065035/benchmark_report.json`

```text
log.calculateImpulse: Build  : 9-89839ae3b8cd
Exec   : calculateImpulse pressureProbes
Date   : Jun 06 2026
Time   : 08:19:13
```

```text
three_level_building_room_pressure_smoke.log: content='#!/bin/sh\ncd ${0%/*} || exit 1    # run from this directory\n\n# Source tutorial run functions\n. $WM_PROJECT_DIR/bin/tools/RunFunctions\n\n# -- Create paraview file\nparaFoam -builtin -touch\n\n# -- Pre-process the stl\nrunApplication surfaceFeatures\n\n# -- Create the mesh for the fluid\nrunApplication blockMesh\n\n# -- Decompose the mesh\nrunApplication decomposePar -copyZero\n\n# -- Cut out the stl\nrunParallel snappyHexMesh -overwrite\n\n# -- Add internal patch\nrunParallel addEmptyPatch internalPatch internal -overwrite\n\n# -- Set the initial conditions for the fluid\nrunParallel setRefinedFields\n\n#- Run the calc\nrunParallel $(getApplication)\n\n#- Sample all times with twice the time resolution\nrunParallel -s ground blastToVTK ground -dt 2.5e-5 \\\n     -interpolationScheme cubicClamp\nrunParallel -s walls blastToVTK walls -dt 2.5e-5 \\\n     -interpolationScheme li
```

### gable_roof_building_envelope_pressure_smoke

- case: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_concrete_from_chapter3_20260606_065034/chapter3_evaluation/raw_e2e_runs/run_20260606_065035/cases/gable_roof_building_envelope_pressure_smoke`
- report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_concrete_from_chapter3_20260606_065034/chapter3_evaluation/raw_e2e_runs/run_20260606_065035/benchmark_report.json`

```text
log.calculateImpulse: Build  : 9-89839ae3b8cd
Exec   : calculateImpulse pressureProbes
Date   : Jun 06 2026
Time   : 08:29:23
```

```text
gable_roof_building_envelope_pressure_smoke.log: content='#!/bin/sh\ncd ${0%/*} || exit 1    # run from this directory\n\n# Source tutorial run functions\n. $WM_PROJECT_DIR/bin/tools/RunFunctions\n\n# -- Create paraview file\nparaFoam -builtin -touch\n\n# -- Pre-process the stl\nrunApplication surfaceFeatures\n\n# -- Create the mesh for the fluid\nrunApplication blockMesh\n\n# -- Decompose the mesh\nrunApplication decomposePar -copyZero\n\n# -- Cut out the stl\nrunParallel snappyHexMesh -overwrite\n\n# -- Add internal patch\nrunParallel addEmptyPatch internalPatch internal -overwrite\n\n# -- Set the initial conditions for the fluid\nrunParallel setRefinedFields\n\n#- Run the calc\nrunParallel $(getApplication)\n\n#- Sample all times with twice the time resolution\nrunParallel -s ground blastToVTK ground -dt 2.5e-5 \\\n     -interpolationScheme cubicClamp\nrunParallel -s walls blastToVTK walls -dt 2.5e-5 \\\n     -interpolationScheme li
```

## 需要人工确认的代码层风险

- metrics 现在优先按 `user_request` 精确匹配；若未来 `metrics_report` 缺失，应改为以 `task_id/run_id/case_id` 绑定。
- 历史结果中曾出现 `orchestrator_empty_output_absent=False`，后续仍应保留 structured routing 回归测试。
- 若 `execution_status_completed=True` 且 solver 有 clean End 但 workflow 进程退出码仍为 1，应优先检查终态状态机和 reviewer 结果合并。