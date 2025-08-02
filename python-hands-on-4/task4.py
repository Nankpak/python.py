"""
Task 4: Tech Conference Registration
The Jos Tech Conference registered participants under ticket categories:

participants = {"VIP": "Alice", "Regular": "Bob", "Student": "Charlie"}

During the first day:
- A "Guest" participant named "Daisy" joined.
- The "Student" participant canceled their registration.
- The organizers created a record for the day before removing the most recently added participant from the live system.
"""

# print(participants_snapshot)
# print(participants)
participants = {"VIP": "Alice", "Regular": "Bob", "Student": "Charlie"}
participants.update({'Guest':'Daisy'})
print(participants)
participants.pop('Student')
print(participants)
record = {'the record created are':'','Guest joint':'Daisy','reg. conceled by student':'Charlie'}
print(record)
participants.popitem()
print(participants)
