import os
import sys
import schedule
import subprocess
import time


def post_ad():
    current_directory = os.getcwd();
    print(current_directory)
    print('Starting kijiji script')
    bash = 'pushd {};source venv/bin/activate;python3 kijiji_repost_headless -u hylann.ma@hotmail.com -p guesswhat? repost ads/dad/item.yaml;deactivate;popd'.format(current_directory)
    process = subprocess.Popen(bash, stdout=sys.stdout, stderr=sys.stderr, shell=True)
    process.wait()
    print('Finished auto repost ad')

post_ad()
# repeat_times = input('Please enter the number of times you would like to repeat post?: ')
# for repeat in range(int(repeat_times)):
#     time_sch = input("Enter the time you would like to repeat for #{} (24h time): ".format(repeat))
#     schedule.every().day.at(time_sch).do(post_ad)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
