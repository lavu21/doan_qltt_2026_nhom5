from django.shortcuts import render
from django.db import connection


def dashboard(request):
    context = {}
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT @@VERSION, @@SERVERNAME, DB_NAME()")
            row = cursor.fetchone()
            context['db_info'] = {
                'version': row[0].split('\n')[0] if row[0] else 'N/A',
                'host': row[1],
                'name': row[2],
            }
            # Stats sẽ được bổ sung khi có bảng dữ liệu (Phase 2)
            context['stats'] = {
                'total_drivers': '–',
                'total_trips': '–',
                'completed_trips': '–',
                'total_revenue': '–',
            }
    except Exception as e:
        context['db_error'] = str(e)

    return render(request, 'booking/dashboard.html', context)
