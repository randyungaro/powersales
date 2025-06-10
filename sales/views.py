import fdb
from django.shortcuts import render
from django.utils import timezone
from django.conf import settings

def daily_sales(request):
    try:
        # Connect to Firebird database
        con = fdb.connect(
            dsn=str(settings.BASE_DIR / 'database/POWERFO.GDB'),
            user='<user>',   # Set your user id Firebird database
            password='<password>',  # set your password Firebird database
            charset='UTF8'
        )
        cursor = con.cursor()

        # Check if DSR_IDs exist
        cursor.execute("""
            SELECT COUNT(*) FROM FODSR
            WHERE DSR_ID IN (8, 42, 59, 67, 69, 70, 71, 74, 81, 91, 97, 99)
        """)
        id_count = cursor.fetchone()[0]

        # Get selected date from GET parameter (YYYY-MM-DD)
        selected_date = request.GET.get('date', None)
        
        # Main query
        query = """
            SELECT FODATE as sale_day, TEXT, AMOUNT
            FROM FODSR
            WHERE DSR_ID IN (8, 42, 59, 67, 69, 70, 71, 74, 81, 91, 97, 99)
        """
        params = []
        if selected_date:
            query += " AND CAST(FODATE AS DATE) = ?"
            params.append(selected_date)
        else:
            # Default to most recent date
            query += " AND CAST(FODATE AS DATE) = (SELECT MAX(CAST(FODATE AS DATE)) FROM FODSR WHERE DSR_ID IN (8, 42, 59, 67, 69, 70, 71, 74, 81, 91, 97, 99))"

        query += " ORDER BY sale_day DESC"
        cursor.execute(query, params)
        sales_data = cursor.fetchall()

        cursor.close()
        con.close()

        context = {
            'sales_data': [{'date': row[0], 'text': row[1], 'amount': float(row[2])} for row in sales_data],
            'selected_date': selected_date,
            'current_date': timezone.now().strftime('%Y-%m-%d'),
            'debug_id_count': id_count
        }
    except fdb.fbcore.DatabaseError as e:
        context = {
            'sales_data': [],
            'selected_date': None,
            'current_date': timezone.now().strftime('%Y-%m-%d'),
            'error': f"Database error: {str(e)}",
            'debug_id_count': 0
        }

    return render(request, 'sales/daily_sales.html', context)
