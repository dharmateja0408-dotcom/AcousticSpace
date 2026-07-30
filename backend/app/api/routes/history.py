



import os

print("Loaded history.py from:")
print(os.path.abspath(__file__))

from fastapi import APIRouter

from app.history import get_all_history , delete_history

router = APIRouter()


@router.get("/")
async def history():

    return {

        "status": "success",

        "total": len(get_all_history()),

        "data": get_all_history()

    }

@router.delete("/{history_id}")
async def remove_history(history_id: int):

    delete_history(history_id)

    return {

        "status": "success",

        "message": "History deleted successfully"

    } 

def get_chart_data():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            filename,
            confidence
        FROM analysis_history
        ORDER BY id ASC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]       