
import Guest

import my_enums


class Reservation:

        
    def __init__(self, row):
        self.ReservationId = row["ReservationId"]
        self.hotel = Hotel[row["hotel"]]
        self.is_canceled = row["is_canceled"]
        self.lead_time = row["lead_time"]
        self.arrival_date_week = row["arrival_date_week_number"]
        self.stays_in_weekend_nights = row["stays_in_weekend_nights"]
        self.stays_in_week_nights = row["stays_in_week_nights"]
        self.meal = Meal[row["meal"]]
        self.market_segment = row["market_segment"]
        self.distribution_channel = Distribution_channel[row["distribution_channel"]]
        self.is_repeated_guest = row["repeated_guest"]
        self.previous_cancellations = row["previous_cancellations"]
        self.previous_bookings_not_cancelled = row["previous_bookings_not_cancelled"]
        self.reserved_room_type = row["reserved_room_type"]
        self.assigned_room_type = row["assigned_room_type"]
        self.booking_changes = row["booking_changes"]
        self.deposit_type = Deposit_type[row["booking_changes"]]
        self.agent = row["agent"]
        self.company = row["company"]
        self.days_in_waiting_list = row["days_in_waiting_list"]
        self.customer_type = row["customer_type"]
        self.adr = row["adr"]
        self.required_car_parking_spaces = row["required_car_parking_spaces"]
        self.total_of_special_requests = row["total_of_special_requests"]
        self.reservation_status = row["reservation_status"]
        self.reservation_status_date = row["reservation_status_date"]
        self.arrival_date = row["arrival_date"]
        self.direct_booking = row["direct_booking"]
        self.GuestId = row["GuestId"]
        self.guest = Guest.Guest(row)

        def __str__(self):
            sb = []
            for key in self.__dict__:
                sb.append("{key}='{value}'".format(key=key, value=self.__dict__[key]))
    
            return ', '.join(sb)
