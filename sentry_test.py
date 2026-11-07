import sentry_sdk

sentry_sdk.init(
    dsn="http://22a82b4c55caaccc65db0a324166d40f@localhost:9000/2", 
    traces_sample_rate=1.0,
)

print("Отправляем тестовое сообщение...")
sentry_sdk.set_tag("experiment", "message_test")
sentry_sdk.capture_message("Привет от локального Sentry! Это тестовое сообщение.")

print("Вызываем ошибку деления на ноль...")
try:
    1 / 0
except ZeroDivisionError as e:
    with sentry_sdk.push_scope() as scope:
        scope.set_level("error")
        scope.set_context("user_details", {"user_id": 42, "action": "division_test"})
        sentry_sdk.capture_exception(e)

print("Скрипт выполнен. Проверьте раздел Issues в Sentry.")