""" Exercise to determine average completion time in minutes of a boat race
    which begins at 8:00 AM on 'day 1'.
"""

import re


class RaceAverage(object):

    def avgMinutes(self, times):
        """ Calculate average finishing time of all boats """

        # Time Format: 'hh:mm xM, DAY n'
        regex = r'(\d{2}):(\d{2}) ([AP])M, DAY (\d+)'

        calculated_times = []

        for time_entry in times:
            match = re.match(regex, time_entry)

            if match is None:
                raise ValueError('Invalid time format: {0}'.format(time_entry))

            # Record values as floats here for proper math later
            time_dict = {
                'hours': float(match.group(1)),
                'minutes': float(match.group(2)),
                'ampm': match.group(3),
                'day': float(match.group(4))
            }

            # Convert AM hour 12s to 0 for purposes of math
            if time_dict['hours'] == 12 and time_dict['ampm'] == 'A':
                time_dict['hours'] = 0

            # Convert hours to minutes, begin calculating total minutes
            time_minutes = time_dict['hours'] * 60

            # For PM (other than 12), add first half of the day in minutes
            if time_dict['ampm'] == 'P' and time_dict['hours'] != 12:
                time_minutes += 12 * 60

            # Add previous day(s) in minutes
            time_minutes += (time_dict['day'] - 1) * 24 * 60

            # Add minutes
            time_minutes += time_dict['minutes']

            # Store the calculated time (8 AM start time)
            calculated_times.append(time_minutes - 8 * 60)

        # Return rounded average
        return int(round(sum(calculated_times) / len(calculated_times)))
