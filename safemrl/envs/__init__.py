# coding=utf-8
# Copyright 2019 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Register default envs."""

from __future__ import absolute_import

import gym
from safemrl.envs import minitaur
from gym.envs.registration import register

registered = False
for env in gym.envs.registry.env_specs:
    if "MinitaurGoalVelocityEnv-v0" in env:
        registered = True
        break

if not registered:
    register(
        id="MinitaurGoalVelocityEnv-v0",
        entry_point=minitaur.MinitaurGoalVelocityEnv,
        max_episode_steps=500
    )
