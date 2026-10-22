# OP3 architecture flowcharts

## Initialization and training setup

Shows how configuration and the robot model feed environment construction and PPO training.

```mermaid
flowchart TD
    T["training/train.py"] -->|"calls"| L["config/loader.py"]

    subgraph Files["Configuration files"]
        A["op3.yaml"]
        B["environment.yaml"]
        C["rewards.yaml"]
        D["ppo.yaml"]
    end

    A & B & C & D -->|"read by"| L

    L -->|"returns validated config"| T

    T -->|"create_environment(config)"| CE["environments/create_environment.py"]
    CE -->|"constructs with config"| ENV["environments/op3_env.py"]

    MJ["OP3 MJCF model"] -->|"loaded by"| ENV

    ENV -->|"environment instance"| CE
    CE -->|"returns env"| T

    T -->|"creates PPO with env + hyperparameters"| PPO["SB3 PPO"]
    PPO -->|"training results"| OUT["policy.zip + TensorBoard logs"]

    style T fill:#006400,color:#fff
```

## One policy step

This is what happens inside op3_env.py. Shows the action, physics, state-reading, and reward sequence that returns a transition to PPO.

```mermaid
flowchart TD
    PPO["SB3 PPO"]
    ENV["environments/op3_env.py"]
    MJ["MuJoCo simulation"]
    STATE["robot/robot_state.py"]
    REW["rewards/calculate_rewards.py"]

    PPO -->|"1. Policy action"| ENV
    ENV -->|"2. Target joint positions"| MJ
    MJ -->|"3. Advance physics"| MJ
    ENV -->|"4. Read model and simulation data"| STATE
    STATE -->|"5. Return RobotState"| ENV
    ENV -->|"6. State + command + actions + reward config"| REW
    REW -->|"7. Total reward + components"| ENV
    ENV -->|"8. Observation + reward + done flags + info"| PPO

    style PPO fill:#DCE7F8,color:#172C4B,stroke:#7B9CCB
    style ENV fill:#DCE7F8,color:#172C4B,stroke:#7B9CCB
```
