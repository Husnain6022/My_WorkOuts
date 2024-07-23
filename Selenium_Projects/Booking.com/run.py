from booking.booking import Booking


with Booking() as bot:
    bot.first_page()
    bot.destination(value='lahore')
    bot.check_in_dates('2024-07-23', '2024-07-29')
    bot.select_adults(count=2)