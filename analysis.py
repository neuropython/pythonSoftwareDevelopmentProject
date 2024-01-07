# -*- coding: utf-8 -*

from path_handler import PathHandler
from ABP._signal_preprocessing import SignalPreprocessing
from ABP.frequency_domain import FrequencyDomain
from ABP.time_domain import TimeDomain
from async_lru import alru_cache
import pyhrv
PATH = r"C:\Users\damia\OneDrive\Pulpit\zdrowi"
name = ["abp_finger_mm_hg_[abp_finger_mm_Hg_]"]
for_ecg_analysis = ["ekg__[ekg__]"]

signals = PathHandler(PATH, name).signals
file_names = PathHandler(PATH, name).all_alaized_files_names
analized_names = PathHandler(PATH, name).all_alaized_names

x = FrequencyDomain(signals[0], 200, 256, 128)


for i, (j, file_name, analized_name) in enumerate(
        zip(
            signals, file_names, analized_names
        )):
    try:
        print(f"Index: {i}, File name: {file_name}, analized name: {analized_name}")
        print(f"Values: {FrequencyDomain(j, 200, 256, 128)}")

        # Sanitize file_name and analized_name
        file_name = re.sub(r'[^\w\s]', '', file_name)
        analized_name = re.sub(r'[^\w\s]', '', analized_name)

        open(fr"C:\Users\damia\OneDrive\Pulpit\zdrowi\results\{file_name}_{analized_name}.txt",
             "w").write(f"{FrequencyDomain(j, 200, 256, 128)}")
    except Exception as e:
        print(f"An error occurred with signal {i} (name) {file_name}: {e}")



# for i, j in enumerate(ecg_signals):
#     if any (j) == 0:
#     result = pyhrv.hrv(j, show=False)
#     print(result)
#
#     # try:
#     #     pyhrv.hrv(j, show=False)
#     # except Exception as e:
#     #     print(f"An error occurred with signal {i}: {e}")