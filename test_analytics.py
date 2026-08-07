from src.analytics import Analytics

analytics = Analytics()

print("Total Sessions")

print(analytics.total_sessions())

print("Average Focus")

print(analytics.average_focus())

print("Total Blinks")

print(analytics.total_blinks())

print("Phone Usage")

print(analytics.total_phone_usage())

print("Total Duration")

print(analytics.total_duration())

print("History")

print(analytics.focus_history())

analytics.close()