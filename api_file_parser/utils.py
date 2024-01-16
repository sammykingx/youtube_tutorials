from fastapi import HTTPException, UploadFile

ALLOWED_FILE_TYPES = ("text/csv")

def check_file(file: UploadFile):
    """checks the intergrity of a file"""

    if file.content_type not in ALLOWED_FILE_TYPES:
        raise HTTPException(
                status_code=415,
                detail="file type not surpported",
            )
