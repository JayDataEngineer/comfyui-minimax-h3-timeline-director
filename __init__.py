"""MiniMax H3 Timeline Director for ComfyUI."""

from .minimax_h3_timeline_director import (
    MiniMaxH3TimelineDirector,
    MiniMaxH3TimelineEncoder,
    MiniMaxH3OmniPromptBridge,
    MiniMaxH3TimelinePlanner,
)
from .minimax_h3_finite_segments import (
    MiniMaxH3FiniteLatentContinuation,
    MiniMaxH3FiniteAudioTrimTail,
    MiniMaxH3FiniteOutputTrim,
    MiniMaxH3FiniteSegmentFinalize,
    MiniMaxH3FiniteSegmentSampler,
    MiniMaxH3LockedAudioSlice,
    MiniMaxH3SilentAudioSlice,
    MiniMaxH3LockAudioLatent,
    MiniMaxH3LockedAudioMaster,
    MiniMaxH3SilentAudioMaster,
)
from .selflift_runtime import SelfLiftH3Sampler

NODE_CLASS_MAPPINGS = {
    "MiniMaxH3TimelineDirector": MiniMaxH3TimelineDirector,
    "MiniMaxH3TimelinePlanner": MiniMaxH3TimelinePlanner,
    "MiniMaxH3TimelineEncoder": MiniMaxH3TimelineEncoder,
    "MiniMaxH3OmniPromptBridge": MiniMaxH3OmniPromptBridge,
    "MiniMaxH3FiniteSegmentSampler": MiniMaxH3FiniteSegmentSampler,
    "MiniMaxH3FiniteAudioTrimTail": MiniMaxH3FiniteAudioTrimTail,
    "MiniMaxH3FiniteOutputTrim": MiniMaxH3FiniteOutputTrim,
    "MiniMaxH3FiniteLatentContinuation": MiniMaxH3FiniteLatentContinuation,
    "MiniMaxH3FiniteSegmentFinalize": MiniMaxH3FiniteSegmentFinalize,
    "MiniMaxH3LockedAudioSlice": MiniMaxH3LockedAudioSlice,
    "MiniMaxH3SilentAudioSlice": MiniMaxH3SilentAudioSlice,
    "MiniMaxH3LockAudioLatent": MiniMaxH3LockAudioLatent,
    "MiniMaxH3LockedAudioMaster": MiniMaxH3LockedAudioMaster,
    "MiniMaxH3SilentAudioMaster": MiniMaxH3SilentAudioMaster,
    "MiniMaxH3TimelineSelfLiftSampler": SelfLiftH3Sampler,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MiniMaxH3TimelineDirector": "MiniMax H3 Timeline Director",
    "MiniMaxH3TimelinePlanner": "MiniMax H3 Material Planner",
    "MiniMaxH3TimelineEncoder": "MiniMax H3 Plan Encoder",
    "MiniMaxH3OmniPromptBridge": "MiniMax H3 Omni Media Prompt Bridge",
    "MiniMaxH3FiniteSegmentSampler": "MiniMax H3 Finite Segment Sampler",
    "MiniMaxH3FiniteAudioTrimTail": "MiniMax H3 Finite Audio Tail Trim (Internal)",
    "MiniMaxH3FiniteOutputTrim": "MiniMax H3 Finite Output Trim (Internal)",
    "MiniMaxH3FiniteLatentContinuation": "MiniMax H3 Finite Latent Continuation (Internal)",
    "MiniMaxH3FiniteSegmentFinalize": "MiniMax H3 Finite Segment Finalize (Internal)",
    "MiniMaxH3LockedAudioSlice": "MiniMax H3 Locked Audio Slice (Internal)",
    "MiniMaxH3SilentAudioSlice": "MiniMax H3 Silent Audio Slice (Internal)",
    "MiniMaxH3LockAudioLatent": "MiniMax H3 Lock Audio Latent (Internal)",
    "MiniMaxH3LockedAudioMaster": "MiniMax H3 Locked Audio Master (Internal)",
    "MiniMaxH3SilentAudioMaster": "MiniMax H3 Silent Audio Master (Internal)",
    "MiniMaxH3TimelineSelfLiftSampler": "MiniMax H3 Two-Stage Sampler (Internal)",
}

WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
