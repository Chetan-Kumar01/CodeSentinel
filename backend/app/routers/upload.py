from fastapi import APIRouter, UploadFile, File
import shutil
import os

from app.services.zip_service import extract_zip
from app.services.file_scanner import scan_python_files
from app.services.ast_parser import ASTParser
from app.services.metrics_analyzer import MetricsAnalyzer
from app.services.code_quality_analyzer import CodeQualityAnalyzer

router = APIRouter()

UPLOAD_FOLDER = "app/uploads"


os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_project(file: UploadFile = File(...)):

    # Save uploaded ZIP file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract ZIP
    extracted_path = extract_zip(file_path)

    # Scan all Python files
    python_files = scan_python_files(extracted_path)

    parser = ASTParser()
    metrics_analyzer = MetricsAnalyzer()
    quality_analyzer = CodeQualityAnalyzer()

    analysis_results = []

    # Analyze every Python file
    for file_path in python_files:

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                code = f.read()

            analysis = parser.parse(code)
            metrics = metrics_analyzer.analyze(code, analysis)
            quality = quality_analyzer.analyze(code)

            analysis_results.append({
                "file": file_path,
                "analysis": analysis,
                "metrics": metrics,
                "quality": quality
            })

        except Exception as e:

            analysis_results.append({
                "file": file_path,
                "error": str(e)
            })

    return {
        "filename": file.filename,
        "message": "Upload Successful",
        "project_folder": extracted_path,
        "analysis": analysis_results
    }