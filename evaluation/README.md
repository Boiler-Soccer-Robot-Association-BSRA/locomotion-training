# OP3 evaluation (planned)

Compare the fixed-pose PD baseline and learned locomotion policy using matching models, controller settings, commands, seeds, and episode conditions. Report upright time, falls, velocity-tracking error, return, and episode length.

Agree on state fields and metric definitions in [INTERFACES.md](../docs/INTERFACES.md#training-and-evaluation). Training and evaluation must share environment construction and restore the checkpoint's configuration and normalization state. The [Humanoid example](../examples/humanoid_v5/README.md) demonstrates checkpoint loading and basic reporting.
