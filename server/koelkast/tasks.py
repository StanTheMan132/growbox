from datetime import datetime, timedelta
from decimal import Decimal
from django.utils import timezone

from celery import shared_task
from koelkast.models import Input, Output, State, Value

import os


def is_time_between(begin_time, end_time, current_time):
    if begin_time < end_time:
        return current_time >= begin_time and current_time <= end_time
    # Crosses midnight
    else:
        return current_time >= begin_time or current_time <= end_time


@shared_task(bind=True)
def task_update(self, output_id):
    try:
        output = Output.objects.get(id=output_id)
        last_state = output.states.order_by("-created_at").first()
        os_type = os.uname().machine
        
        if os_type == "armv6l":
            import RPi.GPIO as io

            io.setmode(io.BCM)
            io.setup(output.pin, io.OUT)

        if output.type == Output.ON_OFF:
            if os_type != "armv6l":
                print(f"Updated pin {output.pin} to state {bool(last_state.value)}")
            else:
                io.output(output.pin, bool(last_state.value))

        elif output.type == Output.TIME:
            current_state = is_time_between(last_state.on_time, last_state.off_time, timezone.now().time())
            if os_type != "armv6l":
                print(f"Updated pin {output.pin} to state {current_state}")
            else:
                io.output(output.pin, current_state)
            

    except Exception as e:
        print(str(e), type(e))
