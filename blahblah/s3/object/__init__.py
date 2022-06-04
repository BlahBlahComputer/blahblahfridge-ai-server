import io

from blahblah.s3 import s3

def get_obj_binary(bucket: str, key: str) -> bytes:
    buf = io.BytesIO()
    s3.download_fileobj(bucket, key, buf)

    return buf.getvalue()