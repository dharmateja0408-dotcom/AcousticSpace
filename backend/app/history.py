


from app.database import get_connection


def save_analysis(data):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO analysis_history
        (
            filename,
            prediction,
            confidence,
            risk,
            duration,
            sample_rate,
            analysis_time
        )
        VALUES
        (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            data["filename"],
            data["prediction"],
            data["confidence"],
            data["risk"],
            data["duration"],
            data["sample_rate"],
            data["analysis_time"],
        ),
    )

    conn.commit()

    conn.close()

def get_all_history():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            filename,
            prediction,
            confidence,
            risk,
            duration,
            sample_rate,
            analysis_time,
            created_at
        FROM analysis_history
        ORDER BY id DESC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]    

def delete_history(history_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM analysis_history
        WHERE id = ?
        """,
        (history_id,)
    )

    conn.commit()

    conn.close()    

def get_dashboard_statistics():

    conn = get_connection()

    cursor = conn.cursor()

    # Total analyses
    cursor.execute(
        "SELECT COUNT(*) FROM analysis_history"
    )
    total = cursor.fetchone()[0]

    # Real audios
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM analysis_history
        WHERE prediction='Real'
        """
    )
    real = cursor.fetchone()[0]

    # Spoof audios
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM analysis_history
        WHERE prediction='Spoof'
        """
    )
    spoof = cursor.fetchone()[0]

    # Average confidence
    cursor.execute(
        """
        SELECT AVG(confidence)
        FROM analysis_history
        """
    )

    avg = cursor.fetchone()[0]

    conn.close()

    return {

        "total": total,

        "real": real,

        "spoof": spoof,

        "average_confidence":
            round(avg, 2) if avg else 0

    }

def get_chart_data():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            filename,
            confidence
        FROM analysis_history
        ORDER BY id ASC
    """)

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]