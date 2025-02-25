# LICENSE HEADER MANAGED BY add-license-header
#
# Copyright 2018 Kornia Team
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
#

from __future__ import annotations

import warnings
from typing import Any

from kornia.models.detection.base import (
    BoundingBox as BoundingBoxBase,
)
from kornia.models.detection.base import (
    BoundingBoxDataFormat,
)
from kornia.models.detection.base import (
    ObjectDetector as ObjectDetectorBase,
)
from kornia.models.detection.base import (
    ObjectDetectorResult as ObjectDetectorResultBase,
)
from kornia.models.detection.base import (
    results_from_detections as results_from_detections_base,
)
from kornia.models.utils import ResizePreProcessor as ResizePreProcessorBase

__all__ = [
    "BoundingBox",
    "BoundingBoxDataFormat",
    "ObjectDetector",
    "ObjectDetectorResult",
    "ResizePreProcessor",
    "results_from_detections",
]


class BoundingBox(BoundingBoxBase):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        warnings.warn(
            "BoundingBox is deprecated and will be removed in v0.8.0. Use kornia.models.detection.BoundingBox instead.",
            DeprecationWarning,
            stacklevel=1,
        )


def results_from_detections(*args: Any, **kwargs: Any) -> list[ObjectDetectorResultBase]:
    """Return detector results."""
    warnings.warn(
        "results_from_detections is deprecated and will be removed in v0.8.0. "
        "Use kornia.models.detection.results_from_detections instead.",
        DeprecationWarning,
        stacklevel=1,
    )
    return results_from_detections_base(*args, **kwargs)


class ResizePreProcessor(ResizePreProcessorBase):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        warnings.warn(
            "ResizePreProcessor is deprecated and will be removed in v0.8.0. "
            "Use kornia.models.utils.ResizePreProcessor instead.",
            DeprecationWarning,
            stacklevel=1,
        )


class ObjectDetector(ObjectDetectorBase):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        warnings.warn(
            "ObjectDetector is deprecated and will be removed in v0.8.0. "
            "Use kornia.models.detection.ObjectDetector instead.",
            DeprecationWarning,
            stacklevel=1,
        )


class ObjectDetectorResult(ObjectDetectorResultBase):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        warnings.warn(
            "ObjectDetectorResult is deprecated and will be removed in v0.8.0. "
            "Use kornia.models.detection.ObjectDetectorResult instead.",
            DeprecationWarning,
            stacklevel=1,
        )
