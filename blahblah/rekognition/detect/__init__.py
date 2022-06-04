from typing import List

from blahblah.rekognition import rekognition

def detect_labels(img: bytes) -> List[str]:
    response = rekognition.detect_labels(
        Image={"Bytes": img}, MaxLabels=10)

    return [label.get("Name") for label in response['Labels']]

