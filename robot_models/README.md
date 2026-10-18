# Robot models (planned)

**Status: no physical BSRA or OP3 model included.** The baseline loads Gymnasium's built-in generic humanoid model automatically via `Humanoid-v5`.

The priority is to build and validate an OP3 MJCF for the PD standing baseline and subsequent locomotion experiments. Document model provenance/license, conversion steps, actuator assumptions, and validation results using [the model checklist](../docs/OP3_MODEL_CHECKLIST.md). Agree on joint/actuator names and mappings in [INTERFACES.md](../docs/INTERFACES.md#model-and-actuator-mapping). Preserve those findings for the future locomotion repository. External model downloads and large meshes belong in ignored `robot_models/external/` or approved artifact storage, not committed by default; reviewed model sources and reproducible asset acquisition instructions should be tracked.
