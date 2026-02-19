# Sprint

In Age of Dragons, humans can "sprint" to move twice as fast. However, sprinting requires __stamina. Each time a human sprints, it loses stamina. Once it is out of stamina, it can no longer sprint.

## Assignment
Complete all the missing methods:

1. Complete the private helper methods, which are intended to be used by the other four sprinting methods.
    1. __raise_if_cannot_sprint(): Raise the exception: not enough stamina to sprint if the human is out of stamina.
    2. __use_sprint_stamina(): Remove one stamina from the human.
2. For each of the sprint methods:
    1. Use __raise_if_cannot_sprint() if there isn't enough stamina to sprint.
    2. Use __use_sprint_stamina() once to use the stamina needed to sprint.
    3. Move twice in the direction of the sprint.