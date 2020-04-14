import subprocess, os

NEEDED_FIELDS = (
    ('Secret key: ', 'SECRET_KEY'),

    ('Email address: ', 'EMAIL_ADDRESS'),
    ('Email password: ', 'EMAIL_PASSWORD'),

    ('Local host name: ', 'LOCAL_HOST'),

    ('Database name: ', 'DB_NAME'),
    ('Database user: ', 'DB_USER'),
    ('Database password: ', 'DB_PASSWORD'),
    ('Database host: ', 'DB_HOST'),
)


with open('.env', 'a') as env:
    for field in NEEDED_FIELDS:
        value = input(field[0])
        env.write(
            '{}=\"{}\"\n'.format(field[1], value)
        )
        os.environ[field[1]] = value

    # Set settings module
    env.write(
        'DJANGO_SETTINGS_MODULE="npp.settings"\n'
    )
    os.environ['DJANGO_SETTINGS_MODULE'] = 'npp.settings'
    env.close()

for command in ['migrate', 'collectstatic', 'createsuperuser']:
    subprocess.run([
        'python', 'manage.py', command
    ])
