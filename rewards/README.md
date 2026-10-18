# Reward functions (planned)

**Status: not implemented in BSRA code.** The starter uses the standard `Humanoid-v5` reward. The planned OP3 locomotion task will combine measurable velocity-tracking, uprightness, effort, and smoothness terms. Balance incentives belong within locomotion training; there is no separate learned-standing stage.

Reward functions should consume the shared named state/action interface in [INTERFACES.md](../docs/INTERFACES.md#rewards) and can be tested against synthetic states before the XML is complete. Document scales and units, keep physical thresholds configurable, and tune weights only after integration with the OP3 model and PD controller. Do not copy unvalidated reward weights from an unrelated robot.
