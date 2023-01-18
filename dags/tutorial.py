from airflow import DAG
from airflow.decorators import task
import datetime as dt

with DAG(
    dag_id="example_python_operator",
    schedule_interval="@daily",
    start_date=dt.datetime(2023, 1, 18),
) as dag:
        @task.virtualenv(
            task_id="virtualenv_python", requirements=["colorama==0.4.0"], system_site_packages=False
        )
        def callable_virtualenv():
            from time import sleep
            from colorama import Back, Fore, Style

            print(Fore.RED + "some red text")
            print(Back.GREEN + "and with a green background")
            print(Style.DIM + "and in dim text")
            print(Style.RESET_ALL)
            for _ in range(4):
                print(Style.DIM + "Please wait...", flush=True)
                sleep(1)
            print("Finished")
        t1 = callable_virtualenv()
        t1
