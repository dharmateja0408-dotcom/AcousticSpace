


from app.history import save_analysis
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import os

from app.ai.predictor import predict_audio
from app.ai.report_generator import generate_report

router = APIRouter()

UPLOAD_FOLDER = "app/uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


@router.post("/")
async def upload_audio(file: UploadFile = File(...)):

    # =====================================
    # Save Uploaded File
    # =====================================

    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    # =====================================
    # Run AI Prediction
    # =====================================

    result = predict_audio(filepath)

    # =====================================
    # Generate PDF Report
    # =====================================

    report_data = {

        "filename": file.filename,

        "prediction": result["prediction"],

        "confidence": result["confidence"],

        "risk": result["risk"],

        "recommendation": result["recommendation"],

        "duration": result["duration"],

        "sample_rate": result["sample_rate"],

        "analysis_time": result["analysis_time"]

    }

    generate_report(report_data)

    # =====================================
    # Return Response
    # =====================================

    save_analysis({

    "filename": file.filename,

    "prediction": result["prediction"],

    "confidence": result["confidence"],

    "risk": result["risk"],

    "duration": result["duration"],

    "sample_rate": result["sample_rate"],

    "analysis_time": result["analysis_time"]

})
    return {

        "status": "success",

        "filename": file.filename,

        "prediction": result["prediction"],

        "confidence": result["confidence"],

        "risk": result["risk"],

        "recommendation": result["recommendation"],

        "duration": result["duration"],

        "sample_rate": result["sample_rate"],

        "analysis_time": result["analysis_time"],

        "report": "analysis_report.pdf"

    }


# ==========================================
# Download Generated PDF
# ==========================================

@router.get("/report")
async def download_report():

    report_path = "app/reports/analysis_report.pdf"

    return FileResponse(

        path=report_path,

        filename="AcousticSpace_Report.pdf",

        media_type="application/pdf"

    )