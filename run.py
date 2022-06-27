import subprocess


def main():
    process = []
    process.append(subprocess.Popen('python manage.py runserver', shell=True))
    process.append(subprocess.Popen('python manage.py run_task', shell=True))
    process.append(subprocess.Popen('python manage.py get_currency', shell=True))
    process.append(subprocess.Popen('python manage.py send_message', shell=True))


if __name__ == '__main__':
    main()
