"""Detector Implementations"""

# Imports trigger registration via decorators
from finbot.ctf.detectors.implementations.policy_bypass_non_compliant import (
    PolicyBypassNonCompliantDetector,
)
from finbot.ctf.detectors.implementations.system_prompt_leak import (
    SystemPromptLeakDetector,
)

__all__ = ["PolicyBypassNonCompliantDetector", "SystemPromptLeakDetector"]
