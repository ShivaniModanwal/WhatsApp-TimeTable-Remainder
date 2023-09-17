import schedules
import schedule
import time

schedule.every().day.at("09:00").do(schedules.morning_qoutes)
schedule.every().day.at("12:55").do(schedules.lunch_break)
schedule.every().monday.at("10:55").do(schedules.monday_tfcs)
schedule.every().monday.at("13:55").do(schedules.monday_coa)
schedule.every().tuesday.at("08:55").do(schedules.tuesday_pm)
schedule.every().tuesday.at("13:55").do(schedules.tuesday_pm_lab)
schedule.every().wednesday.at("08:55").do(schedules.wednesday_tfcs)
schedule.every().wednesday.at("10:55").do(schedules.wednesday_cbot)
schedule.every().wednesday.at("13:55").do(schedules.wednesday_coa)
schedule.every().thursday.at("08:55").do(schedules.thursday_pm)
schedule.every().friday.at("09:55").do(schedules.friday_tfcs)
schedule.every().friday.at("10:55").do(schedules.friday_cbot)
schedule.every().friday.at("13:55").do(schedules.friday_coa)

while True:
    schedule.run_pending()
    time.sleep(1)