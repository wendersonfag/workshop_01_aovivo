from frontend import ExcelValidorUI
from backend import process_excel, excel_to_sql

import sentry_sdk

sentry_sdk.init(
    dsn="https://86a8cb4a29981dddfd025a9843c7279b@o4507296462012416.ingest.us.sentry.io/4507296481411072",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

def main():
    ui = ExcelValidorUI()
    ui.display_header()

    upload_file = ui.upload_file()

    if upload_file:
        df, result, error = process_excel(upload_file)
        ui.display_results(result,error)

        if error:
            ui.display_wrong_message
            sentry_sdk.capture_message("A planilha Excel estava errada")
        elif ui.display_save_button():
            excel_to_sql(df)
            ui.display_sucess_message()
            sentry_sdk.capture_message("O Banco SQL foi atualizado")


if __name__ == "__main__":
    main()