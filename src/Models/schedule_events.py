
"""
This is schedule events module to create, update and delete events

"""
from datetime import datetime
import time
from flask import json
from src import mysql


class SimpleMethod:
    """
    Class to implement method will be used by some other method
    """
    def is_date_time_in_proper_schedule(self, start_date, start_time, end_date, end_time):
        """
        Method to check date and time
        """

        reponse = True if ((end_date > start_date) or (end_date == start_date and end_time > start_time)) else False

        return reponse


class Events:
    
    """
    Events class
    """
    
    def create_event(self, data):

        """
         Create-event method to create event
        """
        cur = mysql.connection.cursor()

        try:

            record = json.loads(data)
        
            start_date = datetime.strptime(record['start_date'], '%Y-%m-%d').date()

            end_date = datetime.strptime(record['end_date'], '%Y-%m-%d').date()

            start_time = datetime.strptime(record['start_time'], '%H:%M:%S').time()

            end_time = datetime.strptime(record['end_time'], '%H:%M:%S').time()  

            method_obj = SimpleMethod()    # class

            if (method_obj.is_date_time_in_proper_schedule(start_date, start_time, end_date, end_time)):

                cur.execute("Insert into event_details(event_name, event_description, organiser_email, start_date, start_time, end_date, end_time) values (%s, %s, %s, %s, %s, %s, %s)", (record['event_name'], record['event_description'], record['organiser_email'], record['start_date'], record['start_time'], record['end_date'], record['end_time']))

                mysql.connection.commit()

                return "Succes fully craeted events"

            return "Please insert date time in proper way ((end_date > start_date) or (end_date == start_date and end_time > start_time))"                 

        finally:
            cur.close()

    def update_event_details(self, data, event_id):

        """
        Update event with givent event_id
        """

        cur = mysql.connection.cursor()

        try:

            record = json.loads(data)

            start_date = datetime.strptime(record['start_date'], '%Y-%m-%d').date()

            end_date = datetime.strptime(record['end_date'], '%Y-%m-%d').date()

            start_time = datetime.strptime(record['start_time'], '%H:%M:%S').time()

            end_time = datetime.strptime(record['end_time'], '%H:%M:%S').time()

            method_obj = SimpleMethod()     # class  

            if (method_obj.is_date_time_in_proper_schedule(start_date, start_time, end_date, end_time)):

                cur.execute("update event_details set event_name = %s, event_description=%s, organiser_email=%s, start_date=%s, start_time=%s, end_date=%s, end_time=%s where event_id = %s", (record['event_name'], record['event_description'], record['organiser_email'], record['start_date'], record['start_time'], record['end_date'], record['end_time'], event_id))
                mysql.connection.commit()

                return "Successfully events has been updated"
        
            return "Please insert date time in proper way ((end_date > start_date) or (end_date == start_date and end_time > start_time))"                 

        finally:
            cur.close()

    def delete_event_detils(self, event_id):

        """
        delete_events for giiven event_id
        """

        cur = mysql.connection.cursor()

        try:
            cur.execute("Delete from event_details where event_id = %s", (event_id,))
            mysql.connection.commit()

            return "Succesfully event has been deleted"
        
        finally:
            cur.close()
   
    def read(self):

        """
        Read all events
        """
        cur = mysql.connection.cursor()
        try:
            
            event_details = []

            cur.execute('select * from event_details')
            records = cur.fetchall()

            for record in records:
                event_detail = {}
                event_detail['event_id'] = record[0]
                event_detail['event_name'] = record[1]
                event_detail['event_description'] = record[2]
                event_detail['event_organiser'] = record[3]
                event_detail['event_start_date'] = str(record[4])
                event_detail['event_start_time'] = str(record[5])
                event_detail['event_end_date'] = str(record[6])
                event_detail['event_end_time'] = str(record[7])
                event_details.append(event_detail)

            return event_details
        finally:
            cur.close()
